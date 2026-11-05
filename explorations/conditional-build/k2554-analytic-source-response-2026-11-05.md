---
title: "K2554 Regular-center analytic source response and overlap descent"
status: active_research
doc_type: exploration
created: "2026-11-05"
classification: CONVENTIONAL_COMPARATOR
target_claim: NONE-NOT-A-KILL
claim_ceiling: local analytic-germ existence and gauge-equivalent splitter changes; no delta-source or global physical domain
scripts:
  - tests/channel-swings/k2554_analytic_source_response_probe.py
---

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
result: K2554
carrier: prescribed radial-pressure source germs and original fields on the selected curved seven-plus-seven product LAYER=toy CHIRALITY=N/A
pairing: indefinite tensor/test pairing with compact divergence-free local tests ON=declared_carrier
real_structure: real nonzero kappa and locally real-analytic data; auxiliary Cartesian radial lifts
grading: scalar source, TT source, original metric, shifted metric and displacement remain distinct
action_owner: repository-construction -- selected comm/symi/symi completion of K2537
target: local analytic source response and gauge-invariant splitter descent MAP-TYPE=evaluation
```

# K2554 Solve the four scalar equations in one analytic germ class

## Result and source boundary

K2552 reduced the conserved radial-pressure source to four scalar equations but
supplied no response inverses. Here all four have selected local analytic right
inverses on a common noncharacteristic B hypersurface, including the regular
radial center. The construction retains all seven B variables and the original
metric h. A change of the auxiliary scalar/TT splitter changes h only by a
linearized diffeomorphism for these coordinated choices. Compact conserved
metric tests therefore descend independently of that splitter.

The source must be analytic locally: A and P are analytic even in r near the
center, satisfy the SAME pressure conservation law, and rho is analytic in all
B variables. A smooth compact profile may be analytic near the center; its
remote cutoff does not have to be analytic. The B point distribution is NOT
admitted. This is a germ construction, not a fixed-radius bounded inverse,
closed operator domain, causal prescription or globally compact-source solution.
No ordinary Cauchy well-posedness, positivity, physical readout, native Met(X),
GU verdict or novelty is claimed.

SC-ACT-01 ASSERTS the source action; SC-GEO-55 ASSERTS gauge-rotated-LC
displacement; SC-GEO-03 ASSERTS Met(X); SC-META-53 remains UNCERTAIN about
indefinite spectra. The selected comm/symi/symi completion and independent
curved product remain repository constructions. Ledger0.263 is unchanged.

## 1. Exact determinant discriminator

Use K2552's complete six-potential matrix M(X,Y), including its skew row.
For nonzero kappa its determinant obeys

    d_kappa(X,Y)=kappa^6 d_1(X/kappa²,Y/kappa²).

Its total degree is five. The exact highest homogeneous part is

    L kappa^-4 (X+Y)^5,
    L=-2605746313310516251459584/22521658027326625 !=0.       (1)

The probe recomputes the determinant from the full matrix and verifies (1),
scaling, and independently evaluated exact determinants. Thus d has differential
order ten after substituting the second-order scalar operators.

A tempting stronger simplification is FALSE. Put P(Z)=d_1(Z,0). Then

    d_1(X,Y)-P(X+Y)=XY Q(X+Y),
    Q(0)=425557062921636685109/260973818179992280940544 !=0. (2)

The probe records all exact P and Q coefficients. The top symbol depends only
on the sum; the full determinant does not. A five-mass factorization using P
would solve a different equation. The actual mixed dependence survives and
cannot be dropped in a common spectral construction.

## 2. Remove the center singularity without changing the radial operators

Use K2552's K, alpha=-KS/C, beta=C/S and analytic S,C with S(0)=0,
S'(0)=C(0)=1 and C'=-KS. Define analytic functions q3,q5 of s=r² by

    4alpha+2beta = 2/r + r q3(r²),
    6alpha+4beta = 4/r + r q5(r²).

Their constant terms are q3(0)=-14K/3 and q5(0)=-22K/3.
Lift radial functions to rotation-invariant functions on auxiliary Cartesian
spaces R³ and R⁵ respectively:

    Xtilde=Delta_R3+q3(|y|²) y·grad_y,
    Dtilde5=Delta_R5+q5(|y|²) y·grad_y.               (3)

On radial functions these are EXACTLY X and D5. The five-dimensional lift is
an auxiliary analytic device for the TT amplitude, not a change of the physical
three normal directions. A rotation-invariant analytic germ is a convergent
series in |y|²; restricting it back gives the required analytic even amplitude.
K2552's tensor reconstruction then has b-a_b=O(r²) and no center delta.

The fixed Dirichlet splitter is locally analytic when its source trace is.
Indeed, with s=r²,

    X=4s d_s²+(6+2s q3(s))d_s.

The regular equation (X+7K)chi=-t/6 determines chi_(n+1) by division by
(n+1)(4n+6), never zero. The analytic regular-singular ODE has one regular
analytic solution for each chi(0); its other Frobenius solution is singular
like r^-1. The smooth K2552 splitter excludes that branch. Its radial TT
amplitude b=P/2+(4alpha+2beta)chi'+6Kchi is analytic even as well.

## 3. A single noncharacteristic hypersurface for all four equations

Take an analytic coordinate t on B with g_B^{-1}(dt,dt)!=0 at the chosen point;
shrink the chart so it remains nonzero. The constant-curvature metric has
analytic local coordinates. Keep its other six coordinates as unrestricted
analytic variables. No Fourier-mode or tangential-frequency cutoff is imposed.

For the lifted operators D5+Y-16K, c(D5+Y+mu-21K), and X+Y+12K, the coefficient
of d_t² is respectively g_B^{tt}, c g_B^{tt}, g_B^{tt}, each nonzero. For
actual d(X,Y), equation (1) gives the d_t^10 coefficient

    L kappa^-4 (g_B^{tt})^5 !=0.                     (4)

The terms in (2) have lower differential order and do not alter (4).
Cauchy--Kowalevskaya therefore gives analytic local solutions with zero t
Cauchy jets through order one for the three second-order equations and through
order nine for dU=phi. These are chosen mathematical data, not a boundary
condition selected by the original action. The theorem is the analytic,
noncharacteristic local existence/uniqueness result stated in
[Han's PDE notes, Theorem 2, p.3](https://sites.math.rutgers.edu/~zchan/517/cauchy.pdf).
Its hypotheses do not establish ordinary Sobolev well-posedness.

The lift, source and t data are rotation invariant. Uniqueness makes the
solutions rotation invariant on a smaller invariant neighborhood. Intersect
the four neighborhoods and return to r. K2552 equations (7),(9),(10) now
produce z,Q,h=z-rE sym(Q),e2=-A2^-1 BQ solving every original selected linear
row with the prescribed analytic source germ. Arbitrary source dependence in
all B variables survives. Neighborhood size may depend on the source; no
uniform norm estimate follows from this theorem.

## 4. Released overlap result: the original metric descends modulo gauge

Let a different regular splitter add psi with Xpsi=-7Kpsi. The source split
changes by opposite copies of Tpsi rho, where

    Tpsi=Hess_A psi+K psi G_A,
    v=(K,0,1,0,0,0)^T.

Tpsi is TT, with Box_A Tpsi=7K Tpsi. Direct substitution into the FULL matrix
proves the polynomial identity

    M(-7K,Y)v=c(Y+mu)v.                              (5)

Consequently, in the polynomial ring in Y,

    d(-7K,Y)=c(Y+mu) R(Y), deg R=4,
    adj(M(-7K,Y))v=R(Y)v.                            (6)

The first equality follows from the eigenvector (a constant change of basis
triangularizes its invariant line); the second follows over the rational
function field and hence polynomially. The probe verifies divisibility and
independent exact cofactor fixtures.

Uniqueness of zero-data CK solutions implies the scalar U for psi rho has
form psi V(B): V solves d(-7K,Y)V=rho with zero jets0..9. Then q=R(Y)V has
zero jets0,1, since R has differential order eight, and solves
c(Y+mu)q=rho. The TT inverse with the same t data is the same q. Therefore
Q_scalar=Q_TT on the overlap. This statement uses the actual lower-order
coefficients in d, not a total-Laplacian approximation.

For the Einstein part choose (Y+5K)W=rho with zero jets0,1. K2552's scalar
formula and TT formula give

    z_s=-(rE/2) S0(psi W), z_t=rE W Tpsi,
    z_s-z_t=-(rE/2) Lie_xi G, xi=W grad_A psi.       (7)

To check (7), S0(psi W) has AA=-2KpsiW G_A, BB=0, and
AB=d_Apsi d_BW. Lie_xi G has AA=2W Hess_Apsi, BB=0 and
AB=d_Apsi d_BW. The Q terms agree, so (7) also gives h_s-h_t.
Changing the splitter thus changes the total response by a diffeomorphism,
not literally zero. The homogeneous compensating sign depends on which split
is subtracted. For every compact symmetric test F with div F=0 inside the
common germ chart, integration by parts gives <F,Lie_xi G>=0. These local
gauge-invariant observations are splitter independent.

This closes the overlap obligation at the gauge-invariant observation level
for this coordinated analytic prescription. It does not select among unrelated
homogeneous physical responses, extend analytic rho to a delta, or produce an
off-source measurement: nonzero analytic germs cannot have a source-free open
subset of a connected analytic neighborhood merely by compact support.

## Verification and next question

Exact determinant, scaling, mixed correction, regular lift, overlap eigenline,
divisibility, cofactor fixtures and metric Lie components are independently
reproducible. CK and analytic regularity are mathematical theorem applications;
fixture counts are not a proof of their hypotheses. The next source test is a
distributional or otherwise justified smooth-source common realization admitting
the actual delta/smoothed source and its original-metric observation. Any such
extension must retain the mixed determinant term and check its own data and
boundary conditions; analytic approximation alone gives no stable limit.
