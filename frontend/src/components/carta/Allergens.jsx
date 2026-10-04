import { Wheat, Shrimp, Egg, Fish, Milk, Nut, Bean, LeafyGreen, Sprout, Wine, Shell, Flower2 } from "lucide-react";
import { ALLERGENS } from "../../data/menu";

const ICONS = { gluten: Wheat, crustaceos: Shrimp, huevo: Egg, pescado: Fish, leche: Milk, frutos: Nut, soja: Bean, apio: LeafyGreen, sesamo: Sprout, sulfitos: Wine, moluscos: Shell, mostaza: Flower2 };
const ABBR = { cacahuetes: "Ca", altramuces: "Al" };
export const allergenLabel = (id) => ALLERGENS.find((a) => a.id === id)?.label;

export const AllergenIcon = ({ id, className = "h-3.5 w-3.5" }) => {
  const I = ICONS[id];
  return I ? <I className={className} strokeWidth={2.2} /> : <span className="text-[10px] font-extrabold leading-none">{ABBR[id]}</span>;
};

export const AllergenDots = ({ ids, testId }) =>
  ids.length ? (
    <div className="flex flex-wrap gap-1.5" data-testid={testId}>
      {ids.map((id) => (
        <span key={id} title={allergenLabel(id)} aria-label={allergenLabel(id)} className="grid h-7 w-7 place-items-center rounded-full bg-coal text-paper">
          <AllergenIcon id={id} />
        </span>
      ))}
    </div>
  ) : (
    <span data-testid={testId} className="text-xs font-semibold opacity-55">Sin declaración · pendiente</span>
  );
