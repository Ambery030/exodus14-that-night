# Stage 0.96E — Corrected East-Wind and Operability Pilot

Date: 2026-08-20

> **QUALIFIED BY THE ORIENTATION AUDIT:** This run uses a true east-to-west
> wind, but it also mirrors the lagoon, ridges, platforms, storage floor and
> inlet.  It is therefore a mirrored synthetic east-wind family, not a
> same-terrain wind-vector correction.  A later 2 x 2 audit found no complete
> route when only the wind was corrected on the original geometry.  See
> `RESULTS_STAGE096_ORIENTATION_AUDIT.md`.  Population capacities below remain
> unresolved and must not be treated as fixed-terrain Ballah results.

## Correction

The prior Stage 0.96 report is withdrawn.  Its wind pointed toward increasing
`x`, while the geometry labelled increasing `x` as east.  That was a
west-to-east wind, not the Exodus east wind.  It also allowed a fixed mixed
population speed during gale-force exposure.

Stage 0.96E mirrors the lagoon, inlet, ridges, platforms and storage basin and
uses a 180-degree wind vector: east to west.  Human flow is prohibited until
the decaying wind falls below a declared operability sensitivity.

## Corrected forcing and mobility

- event zero: 18:00;
- 1 h wind ramp;
- peak wind through 00:00;
- linear decline from peak to a 6 m/s easterly tail by 04:00;
- the 6 m/s tail continues through the simulated night;
- external tide amplitude: 0.15 m, low water at 03:34;
- spring-low relative mean stage: -0.05 m;
- route length: 6.8 km;
- mud remains closed;
- firm sand is passable only at `h <= 0.10 m` and `h|u| <= 0.20 m²/s`.

The mobility limits are explicit sensitivities, not measured ancient
mixed-herd thresholds:

| Class | Enter only once wind ≤ | Speed | Specific flow |
|---|---:|---:|---:|
| urgent pedestrian upper | 16 m/s | 0.90 m/s | 0.65 person/(m·s) |
| mixed people–livestock central | 14 m/s | 0.65 m/s | 0.40 person-equivalent/(m·s) |
| burdened / stock-heavy | 12 m/s | 0.50 m/s | 0.28 person-equivalent/(m·s) |

At peak winds of 20, 21 and 22 m/s, the mixed-central entry gates occur at
approximately 01:43, 01:52 and 02:00.  The model no longer assumes a mixed
group walks normally in 20 m/s wind.

## Coarse mechanism result

At 80 × 64:

| Peak east wind | Complete hydro route? | Mixed-central conditional capacity |
|---:|---|---:|
| 18 m/s | no | 0 |
| 20 m/s | yes, but too little post-operability clearance | 0 |
| 21 m/s | yes | 57,600 |
| 22 m/s | yes | 115,200 |

The burdened/stock-heavy class did not complete a crossing in these four coarse
runs.  Thus the corrected model exposes a sharp wind–operability tradeoff:
weaker wind does not open enough terrain, while stronger wind delays safe
human/stock entry until the route is already recovering.

## Hydrodynamic clocks

Across the 120–160 grids, the 21–22 m/s worlds broadly produced:

- first complete parallel route: 22:10–22:30;
- local route-zone minimum: 01:40–02:00;
- first 2 cm recovery: 02:30–03:00;
- simultaneous parallel-route loss: approximately 04:50–05:50;
- mixed-central entry after wind operability: approximately 02:00;
- first mixed-central arrival: approximately 05:00.

These clocks support a travelling-opening mechanism, but pursuit timing has not
been added and the final population capacity is unresolved.

## Residual water

At route-zone minimum, about 80–90% of the route-zone area remains at least
0.30 m deep across the tested grids.  At 160 × 128, the two lateral probe zones
remain approximately 1.13–1.19 m deep in the 21–22 m/s cases.  The mechanism
does not dry the basin as a whole: sparse firm highs coexist with substantial
water and deeper channels.

The marine connection remains predominantly `sea -> lagoon` after the wind
depresses the lagoon-side head.  Falling external tide mainly reduces adverse
marine refill; it does not act as an automatic outward pump in this geometry.

## Numerical convergence failure

Mixed-central, independent-route capacities for 21 m/s were:

| Grid | Capacity |
|---|---:|
| 80 × 64 | 57,600 |
| 120 × 96 | 115,200 |
| 160 × 128 | 154,800 |
| 200 × 160 | 10,800 |

The abrupt reversal at 200 × 160, together with shifts in route opening and
closure, is a hard numerical failure for population inference.  The cause is
structural: a 60 km domain with 300–750 m cells cannot resolve declared
5–60 m ridges.  Cell-centre alignment and wet/dry classification change which
ridge segments form a continuous route.

Accordingly:

> The corrected model supports the existence of an east-wind travelling-route
> mechanism in the declared synthetic family, but does not provide a converged
> `N_max` for a mixed population.

No value above may be used as a historical population estimate or as proof
that a stated Exodus population crossed.

## Decision

1. Correct east-wind setdown with residual deep water: **survives**.
2. 20 m/s mixed-population passage: **fails the current operability/clearance
   gate**.
3. 21–22 m/s mixed-population passage: **conditional mechanism survives**.
4. Maximum population: **unresolved due non-convergence**.
5. Egyptian pursuit: **not yet admissible**.

The next legitimate experiment is a nested/local high-resolution wetting and
drying model around the ridge network, driven by boundary conditions extracted
from the 60 km basin model.  It must resolve 5–60 m ridges without pretending
the whole regional domain can do so.  Only after local route clocks and widths
converge may population throughput reopen.
