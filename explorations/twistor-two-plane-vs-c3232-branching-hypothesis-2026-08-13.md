---
title: "Twistor two-plane versus the C^(32,32) halves: the 2 (x) 16 branching hypothesis, and the bounded computation that would settle it"
status: draft_hypothesis
doc_type: exploration
artifact_type: exploration_result
created: 2026-08-13
target_claim: NONE-NOT-A-KILL
binding: >-
  Binds nothing. No disposition, no verdict, no claim-status, canon, ledger,
  registry, quotient, datum or posture change. The branching identity below is
  PROPOSED and explicitly NOT established; the repository's own C3-prime pass
  records the module-level identification as still owed.
claim_status_change: none
canon_verdict_change: none
public_posture_change: none
---

# The twistor two-plane is not a `C^(32,32)` half — but it may be a factor inside one

Preserved at Joe's direction, 2026-08-13. Records a hypothesis about how Woit's
twistor construction and GU's carrier relate, with confidences and a bounded
decisive computation. **Filed as a hypothesis, not a result.**

## The question

Are the two `C^(32,32)` halves of the GU carrier the twistor two-plane `S_x` and its
quotient `Q_x`?

## Answer: no literally, plausibly yes at the factor level

A "complex two-plane" means `C^2`, four real dimensions. It is not one of the
32-dimensional sectors. The objects line up as:

```text
Full GU carrier:        C^(64,64)                       dim_C 128
                              |
                        ambient chirality
                       /                  \
             Sigma14+ ~ C^(32,32)   Sigma14- ~ C^(32,32)   dim_C 64 each
```

against the twistor construction:

```text
Twistor space:          T = C^4
Spacetime point x:      S_x = C^2 subset T
Quotient:               Q_x = T / S_x = C^2
Tangent at x:           Hom(S_x, Q_x)                   dim_C 4
```

`S_x` and `Q_x` cannot be the two `C^(32,32)` halves: dimensions and
representation types differ.

## The proposed branching

```text
Sigma14^+  ~=  (S_4^+ (x) N_10^+)  (+)  (S_4^- (x) N_10^-)
Sigma14^-  ~=  (S_4^+ (x) N_10^-)  (+)  (S_4^- (x) N_10^+)
```

with `dim_C S_4^{+/-} = 2` and `dim_C N_10^{+/-} = 16`. Each block is
`2 x 16 = 32`, and two blocks make each complex-64 ambient Weyl half.

> **The twistor two-plane is potentially the `C^2` spacetime-spinor factor
> occurring repeatedly inside the `C^(32,32)` carriers; the remaining `C^16` is the
> normal/internal spinor factor.**

```text
C^(32,32) GU Weyl half
        ~=
(C^2 spacetime spinor (x) C^16 internal)
        (+)
(other C^2 chirality (x) other C^16 chirality)
```

## Verification note added on filing

The **algebra-level** factorization is already computed and recorded in this
repository. `explorations/c3prime-split-commutant-certificates-2026-08-12.md`
(five-lens preflight, representation-theory row) states:

> the computed `C (+) C` matches
> `Cl^0(1,3) (x) Cl^0(6,4) = M(2,C) (x) M(16,C) = M(32,C) (+) M(32,C)`,
> acting with one simple summand per chirality half.

So `M(2,C) (x) M(16,C)` is not conjectural — it is the recorded even-Clifford
factorization. **What remains owed is the module-level identification**, i.e.
attaching the `(2_- (x) 16_+) (+) (2_+ (x) 16_-)` labels to the verified conjugate
complex-32 subrepresentations. That raises confidence in the branching bridge above
the 85% estimated below, since the algebra half is done; the open part is the
labelling, not the factorization.

## Two cautions

**1. `S_x` and `Q_x` are not automatically two copies of the same spinor space.**
Intrinsically `T_x M_C = Hom(S_x, Q_x)`. This repository has already proved there is
**no canonical equivariant identification `Q_x -> S_x`**
(`explorations/woit-principles/twistor-grassmannian-kernel-2026-07-24.md`).

**SCOPE DECISION (Joe direct chat, 2026-08-13): the purely right-handed
reinterpretation is NOT adopted, and this caution is therefore not load-bearing
here.** That missing identification obstructs Woit's programme, which needs
`Q_x -> S_x` to rewrite everything in right-handed terms. It does not obstruct the
branching hypothesis in this file, which only needs `Hom(S_x, Q_x)` and is content
for `S` and `Q` to be genuinely different spaces. Dropping the reinterpretation
removes a known obstruction rather than deferring it.

**What is retained from the Woit line after that scoping:** the signature dependence
of spinor conjugation — that conjugation behaves differently in Euclidean and
Lorentzian signature. That is a fact about spinor structures independent of the
right-handed programme, and this session reached it independently in
`explorations/c3c-covariant-constancy-structure-2026-08-13.md` Result 3: the
split-layer complex structure exists iff the 4-block has odd `q`, i.e. exactly for
Lorentzian signature, verified robust across ambient `(7,7)`, `(9,5)`, `(3,11)`,
`(11,3)`, `(5,9)`. The motivating insight survives; the programme that carried it
is not needed.

**2. The `32 + 32` of the Hermitian signature `(32,32)` must not be assumed to be
the two `2 (x) 16` summands.** "Positive versus negative Krein subspace," "ambient
chirality," and "four-dimensional spinor chirality" are **three different
splittings**. Aligning them requires a constructed fundamental symmetry or real
structure, which is not in hand.

## Strongest revised hypothesis

> `U(64,64)` is the large carrier arena. After the `4+10` reduction its Weyl halves
> factor into spacetime twistor-spinor planes tensored with internal 16-dimensional
> normal spinors. The twistor geometry lives primarily in the `C^2` factors, while
> `J10` acts primarily on the internal factor and makes the combined carrier
> complex.

That reconciles the two constructions without identifying unlike objects.

## Confidence (as stated at authorship)

| claim | confidence |
| --- | ---: |
| the literal identification (halves = `S_x` and `Q_x`) is **false** | 99% |
| the standard `2 (x) 16` branching is the correct representation-theoretic bridge | ~85% |
| GU's actual connection, BV quotient and real structure preserve the factorization sufficiently to make it physical | ~55% |

The 55% is the operative number. It is also exactly where the independently filed
`J10` BV / Green-domain descent gate bites: fixed `J10` fails to descend through the
owned ordinary-gauge BRST quotient (8 of 25 selected gauge directions break it),
while moving `J10` is covariant. Any physical use of this factorization inherits
that obstruction.

## The decisive computation, and it is bounded

1. Complete `C3b` by explicitly branching **both** `C^(32,32)` halves under
   `Spin(1,3) x Spin(6,4)`.
2. Construct — or fail to construct — the equivariant bundle identity

```text
Sigma14^{+/-}  <-->  (S (x) N_{+/-})  (+)  (Q (x) N_{-/+})
```

over the twistor correspondence.

If that closes, the "factor inside each large half" reading is correct in the
precise sense above. If it fails, the failure locates exactly which of the three
splittings refuses to align.

## Scope

No identification with quantum superposition follows from anything here. The
branching is a representation-theoretic statement; the physical content depends on
the unbuilt items named in caution 2 and in the 55% row.
