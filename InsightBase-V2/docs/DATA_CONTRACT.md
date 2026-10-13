# Excel data contract — current schema (2026-10-11)

Every structural change must update the relevant Markdown documents in the same task.

Reference: user-provided `şablon (1).xlsx`. The reference is read-only; financial values are never embedded in source, docs or deliverables.

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
| 4 | 5 | TL Krediler | TL |
| 6 | 6 | YP Krediler | USD |
| 8 | 24 | Non Cash Loans | TL |
| 9 | 25 | TL Non Cash Loans | TL |
| 10 | 26 | FX Non Cash Loans | USD |
| 12 | 8 | Bireysel Krediler | TL |
| 13 | 9 | Tüketici Kredileri | TL |
| 14 | 10 | Tüketici Kredileri NPL | % |
| 15 | 11 | GPL | TL |
| 17 | 12 | Konut | TL |
| 18 | 13 | Taşıt | TL |
| 19 | 15 | KMH | TL |
| 21 | 18 | Ticari Krediler cc hariç | TL |
| 23 | 19 | TL Ticari Krediler | TL |
| 25 | 20 | FX Ticari Krediler | USD |
| 28 | 21 | KOBİ Krediler | TL |
| 29 | 22 | KOBİ Krediler NPL | % |
| 31 | 28 | Kredi Kartları | TL |
| 32 | 29 | Bireysel kk | TL |
| 33 | 30 | Bireysel kk NPL | % |
| 34 | 31 | Ticari kk | TL |
| 35 | 32 | Ticari kk NPL | % |
| 37 | 34 | Mevduatlar | TL |
| 38 | 35 | TL Mevduat | TL |
| 39 | 43 | YP Mevduat | USD |
| 42 | 39 | Vadeli TL | TL |
| 43 | 47 | Vadeli FX | USD |
| 44 | 40 | Tasarruf Vadeli TL | TL |
| 45 | 41 | Ticari Vadeli TL | TL |
| 46 | 48 | Tasarruf Vadeli FX | USD |
| 47 | 49 | Ticari Vadeli FX | USD |
| 50 | 36 | Vadesiz TL | TL |
| 51 | 44 | Vadesiz FX | USD |
| 52 | 37 | Tasarruf Vadesiz TL | TL |
| 53 | 38 | Ticari Vadesiz TL | TL |
| 54 | 45 | Tasarruf Vadesiz FX | USD |
| 55 | 46 | Ticari Vadesiz FX | USD |
| 57 | 52 | LDR | % |
| 104 | 4 | Total Loans NPL | % |
| 114 | 14 | Taşıt NPL | % |
| 116 | 16 | GLP+KMH NPL | % |
| 153 | 53 | TL LDR | % |
| 154 | 54 | FX LDR | % |
| 155 | 55 | Business NPL | % |
| 156 | 56 | Retail NPL | % |

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
| 34 | 31 | Cumulative Operating Revenue | TL |
| 35 | 32 | Cumulative Net Interest Income | TL |
| 36 | 33 | Cumulative Net Fees&Commissions Income | TL |
| 37 | 34 | Cumulative Dividend Income | TL |
| 38 | 35 | Cumulative Net Trading Income | TL |
| 39 | 36 | Cumulative Other Income | TL |
| 40 | 37 | Cumulative Provisions | TL |
| 41 | 38 | Cumulative Total Non-Interest Expenses | TL |
| 42 | 39 | Cumulative Taxation | TL |
| 43 | 40 | Cumulative Net profit | TL |
| 45 | 42 | Cumulative Fee / OPEX | % |
| 49 | 46 | Monthly Net Interest Income | TL |
| 50 | 47 | Monthly Interest Income | TL |
| 51 | 48 | Monthly Interest Expense | TL |
| 52 | 49 | Monthly Non-Funded Income | TL |
| 53 | 50 | Monthly Net Fees&Commision | TL |
| 54 | 51 | Monthly Trading & FX Gain Losses | TL |
| 55 | 52 | Monthly Other Income | TL |
| 56 | 53 | Monthly Total Income | TL |
| 57 | 54 | Monthly Operating Expenses | TL |
| 58 | 55 | Monthly HR | TL |
| 59 | 56 | Monthly Non-HR | TL |
| 60 | 57 | Monthly Pre Provision Profit | TL |
| 61 | 58 | Monthly Expected Credit Loss | TL |
| 62 | 59 | Monthly Other Provisions | TL |
| 63 | 60 | Monthly Profit Before Tax | TL |
| 64 | 61 | Monthly Tax | TL |
| 65 | 62 | Monthly Net Profit | TL |
| 67 | 64 | Monthly ROAA | % |
| 68 | 65 | Monthly ROAE | % |
| 69 | 66 | Monthly Cost/Income | % |
| 70 | 67 | Monthly Net Interest Margin | % |
| 72 | 69 | Monthly Operating Revenue | TL |
| 73 | 70 | Monthly Net Interest Income | TL |
| 74 | 71 | Monthly Net Fees&Commissions Income | TL |
| 75 | 72 | Monthly Dividend Income | TL |
| 76 | 73 | Monthly Net Trading Income | TL |
| 77 | 74 | Monthly Other Income | TL |
| 78 | 75 | Monthly Provisions | TL |
| 79 | 76 | Monthly Total Non-Interest Expenses | TL |
| 80 | 77 | Monthly Taxation | TL |
| 81 | 78 | Monthly Net profit | TL |
| 83 | 80 | Monthly Fee / OPEX | % |


## Balance-sheet ordering — 2026-10-11

BS catalog and displayed BS tables follow ascending physical Excel sourceRow, not stable internal metric ID. This also applies to detail subitem tables and presentation metric selection. The extractor preserves this order on schema regeneration. Summary cards in the BS tab follow their relative Excel order. Internal IDs and calculations remain unchanged.


## Excel title hierarchy — 2026-10-11

Column A formatting is extracted as `titleStyle` (indent, gray, bold) from Excel cellXfs/fonts/alignment. Tables apply it only to the metric title, with 18px per Excel indent level and gray #808080 for the reference gray font. Numeric cells and source captions retain their existing styles. Main and detail BS/P&L metric tables share this rendering. `preview_demo.py --source` builds only temporary preview assets directly from canonical sources; it does not regenerate Windows deliveries. Per user instruction, Windows packages remain frozen until explicitly requested.
