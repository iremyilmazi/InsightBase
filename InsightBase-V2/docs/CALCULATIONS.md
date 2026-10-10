# Financial calculation contract

> Maintenance rule: every new structural change must update the affected Markdown documents in this documentation set in the same task. Changes to architecture, files, data contracts, row mappings, formulas, UI structure, packaging, scope or operational rules are incomplete until the matching documentation is updated. Update the index/status date and change log as appropriate. V1 was deleted with user authorization on 2026-10-09; V2 is the only maintained version.

## Dates and current observations

`latestDate(type,group)` selects the greatest date with any finite value in that sheet. BS and PL therefore have independent latest dates. It is not based on today's expected publication date. Empty future columns are ignored; a finite future-dated column currently qualifies (known limitation). Per-row current selection allows at most 7 days back for BS, 32 days for PL from the sheet anchor. Older row values become unavailable. Source dates are shown; do not silently forward-fill stale cells.

`at()` expects a chronologically sorted series and returns the last finite observation on/before the target within tolerance. Never uses a later observation.

## Formulas and bases

| Metric | Rule |
|---|---|
| Amount growth | `(current / base - 1) * 100` |
| Ratio movement | `currentRatio - baseRatio`, percentage points |
| BS MoM | Target one calendar month before actual current observation; clamp day to prior month's last day. Last finite observation on/before target, at most 7 days back. |
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
| Deposits | BS37 | BS42 TL term, BS50 TL demand, BS43 FX term, BS51 FX demand |

Use components on exactly the total's current date (tolerance 0). Need positive total, nonnegative components and positive component sum. Reject rendering and show a source warning if missing or if `abs(sum-total)/total > 0.005` (0.5%). Shares are component / component sum *100; minor accepted rounding discrepancies are normalized to the component sum. Display ratio labels on slices, titles/amounts in clickable legend. Do not invent 'other', force reconciliation or sum nested subcategories.
