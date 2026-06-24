<template>
  <div class="dchat">
    <button
      v-if="!open"
      class="dchat__fab"
      :aria-label="ui.title"
      @click="open = true"
    >
      <span aria-hidden="true">💬</span>
      <span class="dchat__fab-label">{{ ui.ask }}</span>
    </button>

    <div v-else class="dchat__panel" role="dialog" :aria-label="ui.title">
      <header class="dchat__header">
        <strong>{{ ui.title }}</strong>
        <button class="dchat__close" :aria-label="ui.close" @click="open = false">×</button>
      </header>

      <div ref="scroller" class="dchat__messages">
        <p v-if="!messages.length" class="dchat__hint">{{ ui.hint }}</p>
        <div
          v-for="(m, i) in messages"
          :key="i"
          class="dchat__msg"
          :class="`dchat__msg--${m.role}`"
        >
          <div class="dchat__bubble">
            <span v-if="m.content">{{ m.content }}</span>
            <span v-else-if="m.role === 'assistant' && loading" class="dchat__typing">…</span>
            <ul v-if="m.sources && m.sources.length" class="dchat__sources">
              <li v-for="(s, j) in m.sources" :key="j">
                <NuxtLink :to="s.url" @click="open = false">{{ s.title }}{{ s.heading && s.heading !== s.title ? ` — ${s.heading}` : '' }}</NuxtLink>
              </li>
            </ul>
          </div>
        </div>
        <p v-if="error" class="dchat__error">{{ error }}</p>
      </div>

      <form class="dchat__form" @submit.prevent="send">
        <input
          v-model="input"
          type="text"
          :placeholder="ui.placeholder"
          :disabled="loading"
          aria-label="Question"
        />
        <button type="submit" class="btn btn-primary" :disabled="loading || !input.trim()">
          {{ loading ? '…' : ui.send }}
        </button>
      </form>
    </div>
  </div>
</template>

<script setup>
import { ref, reactive, computed, nextTick } from "vue";
import { useI18n } from "@/i18n";

const { locale } = useI18n();
const docsLang = computed(() => (["en", "ja", "zh"].includes(locale.value) ? locale.value : "en"));

const UI = {
  en: { title: "Ask the docs", ask: "Ask the docs", hint: "Ask anything about LEAPS RTLS, PANS PRO, UDK…", placeholder: "Type your question…", send: "Send", close: "Close" },
  cs: { title: "Zeptejte se dokumentace", ask: "Zeptat se", hint: "Zeptejte se na LEAPS RTLS, PANS PRO, UDK…", placeholder: "Napište dotaz…", send: "Odeslat", close: "Zavřít" },
  ja: { title: "ドキュメントに質問", ask: "質問する", hint: "LEAPS RTLS、PANS PRO、UDK などについて質問できます", placeholder: "質問を入力…", send: "送信", close: "閉じる" },
  zh: { title: "向文档提问", ask: "提问", hint: "可询问 LEAPS RTLS、PANS PRO、UDK 等", placeholder: "输入您的问题…", send: "发送", close: "关闭" },
};
const ui = computed(() => UI[locale.value] || UI.en);

const open = ref(false);
const input = ref("");
const loading = ref(false);
const error = ref("");
const messages = reactive([]);
const scroller = ref(null);

const scrollDown = async () => {
  await nextTick();
  if (scroller.value) scroller.value.scrollTop = scroller.value.scrollHeight;
};

async function send() {
  const q = input.value.trim();
  if (!q || loading.value) return;
  error.value = "";
  input.value = "";
  messages.push({ role: "user", content: q });
  const assistant = reactive({ role: "assistant", content: "", sources: [] });
  messages.push(assistant);
  loading.value = true;
  scrollDown();

  try {
    const res = await fetch("/api/chat", {
      method: "POST",
      headers: { "content-type": "application/json" },
      body: JSON.stringify({
        lang: docsLang.value,
        messages: messages
          .filter((m) => m.content || m.role === "user")
          .map((m) => ({ role: m.role, content: m.content })),
      }),
    });

    if (!res.ok || !res.body) {
      const txt = await res.text().catch(() => "");
      throw new Error(res.status === 503 ? "Chat is not configured yet (missing API keys)." : txt || `Error ${res.status}`);
    }

    const reader = res.body.getReader();
    const dec = new TextDecoder();
    let buf = "";
    while (true) {
      const { done, value } = await reader.read();
      if (done) break;
      buf += dec.decode(value, { stream: true });
      let nl;
      while ((nl = buf.indexOf("\n\n")) >= 0) {
        const line = buf.slice(0, nl).replace(/^data: ?/, "");
        buf = buf.slice(nl + 2);
        if (!line || line === "[DONE]") continue;
        let evt;
        try {
          evt = JSON.parse(line);
        } catch {
          continue;
        }
        if (evt.type === "text") assistant.content += evt.text;
        else if (evt.type === "sources") assistant.sources = evt.sources || [];
        else if (evt.type === "error") error.value = evt.error;
        scrollDown();
      }
    }
  } catch (e) {
    error.value = e.message || "Something went wrong.";
  } finally {
    loading.value = false;
    scrollDown();
  }
}
</script>

<style scoped>
.dchat__fab {
  position: fixed;
  bottom: 1.5rem;
  right: 1.5rem;
  z-index: 1500;
  display: inline-flex;
  align-items: center;
  gap: 0.5rem;
  padding: 0.75rem 1.1rem;
  border-radius: 999px;
  background: var(--color-primary, #b83232);
  color: #fff;
  font-weight: 600;
  font-size: 0.9rem;
  box-shadow: 0 8px 24px rgba(0, 0, 0, 0.18);
}
.dchat__panel {
  position: fixed;
  bottom: 1.5rem;
  right: 1.5rem;
  z-index: 1500;
  width: min(380px, calc(100vw - 2rem));
  height: min(560px, calc(100vh - 3rem));
  display: flex;
  flex-direction: column;
  background: #fff;
  border: 1px solid var(--color-border, #ddd);
  border-radius: var(--radius-lg, 14px);
  box-shadow: 0 16px 48px rgba(0, 0, 0, 0.22);
  overflow: hidden;
}
.dchat__header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 0.85rem 1rem;
  background: var(--color-primary, #b83232);
  color: #fff;
}
.dchat__close {
  font-size: 1.4rem;
  line-height: 1;
  color: #fff;
}
.dchat__messages {
  flex: 1;
  overflow-y: auto;
  padding: 1rem;
  display: flex;
  flex-direction: column;
  gap: 0.75rem;
}
.dchat__hint {
  color: var(--color-text-muted, #777);
  font-size: 0.875rem;
}
.dchat__msg {
  display: flex;
}
.dchat__msg--user {
  justify-content: flex-end;
}
.dchat__bubble {
  max-width: 85%;
  padding: 0.6rem 0.8rem;
  border-radius: 12px;
  font-size: 0.9rem;
  line-height: 1.5;
  white-space: pre-wrap;
}
.dchat__msg--user .dchat__bubble {
  background: var(--color-primary, #b83232);
  color: #fff;
}
.dchat__msg--assistant .dchat__bubble {
  background: var(--color-bg, #f4f4f4);
  color: var(--color-text, #222);
}
.dchat__sources {
  list-style: none;
  margin: 0.6rem 0 0;
  padding: 0.5rem 0 0;
  border-top: 1px solid var(--color-border-light, #e5e5e5);
  font-size: 0.8rem;
}
.dchat__sources li {
  margin: 0.2rem 0;
}
.dchat__sources a {
  color: var(--color-primary, #b83232);
}
.dchat__error {
  color: #b00020;
  font-size: 0.85rem;
}
.dchat__form {
  display: flex;
  gap: 0.5rem;
  padding: 0.75rem;
  border-top: 1px solid var(--color-border-light, #eee);
}
.dchat__form input {
  flex: 1;
  padding: 0.6rem 0.8rem;
  border: 1px solid var(--color-border, #ddd);
  border-radius: var(--radius-md, 8px);
  font-size: 0.9rem;
}
.dchat__form .btn {
  padding: 0.6rem 0.9rem;
}
</style>
