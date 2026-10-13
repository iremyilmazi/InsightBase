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
