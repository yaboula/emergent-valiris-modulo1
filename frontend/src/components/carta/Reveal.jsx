import { useEffect, useState } from "react";
import { AnimatePresence, motion } from "framer-motion";
import { X } from "lucide-react";
import Mascot from "../mascots/Mascot";
import { INK } from "../mascots/parts";
import { eur } from "../../lib/format";

const Cloche = () => (
  <svg viewBox="0 0 200 132" className="w-full" aria-hidden="true">
    <path d="M12 120 Q12 22 100 22 Q188 22 188 120 Z" fill="#ECE7DC" stroke={INK} strokeWidth={4} />
    <path d="M42 100 Q46 54 88 38" stroke="#fff" strokeWidth={9} opacity={0.7} fill="none" strokeLinecap="round" />
    <rect x={2} y={116} width={196} height={12} rx={6} fill="#D2CBBD" stroke={INK} strokeWidth={4} />
    <circle cx={100} cy={16} r={10} fill="#D2CBBD" stroke={INK} strokeWidth={4} />
  </svg>
);

const Sticker = ({ w, d, price }) => (
  <svg viewBox="0 0 200 200" className="h-full w-full" data-testid="reveal-sticker">
    <defs><path id={`ring-${d.id}`} d="M100 100 m-74 0 a74 74 0 1 1 148 0 a74 74 0 1 1 -148 0" /></defs>
    <circle cx={100} cy={100} r={96} fill="#FFFBF2" stroke={INK} strokeWidth={4} />
    <circle cx={100} cy={100} r={58} fill={w.theme.accent} />
    <text fontFamily="Bricolage Grotesque" fontWeight={800} fontSize={15} fill={INK}>
      <textPath href={`#ring-${d.id}`} textLength={458} lengthAdjust="spacing">{`MARCHANDO · ORILLA ${w.num} · ${w.word} · `}</textPath>
    </text>
    <text x={100} y={108} textAnchor="middle" fontFamily="Bricolage Grotesque" fontWeight={800} fontSize={26} fill={INK}>{price}</text>
  </svg>
);

const Sparkles = () => (
  <div className="pointer-events-none absolute inset-0" aria-hidden="true">
    {Array.from({ length: 8 }).map((_, i) => {
      const a = (i / 8) * Math.PI * 2;
      return (
        <motion.span key={i} initial={{ x: 0, y: 0, scale: 0 }} animate={{ x: Math.cos(a) * 130, y: Math.sin(a) * 110, scale: [0, 1.2, 0] }} transition={{ delay: 0.8, duration: 0.9, ease: "easeOut" }} className="absolute left-1/2 top-1/2 h-4 w-4">
          <svg viewBox="0 0 24 24"><path d="M12 0 C13 8 16 11 24 12 C16 13 13 16 12 24 C11 16 8 13 0 12 C8 11 11 8 12 0Z" fill="#FFD23F" /></svg>
        </motion.span>
      );
    })}
  </div>
);

export default function Reveal({ d, w, showImg, price, onClose }) {
  const [present, setPresent] = useState(false);
  const line = w.char.lines[d.id.length % w.char.lines.length];

  useEffect(() => {
    setPresent(false);
    const t = setTimeout(() => setPresent(true), 650);
    return () => clearTimeout(t);
  }, [d.id]);

  return (
    <div className="relative h-[280px] shrink-0 overflow-hidden sm:h-[320px]" style={{ background: w.theme.bg, color: w.theme.ink }} data-testid="dish-reveal">
      <div className="font-display pointer-events-none absolute -bottom-5 left-3 whitespace-nowrap text-[110px] leading-none opacity-40" style={{ color: "transparent", WebkitTextStroke: `2px ${w.theme.accent}` }}>{w.word}</div>
      <button onClick={onClose} data-testid="dish-drawer-close" aria-label="Cerrar" className="absolute right-4 top-4 z-30 grid h-10 w-10 place-items-center rounded-full bg-black/20 transition-transform duration-300 hover:rotate-90">
        <X className="h-5 w-5" />
      </button>
      <div className="absolute right-4 top-12 h-[180px] w-[180px] sm:right-8 sm:h-[230px] sm:w-[230px]">
        <motion.div key={d.id} initial={{ scale: 0.5, rotate: -40, opacity: 0 }} animate={{ scale: 1, rotate: 0, opacity: 1 }} transition={{ delay: 0.75, type: "spring", stiffness: 140, damping: 12 }} className="absolute inset-0 grid place-items-center">
          {showImg ? <img src={d.img} alt="" className="drop h-full w-full object-contain" data-testid="reveal-dish-img" /> : <Sticker w={w} d={d} price={price} />}
        </motion.div>
        <Sparkles key={`s${d.id}`} />
        <motion.div key={`c${d.id}`} initial={{ y: 0, rotate: 0, opacity: 1 }} animate={{ y: -280, rotate: 28, opacity: 0 }} transition={{ delay: 0.6, duration: 0.7, ease: [0.6, 0, 0.4, 1] }} className="absolute inset-x-0 top-8 z-10">
          <Cloche />
        </motion.div>
      </div>
      <motion.div key={`m${d.id}`} initial={{ y: 220 }} animate={{ y: 0 }} transition={{ type: "spring", stiffness: 160, damping: 15, delay: 0.1 }} className="absolute -bottom-2 left-0 h-[170px] w-[142px] sm:h-[220px] sm:w-[184px]">
        <Mascot id={w.char.id} present={present} label={w.char.name} className="drop h-full w-full" />
      </motion.div>
      <AnimatePresence>
        {present && (
          <motion.p data-testid="reveal-bubble" initial={{ scale: 0, opacity: 0, rotate: -10 }} animate={{ scale: 1, opacity: 1, rotate: -3 }} transition={{ type: "spring", stiffness: 260, damping: 16 }} className="absolute left-[118px] top-5 z-20 max-w-[170px] rounded-3xl bg-paper px-4 py-3 font-display text-[15px] leading-tight tracking-tight text-coal shadow-[0_8px_0_rgba(0,0,0,0.18)] sm:left-[150px] sm:max-w-[200px] sm:text-base">
            {line}
          </motion.p>
        )}
      </AnimatePresence>
    </div>
  );
}

export const priceLabel = (p) => `${eur(p.amount)}${p.unit ? "/p" : ""}`;
