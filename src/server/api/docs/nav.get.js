export default defineEventHandler(async (event) => {
  const { lang } = getQuery(event);
  return getDocsNav(String(lang || "en"));
});
