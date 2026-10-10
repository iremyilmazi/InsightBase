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
      engine.js             pure financial functions, Node-compatible tests
      xlsx.js               browser-native ZIP/XML workbook reader
      structure.json        exact template row labels and structure metadata
      structure.js          browser TEMPLATE representation
    package_three_files.py  active production builder
    package_local.py        legacy builder; supplies PowerShell string via AST to active builder
    extract_structure.py    extracts template labels/dates (not real financial data)
    preview_demo.py         synthetic preview generator; patches preview JS only
    local_server.py         legacy development helper
    update_local.py         legacy migration script; do not rerun casually
    tests/
      engine.test.cjs
      local_server_test.py  tests legacy local_server helper, not Windows PowerShell
  InsightBase-Windows/
    InsightBase.html
    InsightBase.css
    InsightBase.js
  InsightBase-Windows.zip   same three entries, root of archive
  *preview.jpg             review artifacts, not production assets
```

## Browser execution flow

HTML shell → bundled `TEMPLATE` → `FinoraEngine` → `LocalXLSX` → Windows setup helper → app entry point → `loadWorkbook()` → fetch local Excel with `cache: no-store` → parser → dataset → render current view.

No framework, npm build or remote chart/XLSX library. Charts are generated SVG. Native APIs include `DOMParser`, `TextDecoder`, `Blob`, `Response`, `DecompressionStream('deflate-raw')`, `AbortController`, and `<dialog>`.

## Global interfaces

- `TEMPLATE`: workbook row schema from structure.js.
- `FinoraEngine`: `DAY`, `iso`, `shift`, `monthEnd`, `monthAgo`, `finite`, `pct`, `at`, `compare`, `series`, `metricSeries`, `cumulativeYoY`, `monthlyChanges`.
- `LocalXLSX.read(file, template)`: Promise of sheets/warnings.
- App `state`: view, group, date (internal latest fallback, no picker), unit (1/1000/1000000), basis, horizon, legacy trend.
- `dataset`: sheets, warnings, demo, hasValues. Read state: loading/ready/error, error message, load token, lastRead.
- Optional browser WebMCP `set_insightbase_view` after packaging changes view/group only. It is optional; production does not require an agent or AI access.

## Important functions

`metric()` uses `latestDate(type,group)`; `getSeries()` preserves source-million values. `render()` produces the current screen, `overview()` produces overview sections, `loanPie(deposits)` renders either composition, `insights()` ranks six MoM candidates, `showDetail()` opens a drilldown, `chartPoints()` gets monthly changes and `chart()` renders one SVG line.

Refresh clears the current dataset while loading; errors show an error state instead of retaining old values as current. A token prevents stale concurrent responses overwriting newer loads. There is no background refresh timer or persisted data cache.
