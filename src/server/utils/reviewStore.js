// Storage for content-review comments (see components/review/ReviewMode.vue).
//
// Two backends, picked by environment:
//  - Upstash Redis over REST when UPSTASH_REDIS_REST_URL/TOKEN (or Vercel KV's
//    KV_REST_API_URL/TOKEN) are set — required on Vercel, where the filesystem
//    is ephemeral.
//  - A local JSON file under .data/ otherwise (dev on this machine).
import { promises as fs } from "node:fs";
import { dirname, join } from "node:path";

const HASH_KEY = "leaps:reviews";
const FILE = join(process.cwd(), ".data", "reviews.json");

function upstash() {
  const url = process.env.UPSTASH_REDIS_REST_URL || process.env.KV_REST_API_URL;
  const token = process.env.UPSTASH_REDIS_REST_TOKEN || process.env.KV_REST_API_TOKEN;
  return url && token ? { url, token } : null;
}

async function redis(command) {
  const { url, token } = upstash();
  const res = await fetch(url, {
    method: "POST",
    headers: { Authorization: `Bearer ${token}`, "Content-Type": "application/json" },
    body: JSON.stringify(command),
  });
  if (!res.ok) {
    throw createError({ statusCode: 502, statusMessage: `Review store error (${res.status})` });
  }
  return (await res.json()).result;
}

// On Vercel the filesystem is ephemeral — without Redis, comments would be
// silently lost between invocations. Fail loudly instead.
function requireDurableStore() {
  if (process.env.VERCEL && !upstash()) {
    throw createError({
      statusCode: 503,
      statusMessage:
        "Review store not configured. Add the Upstash Redis integration (UPSTASH_REDIS_REST_URL/TOKEN) to this Vercel project.",
    });
  }
}

async function readFileStore() {
  requireDurableStore();
  try {
    return JSON.parse(await fs.readFile(FILE, "utf8"));
  } catch {
    return {};
  }
}

async function writeFileStore(map) {
  requireDurableStore();
  await fs.mkdir(dirname(FILE), { recursive: true });
  await fs.writeFile(FILE, JSON.stringify(map, null, 2));
}

export async function listReviews() {
  let map;
  if (upstash()) {
    // HGETALL over REST returns a flat [field, value, field, value, ...] array.
    const flat = (await redis(["HGETALL", HASH_KEY])) || [];
    map = {};
    for (let i = 0; i < flat.length; i += 2) map[flat[i]] = JSON.parse(flat[i + 1]);
  } else {
    map = await readFileStore();
  }
  return Object.values(map).sort((a, b) => a.createdAt.localeCompare(b.createdAt));
}

export async function getReview(id) {
  if (upstash()) {
    const raw = await redis(["HGET", HASH_KEY, id]);
    return raw ? JSON.parse(raw) : null;
  }
  return (await readFileStore())[id] || null;
}

export async function saveReview(review) {
  if (upstash()) {
    await redis(["HSET", HASH_KEY, review.id, JSON.stringify(review)]);
  } else {
    const map = await readFileStore();
    map[review.id] = review;
    await writeFileStore(map);
  }
  return review;
}

export async function deleteReview(id) {
  if (upstash()) {
    await redis(["HDEL", HASH_KEY, id]);
  } else {
    const map = await readFileStore();
    delete map[id];
    await writeFileStore(map);
  }
}

// Optional shared secret: set REVIEW_CODE on the server and hand the client a
// link like https://site/?review=<code>. Without the env var any code passes.
export function requireReviewCode(event) {
  const expected = process.env.REVIEW_CODE;
  if (!expected) return;
  if (getHeader(event, "x-review-code") !== expected) {
    throw createError({ statusCode: 401, statusMessage: "Invalid review code" });
  }
}
