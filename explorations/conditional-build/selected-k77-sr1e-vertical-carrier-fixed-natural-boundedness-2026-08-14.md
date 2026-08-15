---
title: "Selected-K77 SR-1E vertical carrier and fixed-natural boundedness"
status: active_research
doc_type: exact_interface_construction_and_action_obstruction
created: "2026-08-14"
registry: lab/process/selected-k77-sr1e-vertical-carrier-fixed-natural-boundedness.json
probe: tests/channel-swings/selected_k77_sr1e_vertical_carrier_fixed_natural_boundedness_probe.py
grade: "EXACT OBSERVATION-RELATIVE CARRIER MAP AND FIXED-NATURAL RELEASED-BOSONIC-ACTION BOUNDEDNESS OBSTRUCTION"
canon_verdict_change: none
---

# Selected-K77 SR-1E vertical carrier and fixed-natural boundedness

## Result first

The first SR-1E interface object exists. The observation splitting

```text
R^(7,7) = R^(1,3) + R^(6,4)
```

gives a canonical rank-`450` inclusion

```text
V10* tensor so(6,4)  -->  V14* tensor so(7,7),
```

whose image is exactly the vertical block

```text
N* tensor Lambda^2(N) subset V14* tensor Lambda^2(V14).
```

The exact probe checks all `45 x 450 = 20,250` infinitesimal intertwiner
identities. The map is fully `so(6,4)`-equivariant and injective. A planted
horizontal/normal boost exits the image, so this is an observation-relative
block map, not a false full-`so(7,7)` subrepresentation claim.

The map does not rescue the source instability. It transfers its boundedness
problem into the selected K77 action and strengthens it.

## Exact quartic obstruction

Two explicit rays in the embedded vertical carrier use the same noncommuting
compact algebra pair, once on a positive vertical two-plane and once on a
mixed-sign vertical two-plane. Their raw DeWitt/Killing quartics are

```text
K_raw = -4, +4.
```

After the selected `comm/symi/symi` Shiab, each leading residual has exactly
one `Lambda^13 Cl1` cell. The actual fixed-natural trace/Hodge I2B quartics
are

```text
K_I2B = -16, +16.
```

The fixed-natural source owner is already classified as

```text
Q_B = c Q_trace/Hodge,       c != 0.
```

For `c>0`, the first embedded ray has leading action coefficient `-8c`. For
`c<0`, the second has leading coefficient `8c<0`. Changing the normalization
only exchanges which ray runs away. Setting `c=0` is inadmissible because it
deletes the residual-square action and destroys the primalizer.

The eddy-completed first action cannot repair this. Along a constant-amplitude
ray it has degree at most three:

```text
<T,S(F_B)>                    degree 1,
<T,S(D_B T/2)> and kappa T^2 degree 2,
<T,S(T^2/3)>                 degree 3.
```

On the two displayed `Cl2` rays the cubic term actually vanishes separately
by Clifford parity. In any event, no linear, quadratic or cubic contribution
can bound a negative quartic at large amplitude. Background curvature and the
mass term change only subleading coefficients.

Therefore the released fixed-natural `I1B + I2B` bosonic action is unbounded
below on the embedded source carrier for every admissible nonzero fixed-natural
normalization.

## What this decides

The earlier SR-1E ownership gate named six missing objects. This swing:

- **builds** the exact `450 -> 1274` carrier interface, conditional only on the
  already-used observation horizontal/vertical splitting;
- **preserves** the exact source negative-ray witness inside selected K77;
- **kills** a fixed-natural I2B rescaling as the full-action boundedness repair;
  and
- **proves** that the eddy first action is too low in amplitude degree to
  stabilize the runaway.

It does not select a negative orbit, construct a nonzero critical amplitude,
lift a canonical `B_Z` first jet, or recompute the source Euler rows.

## Reverse-scaffold consequence

The next gate is `SR-1F`. A viable repair must change structure, not scale:

1. an action-owned moving fundamental symmetry or field-dependent `Q_B` that
   turns the residual quadratic form positive on the admitted nonlinear
   carrier;
2. a source-derived constraint/BV tangent that excludes every negative
   quartic direction while remaining dynamically closed; or
3. a new source-owned higher-even action term whose leading coefficient is
   positive on the full admitted carrier.

Each route has a sharp kill. A moving fundamental symmetry must be covariant
and included in the action, not chosen after seeing the ray. A constraint must
be source- or BV-owned and preserved by evolution, not a fitted tangent. A
higher term must be present with a fixed sign and dominate both exact rays.

Only after one repair passes should the lane select a nonlinear critical orbit,
solve its exact amplitude, lift a labelled canonical first jet and recompute
translation, Bianchi, primitive epsilon and total fixed-`varpi` metric rows.

`SR-1` remains `BACKGROUND-MISSING`; `VRS-6` remains blocked. No ledger,
canon, residue, quotient datum or public posture changes. No vacuum, physical
cohomology, superposition law, Born rule, spectrum or empirical prediction
follows.

Reproduce with:

```bash
sage -python \
  tests/channel-swings/selected_k77_sr1e_vertical_carrier_fixed_natural_boundedness_probe.py
```

The exact probe passes `40/40`.
