# Development, delivery and validation

> Maintenance rule: every new structural change must update the affected Markdown documents in this documentation set in the same task. Changes to architecture, files, data contracts, row mappings, formulas, UI structure, packaging, scope or operational rules are incomplete until the matching documentation is updated. Update the index/status date and change log as appropriate. V1 was deleted with user authorization on 2026-10-09; V2 is the only maintained version.

## Start here

Read workspace/V2 AGENTS.md and docs/README.md. Only edit V2. User requests override local recommendations. V1 was explicitly released and deleted on 2026-10-09. For structural changes update affected Markdown files in the same task. Do not stop at updating generated assets: canonical code lives in `finora-lens/dist`.

## Production build

From `InsightBase-V2`:

```sh
python3 finora-lens/package_three_files.py
node --check InsightBase-Windows/InsightBase.js
```

Builder bundles structure.js + engine.js + xlsx.js + setup + app.js into one JS, rewrites HTML references and external brand, adds Windows help and extra CSS, asserts exactly three output files and writes ZIP. It reads the PowerShell literal from package_local.py with `ast`, without executing that legacy builder.

Never put docs, screenshots, demo JSON or dataa.xlsx in `InsightBase-Windows/`: the builder assertion intentionally rejects extra files. Documentation belongs outside the three-file deliverable.

## Windows user operation

Put InsightBase.html/css/js and user's dataa.xlsx in one folder. A `file://` HTML cannot automatically fetch adjacent Excel due to browser restrictions. Double-click HTML exposes the embedded startup help/command. Open PowerShell in that folder, paste the command, keep its window open. It starts a loopback TCP HTTP server and opens the dashboard. No Python/internet/installer/extra launcher required. Do not misrepresent direct double-click as a fully working Excel reader.

Server binds Loopback port 8765, falls back to an OS-selected port if occupied. Whitelist only three application files plus dataa.xlsx; GET/HEAD only, no-store, nosniff, same-origin resource policy, connection close. Windows corporate PowerShell restrictions still apply; never bypass them. Windows launch command has not been verified on a Windows machine in this session.

After workbook refresh/recalculation, save it and click Veriyi yenile. The dashboard reads again; no automatic watcher/polling. Historical columns must remain for comparisons.

## Synthetic preview on development host

```sh
python3 finora-lens/preview_demo.py
python3 -m http.server 8768 --bind 127.0.0.1 --directory /private/tmp/insightbase-v2-preview
```

Open `http://127.0.0.1:8768/InsightBase.html`. This URL is a development convention, not a Windows production URL. Check whether the server/tab still exists instead of assuming persisted process IDs. Tool/sandbox approvals may be required for binding localhost.

preview_demo.py copies generated three files to `/private/tmp/insightbase-v2-preview`, creates synthetic JSON, and modifies only the staged JS to load JSON and show DEMO mode. Never copy staged demo JS back into delivery. It creates six sheets, 93 weekly periods (2024-12-27..2026-10-02), 22 monthly periods (2024-12..2026-09), sector sums and coherent cumulative flows. These dates/values are synthetic scenarios, not public-sector facts or a promise of latest real data.

## Checks appropriate to changes

```sh
node --test finora-lens/tests/engine.test.cjs
node --check finora-lens/dist/app.js
node --check InsightBase-Windows/InsightBase.js
```

Current engine suite has 14 tests covering null/nonpositive bases, monthly BS target, leap/month-end clamp, no later observation, seven-day tolerance, YoY/YTD, PL exact month comparisons, stale rows, ratios, cumulative January, 12-slot chart and PL cumulative chart. UI changes require browser checks: expected labels/order, card detail opens, one line, 12 slots, missing values, unit switches and responsive sizing. Inspect the relevant screenshot. Do not add implementation-mirroring tests for minor reversible styling.

Legacy `tests/local_server_test.py` tests local_server.py, not the embedded Windows server. Do not claim it validates Windows.

## Historical V1 snapshot (removed)

The user authorized deleting V1 directory and ZIP on 2026-10-09. There is no V1 manifest to verify. Do not run obsolete snapshot checks or recreate this version.

## Documentation completion gate

Before closing a structural task:

1. Update relevant product/architecture/data/calculation/UI/development docs.
2. Record accepted behavioral changes and verification/limitations in CHANGELOG.
3. Update index verification date only for source actually reviewed.
4. Check relative Markdown links and row catalogs if schema changed.
5. Build only if runtime/source changed; documentation-only tasks do not require regeneration.
6. Confirm exactly three delivery files and do not recreate removed V1.

## Known implementation limits

- Parser does not calculate Excel formulas; uses cached values, with null when absent. User must calculate/save Excel.
- Basic ZIP size defenses are implemented, not a general-purpose hardened XLSX engine.
- Latest date means last finite source period, not freshness compared with today's publication schedule; no freshness alarm.
- Highlight scoring limitations are intentional current state, not financial significance analysis.
- Source row labels/positions must match; unsupported restructured workbooks need an explicit schema update.
- Source includes legacy branding/instructions that builder rewrites. Do not run old migration/build scripts as the active pipeline.

## GitHub transfer preparation — 2026-10-09

Workspace root is the Git repository; only InsightBase-V2 and root AGENTS/README/.gitignore are eligible for tracking. Workbook files, demo JSON, environment files, old top-level copies, preview screenshots and obsolete .openai hosting metadata are excluded. Intended destination: iremyilmazi/InsightBase, private. The private repository iremyilmazi/InsightBase was confirmed through the connected GitHub plugin on 2026-10-09. Transfer uses GitHub connector contents/Git-object APIs because GitHub Desktop control and local CLI authentication were unavailable. Remote and local initial commit IDs can differ; fetch/synchronize before later Git pushes.

An empty legacy nested finora-lens/.git directory inherited during V2 copying was moved to /private/tmp/insightbase-v2-legacy-git-metadata to allow normal root repository tracking. Runtime/source contents were unchanged.

## PowerPoint phase verification and publication

Run `node --test finora-lens/tests/engine.test.cjs finora-lens/tests/presentation.test.cjs` from V2. The vendored browser generator is bundled into InsightBase.js; no runtime npm dependencies or CDN. Verify graph-specific date/group/table selections, all four chart kinds, gaps and native PPTX structures. See PPTX_EXPORT.md. Do not push/upload this phase to GitHub until user instruction.

PDF export is generated locally with vendored jsPDF 3.0.3 and 1920×1080 canvas pages. Check multiple pages, Turkish glyphs, tables, circular pies and independent ranges with synthetic data. Render PDF with Poppler before claiming layout validation. Three-file assertion remains mandatory.

Publication update (2026-10-11): the user explicitly authorized uploading this complete current version to iremyilmazi/InsightBase; earlier publication-hold statements are historical and superseded for this release. Private workbook and preview exclusions remain.


## Windows e-posta demo paketi — 2026-10-11

`InsightBase-Mail-Windows` ve `InsightBase-Windows-Demo.zip` yerel teslim çıktılarıdır. Paket tam beş dosya içerir: üç uygulama dosyası, sentetik `dataa.xlsx` ve `BASLANGIC.md`. Üç dosyalı üretim paketi korunur. Demo çalışma kitabı `package_mail_demo.mjs` ile, `preview_demo.py` tarafından üretilen sentetik JSON üzerinden artifact-tool kullanılarak hazırlanır. Önce `package_three_files.py`, sonra `preview_demo.py` çalıştırılır; builder bundled Node/artifact-tool ortamında çalıştırılır. Rehber kaynağı `finora-lens/WINDOWS_DEMO_README.md` dosyasıdır. Demo Excel’deki `INSIGHTBASE_DEMO` sheet adı uygulamada ve sunumlarda DEMO işaretini etkinleştirir. XLSX okuyucu shared/inline string yanında `t=str` metin hücrelerini de destekler. Gerçek veriler ve yerel demo teslim çıktıları GitHub’a eklenmez. Yeni yapısal değişikliklerde ilgili Markdown belgeleri aynı değişiklik kapsamında güncellenmelidir.


### CMD teslim güncellemesi

Kullanıcının Windows bilgisayarında PowerShell bulunmadığından e-posta paketi altı dosyadır: HTML, CSS, JS, sentetik Excel, `Baslat.cmd` ve rehber. CMD dosyası Edge’i ayrı `%TEMP%\InsightBase-Local` profili ve `--allow-file-access-from-files` ile açar. Sunucu gerekmez. Yerel dosya erişimi paketlenmiş uygulamada desteklenir; normal tarayıcı profili değiştirilmez. Kurum politikaları geçerlidir. Gerçek XLSX okuyucu altı sheet’i uyarısız okudu; yerel file:// akışı Chrome’da aynı bayrakla doğrulandı. Fiziksel Windows doğrulaması yapılmadı. Önceki PowerShell / beş dosya açıklamaları bu teslim için geçersizdir.


## Current schema update — 2026-10-11

The user supplied a new six-sheet reference `şablon (1).xlsx`. DATA_CONTRACT.md is the authoritative current catalog; earlier physical row numbers in this document are superseded. Stable internal metric IDs remain, with explicit `sourceRow`, `format` and `ratio` metadata. BS has 46 supported metrics; P&L 66. Date headers start in C, with B reserved for Format. `extract_structure.py <reference.xlsx>` extracts metadata only and writes both structure.json and structure.js. No financial values are committed.

TL means million TL, USD million USD, % ratio, explicitly confirmed by the user. NPL rows flagged % now use percentage-point changes. Dashboard cards, detail tables, pies and slide outputs preserve each currency. No FX conversion or TL+USD addition occurs. Nominal/pie charts mixing currencies are rejected; growth charts may compare percentage changes and table rows show their own currencies. Monthly P&L-to-cumulative ID offset remains 38 (physical source offset also 38). Removed TL/YP NPL volume rows, branch/headcount and aggregate term/demand source rows are excluded. LDR fallback uses total loans and total deposits, both TL aggregates.

The local 8768 preview keeps synthetic JSON and shows DEMO. The new Windows live delivery excludes Excel; the user provides adjacent dataa.xlsx. Canonical three-file build stays unchanged in count. Additional CMD launcher and guide are operational helpers. Source Excel passed the browser reader with six sheets and zero warnings; 18 engine/presentation tests passed, including ratio deltas and mixed-currency rejection. Local browser preview verified TL/USD labels and USD detail with no page errors. Windows itself remains unverified. This change is not automatically published to GitHub.

New structural changes must update these Markdown files in the same task.

Live build: run `python3 finora-lens/package_three_files.py`, then `python3 finora-lens/package_windows_live.py`. Both live archives have exactly five files, with no Excel. The TXT variant changes only JS/CMD names; original extensions must be restored before launch. `windows_start.cmd` and `WINDOWS_LIVE_README.md` are maintained helper sources. Refresh the local preview with `python3 finora-lens/preview_demo.py`; it keeps synthetic data.


## Excel title hierarchy — 2026-10-11

Column A formatting is extracted as `titleStyle` (indent, gray, bold) from Excel cellXfs/fonts/alignment. Tables apply it only to the metric title, with 18px per Excel indent level and gray #808080 for the reference gray font. Numeric cells and source captions retain their existing styles. Main and detail BS/P&L metric tables share this rendering. `preview_demo.py --source` builds only temporary preview assets directly from canonical sources; it does not regenerate Windows deliveries. Per user instruction, Windows packages remain frozen until explicitly requested.


## Release authorization — 2026-10-12

User authorized publishing the current source to GitHub and rebuilding Windows deliverables. The temporary Windows build hold is lifted for this release. Canonical Windows output has exactly HTML/CSS/JS, with no workbook. Live operational ZIP adds CMD launcher and guide, with no demo or real Excel. Latest schema, TL/USD units, Excel ordering, title hierarchy, subtitle alignment and InsightBase branding are included. Local preview remains synthetic. Workbook and local transfer/demo variants remain excluded from GitHub.


## Reference update — 2026-10-13

Current schema is `şablon (2).xlsx`. BS consumer-loan volume and consumer NPL entries are removed (IDs 13/14); retail loans NPL added as distinct ratio ID112 at source row9. Retail total ID12 remains at source row8. Subsequent BS sources shift up one; stable IDs preserve existing pie/card calculations. BS catalog now has45 metrics; PL retains66 and its source positions. Retail detail uses new ratio plus remaining product breakdowns. Excel source order, title indent/gray/bold and TL/USD/% metadata are regenerated. Local preview retains synthetic data and includes retail NPL. Six source sheets read with zero warnings; existing calculation/export tests passed. Windows packages and GitHub are not rebuilt/published for this task. The current release artifacts therefore remain the preceding release until requested. All structural changes require corresponding MD updates.


## Current release — 2026-10-13

User authorized GitHub publication and Windows rebuild for şablon (2).xlsx support. Previous deferred-build statement is superseded for this release. Windows app output contains exactly three application files; live operational packages add launcher and guide without any Excel. Synthetic local preview remains separate.


## Delivery cleanup — 2026-10-13

User authorized removal of obsolete transfer/delivery artifacts. Removed demo/mail/TXT demo directories and archives, plus duplicate Live-TXT folders numbered2/3/4. Retained current Live and Live-TXT directories/ZIPs and the mandated canonical three-file Windows output/ZIP. Source, local synthetic browser preview and build scripts are preserved. Do not recreate historical demo transfer artifacts during routine production builds.


## Expanded BS highlights — 2026-10-13

Implemented in pure dist/highlights.js (InsightHighlights.analyze), bundled by preview and Windows builders without changing the three-file contract. It reads BS only and emits up to one growth, funding and NPL/risk card; insufficient data may yield fewer cards. Candidate rules: volume MoM, product-vs-total growth, TL/USD growth difference, TL/FX demand-deposit share changes, loan/deposit growth difference, LDR and NPL point changes, completed-month credit acceleration, sector-view private/public growth differences. Composition and contribution are excluded pending scope confirmation. Shared monthlyCompare supplies MoM bases. Derived metrics require identical current/base dates. Demand shares additionally require nonnegative same-currency components and 0.5% total reconciliation at both dates.

No financial significance cutoff or anomaly label is invented. For completed periods with12 prior valid completed observations (searching36months), selection ranks empirical absolute deviation from each candidate's own median; MAD is also recorded. Tied scores use stable IDs. Provisional periods cannot use this history ranking. Without comparable history, explicit fallback kind priority is share, fundingGap, currency, product, ratio, growth, groups, acceleration; within a kind, absolute change ranks candidates. This is a deterministic editorial selection, not a financial importance score. Historical values and scoring details are available in analyze return metadata; card method disclosure explains history/fallback choice. Empty, invalid or unchanged candidates are skipped; missing values are never zero-filled. No inferred funding cost or NPL cause is asserted. P&L basis cannot affect cards. Local preview updated; no GitHub publication or Windows rebuilding requested for this change.


## P&L reference3 — 2026-10-13

User supplied şablon (3).xlsx. Secondary cumulative/monthly reporting blocks removed; current source catalog is DATA_CONTRACT.md. PL has46 metrics:22 cumulative,22 monthly,2 auxiliary stocks. Monthly source section starts35 instead of46; cumulative Fee/OPEX is31 and monthly58. Net Profit uses monthly51/cumulative24. Stable metric IDs keep dashboard formulas and existing configured charts intact. Each monthly spec explicitly records cumulativeRow and basis; app and slides use pairing metadata. Physical source difference is27, not internal ID difference38. Removed IDs34–43 and72–81 are absent from tables/selectors. English source wording is retained, display prefixes hidden; source title formatting extracted. BS unchanged, including approved commercial label alias. Demo source remains synthetic. Six sheets read with zero warnings, pairing regression and financial/export tests pass. Windows/GitHub not rebuilt for this task; publication remains separately requested.


## Release publication — 2026-10-13

User authorized GitHub publication and Windows packages for current reference3 and expanded BS highlights. Prior deferred statements are superseded for this release. Three-file canonical build includes highlights module; live delivery adds CMD launcher/guide, no Excel. Both standard and TXT variants updated; local demo remains separate. 23 automated tests pass.


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
