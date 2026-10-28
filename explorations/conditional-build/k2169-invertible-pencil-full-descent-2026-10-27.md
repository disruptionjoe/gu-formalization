---
title: "K2169 Invertible pencils and complete mixed-port descent"
status: active_research
doc_type: exploration
created: "2026-10-27"
classification: BRIDGE_OR_SEMANTIC_BOUNDARY
target_claim: NONE-NOT-A-KILL
claim_ceiling: normalized zero-order adapters for the declared fixed-splitting coupled operator; no source or physical quotient claim
scripts:
  - tests/channel-swings/k2169_invertible_pencil_full_descent_probe.py
---

# K2169 Invertible pencils and complete mixed-port descent

> **GU-COMPARATOR-ROUTING: scope before inference.** This artifact contains or
> borders a conventional particle-physics comparator. Any result about a
> standard Higgs/VEV, ordinary family index or net chirality, SO(10) `126`
> Majorana mechanism, anomaly selector, VEV-only breaking or familiar vector-
> mass route binds only that named model. It is not evidence for or against
> Weinstein's source-native mechanism without an explicit typed bridge. Read
> `lab/methods/source-native-comparator-routing.md` and follow its source-native
> pointers before reusing this result.

Classification: `BRIDGE_OR_SEMANTIC_BOUNDARY`.

```gu-typed-objects
result: K2169 universal singular-pencil exclusion, full reduced equations and tangential adapter rigidity
carrier: full real Cl77 S128 vector-spinor plus scalar, W(3,1) and N(4,6) fixed LAYER=observed CHIRALITY=S-FULL-DIRAC
pairing: algebraic field-equation evaluation; no physical Hilbert pairing ON=declared_carrier
real_structure: real Clifford representation and independently supplied common reverse row
grading: full Dirac; tangent and normal exterior degrees are bookkeeping
action_owner: repository-construction: simple-contraction coupled operator and its fixed four-dimensional target
target: complete normalized zero-order principal and coefficient intertwiners MAP-TYPE=intertwiner
```

## Result and scope

Every nonzero even-tangent seven-form port that can pass the necessary normalized
adapter equations has an **invertible complex pencil**. Singular pencils cannot hide
solutions. The adapters are unique; the entire frozen mixed problem reduces to ten
explicit normal-Clifford equations in the240 real coefficients of the port. Smooth
fixed-geometry descent additionally forces the adapters to be constant in every
tangential direction. These conclusions do NOT exclude every genuinely mixed port.

[K2167](k2167-mixed-port-complete-adapters-2026-10-27.md) already excludes Z2 and all
pure tangent degrees; its complementary-coordinate mixed family is also excluded.
Those results are reused. Here both normal7 v and normal3 u may be nondecomposable,
singular individually, and noncommuting. No scalar-square hypothesis is imposed.

SC-OP-04 ASSERTS candidate four-independent-field grammar, not this chosen common
reverse, contraction, normalization or target. SC-GEO-55 ASSERTS displacement from
gauge-rotated Levi-Civita, not ordinary torsion. Full source16cell/full20/K-C descent,
source admissibility, native2+1/chirality, a physical quotient and GU remain unproved.
LT-SM8/LT-GR6b/AC-F1, source, ledger and canon are unchanged. Layer0 keeps the fixed
Cl77 W(3,1)+N(4,6) full real Dirac model distinct from source geometry and physical
Hilbert space; no new substrate or L1--L7 physical completion is claimed.

## 1. Singular-pencil classification

Let D=Cl(N)_C, omega=gamma0 gamma1 gamma2 gamma7, omega²=-1. The subalgebra
Cl(N)+omega Cl(N) is isomorphic to D by omega -> i. Real conjugation fixes Cl(N)
and sends i to -i. Set

    Z=v+omega u,  v in Lambda7 N real, u in Lambda3 N real,
    P=7v-15iu, R=v+3iu, C_j=A_j+iB_j.

K2167's complete necessary equations are exactly

    P C_j = -eta_j d_j R, j in N.                         (1)

Here d_j is algebraic metric contraction, NOT a coordinate derivative. For nonzero
Z, (1) is solvable iff P is invertible, with unique solution

    C_j=-eta_j P^-1 d_jR.                                 (2)

To prove necessity let I=P D. Equation(1) puts every d_jR in I. RIGHT Euler contraction
is sum_j eta_j(d_jR)gamma_j=7v+9iu. Subtract P to obtain24iu in I, so u,v belong to I
and I=vD+uD. Thus bar(P)D is contained in I. Conjugation preserves complex dimension,
so bar(P)D=PD. Conjugating the derivative relations now also gives d_j bar(R) in I.
The odd-form Clifford identity gamma_jR=2d_jR-R gamma_j, and its conjugate, imply
both gamma_jv and gamma_ju belong to I. Therefore I=vD+uD is a two-sided ideal.
D is the simple algebra Mat32(C); nonzero Z makes P and I nonzero, hence I=D.
Finite dimensionality then makes P invertible. Sufficiency is immediate from(2).

Do not replace the conjugate-ideal step with the unsupported assertion RD=PD.
Simplicity can also be checked with the1024 distinct joint conjugation characters
of normal Clifford blades, as in K2167. The probe checks that projection instrument;
the written ideal argument, rather than a finite sample, proves the universal claim.

P is odd and its inverse is odd, while d_jR is even. Hence each C_j is odd and
kappa(T_j) corresponds to -bar(C_j). This fact is essential in the full lower row.
The theorem excludes singular P but does not require v or u individually invertible.

## 2. Full lower equation after eliminating every adapter

Write z=v+iu, D_i=d_i z. Preserve the product order in the original maps. On kernel
column j, direct substitution into K2167's E,F gives

    F^j=4iu C_j-eta_j D_j,
    E_i^j=7z delta_ij+2d_i bar(R) C_j+eta_j[D_i,gamma_j], i in N.

The complete remaining lower equation is

    q_j=4iu C_j-eta_jD_j+7bar(C_j)z
        +2 sum_i bar(C_i)d_i bar(R) C_j
        +eta_j sum_i bar(C_i)[D_i,gamma_j] = 0.             (3)

For example the normal upper formula follows by separating the four tangent terms
in sum eta_l gamma_l a_i zeta_l; their conjugation changes z to bar(z), producing
d_i z-4i d_i u=d_i bar(R). No commuting of a general normal coefficient is allowed.
Equation(1) makes E_mu-gamma_mu F vanish. After equation projection, each remaining
upper row equals gamma_mu q_j. Thus (2) and all ten equations(3) are NECESSARY AND
SUFFICIENT for frozen coefficient descent in this normalized family. The induced
observed coefficient is R_T C_source B, using the fixed right inverse B; it is not
a separately prescribed mass or source-owned target coefficient.

The probe uses two noncommuting, nondecomposable normal sums. It computes the inverse
exactly in their finite blade subalgebra, reconstructs the original E,F and R_T, and
checks all ten lower and forty upper identities. This fixture satisfies the necessary
equations but fails the full lower ones: a planted control against claiming L suffices.
Zero ports and scalar tangential connections give full-descent positive controls.

## 3. A finite polynomial criterion with no singular chart

Fix a faithful D=Mat32(C) representation. Let Delta=det P, U=adj P,
J_j=-eta_j U d_jR and delta=Delta bar(Delta). Then C_j=J_j/Delta and delta>0.
Multiplying(3) by delta gives homogeneous degree65 matrix polynomials

    F_j=4iu bar(Delta) J_j-eta_j delta D_j+7Delta bar(J_j)z
        +2 sum_i bar(J_i)d_i bar(R)J_j
        +eta_j Delta sum_i bar(J_i)[D_i,gamma_j].           (4)

The finite criterion is delta != 0 and every F_j=0. Equivalently introduce a real
variable s and impose s delta-1=0. Dropping this inequation admits spurious singular
points and is not an equivalent test. Real-Clifford conjugation need not be entrywise
matrix conjugation in a quaternionic realization; determinant conjugates correctly
because that real structure is entrywise conjugation composed with an inner map.

Delta has degree32, J degree32, delta degree64, so every displayed term has degree65.
This removes all20,480 real adapter coordinates from the genuine mixed problem,
leaving120+120=240 real port coordinates, projectively239 under nonzero real scaling.
It is a finite equivalent formulation, not a claim that solving it is cheap or that
its real solution set is empty. No determinant or Groebner elimination is claimed run.

## 4. Smooth fixed-geometry consequence

K2165 separates the even-tangent frozen lower residual from

    H_j=sum_mu eta_mu gamma_mu partial_mu A_j
           +sum_mu eta_mu gamma_mu omega partial_mu B_j.

Smooth descent requires q_j=H_j=0 separately. The first sum has tangent degree1,
the second degree3. Each consists of four independent tangent blades over Cl(N).
Consequently H_j=0 iff partial_mu A_j=partial_mu B_j=0 for all mu,j. On each connected
tangential patch the unique(2) must therefore be constant. This remains valid through
zeros of Z for a smooth adapter, though formula(2) itself applies only where Z!=0.

This does not force Z constant. Multiplying a hypothetical solution Z by a smooth
nonzero real scalar h leaves(2) unchanged and multiplies the frozen coefficient
residual by h. No derivatives of h enter the algebraic contraction d_j. Normal-coordinate
dependence is not restricted by the tangential operator. Moving gamma/splitting or
changed reverse/operator adds terms and is a different problem.

## Reproducibility, review and next condition

Run `python tests/channel-swings/k2169_invertible_pencil_full_descent_probe.py` using
the repository SymPy environment; `--write` regenerates its exact JSON report.
Independent specialists reconstructed the ideal, full-row and smooth arguments and
challenged the actual implementation. Controls distinguish universal written proof
from exact finite-map verification and reporting hashes. Altered Euler coefficient,
kernel shift, reverse sign, conjugation, product order and volume factor must fail
specific checks after the clean baseline passes. No proof-assistant/external-expert
certificate or novelty claim is made.

Next test the denominator-aware240-coordinate reduced system by a new structural
trace/grade identity or a genuinely different candidate satisfying all ten q_j.
Do not search singular pencils, repeat excluded pure/two-blade families, or use
fixed-geometry adapter derivatives as repair. Mixed odd/even ports, moving geometry,
native mobile-locus integrability and changed source reverse remain distinct routes.
