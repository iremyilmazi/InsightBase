# Accepted changes and current status

> **Maintenance:** Every development must review and update affected Markdown documents in the same task; record changes, checks and any no-contract-change conclusion in CHANGELOG.md. See [HANDOFF.md](HANDOFF.md).

> Current implementation and publication status: [CURRENT_STATE.md](CURRENT_STATE.md), verified 2026-10-21. Older dated addenda are historical; current decisions supersede conflicting past statements.

## V1 freeze — 2026-10-07

Original project preserved in InsightBase-V1 and InsightBase-V1.zip with hash manifest. This protection was superseded by explicit deletion authorization on 2026-10-09. V2 was initially a byte-identical working copy.

## V2 changes accepted in the conversation

- Weekly BS changes replaced by one-calendar-month MoM; YoY and YTD retained.
- Charts now show one selected change series over 12 months; point labels in dialogs.
- Overview replaced Growth rhythm/main table with BS/P&L card blocks.
- Removed sidebar research/phase explanatory text.
- BS source confirmed million TL; removed source-unit choice; single million/billion/trillion display selector.
- Maximum two fractional digits for all financial display values.
- Added credit pie (retail/commercial/cards) and TL/YP loan cards.
- Pie ratios moved to slices; clickable legends show labels/amounts only.
- Restored deterministic highlights, then moved them above both pies.
- Added deposit pie: TL term/demand and FX term/demand.
- BS cards grouped into Krediler / Mevduat, with identical card sizing.
- Removed historical analysis date and latest button; BS/PL use their own latest populated periods.

These changes were incremental; this list records accepted final behavior, not a precise timestamp for each edit.

## Documentation handoff — 2026-10-09

Added comprehensive docs set, complete template row catalog and binding documentation-update rule in agent entry points. Superseded stale V2 instruction claiming no feature changes and replaced stale development README. Documentation-only task; no new product feature or delivery rebuild required.

## Validation evidence and limits

Earlier engine run: 14/14 passed. Browser checks covered unit conversion (percentages unchanged), single-line/detail switching, default MoM with 12 valid points on demo, card dialogs, both pies and subgroup labels, equal BS card dimensions and removed date picker. YoY demo may contain fewer than 12 valid values due to insufficient prior-year data. Do not claim Windows launch was tested. Preview artifacts live in V2, outside delivery.

## V1 removal — 2026-10-09

User explicitly stated V1 was no longer needed. Removed InsightBase-V1 and InsightBase-V1.zip. Updated agent instructions and documentation to make V2 the only maintained version. No V2 runtime or delivery changes. Earlier V1 verification statements above are historical.

## GitHub preparation — 2026-10-09

Added root README and Git allowlist/ignore rules for active V2 only. GitHub Desktop control is currently unavailable; repository creation and upload are not yet confirmed.

## GitHub connection and transfer — 2026-10-09

Verified connected identity iremyilmazi and existing private InsightBase repository with write/admin access. Transferred 32 tracked V2 files (source, documentation and three-file Windows package) to private https://github.com/iremyilmazi/InsightBase through the GitHub plugin; main import commit e2ea6e496521aac4d3e0b78c5da8a57f5827d34d. Workbook data and preview artifacts remain excluded.

## 2026-10-09 — presentation editor

Added Sunum oluştur view: session-only 16:9 layouts, independent metric/group/date/unit selections, line/column/bar/pie, nominal/MoM/YoY/YTD, independent table measurements, slide comments/source/notes and slide management. Bundled offline PptxGenJS 4.0.1 for native editable PPTX export. Three-file Windows delivery retained. BS presentation comparisons use month-end snapshots; PL YTD is cumulative YoY. Added financial/export tests and PPTX_EXPORT.md; updated related handoff documents. User hold: no GitHub publication yet.

## 2026-10-09 — PDF download

Added PDF indir immediately beside PowerPoint indir. All slides export locally as 16:9 landscape pages, including charts, tables, comments and source/footnotes. Vendored jsPDF 3.0.3 within the same delivery JS; no additional application files. PDF is raster visual output; PPTX retains native editability. Verified synthetic four-page PDF, Turkish glyphs, chart kinds and page dimensions. GitHub publication hold remains.

## 2026-10-11 — timestamped exports

PowerPoint and PDF download names now include local save-time date, hour, minute and second, using the common Windows-safe format `InsightBase-Sunum_YYYY-MM-DD_HH-mm-ss.ext`. Updated export documentation and regenerated the three-file delivery. No GitHub publication.

## 2026-10-11 — separate TL and FX deposit pies

Replaced the single overview deposit pie with TL and FX pies, each showing term/demand shares of its own currency total. Credit/TL/FX panels have equal desktop widths and responsive stacking. Updated calculation and product/UI documentation; rebuilt the three-file package.

## 2026-10-11 — shared deposit composition card

TL and FX pies now appear together in one Mevduat dağılımı card, with separate currency subheadings and an internal divider. Credit remains in its own card. Responsive stacking and all currency-specific calculations are preserved. Updated UI/product documents and regenerated delivery.

## 2026-10-11 — current release publication

User authorized GitHub publication of the current project, including slide editor, editable PPTX, PDF, timestamped downloads and the shared TL/FX deposit card. Release checked with financial/export tests and three-file packaging. Earlier publication hold is lifted for this release. Workbook data and preview artifacts remain excluded.


## Windows e-posta demo paketi — 2026-10-11

`InsightBase-Mail-Windows` ve `InsightBase-Windows-Demo.zip` yerel teslim çıktılarıdır. Paket tam beş dosya içerir: üç uygulama dosyası, sentetik `dataa.xlsx` ve `BASLANGIC.md`. Üç dosyalı üretim paketi korunur. Demo çalışma kitabı `package_mail_demo.mjs` ile, `preview_demo.py` tarafından üretilen sentetik JSON üzerinden artifact-tool kullanılarak hazırlanır. Önce `package_three_files.py`, sonra `preview_demo.py` çalıştırılır; builder bundled Node/artifact-tool ortamında çalıştırılır. Rehber kaynağı `finora-lens/WINDOWS_DEMO_README.md` dosyasıdır. Demo Excel’deki `INSIGHTBASE_DEMO` sheet adı uygulamada ve sunumlarda DEMO işaretini etkinleştirir. XLSX okuyucu shared/inline string yanında `t=str` metin hücrelerini de destekler. Gerçek veriler ve yerel demo teslim çıktıları GitHub’a eklenmez. Yeni yapısal değişikliklerde ilgili Markdown belgeleri aynı değişiklik kapsamında güncellenmelidir.


### CMD teslim güncellemesi

Kullanıcının Windows bilgisayarında PowerShell bulunmadığından e-posta paketi altı dosyadır: HTML, CSS, JS, sentetik Excel, `Baslat.cmd` ve rehber. CMD dosyası Edge’i ayrı `%TEMP%\InsightBase-Local` profili ve `--allow-file-access-from-files` ile açar. Sunucu gerekmez. Yerel dosya erişimi paketlenmiş uygulamada desteklenir; normal tarayıcı profili değiştirilmez. Kurum politikaları geçerlidir. Gerçek XLSX okuyucu altı sheet’i uyarısız okudu; yerel file:// akışı Chrome’da aynı bayrakla doğrulandı. Fiziksel Windows doğrulaması yapılmadı. Önceki PowerShell / beş dosya açıklamaları bu teslim için geçersizdir.


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


## Release authorization — 2026-10-12

User authorized publishing the current source to GitHub and rebuilding Windows deliverables. The temporary Windows build hold is lifted for this release. Canonical Windows output has exactly HTML/CSS/JS, with no workbook. Live operational ZIP adds CMD launcher and guide, with no demo or real Excel. Latest schema, TL/USD units, Excel ordering, title hierarchy, subtitle alignment and InsightBase branding are included. Local preview remains synthetic. Workbook and local transfer/demo variants remain excluded from GitHub.


## Reference update — 2026-10-13

Current schema is `şablon (2).xlsx`. BS consumer-loan volume and consumer NPL entries are removed (IDs 13/14); retail loans NPL added as distinct ratio ID112 at source row9. Retail total ID12 remains at source row8. Subsequent BS sources shift up one; stable IDs preserve existing pie/card calculations. BS catalog now has45 metrics; PL retains66 and its source positions. Retail detail uses new ratio plus remaining product breakdowns. Excel source order, title indent/gray/bold and TL/USD/% metadata are regenerated. Local preview retains synthetic data and includes retail NPL. Six source sheets read with zero warnings; existing calculation/export tests passed. Windows packages and GitHub are not rebuilt/published for this task. The current release artifacts therefore remain the preceding release until requested. All structural changes require corresponding MD updates.


## Current release — 2026-10-13

User authorized GitHub publication and Windows rebuild for şablon (2).xlsx support. Previous deferred-build statement is superseded for this release. Windows app output contains exactly three application files; live operational packages add launcher and guide without any Excel. Synthetic local preview remains separate.


## Delivery cleanup — 2026-10-13

User authorized removal of obsolete transfer/delivery artifacts. Removed demo/mail/TXT demo directories and archives, plus duplicate Live-TXT folders numbered2/3/4. Retained current Live and Live-TXT directories/ZIPs and the mandated canonical three-file Windows output/ZIP. Source, local synthetic browser preview and build scripts are preserved. Do not recreate historical demo transfer artifacts during routine production builds.


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


## GitHub publication — 2026-10-13

User authorized publishing current source: unified monthly BS comparisons, global PL Monthly/Cumulative filter, original English PL labels without basis prefixes, removal of table subtitles, commercial credit wording and simplified tab entries. Windows packages are not regenerated for this source publication and remain the preceding delivery release.


## Highlight scope — 2026-10-13

User is revising highlights incrementally. First accepted change: exclude all P&L metrics. Current candidates are BS total loans(ID3), total deposits(ID37), credit cards(ID31); existing absolute MoM ranking remains pending further instructions. PL basis selection no longer affects highlight candidates. Source-only demo updated; no Windows build or GitHub publication.


## Expanded BS highlights — 2026-10-13

Implemented in pure dist/highlights.js (InsightHighlights.analyze), bundled by preview and Windows builders without changing the three-file contract. It reads BS only and emits up to one growth, funding and NPL/risk card; insufficient data may yield fewer cards. Candidate rules: volume MoM, product-vs-total growth, TL/USD growth difference, TL/FX demand-deposit share changes, loan/deposit growth difference, LDR and NPL point changes, completed-month credit acceleration, sector-view private/public growth differences. Composition and contribution are excluded pending scope confirmation. Shared monthlyCompare supplies MoM bases. Derived metrics require identical current/base dates. Demand shares additionally require nonnegative same-currency components and 0.5% total reconciliation at both dates.

No financial significance cutoff or anomaly label is invented. For completed periods with12 prior valid completed observations (searching36months), selection ranks empirical absolute deviation from each candidate's own median; MAD is also recorded. Tied scores use stable IDs. Provisional periods cannot use this history ranking. Without comparable history, explicit fallback kind priority is share, fundingGap, currency, product, ratio, growth, groups, acceleration; within a kind, absolute change ranks candidates. This is a deterministic editorial selection, not a financial importance score. Historical values and scoring details are available in analyze return metadata; card method disclosure explains history/fallback choice. Empty, invalid or unchanged candidates are skipped; missing values are never zero-filled. No inferred funding cost or NPL cause is asserted. P&L basis cannot affect cards. Local preview updated; no GitHub publication or Windows rebuilding requested for this change.


## P&L reference3 — 2026-10-13

User supplied şablon (3).xlsx. Secondary cumulative/monthly reporting blocks removed; current source catalog is DATA_CONTRACT.md. PL has46 metrics:22 cumulative,22 monthly,2 auxiliary stocks. Monthly source section starts35 instead of46; cumulative Fee/OPEX is31 and monthly58. Net Profit uses monthly51/cumulative24. Stable metric IDs keep dashboard formulas and existing configured charts intact. Each monthly spec explicitly records cumulativeRow and basis; app and slides use pairing metadata. Physical source difference is27, not internal ID difference38. Removed IDs34–43 and72–81 are absent from tables/selectors. English source wording is retained, display prefixes hidden; source title formatting extracted. BS unchanged, including approved commercial label alias. Demo source remains synthetic. Six sheets read with zero warnings, pairing regression and financial/export tests pass. Windows/GitHub not rebuilt for this task; publication remains separately requested.


## Release publication — 2026-10-13

User authorized GitHub publication and Windows packages for current reference3 and expanded BS highlights. Prior deferred statements are superseded for this release. Three-file canonical build includes highlights module; live delivery adds CMD launcher/guide, no Excel. Both standard and TXT variants updated; local demo remains separate. 23 automated tests pass.


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


## Real local workbook — 2026-10-13

User supplied populated şablon (4).xlsx and requested replacing synthetic preview. Private working copy is InsightBase-V2/local-data/dataa.xlsx (directory ignored by Git). preview_demo.py now defaults to real-workbook mode whenever this file exists, directly building source app, copying adjacent workbook to temporary8768 preview and removing demo-data.json. No JSON fetch patch or DEMO flag is used. --demo is an explicit synthetic-only override; routine --source refresh keeps real data. Source reference4 read with6sheets and zero warnings, same BS45/PL46 schema. Values are never embedded in code/docs or Windows/GitHub deliverables. User original workbook unchanged. Later workbook updates should replace private dataa.xlsx and rerun source preview. This supersedes all prior instructions to keep local preview synthetic.


## Current source and Windows publication — 2026-10-13

User authorized publishing latest source and rebuilding no-data Windows deliveries. Includes ratio level option, simplified presentation value axes,12-month composition history and arbitrary-month comparison, native pie hover values, en-US numeric separators, real local-workbook preview workflow. Custom floating tooltip is reverted. Private local-data/dataa.xlsx and temporary preview Excel are excluded. 26 tests pass. Previous deferred-release statements are superseded for this release.


## Analysis view rollback — 2026-10-18

User rejected the two trial integrations and requested rollback. Esnek karşılaştırma and Kâr köprüsü are not part of the active product. Removed analysis module/tests, navigation, view registry, events, CSS and loader/bundler hooks. Earlier dashboard, comparison, ratio/composition history, P&L and presentation features retained. Separate synthetic demo in outputs remains isolated for possible future reference. Neither integration was published to GitHub or Windows deliverables, so no release rebuild is needed. Real local workbook remains the active preview input.


## GitHub Raw Windows workflow — 2026-10-20

User now updates the other Windows PC by copying GitHub Raw content, not email. Publish exactly five files under InsightBase-V2/InsightBase-Windows-Live: BASLANGIC.md, Baslat.cmd, InsightBase.css/html/js. Sixth user-local dataa.xlsx must never be committed or overwritten by updates. Explicit gitignore whitelist publishes only the five files; live ZIP, TXT copies and all Excel stay excluded. Canonical InsightBase-Windows still contains exactly three application files. package_windows_live.py defaults to normal live output only; --txt is legacy opt-in. Guide explains authenticated Raw access, full-content copy, UTF-8, visible extensions, same-version updates, local workbook preservation, launch and hard refresh. .gitattributes requests CRLF for CMD and LF for other live files. No updater or network access added to running application. Current code includes rollback of the two trial analysis views. Publishing this five-file folder is authorized by the current request.


## Public access request — 2026-10-20

User explicitly requested public repository access without dataa.xlsx. Audit of10 commits reachable from main found no XLS/XLSX/CSV/TSV, dataa paths, local-data or dotenv files. Publishing Raw-copyable5-file directory is in progress. Repository remains private until administrator changes visibility; current GitHub connector lacks administration capability and browser has no signed-in GitHub session. Do not claim public visibility until verified. Private workbook remains excluded; no demo workbook is published.


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


## Publication approved — 2026-10-21

User approved the current presentation workflow, compact settings, independent table metrics, per-chart decimal selection and refined chart/table composition for GitHub publication. This supersedes the local-only publication hold for this release. Rebuild canonical three-file application and five Windows-Live Raw files to keep source and browser-copyable distribution consistent. Workbook, private preview and TXT transfer packages remain excluded.


## Stable chart typography and adaptive bounds — 2026-10-21

Adding a mini-table no longer shrinks chart labels: preview font sizes compensate for density-based chart height in both dimensions; PDF uses the same physical label size independent of table height, and native PPTX explicitly fixes dataLabelFontSize at 10. Line charts fit finite observations with 22% headroom on each side; constant/narrow series use a 4% magnitude minimum span (absolute floor .01). Unlike bars, line charts do not force zero. Bars/columns retain zero with 18% outer padding. Bounds shared with native PowerPoint; raw data and financial formulas unchanged. Current follow-up remains local until user requests another publication.


## Independent mini-table number settings — 2026-10-21

Each selected table metric exposes 0–4 decimal places; nominal volume metrics additionally expose million/billion/trillion units independently of the chart and other table rows. tableRowFormats stores per-metric settings, survives duplicates and P&L basis remapping, and resets on source-type changes. Ratios retain % and changes retain %/points without nominal unit scaling. Shared tableData formatting applies to browser/PDF/editable PPTX tables; raw observations are unchanged. Local review only.


## Follow-up release approved — 2026-10-21

User approved publishing stable chart-label typography, adaptive line bounds and independent table-row unit/decimal settings. All 32 automated tests pass. Canonical source and Windows-Live Raw distribution are rebuilt together; real workbook and TXT/private preview remain excluded.


## Presentation versions — local review, 2026-10-21

Added explicitly requested portable presentation versions for local review. Previous prohibition on save/open is superseded for this feature. No GitHub, Windows/Raw or package updates until user approval. Feature exports definitions only and recalculates against local Excel, stages imported versions before replacement and rejects incompatible files without changing the working deck.

Validation: 36 automated tests passed. Headless Chrome E2E passed a five-slide/four-chart-type save → browser refresh → staged open → exact restore → native PPTX/PDF export workflow, including cancel, invalid/future files and zero browser errors. A dedicated test confirms changed local Excel values recalculate after restore while saved date ranges remain unchanged. No publication or distribution rebuild performed.


## Published-file diagnostic follow-up — 2026-10-21

Verified local Windows-Live JS/CSS Git blob hashes match public main. Node syntax check passes for published bundled JS. Removed repeated showCatName/showTitle object properties from native presentation chart options (identical values, no behavior change). Added standard line-clamp next to prefixed declaration for editor compatibility. User reported 3 JS / 1 CSS diagnostics on another PC; exact messages/tool remain needed to identify the third JS report and confirm CSS diagnostic. These fixes and version feature remain unpublished; no delivery rebuild.


Diagnostic-only publication: ab3a652a7a822855ca84580da49c5e3e3a204bcd updates duplicate chart keys and standard line-clamp in source and Windows Raw files. Version save/open remains unpublished. Local delivery JS/CSS match this diagnostic-only release; do not run the full package builder until version feature publication is authorized.


## Overview deposit cards — 2026-10-21

Dashboard deposit cards now show [37,38,39,42,50]: total deposits, TL deposits, FX deposits, TL time deposits and TL demand deposits. Replace unsupported aggregate time/demand rows 41/49 with existing TL source metrics 42/50; pie compositions and full balance sheet catalog unchanged. Published Windows-Live JS line 167 belongs to bundled PptxGenJS/JSZip vendor code; Node syntax check passes. Exact external diagnostic still required before modifying third-party code. This follow-up remains local pending publication request; version-save feature remains unpublished.


## Private workbook refresh — 2026-10-21

User-supplied populated şablon (5).xlsx replaces local-data/dataa.xlsx byte-for-byte. Six sheet names and all metric labels/units remain compatible; differences in empty P&L B cells are blank-cell serialization only. BS has 94 date columns and latest populated date 2026-10-16 for all groups; P&L has 21 date columns and latest populated date 2026-08-31. Native app reader loads BS45/PL46 metrics per sheet with zero warnings, no Excel error cells found, and overview TL time/demand cards populate. Source preview refreshed from private workbook; no schema remap, package rebuild or GitHub upload. Real values remain ignored and unembedded.


## Portable-version release authorized — 2026-10-21

User approved GitHub publication of the complete current project including portable presentation version save/open, diagnostic cleanup and overview TL time/demand deposit cards. Previous local-only holds for these features are lifted. Rebuild canonical three-file app and five Windows-Live Raw files; do not include private workbook, saved presentation version files, TXT variants or private test exports. 36 automated tests passed; rerun browser version workflow on the latest private workbook before publication.

## 2026-10-21 — Consolidated agent handoff documentation

User requested complete agent-readable requirements, structure and rules, plus an every-development update obligation. Rewrote root/V2 instructions and readme entry points; added CURRENT_STATE, REQUIREMENTS and HANDOFF; refreshed Architecture, Product and Development; clarified authoritative current presentation contract and overview deposit IDs. Corrected obsolete synthetic-only/PowerShell/no-save guidance and marked historical addenda as superseded. No application code, financial formulas, schema IDs, packages or real workbook contents changed. Documentation-only work remains local; no GitHub publication implied. Validate local Markdown links and current-state claims against source.

Documentation verification completed: 16 Markdown entry/specialist files scanned; zero broken relative links. Source inspection confirmed current CMD launcher, package counts, portable-version envelope, deposit card IDs and monthlyCompare partial/completed behavior. Application code unchanged, so no additional application regression run required for this documentation-only change.


## 2026-10-21 — Documentation publication authorized

User approved uploading the agent handoff Markdown files. Publish documentation-only changes; preserve application/Windows file SHAs and exclude private workbook/test artifacts. No application rebuild or new financial behavior. Relative Markdown links verified before publication.

## 2026-10-21 — Private sector narrative presentation draft

Created the user-requested three-slide sector narrative with separate credit, deposit and P&L pages through the existing InsightBase presentation editor. Outputs remain private under ignored root outputs/sunum-2026-10-21: portable presentation definition, editable PPTX and visual PDF. Titles/comments are editorial text fixed to the source dates shown on each slide; reopening recalculates charts but does not rewrite those messages. No private financial observations are reproduced in documentation.

Verification: current private workbook loaded through the app reader with no warnings; all six widget configurations passed the app's export validation. Portable version was reopened through the actual file chooser. PPTX and PDF downloads completed with zero browser page errors. PDF has three pages; PPTX has six native charts, six embedded chart workbooks and native tables on all three slides. All browser slide previews and all rendered PDF pages inspected. No application source, calculation, schema, UI or packaging contract changed, so no additional application regression run was required. Existing source/package work was preserved. No GitHub publication or Windows rebuild.


## 2026-10-21 — Percentage suffixes and visible negative bar labels

User requested presentation-format corrections without changing messages. Percentage chart/mini-table values now carry %, while ratio movements retain puan and nominal amounts retain their original units. Native PPTX uses quoted literal suffixes for percentage-point-scaled series so data is not multiplied by 100; pie percentage formatting is unchanged. Negative SVG/PDF horizontal-bar labels move outside the left endpoint with end anchoring; negative column labels move below the endpoint instead of inside the fill. Native bar/column labels use supported inEnd placement with dark text (the bundled library filters outEnd for clustered bars).

Verification: all 38 Node tests passed, including new regressions for negative horizontal/vertical geometry, ratio-versus-growth units, native number formats/label position and unchanged raw chart values. Source preview regenerated; three-slide saved narrative version opened through the real chooser with exact equality of slide definitions/text. All three negative percent labels verified in actual chart DOM; all browser slide screenshots and rendered PDF pages inspected. PPTX/PDF exports succeeded with zero browser page errors, three PDF pages and literal-percent native chart formats. Updated private outputs under ignored outputs/sunum-2026-10-21/format-v2. Financial calculations, workbook mapping, authoring schema and narrative text did not change. No Windows rebuild, GitHub publication or private-data disclosure.

## 2026-10-21 — Simplified private narrative deck v3

User requested a cleaner presentation with clearer messages and no table repeating chart evidence. Updated only the private saved presentation and exports under ignored outputs/sunum-2026-10-21/yalin-v3. Removed all three redundant mini-tables, reduced the deposit comparison to the current monthly period, removed an unnecessary deposit series, shortened titles/comments and removed the unrelated cumulative P&L digression. Existing percentage suffixes and visible negative labels are retained. Source dates and provisional-month comparison remain explicit.

Verification: version reopened through the app file chooser, all three pages rendered without tables, six native charts exported in a three-slide PPTX, three-page PDF exported, and zero browser page errors. All browser previews and rendered PDF pages inspected. Reviewed presentation/UI contracts: no application, calculation, schema or default-template contract changed; this is an editorial revision to one private deck. No application regression rerun needed, Windows rebuild or GitHub publication performed. No private financial observations reproduced in documentation.


## 2026-10-21 — Complementary credit table and shared table metadata

User provided a screenshot adding six monthly nominal credit-volume rows below the credit-ratio chart. Reproduced its metric order, source period, trillion-TL units and one-decimal precision in private narrative v4. Simplified common table metadata at application level: one shared measurement/unit caption replaces repeated row suffixes; mixed units/measurements remain explicit on individual rows. Preview uses a table caption; PPTX uses a spanning native cell; PDF includes the same caption with row allocation adjusted. Financial formulas, data schema and version-file schema are unchanged.

Verification: 39 automated tests passed, including homogeneous caption/metric-only rows, mixed-unit fallback and unchanged values. Real-workbook browser import reopened the three-slide v4, asserted exactly one complementary table and its expected caption/metric order, exported PPTX/PDF with zero page errors. Native PPTX has one shared caption and native table with no repeated old row metadata; PDF has three pages. Credit preview and all PDF pages visually inspected. Outputs remain ignored under outputs/sunum-2026-10-21/hacim-v4. No private observations in documentation, Windows rebuild or GitHub publication.


## 2026-10-21 — Left-column metric labels

Moved mini-table metric names from separate full-width label rows into a dedicated left column at the user's request. All values for each metric now share the same row. Common measurement/unit caption remains once above the table; mixed settings retain row-level meaning. Updated preview, editable PPTX and PDF consistently. Chart geometry is preserved and category dates restored so the independently laid-out table does not imply shared plot alignment. Private narrative v5 retains v4 metric selections, source periods, precision and messages.

Verification: 39 Node tests passed, including row-header/value geometry assertions. Browser v5 reopen verified left-column metric names and shared caption, successful exports and zero page errors. Native PPTX table verified as five rows (caption, dates, three metrics) with seven cells per metric (label plus six months). Three PDF pages and browser credit preview visually inspected. No financial/calculation/version schema changes, Windows rebuild or GitHub publication. Private artifacts stay under ignored outputs/sunum-2026-10-21/solda-v5.


## 2026-10-21 — Bar names and consolidated chart/table context

User requested identifying horizontal bars directly and moving repeated sector/currency information into heading context. Added full metric names inside wide preview/PDF bars with white text and a dark above-bar fallback for short/dense bars. Numeric labels retain negative endpoints and percent/point semantics. Removed horizontal legends; other legends show only metric names unless group/currency disambiguation is needed. Native PPTX enables series-name/value labels at center and removes the bar legend. Common group, measurement, unit/source currency and Turkish month/range appear below chart headings. Single-group tables include their own group in the caption, even with mixed row settings.

Verification: 40 automated tests passed, including direct labels/short-bar fallback, removed legends, shared context and existing native export/units/financial checks. Three-slide v6 reopened in browser and exported without page errors. Four native horizontal charts verified to enable series names, center positioning and omit legends. All three rendered PDF pages inspected for direct name readability and retained negative values; credit preview and prior full-slide preview set inspected. Financial formulas, raw observations, saved selections/messages and version schema unchanged. Private v6 artifacts remain ignored; no Windows rebuild or GitHub publication.


## 2026-10-21 — Source dates instead of ambiguous short years

User interpreted the month/two-digit-year chart label as a day. Replaced two-digit presentation years with full years and display actual common observation dates for single-period subtitles/current partial-month chart and table slots. Single-period horizontal category labels are suppressed as redundant. Dates derive from point sourceDate, with month/year fallback for missing or differing series dates. No financial observations, dates, baselines or saved range definitions changed.

Verification: all 41 automated tests passed, including fixed-clock regression for full source dates versus monthly slots, native subtitle/cache date labels and partial-month table header. Browser v7 reopened unchanged financial selections, asserted observation-date subtitle/table, exported PPTX/PDF without page errors. Native chart/table/subtitle labels verified; three PDF pages and credit browser preview visually inspected. Private artifacts remain ignored under outputs/sunum-2026-10-21/tarih-v7. Financial/data/version contracts reviewed unchanged; presentation display contract updated. No Windows rebuild or GitHub publication.


## 2026-10-21 — Hybrid P&L quarterly/monthly presentation and deposit selection

Implemented the user-requested P&L period control: full calendar quarters sum exact monthly flow observations, while open/boundary quarter months remain separate. Shared slots/series drive preview, tables and native PPTX/PDF. Missing months invalidate a quarter; change compares quarter-to-quarter or month-to-month appropriately, YoY uses matching lengths, and YTD uses existing exact-month cumulative pairing. Ratios explicitly require monthly mode because no valid quarterly denominator is supplied. Aggregation persists through duplication and schema-2 versions, with schema-1 backward support and rejection of invalid/downgraded hybrid semantics. Reviewed data mapping: no workbook/catalog changes. Dashboard and BS calculation contracts unchanged.

Also applied the user's follow-up to the private deck: right-hand deposit chart now shows total TL deposits, TL time deposits and TL demand deposits, in that order. Private narrative v8 updates the P&L example to the hybrid view with an explicit three-month/monthly disclosure.

Verification: 46 automated tests passed, covering quarter sums/gaps, like-period comparisons, leading partial quarters, year boundaries, latest-data caps, ratio restrictions, cumulative metric/settings remap, version validation/restore and editable chart contents. Real-workbook browser UI selected hybrid mode and checked both quarter totals against independent sums of exact monthly observations, retained the two available open-quarter months, restored a schema-2 version through the chooser and exported PPTX/PDF with zero page errors. Native quarter/month cache labels verified; three PDF pages and P&L browser preview visually inspected. Final deposit follow-up exported in the same v8. Artifacts remain ignored; no private observations in docs, Windows rebuild or GitHub publication.


## 2026-10-21 — Preserve cumulative P&L in hybrid view

Corrected the unnecessary forced-monthly limitation identified by the user. Quarter-plus-month grouping and monthly/cumulative basis are independent. The cumulative selector remains available; changing grouping preserves identities and independent row settings. Cumulative hybrid values come directly from exact quarter/month-end source cumulative rows, never sums. Missing endpoints stay missing; changes use matching quarter/month-end cumulative levels within the same year, with Q1 year-reset comparison unavailable. YoY/YTD YoY use exact same prior-year month. Ratio restrictions remain. Schema-2 imports now accept cumulative hybrid definitions. Workbook mapping reviewed unchanged.

Verification: 47 Node tests passed. Browser UI selected cumulative basis while retaining hybrid periods, compared all four displayed values to exact cumulative Excel source observations, restored the saved version and exported PPTX/PDF with zero page errors. Private narrative v9 preserves the deposit trio and updates the left P&L chart/note to cumulative endpoints. No Windows rebuild or GitHub publication.

## 2026-10-21 — Match the user's wider cumulative P&L view

Updated private narrative v10 P&L left chart to the supplied screenshot: January 2025 through August 2026, cumulative Net Profit, four completed prior-year quarters, two current-year quarters and two available open-quarter months. Retained the right monthly YoY comparison and other slide configurations. Kept a correct cumulative-source note instead of the screenshot's outdated three-month-total wording.

Verification: browser UI changed the date range, all eight chart values matched exact source cumulative endpoints, schema-2 saved version reopened, PPTX/PDF exported with zero page errors. PDF has three pages; P&L page visually inspected against the screenshot. This is a private deck configuration update; application, calculations and version contracts reviewed unchanged. No application regression rerun, Windows rebuild or GitHub publication. Artifacts remain ignored under outputs/sunum-2026-10-21/genis-v10.


## 2026-10-21 — Current application and v10 publication authorized

User explicitly requested publishing the current application plus the working v10 presentation definition, with no PDF/PPTX. Added only presentations/Sektor-Hikayesi.insightbase.json and its usage guide, documenting the narrow saved-version exception in instructions/current state/development. Real Excel, observation series and all private outputs remain excluded. Source, canonical three-file Windows app and five-file Live wrapper rebuilt together.

Pre-publication verification: remote main inspected at 739d9198fb36422694c6d0b4ac1fc8a3e0df6e8e and local blob hashes compared with its recursive tree, preserving unchanged remote files. All 47 Node tests passed; rebuilt bundled JS syntax check passed; builders asserted exactly three/five distribution files. Current v10 previously passed real-workbook source/browser/schema-2 restore/export and eight cumulative endpoint checks. Publication uses the inspected remote parent and expected-head, non-forced update. Only the approved version is included; no financial observations reproduced in docs.

Production-bundle verification also passed before publication: staged rebuilt HTML/CSS/JS read the real adjacent workbook, restored the approved v10 definition, retained eight cumulative P&L periods and the requested deposit trio, with no configuration or browser page errors. Physical Windows execution remains unverified.

Publication verified: application/deck commit dc99aed685b0817c0e7f0a0a9e195965ae2fe7a7 is on main. All 25 changed file SHAs match the release manifest; all unchanged remote files were preserved. The resulting tree contains 57 files and no Excel, PDF/PPTX, screenshots or local-data paths. The only presentation definition is the explicitly approved v10 file. This follow-up records the verified application commit; it changes documentation only.


## 2026-10-22 — Independent balance-sheet/P&L table source

Added Tablo veri kaynağı selector and independent table P&L monthly/cumulative basis. Each table selects one catalog independently from chart settings. Source changes clear stale table-only IDs/modes/formats/search; basis changes remap table rows/settings without altering the chart. Labels, currencies, ratios and validation now resolve through tableWidget/tablePoints. Cross-source captions identify the source; BS rows on hybrid P&L charts are endpoint stocks rather than quarter sums. Wide period headers are compact/wrapping.

Independent source/basis definitions use schema 3, typed metric references and table-catalog validation; schemas 1/2 inherit their original source/basis and remain supported. Invalid/downgraded imports reject without replacing the working deck. Reviewed DATA_CONTRACT: no workbook/schema ID changes. Financial formulas remain unchanged; source routing and period alignment are explicit in CALCULATIONS.

Verification: all 50 Node tests passed, including cross-source quarter stock versus flow totals, independent table controls/formats, typed schema-3 round-trip/rejection, legacy compatibility and native table exports. Real-workbook browser UI changed P&L-chart tables to BS, independently selected metrics/units/precision, matched all cells to source endpoint observations and preserved chart configuration. Schema-3 file chooser restore, PDF/PPTX downloads and table-only cumulative selection passed with zero browser page errors. Credit/table preview and rendered P&L PDF page visually inspected; native table source captions/BS labels verified. Private check artifacts remain in /private/tmp. Published v10, GitHub and Windows packages unchanged.

## 2026-10-22 — Add the user's P&L YoY table to the working deck

Created private narrative v11 matching the supplied screenshot: left P&L chart retains cumulative Net Profit and its existing quarter/month slots, while its independent P&L table uses monthly Net Profit, YoY measurement and one decimal. Historical comparisons without source history remain unavailable. Other slide configurations and the right P&L chart are unchanged. This uses the local schema-3 table-source/basis feature; published v10 remains unchanged.

Verification: actual browser table controls selected P&L/monthly source, metric, YoY and precision. All displayed table cells matched the screenshot, the chart remained cumulative, and the other two slides/right chart were deep-compared unchanged. Version downloaded through the real save button and restored through the chooser, preserving the table exactly, with zero browser page errors. P&L slide preview visually inspected. No application/calculation/schema contract changes in this artifact-only task, so no additional regression run required. No PDF/PPTX generated, Windows rebuild or GitHub publication. Private definition/preview remain ignored under outputs/sunum-2026-10-22/yoy-tablo-v11; no private financial values in documentation.

## 2026-10-22 — Strengthen the private deck's deposit message

Applied the user's accepted deposit narrative proposal to private v12: title contrasts faster deposit growth with declining TL demand share; the slide comment gives the prior/current TL demand share and movement, the LDR change, and concentration in time deposits. Retained both existing charts and the requested TL-total/time/demand ordering. The P&L YoY table from v11 and credit page remain unchanged.

Verification: recalculated demand/total shares at exactly matched current and engine-selected comparison dates, checked nonnegative components and reconciliation at both dates, and derived LDR movement from the same engine comparison. Browser controls updated only deposit title/comment, deep comparisons confirmed all widgets and other slides unchanged. The real version-save download and file-chooser restore preserved the new text; no browser page errors. Deposit slide visually inspected. No application/calculation/schema contract change or additional regression run, no PDF/PPTX generation, Windows rebuild or GitHub publication. Private v12 definition/preview remain ignored under outputs/sunum-2026-10-22/mevduat-v12; no private observations in documentation.

## 2026-10-22 — Audit narrative context across the private deck

Applied the user-approved deposit explanation connecting displayed time/demand growth to the change in demand share, replacing the isolated share-change line. Removed unsupported standalone LDR figures from the comment and explained the credit/deposit growth relationship instead. Audited all three pages: credit commentary now directly interprets the displayed growth/risk comparisons; P&L headline/comment reference the displayed annual comparison rather than an unshown monthly recovery. P&L left chart title explicitly says cumulative; the note distinguishes cumulative chart, period-flow YoY table and monthly YoY right chart.

Verification: numeric deposit/P&L messages recalculated from current local source observations, all chart/table financial configurations deep-compared unchanged, schema-3 version downloaded and restored with exact slide equality and zero browser page errors. All three final slide previews inspected. Private v13 stays ignored under outputs/sunum-2026-10-22/baglam-v13. No app/calculation/schema contract changed, no additional application regression run, PDF/PPTX generation, Windows rebuild or GitHub publication. No private financial values in documentation.


## 2026-10-22 — Publish independent table sources and context-reviewed v13

User explicitly authorized the latest version. Replaced the single approved presentation path with v13 (schema 3) including the P&L period-flow YoY table and context-reviewed credit/deposit/P&L text. Release includes independent table source/basis support and matching source/three-file Windows/five-file Live output. No PDF/PPTX, Excel or other private outputs included.

Pre-publication checks: remote main inspected at ec3de1645552438a00ce4d79f5895bb070f00de4, preserving its tree as the release base. All 50 Node tests passed. Previous real-workbook UI tests verified independent source/basis, exact stock endpoint values, schema-3 restore/export and exact current narrative restore; all three final slide previews inspected. Publication uses a non-forced expected-head update and resulting blob hashes are checked.

Rebuilt production bundle also passed the real-Excel/approved-v13 restore check: three slides, eight cumulative P&L periods, requested deposit trio and no configuration/browser page errors. Canonical/Live file counts and bundled JS syntax passed. Physical Windows testing remains unverified.

Publication verified: application/v13 commit 228ed174d2fd4e69f37cf141024a10c513c1b271 is on main. All 22 changed file SHAs match the manifest, unchanged remote files are preserved, and the 57-file tree contains no Excel, PDF/PPTX, screenshots or local-data. Windows Raw JS/CSS and the schema-3 v13 definition match local approved content. This follow-up records verification in documentation only.
