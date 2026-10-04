import { WORLDS } from "../data/worlds";

const Star = () => (
  <svg viewBox="0 0 24 24" className="mx-6 inline-block h-[0.6em] w-[0.6em]" aria-hidden="true">
    <path d="M12 0 C13 8 16 11 24 12 C16 13 13 16 12 24 C11 16 8 13 0 12 C8 11 11 8 12 0Z" fill="currentColor" />
  </svg>
);

export default function Marquee() {
  const items = [...WORLDS, ...WORLDS];
  return (
    <div className="relative z-10 overflow-x-clip py-8">
    <div className="-rotate-2 bg-[#F0285F] py-5 text-[#FFF4E2]" data-testid="worlds-marquee">
      <div className="marquee flex w-max whitespace-nowrap font-display text-4xl md:text-6xl">
        {items.map((w, i) => (
          <span key={i} className="flex items-center">
            {w.country.split(" ·")[0]}
            <Star />
          </span>
        ))}
      </div>
    </div>
    </div>
  );
}
