import { useState } from "react";
import { AnimatePresence, motion } from "framer-motion";
import { Minus, Plus, Check, HandPlatter } from "lucide-react";
import { useMesa } from "../lib/mesa";
import Mascot from "./mascots/Mascot";
import { raciones } from "./carta/Mesa";
import { eur } from "../lib/format";

const TIMES = ["13:00", "13:30", "14:00", "14:30", "20:00", "20:30", "21:00"];
const field = "w-full rounded-2xl border-2 border-coal/15 bg-white px-4 py-3 font-medium outline-none transition-colors duration-300 focus:border-[#F0285F]";

export default function ReserveCard() {
  const [people, setPeople] = useState(2);
  const [time, setTime] = useState("14:00");
  const [sent, setSent] = useState(false);
  const mesa = useMesa();

  const submit = (e) => {
    e.preventDefault();
    setSent(true);
    setTimeout(() => setSent(false), 5000);
  };

  return (
    <form onSubmit={submit} data-testid="reserve-form" className="relative rounded-[36px] bg-paper p-7 text-coal shadow-[0_18px_0_rgba(0,0,0,0.25)] md:p-9">
      <Mascot id="oli" className="drop absolute -right-4 -top-24 h-36 w-32 rotate-12 md:-right-8 md:h-44 md:w-36" />
      <p className="kicker text-[#F0285F]">Reservar mesa</p>
      <p className="font-display mt-2 text-4xl leading-none">Guárdanos un sitio.</p>
      {mesa.count > 0 && (
        <button type="button" onClick={() => mesa.setOpen(true)} data-testid="reserve-mesa-summary" className="mt-5 flex w-full items-center gap-3 rounded-2xl bg-[#A8F0DC] px-4 py-3 text-left transition-transform duration-300 hover:-translate-y-0.5">
          <HandPlatter className="h-5 w-5 shrink-0" />
          <span className="flex-1 text-sm font-semibold">Tu selección de la carta: {raciones(mesa.count)} · {eur(mesa.total)}</span>
          <span className="text-xs font-bold underline">Ver</span>
        </button>
      )}
      <div className="mt-7 space-y-4">
        <input required data-testid="reserve-name-input" placeholder="Tu nombre" className={field} />
        <input required type="date" data-testid="reserve-date-input" className={field} />
        <div className="flex flex-wrap gap-2" data-testid="reserve-time-options">
          {TIMES.map((t) => (
            <button type="button" key={t} data-testid={`reserve-time-${t}`} onClick={() => setTime(t)} className={`rounded-full px-4 py-2 text-sm font-bold transition-colors duration-300 ${time === t ? "bg-coal text-paper" : "bg-coal/5 hover:bg-coal/10"}`}>
              {t}
            </button>
          ))}
        </div>
        <div className="flex items-center justify-between rounded-2xl border-2 border-coal/15 bg-white px-4 py-2">
          <span className="font-medium">Personas</span>
          <div className="flex items-center gap-3">
            <button type="button" data-testid="reserve-people-minus" onClick={() => setPeople((p) => Math.max(1, p - 1))} className="rounded-full bg-coal/5 p-2 hover:bg-coal/10"><Minus className="h-4 w-4" /></button>
            <span data-testid="reserve-people-count" className="font-display w-6 text-center text-2xl">{people}</span>
            <button type="button" data-testid="reserve-people-plus" onClick={() => setPeople((p) => Math.min(6, p + 1))} className="rounded-full bg-coal/5 p-2 hover:bg-coal/10"><Plus className="h-4 w-4" /></button>
          </div>
        </div>
      </div>
      <motion.button whileTap={{ scale: 0.96 }} type="submit" data-testid="reserve-submit-btn" className="mt-6 w-full rounded-full bg-[#F0285F] py-4 font-bold text-white transition-transform duration-300 hover:-translate-y-1">
        Solicitar mesa
      </motion.button>
      <p className="mt-3 text-center text-xs opacity-60">Grupos de hasta seis. La mesa se confirma al organizar la visita.</p>
      <AnimatePresence>
        {sent && (
          <motion.div data-testid="reserve-success-toast" initial={{ opacity: 0, y: 12, scale: 0.95 }} animate={{ opacity: 1, y: 0, scale: 1 }} exit={{ opacity: 0, y: 12 }} className="absolute inset-x-6 -bottom-6 flex items-center gap-3 rounded-2xl bg-coal px-4 py-3 text-sm text-paper">
            <Check className="h-5 w-5 shrink-0 text-[#A8F0DC]" />
            Demo: ORILLA es ficticio, la solicitud ({people} pers. · {time}) no se envía.
          </motion.div>
        )}
      </AnimatePresence>
    </form>
  );
}
