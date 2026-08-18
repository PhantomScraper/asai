export default defineEventHandler(async (event) => {
  requireReviewCode(event);
  const review = await getReview(getRouterParam(event, "id"));
  if (!review) throw createError({ statusCode: 404, statusMessage: "Review not found" });

  const body = await readBody(event);
  if (typeof body?.resolved === "boolean") review.resolved = body.resolved;
  if (typeof body?.comment === "string" && body.comment.trim()) {
    review.comment = body.comment.trim().slice(0, 4000);
  }
  await saveReview(review);
  return { review };
});
