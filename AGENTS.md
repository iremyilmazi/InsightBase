# InsightBase — repository instructions

- Only maintained version: `InsightBase-V2/finora-lens`. Canonical application source is its `dist/` directory. Top-level legacy copies are not maintained. V1 was deleted by user authorization on 2026-10-09; do not recreate it.
- Before work read `InsightBase-V2/AGENTS.md`, `InsightBase-V2/docs/README.md`, `CURRENT_STATE.md` and task-specific documents.
- **Every development MUST review and update affected Markdown documents in the same task.** This includes features, fixes, formulas, UI, schema, scope, packaging and operational rules. Record changes and actual checks in `docs/CHANGELOG.md`. If no contract changed, explicitly record that conclusion. Work is incomplete with stale documentation.
- Build Windows applications only with `InsightBase-V2/finora-lens/package_three_files.py`: `InsightBase-V2/InsightBase-Windows` contains exactly three app files. The five-file Windows-Live wrapper is built separately with `package_windows_live.py` and intentionally includes its guide/launcher.
- Never publish private Excel, local-data, unapproved saved presentation versions or private test artifacts. User explicitly authorized only `InsightBase-V2/presentations/Sektor-Hikayesi.insightbase.json` (latest explicitly approved v13) on 2026-10-22; this is not blanket permission for other versions. Documentation must not reproduce private financial values.
- User instructions take precedence. Do not infer future publication authorization from an old approval. Keep review changes local until authorized.
