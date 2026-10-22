# Financial calculation contract

> **Maintenance:** Every development must review and update affected Markdown documents in the same task; record changes, checks and any no-contract-change conclusion in CHANGELOG.md. See [HANDOFF.md](HANDOFF.md).

> Current implementation and publication status: [CURRENT_STATE.md](CURRENT_STATE.md), verified 2026-10-21. Older dated addenda are historical; current decisions supersede conflicting past statements.

## Dates and current observations

`latestDate(type,group)` selects the greatest date with any finite value in that sheet. BS and PL therefore have independent latest dates. It is not based on today's expected publication date. Empty future columns are ignored; a finite future-dated column currently qualifies (known limitation). Per-row current selection allows at most 7 days back for BS, 32 days for PL from the sheet anchor. Older row values become unavailable. Source dates are shown; do not silently forward-fill stale cells.

`at()` expects a chronologically sorted series and returns the last finite observation on/before the target within tolerance. Never uses a later observation.

## Formulas and bases

| Metric | Rule |
|---|---|
| Amount growth | `(current / base - 1) * 100` |
| Ratio movement | `currentRatio - baseRatio`, percentage points |
| BS MoM | Shared monthlyCompare: when asOf is before current month-end, compare actual current date with one calendar month earlier (day clamped); after month close use prior calendar month-end. Last finite observation on/before target, at most 7 days back. |
| PL MoM | Exact previous calendar month-end, tolerance 0. |
| BS YoY | Same day prior year (leap date clamped), at most 7 days back. |
| PL YoY | Exact same month-end previous year. |
| BS YTD | Previous year's December 31, at most 7 days back. |
| PL YTD amount | Source cumulative row, not sum fabricated from monthly cards. |
| PL YTD YoY | Cumulative current versus same prior-year month-end. |
| January cumulative MoM | Do not compare the new year's January cumulative value to prior full-year December; return null. |
| Missing source LDR (BS57) | Same-date BS3 / BS37 * 100 if both finite and deposits positive; label as calculated. Preserve existing source ratio if present. |

Null is not zero. Missing/nonfinite values and amount bases <=0 produce null growth. Current zero with a positive base produces -100%. Missing comparisons appear as “—”. These rules do not imply positive growth is financially beneficial.

## Units and precision

Raw BS and PL amounts are million TL. Display conversion is divide by 1 (million), 1000 (billion) or 1000000 (trillion). YP/FX amounts are TL equivalents, not dollar/euro balances. Ratios and changes never undergo amount conversion. `Intl.NumberFormat('tr-TR', {maximumFractionDigits:2})` applies to displayed values and labels; calculate at full precision and round only for display.

## Twelve-month line charts

- Default horizon MoM. Choices: MoM, YoY, BS YTD / PL YTD YoY.
- One metric, one horizon, one line; no nominal level or normalized index line.
- Twelve consecutive calendar slots anchored to the latest available observation of that metric.
- Use each month's last valid observation on/before month end, within BS 7 / PL 32-day tolerance and in that same month. The current incomplete month uses available observations up to the latest anchor.
- Reapply the comparison engine for each observation. BS MoM uses the one-calendar-month-back target, not necessarily the preceding plotted dot.
- Missing values break the path; never join through gaps or interpolate. Twelve slots do not guarantee twelve valid percentages: YoY needs the prior year's history.
- Detail graphs label each finite point. Spark lines use the same monthly changes without labels. Ratio units are points.

## Deterministic highlights — current algorithm

Candidates in input order: BS3 loans, BS37 deposits, BS31 cards, PL65 profit, PL49 NII, PL53 fees. Compute each metric's MoM, drop nonfinite changes, sort descending by absolute change, take first three. Stable ties preserve candidate order. It always uses MoM even when the card horizon is YoY/YTD.

Text contains direction, absolute percentage magnitude, prior/current dates and signed amount difference. 'Mutlak fark' in UI is the arithmetic amount difference (`current - prior`), not `abs(current - prior)`. The final 'components / FX should be examined' messages are static prompts, not causal findings. Source weekly/monthly updates can leave different latest periods. Unit selection does not alter ranking.

No materiality threshold, amount-based weighting, historical anomaly score, causal attribution or favorable/adverse judgment. Financially small amounts can outrank large movements by percentage.

## Composition pies

| Pie | Total | Exclusive components in display order |
|---|---|---|
| Credits | BS3 | BS12 retail, BS21 commercial, BS31 credit cards |
| TL deposits | BS38 | BS42 TL term, BS50 TL demand |
| FX deposits | BS39 | BS43 FX term, BS51 FX demand |

Use components on exactly the total's current date (tolerance 0). Need positive total, nonnegative components and positive component sum. Reject rendering and show a source warning if missing or if `abs(sum-total)/total > 0.005` (0.5%). Shares are component / component sum *100; minor accepted rounding discrepancies are normalized to the component sum. Display ratio labels on slices, titles/amounts in clickable legend. Do not invent 'other', force reconciliation or sum nested subcategories.

## Presentation series

The presentation editor has independent month ranges and month-end BS baselines, including MoM versus prior month end rather than latest-week rolling baseline. PL YTD means cumulative YoY and requires the current cumulative source month. See [PPTX_EXPORT.md](PPTX_EXPORT.md) for all rules and constraints. This does not change dashboard/detail calculation defaults.

## 2026-10-11 deposit composition update

Overview now has two separate deposit pies. TL total BS38 reconciles against BS42 (TL term) + BS50 (TL demand); FX total BS39 reconciles against BS43 (FX term) + BS51 (FX demand). Each percentage is relative to its own currency total, not overall deposits. Existing same-date, nonnegative-value and 0.5% reconciliation checks apply independently. Credit composition is unchanged.


## Current schema update — 2026-10-11

The user supplied a new six-sheet reference `şablon (1).xlsx`. DATA_CONTRACT.md is the authoritative current catalog; earlier physical row numbers in this document are superseded. Stable internal metric IDs remain, with explicit `sourceRow`, `format` and `ratio` metadata. BS has 46 supported metrics; P&L 66. Date headers start in C, with B reserved for Format. `extract_structure.py <reference.xlsx>` extracts metadata only and writes both structure.json and structure.js. No financial values are committed.

TL means million TL, USD million USD, % ratio, explicitly confirmed by the user. NPL rows flagged % now use percentage-point changes. Dashboard cards, detail tables, pies and slide outputs preserve each currency. No FX conversion or TL+USD addition occurs. Nominal/pie charts mixing currencies are rejected; growth charts may compare percentage changes and table rows show their own currencies. Monthly P&L-to-cumulative ID offset remains 38 (physical source offset also 38). Removed TL/YP NPL volume rows, branch/headcount and aggregate term/demand source rows are excluded. LDR fallback uses total loans and total deposits, both TL aggregates.

The local 8768 preview keeps synthetic JSON and shows DEMO. The new Windows live delivery excludes Excel; the user provides adjacent dataa.xlsx. Canonical three-file build stays unchanged in count. Additional CMD launcher and guide are operational helpers. Source Excel passed the browser reader with six sheets and zero warnings; 18 engine/presentation tests passed, including ratio deltas and mixed-currency rejection. Local browser preview verified TL/USD labels and USD detail with no page errors. Windows itself remains unverified. This change is not automatically published to GitHub.

New structural changes must update these Markdown files in the same task.


## Reference update — 2026-10-13

Current schema is `şablon (2).xlsx`. BS consumer-loan volume and consumer NPL entries are removed (IDs 13/14); retail loans NPL added as distinct ratio ID112 at source row9. Retail total ID12 remains at source row8. Subsequent BS sources shift up one; stable IDs preserve existing pie/card calculations. BS catalog now has45 metrics; PL retains66 and its source positions. Retail detail uses new ratio plus remaining product breakdowns. Excel source order, title indent/gray/bold and TL/USD/% metadata are regenerated. Local preview retains synthetic data and includes retail NPL. Six source sheets read with zero warnings; existing calculation/export tests passed. Windows packages and GitHub are not rebuilt/published for this task. The current release artifacts therefore remain the preceding release until requested. All structural changes require corresponding MD updates.


## Unified BS MoM — 2026-10-13

User accepted shared monthly comparison: completed months compare final weekly stock to previous calendar month-end observation (7-day backward limit). Provisional latest month compares latest stock to one calendar month earlier (7-day backward limit, never a future observation). Calendar completion uses current UTC day against month-end. Dashboard, 12-month detail chart and slide MoM use shared engine monthlyCompare; P&L unchanged. Slides default range includes latest available month; provisional source dates remain in point metadata. Dashboard cards mark provisional periods. Missing historical month-end data remains missing; no substitution with early-month values. Windows/GitHub publication deferred until requested.


## Highlight scope — 2026-10-13

User is revising highlights incrementally. First accepted change: exclude all P&L metrics. Current candidates are BS total loans(ID3), total deposits(ID37), credit cards(ID31); existing absolute MoM ranking remains pending further instructions. PL basis selection no longer affects highlight candidates. Source-only demo updated; no Windows build or GitHub publication.


## Expanded BS highlights — 2026-10-13

Implemented in pure dist/highlights.js (InsightHighlights.analyze), bundled by preview and Windows builders without changing the three-file contract. It reads BS only and emits up to one growth, funding and NPL/risk card; insufficient data may yield fewer cards. Candidate rules: volume MoM, product-vs-total growth, TL/USD growth difference, TL/FX demand-deposit share changes, loan/deposit growth difference, LDR and NPL point changes, completed-month credit acceleration, sector-view private/public growth differences. Composition and contribution are excluded pending scope confirmation. Shared monthlyCompare supplies MoM bases. Derived metrics require identical current/base dates. Demand shares additionally require nonnegative same-currency components and 0.5% total reconciliation at both dates.

No financial significance cutoff or anomaly label is invented. For completed periods with12 prior valid completed observations (searching36months), selection ranks empirical absolute deviation from each candidate's own median; MAD is also recorded. Tied scores use stable IDs. Provisional periods cannot use this history ranking. Without comparable history, explicit fallback kind priority is share, fundingGap, currency, product, ratio, growth, groups, acceleration; within a kind, absolute change ranks candidates. This is a deterministic editorial selection, not a financial importance score. Historical values and scoring details are available in analyze return metadata; card method disclosure explains history/fallback choice. Empty, invalid or unchanged candidates are skipped; missing values are never zero-filled. No inferred funding cost or NPL cause is asserted. P&L basis cannot affect cards. Local preview updated; no GitHub publication or Windows rebuilding requested for this change.


## P&L reference3 — 2026-10-13

User supplied şablon (3).xlsx. Secondary cumulative/monthly reporting blocks removed; current source catalog is DATA_CONTRACT.md. PL has46 metrics:22 cumulative,22 monthly,2 auxiliary stocks. Monthly source section starts35 instead of46; cumulative Fee/OPEX is31 and monthly58. Net Profit uses monthly51/cumulative24. Stable metric IDs keep dashboard formulas and existing configured charts intact. Each monthly spec explicitly records cumulativeRow and basis; app and slides use pairing metadata. Physical source difference is27, not internal ID difference38. Removed IDs34–43 and72–81 are absent from tables/selectors. English source wording is retained, display prefixes hidden; source title formatting extracted. BS unchanged, including approved commercial label alias. Demo source remains synthetic. Six sheets read with zero warnings, pairing regression and financial/export tests pass. Windows/GitHub not rebuilt for this task; publication remains separately requested.


## Ratio level chart option — 2026-10-13

Ratio metric detail charts add Oran alongside MoM/YoY/YTD. Oran uses12 monthly source levels (percentage points stored as percent levels), with % point labels, not growth or percentage-point differences. Missing baseline does not suppress valid nominal levels. Level selection is detail-only and never changes the global dashboard horizon/cards; volume metrics have no level button. Existing independent presentation nominal option remains. Source preview updated; no Windows/GitHub publication.


## Twelve-month composition detail — 2026-10-13

Overview credit/TL deposit/FX deposit pie graphics are keyboard-accessible buttons opening a12-calendar-month modal grid. Uses current bank group and same source rows as entry pies. Each historical month selects last weekly total within7days of month-end; current partial month uses latest dataset cutoff. Parts require exact matching source date, nonnegative values and 0.5% total reconciliation. Percent shares use component sum, consistent with entry pie. Share change is current share minus preceding calendar-month share in percentage points; missing/invalid prior month produces no delta (never skip gap). Requires13 slots internally to compute oldest displayed change. Each monthly card shows source date, source-currency total and category shares/deltas; unavailable months remain visible. Metric legend links still open metric detail. Responsive3/2/1-column layout. No Windows/GitHub rebuild.


## Compare arbitrary composition months — 2026-10-13

12-month pie modal includes start/end selectors over valid monthly compositions. End must follow start. Shows each component start/end volume, absolute change, percentage growth, start/end share and percentage-point difference, plus total change and actual source dates. Same source currency/display unit preserved; zero base gives unavailable growth, while share delta remains valid. Invalid months disabled, reverse/same dates rejected. Default is last two valid months, with exact selected dates clearly shown; not labeled MoM. Pure engine compareComposition tested. Local preview updated; no Windows/GitHub rebuild.


## Analysis view rollback — 2026-10-18

User rejected the two trial integrations and requested rollback. Esnek karşılaştırma and Kâr köprüsü are not part of the active product. Removed analysis module/tests, navigation, view registry, events, CSS and loader/bundler hooks. Earlier dashboard, comparison, ratio/composition history, P&L and presentation features retained. Separate synthetic demo in outputs remains isolated for possible future reference. Neither integration was published to GitHub or Windows deliverables, so no release rebuild is needed. Real local workbook remains the active preview input.


## Stable chart typography and adaptive bounds — 2026-10-21

Adding a mini-table no longer shrinks chart labels: preview font sizes compensate for density-based chart height in both dimensions; PDF uses the same physical label size independent of table height, and native PPTX explicitly fixes dataLabelFontSize at 10. Line charts fit finite observations with 22% headroom on each side; constant/narrow series use a 4% magnitude minimum span (absolute floor .01). Unlike bars, line charts do not force zero. Bars/columns retain zero with 18% outer padding. Bounds shared with native PowerPoint; raw data and financial formulas unchanged. Current follow-up remains local until user requests another publication.

## P&L quarter-plus-month series — 2026-10-21

Optional presentation aggregation quarterlyMonthly supports monthly flow amounts and source cumulative P&L amounts. The default remains monthly. All three calendar months must lie within the chosen range for a quarter bucket. Leading/trailing partial quarters retain individual months; the selected end is capped to latest available P&L month across the selected chart/table groups. Different groups share slots and retain missing values independently. A quarter with any missing source month is unavailable, never a partial total or zero. No summation of cumulative source levels occurs.

- Nominal quarter: sum three exact month-end monthly source values, then scale once to the selected unit. Open-quarter months retain monthly observations. Negative nominal flows remain valid.
- Change: quarter versus the previous complete calendar-quarter sum (QoQ); monthly slot versus previous calendar month (MoM). Label QoQ / MoM explicitly. Never compare an open-quarter month to a three-month total.
- YoY: quarter total versus the same three months one year earlier; monthly slot versus the same prior-year month.
- YTD YoY: cumulative source at the exact slot-ending month versus the same prior-year cumulative month, using existing monthly pairing/availability rules.
- Nonpositive amount bases and missing comparisons retain existing null-growth semantics.
- Quarterly ratios (ROAA/ROAE/NIM and other ratios) cannot be inferred by adding/averaging monthly ratios. Their selection in hybrid charts/tables blocks export with an explicit monthly-view instruction. No balance/average-denominator assumptions are introduced.

Switching aggregation preserves the monthly/cumulative basis and identities; only the explicit basis selector remaps paired rows. The original dashboard/BS comparisons are unchanged. Financial catalog and workbook row mappings were reviewed and do not change.


## Cumulative hybrid correction — 2026-10-21

The preceding three-month sum rules describe monthly basis only. Cumulative basis uses the exact source cumulative observation at each slot endpoint: Q1 is January–March, Q2 January–June, July January–July, August January–August. Never add cumulative monthly balances or derive them from monthly flows. Missing exact cumulative endpoints remain unavailable, even when monthly values exist.

Cumulative Change compares quarter-end cumulative levels to the preceding quarter-end within the same year; monthly slots compare to preceding month-end within the year. The Q1 prior-December reset comparison is unavailable. YoY and YTD YoY compare the exact endpoint to the same prior-year month. These are changes in year-to-date levels, not standalone quarterly flow growth. The chart subtitle explicitly says Kümülatif. Ratio restrictions remain unchanged. This correction supersedes the earlier forced-monthly selection limitation.
