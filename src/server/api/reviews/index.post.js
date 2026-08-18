import { randomUUID } from "node:crypto";

const MAX = { page: 300, selector: 1000, snippet: 200, comment: 4000, author: 80 };

export default defineEventHandler(async (event) => {
  requireReviewCode(event);
  const body = await readBody(event);
  const comment = String(body?.comment || "").trim().slice(0, MAX.comment);
  if (!comment) throw createError({ statusCode: 400, statusMessage: "Empty comment" });

  const review = {
    id: `rv_${randomUUID()}`,
    page: String(body?.page || "/").slice(0, MAX.page),
    selector: String(body?.selector || "").slice(0, MAX.selector),
    snippet: String(body?.snippet || "").trim().slice(0, MAX.snippet),
    comment,
    author: String(body?.author || "").trim().slice(0, MAX.author) || "Anonymous",
    resolved: false,
    createdAt: new Date().toISOString(),
  };
  await saveReview(review);
  return { review };
});
