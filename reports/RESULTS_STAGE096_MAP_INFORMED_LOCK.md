# Stage 0.96 — Map-informed geometry lock

Date: 2026-08-20

## Decision

New tide, water-quantity and wind sweeps must use fixed geographic axes and
`MI_EAST_RELIEF_V1`.  The legacy original/mirrored worlds are retained only as
orientation controls.

The locked structural prior is:

- x increases west to east and y increases south to north;
- true east wind transports water east to west (`180°` from +x);
- lower/wetter storage lies toward the western/lakeward side;
- the primary sandy relief and route hypotheses lie in the eastern sector;
- northern hydraulic inlet position is an independent synthetic axis;
- no whole-world east-west mirror operation is allowed.

## Evidence boundary

### Historical-map informed

- contour-bounded sandy relief east of the canal;
- low/wet ground toward the canal/lake margin;
- segmented and braided morphology permitted along northern/eastern Ballah.

### Synthetic mechanism parameters

- the current 0.30 m west-to-east background relief difference;
- exact ridge count, widths, crest elevations and saddles;
- platform positions;
- inlet position, width, sill and longitudinal profile.

### Unknown

- the LBA surface and vertical datum;
- candidate-specific LBA connectivity;
- exact ancient water volume, stage and marine exchange.

Thus “locked” means that provenance, geographic orientation and parameter
separation are correct.  It does not mean that the numerical surface is a
reconstruction of ca. 1250 BCE.

## Validation

The lock validator confirms:

- mirror disabled;
- eastern background higher than the western low;
- all declared route lanes in the eastern relief sector;
- inlet treated independently;
- true east-wind direction fixed at `180°`.

Machine-readable record:
`outputs_stage096_map_informed_lock/geometry_lock.json`.

## Next experiment boundary

With the geometry lock held fixed, reopen only:

1. initial water stage / water quantity;
2. local eastern-Mediterranean tide amplitude and phase;
3. east-wind peak, duration and physically gradual decay;
4. inlet position/control profile as a separately labelled hydraulic
   uncertainty.

The first pass remains pedestrian/mixed-population only.  Pursuers, chariots
and casualty mechanisms stay excluded until a safe crossing window exists.
