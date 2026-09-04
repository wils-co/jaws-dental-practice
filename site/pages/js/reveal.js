/* Smiles by Design — restrained scroll reveal.
   Consideration pages only; emergency/contact/treatment-risks stay static.

   Fail-safe by design: the hidden state is applied ONLY after this script
   runs (via the .js-reveal class on <html>), so if JS is blocked or errors
   the page renders fully visible. Never hide content in the base stylesheet.

   Budget: 20px travel, 620ms, one reveal per block, small stagger. Slow and
   rare reads expensive; everything sliding on every scroll reads cheap. */
(function () {
  "use strict";

  var reduce = window.matchMedia && window.matchMedia("(prefers-reduced-motion: reduce)");
  if (reduce && reduce.matches) return;          // honour the OS setting: do nothing at all
  if (!("IntersectionObserver" in window)) return; // old browser: leave content visible

  var SELECTORS = [
    ".home-sec-head",
    ".home-tx a",
    ".home-diff .home-diff-card, .home-diff a",
    ".home-edu-grid > *",
    ".home-about-grid > *",
    ".home-visit > *",
    ".home-band .wrap",
    ".treatment-section",
    ".compare-card",
    ".journey-step",
    ".care-callout-box",
    ".doctor-profile-card"
  ].join(",");

  var els = Array.prototype.slice.call(document.querySelectorAll(SELECTORS));
  if (!els.length) return;

  document.documentElement.classList.add("js-reveal");
  els.forEach(function (el) { el.classList.add("reveal"); });

  // Anything already in or above the viewport is shown immediately — a visitor
  // should never watch the top of the page fade in after it has already loaded.
  var vh = window.innerHeight || document.documentElement.clientHeight;
  els.forEach(function (el) {
    if (el.getBoundingClientRect().top < vh * 0.9) el.classList.add("is-in");
  });

  var delivered = false;
  var io = new IntersectionObserver(function (entries) {
    delivered = true;
    entries.forEach(function (entry) {
      if (!entry.isIntersecting) return;
      var el = entry.target;
      // stagger siblings gently so a row of cards arrives as a group, not a wave
      var sibs = el.parentNode ? Array.prototype.slice.call(el.parentNode.children) : [];
      var i = Math.min(sibs.indexOf(el), 5);
      el.style.transitionDelay = (i > 0 ? i * 70 : 0) + "ms";
      el.classList.add("is-in");
      io.unobserve(el);
    });
  }, { rootMargin: "0px 0px -8% 0px", threshold: 0.08 });

  els.forEach(function (el) { io.observe(el); });

  // Watchdog: if the observer never delivers (broken polyfill, odd embedding,
  // headless capture), drop the effect entirely rather than leave the page
  // blank. Reveal-on-scroll must never be the reason content is unreadable.
  // Track observer *delivery*, not element state: the immediate-reveal above
  // always leaves at least one .is-in, so checking for that would suppress
  // this fallback in exactly the case it exists to catch.
  setTimeout(function () {
    if (!delivered) document.documentElement.classList.remove("js-reveal");
  }, 2500);

  // Header gains a hairline shadow once you leave the hero.
  var header = document.querySelector(".site-header");
  if (header) {
    var onScroll = function () {
      header.classList.toggle("is-scrolled", window.scrollY > 24);
    };
    window.addEventListener("scroll", onScroll, { passive: true });
    onScroll();
  }
})();
