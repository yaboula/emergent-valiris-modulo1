import { motion } from "framer-motion";
import { Plus, Star } from "lucide-react";
import { AllergenDots } from "./Allergens";
import { priceText } from "../../lib/format";
import { useMesa } from "../../lib/mesa";

const Badge = ({ children, style, className = "" }) => (
  <span style={style} className={`rounded-full px-2.5 py-1 text-[11px] font-bold ${className}`}>{children}</span>
);

const Badges = ({ d, w }) => (
  <div className="flex flex-wrap gap-1.5">
    {d.sig && (
      <Badge style={{ background: w.theme.bg, color: w.theme.ink }} className="flex items-center gap-1">
        <Star className="h-3 w-3 fill-current" /> Favorito de {w.char.name}
      </Badge>
    )}
    {d.share && <Badge className="bg-coal/5">Para compartir</Badge>}
    {d.min && <Badge className="bg-coal/5">Mín. {d.min} personas</Badge>}
    {d.diet?.includes("vegan") ? <Badge className="bg-[#7CE0A3]/40">Vegano*</Badge> : d.diet?.includes("veg") && <Badge className="bg-[#7CE0A3]/40">Vegetariano*</Badge>}
  </div>
);

export default function DishCard({ d, w, onOpen }) {
  const { add } = useMesa();
  const quick = d.prices.length === 1 && !d.variants;
  const featured = d.sig && d.img;

  const onAdd = (e) => {
    e.stopPropagation();
    if (!quick) return onOpen(d);
    const p = d.prices[0];
    add({ dishId: d.id, name: d.name, world: d.world, priceId: p.id, priceLabel: p.label, amount: p.amount, unit: p.unit, qty: d.min || 1, min: d.min });
  };

  return (
    <motion.article
      layout
      initial={{ opacity: 0, y: 30, scale: 0.96 }}
      animate={{ opacity: 1, y: 0, scale: 1 }}
      exit={{ opacity: 0, scale: 0.9, transition: { duration: 0.2 } }}
      transition={{ type: "spring", stiffness: 220, damping: 24 }}
      whileHover={{ y: -6 }}
      onClick={() => onOpen(d)}
      data-testid={`dish-card-${d.id}`}
      className={`group relative flex cursor-pointer flex-col overflow-hidden rounded-[28px] bg-paper p-6 text-coal shadow-[0_10px_0_rgba(0,0,0,0.14)] transition-shadow duration-300 hover:shadow-[0_16px_0_rgba(0,0,0,0.2)] ${featured ? "md:col-span-2 md:flex-row md:items-center md:gap-6" : ""}`}
    >
      <div className="flex flex-1 flex-col">
        <Badges d={d} w={w} />
        <h4 className={`font-display mt-4 leading-[0.95] tracking-tight ${featured ? "text-3xl md:text-4xl" : "text-2xl"}`}>{d.name}</h4>
        <p className="mt-2 line-clamp-2 text-sm leading-relaxed opacity-70">{d.desc}</p>
        <div className="mt-auto flex items-end justify-between gap-3 pt-6">
          <AllergenDots ids={d.allergens} testId={`dish-allergens-${d.id}`} />
          <div className="flex items-center gap-3">
            <span data-testid={`dish-price-${d.id}`} className="whitespace-nowrap font-display text-xl tracking-tight">{priceText(d)}</span>
            <motion.button
              whileTap={{ scale: 0.85 }}
              onClick={onAdd}
              data-testid={`dish-add-${d.id}`}
              aria-label={`Añadir ${d.name} a mi mesa`}
              style={{ background: w.theme.bg, color: w.theme.ink }}
              className="grid h-11 w-11 place-items-center rounded-full transition-transform duration-300 group-hover:rotate-90"
            >
              <Plus className="h-5 w-5" strokeWidth={2.6} />
            </motion.button>
          </div>
        </div>
      </div>
      {featured && (
        <div className="relative mt-4 md:mt-0 md:w-[44%]">
          <img src={d.img} alt="" className="drop mx-auto w-[80%] transition-transform duration-700 group-hover:rotate-12 group-hover:scale-105 md:w-full" />
          <span className="absolute bottom-0 left-0 text-[10px] font-semibold opacity-50">Representación conceptual del plato</span>
        </div>
      )}
    </motion.article>
  );
}
