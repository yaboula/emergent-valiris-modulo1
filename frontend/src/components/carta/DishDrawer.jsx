import { useEffect, useState } from "react";
import { motion } from "framer-motion";
import { Minus, Plus, Info, AlertTriangle } from "lucide-react";
import Reveal, { priceLabel } from "./Reveal";
import Sheet from "../Sheet";
import { AllergenIcon, allergenLabel } from "./Allergens";
import { WORLDS } from "../../data/worlds";
import { FOOD_NOTICE } from "../../data/menu";
import { eur } from "../../lib/format";
import { useMesa } from "../../lib/mesa";

const Option = ({ on, onClick, children, testId }) => (
  <button type="button" data-testid={testId} onClick={onClick} className={`flex w-full items-center justify-between rounded-2xl border-2 px-4 py-3 text-left font-semibold transition-colors duration-300 ${on ? "border-coal bg-coal text-paper" : "border-coal/15 hover:border-coal/40"}`}>
    {children}
  </button>
);

const AllergenBlock = ({ ids }) => (
  <section className="mt-8" data-testid="dish-drawer-allergens">
    <p className="kicker opacity-60">Alérgenos declarados</p>
    {ids.length ? (
      <div className="mt-3 flex flex-wrap gap-2">
        {ids.map((id) => (
          <span key={id} className="flex items-center gap-2 rounded-full bg-coal px-3 py-1.5 text-sm font-semibold text-paper">
            <AllergenIcon id={id} /> {allergenLabel(id)}
          </span>
        ))}
      </div>
    ) : (
      <p className="mt-3 text-sm font-medium">No hay ninguna declaración positiva de alérgenos. Información pendiente: no significa «sin alérgenos».</p>
    )}
  </section>
);

export default function DishDrawer({ dish, onClose }) {
  const { add } = useMesa();
  const [priceId, setPriceId] = useState(null);
  const [variantId, setVariantId] = useState(null);
  const [qty, setQty] = useState(1);

  useEffect(() => {
    if (!dish) return;
    setPriceId(dish.prices[0].id);
    setVariantId(dish.variants?.[0].id || null);
    setQty(dish.min || 1);
  }, [dish]);

  const d = dish;
  const w = d && WORLDS.find((x) => x.id === d.world);
  const v = d?.variants?.find((x) => x.id === variantId);
  const p = d?.prices.find((x) => x.id === priceId) || d?.prices[0];
  const allergens = v?.allergens || d?.allergens || [];
  const showImg = d?.img && (!d.variants || variantId === "V01");

  const submit = () => {
    add({ dishId: d.id, name: v?.name || d.name, world: d.world, priceId: p.id, priceLabel: p.label, amount: p.amount, unit: p.unit, qty, min: d.min, variantId: v?.id, variantLabel: v?.label });
    onClose();
  };

  return (
    <Sheet open={!!d} onClose={onClose} testId="dish-drawer">
      {d && (
        <>
          <Reveal d={d} w={w} showImg={showImg} price={priceLabel(p)} onClose={onClose} />
          <div className="flex-1 overflow-y-auto px-7 pb-8 pt-6">
            <p className="kicker opacity-60">Orilla {w.num} · {w.title}{showImg ? " · foto conceptual" : ""}</p>
            <h3 data-testid="dish-drawer-title" className="font-display mt-2 text-4xl leading-[0.92]">{v?.name || d.name}</h3>
            <div className="mt-4" />
            <p className="text-base leading-relaxed opacity-80">{v?.desc || d.desc}</p>
            {d.variants && (
              <section className="mt-7 space-y-2" data-testid="dish-drawer-variants">
                <p className="kicker opacity-60">Elige la variante · el precio no cambia</p>
                {d.variants.map((x) => (
                  <Option key={x.id} on={variantId === x.id} onClick={() => setVariantId(x.id)} testId={`dish-variant-${x.id}`}>{x.label}</Option>
                ))}
              </section>
            )}
            <section className="mt-7 space-y-2" data-testid="dish-drawer-formats">
              <p className="kicker opacity-60">Formato</p>
              {d.prices.map((x) => (
                <Option key={x.id} on={p.id === x.id} onClick={() => setPriceId(x.id)} testId={`dish-format-${x.id}`}>
                  <span>{x.label}{x.note && <span className="block text-xs font-medium opacity-70">{x.note}</span>}</span>
                  <span className="font-display text-lg">{eur(x.amount)}{x.unit ? ` / ${x.unit}` : ""}</span>
                </Option>
              ))}
            </section>
            {v?.warn && (
              <p className="mt-4 flex gap-2 rounded-2xl bg-[#FFD23F]/40 p-4 text-sm font-medium" data-testid="dish-variant-warning"><AlertTriangle className="h-5 w-5 shrink-0" /> {v.warn}</p>
            )}
            <AllergenBlock ids={allergens} />
            {d.dietNote && <p className="mt-4 text-sm font-semibold">{d.dietNote}</p>}
            {d.diet && !d.dietNote && <p className="mt-4 text-sm font-medium opacity-70">*Etiqueta de dieta de ejemplo, sin verificar.</p>}
            <p className="mt-2 text-sm opacity-60">Información nutricional pendiente.</p>
            <p className="mt-6 flex gap-2 rounded-2xl bg-coal/5 p-4 text-xs font-medium leading-relaxed" data-testid="dish-food-notice"><Info className="h-4 w-4 shrink-0" /> ORILLA es ficticio. {FOOD_NOTICE}</p>
          </div>
          <div className="flex items-center gap-3 border-t border-coal/10 bg-paper px-7 py-5">
            <div className="flex items-center gap-2 rounded-full border-2 border-coal/15 p-1">
              <button data-testid="dish-qty-minus" onClick={() => setQty((q) => Math.max(d.min || 1, q - 1))} className="grid h-9 w-9 place-items-center rounded-full hover:bg-coal/10" aria-label="Menos"><Minus className="h-4 w-4" /></button>
              <span data-testid="dish-qty" className="font-display w-6 text-center text-xl">{qty}</span>
              <button data-testid="dish-qty-plus" onClick={() => setQty((q) => Math.min(12, q + 1))} className="grid h-9 w-9 place-items-center rounded-full hover:bg-coal/10" aria-label="Más"><Plus className="h-4 w-4" /></button>
            </div>
            <motion.button whileTap={{ scale: 0.96 }} data-testid="dish-add-to-mesa-btn" onClick={submit} className="flex flex-1 items-center justify-between rounded-full bg-[#F0285F] px-6 py-4 font-bold text-white transition-transform duration-300 hover:-translate-y-0.5">
              <span>Añadir<span className="hidden sm:inline"> a mi mesa</span></span>
              <span>{eur(p.amount * qty)}</span>
            </motion.button>
          </div>
        </>
      )}
    </Sheet>
  );
}
