---
title: "Selected-K77 SR-1C parallel-two-jet qualification gate"
status: active_research
doc_type: construction_result
created: "2026-08-14"
registry: lab/process/selected-k77-sr1c-parallel-two-jet-qualification.json
probe: tests/channel-swings/selected_k77_sr1c_parallel_two_jet_qualification_probe.py
grade: "EXACT QUALIFICATION; PARALLEL ANSATZ UNPROVED; NO BRANCH KILL"
canon_verdict_change: none
---

# Selected-K77 SR-1C parallel-two-jet qualification gate

## Result first

The tempting parallel-two-jet shortcut does **not yet construct** the spatial
first jet of the branch momentum. The simple-root relation

\[
28392t^2+91t-351=0
\]

does force `dt=0` for a branch-preserving formal derivative. It does not force
the derivative of the field first jet, the thirteen-cell symmetric `DT`
correction, or the moving coefficient basis to vanish.

The fourteen serialized coefficients `+/- (7/2-t)` and `+/- (9/2-t)` are the
value of `p=E_B-E_T` **after** the point action equations and the correction
have been substituted. Differentiating only that restricted value and setting
`dt=0` gives zero, but this is not the differential of the unreduced local
Euler operator.

The exact local formula exposes the missing direction. If `s` denotes the
symmetric `DT` correction and `A` its rank-195 action map, then its two Euler
responses are

\[
\partial_s E_B=2A,\qquad \partial_s E_T=A,
\qquad \partial_s(E_B-E_T)=A\ne0.
\]

An exact planted column therefore has live `E_T`, `E_B`, and momentum
responses even with `dt=0`. The plant is deliberately not a prolonged
solution; it proves non-identifiability from the restricted zero-jet bank. A
parallel extension remains an admissible candidate, but it must be built and
checked rather than obtained by assigning every entry of `j1p` to zero.

Both algebraic roots remain not yet falsified. `SR-1` remains
`BACKGROUND-MISSING`; the fixed-`varpi` moving metric graph remains open.

## Layer 0 and owner

The object under test is the first covariant jet of the **selected first-action
Euler momentum** in the common K77 basis. It is not:

- the derivative of a polynomial representative in the quadratic root
  algebra alone;
- the derivative of the source-printed residual;
- the parallel-curvature property `nabla R=0` of the pure vertical DeWitt
  symmetric space; or
- total primitive-epsilon or metric stationarity.

The load-bearing fork is restriction versus differentiation. Equality of an
Euler value on the point solution locus does not identify the differential
operator transverse to that locus.

## Exact qualification

The predecessor gives the common `196`-row action map from `9,555` symmetric
`DT` variables with exact rank `195`. In the independent-`B` Euler formula the
formal-adjoint companion has coefficient one, twice the `E_T` half-companion.
Consequently a derivative of the symmetric first-jet correction enters `E_B`
with `2A` and `E_T` with `A`.

The probe selects one nonzero column exactly. The resulting planted second-jet
direction has live support in all three derived responses. Since the same
point field one-jet is retained, this is enough to reject the inference

```text
dt=0 and d(serialized p)=0  =>  j1p=0.
```

It is not enough to reject the existence of a compatible parallel extension.
The planted column changes the differentiated action row and is therefore a
firing control, not a candidate stationary jet.

## Minimum non-circular successor

A claimed parallel two-jet must serialize actual second-jet variables and
pass, on both exact roots:

1. all differentiated `196` translation-action rows;
2. all differentiated `5,096` inherited Bianchi rows;
3. the Ricci/Spencer and holonomicity identities for the nonzero-`T` field;
4. direct differentiation of the unreduced local `E_B-E_T` formula, including
   correction and moving-basis terms; and
5. the signed formal-adjoint contraction producing the `91` primitive-Spin
   components.

Only after those checks may a zero `D_B^!p` be composed with the already exact
zero moving-Shiab return. Moving Hodge, frame, density, lowerer and observation
returns remain a separate metric packet.

## Claim ceiling

This is an exact qualification of one differentiation shortcut. It does not
construct or obstruct a compatible two-jet, decide primitive epsilon, decide
the total metric row, produce an open solution germ, alter a ledger or canon
verdict, or establish superposition.
