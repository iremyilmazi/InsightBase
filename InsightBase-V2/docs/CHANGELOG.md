# Accepted changes and current status

> Maintenance rule: every new structural change must update the affected Markdown documents in this documentation set in the same task. Changes to architecture, files, data contracts, row mappings, formulas, UI structure, packaging, scope or operational rules are incomplete until the matching documentation is updated. Update the index/status date and change log as appropriate. V1 was deleted with user authorization on 2026-10-09; V2 is the only maintained version.

## V1 freeze — 2026-10-07

Original project preserved in InsightBase-V1 and InsightBase-V1.zip with hash manifest. This protection was superseded by explicit deletion authorization on 2026-10-09. V2 was initially a byte-identical working copy.

## V2 changes accepted in the conversation

- Weekly BS changes replaced by one-calendar-month MoM; YoY and YTD retained.
- Charts now show one selected change series over 12 months; point labels in dialogs.
- Overview replaced Growth rhythm/main table with BS/P&L card blocks.
- Removed sidebar research/phase explanatory text.
- BS source confirmed million TL; removed source-unit choice; single million/billion/trillion display selector.
- Maximum two fractional digits for all financial display values.
- Added credit pie (retail/commercial/cards) and TL/YP loan cards.
- Pie ratios moved to slices; clickable legends show labels/amounts only.
- Restored deterministic highlights, then moved them above both pies.
- Added deposit pie: TL term/demand and FX term/demand.
- BS cards grouped into Krediler / Mevduat, with identical card sizing.
- Removed historical analysis date and latest button; BS/PL use their own latest populated periods.

These changes were incremental; this list records accepted final behavior, not a precise timestamp for each edit.

## Documentation handoff — 2026-10-09

Added comprehensive docs set, complete template row catalog and binding documentation-update rule in agent entry points. Superseded stale V2 instruction claiming no feature changes and replaced stale development README. Documentation-only task; no new product feature or delivery rebuild required.

## Validation evidence and limits

Earlier engine run: 14/14 passed. Browser checks covered unit conversion (percentages unchanged), single-line/detail switching, default MoM with 12 valid points on demo, card dialogs, both pies and subgroup labels, equal BS card dimensions and removed date picker. YoY demo may contain fewer than 12 valid values due to insufficient prior-year data. Do not claim Windows launch was tested. Preview artifacts live in V2, outside delivery.

## V1 removal — 2026-10-09

User explicitly stated V1 was no longer needed. Removed InsightBase-V1 and InsightBase-V1.zip. Updated agent instructions and documentation to make V2 the only maintained version. No V2 runtime or delivery changes. Earlier V1 verification statements above are historical.

## GitHub preparation — 2026-10-09

Added root README and Git allowlist/ignore rules for active V2 only. GitHub Desktop control is currently unavailable; repository creation and upload are not yet confirmed.

## GitHub connection and transfer — 2026-10-09

Verified connected identity iremyilmazi and existing private InsightBase repository with write/admin access. Transferring tracked V2 source, documents and three-file Windows package through the GitHub plugin. Workbook data and preview artifacts remain excluded.
