# Current state and binding decisions

> **Mandatory documentation maintenance:** Every development must review and update the affected Markdown documents in the same task, including fixes, features, calculations, UI, data mapping, packaging and operational rules. Record the change and actual verification in CHANGELOG.md. If no contract changes, record that conclusion and verification in the change log. A task is incomplete with stale documentation. Never include private financial values in documentation.

Verified: 2026-10-22. This file supersedes conflicting historical notes elsewhere. Update it whenever the current implementation, restrictions or release status changes.

## Product and environment

- Brand: **InsightBase**. Internal identifiers such as FinoraEngine are implementation details, not product renaming instructions.
- Offline banking-sector finance/strategy dashboard with editable presentation authoring. No AI connection, external API, CDN, cloud storage or network dependency at runtime.
- Production: Windows with CMD and Microsoft Edge; PowerShell is unavailable to the user. Development: macOS.
- Canonical three-file app: InsightBase.html, InsightBase.css, InsightBase.js.
- Windows-Live operational distribution: those three plus Baslat.cmd and BASLANGIC.md. User supplies a sixth file, dataa.xlsx. This is intentional and does not change the three-application-file constraint.
- Baslat.cmd starts Edge with adjacent file reading enabled in a dedicated temporary profile. No Python, Node or PowerShell required. This launch path is inspected but has not been run on a real Windows host in this environment.
- There is no Excel upload screen. The version-file chooser is for presentation definitions only.

## Data and calculations

- Local private source: `InsightBase-V2/local-data/dataa.xlsx`, currently copied from user-supplied şablon (5).xlsx. It is Git-ignored and never embedded in JS, docs, ZIPs or GitHub.
- Local preview now uses real supplied data, not demo. `preview_demo.py --source` stages it in `/private/tmp/insightbase-v2-preview`; `--demo` explicitly requests synthetic mode.
- Six sheets: BS_Sektör/Ozel/Kamu and P&L_Sektör/Ozel/Kamu. Column A labels, B Format, data C onward. BS dates row 1; PL dates row 2. BS45/PL46 mapped metrics per sheet. Stable internal IDs are not physical Excel rows.
- Current file: BS94 date columns, latest populated 2026-10-16; PL21 date columns, latest populated 2026-08-31. Future refreshes must derive dates, never hardcode these values.
- Amounts: million TL or million USD, according to Format; ratios percent. No FX conversion or TL/USD summation. Display units million/billion/trillion. Numeric locale en-US; Turkish date labels.
- Default maximum 2 decimals for dashboard. Presentation charts and table rows independently support 0–4 decimal places.
- Latest available BS and PL periods remain independent. No global historical analysis-date picker. Weekly BS inputs still produce calendar-aware MoM, not fixed four-week comparisons. See CALCULATIONS and engine code for partial/completed month distinction.

## Current UI

- Navigation: Genel bakış, Bilanço, Kârlılık, Grup karşılaştırması, Sunum oluştur, Veri & yöntem.
- Overview: BS-only deterministic highlights; credit pie and a shared card with TL/FX deposit pies; separate credit/deposit card groups and PL cards.
- Deposit cards use stable IDs [37,38,39,42,50]: total, TL, FX, TL time and TL demand deposits. Removed aggregate IDs41/49 must not be restored to these cards.
- BS table follows Excel source order and title hierarchy. PL keeps English source names, strips Monthly/Cumulative display prefixes only. Repeated per-row name/date subtitles are removed.
- P&L monthly/cumulative switch affects PL only. Presentation widgets have their own independent basis.
- Detail charts default to one change series, with MoM/YoY/YTD selection and nominal ratio option, 12 calendar-month slots and point labels.
- Pie history supports 12 monthly compositions and comparison of any selected pair. Native hover titles retained; rejected floating tooltip and verbose comparison footer remain absent.

## Presentation behavior

- Session defaults, templates, per-widget selections/dates/groups/units, duplicate widgets/slides, drag sorting and dashboard import are implemented.
- Local formatting follow-up: horizontal bars identify series directly and omit duplicate legends; short bars use adjacent full-name fallback in preview/PDF. Shared group/measurement/unit context appears below chart headings, and single-group tables include group in their shared caption. Included in this authorized release.
- Local date-label follow-up: four-digit years; single-period headings and current incomplete-month chart/table labels use actual common observation dates. Source dates are derived from points, not hardcoded or inferred from month-end. Included in this authorized release.
- Local P&L extension: optional complete-quarter plus open-quarter-month grouping for monthly or cumulative P&L amounts, shared by charts/tables/PPTX/PDF. Missing quarters stay unavailable; ratios remain monthly. Hybrid versions use schema 2; schema 1 remains supported. Included in this authorized release.
- Charts: line, column, horizontal bar, pie. Independent mini-table metrics, measurements, units and decimals. TL/USD and ratio/amount mixing guards remain enforced.
- Local formatting follow-up: percentage labels include % in charts/mini-tables; ratio changes retain puan. Negative preview/PDF bar labels sit outside the bar endpoint; PPTX uses supported dark inEnd labels. Existing saved definitions need no migration. Included in this authorized release.
- Local mini-table follow-up: common measurement/unit appears once in a caption, with metric names in the left column; mixed selections retain row-specific metadata. Preview/PPTX/PDF share the rule. Included in this authorized release.
- Line bounds fit observed values with padding; bars retain zero. Mini-table addition preserves chart label size. Mini-tables use a left label column (28%) and equal period columns (72%); chart dates remain visible on the independent chart grid.
- PPTX: native editable charts, embedded chart data, editable text/tables. PDF: static 16:9 visual pages. Download names include local date/time/seconds.
- Presentation versions are implemented and published: named `.insightbase.json` files store definitions/text, never Excel observations. Opening recalculates from current local Excel while preserving saved date ranges. Imports are validated and staged before replacing the working deck. No localStorage, autosave or cloud history.
- Rejected flexible-comparison and profit-bridge experiments are not part of the active app. Do not reintroduce them without request.

## Publication and verification

- Repository: https://github.com/iremyilmazi/InsightBase (public).
- Current release verified: `228ed174d2fd4e69f37cf141024a10c513c1b271` (2026-10-22), commit titled `Publish independent table sources and context-reviewed v13 deck`, including all current presentation formatting/date fixes, monthly/cumulative hybrid P&L and the authorized v10 definition. Prior app release: `e909418326245a36bfb851516c5acb7fe8afd6a9`; prior documentation head: `739d9198fb36422694c6d0b4ac1fc8a3e0df6e8e`. Three-file app and five-file Windows-Live Raw outputs rebuilt together.
- Current local baseline: 50 automated tests passed after the presentation-label fixes. Current release baseline is 50 (previous release: 47). Browser E2E verified five-slide/four-chart-type version save, refresh, cancel, exact restore, malformed/future-file rejection, and PPTX/PDF exports. Workbook reader: six sheets, zero warnings; TL deposit cards populated.
- Windows JS line167 is bundled third-party presentation code; Node syntax check passes. User-reported remaining diagnostic cannot be identified without its exact message. Do not claim all Windows editor diagnostics are resolved.
- The user explicitly authorized publishing this documentation refresh on 2026-10-21. This release changes Markdown only; no app/Windows rebuild or private data publication. Future publication requires user authorization for that work; prior approval is not an unlimited future instruction.

## Authorized presentation definition

On 2026-10-21 the user explicitly requested publishing the current app and v10 presentation definition, excluding PDF/PPTX. Only `presentations/Sektor-Hikayesi.insightbase.json` is included with its usage guide. This is a scoped exception to the saved-version privacy default. It contains configuration/editorial text, not workbook observation series; graphics recalculate locally. Other saved versions, workbook data and test/export artifacts remain excluded.

## Local follow-up — 2026-10-22

Independent table source (Bilanço/P&L) and table P&L basis are implemented locally with schema-3 support and legacy schema-1/2 compatibility. Chart selections remain independent, and BS tables on quarterly P&L charts show endpoint stocks. Fifty automated tests passed plus real-workbook browser source/basis, restore and export checks. Published application dc99aed685b0817c0e7f0a0a9e195965ae2fe7a7 and approved v10 definition remain unchanged; no Windows rebuild or publication for this follow-up.

## Release authorization — 2026-10-22

User explicitly authorized publishing the current application and latest working v13 presentation. The local independent-table follow-up and v11–v13 narrative/table updates are included in this release, superseding their local-only status. Source and Windows three/five-file distributions are rebuilt together. Current release is identified by commit title `Publish independent table sources and context-reviewed v13 deck`; preceding verified app/documentation commits remain recorded above. Approved presentation path stays presentations/Sektor-Hikayesi.insightbase.json, now schema 3. Fifty tests pass. PDF/PPTX, Excel and private outputs stay excluded; future versions require fresh authorization.


## Local commentary layout — 2026-10-22

Slide commentary is immediately below the main title in preview/PDF/editable PPTX. Widget content follows it and the source footer stays at the bottom. Financial formulas, saved definitions and schemas are unchanged. Fifty automated tests pass; three-slide real-workbook browser layout and PPTX/PDF checks passed. No Windows rebuild or publication for this follow-up.


## Commentary layout release — 2026-10-22

User authorized GitHub publication of the commentary layout. This supersedes the local-only status above. Release commit title: `Move slide commentary below the title`. Canonical source, three-file Windows app and five-file Live wrapper were rebuilt together. The approved v13 presentation definition is unchanged and uses the new layout when opened in the updated app. Fifty tests and source browser/PDF/PPTX checks passed; packaged JavaScript syntax checked. Private Excel and QA exports remain excluded.
