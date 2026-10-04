import { AnimatePresence, motion } from "framer-motion";
import { Sailboat } from "lucide-react";
import { WORLDS } from "../data/worlds";
import { useActive } from "../lib/active";
import { scrollToId } from "../lib/scroll";

export default function RouteTracker() {
  const { active } = useActive();
  const idx = WORLDS.findIndex((w) => w.id === active);
  const visible = idx !== -1;

  return (
    <AnimatePresence>
      {visible && (
        <motion.div
          data-testid="route-tracker"
          initial={{ y: 100, opacity: 0 }}
          animate={{ y: 0, opacity: 1 }}
          exit={{ y: 100, opacity: 0 }}
          transition={{ type: "spring", stiffness: 200, damping: 24 }}
          className="fixed bottom-5 left-1/2 z-50 -translate-x-1/2"
        >
          <div className="flex items-center gap-1 rounded-full bg-[#0B0F0C]/85 p-1.5 text-white shadow-2xl backdrop-blur-xl">
            <Sailboat className="ml-2 mr-1 hidden h-4 w-4 sm:block" style={{ color: WORLDS[idx].theme.accent }} />
            {WORLDS.map((w, i) => {
              const on = i === idx;
              return (
                <button
                  key={w.id}
                  data-testid={`route-dot-${w.id}`}
                  onClick={() => scrollToId(w.id)}
                  className="relative rounded-full px-3 py-2 text-xs font-bold transition-colors duration-300"
                  style={{ color: on ? w.theme.ink : "rgba(255,255,255,0.7)" }}
                >
                  {on && <motion.span layoutId="route-pill" className="absolute inset-0 rounded-full" style={{ background: w.theme.bg }} transition={{ type: "spring", stiffness: 300, damping: 28 }} />}
                  <span className="relative">{on ? `${w.num} ${w.word}` : w.num}</span>
                </button>
              );
            })}
          </div>
        </motion.div>
      )}
    </AnimatePresence>
  );
}
