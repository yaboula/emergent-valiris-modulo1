# Deliberate adaptation and continuity — proposal 0.2

These are independently composed static SVGs, not a browser layout or device
detector. Canvas height follows content. Inspect `manifest.json` for exact dimensions
and each text/control box. 1440/390 are reference observations, not breakpoints.

| Block | Desktop decision | Phone decision | Preserved / scale / crop / priority | Phone feedback to PC |
| --- | --- | --- | --- | --- |
| Recognition/entry | Identity + CTA in header; visible fiction; secondary section navigation follows. | Identity + CTA remain first; fiction wraps. Descriptor/headline/intro/CTA precede secondary navigation. No drawer prerequisite. | Same name, descriptor, headline, fictional notice and public task. Display 80→46 px, body 22→18 px; the small-header CTA slot is narrower, target height remains ≥48 px. | Avoid allowing navigation to delay proposition on small screens. Normalise PC Ver carta slots while allowing longer return labels. |
| Expression | Separate right-side brand crop study, soft depth; no text inside art. | Brand study below functional content; optional scene omitted. | No raster facts, no indispensable animation. Change aspect ratio/focal grouping, rather than shrinking the desktop page. | Essential content must survive removal of both resource groups. Marker repetition became a distinct tabletop study in H03. Final art remains pending. |
| Kitchen introduction | Full PC culinary explanation, width capped for reading. | Supplied phone opening; exact rice minimum remains. | PC/phone copy versions share IDs and source, not separate restaurant facts. Food-demo limit remains beside food entry. | Keep expressive introduction and offer consultation visually distinct. |
| Offers | Serial rows: full name/description left; named formats/amounts/condition right. | Stack name, immediate state, description, formats, condition, positive/pending food and detail. | No truncation. Units and minimum do not shrink. Berenjena V01/V02 and wine formats have separate compatible facts. | Compact format+amount rows on PC; associate flan state directly with title on both. |
| Story | Complete story in two paragraphs right; optional scene and Inés/Dani captions left. | Complete canonical story in two paragraphs, captions and room description in reading order. | Full access without a simulated disclosure. Source phone summary remains available in content contract but is not required to hide the full story. | Spread PC captions away from a single long text column. No-story reset removes block and link. |
| Hours | Day/local/kitchen table; known exception explicitly dated above ordinary rows. | Each complete day group stacks local then kitchen, including Monday and both dinner periods. | Times/date/unknowns remain full-sized text, never a live badge inferred from host clock. | Group visit facts by reading task; emphasise the actual first sentences without inventing headings. |
| Visit conditions | Seating/services left, access/pending animals right, demo destination limit separately. | Seating, access and unknowns remain individual groups; known negatives and unavailable destinations stay explicit. | No fake call/map/book control. Direct entry and menu-origin return differ. | Make the step and measurements easier to scan, preserving factual uncertainty. |
| Menu/detail bridges | Limited representative rows and variant/format controls. | Stacked radio-like options with full labels, selected indicator and ≥44 px drawn target. | Same source, known applicable format and return; no cart/account gate. The full Digital Menu is outside this artefact. | Limit detail reading width and controls on desktop; retain all recipe uncertainty. |
| Motion/focus | Static; all reading independent of media. | Static, no fixed/sticky obstruction or hover-only task. | No actual hover, touch, keyboard, focus or reduced-motion execution can be inferred. | G2.03/G2.09 need an observable future prototype, not a claim based on these SVGs. |

## Width and text observations

| Frame | Observation / decision | Limit |
| --- | --- | --- |
| UI-P01 1440 | Full two-column expression, offer alignment, story and schedule table. | Intrinsic-width SVG; viewing it in a narrower browser can horizontally scroll. |
| UI-W1280 | Two-column relations retained; headline/names wrap earlier. | Font metrics and art crops are still exploratory. |
| UI-W1024 | Expression, story and schedules form one reading column; three navigation links still fit. | A proposed behaviour range, not a 1100 px implementation breakpoint. |
| UI-W768 | Spacious single-column presentation; nav uses measured labels instead of a full-width stack. | Avoid empty side columns at this width. |
| UI-W430 / UI-T01 390 / UI-W360 | Full names/price conditions wrap and height grows; nav flows across rows after presentation. | No language-expansion proof beyond Spanish; no native safe-area execution. |
| UI-L844 | Landscape width 844; full vertical reading remains; entry crop includes a 390 px height observation. | Rotation behaviour and physical browser viewport are not implemented. |
| UI-Z390 | Text sizes doubled; header/CTA stack, no-art version, taller paragraphs and controls. Nothing essential hidden. | Authored 200% recomposition; **not** a real browser zoom/reflow or user-spacing test. |

The meaningful proposed ranges are: roomy side-by-side compositions when each
column retains its content; a single-column intermediate composition when it does
not; compact phone composition with task before secondary navigation. Engineering
must derive technical thresholds from an implemented layout and actual fonts.

## Source fidelity and maintenance

`tools/build_compositions.py` reads the frozen CASE/COPY tables, derives format and
amount together, and makes new SVG sources for each width/state. It does not
implement routes or handlers. A price/recipe/availability change re-renders affected
uses from the same record. `tools/verify.py` checks critical source relationships,
including milk uncertainty on V02 and price suppression on withdrawal/unconfirmed
targets. This proves source consistency in the design generator, not restaurant
maintenance usability, permissions, publication atomicity or production data binding.
