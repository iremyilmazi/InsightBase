# Excel data contract — current schema (2026-10-13)

> **Maintenance:** Every development must review and update affected Markdown documents in the same task; record changes, checks and any no-contract-change conclusion in CHANGELOG.md. See [HANDOFF.md](HANDOFF.md).

> Current implementation and publication status: [CURRENT_STATE.md](CURRENT_STATE.md), verified 2026-10-21. Older dated addenda are historical; current decisions supersede conflicting past statements.

Every structural change must update the relevant Markdown documents in the same task.

Reference: user-provided `şablon (3).xlsx`. The reference is read-only; financial values are never embedded in source, docs or deliverables.

## Input layout

Adjacent file: `dataa.xlsx`. Six worksheets: BS_Sektör, BS_Ozel, BS_Kamu, P&L_Sektör, P&L_Ozel, P&L_Kamu. BS dates are Excel 1900 serials in row 1; P&L dates in row 2. Data starts at column C. Column A contains labels, B contains Format. New date columns are read automatically and sorted; duplicates are rejected. Empty future values do not select a latest period.

## Units and validation

The user confirmed TL = million TL, USD = million USD, % = ratio. Blank Format on aggregate volume rows defaults to TL, as in the reference. Ratios formatted as Excel percent are scaled by 100; otherwise stored values are percentage points. Source Format, if supplied, must match schema metadata. Labels are validated at sourceRow; unmatched rows produce warnings and are skipped. Duplicate P&L labels are resolved by physical row, never first-label matching.

Internal `row` is a stable metric identifier, not the Excel row. `sourceRow` is the physical Excel row. Existing IDs preserve dashboard and monthly-to-cumulative pairing. New BS IDs: 104 total NPL, 114 vehicle NPL, 116 GPL+KMH NPL, 153 TL LDR, 154 FX LDR, 155 business NPL, 156 retail NPL. Removed source metrics are removed from selectable catalogs, not redirected to unrelated rows. No aggregate term/demand TL+USD sums are manufactured.

## Complete catalog

### BS

| Metric ID | Excel row | Source label | Format |
|---:|---:|---|---|
| 3 | 3 | Total Loans | TL |
| 104 | 4 | Total Loans NPL | % |
| 4 | 5 | TL Krediler | TL |
| 6 | 6 | YP Krediler | USD |
| 12 | 8 | Bireysel Krediler | TL |
| 112 | 9 | Bireysel Krediler NPL | % |
| 15 | 10 | GPL | TL |
| 17 | 11 | Konut | TL |
| 18 | 12 | Taşıt | TL |
| 114 | 13 | Taşıt NPL | % |
| 19 | 14 | KMH | TL |
| 116 | 15 | GLP+KMH NPL | % |
| 21 | 17 | Ticari Krediler | TL |
| 23 | 18 | TL Ticari Krediler | TL |
| 25 | 19 | FX Ticari Krediler | USD |
| 28 | 20 | KOBİ Krediler | TL |
| 29 | 21 | KOBİ Krediler NPL | % |
| 8 | 23 | Non Cash Loans | TL |
| 9 | 24 | TL Non Cash Loans | TL |
| 10 | 25 | FX Non Cash Loans | USD |
| 31 | 27 | Kredi Kartları | TL |
| 32 | 28 | Bireysel kk | TL |
| 33 | 29 | Bireysel kk NPL | % |
| 34 | 30 | Ticari kk | TL |
| 35 | 31 | Ticari kk NPL | % |
| 37 | 33 | Mevduatlar | TL |
| 38 | 34 | TL Mevduat | TL |
| 50 | 35 | Vadesiz TL | TL |
| 52 | 36 | Tasarruf Vadesiz TL | TL |
| 53 | 37 | Ticari Vadesiz TL | TL |
| 42 | 38 | Vadeli TL | TL |
| 44 | 39 | Tasarruf Vadeli TL | TL |
| 45 | 40 | Ticari Vadeli TL | TL |
| 39 | 42 | YP Mevduat | USD |
| 51 | 43 | Vadesiz FX | USD |
| 54 | 44 | Tasarruf Vadesiz FX | USD |
| 55 | 45 | Ticari Vadesiz FX | USD |
| 43 | 46 | Vadeli FX | USD |
| 46 | 47 | Tasarruf Vadeli FX | USD |
| 47 | 48 | Ticari Vadeli FX | USD |
| 57 | 51 | LDR | % |
| 153 | 52 | TL LDR | % |
| 154 | 53 | FX LDR | % |
| 155 | 54 | Business NPL | % |
| 156 | 55 | Retail NPL | % |
### PL

| Metric ID | Excel row | Source label | Format |
|---:|---:|---|---|
| 6 | 3 | FX Deposit | TL |
| 7 | 4 | Precious Metal Deposits | TL |
| 11 | 8 | Cumulative Net Interest Income | TL |
| 12 | 9 | Cumulative Interest Income | TL |
| 13 | 10 | Cumulative Interest Expense | TL |
| 14 | 11 | Cumulative Non-Funded Income | TL |
| 15 | 12 | Cumulative Net Fees&Commision | TL |
| 16 | 13 | Cumulative Trading & FX Gain Losses | TL |
| 17 | 14 | Cumulative Other Income | TL |
| 18 | 15 | Cumulative Total Income | TL |
| 19 | 16 | Cumulative Operating Expenses | TL |
| 20 | 17 | Cumulative HR | TL |
| 21 | 18 | Cumulative Non-HR | TL |
| 22 | 19 | Cumulative Pre Provision Profit | TL |
| 23 | 20 | Cumulative Expected Credit Loss | TL |
| 24 | 21 | Cumulative Other Provisions | TL |
| 25 | 22 | Cumulative Profit Before Tax | TL |
| 26 | 23 | Cumulative Tax | TL |
| 27 | 24 | Cumulative Net Profit | TL |
| 29 | 26 | Cumulative ROAA | % |
| 30 | 27 | Cumulative ROAE | % |
| 31 | 28 | Cumulative Cost/Income | % |
| 32 | 29 | Cumulative Net Interest Margin | % |
| 45 | 31 | Cumulative Fee / OPEX | % |
| 49 | 35 | Monthly Net Interest Income | TL |
| 50 | 36 | Monthly Interest Income | TL |
| 51 | 37 | Monthly Interest Expense | TL |
| 52 | 38 | Monthly Non-Funded Income | TL |
| 53 | 39 | Monthly Net Fees&Commision | TL |
| 54 | 40 | Monthly Trading & FX Gain Losses | TL |
| 55 | 41 | Monthly Other Income | TL |
| 56 | 42 | Monthly Total Income | TL |
| 57 | 43 | Monthly Operating Expenses | TL |
| 58 | 44 | Monthly HR | TL |
| 59 | 45 | Monthly Non-HR | TL |
| 60 | 46 | Monthly Pre Provision Profit | TL |
| 61 | 47 | Monthly Expected Credit Loss | TL |
| 62 | 48 | Monthly Other Provisions | TL |
| 63 | 49 | Monthly Profit Before Tax | TL |
| 64 | 50 | Monthly Tax | TL |
| 65 | 51 | Monthly Net Profit | TL |
| 67 | 53 | Monthly ROAA | % |
| 68 | 54 | Monthly ROAE | % |
| 69 | 55 | Monthly Cost/Income | % |
| 70 | 56 | Monthly Net Interest Margin | % |
| 83 | 58 | Monthly Fee / OPEX | % |

Reference3: BS45 unchanged metrics, PL46 (22 cumulative +22 monthly +2 auxiliary). Cumulative source rows8–29 and31, monthly35–56 and58. Blank rows and section headings are excluded. Removed secondary operating-revenue/provision/expense/tax/profit blocks are not selectable. Stable internal IDs are preserved, with basis and cumulativeRow metadata; monthly ID65 means net profit from source51, paired to cumulative ID27 source24. Fee/OPEX IDs83/45 use source58/31. Internal offset38 remains for compatibility; physical source offset is now27.


## Real local workbook — 2026-10-13

User supplied populated şablon (4).xlsx and requested replacing synthetic preview. Private working copy is InsightBase-V2/local-data/dataa.xlsx (directory ignored by Git). preview_demo.py now defaults to real-workbook mode whenever this file exists, directly building source app, copying adjacent workbook to temporary8768 preview and removing demo-data.json. No JSON fetch patch or DEMO flag is used. --demo is an explicit synthetic-only override; routine --source refresh keeps real data. Source reference4 read with6sheets and zero warnings, same BS45/PL46 schema. Values are never embedded in code/docs or Windows/GitHub deliverables. User original workbook unchanged. Later workbook updates should replace private dataa.xlsx and rerun source preview. This supersedes all prior instructions to keep local preview synthetic.


## Overview deposit cards — 2026-10-21

Dashboard deposit cards now show [37,38,39,42,50]: total deposits, TL deposits, FX deposits, TL time deposits and TL demand deposits. Replace unsupported aggregate time/demand rows 41/49 with existing TL source metrics 42/50; pie compositions and full balance sheet catalog unchanged. Published Windows-Live JS line 167 belongs to bundled PptxGenJS/JSZip vendor code; Node syntax check passes. Exact external diagnostic still required before modifying third-party code. This follow-up remains local pending publication request; version-save feature remains unpublished.


## Private workbook refresh — 2026-10-21

User-supplied populated şablon (5).xlsx replaces local-data/dataa.xlsx byte-for-byte. Six sheet names and all metric labels/units remain compatible; differences in empty P&L B cells are blank-cell serialization only. BS has 94 date columns and latest populated date 2026-10-16 for all groups; P&L has 21 date columns and latest populated date 2026-08-31. Native app reader loads BS45/PL46 metrics per sheet with zero warnings, no Excel error cells found, and overview TL time/demand cards populate. Source preview refreshed from private workbook; no schema remap, package rebuild or GitHub upload. Real values remain ignored and unembedded.
