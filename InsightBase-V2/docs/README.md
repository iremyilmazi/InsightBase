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


Current reference is `şablon (2).xlsx` (2026-10-13); see DATA_CONTRACT.md for the new source row catalog and TL/USD/ratio semantics. Latest delivery is Windows-Live (no demo workbook), with a TXT transfer variant. Local preview remains synthetic.


## Release authorization — 2026-10-12

User authorized publishing the current source to GitHub and rebuilding Windows deliverables. The temporary Windows build hold is lifted for this release. Canonical Windows output has exactly HTML/CSS/JS, with no workbook. Live operational ZIP adds CMD launcher and guide, with no demo or real Excel. Latest schema, TL/USD units, Excel ordering, title hierarchy, subtitle alignment and InsightBase branding are included. Local preview remains synthetic. Workbook and local transfer/demo variants remain excluded from GitHub.
