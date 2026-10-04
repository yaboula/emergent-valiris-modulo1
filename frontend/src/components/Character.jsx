import { motion, useReducedMotion } from "framer-motion";

export default function Character({ src, alt, className = "", delay = 0, testId }) {
  const reduce = useReducedMotion();
  return (
    <motion.div
      className={className}
      animate={reduce ? undefined : { y: [0, -14, 0], rotate: [-2, 2, -2] }}
      transition={{ duration: 3.4, repeat: Infinity, ease: "easeInOut", delay }}
    >
      <motion.img
        data-testid={testId}
        src={src}
        alt={alt}
        draggable={false}
        whileHover={{ scale: 1.08, rotate: [0, -8, 8, -4, 0], transition: { duration: 0.6 } }}
        whileTap={{ scale: 0.92 }}
        className="drop h-full w-full cursor-grab select-none object-contain"
      />
    </motion.div>
  );
}

export const Bubble = ({ children, className = "", testId }) => (
  <motion.div
    data-testid={testId}
    initial={{ scale: 0, opacity: 0, rotate: -12 }}
    whileInView={{ scale: 1, opacity: 1, rotate: -3 }}
    viewport={{ once: false, amount: 0.6 }}
    transition={{ type: "spring", stiffness: 260, damping: 16, delay: 0.25 }}
    className={`absolute z-20 w-max max-w-[260px] rounded-[28px] bg-paper px-5 py-4 font-display text-lg leading-tight tracking-tight text-coal shadow-[0_12px_0_rgba(0,0,0,0.18)] ${className}`}
  >
    {children}
    <span className="absolute -bottom-2 left-8 h-5 w-5 rotate-45 rounded-sm bg-paper" />
  </motion.div>
);
