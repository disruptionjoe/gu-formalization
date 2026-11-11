---
title: 'P3: all lower-order lifts of the exterior symbol pair'
status: active_research
doc_type: exploration
created: '2026-11-11'
program_target: P3xorder_locality
tier: T2
expected_delta: derive a structural-subfamily constraint; no full-C decision
actual_delta: 'constrained: fixed exterior principal symbols have a unique lower-order
  completion, with typed curvature and parameter-domain conditions'
classification: INTERNAL_STRUCTURAL_ONLY
target_claim: NONE-NOT-A-KILL
claim_ceiling: No class-C witness or exclusion, source verdict, physical state or
  generation count
scripts:
- tests/program-focus/p3_exterior_symbol_lift_probe.py
---

> **GU-COMPARATOR-ROUTING — scope before inference.** This artifact contains or
> borders a conventional particle-physics comparator. Any result about a
> standard Higgs/VEV, ordinary family index or net chirality, SO(10) `126`
> Majorana mechanism, anomaly selector, VEV-only breaking or familiar vector-
> mass route binds only that named model. It is not evidence for or against
> Weinstein's source-native mechanism without an explicit typed bridge. Read
> `lab/methods/source-native-comparator-routing.md` and follow its source-native
> pointers before reusing this result.

Classification: `INTERNAL_STRUCTURAL_ONLY`. No conventional-index conclusion is
transported to the native two-true-plus-effective-imposter observation construction.
SC-GEN-02/03/54 ASSERTS the native generation/supercharge claims; SC-CHI-01/51 ASSERTS
the nonchiral-total/effectively-chiral split with the source's stated qualifications.
This note does not adjudicate those claims. RA-F1, AC-F1 and LT-SM8 remain NEEDS.

```gu-typed-objects
result: p3-exterior-symbol-lift
carrier: smooth finite-rank bundles and explicitly defined compatibility or Hilbert complexes LAYER=UNTYPED (no physical identification) CHIRALITY=N/A
pairing: auxiliary Hermitian Hilbert pairing where used ON=declared_carrier
real_structure: real or complex coefficient bundles as stated; complex family K theory only
grading: complex degree, optional commuting internal grading; not physical chirality
action_owner: N/A -- structural subfamily theorem, no action constructed
target: P3xorder_locality MAP-TYPE=homomorphism
```

## Native bookends

program_target: P3xorder_locality
tier: T2
expected_delta: derive a structural-subfamily constraint; no full-C decision
actual_delta: constrained: fixed exterior principal symbols have a unique lower-order completion, with typed curvature and parameter-domain conditions

## Question and exact new scope

For any candidate whose compatibility sequence has the exterior principal
symbols below, which lower-order coefficients can turn its symbol identity into
an actual differential identity on arbitrary parameters? This class is fixed by
its representation and differential symbols, not by an action or a fitted set
of coefficients. It supplies a conditional requirement on C subfamilies that use
such a factor. Class C's order bounds do not require this factor.

The [prior local gauge result](p3-rs-local-gauge-necessity-2026-11-11.md) supplies
the generic-invertibility necessity. [K132](selected-k132-native-i1b-t0-all-grade-noether-complex-2026-08-16.md) already records curvature failure of
a covariant differential, while [K133](selected-k133-native-i1b-t0-flat-complex-kappa-pencil-2026-08-16.md) shows flatness alone does not repair the
actual Shiab symbol. We do not rerun those conclusions. The new endpoint is an
exhaustive classification of *every* zero-order completion at these fixed
leading symbols, followed by a restricted-parameter and global descent test.
H below is a compatibility operator from one-forms to two-forms, generally not
a square Euler Hessian. It is not the complete projected RS/ghost/BV complex.

## 1. Complete local lift classification

Let E be a smooth real or complex rank-r vector bundle over a smooth n-dimensional
base, n>=2. In a coordinate chart and bundle frame fix

    (R f)_i = partial_i f + A_i f,
    (H alpha)_ij = partial_i alpha_j - partial_j alpha_i
                   + sum_k B_ij^k alpha_k,       i<j.

A and B are arbitrary smooth matrix coefficients. These expressions describe
ALL first-order maps with the specified principal symbols, with no order-zero
coefficient omitted. Expanding H R gives the coefficient of partial_k f:

    A_j delta_ik - A_i delta_jk + B_ij^k.

At each point, a compactly supported smooth f can have arbitrary value and
first jet. Hence HR=0 for all f forces, uniquely,

    B_ij^k = A_i delta_jk - A_j delta_ik.

The remaining coefficient is

    F_ij = partial_i A_j - partial_j A_i + [A_i,A_j].

Conversely these equations make every coefficient zero. Thus the full identity
holds iff H=d_A on one-forms and F_A=0. There is no alternative zero-order
correction to H that absorbs nonzero F while keeping R and both principal
symbols fixed. Smooth coefficients suffice; there is no analytic-coefficient,
metric, signature, positivity or integration-by-parts assumption.

This is not a flatness requirement for all gauge theories. For example the
known Yang--Mills detour complex has a different middle operator and closes on
Yang--Mills connections, including nonflat ones. That result is already used in
the native [total-current gate](selected-k77-total-twisted-yang-mills-current-gate-2026-08-14.md);
see also [Gover--Somberg--Soucek](https://arxiv.org/abs/math/0606401).
It changes the operator category and does not evade the classification above.

## 2. General first-order audit and controls

For arbitrary compatible first-order matrix maps R=sum_j r^j partial_j+r0,
H=sum_i h^i partial_i+h0, the complete HR=0 conditions are:

    h^i r^i=0 and h^i r^j+h^j r^i=0 (i<j),
    sum_i h^i partial_i r^j + h^j r0 + h0 r^j=0 (each j),
    sum_i h^i partial_i r0 + h0 r0=0.

These follow by the product rule and independent jets, and are sufficient by
the same expansion. A null leading symbol supplies only the first line. This
formula is a reusable audit, not a claim to classify all its matrix solutions.
Mixed-order Hessians need their own weighted convention.

Supporting controls include a nonconstant flat rank-two connection obtained
from an explicit frame, a scalar nonflat connection with an unchanged principal
symbol, and arbitrary independent first jets. They test actual compositions
rather than assertions copied from a report. The exhaustive proof is the
coefficient matching in section 1, not the number of sampled matrices.

## 3. Released restricted-parameter successor

Freeze the completed d_A and an injection J:S->E. The truncated sequence

    Gamma(S) --d_A J--> Omega1(E) --d_A--> Omega2(E)

is a complex iff F_A J=0. Indeed d_A²(J epsilon)=F_A J epsilon; no derivative
of J remains. A nonparallel curvature-kernel subbundle CAN therefore supply
this truncated sequence. It does not supply the full S-valued exterior complex.
For d_A to map Omega^k(S) into Omega^(k+1)(S), S must also be connection-preserved;
then the induced S connection must be flat for the full sequence.

An exact two-dimensional control separates these claims. Put S=span(e1) in E=R²,
N=E21, P=diag(0,1), A_x=N and A_y=x P+(x²/2)N. Then

    F_xy=P,   F_xy e1=0,   nabla_x e1=e2 outside S.

Thus the truncated identity holds for arbitrary scalar parameter functions,
although the S-valued complex does not close. This is a contrary control to
overbroad parameter-preservation wording, not a guessed action. If H itself
is allowed to change after restricting parameters, section 1's uniqueness no
longer follows: only the jets reached by d_A J are tested. That is a separate
classification, not an unspoken extension of the theorem.

In this control no nonzero parallel flat coefficient subbundle exists: any
such subbundle must lie in ker F=S, hence must equal S locally, which fails
preservation. Equivalently (nabla_x F)e1=[N,P]e1=-e2. Thus even a constant-rank
curvature kernel is not enough for a full flat coefficient subcomplex, while
the truncated identity survives.

## 4. Global flatness is not an untwisted parameter frame

R with identity gradient symbol is a connection; the unique H and its curvature
transform covariantly on overlaps. Flatness therefore gives the global E-valued
complex. On a connected base it gives a global parallel frame iff its holonomy
representation is trivial. Proof: parallel transport of a basis is independent
of path exactly when every based loop fixes that basis. Flatness only supplies
local path independence on simply connected patches.

For a rank-one unitary connection on the two-torus, A=i/2 dtheta, F=0 but the
theta-loop holonomy is exp(-i*pi)=-1. Local parallel sections exist; there is
no nonzero global parallel section. This does NOT mean global smooth sections
or arbitrary gauge-parameter sections are absent. The underlying line bundle
is trivial, while its flat connection is not gauge-equivalent to the trivial
one by a single-valued parallel frame. This control prevents local-flatness
evidence from identifying the global parameter space or its zero modes.

## Matrix consequence

P3xorder_locality gains the all-completion criterion at this stated symbol
category. P3xvariational retains its actual coupled-Hessian/BV burden: it must
check all lower orders and the true parameter domain, rather than inserting a
ghost subtraction from a symbol nullspace. No stabilized action, full-C
flatness theorem, nonlinear gauge closure, physical cohomology, positive state,
source-family count or ledger movement follows. Both Clifford-signature horns
remain unselected; the proof is signature-independent compatibility algebra.

## Reproduction and acceptance

Run [the exact probe](../../tests/program-focus/p3_exterior_symbol_lift_probe.py). Its [saved report](../../lab/process/p3-exterior-symbol-lift.json)
contains supporting identities and contrary controls, not a numerical proof of
all smooth operators or Hilbert families. Universal statements above have written
proofs; independent internal specialist and hostile reviews completed with substantive findings empty. No Lean
or external-expert certification is claimed for this Tier-2 result.
