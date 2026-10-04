import { motion } from "framer-motion";
import { ArrowUpRight } from "lucide-react";
import { Logo } from "./Symbol";
import { scrollToId } from "../lib/scroll";

const LINKS = [
  { id: "egeo", label: "Las orillas" },
  { id: "reparto", label: "El reparto" },
  { id: "casa", label: "La casa" },
  { id: "visita", label: "Visítanos" },
];

export default function Nav() {
  return (
    <motion.header
      initial={{ y: -80, opacity: 0 }}
      animate={{ y: 0, opacity: 1 }}
      transition={{ duration: 0.8, ease: [0.22, 1, 0.36, 1], delay: 0.2 }}
      className="fixed inset-x-0 top-4 z-50 px-4"
    >
      <nav className="glass mx-auto flex max-w-6xl items-center justify-between rounded-full border border-[color:var(--ink)]/10 py-2.5 pl-5 pr-2.5 text-ink" style={{ borderColor: "color-mix(in srgb, var(--ink) 14%, transparent)" }}>
        <button data-testid="nav-logo" onClick={() => scrollToId("inicio")} className="transition-transform duration-300 hover:scale-105">
          <Logo />
        </button>
        <ul className="hidden items-center gap-1 md:flex">
          {LINKS.map((l) => (
            <li key={l.id}>
              <button
                data-testid={`nav-link-${l.id}`}
                onClick={() => scrollToId(l.id)}
                className="rounded-full px-4 py-2 text-sm font-semibold transition-colors duration-300 hover:bg-[color:var(--ink)] hover:text-[color:var(--bg)]"
              >
                {l.label}
              </button>
            </li>
          ))}
        </ul>
        <motion.button
          whileTap={{ scale: 0.95 }}
          data-testid="nav-reserve-btn"
          onClick={() => scrollToId("visita")}
          className="group flex items-center gap-2 rounded-full bg-ink px-5 py-2.5 text-sm font-bold text-bg transition-transform duration-300 hover:-rotate-2"
        >
          Reservar mesa
          <ArrowUpRight className="h-4 w-4 transition-transform duration-300 group-hover:rotate-45" />
        </motion.button>
      </nav>
    </motion.header>
  );
}
