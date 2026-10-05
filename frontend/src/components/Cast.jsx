import { motion } from "framer-motion";
import { ThemedSection } from "../lib/active";
import { THEMES, WORLDS, HOST } from "../data/worlds";
import Mascot from "./mascots/Mascot";

const CAST = [
  { id: "oli", mascot: HOST.id, name: HOST.name, role: HOST.role, color: "#A8F0DC", tag: "Anfitrión" },
  ...WORLDS.map((w) => ({ id: w.id, mascot: w.char.id, name: w.char.name, role: w.char.role, color: w.theme.bg, tag: w.country.split(" ·")[0] })),
];

const Member = ({ m, i }) => (
  <motion.div
    data-testid={`cast-member-${m.id}`}
    initial={{ opacity: 0, y: 60, rotate: i % 2 ? 4 : -4 }}
    whileInView={{ opacity: 1, y: 0, rotate: 0 }}
    viewport={{ once: true, amount: 0.3 }}
    transition={{ type: "spring", stiffness: 120, damping: 16, delay: i * 0.07 }}
    whileHover={{ y: -12, rotate: i % 2 ? 2 : -2 }}
    className="group relative flex w-[60vw] shrink-0 snap-center flex-col items-center md:w-auto"
  >
    <div className="relative flex aspect-[4/5] w-full items-end justify-center overflow-hidden rounded-[999px_999px_36px_36px] pt-6" style={{ background: m.color }}>
      <Mascot id={m.mascot} label={m.name} className="drop relative z-10 h-[86%] w-[80%] transition-transform duration-500 group-hover:scale-110 group-hover:-rotate-6" />
    </div>
    <p className="font-display mt-4 text-2xl leading-none">{m.name}</p>
    <p className="mt-1 text-center text-sm font-medium opacity-70">{m.role}</p>
    <span className="kicker mt-2 rounded-full border-2 border-current px-3 py-0.5 !text-[10px]">{m.tag}</span>
  </motion.div>
);

export default function Cast() {
  return (
    <ThemedSection id="reparto" theme={THEMES.cast} className="relative py-20 md:py-28">
      <div className="mx-auto max-w-[1400px] px-5 md:px-10">
        <div className="mb-12 grid gap-6 md:grid-cols-12 md:items-end">
          <h2 className="font-display text-[clamp(3rem,8vw,7.5rem)] leading-[0.85] md:col-span-7">
            Conoce<br />al <span className="text-accent">reparto.</span>
          </h2>
          <p className="max-w-md text-lg font-medium leading-relaxed opacity-80 md:col-span-5">
            Cada orilla tiene su guardián. Son exigentes, un poco exagerados y saben exactamente cómo debería saber su plato.
          </p>
        </div>
        <p className="kicker mb-4 opacity-60 md:hidden">Desliza para conocerlos →</p>
        <div data-testid="cast-track" className="-mx-5 flex snap-x snap-mandatory gap-4 overflow-x-auto px-5 pb-4 [scrollbar-width:none] md:mx-0 md:grid md:grid-cols-3 md:gap-x-5 md:gap-y-12 md:overflow-visible md:px-0 lg:grid-cols-6">
          {CAST.map((m, i) => <Member key={m.id} m={m} i={i} />)}
        </div>
      </div>
    </ThemedSection>
  );
}
