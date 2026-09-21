// Redirige l'ancienne adresse et le www vers le domaine principal.
export async function onRequest(ctx) {
  const url = new URL(ctx.request.url);
  if (url.hostname === 'artisan-david-s.pages.dev' || url.hostname === 'www.artisan-david-s.fr') {
    return Response.redirect('https://artisan-david-s.fr' + url.pathname + url.search, 301);
  }
  return ctx.next();
}
