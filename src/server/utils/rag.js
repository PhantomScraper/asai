// Server-side RAG helpers: Voyage embeddings + reranking, Qdrant search.
// Keys come from runtimeConfig (.env). See nuxt.config.ts runtimeConfig.
export const RAG_COLLECTION = "leaps_docs";
export const RAG_LANGS = ["en", "ja", "zh"];

export async function embedQuery(text) {
  const { voyageApiKey } = useRuntimeConfig();
  const res = await $fetch("https://api.voyageai.com/v1/embeddings", {
    method: "POST",
    headers: { authorization: `Bearer ${voyageApiKey}` },
    body: { input: [text], model: "voyage-3", input_type: "query" },
  });
  return res.data[0].embedding;
}

export async function searchDocs(vector, lang, limit = 20) {
  const { qdrantUrl, qdrantApiKey } = useRuntimeConfig();
  const res = await $fetch(
    `${qdrantUrl.replace(/\/+$/, "")}/collections/${RAG_COLLECTION}/points/search`,
    {
      method: "POST",
      headers: qdrantApiKey ? { "api-key": qdrantApiKey } : {},
      body: {
        vector,
        limit,
        with_payload: true,
        filter: { must: [{ key: "lang", match: { value: lang } }] },
      },
    }
  );
  return (res.result || []).map((h) => ({
    text: h.payload.text,
    title: h.payload.title,
    heading: h.payload.heading,
    url: h.payload.url,
    slug: h.payload.slug,
    score: h.score,
  }));
}

export async function rerankDocs(query, candidates, topK = 6) {
  if (!candidates.length) return [];
  const { voyageApiKey } = useRuntimeConfig();
  const res = await $fetch("https://api.voyageai.com/v1/rerank", {
    method: "POST",
    headers: { authorization: `Bearer ${voyageApiKey}` },
    body: {
      query,
      documents: candidates.map((c) => c.text),
      model: "rerank-2",
      top_k: Math.min(topK, candidates.length),
    },
  });
  return res.data.map((r) => ({ ...candidates[r.index], score: r.relevance_score }));
}
