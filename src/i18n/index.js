// Lightweight i18n, SSR-safe for Nuxt.
// Locale lives in useState (per-request on the server, reactive on the client)
// and is persisted to a cookie so server render and client hydration agree.
import { computed } from "vue";
import { useState, useCookie } from "#imports";
import en from "./locales/en.js";
import cs from "./locales/cs.js";
import ja from "./locales/ja.js";
import zh from "./locales/zh.js";

const messages = { en, cs, ja, zh };

export const supportedLocales = [
  { code: "en", label: "English" },
  { code: "cs", label: "Čeština" },
  { code: "ja", label: "日本語" },
  { code: "zh", label: "中文" },
];

function getNested(obj, path) {
  return path.split(".").reduce((acc, key) => acc?.[key], obj);
}

export function useI18n() {
  const cookie = useCookie("leaps-locale", { default: () => "en", sameSite: "lax" });
  const locale = useState("locale", () => (messages[cookie.value] ? cookie.value : "en"));

  const t = (key, params) => {
    const loc = locale.value;
    let str = getNested(messages[loc], key) ?? getNested(messages.en, key) ?? key;
    if (params && typeof str === "string") {
      for (const [k, v] of Object.entries(params)) {
        str = str.replace(new RegExp(`\\{${k}\\}`, "g"), v);
      }
    }
    return str;
  };

  const tm = (key) => getNested(messages[locale.value], key) ?? getNested(messages.en, key);

  const setLocale = (code) => {
    if (messages[code]) {
      locale.value = code;
      cookie.value = code;
    }
  };

  const navLinks = computed(() => tm("nav.links") || []);

  return { locale, setLocale, t, tm, navLinks, supportedLocales };
}

export function getPageTitle(titleKey, localeCode = "en") {
  const loc = messages[localeCode] ? localeCode : "en";
  return getNested(messages[loc], titleKey) || "LEAPS";
}
