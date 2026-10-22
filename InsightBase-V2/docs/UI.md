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


## Highlight scope — 2026-10-13

User is revising highlights incrementally. First accepted change: exclude all P&L metrics. Current candidates are BS total loans(ID3), total deposits(ID37), credit cards(ID31); existing absolute MoM ranking remains pending further instructions. PL basis selection no longer affects highlight candidates. Source-only demo updated; no Windows build or GitHub publication.


## Expanded BS highlights — 2026-10-13

Implemented in pure dist/highlights.js (InsightHighlights.analyze), bundled by preview and Windows builders without changing the three-file contract. It reads BS only and emits up to one growth, funding and NPL/risk card; insufficient data may yield fewer cards. Candidate rules: volume MoM, product-vs-total growth, TL/USD growth difference, TL/FX demand-deposit share changes, loan/deposit growth difference, LDR and NPL point changes, completed-month credit acceleration, sector-view private/public growth differences. Composition and contribution are excluded pending scope confirmation. Shared monthlyCompare supplies MoM bases. Derived metrics require identical current/base dates. Demand shares additionally require nonnegative same-currency components and 0.5% total reconciliation at both dates.

No financial significance cutoff or anomaly label is invented. For completed periods with12 prior valid completed observations (searching36months), selection ranks empirical absolute deviation from each candidate's own median; MAD is also recorded. Tied scores use stable IDs. Provisional periods cannot use this history ranking. Without comparable history, explicit fallback kind priority is share, fundingGap, currency, product, ratio, growth, groups, acceleration; within a kind, absolute change ranks candidates. This is a deterministic editorial selection, not a financial importance score. Historical values and scoring details are available in analyze return metadata; card method disclosure explains history/fallback choice. Empty, invalid or unchanged candidates are skipped; missing values are never zero-filled. No inferred funding cost or NPL cause is asserted. P&L basis cannot affect cards. Local preview updated; no GitHub publication or Windows rebuilding requested for this change.


## P&L reference3 — 2026-10-13

User supplied şablon (3).xlsx. Secondary cumulative/monthly reporting blocks removed; current source catalog is DATA_CONTRACT.md. PL has46 metrics:22 cumulative,22 monthly,2 auxiliary stocks. Monthly source section starts35 instead of46; cumulative Fee/OPEX is31 and monthly58. Net Profit uses monthly51/cumulative24. Stable metric IDs keep dashboard formulas and existing configured charts intact. Each monthly spec explicitly records cumulativeRow and basis; app and slides use pairing metadata. Physical source difference is27, not internal ID difference38. Removed IDs34–43 and72–81 are absent from tables/selectors. English source wording is retained, display prefixes hidden; source title formatting extracted. BS unchanged, including approved commercial label alias. Demo source remains synthetic. Six sheets read with zero warnings, pairing regression and financial/export tests pass. Windows/GitHub not rebuilt for this task; publication remains separately requested.


## Ratio level chart option — 2026-10-13

Ratio metric detail charts add Oran alongside MoM/YoY/YTD. Oran uses12 monthly source levels (percentage points stored as percent levels), with % point labels, not growth or percentage-point differences. Missing baseline does not suppress valid nominal levels. Level selection is detail-only and never changes the global dashboard horizon/cards; volume metrics have no level button. Existing independent presentation nominal option remains. Source preview updated; no Windows/GitHub publication.


## Presentation value-axis labels — 2026-10-13

Removed numeric value-axis tick labels from presentation SVG preview and therefore PDF rendering, and set native PPTX valAxisLabelPos=none. Applies to line, column and horizontal bar value axes. Point/bar data labels, category dates, grids and pie labels remain. Dashboard detail charts unchanged. Local preview updated; no Windows/GitHub release.


## Twelve-month composition detail — 2026-10-13

Overview credit/TL deposit/FX deposit pie graphics are keyboard-accessible buttons opening a12-calendar-month modal grid. Uses current bank group and same source rows as entry pies. Each historical month selects last weekly total within7days of month-end; current partial month uses latest dataset cutoff. Parts require exact matching source date, nonnegative values and 0.5% total reconciliation. Percent shares use component sum, consistent with entry pie. Share change is current share minus preceding calendar-month share in percentage points; missing/invalid prior month produces no delta (never skip gap). Requires13 slots internally to compute oldest displayed change. Each monthly card shows source date, source-currency total and category shares/deltas; unavailable months remain visible. Metric legend links still open metric detail. Responsive3/2/1-column layout. No Windows/GitHub rebuild.


## Compare arbitrary composition months — 2026-10-13

12-month pie modal includes start/end selectors over valid monthly compositions. End must follow start. Shows each component start/end volume, absolute change, percentage growth, start/end share and percentage-point difference, plus total change and actual source dates. Same source currency/display unit preserved; zero base gives unavailable growth, while share delta remains valid. Invalid months disabled, reverse/same dates rejected. Default is last two valid months, with exact selected dates clearly shown; not labeled MoM. Pure engine compareComposition tested. Local preview updated; no Windows/GitHub rebuild.


### Composition comparison footnote — 2026-10-13

Removed the user-specified unit/non-MoM explanatory footnote under the arbitrary-month comparison. Selected dates and total-change unit remain visible above the table. Calculation unchanged.


### Pie hover values — 2026-10-13

Overview and12-month composition SVG slice groups expose native title tooltips with metric name, nominal volume in current display/source currency and percent share. Existing on-slice percent labels retained. Tooltip values refresh with unit/group selection; calculations unchanged.


### Explicit pie tooltip — 2026-10-13

Native SVG title fallback supplemented with an immediate pointer-following tooltip. Mounted inside active dialog for top-layer visibility, otherwise body; clipped to viewport, pointer-events:none. Hides when leaving slices, scrolling or closing modal. Shows nominal volume, correct TL/USD display unit and share.


### Pie tooltip rollback — 2026-10-13

User requested reverting the explicit floating tooltip. Removed pointer handlers, data attributes and custom tooltip CSS. Native SVG title tooltips (name, volume, currency and share) remain.


## Numeric separator convention — 2026-10-13

User requires123,323.21-style numbers. Dashboard and presentation/PDF formatted values use Intl.NumberFormat(en-US), with grouping and maximum2 decimals. Source numeric values/calculations unchanged; Turkish date labels remain. Native PPTX language en-US and chart numeric formats [$-409]#,##0.## (pie percent [$-409]0.##%) request the same convention. Windows/GitHub not rebuilt.


## Analysis view rollback — 2026-10-18

User rejected the two trial integrations and requested rollback. Esnek karşılaştırma and Kâr köprüsü are not part of the active product. Removed analysis module/tests, navigation, view registry, events, CSS and loader/bundler hooks. Earlier dashboard, comparison, ratio/composition history, P&L and presentation features retained. Separate synthetic demo in outputs remains isolated for possible future reference. Neither integration was published to GitHub or Windows deliverables, so no release rebuild is needed. Real local workbook remains the active preview input.


## Presentation workflow trial — 2026-10-21

User approved local implementation of five authoring improvements, explicitly excluding save/open and forbidding GitHub publication until later approval. Windows packages and public Raw files must remain unchanged during review. Local rollback copies of presentation.js/app.js/styles.css are under ignored outputs/review-backups/presentation-before-2026-10-21. Real workbook stays private.

Session-only defaults: group, end month,3/6/12/24-month span, display unit. Defaults initialize from latest BS source and apply only to new widgets/slides. Existing widgets retain independent selections; changing defaults never mutates them. Shared end month may exceed latest PL data, preserving missing slots visibly. Settings details stay open while fields change.

Ready templates: credit growth (4BS series, nominal/YoY table), TL/FX deposit composition (2separate nominal pies), monthly profitability (3PL series, nominal/YoY table), LDR ratios (3BS ratios, nominal table). All inherit defaults and remain editable. For24-month presets, optional tables are disabled to respect12-month table limit. No assumptions about mutually exclusive loan composition were introduced.

Graph duplicate deep-copies config. Single-chart slide becomes double; a full two-chart slide creates a new single-chart copy. Quick metric selector changes primary metric and matching single-metric table only; independent table selections remain. PL widgets have explicit monthly/cumulative source selector, including dashboard-imported cumulative rows. Source-type change resets compatible metrics and basis while preserving dates, group and unit.

Metric details offer Sunuma ekle: capture source row, group, unit, horizon/ratio level and12-month range, then open selected new slide. Composition history offers pie-to-slide import with same row/group/currency selections. Existing slides remain. This captures selection settings, not static workbook snapshots; Excel refresh updates underlying series.

Page sidebar shows miniature charts and supports native drag/drop; separate Slaytları sırala grid previews full slides. Drag identity uses unique slide IDs; deep copies regenerate slide/widget IDs. Reorder preserves active slide identity; existing up/down controls remain as keyboard-friendly alternatives. Overview selection returns to editor. No JSON save/open, localStorage or server persistence added.

Validation includes defaults isolation, inherited template settings, deep clone independence, reorder identity, cumulative dashboard import, existing native PPTX exports, local browser preset/default/duplicate/navigation and actual drag/drop. No GitHub or delivery rebuild.


## Pie alignment and table redesign — 2026-10-21

User reported off-center pie graphics and unattractive slide tables. SVG pie center corrected from x150 to x320 in640-wide viewport; native PowerPoint pie plot gets a centered square manual layout. Preview pie legends centered and PDF legends centered when fitting one line. PDF derives the corrected centered SVG.

Table data now supplies structured metric/group/measure/unit metadata. Preview separates main metric from compact muted measure metadata on the same row. Removed dense vertical cell grid: pale header, alternating white/light rows, thin horizontal rules, tabular and right-aligned numbers. Long repeated bank group omitted when only one selected; financial values and independent row/group/mode selections preserved. PPTX uses native editable styled cells (same light header/banding and no vertical rules); PDF uses corresponding horizontal rules and right alignment. Dense preview tables use smaller spacing/font; all rows remain visible rather than clipped by max-height. Live12-month/8-row credit preset tested to fit above footer. Separate/double pie layout visually inspected. Changes remain local review; GitHub/Raw/Windows remain untouched per user hold.


## Compact editor and independent table rows — 2026-10-21

User requested a simpler table and fewer scrolling controls. Settings now use Slayt/Grafik/Veri/Tablo tabs. Wide screens keep a compact sticky right panel; small screens use a bounded-height settings panel. Searchable metric pickers retain keyboard focus/caret across rerenders and show removable selected chips. Graph and table metrics are independently selected; replacing a graph metric no longer modifies a matching table row implicitly.

Table defaults are nominal-only rather than a Cartesian list of all measurements. Each selected table metric can choose its own mode via tableRowModes[row]; legacy global tableModes remains fallback. Actual expanded table row count is used for validation. Table bank groups remain separately selectable. Minimal white table has no row fills or vertical grid, only a quiet header/footer rule in preview/PDF. Common measurement/unit appears once in header; only heterogeneous rows show row-specific metadata. Native editable table uses matching simple header and white cells. Source data and calculations unchanged.

Short tables use larger graph area; taller tables reduce chart height in preview/PPTX/PDF to avoid unused space or overlap. Presets now use nominal-only tables. This supersedes prior table-metadata/banded-row settings. Selection/search/individual measurement/export verified against local real dataset. Local review only: do not update GitHub/public Raw or Windows artifacts until requested. No draft persistence added.


## Per-chart decimal precision — 2026-10-21

Presentation Grafik settings now offer 0–4 decimal places independently per chart (default 2). Labels use fixed selected precision and en-US separators in SVG preview, PDF and editable PowerPoint chart number formats, including pie percentages. Underlying numeric data and table formatting remain unchanged. Duplicates retain precision; changes remain local review only, with no GitHub or Windows rebuild.


## Integrated chart/table layout — 2026-10-21

Time-series with tables share a 30% metric-label gutter and a 70% month grid; table month cells are centered under chart observations. SVG fills its allocated viewport and removes duplicate date labels when table headers supply them. Pie and horizontal bar retain their own axes. Compact preview heights and a quiet legend separator visually connect the sections. PowerPoint uses matching manual plot layout with hidden duplicate category labels and centered table values; PDF uses the shared SVG geometry and centered values. No publication or package rebuild.


## Centered charts and minimal table labels — 2026-10-21

Supersedes the 30% plot-gutter alignment trial: charts retain their centered full-width plot, independent of table label width. Remove the generic Kalem header; each table row identifies its metric followed by measurement and unit, e.g. YP krediler · YTD (%). Shared tableData applies this consistently to preview, PDF and editable PPTX. Table dates remain visible. Local review only.


## Fixed chart width and aligned period columns — 2026-10-21

Charts keep the same full-width SVG geometry whether or not a table is enabled; preview chart height capped at 24cqw and can shrink for dense tables. Table dates and values occupy exactly the existing 60..600/640 plot interval, with metric/measurement labels on separate full-span rows rather than a width-consuming first column. Equivalent manual PPTX plot/table geometry and PDF month cells preserve alignment. Workspace min-width prevents intrinsic table expansion. Local review only.


## Balanced presentation proportions — 2026-10-21

Single-chart slides center the entire chart/table block at 84% of the content width, preserving matching chart/table period geometry and leaving balanced side margins. Single charts use a 28cqw height (compact table charts retain their density-based height); double-chart heights use 19cqw rather than the single-chart height. PPTX and PDF single-chart blocks use the same 84% centered composition. Month inputs use minmax grid columns to avoid settings overflow. Local review only; no GitHub or Windows update.


## Presentation composition correction — 2026-10-21

Supersedes the 84%-width trial: both layouts fill their content columns, use the same 34cqw chart height without tables and density-based 27/23/18cqw heights with tables. Grid rows fit their content and are vertically centered as a shared group, with chart headings aligned at the top. Preview SVG text receives independent horizontal compensation so glyphs retain natural proportions despite plot scaling; double-chart date labels are smaller to avoid collisions. Pie uses its original aspect-preserving rendering. Single PPTX/PDF content width restored. Browser screenshots inspected for single, double and mixed-table layouts; 30 automated tests pass. Local review only.


## Stable chart typography and adaptive bounds — 2026-10-21

Adding a mini-table no longer shrinks chart labels: preview font sizes compensate for density-based chart height in both dimensions; PDF uses the same physical label size independent of table height, and native PPTX explicitly fixes dataLabelFontSize at 10. Line charts fit finite observations with 22% headroom on each side; constant/narrow series use a 4% magnitude minimum span (absolute floor .01). Unlike bars, line charts do not force zero. Bars/columns retain zero with 18% outer padding. Bounds shared with native PowerPoint; raw data and financial formulas unchanged. Current follow-up remains local until user requests another publication.


## Independent mini-table number settings — 2026-10-21

Each selected table metric exposes 0–4 decimal places; nominal volume metrics additionally expose million/billion/trillion units independently of the chart and other table rows. tableRowFormats stores per-metric settings, survives duplicates and P&L basis remapping, and resets on source-type changes. Ratios retain % and changes retain %/points without nominal unit scaling. Shared tableData formatting applies to browser/PDF/editable PPTX tables; raw observations are unchanged. Local review only.


## Presentation versions — local review, 2026-10-21

Sunum oluştur adds a compact version bar with Sürüm adı, Sürümü kaydet and Sürüm aç. Selected files are staged with name/time/slide count; Bu sürümü aç replaces the working deck, Vazgeç preserves it. The confirmation reminds users to save the current deck first. Invalid files produce an inline message and leave current slides unchanged. All text is HTML-escaped.


## Overview deposit cards — 2026-10-21

Dashboard deposit cards now show [37,38,39,42,50]: total deposits, TL deposits, FX deposits, TL time deposits and TL demand deposits. Replace unsupported aggregate time/demand rows 41/49 with existing TL source metrics 42/50; pie compositions and full balance sheet catalog unchanged. Published Windows-Live JS line 167 belongs to bundled PptxGenJS/JSZip vendor code; Node syntax check passes. Exact external diagnostic still required before modifying third-party code. This follow-up remains local pending publication request; version-save feature remains unpublished.
