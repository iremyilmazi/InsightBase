# Requirements and acceptance criteria

> **Mandatory documentation maintenance:** Every development must review and update the affected Markdown documents in the same task, including fixes, features, calculations, UI, data mapping, packaging and operational rules. Record the change and actual verification in CHANGELOG.md. If no contract changes, record that conclusion and verification in the change log. A task is incomplete with stale documentation. Never include private financial values in documentation.

## Product purpose

Help a banking-sector finance/strategy user read current balance-sheet and profitability developments, drill into drivers, compare sector/private/public groups and assemble recurring editable presentations. Financial meaning and modern, restrained UI are equally important.

| ID | Requirement | Acceptance evidence / owning document |
| --- | --- | --- |
| R01 | Offline, no AI/CDN or external data transfer | Architecture; inspect runtime fetches |
| R02 | Adjacent dataa.xlsx, automatic reading, no upload screen | Data contract; workbook-reader browser check |
| R03 | Windows CMD/Edge; no PowerShell/Python installation | Development; launcher inspection, actual Windows check when available |
| R04 | Three app files; five-file Live wrapper | Package assertions; Development |
| R05 | No real workbook, saved versions or private exports published | Ignore rules, publication manifest/tree audit |
| R06 | BS weekly/PL monthly; independent latest dates | Engine tests; Calculations |
| R07 | Calendar-aware MoM incl. incomplete month; YoY/YTD; missing != zero | Engine tests and source-date checks |
| R08 | TL/USD source units and ratio semantics preserved | Data contract, engine/presentation tests |
| R09 | Consistent English-style numeric separators, Turkish dates | UI checks; presentation decimal settings |
| R10 | Excel row order/indent/bold/gray respected for titles | UI and schema metadata checks |
| R11 | PL original metric language; monthly/cumulative scope PL only | UI, engine tests |
| R12 | Highlights deterministic and BS-only | highlights.test.cjs; Calculations |
| R13 | Reconciled credit/TL/FX pies with history and pair comparison | Composition engine tests and browser checks |
| R14 | Independent chart/table rows, groups, measurements, units and decimals | presentation.test.cjs; editor/export checks |
| R15 | Editable PPTX charts/data/text/tables; visual PDF | Native chart XML tests; browser export downloads |
| R16 | Timestamped portable versions, strict import validation, no embedded observations | Version unit tests and browser round-trip |
| R17 | Mini-table does not resize chart labels; aligned periods and padded scales | Bounds tests; visual/browser review |
| R18 | Development changes preserve agreed scope and update docs | Handoff checklist; change log |

## Out of scope / rejected

No automatic AI commentary, cloud synchronization, automatic publishing, Excel upload flow, data-quality-summary project, currency conversion assumptions, rejected profit bridge/flexible comparison, V1 restoration or unsolicited production assets. New features require user scope, not speculation from an old proposal.

## Limits that must remain visible

Presentation chart maximum 24 months and 6 series; mini-table maximum 12 months and 12 expanded metric/group/measurement rows. Version import maximum 5 MB and 100 slides. Missing data stays unavailable. JSON versions preserve definitions, not immutable financial snapshots. Never describe PDF as editable or browser/Node tests as proof of real Windows execution.
