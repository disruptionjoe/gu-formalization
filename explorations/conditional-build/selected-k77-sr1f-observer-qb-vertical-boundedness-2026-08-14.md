---
title: "Selected-K77 SR-1F observer-Q_B vertical boundedness"
status: active_research
doc_type: exact_moving_primalizer_action_obstruction
created: "2026-08-14"
registry: lab/process/selected-k77-sr1f-observer-qb-vertical-boundedness.json
probe: tests/channel-swings/selected_k77_sr1f_observer_qb_vertical_boundedness_probe.py
grade: "EXACT OBSTRUCTION FOR THE EXISTING CONDITIONAL MOVING OBSERVER-HERMITIAN Q_u FAMILY"
canon_verdict_change: none
---

# Selected-K77 SR-1F observer-`Q_B` vertical boundedness

## Result first

The highest-conviction moving repair already present in the repository does
not stabilize the exact SR-1E vertical carrier.

The candidate is the observer-Hermitian associated family

```text
H_u = i B gamma(u),
Q_u(X,Y) = Re Tr((H_u X^dagger H_u)Y)/128,
```

for a unit timelike observer `u` in the selected Lorentz plane. Earlier exact
work established its simultaneous Spin covariance and showed that it repairs
the four-real principal response and the restricted `S_q/H_q` residual
family. That made it the strongest existing structural candidate. It is still
conditional: the source prints a `Q_B` slot but does not identify it with
`Q_u`, and `H_u` is an indefinite Hermitian form rather than a positive
Hilbert majorant.

Evaluated on the two exact SR-1E selected-Shiab residual rays, the moving
quartics are

```text
positive vertical two-plane:  +16 c(u),
mixed-sign vertical two-plane: -16 c(u),

c(u) = u0^2+u1^2+u2^2+u3^2.
```

All four observer-axis values and all six polarizations are computed exactly.
The cross coefficients vanish. For a unit timelike observer,

```text
u0^2-|v|^2 = 1
implies
c(u) = 1+2|v|^2 > 0.
```

Thus every observer leaves one positive and one negative quartic ray. The
rational boosted observer changes the magnitudes from `+16,-16` to
`+656/9,-656/9`, proving the movement is live, but it cannot change the sign
pair.

## Why field dependence does not help this family

Let the observer be chosen covariantly from the field, `u=u(T)`. On either
displayed ray the same pointwise formula holds. Since `c(u(T))` is strictly
positive wherever `u(T)` is unit timelike, field dependence only multiplies
the opposite-sign pair by a positive function. A ray-dependent choice cannot
turn both leading coefficients positive.

An overall nonzero normalization also fails: changing its sign merely
exchanges which ray is negative. The released first bosonic action remains at
most cubic in constant amplitude and cannot bound the surviving negative
quartic at infinity.

This is stronger than the fixed-natural SR-1E obstruction for one specific
reason: it tests the actual existing moving candidate rather than assuming
that movement might repair the sign. It is narrower than a universal no-go:
no theorem here classifies every imaginable field-dependent primalizer.

## Layer-0 fence

Keep distinct:

- an associated moving observer family versus an observer-free basic action;
- an involutive indefinite `H_u` versus a positive Hilbert fundamental
  symmetry;
- the conditional `Q_u` construction versus the fixed-natural source owner;
- boundedness on the admitted carrier versus stationarity of one selected
  orbit;
- a negative carrier ray versus a source/BV-owned dynamically closed tangent;
  and
- an action term printed or derived from the source versus a fitted positive
  higher-order counterterm.

The result kills the existing zero-new-field `Q_u` repair. It does not kill a
different action-derived field-dependent primalizer whose form is not in this
observer-Hermitian family.

## Reverse-scaffold consequence

Advance to `SR-1G`. The remaining live structural routes are:

1. a source/BV-owned constraint whose invariant tangent excludes every
   negative quartic direction and is preserved by the full dynamics; or
2. a source-owned higher-even action term with fixed positive leading sign on
   the full admitted carrier.

The next swing should audit ownership before doing new algebra. A constraint
must be printed or derived from the source/BV complex and dynamically closed;
an imposed slice does not count. A higher-even term must belong to the action,
not be added because the quartic failed, and must dominate both exact rays.

Only after one route passes may the lane select a nonlinear critical orbit,
solve its exact amplitude, lift a labelled canonical `B_Z` first jet, and
recompute translation, Bianchi, `j1E_T`, `j1E_B`, primitive epsilon and total
fixed-`varpi` metric rows.

`SR-1` remains `BACKGROUND-MISSING`; `VRS-6` remains blocked. No ledger,
canon, residue, quotient datum or public posture changes. No vacuum, physical
cohomology, superposition law, Born rule, spectrum or empirical prediction
follows.

Reproduce with:

```bash
sage -python \
  tests/channel-swings/selected_k77_sr1f_observer_qb_vertical_boundedness_probe.py
```

The exact probe passes `35/35`.
