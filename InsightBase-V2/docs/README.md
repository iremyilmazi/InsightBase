# InsightBase — agent handoff index

> **Mandatory documentation maintenance:** Every development must review and update the affected Markdown documents in the same task, including fixes, features, calculations, UI, data mapping, packaging and operational rules. Record the change and actual verification in CHANGELOG.md. If no contract changes, record that conclusion and verification in the change log. A task is incomplete with stale documentation. Never include private financial values in documentation.

Verified against current source on **2026-10-21**. Documentation is English for agent portability; the application and user communication are Turkish.

## Required reading order

1. Workspace `AGENTS.md` and [V2 instructions](../AGENTS.md).
2. [Current state](CURRENT_STATE.md): the authoritative current decisions and publication status.
3. [Requirements](REQUIREMENTS.md): product requirements and acceptance criteria.
4. [Architecture](ARCHITECTURE.md), then the relevant specialist documents below.
5. [Development](DEVELOPMENT.md) and [handoff checklist](HANDOFF.md) before delivery.

| Topic | Document |
| --- | --- |
| Purpose and scope | [PRODUCT.md](PRODUCT.md) |
| Source inventory and execution flow | [ARCHITECTURE.md](ARCHITECTURE.md) |
| Excel structure, stable IDs and physical rows | [DATA_CONTRACT.md](DATA_CONTRACT.md) |
| Financial formulas and comparison dates | [CALCULATIONS.md](CALCULATIONS.md) |
| Views, charts and interface behavior | [UI.md](UI.md) |
| Presentation editor, JSON versions, PPTX/PDF | [PPTX_EXPORT.md](PPTX_EXPORT.md) |
| Run, test, package and publish | [DEVELOPMENT.md](DEVELOPMENT.md) |
| Historical decisions and verification | [CHANGELOG.md](CHANGELOG.md) |

## Resolving historical contradictions

Follow the user's latest explicit instructions. CURRENT_STATE.md and current source describe the present implementation; dated older sections are historical and must not reinstate removed features or old restrictions. CHANGELOG is historical evidence, not a standing authorization for future uploads. Source behavior and docs that disagree require investigation, not silent assumptions.

Only `InsightBase-V2/finora-lens/dist` is canonical application source. V1 was deleted by user request; top-level legacy copies are not maintained. Real Excel, private test exports and local snapshots must never be published.
