---
title: "Selected K77 I2B observer inverse-adjoint correction"
status: exploration
created: 2026-08-12
run_id: RUN-20260812-181434-gu-i2b-observer-inverse-adjoint-correction
claim_status_change: none
canon_verdict_change: none
public_posture_change: none
---

# Selected K77 I2B observer inverse-adjoint correction

## Correction

V0.216's main ownership verdict survives, but one printed control was wrong.
For a noncompactly moved Hermitian form the adjoint is

```text
A sharp_u = H_u^-1 A^dagger H_u,
```

not `H_u A^dagger H_u`.  Recomputing the fixed-field rational boost with the
inverse gives exact blocks

```text
-328/9 I4, +8 I4, +8 I4, +8 I4,
```

with all mixed blocks zero.  The old v0.215/v0.216 control printed
`-8 I4,+328/9 I4,+328/9 I4,+328/9 I4`; that is the result of incorrectly
treating the boosted form as an involution.

The corrected response still differs from the adapted
`-8 I4,+8 I4,+8 I4,+8 I4`.  Therefore diagonal Spin/frame naturality remains
exact and vertical basicness after forgetting `u` remains refuted.  The
correction changes the location and sign of the firing coefficient, not the
ownership classification.

## Prior-art composition

The proposed next step “construct a minimal moving-`u`/`SO(3)` family” was
already done in RB4 on 2026-07-31:

- `u -> P_W(u)` is constructed pointwise and covariantly;
- the exact `SO(3)` stabilizer closes;
- `u -> J` is refuted because the fixed-`u` stabilizer moves every compatible
  `J` candidate.

RB5 then proves the coarse `epsilon_plane -> complete flag` map is refuted:
the stabilizer commutant is scalar, so the target flag does not descend from
that coarse orbit.  A refined `epsilon_flag` and spectral/polar calculus are
typed conditionally but remain action-unselected.  RB6 and RB7 test old W177
action-shaped routes and find nonselection/no stable selection; they do not
test the present `SC-ACT-04` observer-Hermitian action parent.

Consequently another `SO(3)` construction would be duplicate work.  The live
current-action question is whether varying `u` in the `SC-ACT-04` completion
produces a constrained Euler/Ward equation that aligns, removes or propagates
the observer.

## Layer-0 and symplectic fence

- RB4's moving associated family is not a selector of one member.
- RB5's coarse-flag obstruction is not a no-go for a refined independent flag.
- W177 nonselection is not an `SC-ACT-04` calculation.
- A corrected finite Gram is not an Euler equation, moment map, Ward identity,
  presymplectic quotient or positive analytic domain.
- Source `C^(32,32)+C^(32,32)`, derived `U(32,32)xU(32,32)`, full
  `U(64,64)` and independently varied connections remain distinct.

No datum, residue, ledger verdict, quotient, P1/P2/P3, canon or public posture
moves.

## Verification

`selected_k77_i2b_observer_inverse_adjoint_correction_probe.py` passes
`17 exact + 1 planted = 18`.  It recomputes the corrected fixed-field Gram,
rejects the old coefficient placement, replays v0.216 naturality and coarse
nonselection, and certifies the RB4--RB7 prior-art dispositions.

## Next gate

Insert the observer-Hermitian completion into the current `SC-ACT-04` selected
action and derive its constrained unit-timelike `u` Euler equation, including
the Lagrange multiplier and observation/section chain rule.  Test whether the
equation determines `u`, becomes a Ward identity after a refined flag, or
exposes a genuine external three-function cost.  Retain coupled contact as the
independent comparator.
