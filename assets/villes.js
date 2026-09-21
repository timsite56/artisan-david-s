/* ──────────────────────────────────────────────────────────────
   Artisan David S — accordéons du menu mobile et barre d'appel.
   Chargé par toutes les pages, accueil compris.
   ────────────────────────────────────────────────────────────── */
(function () {
  'use strict';

  var TEL1 = { tel: '+33786821293', aff: '07 86 82 12 93' };

  /* Accordéons mobiles. Écoute en capture pour passer avant le handler
     qui referme le menu au clic sur un lien. */
  document.addEventListener('click', function (e) {
    if (window.innerWidth > 960) return;
    var t = e.target.closest ? e.target.closest('.nav-toggle') : null;
    if (!t) return;
    e.preventDefault();
    e.stopPropagation();
    var box = t.classList.contains('mega-head') ? t.closest('.mega-col') : t.parentNode;
    if (!box) return;
    var ouvert = box.classList.contains('open');
    Array.prototype.forEach.call(box.parentNode.children, function (el) { el.classList.remove('open'); });
    if (!ouvert) {
      box.classList.add('open');
      setTimeout(function () { box.scrollIntoView({ block: 'nearest', behavior: 'smooth' }); }, 60);
    }
  }, true);

  window.addEventListener('resize', function () {
    if (window.innerWidth > 960) {
      document.querySelectorAll('.has-sub.open, .has-mega.open, .mega-col.open').forEach(function (el) { el.classList.remove('open'); });
    }
  });

  /* Barre d'appel mobile : appeler + devis */
  document.addEventListener('DOMContentLoaded', function () {
    if (document.querySelector('.callbar')) return;
    var devis = document.getElementById('devis') ? '#devis' : 'index.html#devis';
    var bar = document.createElement('div');
    bar.className = 'callbar';
    bar.innerHTML =
      '<a class="cb-1" href="tel:' + TEL1.tel + '">📞 Appeler<small>' + TEL1.aff + '</small></a>' +
      '<a class="cb-3" href="' + devis + '">Devis<small>gratuit</small></a>';
    document.body.appendChild(bar);
  });
  /* Mobile : textes longs repliés derrière « Lire la suite ». Le texte
     reste dans la page (Google et le niveau de qualité Ads le lisent). */
  document.addEventListener('DOMContentLoaded', function () {
    if (window.innerWidth > 760 || !document.querySelector('.page-hero')) return;
    document.querySelectorAll('.prose, .local-box').forEach(function (el) {
      if (el.scrollHeight < 260) return;
      el.classList.add('replie');
      var b = document.createElement('button');
      b.type = 'button';
      b.className = 'lire-suite';
      b.textContent = 'Lire la suite';
      b.addEventListener('click', function () {
        var ouvert = el.classList.toggle('replie') === false;
        b.textContent = ouvert ? 'Réduire' : 'Lire la suite';
      });
      el.parentNode.insertBefore(b, el.nextSibling);
    });
  });
})();
