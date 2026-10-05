import { useRef } from "react";
import { motion, useScroll, useTransform } from "framer-motion";
import { ThemedSection } from "../lib/active";
import Character, { Bubble } from "./Character";
import MenuTicket from "./MenuTicket";

const ease = [0.22, 1, 0.36, 1];
const reveal = {
  hidden: { opacity: 0, y: 40 },
  show: (i) => ({ opacity: 1, y: 0, transition: { duration: 0.8, ease, delay: i * 0.08 } }),
};

const Reveal = ({ items }) =>
  items.map((el, i) => (
    <motion.div key={i} variants={reveal} custom={i} initial="hidden" whileInView="show" viewport={{ once: true, amount: 0.3 }}>
      {el}
    </motion.div>
  ));

const Head = ({ w }) => (
  <div className="[grid-area:head] lg:self-end">
    <Reveal items={[
      <p key="o" className="kicker flex items-center gap-3">
        <span className="rounded-full bg-[color:var(--ink)] px-3 py-1 text-[color:var(--bg)]">Orilla {w.num} / 05</span>
        {w.country}
      </p>,
      <h2 key="h" data-testid={`world-title-${w.id}`} className="font-display mt-4 text-[clamp(3.2rem,7vw,6.5rem)] leading-[0.86] md:mt-5">{w.title}</h2>,
    ]} />
  </div>
);

const Body = ({ w }) => (
  <div className="[grid-area:body] lg:self-start">
    <Reveal items={[
      <p key="p" className="max-w-md lg:mt-5 text-base font-medium leading-relaxed opacity-90 md:text-lg">{w.intro}</p>,
      <div key="c" className="mt-6 flex flex-wrap gap-2">
        {w.chips.map((c) => (
          <span key={c} className="rounded-full border-2 border-current px-3.5 py-1 text-sm font-semibold">{c}</span>
        ))}
      </div>,
      <MenuTicket key="m" w={w} />,
    ]} />
  </div>
);

export default function World({ w }) {
  const ref = useRef(null);
  const { scrollYProgress } = useScroll({ target: ref, offset: ["start end", "end start"] });
  const wordX = useTransform(scrollYProgress, [0, 1], ["25%", "-55%"]);
  const dishRot = useTransform(scrollYProgress, [0, 1], [-30, 30]);
  const dishScale = useTransform(scrollYProgress, [0.1, 0.42, 0.9], [0.55, 1, 0.85]);
  const charY = useTransform(scrollYProgress, [0.12, 0.4], [260, 0]);
  const charRot = useTransform(scrollYProgress, [0.12, 0.4], [25, 0]);

  return (
    <ThemedSection id={w.id} theme={w.theme}>
      <div ref={ref} className="relative lg:h-[140vh]">
        <div className="relative overflow-hidden py-16 lg:sticky lg:top-0 lg:flex lg:h-screen lg:items-center lg:py-0">
          <div aria-hidden="true" className="pointer-events-none absolute inset-x-0 top-1/2 hidden -translate-y-1/2 lg:block">
            <motion.div style={{ x: wordX }} className="outline-word font-display whitespace-nowrap text-[30vw] leading-[0.8] opacity-70">
              {w.word}
            </motion.div>
          </div>
          <div className="relative z-10 mx-auto grid w-full max-w-[1400px] gap-6 px-5 [grid-template-areas:'head'_'visual'_'body'] md:px-10 lg:grid-cols-[5fr_7fr] lg:gap-x-10 lg:gap-y-0 lg:[grid-template-areas:'head_visual'_'body_visual']">
            <Head w={w} />
            <Body w={w} />
            <div className="relative h-[380px] [grid-area:visual] md:h-[520px] lg:h-[78vh] lg:self-center">
              <motion.div style={{ rotate: dishRot, scale: dishScale }} className="absolute inset-0 flex items-center justify-center">
                <img src={w.dishImg} alt={w.dishes[0].name} data-testid={`world-dish-img-${w.id}`} className="drop max-h-full w-[88%] object-contain" />
              </motion.div>
              <motion.div style={{ y: charY, rotate: charRot }} className="absolute bottom-0 left-0 h-[54%] w-[40%] md:left-[0%]">
                <Bubble testId={`world-bubble-${w.id}`} className="-top-14 left-[55%] max-w-[210px] !px-4 !py-3 !text-[15px] md:-top-14 md:left-[60%] md:max-w-[260px] md:!px-5 md:!py-4 md:!text-lg">«{w.char.quote}»</Bubble>
                <Character mascot={w.char.id} present alt={w.char.name} className="h-full w-full" testId={`world-character-${w.id}`} />
              </motion.div>
            </div>
          </div>
        </div>
      </div>
    </ThemedSection>
  );
}
