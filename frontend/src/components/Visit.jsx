import { MapPin, Clock } from "lucide-react";
import { ThemedSection } from "../lib/active";
import { THEMES, HOURS } from "../data/worlds";
import ReserveCard from "./ReserveCard";

const Hours = () => (
  <ul className="mt-6 divide-y" style={{ borderColor: "color-mix(in srgb, var(--ink) 20%, transparent)" }}>
    {HOURS.map((h) => (
      <li key={h.day} className="grid grid-cols-1 gap-1 py-4 sm:grid-cols-3" style={{ borderColor: "color-mix(in srgb, var(--ink) 18%, transparent)" }}>
        <span className="font-display text-xl tracking-tight">{h.day}</span>
        <span className="text-sm font-medium opacity-80"><span className="opacity-60">Local · </span>{h.local}</span>
        <span className="text-sm font-medium opacity-80"><span className="opacity-60">Cocina · </span>{h.kitchen}</span>
      </li>
    ))}
  </ul>
);

export default function Visit() {
  return (
    <ThemedSection id="visita" theme={THEMES.visit} className="relative py-32 md:py-44">
      <div className="mx-auto grid max-w-[1400px] gap-14 px-5 md:px-10 lg:grid-cols-12">
        <div className="lg:col-span-7">
          <p className="kicker text-accent">Visítanos</p>
          <h2 className="font-display mt-5 text-[clamp(3rem,8vw,7.5rem)] leading-[0.85]">
            Ven a<br />la <span className="text-accent">orilla.</span>
          </h2>
          <div className="mt-10 flex items-start gap-3" data-testid="visit-location">
            <MapPin className="mt-1 h-5 w-5 text-accent" />
            <div>
              <p className="font-display text-2xl">Alcoy (Alicante)</p>
              <p className="text-sm opacity-60">Dirección y contacto de ejemplo no disponibles.</p>
            </div>
          </div>
          <div className="mt-10" data-testid="visit-hours">
            <p className="flex items-center gap-2 kicker"><Clock className="h-4 w-4 text-accent" /> Horario · Europe/Madrid</p>
            <Hours />
            <p className="mt-4 text-sm opacity-60">Comidas de martes a domingo. Cenas los viernes y sábados. No hay terraza.</p>
          </div>
        </div>
        <div className="lg:col-span-5">
          <ReserveCard />
        </div>
      </div>
    </ThemedSection>
  );
}
