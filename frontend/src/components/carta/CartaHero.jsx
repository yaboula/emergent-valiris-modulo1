import { motion } from "framer-motion";
import { Info } from "lucide-react";
import { ThemedSection } from "../../lib/active";
import { WORLDS } from "../../data/worlds";
import { DISHES, FOOD_NOTICE } from "../../data/menu";

export const CARTA_THEME = { bg: "#FFF4E2", ink: "#14110C", accent: "#F0285F" };
const ease = [0.22, 1, 0.36, 1];
const WORD = "La carta".split("");

export default function CartaHero({ onPick }) {
  return (
    <ThemedSection id="carta-inicio" theme={CARTA_THEME} className="relative overflow-hidden pb-12 pt-32 md:pt-40">
      <div className="mx-auto max-w-[1400px] px-5 md:px-10">
        <motion.p initial={{ opacity: 0, y: 10 }} animate={{ opacity: 1, y: 0 }} className="kicker flex items-center gap-3">
          <span className="h-2 w-2 rounded-full bg-[#F0285F]" /> ORILLA · {DISHES.length} platos · 5 orillas
        </motion.p>
        <h1 data-testid="carta-hero-title" aria-label="La carta" className="font-display mt-3 overflow-hidden text-[clamp(4.5rem,17vw,16rem)] leading-[0.85]">
          {WORD.map((l, i) => (
            <motion.span key={i} initial={{ y: "105%" }} animate={{ y: 0 }} transition={{ duration: 0.9, ease, delay: 0.1 + i * 0.05 }} className={`inline-block ${l === " " ? "w-[0.25em]" : ""} ${i > 2 ? "text-[#F0285F]" : ""}`}>
              {l}
            </motion.span>
          ))}
        </h1>
        <div className="mt-8 grid items-end gap-8 md:grid-cols-12">
          <motion.div initial={{ opacity: 0, y: 20 }} animate={{ opacity: 1, y: 0 }} transition={{ delay: 0.6, duration: 0.7, ease }} className="md:col-span-5">
            <p className="font-display text-3xl leading-[0.95] md:text-4xl">Elige orilla, filtra lo que no te sienta bien y monta tu mesa.</p>
            <p className="mt-4 flex max-w-md gap-2 text-xs font-medium leading-relaxed opacity-70" data-testid="carta-food-notice">
              <Info className="h-4 w-4 shrink-0" /> ORILLA es ficticio. {FOOD_NOTICE}
            </p>
          </motion.div>
          <div className="flex gap-2 md:col-span-7 md:justify-end md:gap-4" data-testid="carta-hero-pickers">
            {WORLDS.map((w, i) => (
              <motion.button
                key={w.id}
                onClick={() => onPick(w.id)}
                data-testid={`carta-pick-${w.id}`}
                initial={{ y: 80, opacity: 0 }}
                animate={{ y: 0, opacity: 1 }}
                transition={{ type: "spring", stiffness: 160, damping: 14, delay: 0.5 + i * 0.08 }}
                whileHover={{ y: -14, rotate: i % 2 ? 4 : -4 }}
                whileTap={{ scale: 0.92 }}
                className="group flex flex-1 flex-col items-center md:flex-none"
              >
                <span className="flex aspect-[3/4] w-full items-end justify-center overflow-hidden rounded-[999px_999px_24px_24px] pt-3 md:w-28" style={{ background: w.theme.bg }}>
                  <img src={w.char.img} alt={w.char.name} className="drop h-[88%] object-contain transition-transform duration-500 group-hover:scale-110" />
                </span>
                <span className="mt-2 text-xs font-bold md:text-sm">{w.title.replace("El ", "")}</span>
              </motion.button>
            ))}
          </div>
        </div>
      </div>
    </ThemedSection>
  );
}
