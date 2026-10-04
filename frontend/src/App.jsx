import { useEffect } from "react";
import Lenis from "lenis";
import { ActiveProvider } from "./lib/active";
import { setLenis } from "./lib/scroll";
import { WORLDS } from "./data/worlds";
import Nav from "./components/Nav";
import Hero from "./components/Hero";
import Manifesto from "./components/Manifesto";
import Marquee from "./components/Marquee";
import World from "./components/World";
import RouteTracker from "./components/RouteTracker";
import Cast from "./components/Cast";
import Casa from "./components/Casa";
import Visit from "./components/Visit";
import Footer from "./components/Footer";

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

export default function App() {
  useSmoothScroll();
  return (
    <ActiveProvider>
      <div className="grain relative">
        <Nav />
        <main className="overflow-x-clip">
          <Hero />
          <Manifesto />
          <Marquee />
          {WORLDS.map((w) => <World key={w.id} w={w} />)}
          <Cast />
          <Casa />
          <Visit />
          <Footer />
        </main>
        <RouteTracker />
      </div>
    </ActiveProvider>
  );
}
