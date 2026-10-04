import { createContext, useContext, useEffect, useId, useRef, useState } from "react";
import { animate, motion, useMotionValue, useSpring, useTransform } from "framer-motion";

export const INK = "#14110C";
const Ctx = createContext(null);
export const useFig = () => useContext(Ctx);

const useLook = (ref) => {
  const x = useSpring(0, { stiffness: 140, damping: 14 });
  const y = useSpring(0, { stiffness: 140, damping: 14 });
  useEffect(() => {
    if (!window.matchMedia("(hover: hover)").matches) {
      const id = setInterval(() => { x.set(Math.random() * 2 - 1); y.set(Math.random() * 1.2 - 0.6); }, 2400);
      return () => clearInterval(id);
    }
    const on = (e) => {
      const r = ref.current?.getBoundingClientRect();
      if (!r || r.bottom < 0 || r.top > window.innerHeight) return;
      const dx = e.clientX - (r.left + r.width / 2);
      const dy = e.clientY - (r.top + r.height * 0.42);
      const d = Math.hypot(dx, dy) || 1;
      const k = Math.min(d / 220, 1);
      x.set((dx / d) * k);
      y.set((dy / d) * k);
    };
    window.addEventListener("pointermove", on, { passive: true });
    return () => window.removeEventListener("pointermove", on);
  }, [ref, x, y]);
  return { x, y };
};

const useBlink = () => {
  const s = useMotionValue(1);
  useEffect(() => {
    let t;
    const loop = () => {
      t = setTimeout(() => {
        const twice = Math.random() < 0.25;
        animate(s, twice ? [1, 0.08, 1, 0.08, 1] : [1, 0.08, 1], { duration: twice ? 0.42 : 0.18 });
        loop();
      }, 1800 + Math.random() * 3800);
    };
    loop();
    return () => clearTimeout(t);
  }, [s]);
  return s;
};

export const Eye = ({ cx, cy, r = 13 }) => {
  const { look, blink } = useFig();
  const px = useTransform(look.x, (v) => v * r * 0.42);
  const py = useTransform(look.y, (v) => v * r * 0.42);
  return (
    <motion.g style={{ scaleY: blink, transformBox: "fill-box", transformOrigin: "center" }}>
      <circle cx={cx} cy={cy} r={r} fill="#fff" stroke={INK} strokeWidth={3} />
      <motion.g style={{ x: px, y: py }}>
        <circle cx={cx} cy={cy} r={r * 0.55} fill={INK} />
        <circle cx={cx - r * 0.2} cy={cy - r * 0.22} r={r * 0.19} fill="#fff" />
      </motion.g>
    </motion.g>
  );
};

export const Mouth = ({ cx, cy, w = 26 }) => {
  const { mood } = useFig();
  if (mood === "wow") return <ellipse cx={cx} cy={cy + w * 0.2} rx={w * 0.26} ry={w * 0.34} fill={INK} />;
  const d = `M${cx - w / 2} ${cy} Q${cx} ${cy + w * 0.8} ${cx + w / 2} ${cy} Z`;
  return (
    <g>
      <path d={d} fill={INK} strokeLinejoin="round" stroke={INK} strokeWidth={3} />
      <ellipse cx={cx} cy={cy + w * 0.36} rx={w * 0.2} ry={w * 0.12} fill="#F0285F" />
    </g>
  );
};

export const Cheeks = ({ l, r, y }) => (
  <g fill="#F0285F" opacity={0.42}>
    <ellipse cx={l} cy={y} rx={8} ry={5} />
    <ellipse cx={r} cy={y} rx={8} ry={5} />
  </g>
);

export const Shadow = ({ y = 228, rx = 52 }) => <ellipse cx={100} cy={y} rx={rx} ry={7} fill={INK} opacity={0.16} />;

export const Leg = ({ x1, y1, x2, y2 = 220, dir = 1, shoe = INK, babouche }) => (
  <g>
    <path d={`M${x1} ${y1} L${x2} ${y2}`} stroke={INK} strokeWidth={9} strokeLinecap="round" />
    {babouche ? (
      <path d={`M${x2 - 10 * dir} ${y2 - 4} Q${x2 + 4 * dir} ${y2 - 9} ${x2 + 20 * dir} ${y2 - 2} Q${x2 + 4 * dir} ${y2 + 7} ${x2 - 10 * dir} ${y2 + 5} Z`} fill={shoe} stroke={INK} strokeWidth={2.5} />
    ) : (
      <ellipse cx={x2 + 6 * dir} cy={y2 + 1} rx={13} ry={7} fill={shoe} />
    )}
  </g>
);

export const Arm = ({ d, dUp, glove, gloveUp, children }) => {
  const { present } = useFig();
  const g = present && gloveUp ? gloveUp : glove;
  return (
    <g>
      <motion.path initial={false} animate={{ d: present && dUp ? dUp : d }} transition={{ type: "spring", stiffness: 180, damping: 14 }} stroke={INK} strokeWidth={9} strokeLinecap="round" fill="none" />
      <motion.g initial={false} animate={{ x: g[0], y: g[1] }} transition={{ type: "spring", stiffness: 180, damping: 14 }}>
        <circle r={10} fill="#fff" stroke={INK} strokeWidth={3} />
        <circle cx={-7} cy={-5} r={4} fill="#fff" stroke={INK} strokeWidth={2.5} />
        {children}
      </motion.g>
    </g>
  );
};

export default function MascotSvg({ Figure, className = "", mood = "happy", present = false, label }) {
  const ref = useRef(null);
  const uid = useId().replace(/:/g, "");
  const look = useLook(ref);
  const blink = useBlink();
  const [hover, setHover] = useState(false);
  return (
    <svg ref={ref} viewBox="0 0 200 240" className={className} role="img" aria-label={label} onPointerEnter={() => setHover(true)} onPointerLeave={() => setHover(false)} style={{ overflow: "visible" }}>
      <Ctx.Provider value={{ look, blink, mood: hover ? "wow" : mood, present, uid }}>
        <Figure />
      </Ctx.Provider>
    </svg>
  );
}
