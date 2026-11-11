---
title: "P3: scalar rank tests do not determine a mixed families index"
status: active_research
doc_type: exploration
created: "2026-11-11"
program_target: X-P2-P3
tier: T2
expected_delta: "derive a structural constraint without a full-C decision"
actual_delta: "constrained: mixed odd fibre and parameter classes survive all pointwise scalar index checks"
classification: INTERNAL_STRUCTURAL_ONLY
target_claim: NONE-NOT-A-KILL
claim_ceiling: "No source verdict, class-C exclusion, realized physical count or action witness"
scripts:
  - tests/program-focus/p3_family_index_mixed_twist_probe.py
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
result: p3-family-index-mixed-twist
carrier: F=RP3 x R7 and parameter B=T2; product-oriented proper-support complex K pushforward LAYER=UNTYPED (structural mathematics, not identified physical states) CHIRALITY=N/A
pairing: explicit topological pushforward or symbol composition ON=declared_carrier
real_structure: real metric geometry with complex K or Clifford modules; no physical reality transport
grading: K parity and symbol source/target grading are explicit; no multiplicity-to-count inference
action_owner: N/A -- structural subfamily requirement, no action constructed
target: X-P2-P3 MAP-TYPE=pushforward
```

## Native bookends

program_target: X-P2-P3
tier: T2
expected_delta: derive a structural constraint without a full-C decision
actual_delta: constrained: mixed odd fibre and parameter classes survive all pointwise scalar index checks

## 1. A complete mixed-product calculation

Use the [prior fibre topology](x-d1-p3-three-local-floor-2026-11-11.md), with M=RP³ and F=M x R7. Let x in K^1(M) pair to1
under the chosen odd Spin-c orientation (normalize via the degree-one collapse
RP³->S³ and its top AHSS filtration) and beta in K_c^1(R7) be Bott-normalized.
Put alpha=x beta, so p_!alpha=1. Ordinary K^0(M)=Z+Z/2 has torsion eta with
2eta=eta²=eta x=0; x²=0 by AHSS filtration. For B=T², K^*(B) is the exterior
ring on odd circle generators a,b; ab generates reduced K^0(B).

The torsion-free base K groups make the product Künneth sequence split without
Tor ambiguity. Every even supported coefficient xi and ordinary even twist W
have the forms

    xi = alpha A + beta B1 + eta beta C,
    W  = u + eta v + x w,

where A,u,v lie in K^0(B), and B1,C,w lie in K^1(B); the torsion coefficients v and C
are understood modulo2. Graded products and the fibre pushforward give

    pi_!xi = A,
    pi_!(xi W) = A u + B1 w.

Proof: alpha x=0, eta alpha=0, eta x=0. The mixed term beta B1 x w equals
x beta B1 w: moving x past B1 and beta produces two minus signs. Terms with
eta are killed by the torsion-free output K^0(T²); terms beta times base-odd
have zero pushforward because p_! beta belongs to K^1(point)=0.
This proves the whole product formula, not merely one numerical example.
The tools are [Hatcher's products and Bott theory](https://pi.math.cornell.edu/~hatcher/VBKT/VB.pdf)
and the usual topological pushforward/product structure (see also
[Bunke–Schick's index/pushforward treatment](https://arxiv.org/abs/0707.0046)).
The special formula is derived here from the stated groups, not quoted as a theorem
about native GU families.

## 2. Countercontrol and actual-bundle repair

Take xi=beta a and W=x b. Then rank W=0, pi_!xi=0, yet

    pi_!(xi W)=ab != 0.

Its degree-two Chern character integrates to1 on the oriented parameter torus.
Every restriction to a parameter point gives numeric index0; pointwise equality
therefore misses a nontrivial integral family class. This is a fixed coefficient
and fixed twist, with no parameter-by-parameter refit.

The effect does not depend on allowing rank-zero virtual bundles as actual
fields. On the compact finite CW space M x T², choose N large enough that N+W
is represented by an actual complex bundle E: represent W as E1-E2 and add a
complement E2' with E2+E2' trivial. Then E=E1+E2', rank N, has stably trivial
rank-N restrictions to each fibre, but

    pi_!(xi E)=ab != N pi_!xi=0.

No canonical small N, class-C representation, connection, action or analytic
operator is asserted. The support of xi is compact in R7 and proper over the
compact base. W need not have compact support; multiplication is well-defined.

## 3. Exact condition for the rank-only repair

If W is pulled back solely from F with constant rank r, then w=0 and u=r,
so the numerical rank-only rule extends to the whole family. For a general
mixed W the difference from r pi_!xi is

    A(u-r) + B1 w.

It vanishes for all supported xi iff u=r and w=0: choose A=1,B1=0 to fix u;
then B1=a,b independently detect both coefficients of w in the unimodular
exterior pairing on T². The eta v term is invisible here. This is an exact
classification for this product base, not a universal families theorem.
The scalar rank theorem therefore survives on its original domain and has a
precise stronger hypothesis for this family setting.

## 4. Consuming requirement and preserved boundaries

X-P2-P3 remains constrained. Any attempted phase-to-index argument using only
pointwise numeric indices must state whether the desired conclusion is an
integer on each fibre or a global K^0(B) class. For the latter, the fixed-domain
phase argument must be promoted to a continuous Fredholm family on compatible
bundles; arbitrary mixed twists are not scalar phase rescalings. This result
neither contradicts the existing fixed-family homotopy invariance nor constructs
a phase-changing GU action. It specifies the mixed topological term that a
proposed structural index bridge must control.

F is the parameter base of the older K3 interface, while it is the integration
fibre of this declared topological control. These roles are deliberately distinct.
All three artifacts leave the K3-family symbol, APS/observation descent and
physical interpretation open. In particular ab is a parameter-space K class,
not three particles or three observed generations.

## Reproduction and acceptance

[Exact supporting probe](../../tests/program-focus/p3_family_index_mixed_twist_probe.py)
and [replay report](../../lab/process/p3-family-index-mixed-twist.json) accompany the written proof.
Finite checks test algebra and contrary controls; they do not certify topology,
all differential operators, physical applicability or an analytic APS family.
Independent internal specialist review and an integrated adversarial review
completed with all substantive findings resolved; saved exact reports replay. No Lean certification is claimed for this T2 result.
