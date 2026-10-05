import { useEffect } from "react";
import { AnimatePresence, motion, useDragControls } from "framer-motion";
import { getLenis } from "../lib/scroll";
import useMedia, { MOBILE } from "../lib/useMedia";

const spring = { type: "spring", stiffness: 260, damping: 30 };

export default function Sheet({ open, onClose, children, testId, style }) {
  const isMobile = useMedia(MOBILE);
  const controls = useDragControls();

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

  const from = isMobile ? { y: "100%" } : { x: "100%" };
  const to = isMobile ? { y: 0 } : { x: 0 };

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
            style={style}
            initial={from}
            animate={to}
            exit={from}
            transition={spring}
            drag={isMobile ? "y" : false}
            dragControls={controls}
            dragListener={false}
            dragConstraints={{ top: 0, bottom: 0 }}
            dragElastic={{ top: 0, bottom: 0.7 }}
            onDragEnd={(_, i) => (i.offset.y > 110 || i.velocity.y > 600) && onClose()}
            className={
              isMobile
                ? "absolute inset-x-0 bottom-0 flex max-h-[92svh] flex-col overflow-hidden rounded-t-[32px] bg-paper text-coal shadow-2xl"
                : "absolute right-0 top-0 flex h-full w-full max-w-[540px] flex-col overflow-hidden rounded-l-[36px] bg-paper text-coal shadow-2xl"
            }
          >
            {isMobile && (
              <div onPointerDown={(e) => controls.start(e)} data-testid={`${testId}-handle`} className="absolute inset-x-0 top-0 z-40 flex h-7 cursor-grab touch-none justify-center pt-2.5">
                <span className="h-1.5 w-12 rounded-full bg-black/25" />
              </div>
            )}
            {children}
          </motion.aside>
        </div>
      )}
    </AnimatePresence>
  );
}
