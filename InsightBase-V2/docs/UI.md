# UI and interaction contract

> Maintenance rule: every new structural change must update the affected Markdown documents in this documentation set in the same task. Changes to architecture, files, data contracts, row mappings, formulas, UI structure, packaging, scope or operational rules are incomplete until the matching documentation is updated. Update the index/status date and change log as appropriate. V1 was deleted with user authorization on 2026-10-09; V2 is the only maintained version.

## Shared shell

Brand InsightBase; left navigation: Genel bakış / Bilanço / Kârlılık / Grup karşılaştırması / Sunum oluştur / Veri & yöntem. No 'Sektör araştırmaları' subtitle or phase block. Header includes breadcrumb, Veriyi yenile and mode badge. Main title/subtitle, sector/private/public segmented selector, a single display-unit selector and a source-status notice remain.

No analysis date picker, no source-unit selector, no latest-period button. Default unit is billion TL (1000); million and trillion are available. Do not persist a previously selected preview unit unless implementing an explicit new preference.

## Overview order

1. Full-width Öne çıkan hareketler panel with up to three MoM items (three columns on desktop).
2. Two composition cards: total credit composition, and a shared Mevduat dağılımı card containing separate TL and FX term/demand pies side by side. Percentages on slices, labels and amounts beside the pies. Legend items open corresponding details.
3. Bilanço block, subdivided with headings:
   - Krediler cards in order: BS3 total, BS4 TL, BS6 YP, BS12 retail, BS21 commercial, BS31 cards, BS28 SME, BS57 LDR.
   - Mevduat cards: BS37 total, BS38 TL, BS39 FX, BS41 term, BS49 demand.
4. P&L cards: PL65 profit, PL49 NII, PL53 fees, PL57 operating expenses, PL61 ECL, PL70 NIM, PL68 ROAE, PL69 cost/income.

The BS and PL blocks show source cadence/date and 'Tüm kalemler' navigation. Credit and deposit cards share the same grid and size, including typography/padding. No extra 'Para birimine göre krediler' heading. No Growth rhythm chart or main-indicator table in overview.

## Cards and details

Cards show nominal current value, unit/source date, selected change horizon and a small change spark. Nominal card values are intentional; the requirement to show changes by default applies to line charts. PL YTD selection shows cumulative amount and cumulative YoY change.

Click card/table/legend to open native dialog: title, source context, current amount and comparison stats, horizon controls, 12-month change line with point labels, source row/base details, related children and history. Children may overlap; never sum them automatically. Enter/Space activates interactive table rows. Dialog has close control. Missing data remains explicit.

## Other views

BS: main BS cards + complete template row table.
PL: monthly / cumulative YTD toggle, main cards and corresponding row table.
Compare: sector/private/public amounts with source dates; sector column shows YoY, private/public columns MoM. Do not assume private+public exhaust sector or compute shares across different dates.
Data/method: source availability, parsing warnings and financial definitions.

## Design

Modern restrained banking workspace: light background, white cards, blue primary accent, soft borders, rounded corners, modest shadows, legible hierarchy. SVG pies use blue/teal variations. Desktop cards use four columns; <=1150px two columns. Pie/highlight layouts collapse responsively. Chart can scroll horizontally on narrow widths to keep 12 labels legible. Respect focus styling and reduced motion.

## Known cleanup opportunities, not instructions to change now

app.js still has unused trend state/listener from removed overview chart. Several CSS rules from earlier layouts remain. Graph caption still says 'selected date' although no picker exists. These do not authorize reintroducing removed controls.

## Presentation view

See [PPTX_EXPORT.md](PPTX_EXPORT.md). Slide list with add/duplicate/reorder/delete, 16:9 preview and settings. Large desktop uses three panes; narrower desktop moves settings below the enlarged preview. Global dashboard group/unit toolbar is hidden; graph-specific controls govern each widget. Month ranges are explicit in this view only. Export includes native editable chart/table/text objects.

The slide toolbar places PDF indir next to PowerPoint indir. Both export all slides and disable while an export is preparing. PDF preserves the selected layout as fixed 16:9 visual pages.

The shared deposit card uses TL mevduat and FX mevduat subheadings with an internal divider. Desktop credit/deposit card widths are 1:2; on narrower desktop the cards stack, and on mobile the two deposit charts also stack. Percentages and source totals remain currency-specific.
