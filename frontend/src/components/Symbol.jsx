import { useId } from "react";

const WAVE = "M0 50 Q12.5 40 25 50 T50 50 T75 50 T100 50 T125 50 T150 50 T175 50 T200 50 V100 H0Z";

// Sun over the shore: the "O" of ORILLA
export default function Symbol({ className = "", sun = "currentColor", sea = "var(--accent)", foam = "var(--bg)" }) {
  const id = useId().replace(/:/g, "");
  return (
    <svg viewBox="0 0 100 100" className={className} aria-hidden="true">
      <defs>
        <clipPath id={`c${id}`}>
          <circle cx="50" cy="50" r="49" />
        </clipPath>
      </defs>
      <g clipPath={`url(#c${id})`}>
        <rect width="100" height="100" fill={sun} />
        <g className="wave-move" style={{ transform: "translateY(6px)" }}>
          <path d={WAVE} fill={sea} transform="translate(0 6)" />
        </g>
        <g className="wave-move-slow">
          <path d={WAVE} fill={foam} transform="translate(0 26)" />
        </g>
      </g>
    </svg>
  );
}

export const Logo = ({ className = "" }) => (
  <span className={`inline-flex items-center gap-1.5 font-display text-2xl leading-none ${className}`}>
    <Symbol className="h-[0.8em] w-[0.8em]" />
    <span>RILLA</span>
  </span>
);
