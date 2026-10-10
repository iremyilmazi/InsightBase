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
