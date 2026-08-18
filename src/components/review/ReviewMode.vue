<template>
  <div v-if="active" class="rvw" data-review-ui>
    <!-- Hover highlight while picking an element -->
    <div
      v-if="commenting && hoverRect && !composer && !detail"
      class="rvw-highlight"
      :style="rectStyle(hoverRect)"
    ></div>

    <!-- Flash highlight when jumping to a comment from the sidebar -->
    <div v-if="flashRect" class="rvw-highlight rvw-highlight--flash" :style="rectStyle(flashRect)"></div>

    <!-- Numbered pins on commented elements -->
    <button
      v-for="pin in pins"
      :key="pin.review.id"
      class="rvw-pin"
      :class="{ 'rvw-pin--resolved': pin.review.resolved }"
      :style="{ left: pin.x + 'px', top: pin.y + 'px' }"
      :title="pin.review.comment"
      @click.stop="openDetail(pin)"
    >
      {{ pin.n }}
    </button>

    <!-- Composer popover -->
    <div v-if="composer" class="rvw-pop" :style="{ left: composer.x + 'px', top: composer.y + 'px' }">
      <blockquote v-if="composer.snippet" class="rvw-pop__snippet">{{ composer.snippet }}</blockquote>
      <input v-model="authorName" class="rvw-input" type="text" placeholder="Your name" maxlength="80" />
      <textarea
        ref="composerText"
        v-model="composer.text"
        class="rvw-input rvw-textarea"
        rows="3"
        placeholder="Write a comment…"
        maxlength="4000"
        @keydown.meta.enter.prevent="saveComment"
        @keydown.ctrl.enter.prevent="saveComment"
      ></textarea>
      <div class="rvw-pop__actions">
        <button class="rvw-btn" @click="closePopovers">Cancel</button>
        <button class="rvw-btn rvw-btn--primary" :disabled="!composer.text.trim() || saving" @click="saveComment">
          {{ saving ? "Saving…" : "Comment" }}
        </button>
      </div>
    </div>

    <!-- Detail popover (opened from a pin) -->
    <div v-if="detail" class="rvw-pop" :style="{ left: detail.x + 'px', top: detail.y + 'px' }">
      <div class="rvw-pop__meta">
        <strong>{{ detail.review.author }}</strong>
        <span>{{ formatDate(detail.review.createdAt) }}</span>
        <span v-if="detail.review.resolved" class="rvw-chip rvw-chip--resolved">Resolved</span>
      </div>
      <blockquote v-if="detail.review.snippet" class="rvw-pop__snippet">{{ detail.review.snippet }}</blockquote>
      <p class="rvw-pop__comment">{{ detail.review.comment }}</p>
      <div class="rvw-pop__actions">
        <button class="rvw-btn rvw-btn--danger" @click="removeReview(detail.review)">Delete</button>
        <button class="rvw-btn rvw-btn--primary" @click="toggleResolved(detail.review)">
          {{ detail.review.resolved ? "Reopen" : "Resolve" }}
        </button>
      </div>
    </div>

    <!-- Sidebar with every comment across pages -->
    <aside v-if="sidebarOpen" class="rvw-side">
      <header class="rvw-side__head">
        <strong>Comments</strong>
        <span class="rvw-chip">{{ openCount }} open</span>
        <div class="rvw-side__head-actions">
          <button class="rvw-btn rvw-btn--sm" :disabled="!reviews.length" @click="exportMarkdown">Export</button>
          <button class="rvw-btn rvw-btn--sm" aria-label="Close" @click="sidebarOpen = false">✕</button>
        </div>
      </header>
      <label class="rvw-side__filter">
        <input v-model="hideResolved" type="checkbox" />
        Hide resolved
      </label>
      <div class="rvw-side__list">
        <p v-if="!reviews.length" class="rvw-side__empty">
          No comments yet. With comment mode on, click any element on the page.
        </p>
        <section v-for="g in visibleGroups" :key="g.page">
          <h4 class="rvw-side__page">
            {{ g.page }} <em v-if="g.page === route.path">— this page</em>
          </h4>
          <article
            v-for="r in g.items"
            :key="r.id"
            class="rvw-card"
            :class="{ 'rvw-card--resolved': r.resolved }"
            @click="goToReview(r)"
          >
            <div class="rvw-card__meta">
              <span class="rvw-card__dot" :class="{ 'rvw-card__dot--resolved': r.resolved }"></span>
              <strong>{{ r.author }}</strong>
              <span class="rvw-card__date">{{ formatDate(r.createdAt) }}</span>
            </div>
            <blockquote v-if="r.snippet" class="rvw-card__snippet">{{ r.snippet }}</blockquote>
            <p class="rvw-card__comment">{{ r.comment }}</p>
            <p v-if="r.page === route.path && missingIds.has(r.id)" class="rvw-card__missing">
              ⚠ Element no longer found on this page
            </p>
            <div class="rvw-card__actions">
              <button class="rvw-btn rvw-btn--sm" @click.stop="toggleResolved(r)">
                {{ r.resolved ? "Reopen" : "Resolve" }}
              </button>
              <button class="rvw-btn rvw-btn--sm rvw-btn--danger" @click.stop="removeReview(r)">Delete</button>
            </div>
          </article>
        </section>
      </div>
    </aside>

    <!-- First-run hint -->
    <div v-if="hintVisible" class="rvw-hint">Click any element on the page to leave a comment</div>

    <!-- Floating toolbar -->
    <div class="rvw-bar">
      <button class="rvw-bar__btn" :class="{ 'rvw-bar__btn--on': commenting }" @click="toggleCommenting">
        <span class="rvw-bar__dot"></span>
        Comment mode
      </button>
      <button class="rvw-bar__btn" :class="{ 'rvw-bar__btn--on': sidebarOpen }" @click="sidebarOpen = !sidebarOpen">
        Comments
        <span class="rvw-bar__count">{{ reviews.length }}</span>
      </button>
      <button class="rvw-bar__btn rvw-bar__btn--exit" @click="exitReview">Exit review</button>
    </div>
  </div>
</template>

<script setup>
import { computed, nextTick, onBeforeUnmount, onMounted, ref, watch } from "vue";

const route = useRoute();
const router = useRouter();

const active = ref(false);
const commenting = ref(true);
const sidebarOpen = ref(false);
const hideResolved = ref(false);
const reviews = ref([]);
const pins = ref([]);
const missingIds = ref(new Set());
const hoverRect = ref(null);
const flashRect = ref(null);
const composer = ref(null); // { x, y, selector, snippet, text }
const detail = ref(null); // { x, y, review }
const composerText = ref(null);
const authorName = ref("");
const saving = ref(false);

let code = "";
let timer = null;
let ticking = false;

const byCreated = (a, b) => a.createdAt.localeCompare(b.createdAt);
const openCount = computed(() => reviews.value.filter((r) => !r.resolved).length);

const groups = computed(() => {
  const byPage = new Map();
  for (const r of [...reviews.value].sort(byCreated)) {
    if (!byPage.has(r.page)) byPage.set(r.page, []);
    byPage.get(r.page).push(r);
  }
  return [...byPage.entries()]
    .sort(([a], [b]) => (a === route.path ? -1 : b === route.path ? 1 : a.localeCompare(b)))
    .map(([page, items]) => ({ page, items }));
});

const visibleGroups = computed(() =>
  groups.value
    .map((g) => ({ ...g, items: hideResolved.value ? g.items.filter((r) => !r.resolved) : g.items }))
    .filter((g) => g.items.length)
);

const hintVisible = computed(
  () =>
    commenting.value &&
    !composer.value &&
    !detail.value &&
    !reviews.value.some((r) => r.page === route.path)
);

// --- Activation --------------------------------------------------------

onMounted(() => {
  const q = route.query.review;
  if (q != null && q !== "") {
    code = String(q);
    sessionStorage.setItem("leaps-review-code", code);
  } else {
    code = sessionStorage.getItem("leaps-review-code") || "";
  }
  if (!code) return;

  active.value = true;
  authorName.value = localStorage.getItem("leaps-reviewer-name") || "";
  attachListeners();
  fetchReviews();
  // Re-resolve selectors periodically: doc pages render content async.
  timer = setInterval(refreshPins, 1500);
});

onBeforeUnmount(() => {
  detachListeners();
  if (timer) clearInterval(timer);
  document.documentElement.classList.remove("rvw-crosshair");
});

function exitReview() {
  sessionStorage.removeItem("leaps-review-code");
  active.value = false;
  detachListeners();
  if (timer) clearInterval(timer);
  document.documentElement.classList.remove("rvw-crosshair");
  if (route.query.review != null) {
    const query = { ...route.query };
    delete query.review;
    router.replace({ query });
  }
}

watch(
  [active, commenting],
  ([a, c]) => {
    if (typeof document !== "undefined") {
      document.documentElement.classList.toggle("rvw-crosshair", a && c);
    }
  },
  { immediate: true }
);

watch(
  () => route.path,
  () => {
    closePopovers();
    hoverRect.value = null;
    setTimeout(refreshPins, 400);
  }
);

// --- API ---------------------------------------------------------------

const apiHeaders = () => ({ "x-review-code": code });

async function fetchReviews() {
  try {
    const data = await $fetch("/api/reviews", { headers: apiHeaders() });
    reviews.value = data.reviews;
    await nextTick();
    refreshPins();
  } catch (err) {
    if (err?.statusCode === 401) {
      alert("Invalid review link. Please ask for a new one.");
      exitReview();
    }
  }
}

async function saveComment() {
  const text = composer.value?.text?.trim();
  if (!text || saving.value) return;
  saving.value = true;
  try {
    const name = authorName.value.trim() || "Anonymous";
    localStorage.setItem("leaps-reviewer-name", name);
    const { review } = await $fetch("/api/reviews", {
      method: "POST",
      headers: apiHeaders(),
      body: {
        page: route.path,
        selector: composer.value.selector,
        snippet: composer.value.snippet,
        comment: text,
        author: name,
      },
    });
    reviews.value.push(review);
    composer.value = null;
    refreshPins();
  } catch {
    alert("Could not save the comment. Please try again.");
  } finally {
    saving.value = false;
  }
}

async function toggleResolved(r) {
  try {
    const { review } = await $fetch(`/api/reviews/${r.id}`, {
      method: "PATCH",
      headers: apiHeaders(),
      body: { resolved: !r.resolved },
    });
    Object.assign(r, review);
    refreshPins();
  } catch {
    alert("Could not update the comment. Please try again.");
  }
}

async function removeReview(r) {
  if (!confirm("Delete this comment?")) return;
  try {
    await $fetch(`/api/reviews/${r.id}`, { method: "DELETE", headers: apiHeaders() });
    reviews.value = reviews.value.filter((x) => x.id !== r.id);
    detail.value = null;
    refreshPins();
  } catch {
    alert("Could not delete the comment. Please try again.");
  }
}

// --- Element picking ---------------------------------------------------

function attachListeners() {
  document.addEventListener("mousemove", onMouseMove, true);
  document.addEventListener("click", onDocClick, true);
  window.addEventListener("keydown", onKeydown);
  window.addEventListener("scroll", onScrollOrResize, { passive: true, capture: true });
  window.addEventListener("resize", onScrollOrResize);
}

function detachListeners() {
  document.removeEventListener("mousemove", onMouseMove, true);
  document.removeEventListener("click", onDocClick, true);
  window.removeEventListener("keydown", onKeydown);
  window.removeEventListener("scroll", onScrollOrResize, { capture: true });
  window.removeEventListener("resize", onScrollOrResize);
}

function targetEl(e) {
  const el = e.target;
  if (!(el instanceof Element)) return null;
  if (el.closest("[data-review-ui]")) return null;
  if (el === document.body || el === document.documentElement) return null;
  return el;
}

function onMouseMove(e) {
  if (!active.value || !commenting.value || composer.value || detail.value) {
    hoverRect.value = null;
    return;
  }
  const el = targetEl(e);
  hoverRect.value = el ? el.getBoundingClientRect() : null;
}

function onDocClick(e) {
  if (!active.value) return;
  const inUi = e.target instanceof Element && e.target.closest("[data-review-ui]");
  if (composer.value || detail.value) {
    // Click outside an open popover closes it and is swallowed.
    if (!inUi) {
      e.preventDefault();
      e.stopPropagation();
      closePopovers();
    }
    return;
  }
  if (!commenting.value || inUi) return;
  const el = targetEl(e);
  if (!el) return;
  e.preventDefault();
  e.stopPropagation();
  openComposer(el);
}

function onKeydown(e) {
  if (e.key === "Escape") closePopovers();
}

function closePopovers() {
  composer.value = null;
  detail.value = null;
}

function openComposer(el) {
  const rect = el.getBoundingClientRect();
  composer.value = {
    ...placePopover(rect),
    selector: cssPath(el),
    snippet: (el.innerText || "").trim().replace(/\s+/g, " ").slice(0, 120),
    text: "",
  };
  hoverRect.value = null;
  nextTick(() => composerText.value?.focus());
}

function openDetail(pin) {
  composer.value = null;
  detail.value = { ...placePopover(pin.rect), review: pin.review };
}

function toggleCommenting() {
  commenting.value = !commenting.value;
  if (!commenting.value) hoverRect.value = null;
}

// Stable-ish CSS path: nearest ancestor id, else tag:nth-of-type chain.
function cssPath(el) {
  const parts = [];
  let node = el;
  while (node && node.nodeType === 1 && node.tagName !== "HTML" && node.tagName !== "BODY") {
    if (node.id) {
      parts.unshift(`#${CSS.escape(node.id)}`);
      return parts.join(" > ");
    }
    let sel = node.tagName.toLowerCase();
    const parent = node.parentElement;
    if (parent) {
      const sibs = Array.from(parent.children).filter((c) => c.tagName === node.tagName);
      if (sibs.length > 1) sel += `:nth-of-type(${sibs.indexOf(node) + 1})`;
    }
    parts.unshift(sel);
    node = parent;
  }
  parts.unshift("body");
  return parts.join(" > ");
}

// --- Pins --------------------------------------------------------------

function refreshPins() {
  if (!active.value) {
    pins.value = [];
    return;
  }
  const out = [];
  const missing = new Set();
  const pageReviews = reviews.value.filter((r) => r.page === route.path).sort(byCreated);
  pageReviews.forEach((r, i) => {
    let el = null;
    try {
      el = r.selector ? document.querySelector(r.selector) : null;
    } catch {}
    const rect = el?.getBoundingClientRect();
    if (!rect || (rect.width === 0 && rect.height === 0)) {
      missing.add(r.id);
      return;
    }
    out.push({
      review: r,
      n: i + 1,
      rect,
      x: Math.min(Math.max(8, rect.right - 14), window.innerWidth - 36),
      y: rect.top - 14,
    });
  });
  pins.value = out;
  missingIds.value = missing;
}

function onScrollOrResize() {
  if (ticking) return;
  ticking = true;
  requestAnimationFrame(() => {
    ticking = false;
    refreshPins();
  });
}

// --- Sidebar navigation --------------------------------------------------

async function goToReview(r) {
  if (r.page !== route.path) {
    await navigateTo(r.page);
    setTimeout(() => flashReview(r), 600);
  } else {
    flashReview(r);
  }
}

function flashReview(r) {
  let el = null;
  try {
    el = r.selector ? document.querySelector(r.selector) : null;
  } catch {}
  if (!el) return;
  el.scrollIntoView({ behavior: "smooth", block: "center" });
  setTimeout(() => {
    flashRect.value = el.getBoundingClientRect();
    setTimeout(() => (flashRect.value = null), 1600);
  }, 450);
}

// --- Export --------------------------------------------------------------

function exportMarkdown() {
  const lines = [
    `# Content review — ${location.host}`,
    `_Exported ${new Date().toLocaleString()}_`,
    "",
  ];
  for (const g of groups.value) {
    lines.push(`## Page: ${g.page}`, "");
    g.items.forEach((r, i) => {
      lines.push(
        `### ${i + 1}. ${r.resolved ? "✅ Resolved" : "🔴 Open"} — ${r.author} (${formatDate(r.createdAt)})`
      );
      if (r.snippet) lines.push(`> ${r.snippet}`);
      lines.push("", r.comment, "");
    });
  }
  const blob = new Blob([lines.join("\n")], { type: "text/markdown" });
  const a = document.createElement("a");
  a.href = URL.createObjectURL(blob);
  a.download = `leaps-review-${new Date().toISOString().slice(0, 10)}.md`;
  a.click();
  URL.revokeObjectURL(a.href);
}

// --- Helpers -------------------------------------------------------------

function rectStyle(rect) {
  return {
    left: rect.left - 3 + "px",
    top: rect.top - 3 + "px",
    width: rect.width + 6 + "px",
    height: rect.height + 6 + "px",
  };
}

function placePopover(rect) {
  const W = 320;
  const H = 250;
  const vw = window.innerWidth;
  const vh = window.innerHeight;
  const x = Math.min(Math.max(8, rect.left), Math.max(8, vw - W - 8));
  let y = rect.bottom + 10;
  if (y + H > vh - 8) y = Math.max(8, rect.top - H - 10);
  return { x, y };
}

function formatDate(iso) {
  return new Date(iso).toLocaleString(undefined, {
    day: "2-digit",
    month: "short",
    hour: "2-digit",
    minute: "2-digit",
  });
}
</script>

<style>
/* Unscoped on purpose (rvw- prefix avoids collisions): the crosshair rule
   below must target page elements outside this component. */
html.rvw-crosshair body :not([data-review-ui]):not([data-review-ui] *) {
  cursor: crosshair !important;
}

.rvw {
  font-family: var(--font-body, system-ui, sans-serif);
  font-size: 14px;
  line-height: 1.45;
  color: var(--color-text, #1e1e1e);
}

.rvw-highlight {
  position: fixed;
  z-index: 2147483000;
  pointer-events: none;
  border: 2px solid var(--color-primary, #be1d2f);
  border-radius: 4px;
  background: var(--tint-brand-soft, rgba(190, 29, 47, 0.07));
}

.rvw-highlight--flash {
  animation: rvw-flash 1.6s ease-out forwards;
}

@keyframes rvw-flash {
  0%, 60% { opacity: 1; }
  100% { opacity: 0; }
}

.rvw-pin {
  position: fixed;
  z-index: 2147483200;
  width: 28px;
  height: 28px;
  border-radius: 50% 50% 50% 4px;
  border: 2px solid #fff;
  background: var(--color-primary, #be1d2f);
  color: #fff;
  font-weight: 700;
  font-size: 13px;
  font-family: var(--font-display, sans-serif);
  cursor: pointer !important;
  box-shadow: 0 2px 10px rgba(30, 30, 30, 0.35);
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 0;
  transition: transform 0.15s ease;
}

.rvw-pin:hover {
  transform: scale(1.15);
}

.rvw-pin--resolved {
  background: #6c757d;
  opacity: 0.85;
}

.rvw-pop {
  position: fixed;
  z-index: 2147483400;
  width: 320px;
  max-width: calc(100vw - 16px);
  background: #fff;
  border-radius: var(--radius-md, 12px);
  box-shadow: var(--shadow-lg, 0 12px 40px rgba(30, 30, 30, 0.25));
  border: 1px solid var(--color-border, #e0e0e0);
  padding: 12px;
  display: flex;
  flex-direction: column;
  gap: 8px;
}

.rvw-pop__snippet,
.rvw-card__snippet {
  margin: 0;
  padding: 6px 10px;
  border-left: 3px solid var(--color-primary, #be1d2f);
  background: var(--tint-brand-faint, rgba(190, 29, 47, 0.04));
  color: var(--color-text-muted, #555c66);
  font-style: italic;
  font-size: 12.5px;
  border-radius: 0 6px 6px 0;
  overflow: hidden;
  display: -webkit-box;
  -webkit-line-clamp: 3;
  -webkit-box-orient: vertical;
}

.rvw-pop__meta {
  display: flex;
  align-items: center;
  gap: 8px;
}

.rvw-pop__meta span {
  color: var(--color-text-light, #8b919a);
  font-size: 12px;
}

.rvw-pop__comment {
  margin: 0;
  white-space: pre-wrap;
  word-break: break-word;
  max-height: 40vh;
  overflow-y: auto;
}

.rvw-pop__actions {
  display: flex;
  justify-content: flex-end;
  gap: 8px;
}

.rvw-input {
  width: 100%;
  border: 1px solid var(--color-border, #e0e0e0);
  border-radius: 8px;
  padding: 8px 10px;
  font: inherit;
  color: inherit;
  background: #fff;
  outline: none;
}

.rvw-input:focus {
  border-color: var(--color-primary, #be1d2f);
  box-shadow: 0 0 0 3px var(--tint-brand-soft, rgba(190, 29, 47, 0.07));
}

.rvw-textarea {
  resize: vertical;
  min-height: 64px;
}

.rvw-btn {
  border: 1px solid var(--color-border, #e0e0e0);
  background: #fff;
  color: var(--color-text, #1e1e1e);
  border-radius: var(--radius-pill, 100px);
  padding: 6px 14px;
  font: inherit;
  font-weight: 600;
  cursor: pointer !important;
  transition: background 0.15s ease, border-color 0.15s ease;
}

.rvw-btn:hover:not(:disabled) {
  background: var(--color-bg, #f5f5f5);
}

.rvw-btn:disabled {
  opacity: 0.5;
  cursor: default !important;
}

.rvw-btn--primary {
  background: var(--color-primary, #be1d2f);
  border-color: var(--color-primary, #be1d2f);
  color: #fff;
}

.rvw-btn--primary:hover:not(:disabled) {
  background: var(--color-primary-dark, #8f1523);
}

.rvw-btn--danger {
  color: var(--color-primary-dark, #8f1523);
}

.rvw-btn--sm {
  padding: 3px 10px;
  font-size: 12.5px;
}

.rvw-chip {
  background: var(--tint-brand, rgba(190, 29, 47, 0.14));
  color: var(--color-primary-dark, #8f1523);
  border-radius: var(--radius-pill, 100px);
  padding: 2px 10px;
  font-size: 12px;
  font-weight: 700;
}

.rvw-chip--resolved {
  background: #e8f0e9;
  color: #2e7d32;
}

/* Sidebar */
.rvw-side {
  position: fixed;
  z-index: 2147483300;
  top: 0;
  right: 0;
  bottom: 0;
  width: 360px;
  max-width: 92vw;
  background: #fff;
  border-left: 1px solid var(--color-border, #e0e0e0);
  box-shadow: -8px 0 40px rgba(30, 30, 30, 0.12);
  display: flex;
  flex-direction: column;
}

.rvw-side__head {
  display: flex;
  align-items: center;
  gap: 10px;
  padding: 14px 16px;
  border-bottom: 1px solid var(--color-border-light, #ededed);
  font-family: var(--font-display, sans-serif);
  font-size: 16px;
}

.rvw-side__head-actions {
  margin-left: auto;
  display: flex;
  gap: 6px;
}

.rvw-side__filter {
  display: flex;
  align-items: center;
  gap: 8px;
  padding: 10px 16px;
  border-bottom: 1px solid var(--color-border-light, #ededed);
  color: var(--color-text-muted, #555c66);
  font-size: 13px;
  cursor: pointer !important;
}

.rvw-side__list {
  overflow-y: auto;
  padding: 12px 16px 24px;
  flex: 1;
}

.rvw-side__empty {
  color: var(--color-text-muted, #555c66);
  padding: 24px 8px;
  text-align: center;
}

.rvw-side__page {
  margin: 14px 0 8px;
  font-family: var(--font-display, sans-serif);
  font-size: 13px;
  color: var(--color-text-muted, #555c66);
  word-break: break-all;
}

.rvw-side__page em {
  color: var(--color-primary, #be1d2f);
  font-style: normal;
  font-weight: 600;
}

.rvw-card {
  border: 1px solid var(--color-border, #e0e0e0);
  border-radius: var(--radius-md, 12px);
  padding: 10px 12px;
  margin-bottom: 10px;
  cursor: pointer !important;
  display: flex;
  flex-direction: column;
  gap: 6px;
  transition: border-color 0.15s ease, box-shadow 0.15s ease;
}

.rvw-card:hover {
  border-color: var(--color-primary-light, #d9475a);
  box-shadow: var(--shadow-sm, 0 1px 3px rgba(30, 30, 30, 0.06));
}

.rvw-card--resolved {
  opacity: 0.65;
}

.rvw-card__meta {
  display: flex;
  align-items: center;
  gap: 8px;
  font-size: 13px;
}

.rvw-card__dot {
  width: 8px;
  height: 8px;
  border-radius: 50%;
  background: var(--color-primary, #be1d2f);
  flex-shrink: 0;
}

.rvw-card__dot--resolved {
  background: #2e7d32;
}

.rvw-card__date {
  margin-left: auto;
  color: var(--color-text-light, #8b919a);
  font-size: 11.5px;
}

.rvw-card__comment {
  margin: 0;
  white-space: pre-wrap;
  word-break: break-word;
}

.rvw-card__missing {
  margin: 0;
  color: #b26a00;
  font-size: 12px;
}

.rvw-card__actions {
  display: flex;
  gap: 6px;
  justify-content: flex-end;
}

/* Toolbar */
.rvw-bar {
  position: fixed;
  z-index: 2147483500;
  bottom: 18px;
  left: 50%;
  transform: translateX(-50%);
  display: flex;
  align-items: center;
  gap: 4px;
  background: var(--color-gray-dark, #2e2e2e);
  border-radius: var(--radius-pill, 100px);
  padding: 6px;
  box-shadow: var(--shadow-lg, 0 12px 40px rgba(30, 30, 30, 0.3));
}

.rvw-bar__btn {
  display: flex;
  align-items: center;
  gap: 7px;
  border: none;
  background: transparent;
  color: #fff;
  font: inherit;
  font-weight: 600;
  font-size: 13.5px;
  padding: 8px 14px;
  border-radius: var(--radius-pill, 100px);
  cursor: pointer !important;
  white-space: nowrap;
  transition: background 0.15s ease;
}

.rvw-bar__btn:hover {
  background: rgba(255, 255, 255, 0.12);
}

.rvw-bar__btn--on {
  background: var(--color-primary, #be1d2f);
}

.rvw-bar__btn--on:hover {
  background: var(--color-primary-dark, #8f1523);
}

.rvw-bar__dot {
  width: 8px;
  height: 8px;
  border-radius: 50%;
  background: rgba(255, 255, 255, 0.45);
}

.rvw-bar__btn--on .rvw-bar__dot {
  background: #fff;
  box-shadow: 0 0 8px rgba(255, 255, 255, 0.8);
}

.rvw-bar__count {
  background: rgba(255, 255, 255, 0.18);
  border-radius: var(--radius-pill, 100px);
  padding: 1px 8px;
  font-size: 12px;
}

.rvw-bar__btn--exit {
  color: rgba(255, 255, 255, 0.75);
}

.rvw-hint {
  position: fixed;
  z-index: 2147483500;
  bottom: 74px;
  left: 50%;
  transform: translateX(-50%);
  background: #fff;
  color: var(--color-text, #1e1e1e);
  border: 1px solid var(--color-border, #e0e0e0);
  border-radius: var(--radius-pill, 100px);
  box-shadow: var(--shadow-md, 0 4px 20px rgba(30, 30, 30, 0.08));
  padding: 8px 18px;
  font-size: 13px;
  white-space: nowrap;
  max-width: 92vw;
  overflow: hidden;
  text-overflow: ellipsis;
}

@media (max-width: 640px) {
  .rvw-bar {
    max-width: calc(100vw - 12px);
  }

  .rvw-bar__btn {
    padding: 8px 10px;
    font-size: 12.5px;
  }
}
</style>
