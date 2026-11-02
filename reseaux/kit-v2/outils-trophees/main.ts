import { imageBadge } from "@/lib/sfl/badges-3d/rendu";
const objets = ["coupe-pepite","coupe-buteur","coupe-passeur","coupe-defenseur","coupe-mvp","pepite"] as const;
const metaux = ["or","argent","bronze"] as const;
const keys = objets.flatMap(o => metaux.map(m => [o, m] as const));
const tick = () => {
  const out: Record<string,string|null> = {}; let n = 0;
  for (const [o,m] of keys) { const v = imageBadge(o as any, m as any, 768); out[`${o}__${m}`] = v; if (v) n++; }
  (window as any).__coupes = out;
  if (n === keys.length) document.body.dataset.ok = "1"; else setTimeout(tick, 300);
};
tick();
