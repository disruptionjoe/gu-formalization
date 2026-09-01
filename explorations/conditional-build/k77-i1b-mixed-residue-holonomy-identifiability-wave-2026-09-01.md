---
title: "K77 I1B mixed-residue holonomy identifiability wave"
status: active_research
doc_type: reverse_scaffold_i1b_cross_null_mixed_residue_identifiability_result
date: 2026-09-01
claim_ceiling: exact two-dimensional classification of the trace-free cross-null connection residue and its mixed-curvature coupling to a tangential symplectic coefficient; the forced trace residue and bounded mixed curvature do not select the coefficient, while an independently owned noncommuting trace-free residue plus mixed row can; no source-owned matching datum, physical cross-null bundle, prediction, confirmation, or verdict
manifest: lab/process/k77-i1b-mixed-residue-holonomy-identifiability-wave.json
probe: tests/channel-swings/k77_i1b_mixed_residue_holonomy_identifiability_probe.py
---

# K77 I1B mixed-residue holonomy identifiability wave

> **GU-COMPARATOR-ROUTING — scope before inference.** This artifact contains or
> borders a conventional particle-physics comparator. Any result about a
> standard Higgs/VEV, ordinary family index or net chirality, SO(10) `126`
> Majorana mechanism, anomaly selector, VEV-only breaking or familiar vector-
> mass route binds only that named model. It is not evidence for or against
> Weinstein's source-native mechanism without an explicit typed bridge. Read
> `lab/methods/source-native-comparator-routing.md` and follow its source-native
> pointers before reusing this result.

Classification: `INTERNAL_STRUCTURAL_ONLY`

```gu-typed-objects
result: complete trace-free residue and mixed-curvature identifiability classification on the degenerating I1B Darboux plane
carrier: real degenerating rank-two Darboux block inside the native rank-24 to rank-22 I1B Green quotient jump LAYER=conditional CHIRALITY=N/A
pairing: J_u=uJ_2 with punctured-stratum compatible connection residue ON=native_rank_changing_normal_form
real_structure: real two-dimensional symplectic matrices and real tangential coefficient
grading: scalar forced residue plus trace-free sp(2,R) residue; not a BV-BFV grading
action_owner: native rank jump is source-adjacent I1B data; residue classification and matching equation are repository-derived, with no source-owned trace-free residue supplied
target: mixed normal-tangential curvature residue and holonomy-coefficient identifiability MAP-TYPE=classification
```

## The entire compatible residue family

The predecessor fixed the native normal form

```text
J_u=uJ_2,       J_2=[[0,1],[-1,0]],                  (1)
```

on the degenerating two-plane and proved that every compatible ordinary
connection has trace `-1/u`. Write its residue as

```text
u B_u = R = -(1/2)I_2+C,
C=[[p,q],[r,-p]].                                    (2)
```

Every real trace-free `C` lies in `sp(2,R)`, so

```text
C^T J_2+J_2 C=0.
```

Substitution into the compatibility equation shows that **every** matrix in
(2) is compatible. The forced source-adjacent datum is only `tr R=-1`; the
three real coordinates `(p,q,r)` remain free. The symmetric residue
`-I_2/2` is the single point `p=q=r=0`, not a universal full-matrix answer.

## The only mixed coupling seam

Let the tangential connection on this block be

```text
A_y=aH,       H=diag(1,-1),                          (3)
```

where the predecessor compares `a=log(2)` and `a=log(3)`. For constant
residues and tangential coefficients, the singular part of the mixed
curvature is

```text
res(u F_uy)=[R,aH]=a[C,H]
            =a [[0,-2q],[2r,0]].                    (4)
```

The scalar forced residue commutes with `H` and contributes nothing. The
diagonal trace-free coordinate `p` also commutes. Only the off-diagonal
trace-free residue `(q,r)` can couple normal singular reduction to tangential
holonomy.

Equation (4) sharpens the selector requirement.

1. Requiring bounded mixed curvature sets the residue in (4) to zero. For
   nonzero `a`, this forces `q=r=0` but leaves the magnitude of `a` arbitrary.
   Both `log(2)` and `log(3)` survive.
2. Prescribing a nonzero mixed residue
   `M=[[0,rho],[sigma,0]]` still does not select `a` when `C` is unowned. For
   every nonzero `a`, choose

   ```text
   q=-rho/(2a),       r=sigma/(2a),                  (5)
   ```

   with arbitrary `p`.
3. If a source/action independently owns `C` and `M`, then (4) can select the
   coefficient exactly when the nonzero rows agree:

   ```text
   a=-rho/(2q)=sigma/(2r).                            (6)
   ```

   Inconsistent ratios falsify that owned matching packet.

This is necessary and sufficient in the stated two-dimensional normal form.
It replaces the broad request for a “coupled Hessian” with the exact missing
datum: a noncommuting trace-free residue and its mixed-curvature row, both
owned independently of the coefficient being tested.

## Decision effect and fences

The forced trace residue has zero decision power over `a`. Boundedness of
mixed curvature has zero decision power over its magnitude. Even a nonzero
mixed row has zero decision power while the trace-free residue can be tuned as
in (5). Selection becomes possible only after the off-diagonal residue is
fixed independently.

The source-native fixed-stratum coupled I1B Hessian does not presently supply
that cross-null residue/mixed row. This packet does not infer one from its
local blocks and does not promote the repository normal form into a physical
cross-null bundle. The exact probe checks the full residue family, mixed
commutator, boundedness horn, constructive nonidentifiability and owned-data
selection condition; hostile mutations target the full-matrix overclaim and
false coefficient inference.

## Next condition

Advance the I1B selector only with a source/action-owned cross-null evaluation
that fixes at least one off-diagonal trace-free residue coordinate and the
corresponding mixed-curvature or matching row. Then equation (6) distinguishes
`log(2)` from `log(3)` or rejects both. Requiring only Green compatibility,
trace residue `-1`, the symmetric representative, determinant matching or
bounded mixed curvature cannot do so.
