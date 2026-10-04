let lenis = null;

export const setLenis = (l) => (lenis = l);

export const scrollToId = (id) => {
  const el = document.getElementById(id);
  if (!el) return;
  if (lenis) lenis.scrollTo(el, { duration: 1.6 });
  else el.scrollIntoView({ behavior: "smooth" });
};
