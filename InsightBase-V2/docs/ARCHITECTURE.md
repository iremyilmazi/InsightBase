# Architecture and source inventory

> Maintenance rule: every new structural change must update the affected Markdown documents in this documentation set in the same task. Changes to architecture, files, data contracts, row mappings, formulas, UI structure, packaging, scope or operational rules are incomplete until the matching documentation is updated. Update the index/status date and change log as appropriate. V1 was deleted with user authorization on 2026-10-09; V2 is the only maintained version.

## Directory tree

```text
InsightBase-V2/
  AGENTS.md
  docs/                     this handoff documentation
  finora-lens/
    README.md               development entry point
    dist/                   canonical editable browser source, despite directory name
      index.html            shell, navigation, dialogs, single display-unit selector
      styles.css            UI styling, responsive layouts, SVG label styling
      app.js                state, view rendering, chart/pie/highlight selection, load lifecycle
      presentation.js       slide session state, SVG preview, editable PPTX export
      engine.js             pure financial functions, Node-compatible tests
      xlsx.js               browser-native ZIP/XML workbook reader
      structure.json        exact template row labels and structure metadata
      structure.js          browser TEMPLATE representation
    vendor/                 offline PptxGenJS 4.0.1 / jsPDF 3.0.3 bundles and MIT licenses
    package_three_files.py  active production builder
    package_local.py        legacy builder; supplies PowerShell string via AST to active builder
    extract_structure.py    extracts template labels/dates (not real financial data)
    preview_demo.py         synthetic preview generator; patches preview JS only
    local_server.py         legacy development helper
    update_local.py         legacy migration script; do not rerun casually
    tests/
      engine.test.cjs
      presentation.test.cjs
      local_server_test.py  tests legacy local_server helper, not Windows PowerShell
  InsightBase-Windows/
    InsightBase.html
    InsightBase.css
    InsightBase.js
  InsightBase-Windows.zip   same three entries, root of archive
  *preview.jpg             review artifacts, not production assets
```

## Browser execution flow

HTML shell → bundled `TEMPLATE` → `FinoraEngine` → `LocalXLSX` → vendored PptxGenJS + jsPDF + InsightDeck → Windows setup helper → app entry point → `loadWorkbook()` → fetch local Excel with `cache: no-store` → parser → dataset → render current view.

No framework, npm build or remote chart/XLSX library. Browser charts are SVG; a vendored offline PptxGenJS library builds native editable PowerPoint charts. Native APIs include `DOMParser`, `TextDecoder`, `Blob`, `Response`, `DecompressionStream('deflate-raw')`, `AbortController`, and `<dialog>`.

## Global interfaces

- `InsightDeck`: presentation session/editor/export API; see PPTX_EXPORT.md.
- `PptxGenJS` / `window.pptxgen`: native PPTX generation (vendored).
- `TEMPLATE`: workbook row schema from structure.js.
- `FinoraEngine`: `DAY`, `iso`, `shift`, `monthEnd`, `monthAgo`, `finite`, `pct`, `at`, `compare`, `series`, `metricSeries`, `cumulativeYoY`, `monthlyChanges`.
- `LocalXLSX.read(file, template)`: Promise of sheets/warnings.
- App `state`: view, group, date (internal latest fallback, no picker), unit (1/1000/1000000), basis, horizon, legacy trend.
- `dataset`: sheets, warnings, demo, hasValues. Read state: loading/ready/error, error message, load token, lastRead.
- Optional browser WebMCP `set_insightbase_view` after packaging changes view/group only. It is optional; production does not require an agent or AI access.

## Important functions

`metric()` uses `latestDate(type,group)`; `getSeries()` preserves source-million values. `render()` produces the current screen, `overview()` produces overview sections, `loanPie(currency)` renders credit (null), TL deposit or FX deposit composition, `insights()` ranks six MoM candidates, `showDetail()` opens a drilldown, `chartPoints()` gets monthly changes and `chart()` renders one SVG line.

Refresh clears the current dataset while loading; errors show an error state instead of retaining old values as current. A token prevents stale concurrent responses overwriting newer loads. There is no background refresh timer or persisted data cache.

PDF export uses high-resolution local canvas pages and vendored jsPDF; see PPTX_EXPORT.md for visual-output limitations. No delivery file or runtime endpoint is added.


## Windows e-posta demo paketi — 2026-10-11

`InsightBase-Mail-Windows` ve `InsightBase-Windows-Demo.zip` yerel teslim çıktılarıdır. Paket tam beş dosya içerir: üç uygulama dosyası, sentetik `dataa.xlsx` ve `BASLANGIC.md`. Üç dosyalı üretim paketi korunur. Demo çalışma kitabı `package_mail_demo.mjs` ile, `preview_demo.py` tarafından üretilen sentetik JSON üzerinden artifact-tool kullanılarak hazırlanır. Önce `package_three_files.py`, sonra `preview_demo.py` çalıştırılır; builder bundled Node/artifact-tool ortamında çalıştırılır. Rehber kaynağı `finora-lens/WINDOWS_DEMO_README.md` dosyasıdır. Demo Excel’deki `INSIGHTBASE_DEMO` sheet adı uygulamada ve sunumlarda DEMO işaretini etkinleştirir. XLSX okuyucu shared/inline string yanında `t=str` metin hücrelerini de destekler. Gerçek veriler ve yerel demo teslim çıktıları GitHub’a eklenmez. Yeni yapısal değişikliklerde ilgili Markdown belgeleri aynı değişiklik kapsamında güncellenmelidir.


### CMD teslim güncellemesi

Kullanıcının Windows bilgisayarında PowerShell bulunmadığından e-posta paketi altı dosyadır: HTML, CSS, JS, sentetik Excel, `Baslat.cmd` ve rehber. CMD dosyası Edge’i ayrı `%TEMP%\InsightBase-Local` profili ve `--allow-file-access-from-files` ile açar. Sunucu gerekmez. Yerel dosya erişimi paketlenmiş uygulamada desteklenir; normal tarayıcı profili değiştirilmez. Kurum politikaları geçerlidir. Gerçek XLSX okuyucu altı sheet’i uyarısız okudu; yerel file:// akışı Chrome’da aynı bayrakla doğrulandı. Fiziksel Windows doğrulaması yapılmadı. Önceki PowerShell / beş dosya açıklamaları bu teslim için geçersizdir.


## Current schema update — 2026-10-11

The user supplied a new six-sheet reference `şablon (1).xlsx`. DATA_CONTRACT.md is the authoritative current catalog; earlier physical row numbers in this document are superseded. Stable internal metric IDs remain, with explicit `sourceRow`, `format` and `ratio` metadata. BS has 46 supported metrics; P&L 66. Date headers start in C, with B reserved for Format. `extract_structure.py <reference.xlsx>` extracts metadata only and writes both structure.json and structure.js. No financial values are committed.

TL means million TL, USD million USD, % ratio, explicitly confirmed by the user. NPL rows flagged % now use percentage-point changes. Dashboard cards, detail tables, pies and slide outputs preserve each currency. No FX conversion or TL+USD addition occurs. Nominal/pie charts mixing currencies are rejected; growth charts may compare percentage changes and table rows show their own currencies. Monthly P&L-to-cumulative ID offset remains 38 (physical source offset also 38). Removed TL/YP NPL volume rows, branch/headcount and aggregate term/demand source rows are excluded. LDR fallback uses total loans and total deposits, both TL aggregates.

The local 8768 preview keeps synthetic JSON and shows DEMO. The new Windows live delivery excludes Excel; the user provides adjacent dataa.xlsx. Canonical three-file build stays unchanged in count. Additional CMD launcher and guide are operational helpers. Source Excel passed the browser reader with six sheets and zero warnings; 18 engine/presentation tests passed, including ratio deltas and mixed-currency rejection. Local browser preview verified TL/USD labels and USD detail with no page errors. Windows itself remains unverified. This change is not automatically published to GitHub.

New structural changes must update these Markdown files in the same task.
