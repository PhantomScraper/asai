import { computed } from "vue";
import { useI18n } from "@/i18n";

// Locale-aware internal docs links.
// Docs exist in en/ja/zh; other UI locales (e.g. cs) fall back to en.
export function useDocs() {
  const { locale } = useI18n();
  const docsLang = computed(() =>
    ["en", "ja", "zh"].includes(locale.value) ? locale.value : "en"
  );
  const docsLink = (slug = "") => {
    const s = String(slug).replace(/^\/+|\/+$/g, "");
    return s ? `/docs/${docsLang.value}/${s}` : `/docs/${docsLang.value}`;
  };
  return { docsLang, docsLink };
}
