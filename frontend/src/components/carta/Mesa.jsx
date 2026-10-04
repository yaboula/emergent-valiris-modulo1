import { AnimatePresence, motion } from "framer-motion";
import { useLocation, useNavigate } from "react-router-dom";
import { HandPlatter, Minus, Plus, Trash2, X, ArrowRight } from "lucide-react";
import Sheet from "../Sheet";
import { useMesa } from "../../lib/mesa";
import { eur } from "../../lib/format";
import { WORLDS, HOST } from "../../data/worlds";
import { scrollToId } from "../../lib/scroll";

const Line = ({ i }) => {
  const { setQty, remove } = useMesa();
  const w = WORLDS.find((x) => x.id === i.world);
  return (
    <motion.li layout initial={{ opacity: 0, x: 40 }} animate={{ opacity: 1, x: 0 }} exit={{ opacity: 0, x: -40 }} data-testid={`mesa-line-${i.dishId}`} className="flex gap-4 rounded-3xl bg-white p-4">
      <span className="mt-1 h-10 w-10 shrink-0 rounded-full" style={{ background: w.theme.bg }}>
        <img src={w.char.img} alt="" className="h-full w-full object-contain p-0.5" />
      </span>
      <div className="min-w-0 flex-1">
        <p className="font-display text-lg leading-tight tracking-tight">{i.name}</p>
        <p className="text-xs font-medium opacity-60">{[i.variantLabel, i.priceLabel].filter(Boolean).join(" · ")}{i.min ? ` · mín. ${i.min}` : ""}</p>
        <div className="mt-3 flex items-center justify-between">
          <div className="flex items-center gap-1 rounded-full bg-coal/5 p-1">
            <button data-testid={`mesa-line-minus-${i.dishId}`} onClick={() => setQty(i.key, i.qty - 1)} className="grid h-7 w-7 place-items-center rounded-full hover:bg-coal/10" aria-label="Menos"><Minus className="h-3.5 w-3.5" /></button>
            <span className="w-6 text-center text-sm font-bold" data-testid={`mesa-line-qty-${i.dishId}`}>{i.qty}</span>
            <button data-testid={`mesa-line-plus-${i.dishId}`} onClick={() => setQty(i.key, i.qty + 1)} className="grid h-7 w-7 place-items-center rounded-full hover:bg-coal/10" aria-label="Más"><Plus className="h-3.5 w-3.5" /></button>
          </div>
          <div className="flex items-center gap-2">
            <span className="font-display text-lg">{eur(i.amount * i.qty)}</span>
            <button data-testid={`mesa-line-remove-${i.dishId}`} onClick={() => remove(i.key)} className="grid h-8 w-8 place-items-center rounded-full opacity-50 transition-opacity hover:bg-coal/10 hover:opacity-100" aria-label="Quitar"><Trash2 className="h-4 w-4" /></button>
          </div>
        </div>
      </div>
    </motion.li>
  );
};

const Empty = ({ onExplore }) => (
  <div className="flex flex-1 flex-col items-center justify-center px-8 text-center" data-testid="mesa-empty">
    <img src={HOST.img} alt="" className="drop h-40" />
    <p className="font-display mt-6 text-3xl leading-none">Tu mesa está vacía.</p>
    <p className="mt-2 text-sm opacity-60">Pulsa «+» en cualquier plato para empezar a montarla.</p>
    <button onClick={onExplore} data-testid="mesa-explore-btn" className="mt-6 rounded-full bg-coal px-6 py-3 font-bold text-paper">Explorar la carta</button>
  </div>
);

export function MesaDrawer() {
  const { items, total, count, open, setOpen, clear } = useMesa();
  const navigate = useNavigate();
  const { pathname } = useLocation();
  const close = () => setOpen(false);

  const reserve = () => {
    close();
    if (pathname === "/") setTimeout(() => scrollToId("visita"), 350);
    else navigate("/#visita");
  };
  const explore = () => {
    close();
    if (pathname !== "/carta") navigate("/carta");
  };

  return (
    <Sheet open={open} onClose={close} testId="mesa-drawer">
      <div className="flex items-center justify-between px-7 pb-4 pt-7">
        <div>
          <p className="kicker text-[#F0285F]">Mi mesa</p>
          <p className="font-display text-4xl leading-none">Lo que nos apetece</p>
        </div>
        <button onClick={close} data-testid="mesa-drawer-close" aria-label="Cerrar" className="grid h-10 w-10 place-items-center rounded-full bg-coal/5 transition-transform duration-300 hover:rotate-90"><X className="h-5 w-5" /></button>
      </div>
      {items.length === 0 ? (
        <Empty onExplore={explore} />
      ) : (
        <>
          <ul className="flex-1 space-y-3 overflow-y-auto bg-coal/[0.03] px-5 py-5">
            <AnimatePresence initial={false}>{items.map((i) => <Line key={i.key} i={i} />)}</AnimatePresence>
          </ul>
          <div className="border-t border-coal/10 px-7 py-5">
            <div className="flex items-end justify-between">
              <div>
                <p className="text-sm font-semibold opacity-60">{count} raciones · total orientativo</p>
                <button onClick={clear} data-testid="mesa-clear-btn" className="mt-1 text-xs font-bold underline opacity-60 hover:opacity-100">Vaciar mesa</button>
              </div>
              <p data-testid="mesa-total" className="font-display text-4xl leading-none">{eur(total)}</p>
            </div>
            <motion.button whileTap={{ scale: 0.97 }} onClick={reserve} data-testid="mesa-reserve-btn" className="mt-5 flex w-full items-center justify-center gap-2 rounded-full bg-[#F0285F] py-4 font-bold text-white transition-transform duration-300 hover:-translate-y-0.5">
              Reservar con esta selección <ArrowRight className="h-4 w-4" />
            </motion.button>
            <p className="mt-3 text-center text-xs opacity-55">No es un pedido ni un pago: es una idea para comentarla en sala.</p>
          </div>
        </>
      )}
    </Sheet>
  );
}

export function MesaButton({ always = false }) {
  const { count, total, setOpen, bump } = useMesa();
  if (!always && count === 0) return null;
  return (
    <motion.button
      initial={{ y: 80, opacity: 0 }}
      animate={{ y: 0, opacity: 1 }}
      whileHover={{ y: -4 }}
      whileTap={{ scale: 0.95 }}
      onClick={() => setOpen(true)}
      data-testid="mesa-open-btn"
      className={`fixed right-4 z-50 flex items-center gap-3 rounded-full bg-coal py-2 pl-2 pr-5 text-paper shadow-[0_12px_30px_rgba(0,0,0,0.35)] sm:bottom-5 sm:right-5 ${always ? "bottom-5" : "bottom-20"}`}
    >
      <motion.span key={bump} initial={{ scale: 1 }} animate={{ scale: bump ? [1, 1.35, 1] : 1, rotate: bump ? [0, -15, 10, 0] : 0 }} transition={{ duration: 0.5 }} className="relative grid h-11 w-11 place-items-center rounded-full bg-[#F0285F]">
        <HandPlatter className="h-5 w-5" />
        <span data-testid="mesa-count" className="absolute -right-1 -top-1 grid h-5 min-w-5 place-items-center rounded-full bg-[#FFD23F] px-1 text-[11px] font-extrabold text-coal">{count}</span>
      </motion.span>
      <span className="text-left leading-tight">
        <span className="block text-xs font-semibold opacity-60">Mi mesa</span>
        <span className="font-display text-lg">{eur(total)}</span>
      </span>
    </motion.button>
  );
}
