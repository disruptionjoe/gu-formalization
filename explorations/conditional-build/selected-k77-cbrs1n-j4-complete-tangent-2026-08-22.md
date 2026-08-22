---
title: "Selected-K77 CBRS-1N J4 complete-tangent alignment gate"
status: active_research
doc_type: exact_tangent_method_obstruction
created: "2026-08-22"
registry: lab/process/selected-k77-cbrs1n-j4-complete-tangent.json
probe: tests/channel-swings/selected_k77_cbrs1n_j4_complete_tangent_probe.py
grade: "EXACT RECONSTRUCTION-GRADE 4+10 RESIDUAL CARRIER AND ORBIT; UNALIGNED COMPLETE-RANK CENSUS REJECTED"
target_claim: NONE-NOT-A-KILL
source_return: SOURCE_CONFIRMS_ACTION_PRIMITIVE_EPSILON_AND_METX_GRAMMAR__REPOSITORY_DERIVES_THE_J4_RESIDUAL_CARRIER_ORBIT_AND_ALIGNMENT_OBSTRUCTION__SOURCE_SILENT_ON_THE_CLASS
canon_verdict_change: none
---

# Selected-K77 CBRS-1N J4 complete-tangent alignment gate

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
result: CBRS-1N exact J4 residual carrier and broken-orbit certificate with rejected unaligned scalar-Schur rank census
carrier: all real Omega1-valued Cl(7,7) T coefficients plus independent Spin-grade-two connection coefficients at four radical J4 points LAYER=ambient CHIRALITY=N/A
pairing: selected K77 Clifford scalar-density Hessian pairing ON=complete_pointwise_T_plus_independent_connection_carrier
real_structure: selected real B-skew Clifford bank over the two nested-radical J4 branch fields
grading: exterior bidegree under the repository-native 4_plus_10 J4 split with real-complex Hodge intertwiner alignment still open
action_owner: repository-construction
target: residual carrier diagonal Spin orbit and validity of the complete Hessian multiplicity reduction MAP-TYPE=evaluation
```

## Result first

CBRS-1N freezes the exact complete pointwise carrier and catches a framing
error before it can become a false Hessian theorem.

The four CBRS-1M branches retain the product stabilizer

```text
Spin(1,3)_base x Spin(6,4)_normal,
dim = 6 + 45 = 51.
```

The complete admitted tangent still has

```text
229,376 real T directions + 1,274 independent Spin-grade-two connection
directions = 230,650.
```

Forty-five coarse exterior/hook product families account for every direction.
The coefficient-only Spin orbit has rank `91` and stabilizer zero, while the
diagonal form-plus-coefficient action has a `51`-dimensional stabilizer and a
`40`-dimensional broken orbit. All 40 mixed generators are independent.

The tempting scalar-representative rank census is **rejected**. It reports
apparent ranks `230590` on the normal-J4 pair and `230550` on the base-J4 pair,
but on the normal pair it simultaneously declares the `E1_base tensor
E1_normal` multiplicity matrix full rank `16` while an independently built
nonzero broken-orbit vector pairs to zero with every representative of that
same coarse family. Both statements cannot define the complete Hessian.

The contradiction is the certificate. One arbitrary representative per
coarse real product label is not an aligned scalar-Schur reduction for this
even `4+10` real form. Hodge-equivalent and real/complex intertwiner choices
must be aligned before multiplicity ranks can be lifted to full carrier ranks.
The printed `230590/230550` values are retained only as hostile diagnostics;
they are not Hessian ranks, kernel dimensions, or survivor counts.

## Exact orbit and why it is load-bearing

For a bivector generator `X=gamma_l gamma_r`, the diagonal tangent acts on
both the coefficient and one-form slot. With the probe normalization,

```text
delta T_l = [X,T_l] + 2 eta_l T_r,
delta T_r = [X,T_r] - 2 eta_r T_l.
```

All within-base and within-normal generators cancel exactly on the symbolic
J4 class, giving the `51`-dimensional residual algebra. Every base-normal
generator is nonzero, and the resulting `4 x 10=40` columns have exact rank
`40` on all four radical branches. Selected-action invariance and complete
point field stationarity require this orbit to lie in the Hessian kernel.
The explicit zero pairings therefore provide a hostile truth condition for
any proposed multiplicity reduction.

The coefficient-only commutator orbit remains rank `91`; it is not the
diagonal gauge orbit and is not substituted for it.

## What remains open

CBRS-1M already proves that all 91 pointwise moving-Shiab primitive returns
vanish and that every constant-grade intrinsic metric row has four nonzero
cells. CBRS-1N does not promote that pointwise primitive zero into a tangent
quotient. Because the complete Hessian kernel is not yet aligned, the
following objects remain open:

- additional non-orbit field-kernel directions beyond the certified orbit;
- the primitive-admissible quotient of that kernel;
- the nonfactorizing first-jet metric graph on that quotient; and
- any first-symbol domain or characteristic kernel.

No symbol is constructed from the rejected apparent nullities.

## Hostile return

- **Strongest overclaim:** `230590` and `230550` are rejected diagnostics, not
  complete Hessian ranks.
- **Strongest contrary condition:** the exact broken orbit supplies a known
  kernel that any valid reduction must reproduce before it may count another
  survivor.
- **Strongest representation error:** equal coarse exterior/hook labels do not
  by themselves align real/complex Hodge intertwiners in the even `4+10`
  factors.
- **Strongest metric error:** a nonzero point density does not close the class
  until the aligned non-orbit tangent and its owned first-jet graph are known.
- **Weakest reproducibility seam:** the current probe is deliberately heavy;
  it replays all 45 coarse blocks so the contradiction cannot be blamed on
  missing carrier accounting.

## Reverse-scaffold consequence

Continue with `CBRS-1O`: build an aligned real/complex intertwiner bank for
the `Spin(1,3) x Spin(6,4)` exterior and hook families, with the 40-dimensional
broken orbit as a mandatory kernel control. Recompute the complete Hessian at
all four branches. Only then restrict the certified kernel by primitive
epsilon and the nonfactorizing metric graph, and construct a symbol only if a
metric-admissible non-orbit quotient survives.

Do not tune the J4 action, add a counterterm, mix the full
`{1,J4,J10,Omega}` commutant, use the rejected nullities, advance to CBRS-2,
or infer a global vacuum or spectrum.

No ledger verdict, canon, source ownership, residue, particle assignment,
prediction, confirmation, or public posture changes.

Reproduce with:

```bash
sage -python \
  tests/channel-swings/selected_k77_cbrs1n_j4_complete_tangent_probe.py
```
