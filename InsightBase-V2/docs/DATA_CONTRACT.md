# Excel data contract and exact template catalog

> Maintenance rule: every new structural change must update the affected Markdown documents in this documentation set in the same task. Changes to architecture, files, data contracts, row mappings, formulas, UI structure, packaging, scope or operational rules are incomplete until the matching documentation is updated. Update the index/status date and change log as appropriate. V1 was deleted with user authorization on 2026-10-09; V2 is the only maintained version.

## Workbook and sheets

Production filename `dataa.xlsx`, beside the three application files. Expected BS sheets: BS_Sektör, BS_Ozel, BS_Kamu. Expected monthly sheets: P&L_Sektör, P&L_Ozel, P&L_Kamu. Parser trims/case-normalizes Turkish strings, replaces ö with o for sheet matching. Internal groups are Sektör / Ozel / Kamu; internal types BS / PL.

BS date header is row 1; PL date header row 2. Labels are in column A; dates are numeric Excel serials (1900 date system), accepted serial range 30000..80000. Columns are discovered from numeric headers and sorted chronologically. Duplicate dates reject a sheet. Extend by adding dated columns; preserve past periods and row positions/labels.

Every template row is matched by BOTH original row index and normalized exact label. Normalization trims, lowercases Turkish and collapses whitespace; it is not fuzzy matching. Unmatched rows are skipped with warnings. Repeated PL labels in cumulative/monthly sections must stay in their original positions.

## Parsed dataset

```js
{
  sheets: [{
    type: 'BS' | 'PL', group: 'Sektör' | 'Ozel' | 'Kamu', name: 'source sheet name',
    dates: ['YYYY-MM-DD'], // sorted, unique
    rows: [{row: 3, label: 'exact template label', values: [number, null]}]
  }],
  warnings: ['sheet!cell: reason'],
  demo: false, // app adds; true only in staged synthetic preview
  hasValues: true // app derives
}
```

Values align one-to-one with sheet dates. Raw monetary units are million TL for BS and PL. Nulls must survive extraction. Shared strings, inline strings and numeric cached cells are read. Excel error cells warn; boolean/string-valued formula results are not monetary values. Percent-formatted ratio cells multiply source fraction by 100; ordinary numeric ratio cells are already percentage points.

Ratio rows: BS57; PL29,30,31,32,45,67,68,69,70,83. Monthly PL49+ maps to cumulative row `monthlyRow - 38`; keep this positional dependency aligned across parser, engine, UI and docs when changing schema.

## Unsupported / limits

20 MiB workbook max; declared uncompressed ZIP total max 120,000,000 bytes; at most 10,000 entries. Encrypted ZIP, unsupported compression, unsupported archive metadata, 1904 dates, missing/duplicate date headers or no matching sheets reject loading. Native deflate-raw decompression support required. Formula recalculation is not supported. No interpolation, no implicit currency conversion or external lookup.

## Source provenance

Original blank structure workbook was `/Users/ozgur/Downloads/şablon.xlsx`. It supplied labels/date structure, not actual user financial values. Canonical schema is `../finora-lens/dist/structure.json`; structure.js is its browser counterpart. Any template regeneration must preserve the no-real-data-sharing constraint.

## Complete row catalog

The following labels are copied from the canonical template as verified on 2026-10-09. Display aliases can differ; parser validation uses these source labels.

### BS

| Row / label cell | Exact source label |
|---|---|
| 3 / A3 | (Gross) Krediler |
| 4 / A4 | TL Krediler |
| 5 / A5 | TL Krediler NPL |
| 6 / A6 | YP Krediler |
| 7 / A7 | YP Krediler NPL |
| 8 / A8 | Non Cash Loans |
| 9 / A9 | TL Non Cash Loans |
| 10 / A10 | FX Non Cash Loans |
| 12 / A12 | Bireysel Krediler |
| 13 / A13 | Tüketici Kredileri |
| 14 / A14 | Tüketici Kredileri NPL |
| 15 / A15 | GPL |
| 16 / A16 | GPL NPL |
| 17 / A17 | Konut |
| 18 / A18 | Taşıt |
| 19 / A19 | KMH |
| 21 / A21 | Ticari Krediler |
| 22 / A22 | Ticari Krediler NPL |
| 23 / A23 | TL Ticari Krediler |
| 24 / A24 | TL Ticari Krediler NPL |
| 25 / A25 | FX Ticari Krediler |
| 26 / A26 | FX Ticari Krediler NPL |
| 27 / A27 | Gayrinakdi |
| 28 / A28 | KOBİ Krediler |
| 29 / A29 | KOBİ Krediler NPL |
| 31 / A31 | Kredi Kartları |
| 32 / A32 | Bireysel kk |
| 33 / A33 | Bireysel kk NPL |
| 34 / A34 | Ticari kk |
| 35 / A35 | Ticari kk NPL |
| 37 / A37 | Mevduatlar |
| 38 / A38 | TL Mevduat |
| 39 / A39 | YP Mevduat |
| 41 / A41 | Vadeli |
| 42 / A42 | Vadeli TL |
| 43 / A43 | Vadeli FX |
| 44 / A44 | Tasarruf Vadeli TL |
| 45 / A45 | Ticari Vadeli TL |
| 46 / A46 | Tasarruf Vadeli FX |
| 47 / A47 | Ticari Vadeli FX |
| 49 / A49 | Vadesiz |
| 50 / A50 | Vadesiz TL |
| 51 / A51 | Vadesiz FX |
| 52 / A52 | Tasarruf Vadesiz TL |
| 53 / A53 | Ticari Vadesiz TL |
| 54 / A54 | Tasarruf Vadesiz FX |
| 55 / A55 | Ticari Vadesiz FX |
| 57 / A57 | LDR |

### PL

| Row / label cell | Exact source label |
|---|---|
| 4 / A4 | Şube Sayısı |
| 5 / A5 | Çalışan Sayısı |
| 6 / A6 | FX Deposit |
| 7 / A7 | Precious Metal Deposits |
| 11 / A11 | Cumulative Net Interest Income |
| 12 / A12 | Cumulative Interest Income |
| 13 / A13 | Cumulative Interest Expense |
| 14 / A14 | Cumulative Non-Funded Income |
| 15 / A15 | Cumulative Net Fees&Commision |
| 16 / A16 | Cumulative Trading & FX Gain Losses |
| 17 / A17 | Cumulative Other Income |
| 18 / A18 | Cumulative Total Income |
| 19 / A19 | Cumulative Operating Expenses |
| 20 / A20 | Cumulative HR |
| 21 / A21 | Cumulative Non-HR |
| 22 / A22 | Cumulative Pre Provision Profit |
| 23 / A23 | Cumulative Expected Credit Loss |
| 24 / A24 | Cumulative Other Provisions |
| 25 / A25 | Cumulative Profit Before Tax |
| 26 / A26 | Cumulative Tax |
| 27 / A27 | Cumulative Net Profit |
| 29 / A29 | Cumulative ROAA |
| 30 / A30 | Cumulative ROAE |
| 31 / A31 | Cumulative Cost/Income |
| 32 / A32 | Cumulative Net Interest Margin |
| 34 / A34 | Cumulative Operating Revenue |
| 35 / A35 | Cumulative Net Interest Income |
| 36 / A36 | Cumulative Net Fees&Commissions Income |
| 37 / A37 | Cumulative Dividend Income |
| 38 / A38 | Cumulative Net Trading Income |
| 39 / A39 | Cumulative Other Income |
| 40 / A40 | Cumulative Provisions |
| 41 / A41 | Cumulative Total Non-Interest Expenses |
| 42 / A42 | Cumulative Taxation |
| 43 / A43 | Cumulative Net profit |
| 45 / A45 | Cumulative Fee / OPEX |
| 49 / A49 | Monthly Net Interest Income |
| 50 / A50 | Monthly Interest Income |
| 51 / A51 | Monthly Interest Expense |
| 52 / A52 | Monthly Non-Funded Income |
| 53 / A53 | Monthly Net Fees&Commision |
| 54 / A54 | Monthly Trading & FX Gain Losses |
| 55 / A55 | Monthly Other Income |
| 56 / A56 | Monthly Total Income |
| 57 / A57 | Monthly Operating Expenses |
| 58 / A58 | Monthly HR |
| 59 / A59 | Monthly Non-HR |
| 60 / A60 | Monthly Pre Provision Profit |
| 61 / A61 | Monthly Expected Credit Loss |
| 62 / A62 | Monthly Other Provisions |
| 63 / A63 | Monthly Profit Before Tax |
| 64 / A64 | Monthly Tax |
| 65 / A65 | Monthly Net Profit |
| 67 / A67 | Monthly ROAA |
| 68 / A68 | Monthly ROAE |
| 69 / A69 | Monthly Cost/Income |
| 70 / A70 | Monthly Net Interest Margin |
| 72 / A72 | Monthly Operating Revenue |
| 73 / A73 | Monthly Net Interest Income |
| 74 / A74 | Monthly Net Fees&Commissions Income |
| 75 / A75 | Monthly Dividend Income |
| 76 / A76 | Monthly Net Trading Income |
| 77 / A77 | Monthly Other Income |
| 78 / A78 | Monthly Provisions |
| 79 / A79 | Monthly Total Non-Interest Expenses |
| 80 / A80 | Monthly Taxation |
| 81 / A81 | Monthly Net profit |
| 83 / A83 | Monthly Fee / OPEX |

