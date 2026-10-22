---
title: "K1948: A local obstruction to every variable one-column repair"
status: active_research
doc_type: exploration
created: "2026-10-22"
classification: INTERNAL_STRUCTURAL_ONLY
target_claim: NONE-NOT-A-KILL
claim_ceiling: exact conditional mathematics; no native full20 ownership, physical GU conclusion, novelty or formal proof
scripts:
  - tests/channel-swings/k1948_variable_observation_rigidity.py
  - tests/channel-swings/k1948_variable_observation_rigidity_probe.py
---

# K1948: A local obstruction to every variable one-column repair

> **GU-COMPARATOR-ROUTING — scope before inference.** This artifact contains or
> borders a conventional particle-physics comparator. Any result about a
> standard Higgs/VEV, ordinary family index or net chirality, SO(10) `126`
> Majorana mechanism, anomaly selector, VEV-only breaking or familiar vector-
> mass route binds only that named model. It is not evidence for or against
> Weinstein's source-native mechanism without an explicit typed bridge. Read
> `lab/methods/source-native-comparator-routing.md` and follow its source-native
> pointers before reusing this result.

Classification: `INTERNAL_STRUCTURAL_ONLY`.

```gu-typed-objects
result: local full-carrier variable-coefficient rigidity and residual coercivity
carrier: fixed corrected K77 real512 source and real128 target with32 copies LAYER=toy CHIRALITY=N/A
pairing: fixed K1832 positive H and Euclidean target ON=compressed_conditional_system
real_structure: real coefficient fields; positivity does not transfer to complex bilinear parameters
grading: differential order and auxiliary raw input support, not physical cohomology
action_owner: repository-construction -- fixed compressed principal and leading observation maps
target: arbitrary variable conservative one-input-column completion MAP-TYPE=intertwiner
```

## Result

The special-variable-coefficient escape left open by
[K1945](k1945-energy-compatible-raw-columns-2026-10-22.md) is now excluded
throughout its **fixed-energy, real, one-auxiliary-input-column class**, even
with arbitrary mixing of all32 copies and an arbitrary zero-order observation
correction. The proof is local. It requires no compact domain, boundary
condition, periodicity or static assumption.

A new rational functional annihilates EVERY derivative term and sends the
remaining quadratic defect to a strictly positive weighted sum of squares of
all2080 first-order parameters. Thus the only exact solution is C=B=S=0.
The argument also covers locally square-integrable coefficient fields whose
remaining equation holds weakly. A quantitative residual bound follows.

This is conditional mathematical rigidity. It is not a GU falsification or
an exclusion of different leading observations, energies, moving principal
matrices, dissipative target dynamics, complex bilinear coefficients or added
input columns. [K1947](k1947-minimal-raw-input-support-2026-10-22.md) gives an
explicit surviving larger-support construction.

SC-OP-04 ASSERTS candidate four-independent-field grammar; SC-OP-05 is
UNCERTAIN about a southeast rival. SC-MAS-01 and SC-CHI-02 ASSERT their
stylized curvature-mass toy; SC-META-53 is UNCERTAIN. They do not select the
present H or observation. LT-SM8, LT-GR6b and AC-F1 remain NEEDS. Source,
ledger and canon dispositions are unchanged.

## 1. The complete equations, including the signs

Keep the same constant principal matrices A_i,d_i and leading observation T_i.
For arbitrary real spacetime-dependent coefficients let

    P=partial_t+A_i partial_i+C,
    Q=partial_t+d_i partial_i+B,
    O=T_i partial_i+S.

Require C=N Z Q_aux with Z skew (the complete fixed-H conservative raw
one-column class from K1945), and B skew for target energy conservation.
Here Q_aux denotes auxiliary extraction and is not the differential Q above.
The exact coefficient equations for OP=QO are

    T_i C-B T_i+S A_i-d_i S=0,                            (1)
    E=T_i partial_i C+S C-partial_t S-d_i partial_i S-B S=0. (2)

In particular the time derivative of S has a MINUS sign. Fixed principal
matrices are essential. The complete first-order kernel of(1) is already
certified in K1945: each diagonal copy has three parameters, and each
unordered pair of copies has four. Its dimension is32×3+496×4=2080.
All coefficients satisfying(1) are combinations of these fixed rational
basis triples with arbitrary real scalar functions v_a(t,x).

## 2. A derivative-annihilating positive functional

Write a4×16 diagonal residual block in row-major order, with entries numbered
0,…,63. Define four linear functionals by the following nonzero entries;
all unlisted entries vanish. Multiply each row by its listed scale.

| type | scale | entry3 | entry28 | entry46 | entry58 | entry63 |
|---|---:|---:|---:|---:|---:|---:|
|0|16|1|-9/265|9/263|3|18/69695|
|1|1|1|-18/265|18/263|3|36/69695|
|2|1|1|18/265|18/263|-3|-36/69695|
|3|16|1|9/265|9/263|-3|-18/69695|

Let ell_t be these functionals, and define L(E) as the sum of ell_type(k)
over the32 diagonal copy blocks of E. The certificate verifies two facts on
the ACTUAL rational kernel basis:

1. For every diagonal basis triple(C_a,B_a,S_a),

       ell_t(S_a)=0,
       ell_t(T_i C_a-d_i S_a)=0 for i=1,2,3.             (3)

2. On each diagonal family, and each of the ten unordered coordinate-type
   pairs, the quadratic functional has zero mixed monomials and strictly
   positive square coefficients. The minimum coefficient across all these
   families is exactly

       mu=1689693696/540629375 >0.                        (4)

The new functional was discovered by a finite linear feasibility search in
the exact derivative-annihilator space. A first rational conversion called an
unavailable Sage method and produced no certificate. Exact rationalization
then succeeded, and the proportional rows simplified to the table above.
The producer does not depend on the numerical solver; every final identity
and inequality is rational and separately replayed.

Off-diagonal derivative terms never enter L, which reads only diagonal blocks.
The principal/leading matrices are block diagonal, so their diagonal
derivative terms involve only diagonal C,S. Thus(3) cancels ALL variable
terms, including time variation and arbitrary off-diagonal coefficient
variation. This is stronger than the original K1945 functional, whose
nonzero derivative coefficients allowed only a proposed flux argument.

## 3. Local full-carrier rigidity

For arbitrary coefficients satisfying(1), apply L to(2). The derivative
terms vanish identically by(3). Every diagonal block of SC-BS is the sum of
its own diagonal product and one paired product for each other copy.
There are no three-copy loops or mixed products between distinct pairs in
that diagonal quadratic expression. Therefore

    L(E)=sum_{a=1}^{2080} w_a v_a², w_a>=mu>0.            (5)

The ten type-pair certificates include different copies of the SAME type;
they are not merely tests of ten isolated examples. The identity just given
is the exact composition rule proving(5) for all32 copies.

If E=0, (5) forces every real v_a=0 pointwise. Completeness of the first-order
kernels then gives C=B=S=0. No integration or boundary assumption is used.
An arbitrary-profile ansatz, spatial variation, time variation or cross-copy
mixing cannot evade the result inside this class.

For a weak version, assume the coefficients satisfy(1) almost everywhere,
are locally L2, and satisfy(2) in distributions. The parameter functions are
fixed linear coordinates on a finite-dimensional kernel, so they too are
locally L2. Their quadratic products are locally L1. Equation(3) still
cancels distributional derivatives, leaving the nonnegative locally
integrable function in(5) equal to the zero distribution. It vanishes almost
everywhere, giving the same conclusion. No multiplication of two arbitrary
distributions is used.

## 4. Released quantitative consumer: near intertwiners

Retain exact conservation, support and first-order equations(1), but allow
a nonzero ordinary residual E. In the stored bases, the squared Frobenius
norm of the full functional is

    norm(L)²=39956594547616/971478605.

Cauchy--Schwarz and(5) give the pointwise, derivative-independent bound

    mu |v|² <= L(E) <= norm(L) norm(E)_F,
    |v|⁴ <= K norm(E)_F²,
    K=1055252198748343701015625/250621155772584763392.     (6)

The coefficients and norm are independently recomputed from the matrices;
these are basis-specific quantitative constants, not invariant physical units.
On a region U with E in L1, integration also gives

    integral_U |v|² <= norm(L)/mu integral_U norm(E)_F.

Thus rapid oscillation cannot hide a fixed nonzero parameter magnitude behind
a small full residual while the hypotheses remain exact. This is an actual
stability consequence, not a sampled lower bound or a claim about approximate
first-order equations. If(1) is also approximate, its derivative errors can
enter(2), and no bound of this form has been established here.

## 5. Counterroutes, scope and verification

The decisive contrary route is K1840's variable-mass construction, realized
in raw form by K1947. It changes the input-support premise and remains valid.
This is why the local theorem does not become an all-observations or all-GU
exclusion. The original complex vector escape from a real sum of squares
also explains why the REAL premise is indispensable. A Hermitian complex
problem would need its own equations and positivity certificate.

Run the two frontmatter scripts with Sage Python. The producer checks64 new
exact derivative/positivity/coercivity groups. The independent probe first
replays K1945's119 completeness controls, then rebuilds derivative terms and
all quadratic diagonal products from the actual triples and paired kernels;
it does not trust stored positive labels. Mathematical faults target the
functional, a load-bearing source coefficient, the correction and a pair
kernel. Identity/pin faults are separately reported. An initial arbitrary-entry
mutation set did not detect every alteration because some entries were
invisible to the tested functional; it was not counted as a passing harness.
The final mutations perturb coefficients the claimed calculation actually
uses, after a fresh green baseline.

Preflight compared nonlinear coefficient solving with annihilator/positivity
structure. The latter removes the entire variable one-column search and its
periodic/decay subcases. The weakest remaining seam is physical ownership and
extension to larger support, not an untested boundary transfer. No external
expert acceptance, formal verification or novelty is claimed.

K1947 follows the support alternative through an exact two-slot constant-mass
witness and its global positive observation Gram. Next impose source-owned
cell/barred-map constraints or test a specified nonfactorized variable
profile on that larger-support branch. The arbitrary-variable one-auxiliary-
input-column branch is settled at this exact scope.
