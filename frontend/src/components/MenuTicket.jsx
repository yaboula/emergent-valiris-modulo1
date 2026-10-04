import { useNavigate } from "react-router-dom";
import { ArrowRight } from "lucide-react";

export default function MenuTicket({ w }) {
  const navigate = useNavigate();
  return (
    <div data-testid={`world-menu-${w.id}`} className="mt-8 max-w-lg rounded-[28px] bg-paper p-2 text-coal shadow-[0_14px_0_rgba(0,0,0,0.16)]">
      <div className="flex items-center justify-between px-4 pb-2 pt-3">
        <span className="kicker">De la carta</span>
        <span className="text-xs font-semibold opacity-60">{w.char.name} recomienda</span>
      </div>
      <ul className="divide-y-2 divide-dashed divide-coal/15">
        {w.dishes.map((d, i) => (
          <li key={d.name} data-testid={`world-dish-${w.id}-${i}`} className="group flex items-start justify-between gap-4 rounded-2xl px-4 py-3 transition-colors duration-300 hover:bg-[color:var(--bg)] hover:text-[color:var(--ink)]">
            <div>
              <p className="font-display text-lg leading-tight tracking-tight">{d.name}</p>
              <p className="mt-0.5 text-sm opacity-70">{d.desc}</p>
            </div>
            <span className="shrink-0 whitespace-nowrap pt-0.5 text-sm font-bold">{d.price}</span>
          </li>
        ))}
      </ul>
      <button
        onClick={() => navigate(`/carta?orilla=${w.id}`)}
        data-testid={`world-carta-link-${w.id}`}
        style={{ background: w.theme.bg, color: w.theme.ink }}
        className="group mt-1 flex w-full items-center justify-between rounded-[22px] px-5 py-3.5 text-sm font-bold"
      >
        Ver toda la carta de {w.title}
        <ArrowRight className="h-4 w-4 transition-transform duration-300 group-hover:translate-x-1.5" />
      </button>
    </div>
  );
}
