const fmt = new Intl.NumberFormat("es-ES", { style: "currency", currency: "EUR" });
export const eur = (n) => fmt.format(n);

export const priceText = (d) => {
  const p = d.prices;
  const unit = p[0].unit ? ` / ${p[0].unit}` : "";
  return p.length > 1 ? `desde ${eur(Math.min(...p.map((x) => x.amount)))}` : `${eur(p[0].amount)}${unit}`;
};

export const norm = (s) => s.toLowerCase().normalize("NFD").replace(/[\u0300-\u036f]/g, "");
