// RAG docs chat: retrieve (Voyage embed -> Qdrant -> Voyage rerank) -> Gemini
// generation, streamed back as SSE. Reads keys from runtimeConfig (.env).
//
// Gemini has no document-Citations API (unlike Claude), so we number the
// retrieved chunks in the prompt, ask the model to cite [n], and map those
// markers back to the source list after generation.
import { GoogleGenAI } from "@google/genai";

const LANG_NAME = { en: "English", ja: "Japanese (日本語)", zh: "Chinese (中文)" };

export default defineEventHandler(async (event) => {
  const config = useRuntimeConfig();
  const body = await readBody(event);
  const messages = Array.isArray(body?.messages) ? body.messages : [];
  const lang = RAG_LANGS.includes(body?.lang) ? body.lang : "en";

  if (!config.geminiApiKey || !config.voyageApiKey) {
    throw createError({
      statusCode: 503,
      statusMessage: "RAG not configured. Set GEMINI_API_KEY and VOYAGE_API_KEY in .env.",
    });
  }

  const lastUser = [...messages].reverse().find((m) => m.role === "user");
  const query = String(lastUser?.content || "").slice(0, 2000).trim();
  if (!query) throw createError({ statusCode: 400, statusMessage: "Empty query" });

  // --- Retrieve (Voyage + Qdrant + Voyage rerank) ---
  let top = [];
  try {
    const vector = await embedQuery(query);
    const hits = await searchDocs(vector, lang, 20);
    top = await rerankDocs(query, hits, 6);
  } catch (e) {
    throw createError({ statusCode: 502, statusMessage: `Retrieval failed: ${e.message}` });
  }

  const sources = top.map((c) => ({ title: c.title, heading: c.heading, url: c.url }));
  const contextBlock = top
    .map((c, i) => {
      const label = c.heading && c.heading !== c.title ? `${c.title} — ${c.heading}` : c.title;
      return `[${i + 1}] ${label}\n${c.text}`;
    })
    .join("\n\n");

  const systemInstruction =
    `You are the LEAPS documentation assistant for an Ultra-Wideband RTLS product. ` +
    `Answer ONLY using the numbered documentation context provided in the user message. ` +
    `If the answer is not in the context, say you could not find it and point to the most ` +
    `relevant section. Be concise and technical; use code/identifiers verbatim. ` +
    `Cite the sources you used inline with their bracket numbers, e.g. [1], [2]. ` +
    `Respond in ${LANG_NAME[lang]}.`;

  // History (excluding the current question), mapped to Gemini roles.
  const history = messages
    .filter((m) => m.role === "user" || m.role === "assistant")
    .slice(-6);
  history.pop();
  const contents = history.map((m) => ({
    role: m.role === "assistant" ? "model" : "user",
    parts: [{ text: String(m.content) }],
  }));
  contents.push({
    role: "user",
    parts: [{ text: `Documentation context:\n\n${contextBlock}\n\n---\nQuestion: ${query}` }],
  });

  const ai = new GoogleGenAI({ apiKey: config.geminiApiKey });

  setResponseHeader(event, "content-type", "text/event-stream; charset=utf-8");
  setResponseHeader(event, "cache-control", "no-cache, no-transform");
  setResponseHeader(event, "x-accel-buffering", "no");

  const enc = new TextEncoder();
  return new ReadableStream({
    async start(controller) {
      const send = (obj) => controller.enqueue(enc.encode(`data: ${JSON.stringify(obj)}\n\n`));
      let full = "";
      try {
        const stream = await ai.models.generateContentStream({
          model: config.chatModel || "gemini-2.5-flash",
          contents,
          config: {
            systemInstruction,
            maxOutputTokens: 1024,
          },
        });
        for await (const chunk of stream) {
          const t = chunk.text;
          if (t) {
            full += t;
            send({ type: "text", text: t });
          }
        }
        // Map [n] citation markers back to the source list.
        const cited = new Set();
        for (const m of full.matchAll(/\[(\d+)\]/g)) {
          const idx = Number(m[1]) - 1;
          if (sources[idx]) cited.add(idx);
        }
        const used = [...cited].map((i) => sources[i]);
        send({ type: "sources", sources: used.length ? used : sources.slice(0, 3) });
        controller.enqueue(enc.encode("data: [DONE]\n\n"));
      } catch (e) {
        send({ type: "error", error: e?.message || "generation failed" });
      } finally {
        controller.close();
      }
    },
  });
});
