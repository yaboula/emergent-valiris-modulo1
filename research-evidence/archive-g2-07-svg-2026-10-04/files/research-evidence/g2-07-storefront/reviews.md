# Specialist-tool review record — proposal 0.2

Method: dual-agent Impeccable critique (A: `/root/impeccable_design_review`;
B: `/root/impeccable_evidence_review`), with explicit user authorisation.
Both assessments were isolated; B held all findings until A finished. Review
support is consultative; this is **not G4 independent application approval**.
The author resolves recommendations against CASE/COPY/IA and the founder's direction.

## Sequence and provenance

1. Project/Git sources frozen at `4893d501b750efd1bb9149ff695564f0d2df227b`.
2. Impeccable context was read once during preparation. New-work/craft-floor and
   critique/adapt/polish references were read; project ownership and no-app scope
   take precedence over generic initialization/implementation instructions.
3. PC v0.1 produced first; archive `iterations/pc-v0.1.svg` and `.png`.
   PC-only state stress followed before phone generation.
4. Isolated assessments A/B inspected the complete 1440 × 4473 initial board,
   source, PNG/crops and separate fresh browser tabs. No input from B entered A.
5. Author adapted phone, queried targeted UI/UX Pro Max knowledge, inspected
   intermediate sizes/text enlargement and batched corrections into v0.2.
6. DESIGN.md was derived from that contrast and linted.
7. Vercel guidance was freshly fetched on 4 October 2026 against the mature model;
   then a final Impeccable/UX confirmation is recorded below.

Target slug returned by `critique-storage slug`:
`e-g2-07-storefront-iterations-pc-v0-1-svg-41741358`.
No `.impeccable/critique/ignore.md` was supplied. Reports are stored in this owned
directory instead of creating an out-of-scope `.impeccable` persistence directory.

## Initial Impeccable design assessment A

Verdict: source-specific content with a coherent oven/table proposition; visual
composition remains partly conventional and final object/crop relationships
cannot be judged through resource markers. Strong typography, warm surfaces and
colour proximity are observable. Authorised substitute fonts are not a defect.
The key opportunity was a faster reading rhythm without discarding content.

| Nielsen heuristic | Score / 4 | Scope |
| --- | --- | --- |
| Status visibility | 3 | Visible fiction/availability, no operational feedback. |
| Real-world match | 4 | Concrete names, portions, units, local/kitchen facts. |
| Control/freedom | n/a | No connected navigation/history to assess. |
| Consistency | 3 | Same visual language; CTA widths varied. |
| Error prevention | 3 | Limits/unknowns visible; flan status needed closer association. |
| Recognition | 3 | Four distinct entry destinations; visit conditions needed grouping. |
| Efficiency | n/a | Persuasive static presentation, no accelerators. |
| Aesthetic/minimal | 3 | Clear hierarchy; lengthy previews and concentrated story. |
| Recovery | 3 | Written flan recovery visible; execution untested. |
| Help/documentation | n/a | No usage documentation needed for this presentation. |
| Total applicable | **22/28** | Visible initial model; not functional acceptance. |

Cognitive load: low at entry, moderate among visit conditions. Four distinct
entry destinations; repeated Carta access is one task. No >4-option decision point
was observed. Narrative invitation → consultation → story → calm practical ending
is coherent; the offer sequence and right-heavy story slowed the middle.

| Finding | Severity / location | Adopted resolution in v0.2 |
| --- | --- | --- |
| A01: flan appeared comparable before its status | P2; UI-P01 H02/D08 | Status now directly follows full title, before description/formats. Scoped explanation and Postres recovery remain. |
| A02: offer facts consumed excessive vertical space | P2; H02 D02/D04/D08 | Named format and complete amount share a wrapped row; all descriptions, minimum, notices and detail remain. |
| A03: visit conditions had uniform reading weight | P2; H04 after schedules | Existing first sentences emphasised; PC separates seating/services from access/unknowns, phone stacks groups. No new labels or facts. |
| A04: story/captions concentrated in one column | P2; H03 | Full story split at an existing sentence into two paragraphs; PC captions beside story under optional scene, phone in full reading order. |
| A05: CTA width variation | P3; H01/H04 | Normal PC Ver carta slot 180 px; phone header 132 px for identity fit; longer return/action wording has a separate justified slot. |

Strengths retained: immediate anonymous Carta, exact full offers, visible fiction,
positive food declarations with pending fields, full story, complete visit facts.
Question raised by A about the oven/table relationship is routed into the resource
brief. **Questions skipped: the user authorised execution; no unresolved material
content ambiguity requires an additional founder decision at this checkpoint.**

## Initial Impeccable detector/browser assessment B

One actual `impeccable.cmd detect --json iterations/pc-v0.1.svg` call returned
`[]`, exit 0, zero findings/rule names/file locations. SVG is outside the usual
documented markup extensions; the zero is **not** a coverage or compliance claim.
No false positives occurred. Independent XML/geometry checks were necessary.

Browser rendered the full PC board. Initial viewport 1253 × 706 clipped a fixed
1440-wide artboard; fullPage inspection showed the whole source. This demonstrates
standalone opening, not browser adaptation. DOM: 77 text blocks, 130 IDs, zero
links/buttons/images/scripts. The accessibility tree exposes an image with title
and description, not an operable UI. No overlay was injected: available evaluation
was read-only, so no mutable injection/[Human] presentation existed. A console
error lacking an origin could not be attributed to this script-free SVG.

UTF-8/XML/viewBox/unique IDs/local refs, text/control canvas bounds and all 77
manifest text IDs passed. Twelve drawn controls, minimum 132 × 48, zero connected.
Browser text metrics exceeded two intended 650 px story columns by 4.10/10.36 px,
without a canvas overflow or collision. v0.2 reserves 4% wrapping tolerance.
Two mislabeled section crops were corrected to select the display heading rather
than its navigation copy ID. Full-board review had covered the missed sections.

Archived v0.1 and active v0.2 have separate titles/hashes; `checks/exports.json`
corresponds to active sources, not the archive. The initial v0.1 SVG hash observed
by B was `26e30283de9353e163ef2c33fe4e3a4178621c51957c00ab6384afb1b6e436cc`.

## UI/UX Pro Max knowledge stress

Installed skill queries used the explicit `ux` domain, not a generated art direction:

| Query | Verified top result / source | Fit and decision |
| --- | --- | --- |
| touch target size spacing | Touch Target Size; `ux-guidelines.csv` | Distinguishes native units from web guidance. Keep 44 × 44 as ORILLA's proposed comfort target, not a universal WCAG minimum; ≥8 px between adjacent target proposals. |
| text zoom reflow overflow | Text Reflow and Spacing; same local database | Preserve full content and growing height. Use separate 200% board, avoid clipping; browser zoom/user-spacing validation still pending. |

Touch: no hover-only content, labelled options, no gesture-exclusive action,
no fixed/sticky obstruction. Full names/units/states persist at observation widths.
Focus/keyboard/AT cannot run through drawn controls; no false pass is recorded.
Colour contrast is measured separately. Static absence of motion supports a still
variant, not an implemented `prefers-reduced-motion` contract.

## Vercel final review — independent rule perspective

Source: [current Web Interface Guidelines](https://raw.githubusercontent.com/vercel-labs/web-interface-guidelines/main/command.md),
fetched 4 October 2026. Reviewed mature v0.2 SVG sources, exports and state/return
annotations. This is a different rule perspective applied by the author, **not an
external specialist review or G4 approval**. No UI implementation was commissioned.

| Finding | Severity / location | Relevant rule | Applies to ORILLA? / resolution |
| --- | --- | --- | --- |
| VG01: drawn actions have no navigation/keyboard semantics | P1 future implementation; all SVG controls | Accessibility / semantic controls | Applies to future product; static fidelity boundary is explicit. Keep G2.03/G4 keyboard/AT checkpoint open. |
| VG02: focus is not executed | P1 future prototype; controls and returns | Focus States | Applies; no fixed obstruction proposed. Visible-focus/order/restoration review awaits connected prototype. |
| VG03: pending language/refresh needs clear recovery | P2; S14/S18/S19/S23–25 | Navigation & State; error recovery | Applies. Separate source-compatible fallback, lost-anchor, unknown and withdrawn boards; known recovery targets annotated. |
| VG04: long content must remain understandable | P2; D02, C2, 200% | Content Handling | Applies; full wrapping and growing height. Reject truncation of essential names/units/minimums; real reflow remains pending. |
| VG05: image absence must preserve reading | P2; NOART/NOSTORY | Images / meaningful media | Applies at design level; remove optional media rather than broken slots. Final art, ALT and CLS checks require received assets/implementation. |
| VG06: localised amounts/dates need source fidelity | P2; offers and dated exception | Locale & i18n | Applies to production. Static Spanish fixture deliberately uses its exact source; runtime Intl/configuration remains undefined. |
| VG07: decorative geometry must not create AT noise | P3; resource-study groups | Decorative media | Applied: geometry has aria-hidden, whole board has title/description. Does not make text a semantic website. |
| VG08: still/reduced-motion access | P2 future motion; H01/H03 | Animation | Relevant if motion is added; present model is fully static. No timing or preference handler claimed. |
| VG09: fixed artboard scrolls at other viewport widths | P2 fidelity limit; standalone 1440 SVG | Safe Areas & Layout | Static source limitation documented; separate width compositions supplied. Never hide overflow or call it responsive code. |
| VG10: forms, hydration, dark theme, drag | n/a; no such surface | Corresponding rule sections | No applicable design surface. Dark mode conflicts with founder's light-only direction; no unsolicited mode introduced. |

## Conflicts resolved by project authority

| Advice / conflict | Decision and reason |
| --- | --- |
| Generic mobile-first recommendations vs founder's PC-first sequence | PC first, then deliberate phone adaptation with feedback to PC. Both retain launch capabilities. |
| Generic truncation option vs full essential names/conditions | Wrap/grow. CASE/COPY and R10 prohibit losing ingredients, price unit or minimum. |
| SVG optimisation removing IDs/text vs editability/traceability | Preserve semantic groups, live text and source attributes. No outlined/rasterised functional type. |
| Vercel English heading/copy conventions vs authored Spanish voice | Preserve approved source wording/capitalisation and narrative voice. No ampersand substitution or universal Title Case. |
| Generic design initialization/root DESIGN vs owned paths | Derived DESIGN remains here; existing project contracts govern. No app or new root system. |
| Asset decoration vs exact offer comprehension | Actions/facts outside resource crop; explicit marker and no-art versions. G2.08/G2.06 ownership retained. |

Final confirmation results and preview cleanup are recorded in the delivery/check
evidence after they actually run. Remaining functional checkpoints are listed in
the main contract and prepared returns; none is converted into a pass by this report.
