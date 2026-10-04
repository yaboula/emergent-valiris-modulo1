import { AnimatePresence, motion } from "framer-motion";
import { ThemedSection } from "../../lib/active";
import { CATEGORIES } from "../../data/menu";
import Character from "../Character";
import DishCard from "./DishCard";

const Head = ({ w, n }) => (
  <div className="mb-12 grid items-end gap-6 md:grid-cols-12">
    <div className="relative h-44 w-36 md:col-span-2 md:h-56 md:w-full">
      <Character src={w.char.img} alt={w.char.name} className="h-full w-full" testId={`carta-character-${w.id}`} />
    </div>
    <div className="md:col-span-7">
      <p className="kicker flex items-center gap-3">
        <span className="rounded-full bg-[color:var(--ink)] px-3 py-1 text-[color:var(--bg)]">Orilla {w.num}</span> {w.country}
      </p>
      <motion.h2 initial={{ opacity: 0, y: 40 }} whileInView={{ opacity: 1, y: 0 }} viewport={{ once: true }} transition={{ duration: 0.7, ease: [0.22, 1, 0.36, 1] }} className="font-display mt-4 text-[clamp(3rem,8vw,7rem)] leading-[0.85]" data-testid={`carta-world-title-${w.id}`}>
        {w.title}
      </motion.h2>
    </div>
    <p className="max-w-sm text-base font-medium leading-relaxed opacity-85 md:col-span-3">
      «{w.char.quote}» <span className="mt-2 block text-sm font-bold opacity-80">{n} platos en esta orilla</span>
    </p>
  </div>
);

export default function WorldGroup({ w, items, onOpen }) {
  const cats = CATEGORIES.filter((c) => items.some((d) => d.cat === c.id));
  return (
    <ThemedSection id={`carta-${w.id}`} theme={w.theme} className="relative py-20 md:py-24">
      <div className="mx-auto max-w-[1400px] px-5 md:px-10">
        <Head w={w} n={items.length} />
        {cats.map((c) => (
          <div key={c.id} className="mb-12 last:mb-0" data-testid={`carta-cat-${w.id}-${c.id}`}>
            <div className="mb-5 flex items-center gap-4">
              <h3 className="font-display text-2xl md:text-3xl">{c.label}</h3>
              <span className="h-[2px] flex-1 rounded-full bg-current opacity-25" />
            </div>
            <motion.div layout className="grid gap-5 md:grid-cols-2 xl:grid-cols-3">
              <AnimatePresence mode="popLayout">
                {items.filter((d) => d.cat === c.id).map((d) => <DishCard key={d.id} d={d} w={w} onOpen={onOpen} />)}
              </AnimatePresence>
            </motion.div>
          </div>
        ))}
      </div>
    </ThemedSection>
  );
}
