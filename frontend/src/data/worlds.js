export const THEMES = {
  hero: { bg: "#A8F0DC", ink: "#0B1F17", accent: "#F0285F" },
  manifesto: { bg: "#0B1F17", ink: "#A8F0DC", accent: "#F0285F" },
  cast: { bg: "#FFF4E2", ink: "#14110C", accent: "#F0285F" },
  casa: { bg: "#F0285F", ink: "#FFF4EC", accent: "#FFD23F" },
  visit: { bg: "#0B1F17", ink: "#FFF4E2", accent: "#A8F0DC" },
};

export const WORLDS = [
  {
    id: "egeo",
    num: "01",
    word: "EGEO",
    country: "Grecia",
    title: "El Egeo",
    theme: { bg: "#1F44D6", ink: "#FFFFFF", accent: "#FFD23F" },
    intro: "Islas blancas, aceite verde y una sobremesa que se alarga con el sol. Aquí el queso se sirve entero y el orégano manda.",
    chips: ["Feta entera", "Orégano", "Kalamata", "Miel de tomillo"],
    char: { img: "/img/feta.webp", name: "Feta", role: "El filósofo del sol", quote: "Primero el aceite. Después, la conversación." },
    dishImg: "/img/d_horiatiki.webp",
    dishes: [
      { name: "Horiatiki con feta entera", desc: "Tomate, pepino, cebolla roja, kalamata y orégano.", price: "11,50 €" },
      { name: "Pulpo a la brasa con fava", desc: "Puré de guisante amarillo, alcaparras y limón.", price: "19,00 €" },
      { name: "Yogur griego con miel de tomillo", desc: "Con nueces tostadas.", price: "6,00 €" },
    ],
  },
  {
    id: "tirreno",
    num: "02",
    word: "TIRRENO",
    country: "Italia",
    title: "El Tirreno",
    theme: { bg: "#E8233A", ink: "#FFF4E2", accent: "#7CE0A3" },
    intro: "Tomate de verdad, albahaca recién cortada y la pasta en su punto. Un mantel de cuadros imaginario y mucha gesticulación.",
    chips: ["Pomodoro", "Albahaca", "Burrata", "Al dente"],
    char: { img: "/img/pomodoro.webp", name: "Don Pomodoro", role: "El apasionado", quote: "¿Nata en la carbonara? Ma che dici…" },
    dishImg: "/img/d_pasta.webp",
    dishes: [
      { name: "Spaghetti al pomodoro y albahaca", desc: "Salsa de tomate lenta y parmesano.", price: "14,00 €" },
      { name: "Burrata con tomates asados", desc: "Pan tostado y aceite de albahaca.", price: "12,50 €" },
      { name: "Tiramisù de la casa", desc: "Café espresso y cacao amargo.", price: "6,50 €" },
    ],
  },
  {
    id: "levante",
    num: "03",
    word: "LEVANTE",
    country: "España · nuestra casa",
    title: "El Levante",
    theme: { bg: "#FFB31F", ink: "#1A1205", accent: "#E8233A" },
    intro: "La orilla de casa. Arroz al horno en cassola de barro, verduras asadas y un horno que nunca se apaga en Alcoy.",
    chips: ["Arroz al horno", "Cassola de barro", "Horno", "Para el centro"],
    char: { img: "/img/cassola.webp", name: "Cassola", role: "La reina del domingo", quote: "El arroz, mínimo para dos. Las normas son las normas." },
    dishImg: "/img/d_arroz.webp",
    dishes: [
      { name: "Arroz al horno de verduras y garbanzos", desc: "Calabaza, pimiento y garbanzos. Mínimo 2 personas.", price: "16,00 € / persona" },
      { name: "Berenjena asada con yogur de limón", desc: "Miel y avellanas tostadas. Media ración o ración.", price: "9,50 € · 15,00 €" },
      { name: "Flan de café", desc: "Café y caramelo, porción individual.", price: "6,00 €" },
    ],
  },
  {
    id: "oriente",
    num: "04",
    word: "ORIENTE",
    country: "Líbano",
    title: "El Oriente",
    theme: { bg: "#0E8C66", ink: "#F7F3E8", accent: "#FF8AB3" },
    intro: "Mesas llenas de cuencos, pan caliente para mojar y nadie que se quede con hambre. Compartir aquí no es opcional, es amor.",
    chips: ["Hummus", "Za'atar", "Tahini", "Pan de pita"],
    char: { img: "/img/garbanzo.webp", name: "Garbanzo", role: "El anfitrión generoso", quote: "Toma más pan. No, insisto. Toma más pan." },
    dishImg: "/img/d_hummus.webp",
    dishes: [
      { name: "Hummus con aceite verde y piñones", desc: "Zumaque, pimentón y pita caliente.", price: "9,00 €" },
      { name: "Fattoush con pan crujiente", desc: "Hierbas, rabanito, granada y zumaque.", price: "10,50 €" },
      { name: "Kafta de cordero con tahini", desc: "A la brasa, con perejil y limón.", price: "17,00 €" },
    ],
  },
  {
    id: "magreb",
    num: "05",
    word: "MAGREB",
    country: "Marruecos",
    title: "El Magreb",
    theme: { bg: "#5B2BD9", ink: "#FFFFFF", accent: "#FF8A1F" },
    intro: "Especias que viajan en caravana, cocciones lentas bajo una tapa cónica y un final dulce de azahar.",
    chips: ["Ras el hanout", "Limón confitado", "Cuscús", "Azahar"],
    char: { img: "/img/tajin.webp", name: "Sultán Tajín", role: "El maestro de lo lento", quote: "La prisa no cabe bajo mi sombrero." },
    dishImg: "/img/d_tajin.webp",
    dishes: [
      { name: "Tajín de pollo, limón confitado y aceitunas", desc: "Azafrán, jengibre y cilantro.", price: "18,00 €" },
      { name: "Cuscús de siete verduras", desc: "Garbanzos, pasas y caldo especiado.", price: "15,00 €" },
      { name: "Naranja con canela y agua de azahar", desc: "Fresca y perfumada.", price: "5,50 €" },
    ],
  },
];

export const HOST = { img: "/img/oli.webp", name: "Oli", role: "Tu anfitrión de orilla en orilla" };

export const HOURS = [
  { day: "Lunes", local: "Cerrado", kitchen: "Cerrada" },
  { day: "Martes a jueves y domingo", local: "12:30–17:00", kitchen: "13:00–15:30" },
  { day: "Viernes y sábado", local: "12:30–17:00 · 19:30–23:00", kitchen: "13:00–15:30 · 20:00–22:00" },
];
