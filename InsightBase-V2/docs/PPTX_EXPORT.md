# Presentation editor and editable PowerPoint export

> **Maintenance:** Every development must review and update affected Markdown documents in the same task; record changes, checks and any no-contract-change conclusion in CHANGELOG.md. See [HANDOFF.md](HANDOFF.md).

> Current implementation and publication status: [CURRENT_STATE.md](CURRENT_STATE.md), verified 2026-10-21. Older dated addenda are historical; current decisions supersede conflicting past statements.

## Current presentation contract (2026-10-21)

- 16:9 one/two-chart slides; independent chart dates (max24months), metrics/groups (max6series), BS/PL basis, nominal/MoM/YoY/YTD, units and 0–4 decimals. Templates, defaults, clones, drag sorting and dashboard imports are implemented.
- Mini-table independently chooses rows/groups/measurements and per-row units/decimals, shares dates, max12months/12expandedrows. Labels include measurement/unit; period columns follow chart plot. Chart labels keep physical size when tables are added.
- TL amounts are million TL, USD million USD, ratios %. Currency/ratio mixing checks apply. Weekly inputs use the same partial/completed calendar-month MoM policy as the app; full source precision retained. Defaults use12months, including available current-month data.
- Line scales fit finite observations with22% span padding; minimum span4% of magnitude or .01. Bars retain zero with18% outer padding. Scale bounds do not change financial values.
- Percentage chart labels and mini-table values include a trailing %. Nominal ratios use %, ratio changes use puan, and nominal amounts keep numeric labels with their stated currency/unit. PPTX uses a literal percent suffix for percentage-point-scaled data; pie percentages retain true percent formatting. Negative SVG/PDF bar labels sit outside the negative endpoint (horizontal left/end anchor, vertical below); native PPTX bar/column labels use the supported inEnd placement and dark text.
- PPTX contains native editable charts, embedded selected data, text and tables; PDF is static visual output. Filenames include local date/time/seconds. No vertical value labels on presentation charts; points/bars show values.
- Named portable versions are supported: schema 1 (monthly-only) or schema 2 (hybrid P&L) `.insightbase.json` envelope has app, schemaVersion, name, savedAt, defaults, slides, metricRefs. Definitions exclude workbook observations and runtime IDs. Current Excel is used on restore; saved date ranges stay fixed. Validation caps5MB/100slides, checks identifiers/semantics/enums/ranges/text; import stages confirmation and regenerates IDs. No localStorage/autosave/cloud history.
- Latest published implementation and verification are in CURRENT_STATE. The following dated implementation notes retain evolution history and must not restore old six-month/synthetic-only/TL-only/no-save restrictions.

## Historical implementation notes and subsequent amendments

Accepted and implemented on 2026-10-09. Interface language is Turkish.

## Product contract

`Sunum oluştur` is a separate dashboard navigation view. It offers 16:9 InsightBase slides, one chart or two charts side by side, optional tables below each chart, title, comment, source and footnote fields. Corporate template import is a future extension. Slides can be added, duplicated, reordered and removed (at least one remains). Each slide and chart is independently configured; dashboard group/unit controls are hidden on this view.

Each chart chooses BS or monthly PL, one or more row metrics, one or more sector/private/public groups, line/column/horizontal bar/pie, nominal/MoM/YoY/YTD, million/billion/trillion TL, and start/end months. A chart series is the Cartesian product of metrics and groups. The table independently chooses metrics, groups and measurements, while sharing its chart's period range and unit. Designs exist in memory only: navigation preserves them within the open page; reload closes the design session. No save/reopen function or localStorage is used. Excel refresh retains design selections and updates their values.

## Financial rules

All source amounts are million TL. Nominal amount series divide by 1, 1000 or 1,000,000; ratios remain percent. Amount changes are percentages (nonpositive baseline yields null); ratio changes are percentage points. Maximum two decimal places in preview, tables and chart display formats; underlying chart data keeps precision.

Series contain every selected calendar month, including missing slots. BS values use the last finite observation at/before month end, at most seven days back and within that month. BS MoM compares this month-end snapshot with the preceding month's last observation within seven days of that month end; YoY compares the previous year's same month end; YTD compares prior December end. This is deliberately a month-end series rule, unlike the dashboard's latest-week rolling calendar-month baseline. No weekly WoW option. Defaults use six completed months for BS, excluding a partial newest month; the user can explicitly select any range.

PL uses the monthly source row (49+) and the exact preceding month-end / same-month prior-year baseline. PL YTD is **YTD YoY**, using the matching cumulative row `row-38` versus the previous year's same month, and requiring a current cumulative value from the selected month. It is not growth versus previous December or monthly annualization. Missing values are gaps, never zero; tables show em dash.

Pie charts use only nominal values from the range's final month. Each metric/group is one slice; all source dates must match, every value must be finite and nonnegative, and the sum positive. Selected overlapping metrics or sector-plus-subgroup values are not automatically reconciled: users must select a meaningful mutually exclusive composition. The editor does not infer hierarchy or deduplicate overlapping financial rows.

## Bounds and validation

At most 24 months and six series per chart. Nominal ratios and amounts must be separate charts (currently also enforced for change modes). At least one metric/group and some usable data required. Tables support at most 12 months and 12 rows (metrics × groups × modes). Invalid selections are explained in preview and block export for the entire deck. Each date range is independent; no global slide date filter.

Long tables and labels are dense, especially in two-chart layouts; split them across slides for readability. No dual axes, stacked charts, arbitrary dragging/resizing, template upload, saved designs or automatic narratives yet. All exported objects remain editable in PowerPoint, including chart type/color/data, tables and text.

## Implementation and packaging

`dist/presentation.js` owns session state, selection controls, SVG preview, financial series and native PPTX construction. Public `InsightDeck` interface: render, change, click, points, periods, exportDeck, getState, setContext, problems, tableData. `app.js` passes dataset/template/label/loadState and delegates deck events.

Vendored PptxGenJS 4.0.1 (`vendor/pptxgen.bundle.js`, MIT license in `vendor/PptxGenJS-LICENSE`) includes JSZip. The browser global is `PptxGenJS`, aliased to `window.pptxgen`. `package_three_files.py` embeds the library and presentation module into the single delivery JS; no CDN, package install, internet, AI, additional application files or server-side export needed. Source maps are stripped from the delivery reference.

Export filename: `InsightBase-Sunum_YYYY-MM-DD_HH-mm-ss.pptx`. Native charts include editable XLSX workbooks containing only the chart's selected scaled series; tables and comments are native slide objects. No screenshots of charts. Gaps remain empty chart cache values and blank workbook cells, with `displayBlanksAs: gap`. Arial theme improves Windows compatibility. DEMO synthetic datasets include visible disclosure in preview/export footer and speaker notes. Real data remains local in the browser and downloaded deck.

## Validation

`node --test finora-lens/tests/engine.test.cjs finora-lens/tests/presentation.test.cjs` validates financial baselines, missing months, cumulative YTD and export contents. The exporter test runs the actual vendored browser library in a VM and asserts all four native chart types, embedded workbooks, native tables/text, demo disclosure, no chart images, and missing values remaining blank. Optional `INSIGHTBASE_TEST_PPTX=/private/tmp/example.pptx` writes the synthetic test deck. Browser checks cover two-chart layouts, table/group choices and export completion. LibreOffice rendering is an additional visual check, not a claim of testing in Microsoft PowerPoint or on physical Windows hardware.

## PDF download (2026-10-09)

`PDF indir` sits immediately beside `PowerPoint indir` and exports all current slides in order as separate 16:9 landscape PDF pages. It uses identical metric/group/date/table selections and validations. Titles, comments, sources, footnotes and demo disclosures are included. Filename: `InsightBase-Sunum_YYYY-MM-DD_HH-mm-ss.pdf`.

PDF is a fixed visual output: each page is a 1920×1080 raster canvas embedded with PNG lossless compression, so chart labels and Turkish characters are preserved without font installation. Text is not searchable/selectable and PDF objects are not editable; use the native PPTX output for editing. Line/column/bar use the same SVG financial chart geometry with corrected text proportions; pie proportions remain circular. PDF does not convert the downloaded PPTX or require PowerPoint, printing dialogs, network, AI or an extra server endpoint.

Vendored jsPDF 3.0.3 (`vendor/jspdf.umd.min.js`, MIT license `vendor/jsPDF-LICENSE`) is embedded into the same delivery JS before presentation.js. No optional HTML plugin, html2canvas or dynamic dependencies are invoked. `InsightDeck.exportPDF` manages validation/busy status/download; `pdfSlide` renders a slide canvas. PNG encoding limits canvas lifetime to one page at a time. Both download buttons disable during export. PDF verification covered four synthetic slide pages, all chart kinds, Turkish labels and the 16:9 PDF page size, with Poppler rendering for visual checks. Browser PDF button completes without console errors.

## Timestamped download names (2026-10-11)

Both exports use the shared `downloadName` helper at the save call. Date and time include seconds and follow the computer/browser local clock, not the analysis period or UTC. Format: `InsightBase-Sunum_YYYY-MM-DD_HH-mm-ss.ext`. Zero-padded components and hyphens avoid Windows-invalid colons and slashes. A browser may append its own suffix for repeated downloads within the same second.

Publication update (2026-10-11): the user explicitly authorized uploading this complete current version to iremyilmazi/InsightBase; earlier publication-hold statements are historical and superseded for this release. Private workbook and preview exclusions remain.


## Current schema update — 2026-10-11

The user supplied a new six-sheet reference `şablon (1).xlsx`. DATA_CONTRACT.md is the authoritative current catalog; earlier physical row numbers in this document are superseded. Stable internal metric IDs remain, with explicit `sourceRow`, `format` and `ratio` metadata. BS has 46 supported metrics; P&L 66. Date headers start in C, with B reserved for Format. `extract_structure.py <reference.xlsx>` extracts metadata only and writes both structure.json and structure.js. No financial values are committed.

TL means million TL, USD million USD, % ratio, explicitly confirmed by the user. NPL rows flagged % now use percentage-point changes. Dashboard cards, detail tables, pies and slide outputs preserve each currency. No FX conversion or TL+USD addition occurs. Nominal/pie charts mixing currencies are rejected; growth charts may compare percentage changes and table rows show their own currencies. Monthly P&L-to-cumulative ID offset remains 38 (physical source offset also 38). Removed TL/YP NPL volume rows, branch/headcount and aggregate term/demand source rows are excluded. LDR fallback uses total loans and total deposits, both TL aggregates.

The local 8768 preview keeps synthetic JSON and shows DEMO. The new Windows live delivery excludes Excel; the user provides adjacent dataa.xlsx. Canonical three-file build stays unchanged in count. Additional CMD launcher and guide are operational helpers. Source Excel passed the browser reader with six sheets and zero warnings; 18 engine/presentation tests passed, including ratio deltas and mixed-currency rejection. Local browser preview verified TL/USD labels and USD detail with no page errors. Windows itself remains unverified. This change is not automatically published to GitHub.

New structural changes must update these Markdown files in the same task.


## Unified BS MoM — 2026-10-13

User accepted shared monthly comparison: completed months compare final weekly stock to previous calendar month-end observation (7-day backward limit). Provisional latest month compares latest stock to one calendar month earlier (7-day backward limit, never a future observation). Calendar completion uses current UTC day against month-end. Dashboard, 12-month detail chart and slide MoM use shared engine monthlyCompare; P&L unchanged. Slides default range includes latest available month; provisional source dates remain in point metadata. Dashboard cards mark provisional periods. Missing historical month-end data remains missing; no substitution with early-month values. Windows/GitHub publication deferred until requested.


## P&L reference3 — 2026-10-13

User supplied şablon (3).xlsx. Secondary cumulative/monthly reporting blocks removed; current source catalog is DATA_CONTRACT.md. PL has46 metrics:22 cumulative,22 monthly,2 auxiliary stocks. Monthly source section starts35 instead of46; cumulative Fee/OPEX is31 and monthly58. Net Profit uses monthly51/cumulative24. Stable metric IDs keep dashboard formulas and existing configured charts intact. Each monthly spec explicitly records cumulativeRow and basis; app and slides use pairing metadata. Physical source difference is27, not internal ID difference38. Removed IDs34–43 and72–81 are absent from tables/selectors. English source wording is retained, display prefixes hidden; source title formatting extracted. BS unchanged, including approved commercial label alias. Demo source remains synthetic. Six sheets read with zero warnings, pairing regression and financial/export tests pass. Windows/GitHub not rebuilt for this task; publication remains separately requested.


## Presentation value-axis labels — 2026-10-13

Removed numeric value-axis tick labels from presentation SVG preview and therefore PDF rendering, and set native PPTX valAxisLabelPos=none. Applies to line, column and horizontal bar value axes. Point/bar data labels, category dates, grids and pie labels remain. Dashboard detail charts unchanged. Local preview updated; no Windows/GitHub release.


## Numeric separator convention — 2026-10-13

User requires123,323.21-style numbers. Dashboard and presentation/PDF formatted values use Intl.NumberFormat(en-US), with grouping and maximum2 decimals. Source numeric values/calculations unchanged; Turkish date labels remain. Native PPTX language en-US and chart numeric formats [$-409]#,##0.## (pie percent [$-409]0.##%) request the same convention. Windows/GitHub not rebuilt.


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

Portable .insightbase.json versions have date/time/seconds filenames, preserve all slide and widget authoring options (including P&L basis, groups, fixed date ranges, per-chart precision and per-row table modes/units/precision). Opening uses the current local Excel, never freezes old numeric observations. Catalog metric label/format identities are checked before applying, and missing or changed meanings reject the version. Import validates schema version, maximum 5 MB, 1–100 slides, layout/widget counts, known metric IDs, enum choices, date ranges and bounded text. JSON is never executed. Unknown fields are discarded. Draft/incomplete metric selections can be saved; export validation remains responsible for chart-data readiness. Reopening never auto-shifts date ranges. No localStorage/auto-save, server upload or version database.

## Shared mini-table measurement/unit — 2026-10-21

When all mini-table rows share measurement and unit, show one caption above the period header and only metric/group names on the rows. Nominal volume caption is Hacim and nominal ratio caption is Oran; display expanded Turkish amount units (milyon/milyar/trilyon). Mixed measurements or units keep explicit row metadata and omit the shared caption. Browser preview, native editable PPTX tables and PDF use the same tableData caption/rows. The additional caption is counted in export table height allocation; date columns retain plot alignment. Saved-version schema and financial calculations are unchanged.

The private narrative v4 includes the user's complementary six-month credit-volume table under the ratio chart: total, retail and commercial loans, nominal trillion TL with one decimal. This table provides volume context rather than repeating ratio observations. Local review only.


## Left-column mini-table labels — 2026-10-21

User requested metric names on the left instead of full-width rows above each value row. Mini-tables now use a 28% left label column and 72% equal period columns. Each metric/group/measurement combination occupies one row. The shared measurement/unit caption and mixed-unit fallback remain. Preview uses row-header cells, PPTX uses a native label cell plus period cells, and PDF draws matching columns. Chart plot geometry remains independent; chart category dates are visible again rather than assuming alignment to the table's different grid. This supersedes the full-span-label and plot-aligned-period table layout. Caption/table height allocation counts one row per metric. No schema or calculation changes. Local review only.


## Direct horizontal-bar labels and shared context — 2026-10-21

Horizontal bars identify metrics directly instead of requiring a separate legend. Preview/PDF center white names inside sufficiently wide/tall bars; short/dense bars put the full name immediately above in dark text, retaining outside numeric value labels. Native editable PPTX enables series-name/value labels at center and hides the bar legend. Other chart types retain metric-only legends. Multi-group selections retain group names per series, and mixed source currencies retain currency per series so meanings are not lost.

Chart subtitles share bank group(s), meaningful measurement (Hacim/Oran for nominal), unit, applicable source currency for growth, and a Turkish month/range once below the title. Do not describe ratio-only charts as TL amounts. Common mini-table captions include the single selected table group independently of the chart group; mixed table settings still show their row metadata and group caption. No calculation, unit scaling or version schema changes. Local source/private v6 export only.


## Unambiguous presentation dates — 2026-10-21

Two-digit year labels could be mistaken for a day (Eki 26 meant October 2026). Presentation months now use four-digit years. Single-month selections with one common observed source date show the full observation date in the subtitle. Current incomplete-month chart/table slots use dd.mm.yyyy from actual point sourceDate, never the calendar slot's month-end. Multi-month subtitles use month/full-year start and the actual current partial-month observation date when common. Completed historical slots remain month/year labels. If selected series have different source dates or no observation, keep the month/year label rather than inventing a common date. Single-period horizontal bars omit their redundant category-axis date since the subtitle carries it. Preview, native PPTX caches/tables and PDF use the same rules. Calculation baselines and selected ranges are unchanged.


## P&L completed quarters and open-quarter months — 2026-10-21

Grafik settings for P&L now offer Dönem görünümü: Aylık (default) or Tam çeyrek + açık çeyrek ayları. Hybrid widgets preserve the selected monthly or cumulative source basis. Changing the period view never remaps metric identities; source-type changes reset aggregation to monthly. Both Aylık and Kümülatif remain available while hybrid is active. Duplicates preserve aggregation.

Shared periodSlots/widgetPoints supply quarter and monthly slots to preview, independent mini-tables, editable PPTX chart data/tables and PDF. Full-quarter labels use year plus Ç1–Ç4; open/boundary months use full-year Turkish labels. Missing quarters remain gaps. Chart range remains at most 24 calendar months; tables allow at most 12 displayed slots. See CALCULATIONS for nominal/QoQ/MoM/YoY/YTD rules and unsupported quarterly ratios. Mixed three-month/monthly totals are disclosed in the chart subtitle and sample slide note.

Portable versions with any hybrid widget use schemaVersion 2 and persist aggregation; readers accept schemas 1 and 2. Missing aggregation defaults monthly for older files. Schema 1 cannot contain hybrid semantics, and invalid aggregation and BS hybrid imports are rejected. Monthly-only saves remain schema 1. Older app builds reject schema 2 instead of silently displaying quarter definitions as monthly. No observations are embedded in version files.

## Scoped release authorization — 2026-10-21

Current formatting/date/hybrid/cumulative improvements are authorized for the current application release. The user additionally authorized publishing only v10 at presentations/Sektor-Hikayesi.insightbase.json, with no PDF/PPTX or workbook. Other historical local-only notes are superseded for this release. Future versions still require explicit authorization.
