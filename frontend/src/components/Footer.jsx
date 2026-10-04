import Symbol from "./Symbol";
import { getLenis } from "../lib/scroll";

const toTop = () => {
  const l = getLenis();
  if (l) l.scrollTo(0, { duration: 1.6 });
  else window.scrollTo({ top: 0, behavior: "smooth" });
};

export default function Footer() {
  return (
    <footer data-testid="site-footer" className="relative overflow-hidden px-5 pb-10 pt-10 md:px-10">
      <div className="mx-auto max-w-[1400px]">
        <div className="flex flex-wrap items-center justify-between gap-4 border-t pt-8 text-sm" style={{ borderColor: "color-mix(in srgb, var(--ink) 20%, transparent)" }}>
          <p className="opacity-70">Cinco orillas · Una sola mesa · Alcoy (Alicante)</p>
          <button data-testid="footer-back-top-btn" onClick={toTop} className="rounded-full border-2 border-current px-4 py-2 font-bold transition-colors duration-300 hover:bg-[color:var(--ink)] hover:text-[color:var(--bg)]">
            Volver a la orilla ↑
          </button>
        </div>
        <p aria-hidden="true" className="font-display mt-10 flex items-center text-[22vw] leading-[0.8] text-accent">
          <Symbol className="mr-[0.02em] h-[0.74em] w-[0.74em]" sun="var(--accent)" sea="#F0285F" foam="var(--bg)" />
          RILLA
        </p>
        <p data-testid="fiction-disclaimer" className="mt-8 max-w-2xl text-xs leading-relaxed opacity-50">
          ORILLA es un restaurante ficticio creado para esta demostración. Los ingredientes y alérgenos son ejemplos sin verificar. Esta demostración no sirve para decidir qué puedes comer.
        </p>
      </div>
    </footer>
  );
}
