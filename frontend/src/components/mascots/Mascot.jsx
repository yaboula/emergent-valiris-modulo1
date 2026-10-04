import MascotSvg from "./parts";
import { Oli, Feta, Pomodoro } from "./figuresA";
import { Cassola, Garbanzo, Tajin } from "./figuresB";

const FIGURES = { oli: Oli, feta: Feta, pomodoro: Pomodoro, cassola: Cassola, garbanzo: Garbanzo, tajin: Tajin };

export default function Mascot({ id, ...props }) {
  return <MascotSvg Figure={FIGURES[id]} {...props} />;
}
