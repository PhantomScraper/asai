export default defineEventHandler(async (event) => {
  requireReviewCode(event);
  await deleteReview(getRouterParam(event, "id"));
  return { ok: true };
});
