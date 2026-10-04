import { motion } from "framer-motion";
import { Eye, Mouth, Cheeks, Shadow, Leg, Arm, INK, useFig } from "./parts";

export const Oli = () => (
  <>
    <Shadow />
    <Leg x1={86} y1={186} x2={80} dir={-1} />
    <Leg x1={114} y1={186} x2={120} />
    <motion.g animate={{ rotate: [0, -14, 0, -14, 0] }} transition={{ duration: 1.6, repeat: Infinity, repeatDelay: 1.4 }} style={{ transformBox: "view-box", originX: "46px", originY: "130px" }}>
      <Arm d="M46 130 Q18 118 22 82" glove={[22, 78]} />
    </motion.g>
    <Arm d="M154 136 Q180 150 174 174" glove={[174, 178]} dUp="M154 132 Q186 116 188 82" gloveUp={[188, 78]}>
      <path d="M-12 4 L10 0 L14 26 L-6 30 Z" fill="#fff" stroke={INK} strokeWidth={2.5} />
    </Arm>
    <ellipse cx={100} cy={122} rx={60} ry={74} fill="#8DB33A" />
    <path d="M122 52 A60 74 0 0 1 122 192 A46 66 0 0 0 122 52 Z" fill="#6E9128" />
    <ellipse cx={72} cy={80} rx={10} ry={18} fill="#fff" opacity={0.35} transform="rotate(-24 72 80)" />
    <path d="M100 50 Q101 38 108 30" stroke="#5B3F1E" strokeWidth={5} strokeLinecap="round" fill="none" />
    <path d="M106 32 Q130 6 158 18 Q136 42 106 32 Z" fill="#3F8A3A" />
    <path d="M110 31 Q132 22 152 20" stroke="#2C6A2A" strokeWidth={2} fill="none" />
    <Eye cx={81} cy={104} r={14} />
    <Eye cx={119} cy={104} r={14} />
    <Cheeks l={64} r={136} y={128} />
    <Mouth cx={100} cy={130} w={28} />
    <path d="M82 154 L100 164 L90 176 Z M118 154 L100 164 L110 176 Z" fill="#fff" stroke={INK} strokeWidth={2} strokeLinejoin="round" />
    <path d="M100 166 L80 156 L82 180 Z M100 166 L120 156 L118 180 Z" fill="#F0285F" stroke={INK} strokeWidth={2.5} strokeLinejoin="round" />
    <circle cx={100} cy={167} r={5.5} fill="#B5123F" stroke={INK} strokeWidth={2.5} />
  </>
);

export const Feta = () => {
  const { uid } = useFig();
  return (
    <>
      <defs>
        <clipPath id={`feta-${uid}`}><rect x={40} y={74} width={120} height={122} rx={24} /></clipPath>
      </defs>
      <Shadow />
      <Leg x1={82} y1={192} x2={78} dir={-1} />
      <Leg x1={118} y1={192} x2={122} />
      <Arm d="M44 142 Q18 152 24 178" glove={[24, 182]} />
      <Arm d="M156 142 Q182 134 186 108" glove={[186, 104]} dUp="M156 138 Q190 118 190 80" gloveUp={[190, 76]}>
        <path d="M2 -6 L12 -40" stroke="#5B4A2A" strokeWidth={3.5} strokeLinecap="round" />
        <g fill="#6E9128">
          <ellipse cx={0} cy={-22} rx={4} ry={8} transform="rotate(-40 0 -22)" />
          <ellipse cx={14} cy={-28} rx={4} ry={8} transform="rotate(40 14 -28)" />
          <ellipse cx={8} cy={-42} rx={4} ry={8} transform="rotate(10 8 -42)" />
        </g>
        <circle cx={10} cy={-16} r={4} fill="#3A2A4A" />
      </Arm>
      <g clipPath={`url(#feta-${uid})`}>
        <rect x={40} y={74} width={120} height={122} fill="#FFFDF5" />
        <rect x={136} y={74} width={30} height={122} fill="#ECE4CF" />
        {[154, 168, 182].map((y) => <rect key={y} x={40} y={y} width={120} height={7} fill="#1F44D6" />)}
        <g fill="#E9E0C8">
          <circle cx={58} cy={92} r={3} /><circle cx={142} cy={132} r={4} /><circle cx={66} cy={138} r={2.5} />
        </g>
      </g>
      <path d="M58 74 Q56 40 100 38 Q146 40 144 74 Z" fill="#1B2E6B" />
      <path d="M60 68 Q100 78 142 68" stroke="#F2C84B" strokeWidth={4} fill="none" strokeDasharray="5 3" />
      <path d="M48 80 Q100 94 152 80 L150 72 Q100 86 50 72 Z" fill="#0E1A40" />
      <circle cx={100} cy={50} r={4} fill="#F2C84B" />
      <Eye cx={80} cy={112} r={13} />
      <Eye cx={120} cy={112} r={13} />
      <path d="M68 94 Q80 88 92 94 M108 94 Q120 88 132 94" stroke={INK} strokeWidth={3.5} strokeLinecap="round" fill="none" />
      <Cheeks l={62} r={138} y={132} />
      <Mouth cx={100} cy={132} w={30} />
    </>
  );
};

export const Pomodoro = () => {
  const { uid } = useFig();
  return (
    <>
      <defs>
        <clipPath id={`tri-${uid}`}><path d="M74 166 L126 166 L100 200 Z" /></clipPath>
      </defs>
      <Shadow />
      <Leg x1={86} y1={190} x2={80} dir={-1} />
      <Leg x1={114} y1={190} x2={120} />
      <Arm d="M40 134 Q14 148 20 172" glove={[20, 176]}>
        <path d="M-2 -6 L-8 -48" stroke="#9AA0A6" strokeWidth={3.5} strokeLinecap="round" />
        <circle cx={-9} cy={-54} r={9} fill="none" stroke="#F2C84B" strokeWidth={4} />
        <circle cx={-9} cy={-54} r={4} fill="none" stroke="#F2C84B" strokeWidth={3} />
      </Arm>
      <Arm d="M160 132 Q186 120 184 94" glove={[184, 90]} dUp="M160 128 Q192 108 188 74" gloveUp={[188, 70]}>
        <path d="M-6 -8 Q0 -22 6 -8" fill="#fff" stroke={INK} strokeWidth={2.5} />
      </Arm>
      <circle cx={100} cy={128} r={66} fill="#E8233A" />
      <path d="M128 68 A66 66 0 0 1 128 188 A52 60 0 0 0 128 68 Z" fill="#C41629" />
      <ellipse cx={70} cy={92} rx={10} ry={18} fill="#fff" opacity={0.3} transform="rotate(-30 70 92)" />
      <g fill="#2FA35A">
        {[-60, -25, 10, 45].map((a) => <ellipse key={a} cx={100} cy={58} rx={7} ry={18} transform={`rotate(${a} 100 70)`} />)}
      </g>
      <g transform="rotate(-10 100 50)">
        <ellipse cx={100} cy={60} rx={48} ry={10} fill="#E9B949" stroke="#B8892A" strokeWidth={2} />
        <path d="M74 58 L76 30 Q100 24 124 30 L126 58 Q100 64 74 58 Z" fill="#F2C84B" stroke="#B8892A" strokeWidth={2} />
        <path d="M75 50 Q100 56 125 50 L125 42 Q100 48 75 42 Z" fill="#1E3A8A" />
      </g>
      <Eye cx={80} cy={108} r={13} />
      <Eye cx={120} cy={108} r={13} />
      <path d="M100 132 Q86 122 72 130 Q64 140 74 142 Q80 132 100 138 Q120 132 126 142 Q136 140 128 130 Q114 122 100 132 Z" fill={INK} />
      <Mouth cx={100} cy={146} w={18} />
      <Cheeks l={64} r={136} y={128} />
      <g clipPath={`url(#tri-${uid})`}>
        <rect x={74} y={166} width={18} height={36} fill="#1E9E57" />
        <rect x={92} y={166} width={16} height={36} fill="#fff" />
        <rect x={108} y={166} width={18} height={36} fill="#F6A1A9" />
      </g>
      <path d="M74 166 L126 166 L100 200 Z" fill="none" stroke={INK} strokeWidth={2.5} strokeLinejoin="round" />
    </>
  );
};
