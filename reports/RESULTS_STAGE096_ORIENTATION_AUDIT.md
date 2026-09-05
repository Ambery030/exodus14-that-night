# Stage 0.96 Orientation Audit — Fixed Wind versus Mirrored Terrain

Date: 2026-08-20

## Decision

The Stage 0.96E east-wind result is a result for a **mirrored synthetic
geometry**, not a correction of the wind vector on the original geometry.
The eastern placement of sandy relief has an independent historical-map basis;
the exact mirror operation does not.  This distinction was clarified after
the original audit wording treated all ridge-side placements too equally.

At both tested grids, the fixed original terrain failed to expose a complete
route under a true east-to-west wind.  A route reappeared only after the
lagoon, ridges, platforms, storage floor and inlet were all reflected east to
west.

Therefore:

> The previous success cannot be attributed to correcting wind direction
> alone.  It depends on placing the declared ridge network on the eastern,
> upwind side of the synthetic lagoon.

The 1911 map already supports eastern contour-bounded sandy relief beside
lower/wetter ground.  Thus an eastern ridge family is the map-informed primary
prior, while its numerical ridge count, widths, elevations and connectivity
remain synthetic.  West and centre placements are useful falsification
controls, not equally supported primary hypotheses.

## Experiment

The same `mixed_10` family, 21 m/s peak wind, tide, mean stage, wind profile,
roughness and northern marine boundary were retained.  Only two binary axes
were changed:

1. original (`G0`) or east-west mirrored (`GM`) synthetic geometry;
2. west-to-east (`W2E`, +x) or east-to-west (`E2W`, -x) wind.

No population result was used in the decision.

## Results

### 80 x 64

| Case | Complete route first | Route loss | Window |
|---|---:|---:|---:|
| `G0_W2E` | 22:40 | 04:10 | 5.50 h |
| `G0_E2W` | none | none | 0 h |
| `GM_W2E` | none | none | 0 h |
| `GM_E2W` | 22:40 | 04:20 | 5.67 h |

### 120 x 96

| Case | Complete route first | Route loss | Window |
|---|---:|---:|---:|
| `G0_W2E` | 22:30 | 04:50 | 6.33 h |
| `G0_E2W` | none | none | 0 h |
| `GM_W2E` | none | none | 0 h |
| `GM_E2W` | 22:30 | 04:50 | 6.33 h |

The opening/non-opening classification is stable across the two grids.  The
opening clocks are not promoted to converged human-operability clocks.

## Physical reading

In the original synthetic terrain the candidate ridges occupy the western
side.  A true easterly transports lagoon water westward and increases water
over that ridge zone rather than exposing it.  Reflecting the terrain moves
the ridges to the eastern upwind side, where east-wind setdown can expose them.

The mirror also moved the inlet and asymmetric storage floor.  In particular,
it moved a deep edge pocket eastward even though the admitted historical-map
grammar rises toward eastern sandy relief.  Consequently
this audit does **not** determine how much of the result is caused by:

- ridge-side placement;
- inlet-side placement;
- storage asymmetry;
- interactions among them.

## Evidence boundary

The 1911 Ballah audit supports eastern sandy relief and admits segmented and
braided morphology families at historical-map scale.  It does not supply the
mirrored model's ridge count, 5–60 m widths, platform positions, inlet
position, sill profile, storage depths or LBA connectivity.

Drews and Han's Ballah T6/T7 experiments independently show that winds aligned
with the Ballah Lakes can expose lake bed toward the eastern shore, but those
runs left no water on one side and the authors did not classify them as a land
bridge.  They do not validate the Stage 0.96E multi-ridge geometry.

The proper status is:

> `eastern-upwind relief is map-informed at broad historical-morphology scale;
> the successful whole-world mirror is over-broad and its precise synthetic
> realization remains unresolved`.

## Next legitimate test

Use fixed geographic axes and a true east wind.  Do not mirror the world as a
single operation.  The main family should hold eastern sandy relief beside
western/lakeward low ground, then separate at least:

1. alternative segmented/braided realizations inside the eastern relief zone;
2. northern inlet position and control profile as an independent uncertainty;
3. initial water quantity/stage and tide as forcing uncertainties.

Western and central ridge placements remain negative/exploratory controls.

Any geometry supported only as a sensitivity must remain labelled synthetic.
Only after these contributions are separated may human throughput reopen.
