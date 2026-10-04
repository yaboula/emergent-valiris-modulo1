let lenis = null;

export const setLenis = (l) => (lenis = l);
export const getLenis = () => lenis;

export const scrollToId = (id, offset = 0) => {
  const el = document.getElementById(id);
  if (!el) return;
  if (lenis) lenis.scrollTo(el, { duration: 1.4, offset });
  else window.scrollTo({ top: el.getBoundingClientRect().top + window.scrollY + offset, behavior: "smooth" });
};
