---
title: "P3: supported fibre index, boundary clutching and RS symbol type"
status: active_research
doc_type: exploration
created: "2026-11-11"
program_target: P3xglobal_index
tier: T2
expected_delta: "derive a structural constraint without a full-C decision"
actual_delta: "constrained: support and admissible symbol image, not two-primary torsion, control the index residue"
classification: INTERNAL_STRUCTURAL_ONLY
target_claim: NONE-NOT-A-KILL
claim_ceiling: "No source verdict, class-C exclusion, realized physical count or action witness"
scripts:
  - tests/program-focus/p3_metric_fibre_supported_index_probe.py
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
result: p3-metric-fibre-supported-index
carrier: F=RP3 x R7 with chosen compatible Spin-c orientation; ordinary and compact-support complex K groups LAYER=UNTYPED (structural mathematics, not identified physical states) CHIRALITY=N/A
pairing: explicit topological pushforward or symbol composition ON=declared_carrier
real_structure: real metric geometry with complex K or Clifford modules; no physical reality transport
grading: K parity and symbol source/target grading are explicit; no multiplicity-to-count inference
action_owner: N/A -- structural subfamily requirement, no action constructed
target: P3xglobal_index MAP-TYPE=pushforward
```

## Native bookends

program_target: P3xglobal_index
tier: T2
expected_delta: derive a structural constraint without a full-C decision
actual_delta: constrained: support and admissible symbol image, not two-primary torsion, control the index residue

## 1. Existing geometry, new index question

Reuse the complete quaternionic proof in
[X-D1-P3](x-d1-p3-three-local-floor-2026-11-11.md): the Lorentz metric fibre
F=GL(4,R)/O(3,1) is the total space of E=R+Sym²Q over RP³, and E is noncanonically
trivial of rank7. Since RP³=SO(3) is a Lie group, TF is trivial of rank10.
The auxiliary positive metric used to prove this is not the native DeWitt metric.

Fix a product Spin-c orientation. Existing Bott/AHSS calculations give

    K^0(F)=Z + Z/2,  K^1(F)=Z,
    K_c^0(F)=Z,       K_c^1(F)=Z + Z/2.

Write eta=[L_C]-1 for the ordinary torsion class. For k in K_c^0(F),
2 eta k=0; torsion-freeness forces eta k=0. Every W in K^0(F) therefore acts by

    W k = rank(W) k.

The compact-support pushforward I:K_c^0(F)->Z is surjective. An oriented embedded
coordinate ball R^10 has its Bott coefficient generator; extension by zero and
index excision give I(j_! beta10)=1 with compatible orientations. Equivalently,
let x generate K^1(RP³), normalized by the odd Spin-c pairing1, and beta7 generate
K_c^1(R^7); alpha=x beta7 generates K_c^0(F), I(alpha)=1. The x normalization
follows from a degree-one collapse RP³->S³ and the top AHSS filtration.
Thus I(W k)=rank(W) I(k); the values of unrestricted compact-support classes are
not forced into3Z by the ordinary two-primary torsion.

This is a topological compact-support pairing, not a constructed differential
operator on F. To use it as an analytic index, a symbol Thom identification and
an appropriate relative/Fredholm realization are separate inputs.
[Atiyah–Singer I, index/excision normalization](https://math.uchicago.edu/~shmuel/tom-readings/ASI.pdf)
and [Carey–Wang, Thom and pushforward](https://arxiv.org/html/math/0507414v4)
supply these standard K-theoretic tools; the application to this F is the argument above.

## 2. Executed consequence: what support remembers

Set M=RP³ x D7 and N=RP³ x S6. Under the Bott splitting,
K^1(M)=Z, K^1(N)=Z², K^0(M,N)=Z. Choose the reduced S6 Bott generator so that
in the exact pair sequence

    Z --i--> Z² --delta--> Z --forget--> Z+Z/2
    i(a)=(a,0), delta(a,b)=b, forget(k)=0.

Indeed restriction from the disk factor lands in the constant S6 summand.
The connecting map is the relative disk Bott map on the reduced summand;
its surjectivity forces forget=0. This is the product form of the exact pair
sequence in [Hatcher, §2.2](https://pi.math.cornell.edu/~hatcher/VBKT/VB.pdf).
The free integer is boundary clutching information, entirely invisible after
forgetting support. It is not an automatically selected APS spectral section.

If the image generated by an actual admissible symbol/domain category is dZ,
then twisting by rank r has generated numeric image rdZ. Universal divisibility
by3 is equivalent to3 dividing rd (including d=0). No value of d is inferred here.
This replaces a vague topology obstruction with an exact missing image problem.
It does not assert that admissible objects are closed under every K-group operation.

## 3. RS classes are not interchangeable

The native [June symbol-index calculation](../generation-sector/generation-count-rs-k3-symbol-index-attempt-2026-06-24.md)
already distinguishes the full vector-spinor Dirac class T_C, raw gamma-trace-free
geometric RS class T_C+1, and conditional two-ghost class T_C-1. The sign is not
inferred from bundle rank: gamma trace exchanges chirality,
T_C tensor S^± = R^± + S^∓, and the geometric elliptic symbol theorem supplies
T_C+1. [Richtsfeld, equation5.3](https://link.springer.com/article/10.1007/s10455-026-10043-6)
is an independent primary reference for that raw RS index formula.

For declared vertical Dirac coefficient models the rank multipliers are:

| coefficient rank n | full n | raw-shaped n+1 | two-ghost-shaped n-1 |
|---|---:|---:|---:|
|10|10|11|9|
|14|14|15|13|

These entries are coefficient models, not six admitted GU operators. The n=10
raw elliptic RS model needs a Riemannian symbol interpretation; the native
indefinite metric does not automatically provide it. The n=14 row is merely a
rank14 coefficient twisting a vertical Dirac class. It is not the restriction
of the14-dimensional chiral RS symbol: ambient spinors restrict with both
vertical chiralities and opposite spectator spinors, so grading can cancel.
The ghost subtraction needs its own gauge complex, discussed in
[local gauge necessity](p3-rs-local-gauge-necessity-2026-11-11.md).

## 4. Native family-interface consequence

In [the source-action interface](../../canon/source-action-family-index-interface-SPEC.md),
a K3-fibered family has F as its parameter BASE. Its first family index lies in
K^0(F). That is distinct from a coefficient in K_c^0(F), a symbol in K_c^0(T*F),
and a further integration over F. The extra support/Thom/analytic operation must
be specified before using this calculation. No K3 family, boundary connection,
APS domain or source action is built.

P3xglobal_index becomes constrained, retaining the original analytic gate as an
unfulfilled realization requirement. The derived requirement is to identify the
actual symbol class and its admissible relative image. Neither a two-datum floor,
a physical count, nor any full-C decision follows. The separate
[mixed-family test](p3-family-index-mixed-twist-2026-11-11.md) checks the tempting
extension of rank-only scalar factorization to parameterized families.

## Reproduction and acceptance

[Exact supporting probe](../../tests/program-focus/p3_metric_fibre_supported_index_probe.py)
and [replay report](../../lab/process/p3-metric-fibre-supported-index.json) accompany the written proof.
Finite checks test algebra and contrary controls; they do not certify topology,
all differential operators, physical applicability or an analytic APS family.
Independent internal specialist review and an integrated adversarial review
completed with all substantive findings resolved; saved exact reports replay. No Lean certification is claimed for this T2 result.
