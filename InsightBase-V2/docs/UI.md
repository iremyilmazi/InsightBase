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


## Current schema update — 2026-10-11

The user supplied a new six-sheet reference `şablon (1).xlsx`. DATA_CONTRACT.md is the authoritative current catalog; earlier physical row numbers in this document are superseded. Stable internal metric IDs remain, with explicit `sourceRow`, `format` and `ratio` metadata. BS has 46 supported metrics; P&L 66. Date headers start in C, with B reserved for Format. `extract_structure.py <reference.xlsx>` extracts metadata only and writes both structure.json and structure.js. No financial values are committed.

TL means million TL, USD million USD, % ratio, explicitly confirmed by the user. NPL rows flagged % now use percentage-point changes. Dashboard cards, detail tables, pies and slide outputs preserve each currency. No FX conversion or TL+USD addition occurs. Nominal/pie charts mixing currencies are rejected; growth charts may compare percentage changes and table rows show their own currencies. Monthly P&L-to-cumulative ID offset remains 38 (physical source offset also 38). Removed TL/YP NPL volume rows, branch/headcount and aggregate term/demand source rows are excluded. LDR fallback uses total loans and total deposits, both TL aggregates.

The local 8768 preview keeps synthetic JSON and shows DEMO. The new Windows live delivery excludes Excel; the user provides adjacent dataa.xlsx. Canonical three-file build stays unchanged in count. Additional CMD launcher and guide are operational helpers. Source Excel passed the browser reader with six sheets and zero warnings; 18 engine/presentation tests passed, including ratio deltas and mixed-currency rejection. Local browser preview verified TL/USD labels and USD detail with no page errors. Windows itself remains unverified. This change is not automatically published to GitHub.

New structural changes must update these Markdown files in the same task.


## Balance-sheet ordering — 2026-10-11

BS catalog and displayed BS tables follow ascending physical Excel sourceRow, not stable internal metric ID. This also applies to detail subitem tables and presentation metric selection. The extractor preserves this order on schema regeneration. Summary cards in the BS tab follow their relative Excel order. Internal IDs and calculations remain unchanged.


## Excel title hierarchy — 2026-10-11

Column A formatting is extracted as `titleStyle` (indent, gray, bold) from Excel cellXfs/fonts/alignment. Tables apply it only to the metric title, with 18px per Excel indent level and gray #808080 for the reference gray font. Numeric cells and source captions retain their existing styles. Main and detail BS/P&L metric tables share this rendering. `preview_demo.py --source` builds only temporary preview assets directly from canonical sources; it does not regenerate Windows deliveries. Per user instruction, Windows packages remain frozen until explicitly requested.


### Table subtitle alignment — 2026-10-11

Metric source/date subtitles now share the title’s Excel indentation, while retaining their own muted color and normal weight. Both text lines start at the same horizontal position. Numeric columns remain unchanged. This supersedes the earlier unindented caption behavior. Only canonical source and temporary local preview are updated; Windows delivery builds remain deferred.


### Brand correction — 2026-10-11

Canonical HTML now uses InsightBase in sidebar, page title and footer, with I brand mark/favicon. The registered view tool is set_insightbase_view. Source-only demo preview inherits the canonical brand directly; packaging replacements are no longer needed to establish the product name. Windows builds remain deferred.


## Reference update — 2026-10-13

Current schema is `şablon (2).xlsx`. BS consumer-loan volume and consumer NPL entries are removed (IDs 13/14); retail loans NPL added as distinct ratio ID112 at source row9. Retail total ID12 remains at source row8. Subsequent BS sources shift up one; stable IDs preserve existing pie/card calculations. BS catalog now has45 metrics; PL retains66 and its source positions. Retail detail uses new ratio plus remaining product breakdowns. Excel source order, title indent/gray/bold and TL/USD/% metadata are regenerated. Local preview retains synthetic data and includes retail NPL. Six source sheets read with zero warnings; existing calculation/export tests passed. Windows packages and GitHub are not rebuilt/published for this task. The current release artifacts therefore remain the preceding release until requested. All structural changes require corresponding MD updates.


### Commercial loan title — 2026-10-13

User removed “cc hariç” from Excel. BS metric21 at source row17 is now labeled Ticari Krediler / Ticari krediler. Reader accepts the current label plus the previous exact label via a metric-specific alias for compatibility; no other label validation is relaxed. Only the wording changes; values, row mapping and pie components remain unchanged. Source-only demo updated; Windows packages/GitHub remain the previous release until requested.


## Unified BS MoM — 2026-10-13

User accepted shared monthly comparison: completed months compare final weekly stock to previous calendar month-end observation (7-day backward limit). Provisional latest month compares latest stock to one calendar month earlier (7-day backward limit, never a future observation). Calendar completion uses current UTC day against month-end. Dashboard, 12-month detail chart and slide MoM use shared engine monthlyCompare; P&L unchanged. Slides default range includes latest available month; provisional source dates remain in point metadata. Dashboard cards mark provisional periods. Missing historical month-end data remains missing; no substitution with early-month values. Windows/GitHub publication deferred until requested.


## Global P&L basis selector — 2026-10-13

Monthly/Cumulative segmented selector now sits beside the bank-group toolbar on overview, PL and comparison views. Shared state.basis drives overview P&L cards, deterministic PL highlight candidates, group comparison metrics and PL detail/table source rows. Monthly uses Monthly source IDs, cumulative pairs via offset38; BS is unaffected. Existing PL-tab duplicate selector removed. Cumulative MoM is change in cumulative level, not monthly flow; January year reset remains unavailable. Slide editor retains independent chart settings. Temporary demo preview updated; Windows and GitHub publication deferred until requested.


### P&L display labels — 2026-10-13

UI strips leading Monthly/Cumulative from PL display labels, source captions and detail source descriptions. Schema labels remain intact for strict Excel validation and pairing. Existing selected Aylık/Kümülatif filter communicates basis. Presentation selection, series and export labels inherit the same display helper. Calculations and workbook data unchanged. Windows/GitHub are not regenerated.


### Preserve P&L source terminology — 2026-10-13

User requires original English PL metric names. Display labels now use source schema names rather than Turkish plTitles overrides, stripping only leading Monthly/Cumulative. Applies to cards, tables, detail headings, highlights, comparisons and presentation/export labels. Workbook validation and financial calculations unchanged.


### Remove repeated metric subtitles — 2026-10-13

User requested removal of the repeated metric-name/date line under each BS and PL table row. Shared metric table now renders only the primary title, preserving source indent/gray/bold. Applies to primary tables and detail subitem tables. Source dates remain accessible in metric details and section metadata; calculations and data unchanged. This supersedes the earlier subtitle-alignment requirement. Preview updated; Windows and GitHub remain deferred.


## Simplified tab entry — 2026-10-13

All tabs use one compact navigation-name heading. Promotional subtitle and eyebrow removed from visible entry, duplicate header breadcrumb hidden. Bank group, unit, PL basis and change horizon share one wrapping toolbar; previous separate horizon row removed. Data/deck hide irrelevant global toolbar. Ready-state notice shows only BS/PL dates, with full original read status in tooltip; error/loading messages remain visible. Slide editor duplicate heading/intro hidden while actions remain. Source-only preview refreshed; Windows/GitHub not rebuilt.
