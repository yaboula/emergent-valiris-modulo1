import { useRef } from "react";
import { motion, useScroll, useTransform } from "framer-motion";
import { ArrowDown } from "lucide-react";
import Symbol from "./Symbol";
import Character, { Bubble } from "./Character";
import { ThemedSection } from "../lib/active";
import { THEMES, HOST } from "../data/worlds";
import { scrollToId } from "../lib/scroll";

const ease = [0.22, 1, 0.36, 1];
const LETTERS = ["R", "I", "L", "L", "A"];

const Wordmark = () => (
  <h1 data-testid="hero-wordmark" aria-label="ORILLA" className="font-display flex items-center text-[clamp(5.2rem,21vw,21rem)] leading-[0.82]">
    <motion.span initial={{ scale: 0, rotate: -180 }} animate={{ scale: 1, rotate: 0 }} transition={{ duration: 1.1, ease, delay: 0.3 }} className="mr-[0.02em] inline-block">
      <Symbol className="h-[0.74em] w-[0.74em]" sun="var(--ink)" sea="#F0285F" foam="#A8F0DC" />
    </motion.span>
    {LETTERS.map((l, i) => (
      <motion.span key={i} initial={{ y: "110%" }} animate={{ y: 0 }} transition={{ duration: 0.9, ease, delay: 0.45 + i * 0.07 }} className="inline-block">
        {l}
      </motion.span>
    ))}
  </h1>
);

const Plane = () => (
  <div className="absolute inset-x-0 bottom-0 h-[44%]">
    <svg viewBox="0 0 1440 60" preserveAspectRatio="none" className="absolute -top-[59px] h-[60px] w-[200%] wave-move-slow">
      <path d="M0 30 Q90 0 180 30 T360 30 T540 30 T720 30 T900 30 T1080 30 T1260 30 T1440 30 V60 H0Z" fill="#F0285F" />
    </svg>
    <div className="h-full w-full bg-[#F0285F]" />
  </div>
);

export default function Hero() {
  const ref = useRef(null);
  const { scrollYProgress } = useScroll({ target: ref, offset: ["start start", "end start"] });
  const wordY = useTransform(scrollYProgress, [0, 1], [0, -160]);
  const dishRot = useTransform(scrollYProgress, [0, 1], [0, 45]);
  const dishY = useTransform(scrollYProgress, [0, 1], [0, 140]);
  const oliX = useTransform(scrollYProgress, [0, 1], [0, 220]);

  return (
    <ThemedSection id="inicio" theme={THEMES.hero} className="relative min-h-[100svh] overflow-hidden">
      <div ref={ref} className="relative min-h-[100svh]">
        <Plane />
        <div className="relative z-10 mx-auto max-w-[1500px] px-5 pt-28 md:px-10 md:pt-32">
          <motion.p initial={{ opacity: 0, y: 12 }} animate={{ opacity: 1, y: 0 }} transition={{ delay: 0.2 }} className="overline mb-3 flex items-center gap-3">
            <span className="h-2 w-2 rounded-full bg-[#F0285F]" /> Cocina mediterránea · Alcoy (Alicante)
          </motion.p>
          <motion.div style={{ y: wordY }}>
            <Wordmark />
          </motion.div>
          <div className="mt-4 grid gap-6 md:mt-6 md:grid-cols-12">
            <motion.div initial={{ opacity: 0, y: 20 }} animate={{ opacity: 1, y: 0 }} transition={{ delay: 1, duration: 0.8, ease }} className="md:col-span-5">
              <p className="font-display text-3xl leading-[0.95] md:text-5xl">Cinco orillas.<br />Una sola mesa.</p>
              <p className="mt-4 max-w-sm text-base font-medium leading-relaxed opacity-80">Del Egeo al Magreb sin levantarte de la silla. Cada cocina, un mundo. Cada mundo, un personaje.</p>
              <div className="mt-6 flex flex-wrap gap-3">
                <motion.button whileTap={{ scale: 0.95 }} data-testid="hero-start-journey-btn" onClick={() => scrollToId("manifiesto")} className="group flex items-center gap-2 rounded-full bg-ink px-6 py-3.5 font-bold text-[#A8F0DC] transition-transform duration-300 hover:-translate-y-1">
                  Empezar el viaje <ArrowDown className="h-4 w-4 transition-transform duration-300 group-hover:translate-y-1" />
                </motion.button>
                <motion.button whileTap={{ scale: 0.95 }} data-testid="hero-reserve-btn" onClick={() => scrollToId("visita")} className="rounded-full border-2 border-ink px-6 py-3.5 font-bold transition-colors duration-300 hover:bg-ink hover:text-[#A8F0DC]">
                  Reservar mesa
                </motion.button>
              </div>
            </motion.div>
          </div>
        </div>

        <motion.div style={{ rotate: dishRot, y: dishY }} initial={{ opacity: 0, scale: 0.6 }} animate={{ opacity: 1, scale: 1 }} transition={{ delay: 0.9, duration: 1.2, ease }} className="absolute -bottom-[4%] left-[10%] z-10 w-[80vw] max-w-[600px] md:left-[54%] md:w-[36vw]">
          <img src="/img/d_berenjena.webp" alt="Berenjena asada con yogur de limón, miel y avellanas" className="drop w-full" data-testid="hero-dish-img" />
        </motion.div>

        <motion.div style={{ x: oliX }} className="absolute bottom-[8%] right-[3%] z-20 hidden h-[34vh] w-[24vh] md:block">
          <Bubble testId="hero-oli-bubble" className="-left-40 -top-6">¡Hola! Soy {HOST.name}. ¿Viajamos?</Bubble>
          <Character src={HOST.img} alt={HOST.name} className="h-full w-full" testId="hero-oli-character" />
        </motion.div>
      </div>
    </ThemedSection>
  );
}
