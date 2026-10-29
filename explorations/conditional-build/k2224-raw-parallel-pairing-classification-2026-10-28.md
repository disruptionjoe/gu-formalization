---
title: "K2224 Parallel pairing classification for the unchanged raw flavor connection"
status: active_research
doc_type: exploration
created: "2026-10-28"
scripts:
  - tests/channel-swings/k2224_raw_parallel_pairing_classification_probe.py
classification: INTERNAL_STRUCTURAL_ONLY
target_claim: NONE-NOT-A-KILL
claim_ceiling: conditional connection-pairing classification; no source-selected parent, action, observation or physical positivity
---

# K2224 Parallel pairing classification for the unchanged raw flavor connection

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
result: complete parallel pairing classification for the fixed K2221 raw spinor connection
carrier: real128 Cl77 spinor on connected product time-space chart LAYER=toy CHIRALITY=S-FULL-DIRAC
pairing: arbitrary real nonsingular bilinear matrix G; symmetric cases and original Clifford B identified separately ON=declared_carrier
real_structure: ordinary conjugation in real Cl77 basis
grading: Clifford grade only; not physical chirality
action_owner: repository-construction -- K2221 unchanged raw coefficient connection
target: connection-parallel bilinear form MAP-TYPE=homomorphism
```

## Preflight: object, predecessor, routes and inference ceiling

The operative object is the spinor connection with K2221's numerical raw
principal and lower return held fixed. It is not the positive reduced L2
current on V1152, and connection compatibility is not the combined trace-Hq
coefficient identity. The supplied mass and flavor coefficients are not
source-selected. Relevant routing is T02/T04/T10/T11/T15/T16: real form,
observation, adjoint, domain, positivity and parameter selection stay typed.

K2212 proves the separate B-skew plus normal-commuting algebra classification;
K2218 proves reduced local multiplier rigidity in its scalar coefficient
class; K2221 supplies the enlarged grade12 raw lift and says moving pairings
are outside its fixed-B theorem. K151's moving distortion lowerer concerns a
different 56-dimensional action packet. K431/K432 concern transported
observation/domain pairings for a rank-two covariant differential. None is a
replacement for the same-connection calculation below. This is a local
repository search, not a novelty claim.

Three routes were compared. A B-preserving frame cannot repair K2221's
fixed-B defect. A freely chosen positive or split constant pairing can be
parallel but changes the pairing parent. Allowing an arbitrary moving G
while keeping the entire connection fixed is the exact question solved here.
No physical claim changes when that question is answered.

## 1. Compatibility and curvature integrability

Use K2221's real matrices

    T=product of ten normal gammas,
    A=gamma0 J,
    C_j=gamma0 gamma_j, X_j=C_j T, j=7,8,9,
    K(x)=m A+sum a_j(x)X_j,
    Omega0=K(x), Omega_i=0 (i != 0).

Here m is constant and the a_j are smooth and time independent. The
matrices A,X7,X8,X9 are real-transpose skew, square to -I and mutually
anticommute. Work on a connected product chart I x U with coordinates in
all declared zero-connection directions; the familiar R3 spatial case is a
specialization. For connection convention nabla=d+Omega, a bilinear form is
parallel exactly when

    partial_mu G=Omega_mu^t G+G Omega_mu.

Consequently G is independent of every spatial coordinate, and

    G'(t)=[G(t),K(x)] for EVERY x.                    (1)

Spatially varying pairings are already excluded, even if singular or
nonsymmetric pairings were allowed. Commuting covariant derivatives gives

    F_mu,nu^t G+G F_mu,nu=0,
    F_i0=partial_i K.

These equations are necessary integrability conditions. Curvature invariance
alone is not substituted for (1); the next section solves (1) completely.

## 2. Complete classification for nonconstant a

If a takes at least two distinct values, EVERY solution G of (1) is constant
in both space and time. The solutions are exactly

    G constant, [G,K(x)]=0 for all x,                 (2)

with symmetry and nonsingularity imposed if desired.

Proof: choose x* and x1 with v=a(x1)-a(x*) nonzero. Set
K*=K(x*), V=sum v_j X_j and s=|v|^2>0. Equation (1) implies
[G,V]=0 and G'=[G,K*]. Differentiating the first equation and using Jacobi
gives [G,[K*,V]]=0. The Clifford relations give

    V^2=-sI, {K*,V}=-2(a(x*) dot v)I,
    [K*,V]V=-2sK*+2(a(x*) dot v)V.                   (3)

G commutes with both factors on the left and with V on the right. Since
s>0 it commutes with K*, so G'=0. Substitution proves (2); its converse is
immediate. This proof needs no nonzero-mass assumption and does not rely on
a nonzero derivative at a chosen point. Connectedness and smoothness are
more than sufficient for the original connection formulation.

## 3. Constant a and the original B anchor

When a is spatially constant, all solutions are

    G(t)=exp(t K^t) G0 exp(t K)
        =exp(-tK)G0 exp(tK),                         (4)

after shifting the initial time to zero. Symmetry, nonsingularity and
inertia are preserved by congruence. For the original Clifford pairing B,
one may use the canonical real-basis representative

    B=gamma7 gamma8 ... gamma13.

It is a symmetric involution with trace zero, giving inertia(64,64), and
gamma_r^t B=-B gamma_r for all fourteen gammas. A commutes with B while
each X_j anticommutes with B. Thus

    K^tB+BK=2B sum a_jX_j.                           (5)

For constant nonzero a, (4) with G0=B is genuinely time dependent and is a
valid parallel moving pairing for the original connection. It does not
preserve the original fixed B-adjoint on all timeslices.

For nonconstant a, no solution may equal B on any entire time slice:
the preceding theorem forces it to be the constant B, and (5) then forces
a=0 everywhere. The local curvature obstruction at B is

    (partial_i K)^t B+B partial_iK
        =2B sum (partial_i a_j)X_j.

The square of the flavor sum is -|partial_i a|^2 I, so a nonzero derivative
has a nonzero, indeed invertible, obstruction. A tempting formula
exp(-tK(x))B exp(tK(x)) solves the time equation pointwise but violates the
spatial equations. At t=0 its mixed spatial-time derivative is precisely
the displayed defect. Flat REDUCED a=dtheta does not fix this: for
a7=sin x7 the raw F_70=cos x7 X7 is nonzero.

## 4. Positive and split controls; what they do not repair

The constant G=I is always a positive compatible spinor pairing, since K is
ordinary-transpose skew. A second explicit universal compatible form is

    G_split=gamma1 gamma10.

Both indices are normal; their Clifford signs are opposite. G_split is a
symmetric involution, has trace zero and inertia(64,64), and commutes with A
and every X_j. It therefore passes (2) for all profiles. This defeats any
claim that the original fixed-B obstruction excludes every nondegenerate or
every indefinite pairing. It does not reproduce the original B-adjoint;
for example gamma2 is self-adjoint for G_split instead of B-skew.

Two optional stronger requirements expose the exact missing bridges.

* If the SAME G must be parallel and ALSO satisfy the corresponding normal
  trace equation K^t G gamma_r+G gamma_r K=0, compatibility with constant G
  reduces it to G[gamma_r,K]=0. For nonconstant a, (2) therefore forces
  [gamma_r,K]=0 and hence sum a_jX_j=0. Thus the original trace-Hq identities
  cannot simply be relabeled with the changed constant pairing. The existing
  identities with B remain valid as distinct fixed-form coefficient tests.
* If all fixed gamma matrices must retain gamma_r^t G=-G gamma_r, then
  B^-1G commutes with every gamma. Faithful Cl(7,7)=Mat128(R) forces G=cB
  pointwise. Compatibility gives c spatially constant and
  c' I=2c sum a_jX_j; scalar/blade separation forces a=0 and c'=0.
  This extra Clifford-adjoint requirement is not implied merely by retaining
  the numerical raw principal matrices.

The second bullet concerns the irreducible real128 spinor parent. Enlarged
raw-slot or nine-copy pairing matrices have multiplicity freedom and must
be typed separately; no arbitrary full1920 pairing classification is claimed.

## 5. Followthrough and next construction

The candidate survives as a complete conditional pairing classification.
The strongest false negative is refuted by I and G_split; the strongest
false repair is refuted by the missing spatial compatibility equation.
No source, physical positivity, empirical, family or ledger credit follows.
K2221's reduced current, its original B-based trace-Hq test and a newly
chosen compatible spinor G are three distinct objects.

To obtain spatially varying parallel pairings one must change the spatial
connection or geometry. A useful next construction must declare the added
Omega_i and G, solve partial_iG=Omega_i^tG+G Omega_i, then retest the actual
original raw rows, normal trace equations with their stated pairing, and
principal intertwining. A general frame change transports the principal
matrices too and cannot be silently advertised as the unchanged raw model.
If a different fixed parent is pursued instead, G_split is an exact supplied
candidate whose Clifford/trace/action bridge must be built explicitly.

## Postflight and evidence boundary

The exact probe verifies the Clifford identities, original B
realization, the positive and split controls, the constant-coefficient moving
B first jet, the nonconstant mixed-jet obstruction, and the rigidity identity
with rational coefficients. Genuine mutations reverse the transport jet,
change the rigidity identity sign, replace the split control by an
incompatible normal generator, and reverse the mixed-jet derivative. The
universal proof, finite controls and predecessor raw-return proof are
different evidence kinds. No large matrix, heavy test, external-expert,
proof-assistant, remote-CI or novelty certification is claimed. The report is [the exact certificate](../../lab/process/k2224-raw-parallel-pairing-classification.json).
