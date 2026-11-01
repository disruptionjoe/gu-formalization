---
title: "K2446 Quantitative augmented diagonal and mixed-degree ceiling"
status: active_research
doc_type: exploration
created: "2026-11-01"
classification: CONVENTIONAL_COMPARATOR
target_claim: NONE-NOT-A-KILL
claim_ceiling: "geometric augmented transverse inverse and quadratic-exponential mixed linear bound; no analytic mixed or nonlinear convergence"
---

# K2446 Quantitative augmented diagonal and mixed-degree ceiling

> **GU-COMPARATOR-ROUTING — scope before inference.** This artifact contains or
> borders a conventional particle-physics comparator. Any result about a
> standard Higgs/VEV, ordinary family index or net chirality, SO(10) `126`
> Majorana mechanism, anomaly selector, VEV-only breaking or familiar vector-
> mass route binds only that named model. It is not evidence for or against
> Weinstein's source-native mechanism without an explicit typed bridge. Read
> `lab/methods/source-native-comparator-routing.md` and follow its source-native
> pointers before reusing this result.

Classification: `CONVENTIONAL_COMPARATOR`.

```gu-typed-objects
result: K2446
carrier: original repeated-polar hook fields and raw105 symmetric receivers with seven transverse and seven passive coordinates LAYER=toy CHIRALITY=N/A
pairing: summed ordinary coefficient l1 norm in a fixed adapted coordinate system ON=declared_carrier
real_structure: original real split-metric hooks over the fixed real embedding of Q(sqrt2)
grading: total field degree d and receiver transverse degree k
action_owner: repository-construction -- supplied conditional mathematical model
target: parameter-stable augmented diagonal and finite mixed inverse bound MAP-TYPE=evaluation
```

## Result

[K2443](k2443-hook-quantitative-symbol-2026-11-01.md) supplies a geometric ordinary transverse right inverse. Composing it with the actual scalar-null direction of [K2437](k2437-augmented-compatibility-adjoint-2026-11-01.md) gives a complete augmented transverse diagonal inverse with

    ||B_(k,d)(F,g)||1 <= d C^(k+1)(||F||1+||g||1),           (1)

for one fixed C and compatible ordinary forcing F, arbitrary scalar g. Passive parameter coefficients add no new exponential. On the full ambient-compatible image, the finite mixed recurrence then has the conservative bound

    ||R_d|| <= d^2 max(1,B)^(d-1) d^[3(d-1)] C^(d^2).        (2)

These are existence upper bounds, not necessary growth rates or efficient solver costs. Equation(2) does not prove analytic mixed inversion; it identifies the precise loss that the separate diagonal estimates fail to control. No nonlinear convergence or native GU solution follows. SC-ACT-01/GEO-55 remain ASSERTS at their source scopes; SC-META-53 remains UNCERTAIN. Ledger0.263/source/canon unchanged.

## 1. Actual diagonal, including its normalization

Use K2437's original constant hook h=rep32+(9012/8519)rep55. Direct original contractions give D_E h=0 and

    Jstar_E(h f)=a partial_y1 f+b partial_y2 f,
    a=2253/2, b=2253/17038,

with all343 transverse second-order coefficients zero. The actual degree-d top scalar row is J_d=(4/d)Jstar, not unscaled Jstar. In the single fixed shear u=y1, v=y2-y1/8519, the displayed directional derivative is a partial_u. Let S=a^(-1) I_u with zero integration constant. Ordinary coefficient l1 norm obeys ||S||<=1/a in these adapted coordinates. It acts coefficientwise on passive W polynomials and does not differentiate W.

Let R_k be K2443's ordinary inverse synthesized into the actual degree-(k+1) hook field, with ||R_k||<=C0^(k+1). A fixed finite generator-synthesis constant is absorbed in C0; unused generators may be zero. Define

    B_(k,d)(F,g)=R_k F+h S[(d/4)g-Jstar_E R_k F].            (3)

Then D_E B=F and J_d B=g. These are exact identities, not rank extrapolations. The scalar operator consists of fixed first-order terms plus fixed coefficients of y_t partial_r partial_s. Thus ||Jstar_E V||<=M(k+1)^2||V|| on its degree-(k+1) fields. Equation(3), the fixed norm of h, and ||S||<=1/a prove(1), absorbing polynomial factors and fixed coordinate changes into C. The d factor is necessary in this estimate because it inverts4/d; do not call the estimate independent of total degree.

Multiplication by passive monomials changes none of these constants under the sum of coefficient norms. An active W derivative is different and belongs to the offdiagonal operator below. The fixed shear itself was already available in K2437 and is reused; the new conclusion is the complete ordinary-plus-scalar diagonal estimate and its mixed consumer.

## 2. Mixed-degree elimination and what it actually bounds

Fix total field degree d. Blocks are indexed by receiver transverse degree k=0,...,d-1. Write L=L0+N. The diagonal inverse D stacks(3), so ||D||<=d C^d. Original ambient formulas show D_W raises output E-degree by one relative to the diagonal; Jstar_EW raises it by one and Jstar_WW by two. There are only fixed coefficient banks and at most two derivatives; hence ||N||<=B d^2 for a fixed B in summed actual-field norms.

If an inverse is defined only on its compatible range, extend it by an orthogonal projection in normalized Fischer norms. Coefficient/Fischer conversion costs a fixed exponential in degree, absorbed in C. The K2437 compatibility induction ensures the sequential residuals of ambient-compatible forcing lie in the true diagonal images; extension is only bookkeeping and supplies no extra solvability claim. Each correction preserves the full ambient trace/double-divergence identities; after lower transverse blocks vanish, the leading residual satisfies the transverse compatibility conditions. The scalar residual is unrestricted. This uses the inherited full image theorem, not triangularity alone.

DN strictly raises block index. Therefore (DN)^d=0 and on compatible forcing

    R_d=sum_(j=0)^(d-1) (-DN)^j D.                          (4)

Substituting L0 D=identity on the successive compatible residuals proves the right-inverse identity. Its norm is at most

    d C^d sum_(j=0)^(d-1)(B d^3 C^d)^j,

which is bounded by(2), enlarging C>=1. This is exp(O(d^2+d log d)), not a geometric C1^d estimate. It remains useful for finite-degree conditioning and choosing an ultrafast-decaying forcing class, but cannot make a general analytic forcing series converge.

A sufficient linear-series consequence is explicit: if ambient-compatible forcing for field degree d (receiver degree d-1) has norm at most exp(-A d^2) R^(-d), with A>log C, then(2) makes the resulting preimage series converge on every finite coefficient radius. The negative quadratic dominates d log d and any fixed linear radius term. This restricted entire-forcing statement is linear; it says nothing about closure of the nonlinear recurrence in that forcing class. Constants are existence bounds inherited from K2443, not practical numerical estimates.

## 3. Controls and next decisive question

The original h with passive monomials has nonzero ambient Euler output even though D_E(h f)=0; K2437's actual mixed fixture is reused and directly checked here. Thus the transverse kernel cannot be silently treated as a full ambient kernel. The actual scalar factor4/d is replayed. A finite triangular matrix example validates the algebra of(4), while the abstract diagonal L0=diag(2^(-i)) with unit subdiagonal N has ||N||1=1, geometrically bounded diagonal inverses, and bottom inverse entry2^[d(d-1)/2]. Thus even polynomially bounded offdiagonal coefficients do not turn separate geometric diagonal bounds into a geometric full inverse. That comparison is not a lower bound for the hook system.

K2443's determinant division survives review: degree88 support uses base89 weights, each replacement strictly lowers integer weight, exact divisibility supplies the quotient, and the fixed denominator gives a nonzero leading-coefficient lower bound. No new determinant expansion is needed. Its huge constants and fixed radius loss remain in force.

The next useful step is a bound on the actual products R_(k+1) N R_k retaining directional denominators or cancellations, or another joint inverse construction. Improving the scalar primitive alone or adding finite ranks cannot resolve that. Even a geometric mixed bound would still leave the nonlinear majorant and shared-section realization to prove. The present bound is a proved upper ceiling on one construction, not a divergence verdict.
[Exact probe](../../tests/channel-swings/k2446_augmented_diagonal_estimate_probe.py), [report](../../lab/process/k2446-augmented-diagonal-estimate.json). Written universal proofs and finite exact controls are distinct evidence. Independent internal review is not proof-assistant or external-expert certification.
