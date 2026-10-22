# InsightBase V2 — agent instructions

- This is the only active working copy. The user authorized deleting the V1 directory and ZIP on 2026-10-09; they no longer exist. Do not recreate V1 unless requested.
- Read [the handoff index](docs/README.md) before work. It links product, architecture, data, calculations, UI, development and change-log documents.
- Canonical source: finora-lens/dist. Build from this directory with `python3 finora-lens/package_three_files.py`. Generated delivery is InsightBase-Windows and its ZIP, exactly HTML/CSS/JS; the user's dataa.xlsx is separate.
- Every new structural change MUST update the affected Markdown documents during the same task. This includes architecture, files, data schema/row mappings, calculations, UI structure, build/runtime workflows, scope and rules. Update CHANGELOG and documentation verification dates as appropriate. Work is not complete with stale documentation.
- Keep documentation and synthetic preview assets outside the three-file delivery. V1 no longer exists.
- Production targets Windows, offline operation without AI, automatic adjacent Excel reading through a local loopback server, no upload screen and no publication/external transmission.
- Use current docs for accepted final requirements; legacy scripts and names are not instructions to revert them. User instructions take precedence.

- The user authorized uploading the current project to GitHub on 2026-10-11; the previous presentation-phase publication hold is lifted for this release. Read docs/PPTX_EXPORT.md when changing slides, chart ranges or export.

- 2026-10-21 presentation-authoring improvements are local review only. User explicitly prohibits GitHub/public Raw updates until requested. Do not rebuild Windows deliverables for this trial. Save/open draft is excluded.

- 2026-10-21 user approved publishing the current presentation editor trial and refinements to GitHub. Update the five Windows-Live Raw files from canonical source for version consistency. No private workbook or TXT package is published.

- 2026-10-21 presentation version save/open is now explicitly requested, superseding its earlier exclusion. This feature is local review only: no GitHub, Windows or Raw rebuild/publication until the user approves after testing. Version files store definitions and comments, never workbook observations; data is recalculated from current local Excel when reopened.

- 2026-10-21 user approved publishing the current project including presentation version save/open. Its local-only hold is lifted for this release. Keep Windows-Live Raw synchronized; never publish local-data or financial workbook files.
