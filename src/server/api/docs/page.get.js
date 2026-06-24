export default defineEventHandler(async (event) => {
  const { lang, slug } = getQuery(event);
  const page = await getDocPage(String(lang || "en"), String(slug || "index"));
  if (!page) {
    throw createError({ statusCode: 404, statusMessage: "Documentation page not found" });
  }
  return page;
});
