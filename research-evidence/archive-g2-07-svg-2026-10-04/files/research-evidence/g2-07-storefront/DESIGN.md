---
version: alpha
name: ORILLA Storefront proposal 0.2
description: Proposed rules derived from the desktop and phone static composition. Not approved production branding.
colors:
  primary: "#243EB8"
  paper: "#FFF8EC"
  ink: "#20251E"
  muted: "#53594C"
  coral: "#FA735A"
  pink: "#F7CADD"
  mint: "#DDEBBE"
  yellow: "#F3DE8A"
  line: "#CCC6B8"
  white: "#FFFFFF"
typography:
  display:
    fontFamily: Arial Black
    fontSize: 80px
    fontWeight: 900
    lineHeight: 1.1
  section:
    fontFamily: Arial Black
    fontSize: 48px
    fontWeight: 900
    lineHeight: 1.15
  body:
    fontFamily: Segoe UI
    fontSize: 20px
    fontWeight: 400
    lineHeight: 1.45
  label:
    fontFamily: Segoe UI
    fontSize: 18px
    fontWeight: 700
    lineHeight: 1.4
rounded:
  notice: 12px
  resource: 20px
  action: 9999px
spacing:
  small: 8px
  medium: 24px
  large: 72px
components:
  button-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.white}"
    typography: "{typography.label}"
    rounded: "{rounded.action}"
    padding: "{spacing.medium}"
    height: 48px
  button-secondary:
    backgroundColor: "{colors.paper}"
    textColor: "{colors.ink}"
    typography: "{typography.label}"
    rounded: "{rounded.action}"
  heading:
    textColor: "{colors.ink}"
    typography: "{typography.display}"
    padding: "{spacing.large}"
  section-heading:
    textColor: "{colors.ink}"
    typography: "{typography.section}"
  body:
    textColor: "{colors.ink}"
    typography: "{typography.body}"
  caption:
    textColor: "{colors.muted}"
    padding: "{spacing.small}"
  food-notice:
    backgroundColor: "{colors.mint}"
    textColor: "{colors.ink}"
    rounded: "{rounded.notice}"
  visit:
    backgroundColor: "{colors.yellow}"
    textColor: "{colors.ink}"
  resource-study:
    backgroundColor: "{colors.pink}"
    textColor: "{colors.ink}"
    rounded: "{rounded.resource}"
  decorative-object:
    backgroundColor: "{colors.coral}"
  separator:
    backgroundColor: "{colors.line}"
---

# ORILLA — derived visual contract

## Overview

Status: **proposed**, derived after UI-P01/UI-T01 and content stress. The complete
G2.07 contract is [m1-storefront-ui-adaptive.md](../../docs/design/m1-storefront-ui-adaptive.md).
This file does not approve a commercial model or replace its state/adaptation evidence.

Selected source: Modern Product-Centric Web Design — Bold Graphic, Editorial &
Soft Depth, with Playful Branding and Brand-led UI. Preserve light, flexible
colour and an open culinary repertoire. Presentation may express; consultation
must let readers recognise exact offers and conditions. Original ORILLA stays intact.

Stable proposed rules: real editable type over artwork; light surfaces; restaurant
identity first; direct public Carta; distinct narrative and practical rhythms;
full offer names and conditions; optional imagery; separate local/kitchen hours.

## Colors

Blue identifies primary actions, ink carries reading, paper is the main ground.
Coral/pink support expression; yellow marks practical visit information; mint
groups the food-demo limit. Colour alone never conveys availability or safety.
These hex values are **exploratory samples**, not a frozen brand palette.
Calculated text contrast ranges from 6.86:1 to 14.79:1 for the inspected pairs.
Thin separators are decorative; they do not define a control's only boundary.

## Typography

Arial Black and Segoe UI are **local exploratory substitutes**, expressly chosen
for these boards. They do not establish Marshmallow fidelity or production rights.
No font binaries, licensing decision or fallback deployment is delivered.

Desktop hero 80 px; phone 46 px; section headings 48/36 px; body 20/18 px; action
labels 18 px. These are canvas values, not CSS tokens guaranteed across platforms.
Names wrap. Body leading 1.45, display 1.1–1.2. Preserve diacritics, punctuation,
quantity/unit and decimal amount/euro groups. Reserve metric tolerance between
PIL/librsvg/browser. The 200% board enlarges text and recomposes vertically.

## Layout

Desktop uses an asymmetric presentation, serial offer rows, a two-column story
and a labelled schedule table. Phone puts recognition/proposition/CTA first,
then secondary navigation, stacked offers and day groups. Full story remains
visible; no simulated disclosure is required. Whitespace follows reading groups.

Canvas gutters 72 px wide, 48 px intermediate, 24 px phone are exploratory.
1440/390 and 360/430/768/844/1024/1280 are observation widths, **not breakpoints**.
Height follows content. Do not scale desktop artwork/text into a phone product.
No fixed/sticky element is proposed. Orientation should retain scroll and facts.

## Elevation & Depth

Soft offset shadow is confined to decorative crop-study objects: 0/10 px offset,
10 px standard deviation, ink at 12%. Reading surfaces and controls use contrast,
position and borders. No shadow communicates availability or turns prices into art.
These are exploratory depth values; final G2.08 layers remain pending.

## Shapes

Pill actions at normal text size, with taller multiline controls allowed; soft
12 px notices and 20 px resource studies. Fine horizontal separators organise
offer rows. Avoid a repeated uniform card grid. No mandatory character cast.
Iconography stays subordinate to literal labels; decorative geometry is hidden
from assistive technology in the SVG image representation.

## Components

The offer pattern keeps full current name → immediate status if applicable →
description → named format/amount → condition → positive/pending food facts →
detail. Desktop aligns offer facts beside the name; phone puts them below it.
The flan stays readable while temporarily unavailable, disappears from the
current Storefront preview when withdrawn, and has a distinct direct-target recovery.

Ver carta uses the same blue treatment and a 180 px normal desktop slot; phone
header uses 132 px to preserve identity, and longer return labels need wider slots.
44 × 44 px is a proposed design target; these SVG shapes are not operable controls.
Visible keyboard focus, semantic links/buttons and live feedback are future
observable checkpoints, not inferred from colour or lint.

## Do's and Don'ts

- Do preserve source IDs, exact amounts, portions, minimum, known positives and unknowns.
- Do label fiction and unverified food at the actual entry; retain task without images.
- Do keep variant choice and actual-origin return consistent; show loss explicitly.
- Do revise desktop when phone exposes hierarchy or content problems.
- Don't invent real opening/stock status, destinations, photographs or translations.
- Don't truncate essential content, use hover-only actions or replace words with colour.
- Don't freeze exploratory widths/fonts/crops as implementation decisions.
- Don't call SVG markup validation, this lint or author review G4 approval or WCAG certification.
