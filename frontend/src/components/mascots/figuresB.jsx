import { motion } from "framer-motion";
import { Eye, Mouth, Cheeks, Shadow, Leg, Arm, INK, useFig } from "./parts";

const Star8 = ({ x, y, s = 5, fill = "#F2C84B" }) => (
  <g transform={`translate(${x} ${y})`} fill={fill}>
    <rect x={-s} y={-s} width={s * 2} height={s * 2} />
    <rect x={-s} y={-s} width={s * 2} height={s * 2} transform="rotate(45)" />
  </g>
);

export const Cassola = () => {
  const { uid } = useFig();
  return (
    <>
      <defs>
        <pattern id={`ging-${uid}`} width={10} height={10} patternUnits="userSpaceOnUse">
          <rect width={10} height={10} fill="#fff" />
          <rect width={5} height={10} fill="#2B5BB8" opacity={0.55} />
          <rect width={10} height={5} fill="#2B5BB8" opacity={0.55} />
        </pattern>
      </defs>
      <Shadow rx={62} />
      <Leg x1={82} y1={194} x2={76} dir={-1} />
      <Leg x1={118} y1={194} x2={124} />
      <Arm d="M34 150 Q8 160 14 184" glove={[14, 188]} />
      <Arm d="M166 150 Q190 140 190 116" glove={[190, 112]} dUp="M166 146 Q196 124 192 86" gloveUp={[192, 82]}>
        <path d="M2 -4 L8 -48" stroke="#B88746" strokeWidth={5} strokeLinecap="round" />
        <ellipse cx={9} cy={-54} rx={8} ry={12} fill="#C99A5A" stroke="#8A6330" strokeWidth={2} />
      </Arm>
      <ellipse cx={24} cy={106} rx={14} ry={9} fill="#A9481F" />
      <ellipse cx={176} cy={106} rx={14} ry={9} fill="#A9481F" />
      <path d="M26 98 Q28 198 100 198 Q172 198 174 98 Z" fill="#D06A35" />
      <path d="M150 104 Q172 104 172 112 Q166 186 112 196 Q156 170 150 104 Z" fill="#B4532A" />
      <ellipse cx={100} cy={98} rx={76} ry={16} fill="#B9532A" />
      <ellipse cx={100} cy={96} rx={66} ry={11} fill="#F2B33D" />
      <g>
        <circle cx={70} cy={95} r={6} fill="#E8433A" /><circle cx={128} cy={98} r={6} fill="#E8433A" />
        <ellipse cx={100} cy={90} rx={9} ry={7} fill="#FFF4E2" stroke="#E2CDA8" strokeWidth={2} />
        <circle cx={86} cy={100} r={3.5} fill="#E7C27A" /><circle cx={112} cy={102} r={3.5} fill="#E7C27A" /><circle cx={146} cy={94} r={3.5} fill="#E7C27A" />
        <rect x={50} y={95} width={10} height={4} rx={2} fill="#2FA35A" transform="rotate(-20 55 97)" />
      </g>
      <path d="M30 114 Q100 136 170 114 L170 128 Q100 150 30 128 Z" fill={`url(#ging-${uid})`} stroke={INK} strokeWidth={2.5} strokeLinejoin="round" />
      <path d="M150 126 L166 146 L152 148 Z M154 124 L174 138 L162 146 Z" fill={`url(#ging-${uid})`} stroke={INK} strokeWidth={2.5} strokeLinejoin="round" />
      <circle cx={152} cy={128} r={6} fill="#2B5BB8" stroke={INK} strokeWidth={2.5} />
      <Eye cx={80} cy={154} r={13} />
      <Eye cx={120} cy={154} r={13} />
      <Cheeks l={60} r={140} y={174} />
      <Mouth cx={100} cy={172} w={28} />
    </>
  );
};

export const Garbanzo = () => (
  <>
    <Shadow />
    <Leg x1={86} y1={190} x2={80} dir={-1} />
    <Leg x1={114} y1={190} x2={120} />
    <Arm d="M40 142 Q14 154 20 178" glove={[20, 182]} />
    <Arm d="M160 142 Q186 150 186 132" glove={[186, 128]} dUp="M160 138 Q192 118 190 84" gloveUp={[190, 80]}>
      <ellipse cx={-8} cy={-14} rx={22} ry={15} fill="#E8C07A" stroke="#B88746" strokeWidth={2} />
      <g fill="#C99A4E"><circle cx={-14} cy={-18} r={2.5} /><circle cx={-2} cy={-10} r={2.5} /><circle cx={-6} cy={-20} r={2} /></g>
    </Arm>
    <path d="M100 52 C150 50 172 92 168 132 C164 176 132 196 100 196 C64 196 34 172 34 128 C34 86 56 54 100 52 Z" fill="#E9C88A" />
    <path d="M120 56 Q134 44 130 64 Z" fill="#E9C88A" />
    <path d="M146 72 C176 110 164 176 118 194 C150 168 160 116 146 72 Z" fill="#D3AE6B" />
    <path d="M100 56 Q92 96 100 132" stroke="#D3AE6B" strokeWidth={3} fill="none" strokeLinecap="round" />
    <path d="M38 136 C40 176 66 196 100 196 C134 196 160 176 162 136 L120 150 L100 190 L80 150 Z" fill="#12324A" />
    <g fill="#F2C84B">
      {[[80, 152], [86, 164], [92, 176], [120, 152], [114, 164], [108, 176], [52, 160], [148, 160]].map(([x, y]) => <circle key={`${x}${y}`} cx={x} cy={y} r={2.6} />)}
    </g>
    <path d="M44 170 Q100 188 156 170" stroke="#C8102E" strokeWidth={6} fill="none" />
    <path d="M74 60 L80 28 Q100 22 120 28 L126 60 Q100 66 74 60 Z" fill="#C8102E" />
    <ellipse cx={100} cy={27} rx={20} ry={5} fill="#A00D24" />
    <motion.g animate={{ rotate: [-10, 14, -10] }} transition={{ duration: 2.4, repeat: Infinity, ease: "easeInOut" }} style={{ transformBox: "view-box", originX: "100px", originY: "26px" }}>
      <path d="M100 26 Q118 24 124 34" stroke={INK} strokeWidth={2.5} fill="none" />
      <path d="M120 34 L130 34 L132 54 L118 54 Z" fill={INK} />
    </motion.g>
    <Eye cx={82} cy={100} r={13} />
    <Eye cx={118} cy={100} r={13} />
    <Cheeks l={64} r={136} y={122} />
    <Mouth cx={100} cy={122} w={28} />
  </>
);

export const Tajin = () => (
  <>
    <Shadow rx={70} />
    <Leg x1={86} y1={196} x2={78} dir={-1} shoe="#F2C84B" babouche />
    <Leg x1={114} y1={196} x2={122} shoe="#F2C84B" babouche />
    <Arm d="M66 142 Q36 152 34 176" glove={[34, 180]} />
    <Arm d="M134 142 Q164 132 166 106" glove={[166, 102]} dUp="M134 138 Q170 116 172 80" gloveUp={[172, 76]}>
      <rect x={-3} y={-46} width={7} height={44} rx={3} fill="#8B4A22" transform="rotate(14)" />
      <Star8 x={-9} y={-50} s={4} fill="#FFD23F" />
    </Arm>
    <ellipse cx={100} cy={190} rx={80} ry={14} fill="#9C3E1F" />
    <ellipse cx={100} cy={182} rx={80} ry={10} fill="#B9532A" />
    <path d="M100 34 C110 34 112 50 116 70 C128 120 160 160 170 178 Q100 194 30 178 C40 160 72 120 84 70 C88 50 90 34 100 34 Z" fill="#D06A35" />
    <path d="M112 50 C124 110 156 156 170 178 Q150 184 128 186 C150 160 124 100 112 50 Z" fill="#B4532A" />
    <path d="M52 150 Q100 164 148 150 L160 168 Q100 184 40 168 Z" fill="#12A3A3" />
    {[[66, 162], [100, 170], [134, 162]].map(([x, y]) => <Star8 key={x} x={x} y={y} s={4.5} />)}
    <path d="M86 82 Q100 88 114 82" stroke="#F2C84B" strokeWidth={4} fill="none" strokeLinecap="round" />
    <circle cx={100} cy={32} r={8} fill="#9C3E1F" />
    <motion.path d="M100 22 Q92 14 100 6 Q108 -2 100 -10" stroke="#fff" strokeWidth={3.5} fill="none" strokeLinecap="round" opacity={0.75} animate={{ pathLength: [0, 1, 1], opacity: [0, 0.8, 0] }} transition={{ duration: 2.6, repeat: Infinity }} />
    <Eye cx={88} cy={112} r={11} />
    <Eye cx={112} cy={112} r={11} />
    <path d="M78 100 L96 104 M122 100 L104 104" stroke={INK} strokeWidth={3.5} strokeLinecap="round" />
    <Cheeks l={74} r={126} y={132} />
    <Mouth cx={100} cy={130} w={20} />
  </>
);
