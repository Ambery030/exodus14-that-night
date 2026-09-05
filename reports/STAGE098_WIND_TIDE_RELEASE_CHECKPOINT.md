# Stage 0.98 — Wind–Tide Storage and Release Checkpoint

## Decision in one paragraph

Within the fixed idealized `MI_EAST_RELIEF_V1` world, a regional micro-tide and
an east-to-west gale can cooperate to open a small network of firm sandy routes,
while the wind stores a large internal water-level gradient.  When the wind
falls away, that internal gradient produces a visible, progressive return and
the available route network collapses around dawn.  This supplies a plausible
physical reason for a force already experiencing mobility trouble to decide
that retreat is urgent.  It does **not** produce a cinematic bore or an acutely
destabilizing current: the present return is too slow and weak to serve as a
stand-alone drowning or overturning mechanism.

This is a mechanism-family result, not a reconstruction of Late Bronze Age
Ballah and not a historical conclusion about Exodus.

## Question tested

Can the following sequence occur without adding an artificial time lag or a
hand-specified return wave?

1. An easterly acts through the night.
2. Falling external water level and wind setdown expose firm routes.
3. Mixed people/stock begin moving as soon as a travelling route becomes usable.
4. Wind stress maintains a westward water pile/head while the external tide
   approaches and passes low water.
5. Wind decays to zero near dawn.
6. Stored lagoon head and the rising external boundary cause progressive rewetting
   and loss of the route network.

No Egyptians, chariots, injury, panic, or fatality process is simulated here.
The reported `alarm_proxy` is only a transparent physical-operational screen.

## Read-only textual constraints retained

- Exodus 14:19–20: the camps are separated during the night.
- Exodus 14:21: a strong easterly acts across the night; the sea is driven/made
  dry and the waters divide.  The verse does not specify a constant wind speed
  or an instantaneous opening.
- Exodus 14:22: the Israelites move within the sea-space on dry ground, with
  substantial lateral water boundaries.  Exposed mud is not automatically
  treated as dry, trafficable ground.
- Exodus 14:23: the Egyptians later enter the sea-space after the Israelites.
- Exodus 14:24: the morning-watch disturbance follows Egyptian entry; it is not
  used here as a claim that pursuit starts only at sunrise.
- Exodus 14:25–28: mobility/driving trouble and recognition of retreat precede
  the commanded major return and covering.

Stage 0.98 tests only the opening and natural return clocks needed before the
Egyptian sequence can be inserted.

## Fixed idealized world

| Item | Setting | Evidence status |
|---|---:|---|
| Domain | 60 × 20 km | Computational world, not crossing distance |
| Orientation | east wind pushes water west | Locked physical direction |
| Geometry | `MI_EAST_RELIEF_V1`; three resolved synthetic sandy backbones | Map-informed synthetic family; not an LBA DEM |
| Nominal backbone widths | 60, 45, 30 m | Hypothesis, not measured ancient ridges |
| Low ground | mud/sabkha closed to traffic | Conservative substrate rule |
| Mean relative stage | −0.20 m | Sensitivity initial condition |
| External tide | 0.15 m amplitude, 0.30 m range | Regional microtidal analogue |
| External low-water clocks | 02:30–06:00, 30-min increments | Phase sensitivity, not an ancient tide prediction |
| Peak wind | 18.5, 19.0, or 19.5 m/s | Gale sensitivity; human operability is limited |
| Wind profile | 1 h ramp; peak 17:00–22:00; decay to 12 m/s by 01:00; 12 m/s tail; final 0.5 h decay to calm | Hypothetical text-compatible profile, not observed ancient weather |
| Calm clocks | 04:00, 04:30, or 05:00 | Sensitivity |
| Mixed movement | 0.60 m/s; 0.30 equivalent units/(m·s); entry allowed below 13 m/s | Conservative modelling surrogate, not a census or field calibration |

The 19 m/s peak is not called comfortable.  The project evidence ledger notes
that official Beaufort descriptions put roughly 17.2–20.7 m/s in a band where
progress is generally impeded, and wind-tunnel evidence shows substantial
class/orientation sensitivity near 20 m/s.  Accordingly, mixed traffic is not
released during the peak gale.

## Controls

At 120 × 96 cells:

- **Tide only:** negligible route-opening effect.
- **Wind only:** built the larger restoring current, but did not lower this
  particular route network enough to form a complete trafficable crossing.
- **Wind + tide:** formed a complete travelling route.  The tide therefore
  assists the *opening threshold*, but it does not amplify the immediate
  post-wind current in a simple monotonic way.

This is interaction, but not a claim that two equal opposing forces form a
stationary vertical stack.  In shallow-water terms the wind stress is balanced
by a free-surface pressure gradient, friction, storage redistribution, and
boundary exchange.

## Phase-screen result

Twenty-four 19 m/s cases combined eight low-water clocks (02:30–06:00) with
three final calm clocks (04:00, 04:30, 05:00):

- 18/24 delivered a positive safe mixed-equivalent capacity by 05:30.
- Every phase case produced `noticeable_progressive_return` under the declared
  operational screen.
- None reached `urgent_retreat_pressure` or the acute `h|u|` screen.
- Low water near 04:30–05:00 gave the largest capacities in the 80 × 64 screen;
  low water at 02:30 closed too early, while 06:00 was mostly too late.
- Successful cases occupied a multi-hour phase band, not a single magic minute.

The low-water clocks remain sensitivities because no securely dated ancient
tide has been reconstructed.

## Representative converged results

### Case A — low water 04:30, calm 04:30

| Grid | First route | Route depth minimum | +2 cm local rewet | All tested segments closed | Safe mixed-equivalent completion by 05:30 |
|---:|---:|---:|---:|---:|---:|
| 80 × 64 | 00:50 | 05:10 | 05:50 | 06:00 | 54,000 |
| 120 × 96 | 01:00 | 05:10 | 05:40 | 06:40 | 43,200 |
| 160 × 128 | 01:00 | 05:10 | 06:10 | 06:50 | 43,200 |

### Case B — low water 03:30, calm 05:00

| Grid | First route | Route depth minimum | +2 cm local rewet | All tested segments closed | Safe mixed-equivalent completion by 05:30 |
|---:|---:|---:|---:|---:|---:|
| 80 × 64 | 01:00 | 05:20 | 06:10 | 06:00 | 43,200 |
| 120 × 96 | 01:00 | 05:20 | 06:00 | 06:30 | 32,400 |
| 160 × 128 | 01:10 | 05:20 | 06:20 | 06:50 | 32,400 |

The capacity stabilizes between 120 × 96 and 160 × 128 in these two screens.
The exact +2 cm rewet clock still carries about ±30 min numerical uncertainty.
The closure clock is more stable at the two finer resolutions (10–20 min
difference), but it is not a field prediction.

### Wind robustness at low water 04:30 and calm 04:30 (120 × 96)

| Peak wind | First route | +2 cm local rewet | All segments closed | Safe completion by 05:30 |
|---:|---:|---:|---:|---:|
| 18.5 m/s | 01:00 | 05:40 | 06:20 | 43,200 |
| 19.0 m/s | 01:00 | 05:40 | 06:40 | 43,200 |
| 19.5 m/s | 00:50 | 05:40 | 06:50 | 43,200 |

The result is not sensitive to a 0.5 m/s adjustment around 19 m/s.  Stronger
wind in this narrow range tends to postpone final closure rather than increase
the 05:30 capacity.

## What actually stores and returns the water?

In the 120 × 96 reference case (low water 03:30, calm 04:30):

- maximum pre-calm west-minus-east free-surface difference: about **0.87 m**;
- west-minus-east difference at calm: about **0.62 m**;
- west-zone storage above its initial value at calm: about **39 million m³**;
- west-zone volume lost from 04:30 to 06:30: about **13 million m³**;
- the specifically monitored sill flux at calm was effectively zero.

The key result is therefore a **staged return**:

1. Falling external tide helps lower the route threshold.
2. Wind maintains a large internal westward surface tilt.
3. When wind stress vanishes, the lagoon's own pressure gradient first restores
   water eastward across the route area.
4. The rising external boundary later adds water and maintains closure pressure.

The model does **not** show a large Mediterranean surge immediately crossing the
tested sill after calm.  In this geometry the sill is nearly dry-disconnected
during the first return interval.  A direct “wind and incoming tide hold a wall
of water at the inlet, then the sea rushes in” interpretation is therefore not
supported by this run.

## Is the return alarming?

Across the 24-phase 80 × 64 screen:

- post-calm route p95 speed: **0.106–0.141 m/s** (about 0.38–0.51 km/h);
- local maximum `h|u|`: **0.029–0.050 m²/s**;
- maximum median-route depth rise: **0.083–0.093 cm/min** (about 5.0–5.6 cm/h);
- the resolved route width eventually falls to zero.

The finer selected cases give comparable p95 speeds up to about 0.15 m/s and
depth-rise rates around 0.08–0.11 cm/min.

This is enough to produce observable cues: moving water, steadily deepening
footing, disappearance of alternative sandy lanes, and a closing retreat clock.
For an already mobility-degraded force, those cues are a physically reasonable
basis for recognizing danger and attempting retreat.  The model does not and
cannot calculate the emotion “panic.”

It is not an acute hydraulic knockdown:

- the local `h|u|` result is far below the deliberately lenient project screen
  of 0.70 m²/s;
- it is also far below the commonly cited adult moment-instability scale around
  1.32 m²/s used only as an external comparator.

Thus the present verdict is:

- **reason to become alarmed and retreat:** physically plausible, conditional
  on prior mobility trouble and loss of route options;
- **violent rollback by water alone:** not demonstrated;
- **drowning/overturning/fatality:** not tested and not inferable.

## Text-clock alignment offered by the surviving family

One representative, not unique, sequence is:

| Local clock | Model event | Text relationship |
|---:|---|---|
| 16:00 | event/camp clock begins | schematic only |
| 17:00–22:00 | 19 m/s easterly peak | strong east wind across the night |
| 22:00–01:00 | easterly decays to 12 m/s | still easterly; peak human exposure avoided |
| about 01:00 | first travelling route; mixed traffic begins | Israelites can enter before the full route is simultaneously dry |
| 03:30–05:00 | tested external low-water band | sensitivity, not dated ancient tide |
| 04:00–05:00 | final easterly decay to calm | allows movement without the peak headwind |
| 05:10–05:20 | route depth minimum in selected cases | maximum opening need not equal first entry |
| 05:40–06:20 | local route has risen 2 cm | progressive return cue |
| 06:30–06:50 | all tested sandy segments closed at finer grids | later closure envelope |

Exodus 14:23 places Egyptian entry before the morning-watch disturbance of
14:24.  Stage 0.98 has not inserted the Egyptians, so this timeline is not yet a
complete textual pass.  The next stage must freeze the terrain, forcing, and
water clocks before pursuit is added.

The phrase “all night” remains a textual sensitivity.  A weakening easterly that
finally becomes calm near the predawn/morning boundary is not directly excluded
by a text that gives no meteorological timestamp, but a reading that requires
strong wind through sunrise would conflict with these human-operability cases.

## Hard limitations

1. The tide phase is not an ancient astronomical reconstruction.
2. The terrain is synthetic and map-informed, not an LBA DEM.
3. Only three resolved sandy backbones are used here; the intended mixed
   fine-ridge/coarse-ridge/platform family is not yet represented.
4. The 32,400–43,200 results are mixed-equivalent capacities under one chosen
   speed and specific-flow surrogate, not a census of people plus animals.
5. Livestock performance under sustained 18–22 m/s wind remains an evidence gap.
6. No Egyptian entry, wheel degradation, retreat queue, route-choice error,
   injury, or fatality mechanism is present.

## Decision gate

The wind–tide–storage family passes a limited gate:

> It can produce an overnight opening, early travelling entry, stored internal
> head, and a dawn-scale progressive closure over a non-singleton phase and wind
> range.

It fails the stronger gate:

> The present return is not independently violent enough to explain acute
> incapacitation or covering of the pursuers.

The legally next experiment is to freeze selected surviving worlds and add the
Egyptian sequence as a multi-class route/vehicle problem.  A case passes only if
the Egyptians enter, mobility trouble precedes the return, retreat becomes
operationally impossible before the network recovers, and no forcing or terrain
parameter is retuned after seeing the pursuit result.

## Source anchors

- Exodus text ledger: Sefaria, Exodus 14:19–28 and BDB lexical anchors.
- A. B. Tulloch (1894/95), historical report of the 1882 Lake Menzaleh easterly
  setdown: <https://biblicalstudies.org.uk/articles_jtvi-02.php>
- Drews & Han (2010), wind-setdown mechanism/control model:
  <https://doi.org/10.1371/journal.pone.0012481>
- Elshinnawy et al. (2021), modern Bardawil regional micro-tide analogue:
  <https://doi.org/10.3390/su13137392>
- FAO, lagoon hydraulic controls:
  <https://www.fao.org/4/t0369E/T0369E02.htm>
- U.S. National Weather Service Beaufort scale:
  <https://www.weather.gov/mfl/beaufort>
- Jordan et al. (2008), human gust-response experiment:
  <https://doi.org/10.1016/j.buildenv.2007.08.004>
- Jonkman & Penning-Rowsell (2008), human hydraulic-instability comparator:
  <https://doi.org/10.1111/j.1752-1688.2008.00217.x>

## Reproducibility

- Driver: `stage098_wind_tide_release.py`
- Hydro diagnostics: `stage096_coupled_pilot.py`
- Corrected phase screen: `outputs_stage098_phase80_corrected/`
- 120 × 96 selected cases: `outputs_stage098_refine120/`
- 160 × 128 convergence cases: `outputs_stage098_refine160/`
- Verification: `python -m unittest discover -s tests -v` — 78 tests passed.

