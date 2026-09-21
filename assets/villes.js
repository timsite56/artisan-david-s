/* ──────────────────────────────────────────────────────────────
   Artisan David S — accordéons du menu mobile et barre d'appel.
   Chargé par toutes les pages, accueil compris.
   ────────────────────────────────────────────────────────────── */
(function () {
  'use strict';

  var TEL1 = { nom: 'Noé', tel: '+33604417382', aff: '06 04 41 73 82' };
  var TEL2 = { nom: 'David', tel: '+33786821293', aff: '07 86 82 12 93' };

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

  /* Barre d'appel mobile : les deux numéros + devis */
  document.addEventListener('DOMContentLoaded', function () {
    if (document.querySelector('.callbar')) return;
    var devis = document.getElementById('devis') ? '#devis' : 'index.html#devis';
    var bar = document.createElement('div');
    bar.className = 'callbar';
    bar.innerHTML =
      '<a class="cb-1" href="tel:' + TEL1.tel + '">📞 Appeler<small>' + TEL1.aff + '</small></a>' +
      '<a class="cb-2" href="tel:' + TEL2.tel + '">📞 2ᵉ numéro<small>' + TEL2.aff + '</small></a>' +
      '<a class="cb-3" href="' + devis + '">Devis<small>gratuit</small></a>';
    document.body.appendChild(bar);
  });
})();
