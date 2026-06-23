---
title: "Type II_1 OQ1: J^2 on the Section Pullback s^*(S)"
status: exploration
doc_type: research_note
updated_at: "2026-06-23"
problem_label: "type-ii1-oq1-j2-section-pullback"
verdict: "SIGN_REMAINS_MINUS_ONE"
---

# Type II_1 OQ1: J^2 on the Section Pullback s^*(S)

## 1. Problem

Run OQ1 from `explorations/type-ii1-sm-checklist-tightening-2026-06-23.md`:

```text
Compute J^2 on s^*(S) over X^4 for the GU quaternionic J.
Does J^2 change sign under section pullback?
```

The gate is FX.1 in the Type II_1 checklist. The CC finite Standard Model control
requires a KO-dim 6 real structure with:

```text
J^2 = +1.
```

The GU source data have:

```text
Cl(9,5) ~= M(64,H),
S = H^64,
J_GU^2 = -1
```

where `J_GU` is the quaternionic structure on the spinor module.

## 2. Local Sources Read

- `explorations/type-ii1-sm-checklist-tightening-2026-06-23.md`
- `explorations/signed-readout-oq2a-k-theory-lift-2026-06-23.md`
- `explorations/n1-signature-audit-y14-clifford-algebra-2026-06-22.md`
- `explorations/n2-shiab-computation-spin77-branching-rules-2026-06-22.md`
- `explorations/sc1-shiab-domain-codomain-2026-06-23.md`
- `explorations/sc1-oq1-shiab-uniqueness-2026-06-23.md`
- `explorations/4d-reduction-section-pullback-2026-06-22.md`
- `explorations/codazzi-sp64-bundle-2026-06-23.md`
- `explorations/codazzi-sp64-2026-06-23.md`
- `explorations/vz-schur-complement-2026-06-23.md`
- `explorations/vz-oq1-sr-squared-identity-2026-06-23.md`
- `explorations/vz-subprincipal-symbol-rs-2026-06-23.md`

## 3. Assumptions

**A1. GU J.** The operator being pulled back is the GU quaternionic structure named in
the Type II_1 checklist and signed-readout K-theory note. Fiberwise, it is right
multiplication by a fixed unit imaginary quaternion, or the equivalent pseudoreal
complex antiunitary presentation. In both cases:

```text
J_GU^2 = -Id_S.
```

**A2. Ordinary section pullback.** The pullback is the standard bundle pullback along
a section:

```text
s: X^4 -> Y^14,
s^*(S)_x = S_{s(x)}.
```

For a bundle endomorphism `J: S -> S`, the pulled-back endomorphism is:

```text
(s^*J)_x = J_{s(x)}: S_{s(x)} -> S_{s(x)}.
```

**A3. No extra operator is silently inserted.** The computation is for `s^*(J_GU)`,
not for a newly defined real structure such as `K s^*(J_GU)` using a horizontal
chirality, complex conjugation, quotient, or extra charge-conjugation operator.

**A4. The section may change the Dirac operator, not the algebraic square of J.**
The section pullback introduces horizontal/vertical splitting, `II_s`, Codazzi
corrections, and lower-order Shiab/curvature terms. These affect `s^*(D_GU)` and the
4D field equations, but they do not by themselves change the fiberwise endomorphism
identity satisfied by `J_GU`.

## 4. Computation

Let `S -> Y^14` be the GU spinor bundle with fiber `H^64`. Let:

```text
J_GU: S -> S
```

be the quaternionic structure. The established local data give:

```text
J_GU^2 = -Id_S.
```

Pull back this identity along `s`. Pullback is functorial, so it preserves
composition and identity maps:

```text
s^*(J_GU^2) = s^*(J_GU o J_GU)
            = s^*(J_GU) o s^*(J_GU),

s^*(-Id_S) = -Id_{s^*(S)}.
```

Therefore:

```text
(s^*J_GU)^2 = -Id_{s^*(S)}.
```

Fiberwise, for `x in X^4` and `psi in s^*(S)_x = S_{s(x)}`:

```text
((s^*J_GU)^2 psi)
  = J_{s(x)}(J_{s(x)} psi)
  = -psi.
```

So the sign remains negative pointwise on every pulled-back fiber.

### 4.1 Branching Check

The 4D reduction note branches the pulled-back spinor as:

```text
s^*(S) ~= S(3,1) tensor_R S(6,4)
```

with the underlying GU module still carrying the right-H structure inherited from
`S = H^64`. Any H-linear identification of `s^*(S)` with this branched model only
conjugates the pulled-back operator:

```text
J_branch = T (s^*J_GU) T^{-1}.
```

Conjugation preserves the square:

```text
J_branch^2 = T (s^*J_GU)^2 T^{-1}
           = -Id.
```

Thus the spinor branching under the section does not convert the quaternionic
structure into an involution.

### 4.2 Projection and Constraint Check

The SC1 and VZ notes use H-linear Clifford contraction, gamma-trace projections,
RS blocks, and Schur complements. These structures can restrict or couple sectors,
but they do not flip `J^2`.

If a subbundle `E subset s^*(S)` is preserved by `s^*J_GU`, then the restricted
operator still satisfies:

```text
(s^*J_GU|_E)^2 = -Id_E.
```

If the subbundle is not preserved by `s^*J_GU`, then `s^*J_GU` does not descend to
that subbundle or quotient as a well-defined operator. That is not a sign flip; it
is loss of an induced `J`.

### 4.3 How a Plus Sign Could Be Engineered

One could define a new operator:

```text
J_new = K s^*(J_GU)
```

where `K` is an additional endomorphism with `K^2 = -1` commuting with `s^*(J_GU)`.
Then:

```text
J_new^2 = K^2 (s^*J_GU)^2 = (+1) Id.
```

But this is not the section pullback of the GU quaternionic `J`. It is a twisted
real structure requiring new input. It would need its own checks:

```text
J_new^2 = +1,
J_new D = D J_new,
J_new gamma = - gamma J_new,
order-zero/order-one compatibility,
compatibility with the Sp(64) and KSp structures.
```

Without that extra construction, the FX.1 computation has a binary result:

```text
(s^*J_GU)^2 = -1.
```

## 5. Verdict

**Verdict: SIGN_REMAINS_MINUS_ONE.**

The ordinary section pullback cannot change:

```text
J_GU^2 = -1
```

into:

```text
J^2 = +1.
```

The reason is purely functorial: pullback preserves composition and identity maps.
The section can change the operator `D_GU` through horizontal/vertical splitting,
`II_s`, Codazzi residuals, and lower-order curvature terms, but it does not alter
the fiberwise square of the pulled-back quaternionic structure.

Therefore FX.1 resolves negatively for CC KO-dim 6 compatibility by section pullback
alone:

```text
(s^*J_GU)^2 = -Id_{s^*(S)}.
```

The GU/Type II_1 contact remains in the quaternionic/KSp lane:

```text
KSp^0(X^4) = KO^4(X^4),
```

not the CC finite-model KO-dim 6 lane.

## 6. Failure Conditions

**F1. Nonstandard pullback.** If future notes redefine `s^*(S)` not as the ordinary
pullback bundle but as a quotient, real form, or selected complex subbundle, then this
note no longer applies directly. In that case the induced operator must be specified
from scratch.

**F2. Different J.** If the operator called `J` is not the GU quaternionic structure
but a new charge-conjugation operator, its square may differ. That would be a new
construction, not the pullback of `J_GU`.

**F3. H-structure broken.** If the pulled-back spinor bundle loses the global right-H
module structure because the transition functions cease to be Sp(64)/H-linear, then
`s^*J_GU` may fail to be globally defined. This would not produce `J^2=+1`; it would
remove the pulled-back quaternionic structure.

**F4. Twisted real structure.** A deliberately twisted operator `K s^*(J_GU)` can be
made to square to `+1` if `K^2=-1` and the commutation signs are favorable. This is a
separate KO-dim 6 proposal and must pass the full sign triple and order-one tests.

## 7. Next Action

Treat OQ1/FX.1 as resolved for the literal GU section pullback:

```text
s^*(J_GU)^2 = -1.
```

Do not use section pullback alone as the KO-dim 6 bridge. The next viable Type II_1
contact test is either:

1. Work in the KSp/KO^4 lane and compare a Type II_1 Breuer-Fredholm index to the
   GU `KSp^0` class; or
2. Propose an explicit twisted real structure `J_new` and run the full KO-dim 6 sign
   triple plus order-zero/order-one checks.
