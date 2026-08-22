---
title: "Selected-K77 CBRS-1O J4 coordinate-component alignment gate"
status: active_research
doc_type: exact_tangent_method_correction
created: "2026-08-22"
registry: lab/process/selected-k77-cbrs1o-j4-aligned-hessian.json
probe: tests/channel-swings/selected_k77_cbrs1o_j4_aligned_hessian_probe.py
grade: "EXACT RECONSTRUCTION-GRADE COORDINATE-COMPONENT ALIGNMENT AND ORBIT LOCATION; COMPLETE COMPONENT RANKS OPEN"
target_claim: NONE-NOT-A-KILL
source_return: SOURCE_CONFIRMS_ACTION_PRIMITIVE_EPSILON_AND_METX_GRAMMAR__REPOSITORY_DERIVES_THE_J4_COORDINATE_COMPONENT_BANK_AND_ALIGNMENT_OBSTRUCTION__SOURCE_SILENT_ON_THE_CLASS
canon_verdict_change: none
---

# Selected-K77 CBRS-1O J4 coordinate-component alignment gate

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
result: CBRS-1O exact J4 coordinate-component alignment bank with nominal residual-irrep obstruction
carrier: all real Omega1-valued Cl(7,7) T coefficients plus independent Spin-grade-two connection coefficients at four radical J4 points LAYER=ambient CHIRALITY=N/A
pairing: selected K77 Clifford scalar-density Hessian support ON=complete_pointwise_T_plus_independent_connection_carrier
real_structure: selected normalized B-skew Clifford bank over the two nested-radical J4 branch fields
grading: canonical q=coefficient_mask_XOR_form_slot modulo the repository-native J4 mask
action_owner: repository-construction
target: invariant coordinate support components and broken diagonal-Spin orbit location MAP-TYPE=evaluation
```

## Result first

CBRS-1O rejects the premise that the 45 CBRS-1N exterior/hook dimension
families already form invariant residual-Schur blocks in the normalized real
Clifford basis. This is stronger than the earlier statement that their phases
were merely unaligned.

The nominal `E1_base tensor E1_normal` bank contains sixteen independent
chosen representatives. An explicit nonzero broken-orbit vector for generator
`gamma_0 gamma_4` raises the coordinate-span rank from `16` to `17`. The orbit
vector is therefore outside the nominal representative span before any
Hessian-rank lift. A literal complementary-Hodge transport leaves the rejected
apparent totals `230590/230550` unchanged and does not repair this defect.

The complete selected Hessian does have a canonical exact alignment:

```text
q(form_slot, coefficient_mask)
  = coefficient_mask XOR (1 << form_slot),

component key = {q, q XOR J4}.
```

A support-only replay of the selected action Hessian erases coefficients and
signs but mirrors every Clifford multiplication, form wedge, Hodge operation,
Shiab channel, and linearized pairing. It is an over-approximation: every
possible `T/T`, connection/connection, and connection/`T` term preserves the
component key before cancellation, so every actual nonzero term preserves it.
Affine-XOR covariance is checked on route-changing masks.

The result is an exact complete-carrier partition:

| component dimension | number of components |
| ---: | ---: |
| 28 | 7,848 |
| 31 | 300 |
| 34 | 30 |
| 41 | 10 |
| 44 | 4 |

There are `8,192` components. Every component contains `28` real `T`
directions. The larger components distribute all `1,274` independent
Spin-grade-two connection directions exactly once. Their dimensions sum to
`230,650`.

Each of the `4 x 10 = 40` broken base-normal diagonal-Spin generators lies in
one component, the 40 keys are distinct, and the resulting orbit matrix has
rank `40` at all four radical branches. Thus CBRS-1P can rank small exact
coordinate matrices with the orbit column inside each affected component,
without any arbitrary residual-irrep representative.

## What this corrects

The old labels remain valid as a coarse dimension census only. They are not an
invariant decomposition in the normalized real basis. The concrete mismatch
appears already in the orbit component: naive exterior contraction inserts
signature signs that do not reproduce the actual form-plus-coefficient Spin
action. Consequently neither a raw representative nor a Hodge-phase tweak can
license a Schur rank multiplier.

The coordinate key is target-native and basis-explicit. It follows from the
two background coefficient masks per form slot, `gamma_i` and
`gamma_i J4`, and from Clifford multiplication by XOR. It does not claim a
canonical Spin(7,7)-invariant splitting or an observed 3+1 decomposition.

## What remains open

No component rank was inferred from support closure. The following remain
open:

- the exact four-branch rank of every component;
- whether the 40 orbit directions exhaust the complete kernel;
- any additional non-orbit field-kernel directions;
- the primitive-epsilon restriction of a certified kernel;
- the nonfactorizing first-jet metric graph on the primitive quotient; and
- any first-symbol domain or characteristic kernel.

The rejected `230590/230550` values remain diagnostics only.

## Route and hostile review

The council compared an explicit highest-weight/Hodge bank, a full
`230650 x 230650` sparse matrix, a phase repair of the old blocks, and a
coordinate-support decomposition. The phase repair was tried and falsified;
the full matrix was dominated by the exact small-component factorization. The
coordinate route was selected because it is invariant under the actual
operator support and exposes the orbit without assuming the disputed
representation map.

- **Strongest overclaim:** component closure is not component rank, complete
  kernel, or metric stationarity.
- **Strongest contrary condition:** one of the 8,192 exact component matrices
  may contain a non-orbit null direction.
- **Strongest representation error:** the 45 nominal families account for
  dimensions but do not supply an invariant Schur bank in the normalized real
  Clifford basis.
- **Strongest arithmetic seam:** a future good-prime lower bound must state
  radical and denominator nonvanishing and must be matched to a
  characteristic-zero upper bound; a modular rank alone is not a theorem.
- **Weakest reproducibility seam:** the support replay must remain an
  over-approximation. Deleting either the form-slot XOR or the `J4` quotient
  is caught by planted controls.

## Reverse-scaffold consequence

Continue with `CBRS-1P`: evaluate every canonical component over the exact
normal- and base-J4 radical fields, or use good-prime ranks only inside an
explicit characteristic-zero rank sandwich. Every affected cross component
must reproduce its known orbit column. Then, and only then, restrict the
certified complete kernel by primitive epsilon and the nonfactorizing metric
graph and construct a symbol if a metric-admissible non-orbit quotient
survives.

Do not tune the action, add a counterterm, mix the full
`{1,J4,J10,Omega}` commutant, reuse the rejected ranks, or advance to CBRS-2.

No ledger verdict, canon, source ownership, residue, particle assignment,
prediction, confirmation, or public posture changes.

Reproduce with:

```bash
sage -python \
  tests/channel-swings/selected_k77_cbrs1o_j4_aligned_hessian_probe.py
```
