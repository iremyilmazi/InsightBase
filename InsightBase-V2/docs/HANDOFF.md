# Agent completion and handoff checklist

> **Mandatory documentation maintenance:** Every development must review and update the affected Markdown documents in the same task, including fixes, features, calculations, UI, data mapping, packaging and operational rules. Record the change and actual verification in CHANGELOG.md. If no contract changes, record that conclusion and verification in the change log. A task is incomplete with stale documentation. Never include private financial values in documentation.

## Before implementation

1. Read both AGENTS files, README, CURRENT_STATE and task-specific docs.
2. Inspect canonical code and current local/remote state; separate unpublished work from published releases.
3. Identify the authorized scope. Read-only checks and local reversible implementation do not require repeated permission. Do not upload to GitHub when the user asked for a local trial.
4. Locate data privately. Never print large private tables or put real numeric observations in fixtures, comments, docs or source.

## During development

- Work only in V2 canonical source. Generated Windows files are not the implementation authority.
- Preserve existing financial definitions and explicitly label unavoidable assumptions.
- Run focused checks, then existing relevant tests. Use visual checks for layout; syntax/test success alone is not visual verification.
- Keep local review rollback material private. Do not reset unrelated user work or recreate legacy versions.

## Documentation update matrix — mandatory on every development

| Change | Required documents to review/update |
| --- | --- |
| Feature, requirement or scope | REQUIREMENTS, PRODUCT, CURRENT_STATE, UI |
| Modules/files/dependencies | ARCHITECTURE, DEVELOPMENT |
| Workbook schema/labels/units/row mapping | DATA_CONTRACT, CALCULATIONS, CURRENT_STATE |
| Financial comparisons/highlights | CALCULATIONS, relevant DATA_CONTRACT/UI |
| Presentation settings, layout, export or JSON schema | PPTX_EXPORT, UI, ARCHITECTURE as affected |
| Launch, packaging, privacy, publishing | DEVELOPMENT, AGENTS, CURRENT_STATE |
| Fix without contract change | CHANGELOG with defect, impact and checks; affected guides if instructions change |
| Any development | CHANGELOG, verification date/status; document limitations honestly |

Update affected documents in the same task. Add/change links when files are added/renamed. Do not mass-touch unchanged docs merely to change dates. If a document has no applicable change, record the reviewed no-change conclusion in CHANGELOG. Historical notes must not contradict the current-state summary without an explicit supersession label.

## Before delivery

- Relevant tests pass; failures/untested platforms are stated clearly.
- Preview and exports inspected when layout/data flow changes.
- Markdown links resolve; current status reflects actual publication, not merely user approval.
- Private data and local test artifacts remain excluded; package file counts correct if built.
- Publishing: authorized scope only, current remote parent, no force overwrite, verify resulting head and Raw versions. Never accidentally include a pending feature in a diagnostic-only release.
- Final answer states outcome, verification, limitations and whether GitHub/Windows were updated.
