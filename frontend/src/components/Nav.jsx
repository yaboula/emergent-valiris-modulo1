import { motion } from "framer-motion";
import { useLocation, useNavigate } from "react-router-dom";
import { ArrowUpRight } from "lucide-react";
import { Logo } from "./Symbol";
import { scrollToId } from "../lib/scroll";

const LINKS = [
  { id: "egeo", label: "Las orillas" },
  { id: "carta", label: "La carta", route: "/carta" },
  { id: "reparto", label: "El reparto" },
  { id: "casa", label: "La casa" },
  { id: "visita", label: "Visítanos" },
];

export const useGo = () => {
  const navigate = useNavigate();
  const { pathname } = useLocation();
  return (id) => (pathname === "/" ? scrollToId(id) : navigate(`/#${id}`));
};

export default function Nav() {
  const go = useGo();
  const navigate = useNavigate();
  const { pathname } = useLocation();

  return (
    <motion.header initial={{ y: -80, opacity: 0 }} animate={{ y: 0, opacity: 1 }} transition={{ duration: 0.8, ease: [0.22, 1, 0.36, 1], delay: 0.2 }} className="fixed inset-x-0 top-4 z-50 px-4">
      <nav className="glass mx-auto flex max-w-6xl items-center justify-between rounded-full border py-2.5 pl-5 pr-2.5 text-ink" style={{ borderColor: "color-mix(in srgb, var(--ink) 14%, transparent)" }}>
        <button data-testid="nav-logo" onClick={() => go("inicio")} className="transition-transform duration-300 hover:scale-105">
          <Logo />
        </button>
        <ul className="hidden items-center gap-1 md:flex">
          {LINKS.map((l) => {
            const on = l.route && pathname === l.route;
            return (
              <li key={l.id}>
                <button
                  data-testid={`nav-link-${l.id}`}
                  onClick={() => (l.route ? navigate(l.route) : go(l.id))}
                  className={`rounded-full px-4 py-2 text-sm font-semibold transition-colors duration-300 hover:bg-[color:var(--ink)] hover:text-[color:var(--bg)] ${on ? "bg-[color:var(--ink)] text-[color:var(--bg)]" : ""}`}
                >
                  {l.label}
                </button>
              </li>
            );
          })}
        </ul>
        <div className="flex items-center gap-2">
          <button data-testid="nav-carta-mobile-btn" onClick={() => navigate("/carta")} className="rounded-full border-2 border-current px-4 py-2 text-sm font-bold md:hidden">Carta</button>
          <motion.button whileTap={{ scale: 0.95 }} data-testid="nav-reserve-btn" onClick={() => go("visita")} className="group flex items-center gap-2 rounded-full bg-ink px-5 py-2.5 text-sm font-bold text-bg transition-transform duration-300 hover:-rotate-2">
            <span>Reservar<span className="hidden sm:inline"> mesa</span></span>
            <ArrowUpRight className="h-4 w-4 transition-transform duration-300 group-hover:rotate-45" />
          </motion.button>
        </div>
      </nav>
    </motion.header>
  );
}
