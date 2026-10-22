# Product purpose and scope

> **Mandatory documentation maintenance:** Every development must review and update the affected Markdown documents in the same task, including fixes, features, calculations, UI, data mapping, packaging and operational rules. Record the change and actual verification in CHANGELOG.md. If no contract changes, record that conclusion and verification in the change log. A task is incomplete with stale documentation. Never include private financial values in documentation.

InsightBase is an offline banking-sector dashboard and recurring presentation workbench. The user must understand balance-sheet growth, funding structure and profitability, drill into details and produce editable presentations without AI access. Prefer useful finance/strategy analysis and restrained modern design over technical controls and dense instructions.

The current normative requirements are in REQUIREMENTS.md; current decisions and release status are in CURRENT_STATE.md. Excel structure/formulas are owned by DATA_CONTRACT.md and CALCULATIONS.md, not by assumptions from metric names.

## Non-negotiable product rules

- Preserve InsightBase brand, source metric meaning/language, Excel title hierarchy and financial units.
- Automatic adjacent Excel reading with no workbook upload screen; support Windows CMD and offline Edge.
- No external transmission of real data. Real supplied files may be used locally at the user's request; the former synthetic-only development rule is obsolete.
- Latest BS/PL data independently; no global historical analysis-date selector. MoM, YoY and YTD are explicit, not conflated.
- UI numbers use en-US separators, with chart/table precision controls where implemented. Dates remain Turkish.
- PL monthly/cumulative selection affects only PL. Keep original English metric names; hide leading Monthly/Cumulative in display only.
- Mini-table settings are independent of chart settings; chart labels must remain legible. PPTX is editable, PDF is a visual export.
- Portable presentation versions preserve definitions and recalculate against local Excel. The old save/open exclusion was explicitly superseded and the feature published.
- No automatic GitHub publishing. Trial changes remain local until the user authorizes release.

## Scope boundaries

Data-quality-summary development, profit bridge and flexible-comparison experiments were declined. Custom floating pie tooltip and verbose period-comparison footer were rolled back. Do not treat old proposals or historical demo files as accepted product requirements. V1 remains deleted. User can request changes to these decisions explicitly.
