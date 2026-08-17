---
title: "TW3-B: current-K77 dual pairing, normal orientation, and four-corner gluing"
status: exploration
doc_type: conditional_build_exact_dual_pairing_and_corner_gluing_result
artifact_type: exact_current_k77_bilinear_krein_contragredient_certificate
created: 2026-08-16
updated_at: 2026-08-17
work_item: TW-3B
channel: joe_directed_superposition_twistor_conditional_build
target_claim: HYP-TW-COHERENCE-01
grade: "EXACT fibrewise current-real-K77 and normal-Cl(6,4) bilinear/Krein theorem, exact finite Spin contragredient covariance, and exact four-corner convention classifier. The conjugate/Krein reading of the TW2 target closes formally; a strict complex-algebraic-star reading has a different corner target and may not be conflated with it. No positive pairing, analytic adjoint/domain, rolled descent, action, background, quotient, family selector, physical state, or superposition theorem."
disposition: FORMAL_KREIN_DUAL_GLUING_CLOSES__ALGEBRAIC_STAR_NOT_EQUAL_TO_KREIN_OVERLINE__CONTRAGREDIENT_REQUIRED_BEFORE_RIESZ_IDENTIFICATION__ALL_FOUR_CORNERS_RETAINED__ROLLED_DESCENT_LEFT_TO_TW3C
source_return: SOURCE_SILENT__REPOSITORY_DERIVED_CURRENT_K77_FIBRE_KINEMATICS_ONLY
probe: tests/channel-swings/joe_directed_tw3b_dual_pairing_orientation_gluing_probe.py
canon_verdict_change: none
depends_on:
  - lab/methods/source-native-comparator-routing.md
  - lab/active-research/joe-directed/conditional-build-channel-read-packet-2026-08-16.md
  - lab/active-research/joe-directed/high-energy-two-plus-one/he4-path-reprioritization-2026-08-16.md
  - lab/active-research/joe-directed/superposition-twistor/tw1-normal-twistor-spin-lift-2026-08-16.md
  - lab/active-research/joe-directed/superposition-twistor/tw2-four-dimensional-detour-symbol-factorization-2026-08-16.md
  - lab/process/hostile-reviews/2026-08-16-joe-directed-twistor-conditional-composition-review.md
---

> [!IMPORTANT]
> **GU-COMPARATOR-ROUTING — scope before inference.** This artifact contains or
> borders a conventional particle-physics comparator. Any result about a
> standard Higgs/VEV, ordinary family index or net chirality, SO(10) `126`
> Majorana mechanism, anomaly selector, VEV-only breaking or familiar vector-
> mass route binds only that named model. It is not evidence for or against
> Weinstein's source-native mechanism without an explicit typed bridge. Read
> `lab/methods/source-native-comparator-routing.md` and follow its source-native
> pointers before reusing this result.
>
> Classification: `BRIDGE_OR_SEMANTIC_BOUNDARY`.

# TW3-B — dual pairing, orientation, and four-corner gluing

## Result first

TW2's displayed matrix copy of the dual target is equivariant, but only after
one states which dual is meant and lets the raw dual transform
**contragrediently**. The current real-K77 module supplies two related but
noninterchangeable exact structures:

1. a real Spin-invariant skew bilinear form, whose complex-bilinear Riesz map
   exchanges the two normal half-spin factors; and
2. an induced sesquilinear Hermitian/Krein form of signature `(8,8)` on each
   complex normal half, whose antilinear Riesz map keeps the normal-half label.

The second is the convention compatible with TW2's chiral line

```text
Tw_+ -> overline(Tw)_-,
Tw_- -> overline(Tw)_+.
```

With that conjugate/Krein target convention, the four K77 observation corners
glue as

```text
++ <-> -+,
+- <-> --.
```

In words: the base Weyl label flips and the internal `S10+/-` label stays
fixed. This is exactly the corner action already implicit in TW2's matrix
chirality calculation. All four corners and both ambient K77 halves remain;
the target map exchanges the two ambient halves rather than selecting one.

A strict complex-linear algebraic-star reading is different. The invariant
bilinear form pairs

```text
++ <-> +-,
-- <-> -+,
```

so the base label stays fixed and the internal half exchanges. Therefore the
notations `Tw*` and `overline(Tw)` in the prior prose cannot be treated as
synonyms at the corner level. This is an exact typing correction, not a
failure of the TW2 identities `N3 T=0`, `T# N3=0`, or of its rank table.

The formal finite gluing therefore closes on the **Krein/conjugate-dual
reading**. It does not close on a strict algebraic-star reading without
retyping the target. The raw covector action is always contragredient; a
primal-looking matrix appears only after the appropriate Riesz identification.

## Conditional horn and stop boundary

The horn is deliberately smaller than a global twistor construction:

```text
TW3B-DUAL:
  retain TW1's supplied fibrewise normal complex structure and Spin lift;
  equip the already-owned current-K77 spin module with its invariant
  bilinear form and the resulting normal Krein form;
  ask whether TW2's algebraic dual matrices glue equivariantly on all four
  observation corners.
```

No source passage selects this horn. It constructs no global `J_N` or `Tw^2`
field, action, background, external datum, total current, connection, analytic
domain, quotient, positive Hilbert pairing, family row, particle state, or
physical superposition. Full rolled-symbol/stabilizer descent belongs to
TW3-C and is not performed here.

## Twelve-lens preflight and assessment

| lens | exact disposition |
|---|---|
| source fidelity | `SOURCE_SILENT`: no source row asserts this pairing or corner map. |
| comparator routing | This is a source-native semantic boundary; standard family, Higgs/VEV, `126`, anomaly and vector-mass routes do not adjudicate it. |
| `2+1` referent custody | No eigenspace or corner is identified with source `F`, multiplicity space `M_3`, or the distinct partner `144`. |
| emergent chirality | The parent remains fundamentally non-chiral; both ambient halves and all four corners are retained. No ordinary net-chirality index is used. |
| current real form | The certificate uses the exact real `Cl(7,7)` K77 module and its normal `Cl(6,4)` factor; no K95 pairing transfers. |
| invariant-form lens | `C10` is skew and Spin invariant; `C10 J10` is neutral symmetric. Neither is positive. |
| complex-half lens | The bilinear form pairs `S10+` with `S10-`; the induced Hermitian/Krein form is nondegenerate of signature `(8,8)` on each half. |
| dual/contragredient lens | Raw duals carry `rho(g)^(-T)`. The matrix copy carries `rho(g)` only after equivariant Riesz identification. |
| orientation/component lens | `S_J` versus `-S_J` changes central phase only; `J_N` versus `-J_N` uses `S_J^-1`, reverses the square sign relative to fixed `J10`, and exchanges the fixed-half phase tables. |
| corner-gluing lens | Krein/conjugate dual flips base only; strict algebraic bilinear dual flips normal only. Deleting or merging a corner fails. |
| archaeology/novelty lens | TW1 owned the lift and phase spectra; TW2 owned the cubic and matrix target; the prior hostile review explicitly left the dual convention as TW3's seam. The exact pairing/corner classifier is new. |
| falsification/ceiling lens | Degenerate or definite Gram, failed contragredient covariance, central/component conflation, one-half deletion, or equality of the two corner maps would kill the result. Exact controls reject all five. |

## 1. Exact normal-spin bilinear and Krein structures

Use a real `32 x 32` representation of `Cl(6,4)` with

```text
gamma_a^2 = +1,  a=1,...,6,
gamma_a^2 = -1,  a=7,...,10.
```

Define

```text
C10 = gamma_1 ... gamma_6,
J10 = gamma_1 ... gamma_10,
G10 = C10 J10.
```

The exact rational certificate gives

```text
C10^T = -C10,       C10^2 = -1,
gamma_a^T C10 = -C10 gamma_a,
J10^2 = -1,         J10^T C10 = -C10 J10,
G10^T = G10,        G10^2 = 1,
signature_R(G10) = (16,16).
```

Hence every even normal Spin generator preserves `C10`. Since `J10` is
central in the even normal Clifford algebra, the observer-normal Spin action
also preserves `G10`. The adjective *Krein* here means nondegenerate and
indefinite. This is not a positive pairing.

After complexification let

```text
S10+ = ker(J10-i),
S10- = ker(J10+i).
```

The complex-bilinear form

```text
B10(x,y)=x^T C10 y
```

vanishes on `S10+ x S10+` and on `S10- x S10-`, while its cross-half Gram has
rank `16`. Thus its linear Riesz map exchanges the two halves.

On either half, with `delta=+1` on `S10+` and `delta=-1` on `S10-`, the
uniform conjugate form

```text
h_delta(x,y)
  = delta i conjugate(x)^T C10 y
  = conjugate(x)^T G10 y
```

is Hermitian. The `delta` sign is required: on `S10-`, `J10=-i`, so the
restriction of the one real form `G10=C10 J10` is `-i C10`, not `+i C10`.
In an exact `Q(i)` half-spin basis each correctly signed restriction has
characteristic polynomial

```text
(lambda-2)^8 (lambda+2)^8,
```

on both halves. Therefore each complex half is an exact Krein space of
signature `(8,8)`. Complex conjugation first exchanges the `J10` eigenspaces;
the bilinear Riesz map exchanges them again. The resulting sesquilinear Riesz
map keeps the displayed `S10+/-` label. That double exchange is why the
bilinear and Krein corner rules differ.

## 2. The current-K77 parent form

In the exact real `128 x 128` `Cl(7,7)` bank, let

```text
C14 = gamma_1 ... gamma_7
```

for the seven positive generators. Then

```text
C14^T=-C14,
gamma_a^T C14=C14 gamma_a,
```

so every ambient Spin bivector preserves `C14`. Relative to the repository's
fixed base volume `W4`, normal volume `J10`, and ambient chirality `W14`,

```text
W4^T  C14 = +C14 W4,
J10^T C14 = -C14 J10,
W14^T C14 = -C14 W14.
```

These three identities are the exact four-corner selection rule: the
complex-bilinear pairing keeps base chirality, exchanges normal chirality, and
pairs opposite ambient K77 halves. The observer-normal symmetric form
`C14 J10` is an involution with trace zero and real signature `(64,64)`. It is
observer-subgroup invariant, not a positive metric and not a new full-K77
reduction.

## 3. Why contragredient action is compulsory

For a raw linear dual, the finite action is

```text
rho_dual(g)=rho(g)^(-T).
```

Let `R_B` be the Riesz map defined by `C10`. Spin invariance is exactly

```text
R_B rho(g) = rho(g)^(-T) R_B,
R_B^(-1) rho(g)^(-T) R_B = rho(g).
```

This proves two different statements that must not be collapsed:

- on the raw dual target, the action is contragredient;
- after the invariant Riesz identification, its matrix copy is primal.

This fibre Riesz map is not an analytic adjoint and supplies no operator
domain.

For TW1's rationally scaled lift `T=sqrt(32) S_J`, the probe verifies

```text
T^T C10 T = 32 C10,
T^T G10 T = 32 G10,
32 C10^(-1) T^(-T) C10 = T.
```

The selected lift happens to commute with `C10`, so it is a poor adverse
control for the primal/dual distinction. The probe therefore also uses the
exact rational noncompact Spin element

```text
U=(5+4 gamma_1 gamma_7)/3.
```

It satisfies

```text
U^T C10 U=C10,
C10^(-1) U^(-T) C10=U,
C10^(-1) U C10 != U.
```

Thus using the primal action on the raw dual is an exact failure even though a
Riesz-identified matrix target may look primal. No analytic adjoint or common
operator domain is involved.

## 4. Orientation, central sign, and exact phases

TW1's selected orientation-aligned lift has

```text
S_J^2=-J10.
```

Changing the central preimage `S_J -> -S_J` preserves the square and the
pairings. It shifts every eighth-root phase exponent by four but does not
permute a corner:

```text
S10+ : {7 x10, 3 x6} -> {3 x10, 7 x6},
S10- : {1 x10, 5 x6} -> {5 x10, 1 x6}.
```

Changing the vector component `J_N -> -J_N` is different. Relative to the
fixed normal orientation its exponential lift is `S_J^-1` and

```text
(S_J^-1)^2=+J10.
```

It does not relabel the fixed eigenspaces of `J10`, but it exchanges their
phase tables:

```text
fixed S10+ receives {1 x10, 5 x6},
fixed S10- receives {7 x10, 3 x6}.
```

The raw contragredient spectrum on one half is the inverse spectrum and equals
the primal spectrum on its bilinear partner half. Under the antilinear Krein
Riesz map, complex conjugation supplies the second inversion, so the
Riesz-identified matrix action again carries the primal phase table on the
same displayed internal half.

On admitted overlaps, changing a Spin overlap lift by its central sign changes
both transported representatives by the same sign; the bilinear or
sesquilinear pairing cancels it. This is the only overlap-sign statement used
here. No global cocycle or normal-twistor section is constructed.

## 5. TW2 target retyping and exact corner maps

Write a corner as `(epsilon_4,delta_10)`. There are two honest maps:

| target convention | internal dual behavior | corner map | ambient-half behavior |
|---|---|---|---|
| strict complex-bilinear `B14` dual | `S10_delta^*` is represented by `S10_-delta` | `(epsilon,delta)->(epsilon,-delta)` | exchanges ambient halves |
| conjugate/Krein dual | conjugation and `B10` exchange cancel | `(epsilon,delta)->(-epsilon,delta)` | exchanges ambient halves |

TW2's exact chiral matrix computation is the second row:

```text
++ -> -+,   -+ -> ++,
+- -> --,   -- -> +-.
```

Therefore its earlier prose should be read as follows:

```text
overline(Tw) target:  exact Krein/conjugate-dual matrix copy;
Tw* target:           acceptable shorthand only after that convention is stated;
strict algebraic Tw*: a different target and not the same corner map.
```

With this repair, `T`, `N3`, `T#`, and the compressed `Q,T,-T#` blocks are
normal-Spin equivariant at fibre grade: normal transport acts on the
coefficient factor, raw targets transform contragrediently, and the invariant
Krein Riesz map returns the matrix copy. The closure is not merely an assertion
that tensors commute; the dual convention and the internal-half double
exchange are load-bearing.

## Mutants and falsifiers

The exact probe rejects:

1. primal action on a raw dual instead of `rho^(-T)`;
2. identifying the central-sign lift with the opposite orientation component;
3. treating the algebraic-bilinear and Krein/conjugate corner maps as equal;
4. deleting one K77 half or one of the four corners;
5. identifying the two fixed normal half-spin spectra;
6. calling the neutral `(8,8)` form positive;
7. promoting an algebraic Riesz map to an analytic adjoint/domain; and
8. reading a corner, phase multiplicity, or Krein signature as a family or
   physical-particle count.

The source imposter `F`, multiplicity space `M_3`, partner `144`, and
Weinstein's proposed emergent chirality are unchanged. Nothing here supplies
an ordinary family index or a physical selector.

## Fertility and handoff

This is a **formal closure with a nontrivial notation/type repair**, fertility
`6/10` for the bounded TW3 program. The normal pairing does not obstruct the
Krein/conjugate TW2 gluing, and the phase/component bookkeeping is exact. But
the result also shows that a future artifact cannot alternate casually between
`Tw*` and `overline(Tw)`; strict algebraic duality lands in different corners.

TW3-C should carry the conjugate/Krein target convention explicitly when it
tests the compressed rolled blocks. It should not redo the pairing, invent a
positive form, or widen into an action, background, global `J_N`, `Tw^2`
field, analytic domain, quotient, or physical state. If the remaining rolled
test is only ordinary tensor-product covariance after this retyping, bank it
and deprioritize the twistor path as already instructed.

## Reproduction and claim ceiling

```text
DOT_SAGE=/tmp/gu-tw3b-sage sage -python tests/channel-swings/joe_directed_tw3b_dual_pairing_orientation_gluing_probe.py
DOT_SAGE=/tmp/gu-tw3b-sage sage -python tests/channel-swings/joe_directed_tw3b_dual_pairing_orientation_gluing_probe.py --selftest
```

The strongest licensed statement is:

> The current real-K77 spin module has an exact invariant skew bilinear form
> and an induced neutral normal Krein structure. Raw TW2 dual targets must
> transform contragrediently. After the conjugate/Krein Riesz identification,
> the matrix target is equivariant, preserves the internal half label, flips
> base Weyl chirality, and retains all four K77 corners for both normal-
> twistor orientation components and both central-sign lifts.

It is not licensed to call the form positive, the Riesz map an analytic
adjoint, the target a physical state space, a phase a family selector, or this
finite gluing a proof of emergent chirality or quantum superposition.
