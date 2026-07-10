---
title: "Source-Action Buildbench Packet"
status: exploration
doc_type: packet
date: "2026-07-10"
---

# Source-Action Buildbench Packet

## Scope

This is the first hourly-progress swing from `NEXT-STEPS.md`:

1. make source-action candidates comparable;
2. force each candidate to state its declaration triple;
3. collect hard guards, computable loss channels, and named missing carriers;
4. stop before the anchor-scale A-door computation.

This packet does not build `S_IG`, does not change the generation-count verdict, and does not promote any
source-action claim.

## Built Artifact

Executable buildbench:

- `lib/source_action_buildbench.py`
- `tests/test_source_action_buildbench.py`

Run:

```text
python tests/test_source_action_buildbench.py
```

## Current Rows

| Candidate | Effective declaration | Phase | Buildbench verdict | Next action |
|---|---|---|---|---|
| `sg4-minimal-bv-kt-finite-fiber-closure` | full vector-spinor | source Noether/tau | missing-carrier blocked | derive the projected BV/KT gauge differential from a source-level Noether/tau carrier |
| `non-equivariant-compensator-bv-closure` | full vector-spinor | BV closure | missing-carrier blocked | supply non-equivariant anti-trap compensator plus full BV/Koszul-Tate closure |
| `boundary-spectral-section-bridge` | boundary-external | boundary bridge | boundary-index wall | do not read the present symbol as APS index; build the BV-to-boundary-Dirac bridge |
| `available-loss-only-security-budget` | selector-not-action | downstream selector | downstream premature | use only as a selector over declared candidates; it is not itself `S_IG` |

## Computed Guards

Every declared/default row keeps:

- `L_target_import = 0`;
- `L_acausal_trap = 0`;
- `L_boundary_symbol = 0`;
- `L_boundary_index = 1`.

The boundary-index loss remains a computed wall: the present boundary operator carries `C2` as a
Hilbert-Schmidt symbol norm while eta is forced to zero. It is not a generation-count or APS-index carrier.

Every serious candidate still reports the named missing carriers:

- `L_anomaly`;
- `L_RS_BRST`;
- `L_theta_source`;
- `L_weak_field`;
- `L_families_pushforward`.

## Handoff

Update after `ANCHOR-SCALE-A-DOOR-PACKET-2026-07-10.md`: the A-door fork reached
`PARTIAL_PASS_BV_TAU_BLOCKED`, so the next reasonable hourly progress point is now:

```text
MINIMAL-BV-CLOSURE
```

That run should attempt the smallest non-equivariant, anti-trap compensator plus Koszul-Tate leg. It must not
ignore the null-direction tau caveat exposed by the anchor-scale fork.

Update after `MINIMAL-BV-KT-CLOSURE-PACKET-2026-07-10.md`: the finite-fiber BV/Koszul-Tate bicomplex closes
after projecting the scalar-spinor gauge map into `ker Gamma`, while the raw map remains second-class. The
next reasonable hourly progress point is now:

```text
SOURCE-NOETHER-TAU-CARRIER
```

That run should derive the projected differential from source-level Noether/tau data rather than treating the
projection as an input.
