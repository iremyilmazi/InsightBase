# InsightBase version workflow

- The user authorized removing V1 on 2026-10-09. InsightBase-V1 and InsightBase-V1.zip have been deleted. V2 is the only maintained version; do not recreate V1 unless requested.
- Perform all subsequent development in InsightBase-V2/finora-lens. Build Windows deliverables using its package_three_files.py; the output stays in InsightBase-V2/InsightBase-Windows and contains exactly three application files.
- Original top-level finora-lens and InsightBase-Windows are legacy copies; do not use them for V2 work.

# Agent handoff and documentation maintenance

- Before V2 work read InsightBase-V2/AGENTS.md and InsightBase-V2/docs/README.md, then the documents relevant to the task.
- Every new structural change MUST update the affected project Markdown documents in the same task. Architecture, file structure, data schema/row mapping, formulas, UI structure, scope, packaging and operational-rule changes are incomplete without documentation updates. Record accepted changes in InsightBase-V2/docs/CHANGELOG.md.
- Documentation is outside the three-file Windows deliverable. Never place it in InsightBase-V2/InsightBase-Windows. V1 no longer exists.
