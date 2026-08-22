---
title: "Selected-K77 CBRS-1G whole-grade first-jet frontier"
status: active_research
doc_type: exact_class_obstruction
created: "2026-08-21"
registry: lab/process/selected-k77-cbrs1g-whole-grade-frontier.json
probe: tests/channel-swings/selected_k77_cbrs1g_whole_grade_frontier_probe.py
grade: "EXACT ALL-GRADE FIRST-JET METRIC OBSTRUCTION; NOT A FULL ALL-GRADE HESSIAN-RANK OR SECOND-JET THEOREM"
target_claim: NONE-NOT-A-KILL
source_return: SOURCE_CONFIRMS_TWO_CONNECTION_MOVING_SHIAB_PRIMITIVE_EPSILON_AND_METX_GRAMMAR__REPO_DERIVES_THE_WHOLE_GRADE_FIRST_JET_SELECTION_AND_METRIC_OBSTRUCTION__SOURCE_SILENT_ON_THE_CLASS
canon_verdict_change: none
---

# Selected-K77 CBRS-1G whole-grade first-jet frontier

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
result: CBRS-1G whole-grade first-jet selection and intrinsic metric obstruction
carrier: Omega1_base_tensor{Spin_grade2_connection plus real_u6464_T_all_Clifford_grades} at the K77 anisotropic point LAYER=ambient CHIRALITY=N/A
pairing: K77 Clifford scalar-density pairing ON=Omega1_Cl77
real_structure: real B-skew Clifford grades plus i-times-B-self Clifford grades inside the u(64,64) comparator
grading: exterior form degree and complete Clifford grade 0 through 14
action_owner: repository-construction
target: all-grade first-jet field kernel primitive-epsilon restriction and intrinsic metric covector MAP-TYPE=evaluation
```

## Result first

At the frozen coefficient-anisotropic point

```text
(a,b)=(-13/96,1/48),
```

the exact first-jet Hessian obeys two whole-grade selection rules:

```text
H(T_p,T_q) = 0  for p != q,
H(B_2,T_q) = 0  for q != 2.
```

The first rule was checked on the complete `14*2^14=229,376` real-form `T`
carrier through all 500 orbits of the exact residual signed-permutation
symmetry.  The second was checked through all 21 orbits covering the 1,274
Spin-grade-two connection directions.  Every evaluated Hessian entry is real
on the declared real-form basis.  This both explains CBRS-1F's cross-grade
zeros and replaces serial grade guessing with an exact support graph.

CBRS-1E already proves that the complete `B2+T2` block has rank 2,548 and
nullity zero.  Therefore every kernel of the complete all-grade first-jet
Hessian has zero `B2` and `T2` components.  Any remaining field kernel lives
entirely in isolated `T_q` blocks with `q != 2`.

That fact decides the metric gate without computing the rank of every large
grade block.  The fixed-`varpi` Levi-Civita graph lands in the Spin-grade-two
connection channel.  Since no surviving first-jet kernel has a grade-two
momentum response, its graph-adjoint return is zero.  The inherited action
density remains `221/55296`, with normalized intrinsic metric row

```text
(-221/27648,0,0,0,221/27648,0,0,221/27648,0,221/27648).
```

It is nonzero.  Thus the complete all-grade first-jet carrier is killed at
intrinsic metric stationarity before a full all-grade rank, stabilizer, or
spectrum is needed.

## Complete small-block census and the hostile survivor

The exact certificate also closes the five smallest untouched complete `T`
blocks:

| grade | real-form dimension | rank | nullity | nonzero entries |
| ---: | ---: | ---: | ---: | ---: |
| 0 | 14 | 14 | 0 | 14 |
| 1 | 196 | 183 | 13 | 560 |
| 12 | 1,274 | 1,274 | 0 | 5,642 |
| 13 | 196 | 196 | 0 | 560 |
| 14 | 14 | 14 | 0 | 14 |

Grade one supplies the essential hostile control against an overstrong field-
rigidity claim.  Its complete kernel is exactly

```text
span { e^0 tensor gamma_j + eta_j e^j tensor gamma_0 : j=1,...,13 }.
```

This 13-dimensional space is not the pointwise Spin orbit.  The latter has
rank 91, the grade-one Hessian is injective on it, and its intersection with
the kernel is zero.  Calling the survivor a gauge orbit fails both dimension
and exact Hessian tests.

The field survivor does not rescue the branch.  The `T/T` grade theorem and
the `B2/T2`-only connection rule force its grade-two momentum response to
zero.  The moving-Shiab base return is also zero on all 91 Spin generators, so
the primitive-epsilon return vanishes.  The same zero momentum makes the
fixed-`varpi` metric graph return vanish, leaving the nonzero density trace.

## Source fence and hostile return

The released source supplies the two-connection action, moving Shiab,
primitive-epsilon, and intrinsic `MET(X)` grammar.  It does not supply the
anisotropic point, the residual-symmetry quotient, these selection rules, the
grade-one kernel, or the all-grade first-jet obstruction.  The older exact
all-grade parent census was found before execution, but it binds the distinct
Spin-invariant scalar branch `T=-(1/312)Phi1`; its rank data were not imported.

- **Strongest overclaim:** the result does not give ranks for grades 4 through
  11 and is not a full all-grade Hessian-rank theorem.
- **Strongest contrary construction:** another isolated grade may carry a
  field kernel; the theorem allows it and shows only that it cannot reach the
  grade-two Levi-Civita graph at first-jet order.
- **Strongest mistyping:** the 13-dimensional grade-one kernel is not the
  91-dimensional pointwise Spin orbit.
- **Weakest reproducibility seam:** the exact grade-12 rank dominates replay
  time; a numerical rank is not substituted.

The obstruction is first-jet only.  A second jet can differentiate the field
momentum and may create a grade-two graph return even though every first-jet
kernel is graph-invisible.  The next gate is `CBRS-1H`: construct the smallest
complete second-jet carrier capable of a nonzero grade-two momentum derivative
and solve the field, primitive-epsilon, and intrinsic metric equations
together.  No stabilizer, `mu6`, `J`/Higgs, photon, extra-`U(1)`, or
gravitational spectrum is admissible before that gate.

No ledger verdict, source ownership, canon, residue, quotient datum, particle
assignment, prediction, confirmation, or public posture changes.

Reproduce with:

```bash
sage -python \
  tests/channel-swings/selected_k77_cbrs1g_whole_grade_frontier_probe.py
```

The exact probe passes `47/47`.
