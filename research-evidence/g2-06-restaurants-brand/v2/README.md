# Revised brand proposal v2

3 October 2026. **General direction idea, not definitive branding.** Recommend A / Carácter a la mesa; compare B / Sala viva. The founder positively receives the general idea and finds the direction clear, while colors and many details need refinement. The repertoire is freely open to anything related to food, cooking and restaurants; plate, pear, aubergine and cup are four examples, not a fixed cast. Palette, final assets and R1 endorsement remain unapproved. [Founder clarification](founder-clarification.md) records this explicitly; v1 remains rejected.

The primary [guide](../../../docs/design/valiris-restaurants-brand-direction.md) explains meaning, relationships, maintenance, sources and specialist briefs. [Figma v2](https://www.figma.com/design/uJSv4mj3oi9Br8Za9WuZAz?node-id=20-2) contains editable text, custom lettering vectors, native layout and conceptual content images. It is an evaluation board, not application implementation.

| Sheet | Native node | Local export |
| --- | --- | --- |
| Five-reference mechanisms | 20:3 | [01](boards/01-reference-analysis.png) |
| A: kitchen family, recommended | 20:29 | [02](boards/02-a-caracter-a-la-mesa.png) |
| B: social hospitality alternative | 20:57 | [03](boards/03-b-sala-viva.png) |
| Open family: four prototype silhouettes and acting examples | 20:84 | [04](boards/04-kitchen-family.png) |
| Original lettering, color and reading | 20:109 | [05](boards/05-lettering-color.png) |
| Two intensities, identical offer facts | 20:167 | [06](boards/06-two-intensities.png) |
| One conceptual 3D scene and plate keyframes | 20:196 | [07](boards/07-3d-motion.png) |
| Long name, language, R1/R2/R3, base/bespoke and untouched ORILLA | 20:213 | [08](boards/08-contrasts-handoff.png) |

## Available sources

- [Detailed analysis of all five supplied references](reference-analysis.md), including complete-timeline contact sheets and all seven PDF page renders in [reference-evidence](reference-evidence/).
- [Generated conceptual images and original lettering SVG](assets/). Selected art is clearly separated from superseded sensory exploration and intermediate refinements in [prompts](prompts.json) and [manifest](manifest.json).
- [Font notices](sources/): Gabarito and Source Sans 3, Google Fonts commit 9710da1eacb3be272583c3224dcb70f9da6eadbb; no font binaries included.
- [Author review](author-review.md), [native validation](figma-validation.json), [reproducible checks](checks.json) and [Spanish return](RETORNO_G1.es.md).

## Reconstruction and checks

[figma-open-family.js](figma-open-family.js) records the later founder clarification on page title and sheets 02/04/05; [its result](figma-open-family-result.json) contains affected IDs and declarations. The three affected PNG exports were refreshed and inspected. Apply this correction after original construction/fixes in a reconstruction, adapting IDs as necessary.

The native build is retained in [figma-build.js](figma-build.js), with [construction metadata](figma-construction.json), [targeted fixes](figma-fixes.js) and [audit](figma-audit.js). Inject the two SVG strings into LETTERING_A and LETTERING_B before the build. The file refuses a duplicate v2 page. These scripts describe original creation and corrections; do not rerun creation in the delivered page. IDs in corrections/audit are for this file; a reconstruction must use its returned IDs and equivalent child lookup. Upload original content images to the recorded rectangles using the supported asset upload tool. Short-lived URLs are not archived.

No published UI library or Code Connect mappings were used: these are original editorial branding specimens and two bounded native text fragments, not reusable components or a production screen. Artwork fills are discrete content images; the UI fragments are native text/layout, not flattened full-screen images.

Run `python research-evidence/g2-06-restaurants-brand/v2/verify.py` from the repository to check delivery integrity without modifying files. `--write-checks` deliberately refreshes the report; [refresh-manifest.py](refresh-manifest.py) refreshes owned asset/document hashes after an intentional edit. The v1 verifier and checks are historical; they do not validate v2 selection or approval.

## Evidence limits

Author review only. No full accessibility, interaction, user, localisation or legal/exclusivity test. Generated art is not a real restaurant or offered dish. The 3D file is a raster concept, not a model. Motion is a storyboard, not implemented animation. Final resource production, optical logo variants, precise colour/print calibration and application review are pending specialists and selection. G1 shared sources and ORILLA remain untouched. No merge or issue closure.
