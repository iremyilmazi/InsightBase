# Accepted changes and current status

> Maintenance rule: every new structural change must update the affected Markdown documents in this documentation set in the same task. Changes to architecture, files, data contracts, row mappings, formulas, UI structure, packaging, scope or operational rules are incomplete until the matching documentation is updated. Update the index/status date and change log as appropriate. V1 was deleted with user authorization on 2026-10-09; V2 is the only maintained version.

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
