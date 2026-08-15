---
title: "Selected-K108 RSAP physical-split positivity and owner gate"
status: active_research
doc_type: exact_source_native_noninvariant_selector_positivity_and_reduction_owner_test
created: "2026-08-15"
registry: lab/process/selected-k108-rsap-physical-split-positivity-owner-gate.json
probe: tests/channel-swings/selected_k108_rsap_physical_split_positivity_owner_gate_probe.py
grade: "THE SOURCE-CONFIRMED PHYSICAL 4|10 OBSERVATION SPLIT IS A REAL CONCRETE NONINVARIANT KINEMATIC SELECTOR, BUT ITS CONDITIONAL RIGHT REDUCTION IS A DISTINCT 80D PHASE SPACE WITH 18|22 BASE AND 36|44 PHASE SIGNATURES; IT NEITHER POSITIVIZES NOR SELECTS THE 98D BALANCED RSAP"
target_claim: K107_NEXT_GATE__THE_SOURCE_PHYSICAL_1_3_PLUS_6_4_SPLIT_IS_A_CONCRETE_NONINVARIANT_SELECTOR_THAT_POSITIVIZES_THE_BALANCED_98D_RSAP
target_verdict: NO__IT_DEFINES_A_DISTINCT_CONDITIONAL_80D_QUOTIENT_WITH_18_22_BASE_AND_36_44_PHASE_SIGNATURES__RIGHT_REDUCTION_NOT_ACTION_SELECTED
canon_verdict_change: none
---

# Selected-K108 RSAP physical-split positivity and owner gate

> **GU-COMPARATOR-ROUTING — scope before inference.** This is a source-native
> observation-split, phase-space and positivity question. Ordinary Higgs/VEV,
> family-index, net-chirality, anomaly, symmetry-breaking and familiar four-
> dimensional gauge-model conclusions do not adjudicate it. Read
> `lab/methods/source-native-comparator-routing.md` before importing any such
> comparator.

Classification: `SOURCE_NATIVE_ROUTE`.

Scope: Weinstein's declared `TX^(1,3)+N^(6,4)` carrier split inside
`TY^(7,7)`, its homogeneous isotropy representation, and the conditional
cotangent reduction that would result if right `H_phys` were separately
constrained and declared gauge. This does not question the source's
observation construction or treat its kinematic split as an action-selected
boundary law.

## Result in plain English

The physical observation split is a genuine concrete non-invariant object,
not an invented standard-model comparator. It is nevertheless not the
missing positive selector for the balanced reverse RSAP.

The split stabilizer is

```text
H_phys = Spin(1,3) x Spin(6,4),       dim H_phys=6+45=51.
```

Its homogeneous tangent is

```text
p_phys = R^(1,3) tensor R^(6,4),      dim p_phys=40,
signature(p_phys)=(18,22).
```

Consequently a hypothetical right-`H_phys` cotangent reduction of the same
`182D` parent would have dimension

```text
182-2(51)=80,
```

not `98`. Its zero-section compatible phase metrics have signatures
`36|44` or `44|36`; they are still indefinite.

So this candidate fails twice as a repair:

1. it changes the balanced `98D` theory into a distinct `80D` theory; and
2. it does not produce a positive invariant kinetic or phase-space pairing.

There is also an ownership boundary. The source confirms the physical
carrier split. It does not thereby impose the right-`H_phys` moment-zero
equation, declare right `H_phys` gauge, or supply a positive quantum domain.
The `80D` reduction is therefore conditional too.

## 1. Source return and Layer 0

`SC-CHI-03` records the draft's

```text
gimel: X^(1,3) -> Y^(7,7),
TY|_X = TX^(1,3) + N^(6,4).
```

The source-native ownership split is:

```text
SOURCE-CONFIRMS:
  the 4|10 physical carrier decomposition and its luminous/dark spinor
  context.

REPOSITORY-DERIVES:
  the H_phys isotropy module, its invariant signature, and the dimensions of
  a conditional right-H_phys cotangent reduction.

SOURCE-SILENT:
  right-H_phys moment-zero boundary equation, right-H_phys gauge declaration,
  positive kinetic form, closed domain and quantum cohomology.
```

The observation split, internal right-gauge reduction, Green boundary domain,
and positive physical state space are four different object types.

## 2. Exact physical-split signature

For forms of signatures `(r,s)` and `(u,v)`, the tensor product has signature

```text
(ru+sv, rv+su).
```

Therefore

```text
(1,3) tensor (6,4)
  = (1*6+3*4, 1*4+3*6)
  = (18,22).
```

The standard representations of `so(1,3)` and `so(6,4)` each have scalar
commutant. The exact probe obtains commutator-system ranks `15/16` and
`99/100`. The same two-factor block argument as K106 makes the product
commutant scalar, so the tensor metric is the unique invariant symmetric form
up to scale. Overall sign only exchanges `18` and `22`.

Cotangent doubling does not help. K107's complete phase-space argument applies
with `q_(18,22)` in place of `q_(24,25)`: every invariant compatible complex
metric is `B tensor q`, with definite two-dimensional `B`, and hence has

```text
(36,44) or (44,36).
```

Neither the base Lorentz factor `(1,3)` nor the normal factor `(6,4)` is
positive. Selecting only their positive directions breaks the corresponding
noncompact stabilizer and requires another owner.

## 3. It is a different quotient, not a repair of the balanced one

The balanced and physical involutions are not conjugate:

| split | eigenspace multiplicities | trace | stabilizer | quotient |
|---|---:|---:|---:|---:|
| physical `(1,3)|(6,4)` | `4|10` | `-6` | `51` | `80D` |
| balanced `(3,4)|(4,3)` | `7|7` | `0` | `42` | `98D` |

Conjugation preserves multiplicities and trace. Thus epsilon dressing cannot
turn the physical split into the balanced one. Choosing `H_phys` does not
positivize the existing `98D` carrier; it changes which constraint and gauge
system is being proposed.

The source-confirmed observation geometry survives this conclusion. The
failed inference is only

```text
physical observation split
  => action-selected right-H_phys reduction
  => positive replacement for the balanced 98D RSAP.
```

Neither arrow is supplied.

## 4. Disposition

Retain the physical `4|10` split as source-confirmed kinematic geometry. Do
not identify it with the balanced `7|7` order parameter, and do not book its
conditional `80D` quotient as a physical phase space.

The next concrete positivity candidate must own all three of the following on
the actual phase/BFV carrier:

1. the non-invariant selector or constraint;
2. the positive pairing; and
3. the analytic domain plus moving-order-parameter Noether compatibility.

A spinor complex structure without an owned Hermitian form, or a boundary
condition without an action/domain law, does not meet that entry criterion.

No ledger, datum, quotient booking, canon, public posture, particle or
phenomenology claim changes. Reproduce:

```bash
python3 tests/channel-swings/selected_k108_rsap_physical_split_positivity_owner_gate_probe.py
```
