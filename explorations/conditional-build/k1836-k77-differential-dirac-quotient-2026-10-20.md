---
title: "K1836: local differential Dirac observations and conservative mass lifts"
status: active_research
doc_type: exploration
created: "2026-10-20"
classification: INTERNAL_STRUCTURAL_ONLY
target_claim: NONE-NOT-A-KILL
claim_ceiling: conditional compressed constant-coefficient fixture; no source-owned observation, physical mass or interacting quotient
---

# A local differential quotient repairs the constant-observation obstruction

The corrected compressed E512 system admits a first-order differential
observation onto a real128 single-speed Dirac system. It is surjective at every
nonzero spatial frequency. Recovering its slow-sector representative requires
an inverse Laplacian; this is not an invertible local field split. There are
also conservative lower-order coefficients lifting two independent Dirac mass
matrices. Their coefficients are supplied choices, not GU predictions.

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
result: complete degree-one slow Dirac observations, differential lifting and conservative mass realization
carrier: corrected E512 fixture as 32 equivalent real16 modules; real4 target per module LAYER=toy CHIRALITY=N/A
pairing: K1832 positive common H and Euclidean target norm ON=constant_coefficient_real_fields
real_structure: rational real matrices and real Fourier conjugation
grading: spatial differential order; no physical or cohomological grading
action_owner: repository-construction -- imported Dirac target and conditional compressed evolution
target: single-speed local differential observation MAP-TYPE=quotient
```

## 1. Exact object and the missing distinction

K1834 excludes nonzero constant invariant pure-speed fields, and provides a
nonlocal slow projector G(xi). An observation is a map out of the fields;
it need not be an invariant constant subspace. Here it is differential.
We use K1832's exact rational A1,A2,A3 and H on each of four coordinate
block types, and K1824's equivalence of all32 real16 modules. No uncompressed
source descent is assumed. SC-OP-04 ASSERTS the four-field candidate grammar;
SC-OP-05 is UNCERTAIN about a southeast rival; ACT-01/02/06 ASSERTS their
respective action/equation claims; META-53 remains UNCERTAIN. RA-F1, AC-F1
and LT-SM8 stay unchanged. This construction supplies a conditional local
causal interface, not their missing physical carrier, action or positivity.

Set X=[[0,1],[1,0]], Z=diag(1,-1), E=[[0,1],[-1,0]]. Define symmetric
real4 matrices

```
D1=X tensor I2, D2=Z tensor I2, D3=E tensor E.
D_i D_j + D_j D_i = 2 delta_ij I4, J=D1 D2 D3, J²=-I4.
```

The target is psi_t + D(partial)psi/24=0. Its single speed is1/24 in the
fixture's units. This ordinary target is demand-selected, not source-selected.

## 2. Complete degree-one classification and all-direction rank

Write T(xi)=sum xi_i T_i, with real rational4-by16 matrices. Equating
coefficients in T(xi)A(xi)=D(xi)T(xi)/24 gives

```
T_i A_i=D_i T_i/24,
T_i A_j+T_j A_i=(D_i T_j+D_j T_i)/24, i<j.             (1)
```

The full384-by192 rational system has nullity2 in every coordinate type.
Its complete basis is in the certificate. Every solution is (a I4+b J)T
for one recorded nonzero T. A constant observation instead solves the
192-by64 system T A_i=D_i T/24, whose kernel is zero. These are complete
linear classifications, not bounds obtained from sampled directions.

For the selected T, exact coefficient identities give a positive rational
alpha (138/25 for block0) such that

```
T(xi) H^-1 T(xi)^T = alpha |xi|² I4.                 (2)
```

Axis terms and all mixed terms are checked separately. Thus T has rank4
at EVERY nonzero real xi. J is skew and J²=-I, so aI+bJ multiplies the Gram
by a²+b². Every nonzero member of the classified family has the same rank
property. Summing the32 transported copies gives target dimension128.
Neither this dimension nor the real4 Clifford representation is a family count.

## 3. Lifting, kernel, derivative loss and zero modes

Let Q_i=H^-1 T_i^T/alpha. Exact identities are

```
T(xi)Q(xi)=|xi|² I4,
Q(xi)T(xi)=576(|xi|² I16-A(xi)²)/575=|xi|² G(xi),
A(xi)Q(xi)=Q(xi)D(xi)/24.                           (3)
```

The second identity is checked coefficient by coefficient and agrees with
K1834's projector. For xi!=0, ker T is exactly the fast12-dimensional
space, while im Q is exactly the slow4-dimensional space. This gives an exact
symbol sequence from fast modes to all16 fields to the real4 Dirac target.
It is not an exact source gauge or BV sequence.

For constant coefficients, psi=T(partial)u solves the target whenever u
solves the original free evolution. Conversely

```
u=Q(partial) Delta^-1 psi
```

is a slow representative and solves the original free evolution wherever the
inverse Laplacian and this expression are defined. The signs follow from
T(partial)Q(partial)=Delta, not -Delta. On a torus the formula works for
mean-zero data. On R3 one may first use smooth Fourier data supported away
from zero; the symbol is of order-1, with the stated homogeneous Sobolev
extension when its norm is finite. It is not a bounded inhomogeneous inverse
at low frequency. At xi=0 the observation vanishes; constant target modes on
a torus are not obtained from periodic u by this derivative map.

T(partial) is local and preserves support. The inverse is nonlocal. The
energy identity (2) implies that the observed L2 energy is alpha times the
homogeneous H1 energy of the original slow component. Consequently derivative
loss and low-frequency recovery cannot be hidden by equal solution dimensions.
This is compatible with the unsplit speed1 estimate and the slower quotient.

## 4. All local constant lower-order lifts; conservative mass repair

For u_t+A(partial)u+C u=0 and psi_t+D(partial)psi/24+B psi=0, the same
observation works exactly when

```
T_i C = B T_i, i=1,2,3.                             (4)
```

The stacked12-by16 matrix W=(T1;T2;T3) has rank12. For every real4-by4 B,
W C=diag(B,B,B)W is soluble because W has a right inverse. Its kernel has
64 dimensions: arbitrary maps into ker W, which has dimension4. Thus the
complete pair space(C,B) has dimension80, projecting onto ALL16 target
coefficients. No fitted coefficient is being passed off as source-owned.

Requiring H C+C^T H=0 leaves a9-dimensional pair space; its image in B has
dimension3 and its B=0 kernel has dimension6. Exact bases, including lifts,
are supplied for all four coordinate types. Every such B is Euclidean-skew.
Its target image has the following basis (sign choices are immaterial):

```
B0 = [[0,1,0,0],[-1,0,0,0],[0,0,0,1],[0,0,-1,0]],
B1 = [[0,0,1,0],[0,0,0,-1],[-1,0,0,0],[0,1,0,0]],
B2 = [[0,0,0,1],[0,0,1,0],[0,-1,0,0],[-1,0,0,0]].
```

They square to-I and anticommute pairwise. B0 commutes with every D_i;
B1 and B2 anticommute with every D_i. Hence B=m1 B1+m2 B2 has a conservative
lift and the target satisfies

```
psi_tt - Delta psi/576 + (m1²+m2²) psi=0.            (5)
```

This is an exact local massive Dirac realization with supplied parameters,
not a physical mass prediction. A B0 term instead commutes with the spatial
symbol and must not be included silently in the Klein-Gordon mass formula.
The source u need not satisfy that same second-order equation in its fast
sector. Equation(5) is a consequence, and its arbitrary wave solutions still
owe the first-order Dirac constraint.

Every conservative solution of(4) preserves ker T(xi); skewness then preserves
its H-orthogonal slow complement. Thus it commutes with all G(xi). K1834
classified the complete conservative speed-compatible space as dimension9 per
module. The equal dimension proves that ALL of those9 coefficients admit this
local Dirac observation, not merely the examples found here. For general
nonconservative C, condition(4) preserves the fast kernel but need not preserve
the slow representative. The arbitrary80-dimensional lift class therefore
must not be equated to K1834's20-dimensional sector-preserving class.

## 5. Verification and honest remaining work

```
sage -python tests/channel-swings/k1836_k77_differential_dirac_quotient.py
sage -python tests/channel-swings/k1836_k77_differential_dirac_quotient_probe.py
```

The producer solves full rational coefficient systems, then verifies exact
Gram, kernel/lift and mass identities. The separate probe assembles the
observation equations by Kronecker products over a good finite field, obtaining
rank190 (rational solutions give the matching upper bound), and checks direct
rational polynomial consequences, wrong speed/sign/data controls, and mass
lifts. Reporting mutations have a separate count. Written arguments establish
the continuum and PDE interpretation; direction samples alone do not.

Inline hostile review checked observation versus invariant inclusion, all
mixed polynomial terms, H-adjoint orientation, Delta signs, zero modes,
arbitrary B versus conservative B, and free versus mass dispersion. No
unresolved finding within this scope; no separate-agent review or novelty
claim. Source, ledger and canon remain unchanged.

The next source-facing gate is whether an actual source observation and its
same-background operator obey(1) and(4), including variable-coefficient
commutator terms, barred pairing and domain. Existence of these constant
conditional maps does not supply that identification. The mass lifts show
that locality and positive energy alone do not fix the missing coefficients.
For the conditional PDE itself, variable-background compatibility and global
boundary-domain descent remain substantial open questions.
