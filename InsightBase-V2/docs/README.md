# InsightBase — agent handoff index

> Maintenance rule: every new structural change must update the affected Markdown documents in this documentation set in the same task. Changes to architecture, files, data contracts, row mappings, formulas, UI structure, packaging, scope or operational rules are incomplete until the matching documentation is updated. Update the index/status date and change log as appropriate. V1 was deleted with user authorization on 2026-10-09; V2 is the only maintained version.

Verified against active V2 source on 2026-10-13. Documentation language is English for agent portability; product UI and user communication are Turkish.

Read these documents before making changes:

1. [Product scope and decisions](PRODUCT.md)
2. [Architecture and file inventory](ARCHITECTURE.md)
3. [Excel data contract and complete row catalog](DATA_CONTRACT.md)
4. [Financial calculations and chart rules](CALCULATIONS.md)
5. [UI structure and interaction contract](UI.md)
6. [Build, run, validation and maintenance workflow](DEVELOPMENT.md)
7. [Presentation editor and PowerPoint export](PPTX_EXPORT.md)
8. [Decision/change log](CHANGELOG.md)

The binding instruction entry points are the workspace `AGENTS.md` and `InsightBase-V2/AGENTS.md`. This set records current implementation, explicit user constraints and known limitations; do not assume proposed improvements are implemented.

## Version ownership

- Workspace: `/Users/ozgur/Documents/ChatGPT/aylik_dek`.
- V1 directory and ZIP were deleted with explicit user authorization on 2026-10-09; only V2 is maintained.
- Active source: `InsightBase-V2/finora-lens/`.
- Generated delivery: `InsightBase-V2/InsightBase-Windows/` and its sibling ZIP.
- Top-level `finora-lens/`, `InsightBase-Windows/` and Sektovista artifacts are legacy copies. Do not use them as V2 source.

## Current state

V2 has a card-based banking dashboard, local Excel reading, monthly changes from weekly BS data, monthly P&L, 12-month change charts, three composition pies (credit, TL deposits and FX deposits), deterministic highlights and only the latest populated periods. The dashboard has no historical date picker, source-unit selector or AI dependency. The presentation editor supports independent chart month ranges and native editable PowerPoint export and PDF download; see PPTX_EXPORT.md. The distributable has exactly three application files.


Current reference is `şablon (3).xlsx` (2026-10-13); see DATA_CONTRACT.md for the new source row catalog and TL/USD/ratio semantics. Latest delivery is Windows-Live (no demo workbook), with a TXT transfer variant. Local preview remains synthetic.


## Release authorization — 2026-10-12

User authorized publishing the current source to GitHub and rebuilding Windows deliverables. The temporary Windows build hold is lifted for this release. Canonical Windows output has exactly HTML/CSS/JS, with no workbook. Live operational ZIP adds CMD launcher and guide, with no demo or real Excel. Latest schema, TL/USD units, Excel ordering, title hierarchy, subtitle alignment and InsightBase branding are included. Local preview remains synthetic. Workbook and local transfer/demo variants remain excluded from GitHub.


## Real local workbook — 2026-10-13

User supplied populated şablon (4).xlsx and requested replacing synthetic preview. Private working copy is InsightBase-V2/local-data/dataa.xlsx (directory ignored by Git). preview_demo.py now defaults to real-workbook mode whenever this file exists, directly building source app, copying adjacent workbook to temporary8768 preview and removing demo-data.json. No JSON fetch patch or DEMO flag is used. --demo is an explicit synthetic-only override; routine --source refresh keeps real data. Source reference4 read with6sheets and zero warnings, same BS45/PL46 schema. Values are never embedded in code/docs or Windows/GitHub deliverables. User original workbook unchanged. Later workbook updates should replace private dataa.xlsx and rerun source preview. This supersedes all prior instructions to keep local preview synthetic.


## GitHub Raw Windows workflow — 2026-10-20

User now updates the other Windows PC by copying GitHub Raw content, not email. Publish exactly five files under InsightBase-V2/InsightBase-Windows-Live: BASLANGIC.md, Baslat.cmd, InsightBase.css/html/js. Sixth user-local dataa.xlsx must never be committed or overwritten by updates. Explicit gitignore whitelist publishes only the five files; live ZIP, TXT copies and all Excel stay excluded. Canonical InsightBase-Windows still contains exactly three application files. package_windows_live.py defaults to normal live output only; --txt is legacy opt-in. Guide explains authenticated Raw access, full-content copy, UTF-8, visible extensions, same-version updates, local workbook preservation, launch and hard refresh. .gitattributes requests CRLF for CMD and LF for other live files. No updater or network access added to running application. Current code includes rollback of the two trial analysis views. Publishing this five-file folder is authorized by the current request.


## Local review status — 2026-10-21

Presentation workflow trial is available locally (presets, defaults, graph duplication, dashboard import, drag sorting). Public Raw/GitHub and Windows deliveries intentionally remain the earlier approved release. No save/open draft feature. Read PPTX_EXPORT.md for accepted scope and rollback location.


## Publication approved — 2026-10-21

User approved the current presentation workflow, compact settings, independent table metrics, per-chart decimal selection and refined chart/table composition for GitHub publication. This supersedes the local-only publication hold for this release. Rebuild canonical three-file application and five Windows-Live Raw files to keep source and browser-copyable distribution consistent. Workbook, private preview and TXT transfer packages remain excluded.


## Follow-up release approved — 2026-10-21

User approved publishing stable chart-label typography, adaptive line bounds and independent table-row unit/decimal settings. All 32 automated tests pass. Canonical source and Windows-Live Raw distribution are rebuilt together; real workbook and TXT/private preview remain excluded.


## Presentation versions — local review, 2026-10-21

Presentation version save/open is now implemented locally and awaiting user review; this supersedes the previous draft-save exclusion. No GitHub/Raw/Windows delivery updates are authorized for this feature yet.


## Private workbook refresh — 2026-10-21

User-supplied populated şablon (5).xlsx replaces local-data/dataa.xlsx byte-for-byte. Six sheet names and all metric labels/units remain compatible; differences in empty P&L B cells are blank-cell serialization only. BS has 94 date columns and latest populated date 2026-10-16 for all groups; P&L has 21 date columns and latest populated date 2026-08-31. Native app reader loads BS45/PL46 metrics per sheet with zero warnings, no Excel error cells found, and overview TL time/demand cards populate. Source preview refreshed from private workbook; no schema remap, package rebuild or GitHub upload. Real values remain ignored and unembedded.


## Portable-version release authorized — 2026-10-21

User approved GitHub publication of the complete current project including portable presentation version save/open, diagnostic cleanup and overview TL time/demand deposit cards. Previous local-only holds for these features are lifted. Rebuild canonical three-file app and five Windows-Live Raw files; do not include private workbook, saved presentation version files, TXT variants or private test exports. 36 automated tests passed; rerun browser version workflow on the latest private workbook before publication.
