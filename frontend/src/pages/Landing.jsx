import { useEffect } from "react";
import { useLocation } from "react-router-dom";
import { WORLDS } from "../data/worlds";
import { scrollToId } from "../lib/scroll";
import Hero from "../components/Hero";
import Manifesto from "../components/Manifesto";
import Marquee from "../components/Marquee";
import World from "../components/World";
import RouteTracker from "../components/RouteTracker";
import Cast from "../components/Cast";
import Casa from "../components/Casa";
import Visit from "../components/Visit";
import Footer from "../components/Footer";
import { MesaButton } from "../components/carta/Mesa";

export default function Landing() {
  const { hash } = useLocation();

  useEffect(() => {
    if (!hash) return;
    const t = setTimeout(() => scrollToId(hash.slice(1)), 450);
    return () => clearTimeout(t);
  }, [hash]);

  return (
    <>
      <main>
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
      <MesaButton />
    </>
  );
}
