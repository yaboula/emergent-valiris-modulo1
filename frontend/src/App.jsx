import { useEffect } from "react";
import { BrowserRouter, Routes, Route, useLocation } from "react-router-dom";
import Lenis from "lenis";
import { ActiveProvider } from "./lib/active";
import { MesaProvider } from "./lib/mesa";
import { setLenis, getLenis } from "./lib/scroll";
import Nav from "./components/Nav";
import Landing from "./pages/Landing";
import Carta from "./pages/Carta";
import { MesaDrawer } from "./components/carta/Mesa";

const useSmoothScroll = () => {
  useEffect(() => {
    if (window.matchMedia("(prefers-reduced-motion: reduce)").matches) return;
    const lenis = new Lenis({ lerp: 0.09 });
    setLenis(lenis);
    let id;
    const raf = (t) => {
      lenis.raf(t);
      id = requestAnimationFrame(raf);
    };
    id = requestAnimationFrame(raf);
    return () => {
      cancelAnimationFrame(id);
      lenis.destroy();
      setLenis(null);
    };
  }, []);
};

const ScrollReset = () => {
  const { pathname } = useLocation();
  useEffect(() => {
    const l = getLenis();
    if (l) l.scrollTo(0, { immediate: true });
    else window.scrollTo(0, 0);
  }, [pathname]);
  return null;
};

export default function App() {
  useSmoothScroll();
  return (
    <BrowserRouter future={{ v7_startTransition: true, v7_relativeSplatPath: true }}>
      <ActiveProvider>
        <MesaProvider>
          <ScrollReset />
          <div className="grain relative">
            <Nav />
            <Routes>
              <Route path="/" element={<Landing />} />
              <Route path="/carta" element={<Carta />} />
              <Route path="*" element={<Landing />} />
            </Routes>
            <MesaDrawer />
          </div>
        </MesaProvider>
      </ActiveProvider>
    </BrowserRouter>
  );
}
