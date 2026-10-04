import { useRef } from "react";
import { motion, useScroll, useTransform } from "framer-motion";
import { ThemedSection } from "../lib/active";
import { THEMES } from "../data/worlds";

const TEXT = "El Mediterráneo no es un mar. Es una mesa larga con cinco orillas. Nosotros ponemos la nuestra en Alcoy, encendemos el horno y os invitamos a sentaros.";
const HIGHLIGHT = ["mesa", "larga", "cinco", "orillas.", "horno"];

const Word = ({ word, progress, range }) => {
  const opacity = useTransform(progress, range, [0.14, 1]);
  const hl = HIGHLIGHT.includes(word);
  return (
    <motion.span style={{ opacity }} className={`mr-[0.22em] inline-block ${hl ? "text-accent" : ""}`}>
      {word}
    </motion.span>
  );
};

export default function Manifesto() {
  const ref = useRef(null);
  const { scrollYProgress } = useScroll({ target: ref, offset: ["start start", "end end"] });
  const words = TEXT.split(" ");
  return (
    <ThemedSection id="manifiesto" theme={THEMES.manifesto} className="relative">
      <div ref={ref} className="relative h-[220vh]">
        <div className="sticky top-0 flex h-screen items-center">
          <div className="mx-auto max-w-6xl px-5 md:px-10">
            <p className="overline mb-8 opacity-70">Manifiesto · 00</p>
            <p data-testid="manifesto-text" className="font-display text-[clamp(2.2rem,5.6vw,5.4rem)] leading-[0.98]">
              {words.map((w, i) => (
                <Word key={i} word={w} progress={scrollYProgress} range={[i / words.length * 0.85, (i + 1) / words.length * 0.85]} />
              ))}
            </p>
          </div>
        </div>
      </div>
    </ThemedSection>
  );
}
