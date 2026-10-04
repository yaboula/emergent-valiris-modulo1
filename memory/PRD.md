# ORILLA — Storefront landing (creative)

## Original problem
"si tengo como referencia este estilos de creatividad (Marshmallow rebrand + Headspace), y quiero crear un storefront para un restaurante que hace diferentes tipos de cocinas. como podemos ser también muy creativos"
User choices: landing page only (very representative), continuous-scroll "journey" where each cuisine is a world with its own character and colour; name ORILLA, Mediterranean food; no payments; no AI; wants real branding & identity (Marshmallow level).

## Architecture
- Frontend: Vite + React 18 + Tailwind 3 + framer-motion + lenis (/app/frontend, `yarn start` on :3000)
- Backend: minimal FastAPI /api/health only (/app/backend)
- Assets: 6 generated 3D clay characters + 6 dish images (bg removed, webp) in /app/frontend/public/img
- Repo context: fictional ORILLA case in /app/docs/design/orilla-case.md (Alcoy, Inés & Dani, hours, dishes) reused

## Implemented (2026-10-04)
- Brand identity: "sun over shore" symbol as the O of ORILLA (animated waves), wordmark, favicon, Bricolage Grotesque + Plus Jakarta Sans, grain overlay
- Hero (mint/raspberry plane, giant wordmark, berenjena signature dish, host Oli w/ bubble)
- Scroll-driven manifesto word reveal; country marquee
- 5 worlds (Egeo, Tirreno, Levante, Oriente, Magreb): page colour morph via @property CSS vars, sticky stage, giant outline word parallax, character + quote bubble, dish rotation, menu ticket with prices
- Route tracker pill, Cast ("El reparto"), La casa story, Visit (hours, Alcoy), reservation form (MOCKED: demo toast only), footer w/ fiction disclaimer
- Tested: iteration_1 all pass; mobile overflow fixed

## Fixes (2026-10-04, iteration 2)
- Manifesto sticky restored (removed html overflow-x clip that broke position:sticky)
- Hero buttons/text locked to hero palette (no invisible 'Empezar el viaje' when theme changes)
- Reduced vertical spacing: worlds 140vh, manifesto 180vh, sections py-20/28

## Carta Digital (2026-10-04, iteration 3)
- Route /carta (react-router): hero with character world pickers, sticky glass filter bar (search accent-insensitive, world tabs synced to ?orilla=, categories, diet, 14 EU allergen exclusion), colour morph per world group
- 35 dishes (data/menu.js); Levante = real ORILLA case menu (ORI-DISH-01..11, formats P01..P13, berenjena variants V01/V02 with warning, arroz min 2, vegano de ejemplo, 'pendiente' when no declaration)
- Dish drawer (variants, formats, qty with min, allergens, food notice, conceptual image label); quick add
- Mi mesa (localStorage) floating button + drawer -> 'Reservar con esta selección' -> landing #visita, summary in ReserveCard (MOCKED, no order/payment)
- Landing tie-ins: nav 'La carta', hero 'Ver la carta', per-world 'Ver toda la carta de…'
- Tested iteration_2: 29/29 pass; forwardRef warning fixed

## Iteration 4 (2026-10-04) — Personajes vectoriales, Ojos vivos, Platos reveladores
- 6 hand-built SVG mascots (components/mascots) with regional dress: Oli (bow tie host), Feta (Greek fisherman cap + Breton stripes), Don Pomodoro (Neapolitan paglietta + tricolore kerchief), Cassola (Valencian gingham mocador), Garbanzo (Lebanese tarboush + embroidered vest), Sultán Tajín (zellige band + babouche)
- Ojos vivos: pupils follow pointer (springs), random blinks/double blinks, wander on touch, hover = 'wow' mouth; presenting arm animates (path d)
- Platos reveladores: dish drawer stage — mascot springs in, cloche lifts, photo or 'MARCHANDO' price sticker, sparkles, speech bubble line per character
- New top-down editorial dish photos /img/top_*.webp (arroz regenerated strictly vegetable per case); old AI char/dish webps removed
- Tested iteration_3: 18/18 pass

## Backlog
- P1: Compartir mesa por WhatsApp (resumen + enlace que reabre la selección) — user chose format, deferred this round
- P1: Real reservation channel (WhatsApp/email) when real data exists
- P2: Character micro-animations (blink, cursor-follow eyes), sound toggle, EN/FR/DE translations
