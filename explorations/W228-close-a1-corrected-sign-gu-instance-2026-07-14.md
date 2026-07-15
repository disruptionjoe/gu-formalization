---
artifact_type: exploration
label: W228
created: 2026-07-14
status: exploration
posture: adversarial; truth-seeking; native-object first; no verdict movement
title: "W228 close A1: corrected reservoir-sign theorem, GU-specific instance -- GU's good-stable stabilizer is the CANONICAL forced-unique case, not the degenerate continuum; the C-grading sign is forced UNIQUE at the kinematic-stabilizer level"
grade: "EXACT for the finite-dimensional representation-theory computation (constituent lists, non-coincidence, grading-moduli dimension, and explicit eta-frame positivity enumeration are all deterministic and machine-checked: tests/W228_corrected_sign_gu_instance.py, 22/22, exit 0). This complements, does not duplicate, the GENERAL corrected theorem in papers/drafts/structurally-forced-internally-undecidable/. KINEMATIC-STABILIZER grade for the physical conclusion: the forcing is proven for the derived compact C-commutant of the (9,5) structure; the DYNAMICAL good-stable stabilizer (interacting vacuum + observable algebra) is still not built (W219), so bar (b) does not flip. No canon, RESEARCH-STATUS, bar (b), or H59 change."
depends_on:
  - papers/drafts/structurally-forced-internally-undecidable/HARDENING-REPORT.md
  - explorations/W203-branch3-source-action-fixed-coefficients-2026-07-14.md
  - explorations/W206-decisive-bit-counterfactual-invariance-2026-07-14.md
  - explorations/W211-krein-sign-godel-independent-five-method-synthesis-2026-07-14.md
  - explorations/W219-native-good-stable-stabilizer-input-gate-2026-07-14.md
  - explorations/W168-reduction-krein-signature-2026-07-14.md
scripts:
  - tests/W228_corrected_sign_gu_instance.py
supersedes_conclusion_of:
  - "W206 verdict RESIDUAL-BIT-STANDS (free Z/2): CORRECTED here for the GU instance -- the grading sign is FORCED UNIQUE; W206's dim-2 was the invariant-form/majorant cone, not the grading space"
  - "W211 Godel-INDEPENDENT synthesis: its GU-specific leg is withdrawn (already killed in the hardening report)"
---

# W228 close A1: corrected reservoir-sign theorem, GU-specific instance

## Result in one paragraph

For GU's actual good-stable stabilizer -- the maximal-compact C-commutant of
the `(9,5)` Clifford structure, whether resolved as `SO(9) x SO(5)` or refined
to `SO(3) x SO(6) x SO(4)` on the `(9,5) = (3,1) + (6,4)` frame -- the two
eigenspaces of the Krein grading `C` share NO irreducible constituent. The
non-coincidence hypothesis of the corrected theorem HOLDS. Therefore positivity
plus the involution constraint (`C^2 = I`, `C` eta-self-adjoint, `eta.C`
positive-definite) forces the admissible `C`-grading UNIQUE: the grading-sign
moduli space has dimension `0`. GU sits in the CANONICAL (forced-unique) case of
the general theorem, not the degenerate (continuum) case. This is the GU-specific
complement to the paper's general corrected-theorem rewrite, and it directly
corrects W206, whose `RESIDUAL-BIT-STANDS` / free-`Z/2` conclusion mistook the
2-dimensional invariant-symmetric-FORM cone (the positive-majorant scale freedom)
for a grading-sign freedom. Verdict: **COMPLETED-FORCED-INTERNAL**, at the
kinematic-stabilizer level. The one honest caveat, carried below and unresolved,
is that this is the isotropy of the derived compact commutant; the interacting
DYNAMICAL good-stable stabilizer is still unbuilt (W219), so bar (b) does not
flip on this result alone -- but every currently-derivable candidate stabilizer
lands in the forced-unique case.

## 1. The question, stated as the general theorem's dichotomy

The 2026-07-14 hardening report replaced the old "free grading `Z/2`" claim with
a finite-dimensional classification. For a real Krein space `(V, eta)` and a
compact stabilizer `K`, the admissible grading operators
`{C : C^2 = I, C eta-self-adjoint, eta.C positive-definite}` form a space of real
dimension

```
sum_lambda dim_R(D_lambda) * a_lambda * b_lambda,
```

where `lambda` runs over irreducible `K`-types, `D_lambda in {R,C,H}` is the
endomorphism ring, and `(a_lambda, b_lambda)` is the +/- multiplicity of type
`lambda` across the eigenspaces of `C`. The admissible grading is **unique**
(dimension `0`) exactly when no type occurs on both sides (the "non-coincidence"
hypothesis). A continuum appears **only** in the degenerate case where a `+`
constituent and a `-` constituent are the same irreducible `K`-type.

Lane A1's question is therefore sharp and binary: **for GU's actual stabilizer,
does a `+` constituent coincide with a `-` constituent, or not?**

## 2. GU's actual good-stable stabilizer (from W203/W206/W219)

The good-stable data the deformations must preserve are the indefinite Clifford
metric `eta` of signature `(9,5)` (W203's forced kernel) together with the
positive-definite total metric `eta_+ = eta.C = |eta|`, `C = sign(eta)`
(W206 sec. 2-3). The common isometry group of an indefinite form and its
positive absolute value is the maximal compact subgroup, so the kinematic
good-stable stabilizer is

```
G* = so(9,5) cap o(14) = so(9) (+) so(5),   dim = 36 + 10 = 46,
```

exactly W206's and W219's `SO(9) x SO(5)`. Refining by the good-stable base/fiber
structure -- base `(3,1)`, DeWitt fiber `(6,4)`, with the fiber's geometric-`6` /
record-count-`4` Krein split (W168) -- takes the stabilizer down to the maximal
compact of `SO(3,1) x SO(6,4)`:

```
G*_refined = SO(3) x SO(6) x SO(4),   dim = 3 + 15 + 6 = 24.
```

At the fully native spinor level (W219) the same object is the Cartan
centralizer `Sp(32) x Sp(32)` inside `Sp(32,32;H)`, with spin-lift image
`Spin(9) x Spin(5)`. All four are candidate resolutions of the SAME good-stable
stabilizer at different construction levels.

## 3. The decisive computation: non-coincidence HOLDS at every resolution

The grading `C = sign(eta)` splits the 14-frame vector rep into its
`eta`-positive `9` and `eta`-negative `5`. Listing the constituents under each
stabilizer:

| stabilizer | `V+` (C = +1, dim 9) | `V-` (C = -1, dim 5) | shared type? |
|---|---|---|---|
| `SO(9) x SO(5)` | `(9, 1)` | `(1, 5)` | none |
| `SO(3) x SO(6) x SO(4)` | `(3,1,1) (+) (1,6,1)` | `(1,1,1) (+) (1,1,4)` | none |
| `Sp(32) x Sp(32)` (W219) | first-factor standard | second-factor standard | none |
| `Spin(9) x Spin(5)` (W219) | `Spin(9)` spinor | `Spin(5)` spinor | none |

In every row the `+` and `-` constituent sets are **disjoint**: they live in
different factors, or carry different dimensions, or both. The non-coincidence
hypothesis holds. Hence

```
grading-sign moduli dim = sum_lambda dim_R(D) a_lambda b_lambda = 0
```

at each resolution, and the admissible `C` is **unique**. GU is the CANONICAL
forced-unique case. (Machine check: `[GU]` and `[CG]` blocks, 22/22 pass.)

The explicit eta-frame confirmation (`[EX]` block): build
`eta = diag(+1^9, -1^5)` and enumerate the block-scalar involutions
`C = sum s_i P_i`, `s_i in {+1,-1}`. Four candidates for `SO(9) x SO(5)`
(sixteen for the four-block refinement); positivity of `eta.C` picks out
**exactly one** in each case, namely `C = eta` itself. The sign flip
`C = -eta` gives `eta.C = -I`, negative-definite, so positivity kills it. This
is Corollary 3 of the hardening report, instantiated on GU's numbers.

## 4. Why W206 read a "free Z/2" -- the corrected diagnosis

W206 computed `dim {G*-invariant symmetric forms} = 2` (basis `{eta_+, eta}`)
and `= 4` for the finer split, and read the `{eta_+ vs eta}` pair as a free
grading sign. That is the exact conflation the hardening report killed:

- The invariant symmetric FORMS `B = c1 P9 + c2 P5` are a 2-parameter object,
  and the positive-definite ones form the open cone `c1, c2 > 0`. This is the
  **positive-majorant scale freedom**: one independent Schur scale per isotypic
  block. It is real and is correctly counted by
  `sum_lambda d_R(a_lambda + b_lambda)` = 2 (and 4 after refinement).
- The admissible **gradings** are a different object. `eta = P9 - P5` is NOT a
  positive metric (it is indefinite `(9,5)`); it is not a competing point in the
  positive cone. It is the unique involution surviving `C^2 = I` and
  `eta.C > 0`. Its moduli dimension is `0`.

So W206's number `2` is genuine but mislabelled: it is the majorant cone's
dimension, not a grading-sign dimension. The map "invariant-form space ->
grading space" is not the identity; W206 applied Schur to the wrong object.
Correspondingly, W206's "refining the good stable ENLARGES the residual from 2
to 4" is true of the majorant cone and false of the grading space: refinement
adds independent block scales (more positive metrics) while the grading stays
unique, because refinement only splits constituents further apart -- it never
makes a `+` type coincide with a `-` type. The machine check `GU3` verifies
exactly this: form-space `2 -> 4`, grading-space `0 -> 0`.

This also withdraws the GU-specific leg of W211's "Godel-independent" synthesis,
already flagged as killed in the hardening report; W228 supplies the positive
replacement (forced-unique) rather than merely negating the old claim.

## 5. Personas

**Invariant-theory / Schur specialist.** The residual is governed by the real
isotypic decomposition, not by counting invariant forms. On `SO(9) x SO(5)` the
`9` and `5` are distinct real irreducibles with `End = R`; there is no
intertwiner from `V+` to `V-`, so no off-diagonal grading deformation exists.
Schur gives one scale per block for the FORM (hence dim 2) and zero intertwiners
for the GRADING (hence dim 0). Both facts are Schur; W206 reported only the
first and attached it to the second's question. On the refinement the four
irreducibles `3, 6, 1, 4` are pairwise inequivalent, so the same holds with four
block scales and still zero cross-intertwiners.

**Krein / involution-and-positivity specialist.** The admissible set is
`F_K(eta) = {C : C^2 = I, eta.C symmetric, eta.C > 0}`. On a Krein space with
`C`-commutant `K`, `F_K(eta)` is the product over shared types of
`U(a,b)/(U(a) x U(b))`; a type with `b_lambda = 0` contributes a point. GU has
`b_lambda = 0` on every `+` type and `a_lambda = 0` on every `-` type, so
`F_K(eta)` is a single point. Positivity is what does the cutting: of the four
sign involutions commuting with the block structure, `eta.C` is positive for one
and indefinite or negative for the other three. Verified by direct
diagonalization.

**GU-stabilizer / (9,5)-structure specialist.** The physically correct
stabilizer is the commutant of `C = sign(eta)` inside `so(9,5)`, which is
precisely `so(9) + so(5)` -- not some smaller subgroup under which the `9` could
break into pieces equivalent to pieces of the `5`. That larger-group fact is
what guarantees non-coincidence: the good-stable structure (preserving `eta` AND
`eta_+`) keeps the `+` and `-` sectors in separate factors by construction. The
`(3,1)+(6,4)` refinement respects the DeWitt base/fiber and the geometric/record
Krein split (W168), and each of those pieces is still labelled by a distinct
compact factor. There is no GU-motivated refinement that identifies a `+`
constituent with a `-` constituent.

**Ruthless skeptic.** Two honest limits. (i) This is the isotropy of the DERIVED
KINEMATIC compact commutant. The interacting DYNAMICAL good-stable stabilizer --
the isotropy of an actual vacuum together with the physical observable algebra --
is not built (W219: "DYNAMICAL-GOOD-STABLE-STABILIZER: NOT YET DEFINED"). If that
object turned out to be some strictly smaller group under which a `9`-piece and a
`5`-piece coincide, the continuum could reappear. Nothing in the built repository
produces such a group, but nothing forbids it a priori either. (ii) The
degenerate case is real and reachable in principle -- the diagonal
`O(r) <= O(r,r)` control shows a genuine `r`-parameter continuum, and the torus
control shows `r^2`. GU simply is not in it, because its derived stabilizer is
large enough to separate the sectors. The claim is therefore precisely:
forced-unique for every candidate stabilizer the program can currently derive,
NOT an unconditional theorem about an object that has not been constructed.
Accordingly bar (b) does not flip here; it CLEARS only when the dynamical
stabilizer is built and shown to be one of these (or any other non-coincident)
groups. That last step is exactly the W219 front door and is out of A1's scope.

## 6. Verdict

```
LANE A1: COMPLETED-FORCED-INTERNAL
  GU's good-stable stabilizer (kinematic, all derivable resolutions:
    SO(9)xSO(5), SO(3)xSO(6)xSO(4), Sp(32)xSp(32), Spin(9)xSpin(5))
  is the CANONICAL forced-unique case of the corrected reservoir-sign theorem.
  Non-coincidence hypothesis: HOLDS (V+ and V- share no G*-irreducible).
  Admissible C-grading: UNIQUE (grading-sign moduli dim = 0).
  Positivity kills the sign flip explicitly (eta.C < 0 for the flip).

  W206's RESIDUAL-BIT-STANDS (free Z/2): CORRECTED. Its dim-2 (dim-4 refined)
  was the invariant-form / positive-majorant cone, not the grading space.

  The Krein-sign conditional resolves INTERNALLY at the kinematic-stabilizer
  level. bar (b) does NOT flip here: clearing it requires the interacting
  DYNAMICAL good-stable stabilizer (W219, unbuilt) to be shown non-coincident.
  Every currently-derivable candidate already is.
```

## 7. What this changes and what it does not

Changes (exploration-tier, no canon movement):

- Establishes the GU-specific instance of the corrected theorem: forced-unique,
  complementing the general rewrite in the paper draft.
- Corrects W206's central conclusion for the GU case and withdraws W211's
  GU-specific "Godel-independent" leg (already killed in the hardening report).
- Gives the positive replacement result: the sign is derived-as-invariant, not
  posited, at the kinematic stabilizer.

Does not change:

- bar (b) and H59 remain OPEN. No RESEARCH-STATUS, claim-status, verdict, or
  posture movement.
- Does not build the interacting vacuum, observable algebra, or dynamical
  isotropy group. The single remaining risk (W219, sec. 4-6) is unchanged: the
  physical good-stable representation is not yet derived. The next pickup is the
  W219 front door -- derive the dynamical stabilizer and confirm it is one of the
  non-coincident groups above.

## 8. Machine receipt

```
python -u tests/W228_corrected_sign_gu_instance.py
```

Result on 2026-07-14: `22/22 checks passed`, exit `0`. Positive controls first:
the canonical `O(p)xO(q)` case (grading dim 0), the DEGENERATE diagonal
`O(r) <= O(r,r)` and torus cases (grading dim `> 0`, up to `r^2`), so the
detector demonstrably sees a continuum where one exists. Then GU at both
resolutions (grading dim 0, form dim 2 and 4), the explicit eta-frame positivity
enumeration (exactly one admissible `C` of 4 and of 16 sign choices), and the
every-candidate guard. Regression test, not a construction of the missing
interacting vacuum.

## Governance

Exploration grade only. No canon or scientific-status change. No cross-repository
identity. bar (b) and H59 remain OPEN.
