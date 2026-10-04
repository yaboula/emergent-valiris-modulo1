import { motion } from "framer-motion";
import { Flame, Users, Soup } from "lucide-react";
import { ThemedSection } from "../lib/active";
import { THEMES } from "../data/worlds";

const FACTS = [
  { icon: Users, big: "6", label: "Una mesa larga para seis, y mesas pequeñas para dos o cuatro." },
  { icon: Flame, big: "1", label: "Un horno a la vista: el centro de trabajo de la cocina." },
  { icon: Soup, big: "2", label: "El arroz al horno se prepara para un mínimo de dos personas." },
];

export default function Casa() {
  return (
    <ThemedSection id="casa" theme={THEMES.casa} className="relative overflow-hidden py-20 md:py-28">
      <div className="mx-auto grid max-w-[1400px] gap-12 px-5 md:px-10 lg:grid-cols-12">
        <div className="lg:col-span-6">
          <p className="kicker opacity-80">La casa · Alcoy</p>
          <h2 className="font-display mt-5 text-[clamp(2.8rem,6.5vw,6rem)] leading-[0.88]">
            Dos hermanos.<br />Una discusión<br />de domingo.
          </h2>
          <div className="mt-8 max-w-xl space-y-4 text-lg font-medium leading-relaxed opacity-90">
            <p>Inés quería que todos probaran la verdura mientras seguía caliente. Dani quería que nadie tuviera prisa por levantarse después.</p>
            <p>ORILLA es su respuesta: platos para el centro y platos para uno, un horno siempre encendido y una mesa de madera para seis que Dani reparó con sus manos.</p>
          </div>
        </div>
        <div className="relative lg:col-span-6">
          <motion.img
            initial={{ rotate: -20, scale: 0.8, opacity: 0 }}
            whileInView={{ rotate: -6, scale: 1, opacity: 1 }}
            viewport={{ once: true, amount: 0.3 }}
            transition={{ type: "spring", stiffness: 80, damping: 14 }}
            src="/img/top_arroz.webp"
            alt="Arroz al horno en cassola de barro"
            className="drop mx-auto w-[85%]"
            data-testid="casa-dish-img"
          />
        </div>
        <div className="grid gap-4 md:grid-cols-3 lg:col-span-12">
          {FACTS.map((f, i) => (
            <motion.div
              key={i}
              data-testid={`casa-fact-${i}`}
              initial={{ opacity: 0, y: 40 }}
              whileInView={{ opacity: 1, y: 0 }}
              viewport={{ once: true }}
              transition={{ delay: i * 0.1, duration: 0.7 }}
              className="group rounded-[32px] bg-paper p-7 text-coal transition-transform duration-300 hover:-translate-y-2 hover:rotate-1"
            >
              <div className="flex items-start justify-between">
                <span className="font-display text-7xl leading-none text-[#F0285F]">{f.big}</span>
                <f.icon className="h-7 w-7 transition-transform duration-500 group-hover:rotate-12" />
              </div>
              <p className="mt-5 font-medium leading-relaxed">{f.label}</p>
            </motion.div>
          ))}
        </div>
      </div>
    </ThemedSection>
  );
}
