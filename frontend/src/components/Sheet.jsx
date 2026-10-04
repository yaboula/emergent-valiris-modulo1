import { useEffect } from "react";
import { AnimatePresence, motion } from "framer-motion";
import { getLenis } from "../lib/scroll";

export default function Sheet({ open, onClose, children, testId }) {
  useEffect(() => {
    if (!open) return;
    const onKey = (e) => e.key === "Escape" && onClose();
    window.addEventListener("keydown", onKey);
    getLenis()?.stop();
    return () => {
      window.removeEventListener("keydown", onKey);
      getLenis()?.start();
    };
  }, [open, onClose]);

  return (
    <AnimatePresence>
      {open && (
        <div className="fixed inset-0 z-[70]">
          <motion.div data-testid={`${testId}-backdrop`} onClick={onClose} initial={{ opacity: 0 }} animate={{ opacity: 1 }} exit={{ opacity: 0 }} className="absolute inset-0 bg-black/50 backdrop-blur-sm" />
          <motion.aside
            data-testid={testId}
            data-lenis-prevent
            role="dialog"
            aria-modal="true"
            initial={{ x: "100%" }}
            animate={{ x: 0 }}
            exit={{ x: "100%" }}
            transition={{ type: "spring", stiffness: 260, damping: 30 }}
            className="absolute right-0 top-0 flex h-full w-full max-w-[540px] flex-col overflow-hidden bg-paper text-coal shadow-2xl sm:rounded-l-[36px]"
          >
            {children}
          </motion.aside>
        </div>
      )}
    </AnimatePresence>
  );
}
