import { createContext, useContext, useEffect, useMemo, useState } from "react";

const KEY = "orilla-mesa";
const MesaCtx = createContext(null);

const load = () => {
  try {
    return JSON.parse(localStorage.getItem(KEY)) || [];
  } catch {
    return [];
  }
};

export const MesaProvider = ({ children }) => {
  const [items, setItems] = useState(load);
  const [open, setOpen] = useState(false);
  const [bump, setBump] = useState(0);

  useEffect(() => localStorage.setItem(KEY, JSON.stringify(items)), [items]);

  const value = useMemo(() => {
    const add = (line) => {
      const key = `${line.dishId}|${line.priceId}|${line.variantId || ""}`;
      setItems((prev) => {
        const ex = prev.find((i) => i.key === key);
        if (ex) return prev.map((i) => (i.key === key ? { ...i, qty: i.qty + line.qty } : i));
        return [...prev, { ...line, key }];
      });
      setBump((b) => b + 1);
    };
    const setQty = (key, qty) => setItems((prev) => prev.map((i) => (i.key === key ? { ...i, qty: Math.max(i.min || 1, qty) } : i)));
    const remove = (key) => setItems((prev) => prev.filter((i) => i.key !== key));
    const clear = () => setItems([]);
    const count = items.reduce((s, i) => s + i.qty, 0);
    const total = items.reduce((s, i) => s + i.amount * i.qty, 0);
    return { items, add, setQty, remove, clear, count, total, open, setOpen, bump };
  }, [items, open, bump]);

  return <MesaCtx.Provider value={value}>{children}</MesaCtx.Provider>;
};

export const useMesa = () => useContext(MesaCtx);
