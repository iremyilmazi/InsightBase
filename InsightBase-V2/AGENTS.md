# InsightBase V2 — agent instructions

## Start here

Read [docs/README.md](docs/README.md), [CURRENT_STATE.md](docs/CURRENT_STATE.md), [REQUIREMENTS.md](docs/REQUIREMENTS.md) and the relevant specialist guides. CURRENT_STATE resolves old dated decisions; user instructions take precedence. Only V2 is maintained; V1 remains deleted.

## Mandatory documentation maintenance

**For every development, update affected Markdown files in the same task.** Features, fixes, calculations, workbook mappings, UI, version files, exports, packaging and operating rules are included. Use the [documentation matrix](docs/HANDOFF.md). Always record changes and actual verification in [CHANGELOG.md](docs/CHANGELOG.md). If the contract did not change, record the reviewed no-change conclusion. Stale docs mean incomplete work. Update current-state/release facts when they change; never invent test results or publication status.

## Source and production rules

- Edit `finora-lens/dist` as the canonical source; generated Windows files are build outputs.
- Application is offline Windows software. User uses CMD and Microsoft Edge, without PowerShell or AI. Runtime reads adjacent dataa.xlsx; no workbook upload screen. Dedicated CMD/Edge launcher is current; old loopback/PowerShell instructions are historical.
- Run `python3 finora-lens/package_three_files.py` from V2 for exactly three application files under InsightBase-Windows. Run package_windows_live.py afterward for the five-file Live wrapper. Documentation stays outside the three-file directory.
- Never upload/embed real workbooks, local-data, unapproved presentation-version files, private screenshots or data-bearing test exports. No TL/USD summation or assumed FX conversion. Preserve Excel semantics and stable-ID/sourceRow distinction.
- Test financial/date changes with relevant Node tests; visually verify chart/layout changes and test exports when affected. Do not claim actual Windows testing from macOS/headless checks.
- Presentation version save/open is accepted and published. Versions contain definitions/text, never workbook observations; reopening recalculates against local Excel. Do not reinstate the old exclusion.

## Publication scope

Current release verified at `dc99aed685b0817c0e7f0a0a9e195965ae2fe7a7` on 2026-10-21: presentation formatting, unambiguous source dates, quarterly/monthly and cumulative P&L support, plus the specifically authorized v10 definition at `presentations/Sektor-Hikayesi.insightbase.json`. Release commit title: `Publish presentation refinements, quarterly P&L and approved sector deck`. Source, three-file Windows output and five-file Live wrapper are rebuilt together. Prior application release: e909418326245a36bfb851516c5acb7fe8afd6a9; prior documentation head: 739d9198fb36422694c6d0b4ac1fc8a3e0df6e8e.

Only this one presentation definition is authorized for publication; it contains definitions/editorial text and recalculates from the user's local Excel. Other saved versions, Excel, PDF/PPTX, private screenshots/test outputs remain excluded. Future publication requires user authorization for that work. Preserve current remote parent and use a non-forced expected-head update.
