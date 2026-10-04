export const ALLERGENS = [
  { id: "gluten", label: "Gluten" },
  { id: "crustaceos", label: "Crustáceos" },
  { id: "huevo", label: "Huevo" },
  { id: "pescado", label: "Pescado" },
  { id: "cacahuetes", label: "Cacahuetes" },
  { id: "soja", label: "Soja" },
  { id: "leche", label: "Leche" },
  { id: "frutos", label: "Frutos de cáscara" },
  { id: "apio", label: "Apio" },
  { id: "mostaza", label: "Mostaza" },
  { id: "sesamo", label: "Sésamo" },
  { id: "sulfitos", label: "Sulfitos" },
  { id: "altramuces", label: "Altramuces" },
  { id: "moluscos", label: "Moluscos" },
];

export const CATEGORIES = [
  { id: "picar", label: "Para picar" },
  { id: "centro", label: "Para el centro" },
  { id: "principal", label: "Principales" },
  { id: "postre", label: "Postres" },
  { id: "bebida", label: "Bebidas" },
];

export const DIETS = [
  { id: "veg", label: "Vegetariano" },
  { id: "vegan", label: "Vegano" },
];

const one = (amount, label = "Plato individual") => [{ id: "u", label, amount }];

export const DISHES = [
  // Egeo
  { id: "eg-pita", world: "egeo", cat: "picar", name: "Pan pita con tzatziki", desc: "Pita caliente, yogur, pepino, ajo y eneldo.", prices: one(6.5, "Para compartir"), allergens: ["gluten", "leche"], diet: ["veg"], share: true },
  { id: "eg-spanako", world: "egeo", cat: "picar", name: "Spanakopita de espinacas y feta", desc: "Hojaldre filo crujiente relleno de espinacas, feta y eneldo.", prices: one(8), allergens: ["gluten", "leche", "huevo"], diet: ["veg"] },
  { id: "eg-horiatiki", world: "egeo", cat: "centro", name: "Horiatiki con feta entera", desc: "Tomate, pepino, cebolla roja, pimiento, kalamata y un bloque de feta con orégano.", prices: one(11.5, "Para compartir"), allergens: ["leche"], diet: ["veg"], share: true, sig: true },
  { id: "eg-pulpo", world: "egeo", cat: "principal", name: "Pulpo a la brasa con fava", desc: "Puré de guisante amarillo de Santorini, alcaparras y limón.", prices: one(19), allergens: ["moluscos"] },
  { id: "eg-souvlaki", world: "egeo", cat: "principal", name: "Souvlaki de cerdo al orégano", desc: "Brochetas marinadas con limón, pita y tzatziki.", prices: one(15), allergens: ["gluten", "leche"] },
  { id: "eg-yogur", world: "egeo", cat: "postre", name: "Yogur griego con miel de tomillo", desc: "Con nueces tostadas.", prices: one(6, "Ración"), allergens: ["leche", "frutos"], diet: ["veg"] },

  // Tirreno
  { id: "ti-focaccia", world: "tirreno", cat: "picar", name: "Focaccia de romero y sal", desc: "Masa madre, aceite de oliva y sal en escamas.", prices: one(5.5, "Para compartir"), allergens: ["gluten"], diet: ["veg", "vegan"], share: true },
  { id: "ti-burrata", world: "tirreno", cat: "centro", name: "Burrata con tomates asados", desc: "Tomates de horno, aceite de albahaca y pan tostado.", prices: one(12.5, "Para compartir"), allergens: ["leche", "gluten"], diet: ["veg"], share: true },
  { id: "ti-vitello", world: "tirreno", cat: "centro", name: "Vitello tonnato", desc: "Ternera fría en láminas, salsa de atún y alcaparras.", prices: one(14.5, "Para compartir"), allergens: ["huevo", "pescado", "mostaza"], share: true },
  { id: "ti-spaghetti", world: "tirreno", cat: "principal", name: "Spaghetti al pomodoro y albahaca", desc: "Salsa de tomate lenta, albahaca fresca y parmesano.", prices: one(14), allergens: ["gluten", "leche"], diet: ["veg"], sig: true },
  { id: "ti-risotto", world: "tirreno", cat: "principal", name: "Risotto al limón", desc: "Arroz carnaroli, limón, mantequilla y un toque de vino blanco.", prices: one(15.5), allergens: ["leche", "sulfitos"], diet: ["veg"] },
  { id: "ti-tiramisu", world: "tirreno", cat: "postre", name: "Tiramisù de la casa", desc: "Café espresso, mascarpone y cacao amargo.", prices: one(6.5, "Ración"), allergens: ["gluten", "huevo", "leche"], diet: ["veg"] },

  // Levante — carta del caso ORILLA (ORI-MENU-01)
  { id: "ORI-DISH-01", world: "levante", cat: "picar", name: "Tomate aliñado, aceitunas partidas y pan tostado", desc: "Tomate en gajos, aceitunas partidas y aceite de oliva. El pan tostado llega al lado para recoger el aliño.", prices: [{ id: "P01", label: "Plato para compartir", amount: 8.5, note: "Pan tostado incluido." }], allergens: ["gluten"], share: true },
  {
    id: "ORI-DISH-02", world: "levante", cat: "centro", name: "Berenjena asada con yogur de limón, miel y avellanas tostadas", desc: "Berenjena tierna de horno, con yogur de limón, un hilo de miel y avellanas tostadas. Elige media ración o ración.",
    prices: [{ id: "P02", label: "Media ración", amount: 9.5 }, { id: "P03", label: "Ración", amount: 15 }], allergens: ["leche", "frutos"], sig: true, share: true,
    variants: [
      { id: "V01", label: "Con yogur de limón", name: "Berenjena asada con yogur de limón, miel y avellanas tostadas", desc: "Berenjena tierna de horno, con yogur de limón, un hilo de miel y avellanas tostadas.", allergens: ["leche", "frutos"] },
      { id: "V02", label: "Con aceite de limón, sin yogur", name: "Berenjena asada con aceite de limón, miel y avellanas tostadas", desc: "La misma berenjena con aceite de limón en lugar de yogur. Conserva la miel y las avellanas.", allergens: ["frutos"], warn: "Quitar el yogur no garantiza que no contenga leche. La información de preparación está pendiente." },
    ],
  },
  { id: "ORI-DISH-03", world: "levante", cat: "principal", name: "Alubias blancas con calabaza y romero", desc: "Alubias y calabaza cocinadas en caldo de verduras, con aceite de oliva y romero. Se sirven en plato hondo.", prices: [{ id: "P04", label: "Plato individual", amount: 13.5 }], allergens: [], diet: ["vegan"], dietNote: "Declaración de ejemplo: vegano. Sin verificar." },
  { id: "ORI-DISH-04", world: "levante", cat: "principal", name: "Arroz al horno de verduras y garbanzos", desc: "Arroz de horno con calabaza, pimiento y garbanzos. Se prepara para un mínimo de dos personas.", prices: [{ id: "P05", label: "Por persona", amount: 16, unit: "persona" }], min: 2, allergens: [], sig: true },
  { id: "ORI-DISH-05", world: "levante", cat: "principal", name: "Merluza al horno con patata, cebolla y limón", desc: "Merluza al horno sobre patata y cebolla, terminada con limón y aceite de oliva.", prices: [{ id: "P06", label: "Plato individual", amount: 18.5 }], allergens: ["pescado"] },
  { id: "ORI-DISH-06", world: "levante", cat: "principal", name: "Pollo asado al limón con patata y romero", desc: "Pollo asado con patata y su jugo de limón y romero. Un plato individual.", prices: [{ id: "P07", label: "Plato individual", amount: 15.5 }], allergens: [] },
  { id: "ORI-DISH-07", world: "levante", cat: "postre", name: "Naranja con aceite de oliva y chocolate negro", desc: "Gajos de naranja con aceite de oliva y chocolate negro rallado.", prices: [{ id: "P08", label: "Ración", amount: 5 }], allergens: [] },
  { id: "ORI-DISH-08", world: "levante", cat: "postre", name: "Flan de café", desc: "Flan de café y caramelo, servido en una porción individual.", prices: [{ id: "P09", label: "Ración", amount: 6 }], allergens: ["leche", "huevo"] },
  { id: "ORI-DISH-09", world: "levante", cat: "bebida", name: "Agua", desc: "Botella de agua de 750 ml.", prices: [{ id: "P10", label: "Botella · 750 ml", amount: 3 }], allergens: [] },
  { id: "ORI-DISH-10", world: "levante", cat: "bebida", name: "Vino blanco de la casa", desc: "Vino blanco servido por copa de 125 ml o botella de 750 ml.", prices: [{ id: "P11", label: "Copa · 125 ml", amount: 3.5 }, { id: "P12", label: "Botella · 750 ml", amount: 17.5 }], allergens: ["sulfitos"] },
  { id: "ORI-DISH-11", world: "levante", cat: "bebida", name: "Café espresso", desc: "Café espresso, una taza de 30 ml.", prices: [{ id: "P13", label: "Taza · 30 ml", amount: 1.8 }], allergens: [] },

  // Oriente
  { id: "or-hummus", world: "oriente", cat: "picar", name: "Hummus con aceite verde y piñones", desc: "Zumaque, pimentón y pita caliente para mojar.", prices: one(9, "Para compartir"), allergens: ["sesamo", "gluten"], diet: ["veg", "vegan"], share: true, sig: true },
  { id: "or-baba", world: "oriente", cat: "picar", name: "Baba ganoush ahumado", desc: "Berenjena a la llama, tahini, granada y perejil.", prices: one(8.5, "Para compartir"), allergens: ["sesamo"], diet: ["veg", "vegan"], share: true },
  { id: "or-falafel", world: "oriente", cat: "picar", name: "Falafel con salsa tahini", desc: "Garbanzo y hierbas, crujiente por fuera y verde por dentro.", prices: one(9.5, "Ración"), allergens: ["sesamo"], diet: ["veg", "vegan"] },
  { id: "or-fattoush", world: "oriente", cat: "centro", name: "Fattoush con pan crujiente", desc: "Hierbas, rabanito, tomate, granada y zumaque.", prices: one(10.5, "Para compartir"), allergens: ["gluten"], diet: ["veg", "vegan"], share: true },
  { id: "or-kafta", world: "oriente", cat: "principal", name: "Kafta de cordero con tahini", desc: "A la brasa, con perejil, cebolla y limón.", prices: one(17), allergens: ["sesamo"] },
  { id: "or-mouhalabieh", world: "oriente", cat: "postre", name: "Mouhalabieh de agua de rosas", desc: "Crema de leche suave con pistacho picado.", prices: one(6, "Ración"), allergens: ["leche", "frutos"], diet: ["veg"] },

  // Magreb
  { id: "ma-zaalouk", world: "magreb", cat: "picar", name: "Zaalouk de berenjena y tomate", desc: "Comino, pimentón dulce y cilantro.", prices: one(7.5, "Para compartir"), allergens: [], diet: ["veg", "vegan"], share: true },
  { id: "ma-briouats", world: "magreb", cat: "picar", name: "Briouats de queso y hierbas", desc: "Triángulos de masa warka rellenos y dorados.", prices: one(8, "Ración"), allergens: ["gluten", "leche", "huevo"], diet: ["veg"] },
  { id: "ma-harira", world: "magreb", cat: "centro", name: "Harira de lentejas y garbanzos", desc: "Sopa especiada con tomate, apio y cilantro.", prices: one(9, "Plato hondo"), allergens: ["apio", "gluten"], diet: ["veg", "vegan"] },
  { id: "ma-tajin", world: "magreb", cat: "principal", name: "Tajín de pollo, limón confitado y aceitunas", desc: "Azafrán, jengibre y cilantro, cocinado lento bajo la tapa.", prices: one(18), allergens: [], sig: true },
  { id: "ma-cuscus", world: "magreb", cat: "principal", name: "Cuscús de siete verduras", desc: "Garbanzos, pasas y caldo especiado.", prices: one(15), allergens: ["gluten", "apio"], diet: ["veg", "vegan"] },
  { id: "ma-naranja", world: "magreb", cat: "postre", name: "Naranja con canela y azahar", desc: "Fresca y perfumada.", prices: one(5.5, "Ración"), allergens: [], diet: ["veg", "vegan"] },
];

export const FOOD_NOTICE = "Los ingredientes y alérgenos son ejemplos sin verificar. Esta demostración no sirve para decidir qué puedes comer.";
