import { useEffect, useRef, useState } from "react";
import { AnimatePresence, motion } from "framer-motion";
import { Search, SlidersHorizontal, X } from "lucide-react";
import { WORLDS } from "../../data/worlds";
import { ALLERGENS, CATEGORIES, DIETS } from "../../data/menu";
import { AllergenIcon } from "./Allergens";
import { useActive } from "../../lib/active";
import useMedia, { MOBILE } from "../../lib/useMedia";
import Sheet from "../Sheet";

const Chip = ({ on, onClick, children, testId, style }) => (
  <button
    type="button"
    data-testid={testId}
    onClick={onClick}
    style={on ? style : undefined}
    className={`flex shrink-0 items-center gap-2 rounded-full border-2 px-3.5 py-1.5 text-sm font-semibold transition-colors duration-300 ${on ? "border-[color:var(--ink)] bg-[color:var(--ink)] text-[color:var(--bg)]" : "border-[color:var(--ink)]/20 hover:border-[color:var(--ink)]"}`}
  >
    {children}
  </button>
);

const toggle = (arr, set, id) => set(arr.includes(id) ? arr.filter((x) => x !== id) : [...arr, id]);

const PanelBody = ({ f }) => (
  <div className="grid gap-6 md:grid-cols-12">
    <div className="md:col-span-4">
      <p className="kicker mb-3 opacity-70">Tipo de plato</p>
      <div className="flex flex-wrap gap-2">
        {CATEGORIES.map((c) => <Chip key={c.id} on={f.cats.includes(c.id)} onClick={() => toggle(f.cats, f.setCats, c.id)} testId={`filter-cat-${c.id}`}>{c.label}</Chip>)}
      </div>
      <p className="kicker mb-3 mt-5 opacity-70">Dieta (ejemplo)</p>
      <div className="flex flex-wrap gap-2">
        {DIETS.map((c) => <Chip key={c.id} on={f.diets.includes(c.id)} onClick={() => toggle(f.diets, f.setDiets, c.id)} testId={`filter-diet-${c.id}`}>{c.label}</Chip>)}
      </div>
    </div>
    <div className="md:col-span-8">
      <p className="kicker mb-3 opacity-70">Ocultar platos que declaran</p>
      <div className="flex flex-wrap gap-2">
        {ALLERGENS.map((a) => (
          <Chip key={a.id} on={f.exclude.includes(a.id)} onClick={() => toggle(f.exclude, f.setExclude, a.id)} testId={`filter-allergen-${a.id}`}>
            <AllergenIcon id={a.id} /> {a.label}
          </Chip>
        ))}
      </div>
      <p className="mt-3 text-xs font-medium opacity-70">Ocultar un plato no hace seguros a los demás: los alérgenos son ejemplos sin verificar.</p>
    </div>
  </div>
);

const DesktopPanel = ({ f }) => (
  <motion.div initial={{ height: 0, opacity: 0 }} animate={{ height: "auto", opacity: 1 }} exit={{ height: 0, opacity: 0 }} transition={{ duration: 0.35, ease: [0.22, 1, 0.36, 1] }} className="overflow-hidden" data-testid="filter-panel">
    <div className="pb-2 pt-5"><PanelBody f={f} /></div>
  </motion.div>
);

const MobilePanel = ({ f, open, onClose, count }) => (
  <Sheet open={open} onClose={onClose} testId="filter-sheet" style={{ "--ink": "#14110C", "--bg": "#FFFBF2" }}>
    <div className="flex items-center justify-between px-6 pb-3 pt-8">
      <p className="font-display text-3xl leading-none">Filtros</p>
      <button onClick={onClose} data-testid="filter-sheet-close" aria-label="Cerrar" className="grid h-10 w-10 place-items-center rounded-full bg-coal/5"><X className="h-5 w-5" /></button>
    </div>
    <div className="flex-1 overflow-y-auto px-6 pb-6" data-testid="filter-panel"><PanelBody f={f} /></div>
    <div className="flex items-center gap-3 border-t border-coal/10 px-6 py-4">
      <button onClick={f.reset} data-testid="filter-sheet-reset" className="px-2 text-sm font-bold underline">Limpiar</button>
      <button onClick={onClose} data-testid="filter-sheet-apply" className="flex-1 rounded-full bg-[#F0285F] py-3.5 font-bold text-white">Ver {count} platos</button>
    </div>
  </Sheet>
);

const WorldTabs = ({ f }) => {
  const { active } = useActive();
  const ref = useRef(null);
  useEffect(() => {
    const el = ref.current?.querySelector(`[data-testid="world-tab-${f.world}"]`);
    if (el) ref.current.scrollTo({ left: el.offsetLeft - 16, behavior: "smooth" });
  }, [f.world]);
  return (
    <div ref={ref} className="-mx-4 flex gap-2 overflow-x-auto px-4 pb-1 pt-3 [scrollbar-width:none] md:-mx-1 md:px-1" data-testid="world-tabs">
      <Chip on={f.world === "all"} onClick={() => f.setWorld("all")} testId="world-tab-all">Todas<span className="hidden sm:inline"> las orillas</span></Chip>
      {WORLDS.map((w) => (
        <Chip key={w.id} on={f.world === w.id} onClick={() => f.setWorld(f.world === w.id ? "all" : w.id)} testId={`world-tab-${w.id}`} style={{ background: w.theme.bg, color: w.theme.ink, borderColor: w.theme.bg }}>
          <span className={`h-2.5 w-2.5 rounded-full transition-transform duration-300 ${active === `carta-${w.id}` ? "scale-150" : ""}`} style={{ background: w.theme.bg, boxShadow: "0 0 0 2px currentColor" }} />
          {w.title.replace("El ", "")}
        </Chip>
      ))}
    </div>
  );
};

export default function FilterBar({ f, count }) {
  const [open, setOpen] = useState(false);
  const isMobile = useMedia(MOBILE);
  const n = f.cats.length + f.diets.length + f.exclude.length;
  return (
    <div className="sticky z-40 px-3 transition-[top] duration-300 md:px-4" style={{ top: "var(--nav-offset)" }} data-testid="filter-bar">
      <div className="glass mx-auto max-w-[1400px] overflow-hidden rounded-[28px] border px-4 py-3 text-ink md:px-5" style={{ borderColor: "color-mix(in srgb, var(--ink) 14%, transparent)" }}>
        <div className="flex items-center gap-2 md:gap-3">
          <label className="flex min-w-0 flex-1 items-center gap-2 rounded-full px-4 py-2.5" style={{ background: "color-mix(in srgb, var(--ink) 8%, transparent)" }}>
            <Search className="h-4 w-4 shrink-0 opacity-70" />
            <input value={f.q} onChange={(e) => f.setQ(e.target.value)} data-testid="filter-search-input" placeholder="Busca un plato…" className="w-full min-w-0 bg-transparent text-base font-medium outline-none placeholder:text-[color:var(--ink)] placeholder:opacity-50 md:text-sm" />
            {f.q && <button onClick={() => f.setQ("")} data-testid="filter-search-clear" aria-label="Borrar búsqueda"><X className="h-4 w-4" /></button>}
          </label>
          <button onClick={() => setOpen((o) => !o)} data-testid="filter-toggle-btn" aria-expanded={open} className="flex shrink-0 items-center gap-2 rounded-full bg-[color:var(--ink)] px-4 py-2.5 text-sm font-bold text-[color:var(--bg)]">
            <SlidersHorizontal className="h-4 w-4" /> <span className="hidden sm:inline">Filtros</span>
            {n > 0 && <span className="grid h-5 min-w-5 place-items-center rounded-full bg-[#FFD23F] px-1 text-[11px] text-coal">{n}</span>}
          </button>
          <span data-testid="filter-result-count" className="hidden whitespace-nowrap text-sm font-bold md:block">{count} platos</span>
          {(n > 0 || f.q || f.world !== "all") && (
            <button onClick={f.reset} data-testid="filter-reset-btn" className="hidden text-sm font-bold underline md:block">Limpiar</button>
          )}
        </div>
        <WorldTabs f={f} />
        {!isMobile && <AnimatePresence>{open && <DesktopPanel f={f} />}</AnimatePresence>}
      </div>
      {isMobile && <MobilePanel f={f} open={open} onClose={() => setOpen(false)} count={count} />}
    </div>
  );
}
