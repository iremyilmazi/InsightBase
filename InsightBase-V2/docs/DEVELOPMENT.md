# Development, testing, delivery and publication

> **Mandatory documentation maintenance:** Every development must review and update the affected Markdown documents in the same task, including fixes, features, calculations, UI, data mapping, packaging and operational rules. Record the change and actual verification in CHANGELOG.md. If no contract changes, record that conclusion and verification in the change log. A task is incomplete with stale documentation. Never include private financial values in documentation.

## Canonical workflow

Work in `InsightBase-V2/finora-lens/dist`. Read CURRENT_STATE and HANDOFF first. Do not implement in generated Windows files or legacy top-level copies. Existing local Git history can lag connector-published remote history; inspect before committing/pushing, never reset or force-push to make it look synchronized.

## Run a local source preview

From repository root:

```sh
python3 InsightBase-V2/finora-lens/preview_demo.py --source
python3 -m http.server 8768 --bind 127.0.0.1 --directory /private/tmp/insightbase-v2-preview
```

Open `http://127.0.0.1:8768/InsightBase.html`. Reuse an existing server on that directory rather than repeatedly starting a conflicting process. `--source` uses private local-data/dataa.xlsx when present; `--demo` explicitly requests synthetic data. Updating a workbook means replace the private copy, refresh staged preview, then reload browser. Original user attachments are not edited.

## Checks

```sh
node --test InsightBase-V2/finora-lens/tests/*.test.cjs
node --check InsightBase-V2/finora-lens/dist/presentation.js
```

Current local baseline: 50 passing Node tests (release baseline: 50). Legacy Python server tests do not establish Windows launcher compatibility. Browser tests should check actual Excel reading, scope of filters, chart/table geometry, no console errors and successful downloads as relevant. Presentation-version E2E covers save, refresh, staged restore/cancel, exact choices, malformed/future files and exports. Private test outputs must remain outside Git. Actual Windows execution is still a separate verification step; do not claim it was performed from macOS checks.

## Build deliverables when authorized

```sh
python3 InsightBase-V2/finora-lens/package_three_files.py
python3 InsightBase-V2/finora-lens/package_windows_live.py
node --check InsightBase-V2/InsightBase-Windows-Live/InsightBase.js
```

The first builder creates exactly three app files and its ZIP. The second wraps them with Baslat.cmd and BASLANGIC.md (exactly five files). It does not build canonical code itself: run the first builder first. TXT is legacy `--txt` opt-in, not the current update mechanism. Never bundle real/demo Excel in Live. Current user workflow is GitHub Raw copy.

## Windows operation

User places five Windows-Live files and their own dataa.xlsx in one directory, then runs Baslat.cmd. It launches Microsoft Edge with `--allow-file-access-from-files` and a dedicated `%TEMP%/InsightBase-Local` profile. No PowerShell, Python, Node or admin install is required by this script. Corporate browser policy may affect launch; do not invent bypasses. The HTML startup help also contains a CMD launch command. Ordinary double-click in an arbitrary browser cannot guarantee adjacent workbook reading.

Copy complete Raw content as UTF-8, keep exact extensions and take all app files from the same release. Preserve dataa.xlsx. Close the dedicated Edge window before update, reopen and hard refresh if necessary. Recalculate/save Excel before Veriyi yenile. There is no automatic watcher.

## Publication

Repository: https://github.com/iremyilmazi/InsightBase (public). Publish only work authorized by the user, after local trial if requested. Last application release: see CURRENT_STATE.

1. Inspect remote main head and tree. Compare exact local Git blob hashes to remote; local status alone is insufficient.
2. Confirm staged changes exclude private Excel, local-data, unapproved saved presentation versions, screenshots/test exports, TXT/mail variants and accidental secrets.
3. Source, docs and five Windows-Live Raw files must describe the same release. A diagnostic-only publish must exclude unapproved feature code.
4. Use an available authenticated Git tool/connector with current remote parent, expected-head lease and no force overwrite. If GitHub CLI is unavailable, do not invent authentication or expose credentials.
5. Verify resulting main head and changed file SHAs. Do not imply a push succeeded from merely creating a commit.

No routine upload is implied by development or documentation tasks. Application runtime must not contact GitHub or upload data. User manually copies Raw files on their other PC.

## Troubleshooting

- Check file completeness/UTF-8, version consistency and launcher context first.
- A bundled vendor line can contain huge minified code; ask for exact diagnostic text and tool/browser version. A line number alone is insufficient.
- Distinguish editor lint warnings from runtime errors. Node syntax success does not prove every editor diagnostic resolved.
- Never add false zero data to hide missing workbook inputs. Verify source row/Format/date identity.
- Repair canonical code and regenerate only when release scope permits.

Hybrid P&L versions require the locally updated app (schema 2); monthly-only schema-1 files remain compatible. Quarterly checks cover missing months, year boundaries, availability caps, like-period growth, cumulative-to-monthly remapping and native exports.

The 2026-10-21 release explicitly includes only presentations/Sektor-Hikayesi.insightbase.json (v10) plus its guide. This scoped exception does not authorize other local versions or PDF/PPTX publication. Include that exact definition in the release manifest, not the ignored outputs directory.

Local 2026-10-22 table-source extension uses schema 3 for independent source/basis; published schema-2 v10 remains compatible and unchanged. Browser regression covers BS tables under quarterly/cumulative P&L charts, table-only P&L remapping and schema-3 restore/export.

2026-10-22 release: the specifically approved presentation path now contains v13 (schema 3); independent table-source/basis support is included in rebuilt production files. No other saved versions or PDF/PPTX are authorized for publication.


2026-10-22 commentary layout publication: user authorized publishing the title/comment/content order. Both Windows distributions rebuilt using the prescribed builders; package JavaScript syntax passed. Approved v13 definition and schema remain unchanged.
