# Product purpose, scope and mandatory constraints

> Maintenance rule: every new structural change must update the affected Markdown documents in this documentation set in the same task. Changes to architecture, files, data contracts, row mappings, formulas, UI structure, packaging, scope or operational rules are incomplete until the matching documentation is updated. Update the index/status date and change log as appropriate. V1 was deleted with user authorization on 2026-10-09; V2 is the only maintained version.

## Purpose

InsightBase is an internal banking-sector finance and strategy analysis dashboard. It helps the user see growth, funding composition, costs and profitability, then drill from a main indicator into its source, comparisons, related subrows and history. Treat financial usability and modern visual design as first-class requirements.

## User environment and data privacy

- Production machine is Windows; development host is macOS.
- User cannot share real work data. Develop/preview with synthetic data or the blank workbook structure.
- Must operate without AI access and without an internet dependency. No AI service is needed for calculations, highlights or rendering.
- No upload/file chooser screen. Read the user's `dataa.xlsx` from the same folder as the application.
- Carry exactly HTML, CSS and JS application files. The user's Excel is a separate fourth data file, not bundled in the three-file ZIP.
- Do not add launchers, installers, libraries, JSON data files, fonts, images or extra application assets to production delivery.
- Do not publish, upload or transmit the workbook to any external service. Do not expose the server on the LAN.

## Accepted product decisions

- Brand: InsightBase. Finora/Sektovista names still appear in source internals and older files; packager converts external branding.
- Latest data is sufficient: no historical analysis date picker and no 'return to latest' button.
- BS is refreshed weekly; P&L monthly. Each type/group uses its own latest populated date. Source dates remain visible.
- All period-change displays use MoM, including weekly BS input. Keep YoY and YTD choices.
- One display-unit selector: million/billion/trillion TL. Both source types use million TL.
- Maximum two decimal digits, Turkish number formatting. Do not force trailing zeros.
- Main charts show changes, one line at a time; 12 calendar months and point labels in detail dialogs.
- Overview contains highlights first, three composition pies in two cards (credit, and a shared TL/FX deposit card) next, then balance-sheet credit/deposit card groups, then P&L cards.
- No 'Growth rhythm' overview chart, no 'Main indicators' overview table, no sidebar 'Sector research' heading or phase explanatory block.
- Credit and deposit cards have the same dimensions, padding and typography.

## In scope now

Session-only slide editor, editable PowerPoint output and fixed PDF output (see [PPTX_EXPORT.md](PPTX_EXPORT.md)), local XLSX import, sector/private/public switching, overview, BS details, P&L monthly/cumulative views, bank-group comparisons, data/method information, refresh, source warnings and synthetic development preview.

## Future phase / explicitly not implemented

Corporate PowerPoint templates will be supplied later. The initial InsightBase slide editor and export are implemented. Financial-importance scoring, causal AI comments, FX-neutral/reel growth, attribution bridges and historical anomaly scoring are not implemented. Do not describe highlights as any of these.

## Publication hold

User explicitly requested no GitHub upload/push for this new phase until they review and ask. Local development and Windows builds are authorized.

Publication update (2026-10-11): the user explicitly authorized uploading this complete current version to iremyilmazi/InsightBase; earlier publication-hold statements are historical and superseded for this release. Private workbook and preview exclusions remain.


## Global P&L basis selector — 2026-10-13

Monthly/Cumulative segmented selector now sits beside the bank-group toolbar on overview, PL and comparison views. Shared state.basis drives overview P&L cards, deterministic PL highlight candidates, group comparison metrics and PL detail/table source rows. Monthly uses Monthly source IDs, cumulative pairs via offset38; BS is unaffected. Existing PL-tab duplicate selector removed. Cumulative MoM is change in cumulative level, not monthly flow; January year reset remains unavailable. Slide editor retains independent chart settings. Temporary demo preview updated; Windows and GitHub publication deferred until requested.
