'use strict';

const navbar = document.querySelector('[data-navbar]');
const navTogglers = document.querySelectorAll('[data-nav-toggler]');
const overlay = document.querySelector('[data-overlay]');
const header = document.querySelector('[data-header]');

function setMenu(open) {
  if (!navbar || !overlay) return;
  navbar.classList.toggle('active', open);
  overlay.classList.toggle('active', open);
  document.body.classList.toggle('nav-active', open);
  document.querySelector('.nav-toggle')?.setAttribute('aria-expanded', String(open));
}

navTogglers.forEach((toggle) => toggle.addEventListener('click', () => setMenu(!navbar.classList.contains('active'))));
navbar?.querySelectorAll('a').forEach((link) => link.addEventListener('click', () => setMenu(false)));
navbar?.querySelectorAll('.nav-link').forEach((link) => {
  if (link.pathname === window.location.pathname) link.classList.add('is-active');
});
window.addEventListener('keydown', (event) => { if (event.key === 'Escape') setMenu(false); });
window.addEventListener('scroll', () => header?.classList.toggle('is-scrolled', window.scrollY > 12), { passive: true });
