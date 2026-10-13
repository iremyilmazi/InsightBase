# Presentation editor and editable PowerPoint export

> Maintenance rule: every new structural change MUST update this document and other affected Markdown documents in the same task. Do not publish current work to GitHub until the user explicitly requests it.

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
