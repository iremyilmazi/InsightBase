# Excel data contract — current schema (2026-10-13)

Every structural change must update the relevant Markdown documents in the same task.

Reference: user-provided `şablon (2).xlsx`. The reference is read-only; financial values are never embedded in source, docs or deliverables.

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
| 21 | 17 | Ticari Krediler cc hariç | TL |
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

Current BS reference has 45 supported metrics. Consumer loans (ID 13) and consumer NPL (ID 14) are removed. New retail loans NPL is ID 112, source A9, Format %. ID 12 remains retail loan total at A8 and feeds the credit pie. After the removed row all subsequent BS source positions shift up one. New ID 112 is a distinct ratio, not a rename of the removed volume. Source title styling remains in titleStyle.
