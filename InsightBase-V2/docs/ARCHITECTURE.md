# Architecture and source inventory

> **Mandatory documentation maintenance:** Every development must review and update the affected Markdown documents in the same task, including fixes, features, calculations, UI, data mapping, packaging and operational rules. Record the change and actual verification in CHANGELOG.md. If no contract changes, record that conclusion and verification in the change log. A task is incomplete with stale documentation. Never include private financial values in documentation.

## Maintained directory structure

```text
AGENTS.md / README.md                 repository entry points
InsightBase-V2/
  AGENTS.md                          current operational instructions
  docs/                              requirements and handoff guides
  local-data/dataa.xlsx               PRIVATE, ignored; never distribute
  finora-lens/
    dist/                            canonical editable browser source
      index.html                     shell, navigation, dialogs
      styles.css                     app and presentation styling
      app.js                         state, loading, views, UI events
      engine.js                      pure date/financial/composition functions
      xlsx.js                        browser ZIP/XML Excel reader
      structure.json / structure.js  label/format/style/row metadata only
      highlights.js                  deterministic BS insights
      presentation.js                editor, SVG, PPTX/PDF, portable versions
    vendor/                          offline PPTX/jsPDF bundles + licenses
    tests/                           engine, highlights, presentation tests
    extract_structure.py             schema extraction, never numeric observations
    preview_demo.py                  source preview; real Excel by default if present
    package_three_files.py           canonical three-file production builder
    package_windows_live.py          Live wrapper; TXT opt-in legacy only
    windows_start.cmd                current CMD/Edge launcher source
    WINDOWS_LIVE_README.md           source for generated BASLANGIC.md
    package_local.py / local_server.py / update_local.py
                                     legacy helpers, not current launch workflow
  InsightBase-Windows/                generated HTML/CSS/JS, exactly 3 files
  InsightBase-Windows-Live/           generated five Raw-copyable files
```

Top-level legacy project copies and deleted V1 are not maintained. ZIPs, synthetic/transfer assets and private review outputs are not canonical. Do not put documentation in the three-file output; the Live guide is the intentional five-file wrapper exception.

## Runtime

HTML → TEMPLATE → FinoraEngine → LocalXLSX → highlights → offline PptxGenJS/jsPDF → InsightDeck → startup helper → app loadWorkbook → local dataa.xlsx → in-memory dataset → view rendering.

No framework or npm build step. SVG renders browser charts; native editable PPTX charts include their embedded data; PDF uses canvas pages. Native browser APIs include DOMParser, DecompressionStream, Blob, URL, fetch, dialog and File.text. Real Excel is not serialized into application files.

## State ownership

- app.js: navigation, group, display unit, horizon, PL basis, load state and current dataset.
- engine.js: pure calculations; no UI/network persistence.
- xlsx.js: template-validated extraction and warnings.
- highlights.js: BS-only deterministic selection.
- presentation.js: slides/defaults/widget selection, per-widget/table settings, SVG and exports. JSON versions whitelist definitions, regenerate runtime IDs on restore, check metric identity and stage imports before apply. No localStorage/server persistence.
- structure metadata: stable IDs, sourceRow, label/aliases, format, ratio, titleStyle, PL basis/cumulativeRow. Never equate internal ID with physical worksheet row.

## Delivery vs preview

Canonical builders inline source/vendor code into one JS and reference one CSS. Windows-Live uses the CMD/Edge file-access path; development preview uses loopback HTTP port8768. package_local.py contributes a historical literal via AST extraction only; do not infer PowerShell is required by the current launcher. The application has no runtime GitHub dependency.
