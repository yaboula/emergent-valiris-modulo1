import { useEffect, useMemo, useState } from "react";
import { AnimatePresence, motion } from "framer-motion";
import { useSearchParams } from "react-router-dom";
import { WORLDS, HOST } from "../data/worlds";
import { DISHES } from "../data/menu";
import { norm } from "../lib/format";
import { scrollToId } from "../lib/scroll";
import CartaHero from "../components/carta/CartaHero";
import FilterBar from "../components/carta/FilterBar";
import WorldGroup from "../components/carta/WorldGroup";
import DishDrawer from "../components/carta/DishDrawer";
import { MesaButton } from "../components/carta/Mesa";
import Footer from "../components/Footer";
import Mascot from "../components/mascots/Mascot";

const IMGS = { "eg-horiatiki": "/img/top_horiatiki.webp", "ti-spaghetti": "/img/top_pasta.webp", "ORI-DISH-02": "/img/top_berenjena.webp", "ORI-DISH-04": "/img/top_arroz.webp", "or-hummus": "/img/top_hummus.webp", "ma-tajin": "/img/top_tajin.webp" };
const ALL = DISHES.map((d) => ({ ...d, img: IMGS[d.id] }));

const useFilters = () => {
  const [params, setParams] = useSearchParams();
  const [q, setQ] = useState("");
  const [cats, setCats] = useState([]);
  const [diets, setDiets] = useState([]);
  const [exclude, setExclude] = useState([]);
  const world = WORLDS.some((w) => w.id === params.get("orilla")) ? params.get("orilla") : "all";
  const setWorld = (id) => setParams(id === "all" ? {} : { orilla: id }, { replace: true });
  const reset = () => { setQ(""); setCats([]); setDiets([]); setExclude([]); setWorld("all"); };

  const results = useMemo(() => {
    const nq = norm(q.trim());
    return ALL.filter((d) =>
      (world === "all" || d.world === world) &&
      (!cats.length || cats.includes(d.cat)) &&
      diets.every((x) => d.diet?.includes(x)) &&
      !d.allergens.some((a) => exclude.includes(a)) &&
      (!nq || norm(`${d.name} ${d.desc}`).includes(nq))
    );
  }, [q, world, cats, diets, exclude]);

  return { q, setQ, world, setWorld, cats, setCats, diets, setDiets, exclude, setExclude, reset, results };
};

const Empty = ({ onReset }) => (
  <motion.div initial={{ opacity: 0, y: 30 }} animate={{ opacity: 1, y: 0 }} className="mx-auto flex max-w-xl flex-col items-center px-5 py-28 text-center" data-testid="carta-empty-state">
    <Mascot id={HOST.id} className="drop h-48 w-40 -rotate-6" />
    <p className="font-display mt-6 text-5xl leading-[0.9]">Ninguna orilla tiene eso hoy.</p>
    <p className="mt-3 font-medium opacity-70">Prueba con menos filtros u otra palabra.</p>
    <button onClick={onReset} data-testid="carta-empty-reset-btn" className="mt-6 rounded-full bg-coal px-6 py-3 font-bold text-paper">Limpiar filtros</button>
  </motion.div>
);

export default function Carta() {
  const f = useFilters();
  const [dish, setDish] = useState(null);
  const groups = WORLDS.map((w) => ({ w, items: f.results.filter((d) => d.world === w.id) })).filter((g) => g.items.length);

  useEffect(() => {
    if (f.world !== "all") setTimeout(() => scrollToId("carta-resultados", -150), 60);
  }, [f.world]);

  return (
    <>
      <main className="pb-20 md:pb-0">
        <CartaHero onPick={f.setWorld} />
        <FilterBar f={f} count={f.results.length} />
        <div id="carta-resultados" data-testid="carta-results">
          <AnimatePresence mode="wait">
            {groups.length === 0 && <Empty key="empty" onReset={f.reset} />}
          </AnimatePresence>
          {groups.map((g) => <WorldGroup key={g.w.id} w={g.w} items={g.items} onOpen={setDish} />)}
        </div>
        <Footer />
      </main>
      <DishDrawer dish={dish} onClose={() => setDish(null)} />
      <MesaButton always />
    </>
  );
}
