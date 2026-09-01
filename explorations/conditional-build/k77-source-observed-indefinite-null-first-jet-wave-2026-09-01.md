---
title: "K77 source-observed indefinite-null first-jet bridge classification wave"
status: active_research
doc_type: reverse_scaffold_source_observed_indefinite_null_first_jet_bridge_result
date: 2026-09-01
claim_ceiling: exact highest-jet classification for one real observed field, a Lorentzian 1+1 base, a real two-dimensional source carrier with a fixed nondegenerate symmetric form, C2 local first-jet substitutions, and off-shell comparison to a first-order target modulo first-jet boundary terms; no full-carrier, complete bridge-existence, gauge-reduced, analytic-domain or physical equivalence theorem
manifest: lab/process/k77-source-observed-indefinite-null-first-jet-wave.json
probe: tests/channel-swings/k77_source_observed_indefinite_null_first_jet_probe.py
---

# K77 source-observed indefinite-null first-jet bridge classification wave

> **GU-COMPARATOR-ROUTING — scope before inference.** This artifact contains or
> borders a conventional particle-physics comparator. Any result about a
> standard Higgs/VEV, ordinary family index or net chirality, SO(10) `126`
> Majorana mechanism, anomaly selector, VEV-only breaking or familiar vector-
> mass route binds only that named model. It is not evidence for or against
> Weinstein's source-native mechanism without an explicit typed bridge. Read
> `lab/methods/source-native-comparator-routing.md` and follow its source-native
> pointers before reusing this result.

Classification: `BRIDGE_OR_SEMANTIC_BOUNDARY`

```gu-typed-objects
result: exact Lorentzian 1+1 highest-jet classification; nonzero velocity dependence survives the quadratic obstruction exactly when its derivative image is totally null
carrier: one real observed scalar q and a repository-owned real two-component source field T on a Lorentzian 1+1 base LAYER=conditional CHIRALITY=N/A
pairing: base symbol eta=diag(1,-1) and fixed source-carrier form H, with the indefinite witness H=diag(1,-1) and the positive control H=I2
real_structure: real C2 local first-jet substitutions T=Phi(q,v0,v1), symmetric second jets A_mn=A_nm, and real symmetric nondegenerate H
grading: jet order through two; the target and boundary current are first-jet objects and no gauge, BRST or BV quotient is supplied
action_owner: source owns only the I1B cubic transgression grammar; the two-component kinetic symbol, target action and bridge classification are repository-derived
target: survival of derivative dependence under off-shell equality to a first-order target modulo divergence of a first-jet current MAP-TYPE=classification
```

## Result first

The indefinite horn left open by the positive one-axis packet is real, but it
is sharply constrained. Freeze Lorentzian base coordinates `x^0,x^1`, one
observed scalar `q`, velocities `v_mu=partial_mu q`, and a `C2` local map

```text
T=Phi(q,v_0,v_1) in R^2.                              (1)
```

Let `H` be the fixed nondegenerate symmetric form on the source carrier and
write

```text
w_0=partial Phi/partial v_0,   w_1=partial Phi/partial v_1,
<u,z>_H=u^T H z.                                      (2)
```

For the symmetric second jet

```text
A_00=r,   A_01=A_10=s,   A_11=t,                     (3)
```

the highest-jet pieces of `partial_mu T` are

```text
U_0=w_0 r+w_1 s,       U_1=w_0 s+w_1 t.              (4)
```

The quadratic highest-jet part of the pulled source kinetic density is

```text
Q_2(r,s,t)=(1/2)(<U_0,U_0>_H-<U_1,U_1>_H)
 = (1/2)<w_0,w_0> r^2
   + <w_0,w_1> r s
   + (1/2)(<w_1,w_1>-<w_0,w_0>) s^2
   - <w_0,w_1> s t
   - (1/2)<w_1,w_1> t^2.                             (5)
```

A first-order target has no second jets. For any first-jet current
`B^mu(q,v_0,v_1)`, its divergence

```text
D_mu B^mu=B^mu_q v_mu+B^mu_(v_alpha) A_(mu alpha)    (6)
```

is only linear in `r,s,t`. It cannot cancel (5). Because `r,s,t` are
independent off shell, the coefficients of `r^2`, `t^2`, and `rs` give the
exact equivalence

```text
Q_2 identically zero
iff <w_0,w_0>_H=<w_0,w_1>_H=<w_1,w_1>_H=0
iff im(D_v Phi)=span{w_0,w_1} is totally H-null.      (7)
```

Thus, pointwise in the first-jet variables, nonzero velocity dependence
survives the **quadratic highest-jet test** if and only if its complete
velocity-derivative image is totally null. This is
not yet an existence theorem for the full bridge: lower, linear second-jet
terms, the potential, and all first-order target coefficients must still
match.

## Nonzero null witness and controls

Take the source-carrier form `H=diag(1,-1)`, the null vector `n=(1,1)` and the
opposite null vector `m=(1,-1)`. The explicit map

```text
Phi(q,v_0,v_1)=m q+n (v_0+2v_1)                     (8)
```

has `w_0=n` and `w_1=2n`. Its velocity derivative is nonzero and has rank one,
but every pair in its image has zero `H` pairing. Hence (5) vanishes for every
symmetric second jet. Its total differential has rank two because `m,n` are
independent, so the witness is not a rank-one parametrization of the source
carrier. Linear second-jet terms survive through the `m`--`n` cross pairing;
the witness passes only the quadratic obstruction, exactly as claimed.

Two controls prevent weaker readings:

- With the same `w_0=n,w_1=2n` but positive-definite `H=I_2`, the `r^2`
  coefficient is `1`, so the derivative dependence is detected and excluded.
- With indefinite `H=diag(1,-1)`, choose `w_0=(1,1)` and `w_1=(1,-1)`.
  Each column is individually null, but `<w_0,w_1>_H=2`; the `rs` and `st`
  cross terms survive. Individual nullity is insufficient.

Pointwise, in signature `(1,1)`, a totally null subspace has dimension at most
one. Consequently all nonzero velocity columns must lie on the same null line:
the two velocity slots may carry different scalar coefficients, but they
cannot occupy the two opposite null lines. This is the complete multi-velocity
cross-term classification for the frozen carrier.

## Relation to the positive one-axis result

The predecessor's scalar positive coefficient has no nonzero null vector, so
its condition `h(Phi) Phi_v^2=0` forces `Phi_v=0`. The present result replaces
that positivity inference with its exact indefinite statement: the
velocity-derivative image need not vanish, but its entire Gram matrix must.
For positive-definite `H`, total nullity again implies `D_v Phi=0`, recovering
the prior rigidity even on the two-axis base.

Indefiniteness of the **base symbol alone** does not produce the escape. The
`r^2` and `t^2` coefficients separately test the two velocity columns. The
escape requires null directions in the source-carrier kinetic form (or some
other assumption change outside this packet).

## Hostile review and claim ceiling

The strongest overclaim would say that a totally null derivative image gives
an actual K77 source-to-observed bridge. It only removes the quadratic
highest-jet obstruction in this repository-owned model. Linear acceleration
terms may fail the boundary-current integrability conditions, potentials and
lower-order terms may fail, and regularity can fail.

For a concrete lower-order counterexample, keep the null derivative image but
add source potential `P=1` against a zero target. At `v=A=0`, every divergence
of a first-jet current vanishes while the constant mismatch remains. Total
nullity is therefore not sufficient for full variational equivalence.

The source owns the I1B cubic transgression grammar, not the `R^2` carrier,
`H`, the target Lagrangian, or map (1). No source-owned rank-1920 principal
symbol or source-to-observed map is inferred. No complete K77 carrier,
connection, gauge complex, constraint/BV quotient, Green form, boundary
condition, closed operator domain, positive physical pairing, or physical
observable is constructed. Singular, higher-jet, nonlocal, auxiliary-field,
on-shell and gauge-reduced equivalences remain outside the off-shell
classification.

Accordingly the packet earns no source-action, full-carrier bridge,
physical-state, prediction, confirmation, held-out or GU-verdict credit.

## Next condition

Obtain an independently source/action-owned full-carrier principal symbol,
gauge complex and analytic domain. Then compute the Gram form of the complete
velocity-derivative image after the gauge and domain restrictions, followed by
the linear highest-jet/boundary-current integrability equations. A proposed
null escape must name its actual source-carrier null subbundle and prove it is
preserved by the relevant connection and quotient; the rank-one witness above
is a control, not that construction.

Reproduce with:

```bash
python3 tests/channel-swings/k77_source_observed_indefinite_null_first_jet_probe.py
python3 tests/channel-swings/k77_source_observed_indefinite_null_first_jet_probe.py --selftest
```
