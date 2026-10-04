import { createContext, useContext, useEffect, useRef, useState } from "react";
import { useInView } from "framer-motion";

const ActiveCtx = createContext({ active: "inicio", setActive: () => {} });

export const ActiveProvider = ({ children }) => {
  const [active, setActive] = useState("inicio");
  return <ActiveCtx.Provider value={{ active, setActive }}>{children}</ActiveCtx.Provider>;
};

export const useActive = () => useContext(ActiveCtx);

const applyTheme = (t) => {
  const s = document.documentElement.style;
  s.setProperty("--bg", t.bg);
  s.setProperty("--ink", t.ink);
  s.setProperty("--accent", t.accent);
};

export const ThemedSection = ({ id, theme, className = "", children, ...rest }) => {
  const ref = useRef(null);
  const inView = useInView(ref, { margin: "-50% 0px -50% 0px" });
  const { setActive } = useActive();

  useEffect(() => {
    if (!inView) return;
    applyTheme(theme);
    setActive(id);
  }, [inView, theme, id, setActive]);

  return (
    <section ref={ref} id={id} data-testid={`section-${id}`} className={className} {...rest}>
      {children}
    </section>
  );
};
