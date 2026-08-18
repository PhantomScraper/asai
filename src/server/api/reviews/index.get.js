export default defineEventHandler(async (event) => {
  requireReviewCode(event);
  return { reviews: await listReviews() };
});
