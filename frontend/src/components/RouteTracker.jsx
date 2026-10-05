import { AnimatePresence, motion } from "framer-motion";
import { Sailboat } from "lucide-react";
import { WORLDS } from "../data/worlds";
import { useActive } from "../lib/active";
import { useMesa } from "../lib/mesa";
import { scrollToId } from "../lib/scroll";

export default function RouteTracker() {
  const { active } = useActive();
  const { count } = useMesa();
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
          className={`pointer-events-none fixed inset-x-0 z-50 flex justify-center px-3 md:bottom-5 ${count ? "bottom-[84px]" : "bottom-4"}`}
        >
          <div className="pointer-events-auto flex items-center gap-1 rounded-full bg-[#0B0F0C]/85 p-1.5 text-white shadow-2xl backdrop-blur-xl">
            <Sailboat className="ml-2 mr-1 hidden h-4 w-4 sm:block" style={{ color: WORLDS[idx].theme.accent }} />
            {WORLDS.map((w, i) => {
              const on = i === idx;
              return (
                <button
                  key={w.id}
                  data-testid={`route-dot-${w.id}`}
                  onClick={() => scrollToId(w.id)}
                  className="relative rounded-full px-2.5 py-2 text-xs font-bold transition-colors duration-300 sm:px-3"
                  style={{ color: on ? w.theme.ink : "rgba(255,255,255,0.7)" }}
                >
                  {on && <motion.span layoutId="route-pill" className="absolute inset-0 rounded-full" style={{ background: w.theme.bg }} transition={{ type: "spring", stiffness: 300, damping: 28 }} />}
                  <span className="relative">{w.num}{on && <span className="hidden sm:inline"> {w.word}</span>}</span>
                </button>
              );
            })}
          </div>
        </motion.div>
      )}
    </AnimatePresence>
  );
}
