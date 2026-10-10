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
- Overview contains highlights first, two composition pies side by side next, then balance-sheet credit/deposit card groups, then P&L cards.
- No 'Growth rhythm' overview chart, no 'Main indicators' overview table, no sidebar 'Sector research' heading or phase explanatory block.
- Credit and deposit cards have the same dimensions, padding and typography.

## In scope now

Local XLSX import, sector/private/public switching, overview, BS details, P&L monthly/cumulative views, bank-group comparisons, data/method information, refresh, source warnings and synthetic development preview.

## Future phase / explicitly not implemented

PowerPoint output will be specified by the user later. Do not invent/export slides now. Financial-importance scoring, causal AI comments, FX-neutral/reel growth, attribution bridges and historical anomaly scoring are not implemented. Do not describe highlights as any of these.
