# InsightBase V2 development

Read [V2 agent instructions](../AGENTS.md), [handoff index](../docs/README.md) and [current state](../docs/CURRENT_STATE.md). `dist/` is the canonical source despite its name.

From repository root:

```sh
node --test InsightBase-V2/finora-lens/tests/*.test.cjs
python3 InsightBase-V2/finora-lens/preview_demo.py --source
```

Preview uses the private local workbook if present. See [Development](../docs/DEVELOPMENT.md) for loopback serving, Windows CMD operation, builders and GitHub Raw publishing. Build production packages only when scope permits; source, three-file app and five-file Live wrapper are separate artifacts. Never package or upload the real workbook.

Presentation authoring, editable PPTX, PDF and portable JSON versions are described in [PPTX_EXPORT.md](../docs/PPTX_EXPORT.md). Every development must update affected Markdown documents and CHANGELOG during the same task; use [HANDOFF.md](../docs/HANDOFF.md).
