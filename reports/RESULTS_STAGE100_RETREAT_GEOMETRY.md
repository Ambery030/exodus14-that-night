# Stage 1.00 — Geometry-Derived Retreat and Crew-Abandonment Bound

## Verdict

Replacing the hand-set 20/55/90% chariot turn fractions with explicit geometric
bounds weakens the current destruction hypothesis.

Under the locked central formation—12 columns occupying 36 m across three
nominally firm 60/45/30 m backbones—the formation leaves substantial lateral
space.  If most of those declared firm widths remain usable, 4–13 simultaneous
turn pockets fit under the tested 10/15/20 m swept-width envelopes.  That is
enough capacity for almost every still-mobile chariot to turn and return before
the frozen 06:40 closure.

More importantly, immobilizing a chariot does not immobilize its two crewmen.
From the first Stage 0.99 failure at 1 km, even a 0.5 m/s pedestrian can return
to the origin before the first 05:40 rewet cue if retreat begins at 04:15.  If
the crew waits until 05:40, the same pedestrian can still cover 1.8 km before
06:40 closure.  The present slow progressive-return world therefore traps
vehicles much more readily than people.

This does not disprove every Ballah-like mechanism.  It does show that the
current Stage 0.98–0.99 family has **not** physically explained the Exodus
14:28 no-remnant outcome.  Vehicle immobilization, queueing, and progressive
rewetting cannot be promoted into personnel destruction without another
independently demonstrated constraint.

## Frozen inputs

Stage 1.00 reads the Stage 0.99 result table without rerunning or editing soil,
hydrodynamics, wind, tide, route, or population clocks.

- Input: `outputs_stage099_chariot_soil/chariot_soil_screen.csv`
- SHA-256: `05ecb2af255b86bd5db2a70b1c8f816673394b6a4389deadb6c2f62eed8f6031`
- Chariots: 600
- Central columns: 5 + 4 + 3 = 12
- Central dynamic envelope: 3 m per column
- Nominal firm backbones: 60 + 45 + 30 = 135 m
- Central recognition: 04:15
- First archived rewet cue: 05:40
- Final tested-segment closure: 06:40
- First Stage 0.99 failure: 1 km from the origin

The central formation uses only 36/135, about 27%, of the declared aggregate
firm width.  Calling that formation “dense” is accurate longitudinally but not
laterally across the entire nominal backbone system.  This is an important
correction to the Stage 0.99 interpretation.

## External evidence boundary

The Tutankhamun archive and experimental reconstructions support a light,
two-wheeled, two-horse, maneuverable vehicle.  NOVA's Egyptian replica was put
through tight-turn maneuverability tests and described as agile.  No reliable
published numerical Egyptian U-turn radius or wet-sand turn time was recovered.

Accordingly, Stage 1.00 tests geometric envelopes rather than claiming an
ancient measurement:

- swept turn width: 10, 15, or 20 m;
- turn service time: 30, 45, or 60 s;
- usable firm width: 50%, 75%, or 100% of the locked backbone width;
- immediate shoulder-only turning versus use of the full backbone after the
  formation halts.

Sources: [NOVA experimental reconstruction](https://www.pbs.org/video/nova-building-pharaohs-chariot-pro/),
[Tutankhamun Archive](https://www.griffith.ox.ac.uk/gri/4tutchar.html),
[National AgrAbility horse-drawn vehicle guidance](https://www.agrability.org/wp-content/uploads/2015/11/ps25.pdf).

These sources support maneuverability qualitatively.  They do not calibrate any
Stage 1.00 numeric turn envelope.

## Vehicle-turn results

`Mobile candidates` exclude vehicles already at the far shore and vehicles
actually immobilized in Stage 0.99.

### Marginal wet sand

- Already at far shore: 87
- Actually immobilized: 10
- Mobile retreat candidates: 503

| Turning surface | Usable firm width | Turn pockets across sweep cases | Vehicles able to return | Vehicles left trapped |
|---|---:|---:|---:|---:|
| Shoulder only | 100% | 4–9 | 503 | 10 |
| Shoulder only | 75% | 2–6 | 264–503 | 10–249 |
| Shoulder only | 50% | 0–2 | 0–503 | 10–513 |
| Full width after halt | 100% | 6–13 | 503 | 10 |
| Full width after halt | 75% | 4–9 | 503 | 10 |
| Full width after halt | 50% | 2–6 | 264–503 | 10–249 |

### Patchy sand over soft material

- Already at far shore: 8
- Actually immobilized: 18
- Mobile retreat candidates: 574

| Turning surface | Usable firm width | Turn pockets across sweep cases | Vehicles able to return | Vehicles left trapped |
|---|---:|---:|---:|---:|
| Shoulder only | 100% | 4–9 | 528–574 | 18–64 |
| Shoulder only | 75% | 2–6 | 264–574 | 18–328 |
| Shoulder only | 50% | 0–2 | 0–530 | 62–592 |
| Full width after halt | 100% | 6–13 | 574 | 18 |
| Full width after halt | 75% | 4–9 | 528–574 | 18–64 |
| Full width after halt | 50% | 2–6 | 264–574 | 18–328 |

The family therefore has no robust vehicle-entrapment result.  It traps almost
all mobile vehicles only when the majority of nominal firm width is made
unavailable for turning.  That cannot be asserted while the upstream model
continues to describe 60/45/30 m firm backbones.

Every case also inherits far-shore escape from Stage 0.99: 87 marginal or 8
patchy chariots.  Consequently no Stage 1.00 row passes the strict no-far-shore
escape gate.

## Crew abandonment bound

The table asks only how far a dismounted crew member could travel toward the
origin before the archived clocks.  It does not assume that every crew member
would choose correctly, remain uninjured, or encounter no crowd obstruction.

### If crew dismount at 04:15 recognition

| Foot speed | Distance before 05:40 rewet | Distance before 06:40 closure | First 1 km failure can clear before rewet? |
|---:|---:|---:|---|
| 0.5 m/s | 2.55 km | 4.35 km | Yes |
| 0.8 m/s | 4.08 km | 6.96 km | Yes |
| 1.0 m/s | 5.10 km | 8.70 km | Yes |
| 1.3 m/s | 6.63 km | 11.31 km | Yes |

### If crew wait until the first 05:40 rewet cue

| Foot speed | Distance before 06:40 closure | First 1 km failure can clear? |
|---:|---:|---|
| 0.5 m/s | 1.80 km | Yes |
| 0.8 m/s | 2.88 km | Yes |
| 1.0 m/s | 3.60 km | Yes |
| 1.3 m/s | 4.68 km | Yes |

Thus the current first-failure location and water clock provide a large human
escape margin.  Horse entanglement, collision, confusion, darkness, command
delay, and crowding can reduce that margin, but Stage 0.99 produced only two
sudden-stop conflict exposures in its most compressed case.  Those mechanisms
cannot currently close the gap without unsupported assumptions.

## A remaining model caveat

Stage 1.00 uses the final 06:40 all-segment closure as a permissive return-path
bound.  Stage 0.98 did not archive a resolution-independent, directional
chariot-return graph for every link.  A specific backward route might disappear
earlier than the final aggregate closure.

That uncertainty can reduce vehicle retreat.  It is much less able to eliminate
pedestrian escape because Israelites themselves still use the travelling human
network into the dawn interval.  Nevertheless, directional link connectivity
must be extracted before claiming exact survivor numbers.

## Hard interpretation

| Gate | Result |
|---|---|
| Prior water/soil/traffic results preserved | Pass |
| Hand-set turn fractions removed | Pass |
| Firm widths allow substantial maneuver space | Yes |
| Robust whole-detachment vehicle trap | Fail |
| Robust personnel trap after vehicle failure | Fail |
| Collision/trampling fatality mechanism | Not demonstrated |
| Exodus 14:25 ordering | Conditionally compatible |
| Exodus 14:28 no-remnant outcome | Physically unexplained |

Current verdict:

> **The tested world can open a route and can degrade Egyptian chariot mobility,
> but its slow return and broad declared firm ridges leave too much opportunity
> for vehicle retreat or crew abandonment.**

## Stop/review decision

The project should pause before adding another fatality mechanism.  The useful
review questions are now narrow:

1. Did Stage 0.98 overstate firm chariot-usable width by treating nominal sandy
   backbones as uniformly maneuverable?
2. Can archived spatial fields prove that the backward pedestrian/chariot path
   is cut substantially earlier than 06:40?
3. Can any independently supported mechanism delay recognition until escape
   distance becomes short, while retaining Exodus 14:25's decision-to-flee
   before the main return?
4. If none can, the opening mechanism may remain physically plausible while the
   complete pursuit/destruction mechanism fails in this model family.

Machine-readable outputs:

- `stage100_retreat_geometry.py`
- `outputs_stage100_retreat_geometry/vehicle_turn_bounds.csv`
- `outputs_stage100_retreat_geometry/crew_abandonment_bounds.csv`
- `outputs_stage100_retreat_geometry/frozen_stage099_manifest.json`

