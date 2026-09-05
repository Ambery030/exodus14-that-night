# Stage 0.99 — Frozen-Hydro Chariot, Soil, and Queue Screen

## Verdict

The frozen Stage 0.98 world can support the required *ordering* in a declared
family of marginal or patchy wet-sand surfaces:

> 600 chosen chariots enter the sea-space → repeated traffic degrades local
> wheel/hoof mobility → the force recognizes retreat before the first archived
> return cue → dense queues remain when the frozen route network closes.

That result is **conditional**, not a historical reconstruction.  It requires
surface support that is initially trafficable but degrades under repeated
passes or contains soft patches.  A firm-sand control sends all 600 chariots to
the far shore and therefore fails the text.

The screen does **not** show that chariot crashes and horse trampling alone kill
the force.  Sudden-stop conflict appears only weakly in the most compressed
case.  Turning/retreat operability controls the result much more strongly.
Even the best trapping cases allow substantial numbers to return to the
departure shore under the present assumptions, so no tested case yet satisfies
the full Exodus 14:28 no-remnant condition.

No casualties, drowning, injuries, or deaths were simulated.

## Read-only upstream world

The experiment reads, but never reruns or edits:

- `outputs_stage098_refine120/timeseries_phase_w19.0_low04.5_stop04.0_120x96.csv`
- SHA-256: `050c0abccddf3db2c7997dc79c40d4b7d1cd6ac7253460909459904c0d85d5f3`
- Stage 0.98 summary SHA-256:
  `0b5b7977240fc73166cb1b1b4d120505e46a319eae019ad7ab5a6026f9fc1276`

Locked conditions include the 19 m/s east-to-west wind family, 0.15 m external
micro-tide amplitude, 04:30 low-water clock, final wind decay to calm at 04:30,
the fixed 60/45/30 m synthetic sandy backbones, the 05:40 local +2 cm rewet cue,
and 06:40 final tested-segment closure.

The 7 km route is still an idealized model route.  The three backbone widths are
hypotheses, not measured Late Bronze Age ridges.

## Text gates retained

- Exodus 14:7 explicitly supplies 600 chosen chariots, but also mentions the
  broader Egyptian chariot force.  Stage 0.99 therefore treats 600 as a
  conservative explicit detachment, not as proof that only 600 pursued.
- Exodus 14:23 requires Egyptian entry into the sea-space.
- Exodus 14:24 places the morning-watch disturbance after that entry.
- Exodus 14:25 requires driving/wheel difficulty and the decision to flee before
  the main commanded water return.
- Exodus 14:28 scopes the covered/no-remnant force to those who entered the
  sea-space.  Pharaoh's personal location and fate are not modeled.

The model clock 05:30 is only a declared morning-watch diagnostic, not a lexical
translation of `be'ashmoret habboqer` into one exact modern minute.

## Vehicle and queue lock

| Quantity | Central value | Status |
|---|---:|---|
| Chariots | 600 | Text-anchored lower-bound detachment |
| Crew | 2 per chariot | Egyptian iconographic/reconstruction norm |
| Horses | 2 per chariot | Egyptian chariot norm |
| Hardware width comparator | about 1.75 m wheel-to-wheel | Tutankhamun archive |
| Dynamic lateral envelope | 3.0 m central; 2.5/4.0 m sensitivities | Hypothesis |
| Dense columns | 12 central; 9/16 sensitivities | Hypothesis |
| Longitudinal pitch | 10 m central; 7/14 m sensitivities | Hypothesis |
| Team length | 6 m | Explicit screening hypothesis |
| Outbound speed | 1.8 m/s central; 1.5/2.2 m/s sensitivities | Hypothesis |
| Entry clock | 04:00 central | Text-compatible sensitivity |
| Recognition delay | 6 min central | Operational hypothesis |
| Turn success | 55% central; 20/90% sensitivity | Dominant unresolved variable |

The Tutankhamun archive reports an undercarriage about 1.75 m across; a Brown
experimental reconstruction used a 91.75 in (about 2.33 m) axle.  Neither value
is a safe formation width, so the model uses wider dynamic envelopes rather
than packing vehicles wheel-to-wheel.

Sources: [Griffith Institute Tutankhamun Archive](https://www.griffith.ox.ac.uk/gri/4tutchar.html),
[Brown reconstruction record](https://webhelper.brown.edu/joukowsky/courses/fightingpharaohs10/9985.html).

## Soil model and its evidence boundary

The model compares wheel/hoof demand with a declared `kPa-equivalent support`
index that can fall as passes remould a wet surface and as the archived route
rewets.  It is a reduced mobility screen, not calibrated terramechanics.

Three families were tested:

1. `firm_sand_control`: high support and mild pass degradation;
2. `marginal_wet_sand`: initially passable, but support falls with repeated
   traffic;
3. `patchy_sand_over_soft`: marginal backbones plus deterministic soft patches.

The first 1 km is declared as a firm entrance apron so the model cannot trap the
force before it has meaningfully entered the sea-space.  The transition begins
at 1 km.  This apron is a hypothesis, not an ancient observation.

The external basis is qualitative.  USACE guidance relates mobility on wet
sediment to ground pressure and soil strength and warns that breaking through a
critical layer can expose weaker material and immobilize equipment.  General
wheel–soil mechanics likewise makes sinkage and shear/slip central.  These
modern sources justify the *mechanism direction* but cannot numerically
calibrate ancient wooden wheels, horses, or Ballah sediment.

Sources: [USACE EM 1110-2-5027, Appendix I](https://www.publications.usace.army.mil/Portals/76/Publications/EngineerManuals/EM_1110-2-5027.pdf),
[NASA Mechanics of Wheel–Soil Interaction](https://ntrs.nasa.gov/api/citations/19730021941/downloads/19730021941.pdf).

## Principal results

All rows begin with exactly 600 entrants.  `Immobilized` is a subset of those
still trapped at closure, not an additional population.

| Soil / traffic | Far shore | Returned to origin | Actually immobilized | Trapped at 06:40 | First failure | Max queued |
|---|---:|---:|---:|---:|---:|---:|
| Firm / central | 600 | 0 | 0 | 0 | none | 0 |
| Marginal / central | 87 | 328 | 10 | 185 | 04:09:15 at 1.0 km | 175 |
| Patchy / central | 8 | 327 | 18 | 265 | 04:09:15 at 1.0 km | 247 |
| Patchy / high turnability | 8 | 537 | 11 | 55 | 04:09:15 at 1.0 km | 44 |
| Patchy / low turnability | 4 | 120 | 19 | 476 | 04:09:15 at 1.0 km | 457 |
| Patchy / compressed disorder | 3 | 179 | 11 | 418 | 04:26:05 at 1.0 km | 407 |

The marginal/patchy failures precede the locked 05:40 return cue by about 1 h
31 min.  Recognition follows at about 04:15 in central cases.  The ordering gate
therefore passes:

> entry → mobility degradation → retreat recognition → progressive return.

But full textual compatibility does not pass:

- firm sand allows every chariot to complete the crossing;
- marginal/patchy cases still allow 3–87 to reach the far shore;
- central and high-turnability cases allow 327–537 to return to origin;
- even the low-turnability case lets 120 return before closure.

Those vehicles cannot be declared covered by the present model.

## Collision and trampling question

The central 10 m pitch cases did not produce a nonzero sudden-stop collision
proxy.  The compressed 7 m pitch cases produced only **2** conflict exposures,
despite queues exceeding 400 chariots.  This means:

- a dense immobilized queue and thousands of crew–horse interaction minutes are
  physically present;
- collision, entanglement, loss of control, and trampling are plausible hazard
  families in that state;
- the current model does **not** demonstrate enough collisions or trampling to
  explain mass fatality;
- converting queue exposure into deaths would be invented precision.

The dominant discriminator is instead retreat geometry: how many teams can
turn, unhitch, reverse, or leave the chariot on a narrow, wet, crowded ridge?
Changing only central turn success from 90% to 20% changes the patchy result
from 55 trapped to 476 trapped.  That variable is presently uncalibrated.

## Israelite rear separation check

The model represents only the last Israelite group's trajectory, using the
locked 0.60 m/s mixed speed and 05:30 exit.  Several central runs allow at least
one mobile chariot to close the gap to that rear before soil failure.  Patchy
central comes closest without preventing all contact in every realization.
Therefore the physical separator/pursuit-distance problem remains unresolved;
Stage 0.99 cannot claim that chariots fail before reaching the Israelite rear.

## Classification

| Question | Result |
|---|---|
| Can firm ancient-style chariots enter the frozen route? | Yes |
| Can initially trafficable but remoulding wet sand create later mobility failure? | Yes, as a sensitivity family |
| Can failure occur before archived return? | Yes |
| Can dense traffic produce large queues? | Yes |
| Is trapping robust to turnability? | No; highly sensitive |
| Do crashes/trampling alone explain the force's destruction? | Not demonstrated |
| Does any tested case satisfy no far-shore or origin escape? | No |
| Is the complete Exodus 14 event chain physically reproduced? | Not yet |

Overall verdict: **conditional mobility-ordering success; full-event failure**.

## Legal next experiment

Do not change Stage 0.98 water, terrain, wind, tide, or Israelite clocks.  The
next useful test is a narrow retreat-maneuver bound, not a casualty simulation:

1. bound the space required for a two-horse team to turn or unhitch on 30/45/60
   m wet ridges while other teams occupy the same surface;
2. replace the hand-set 20/55/90% turn fractions with geometry-derived upper and
   lower bounds;
3. rerun the same 600-vehicle ledger;
4. stop if more than a small fraction can still return or reach the far shore;
5. only if a robust trapped state exists should collision/trampling and later
   progressive inundation be examined as fatality mechanisms.

Stage 0.99 source code and machine-readable outputs:

- `stage099_chariot_soil_pursuit.py`
- `outputs_stage099_chariot_soil/chariot_soil_screen.csv`
- `outputs_stage099_chariot_soil/frozen_inputs.json`
- `outputs_stage099_chariot_soil/parameter_manifest.json`

