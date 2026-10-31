---
title: "K2351 Mixed-parity auxiliary reduction of the selected first action"
status: active_research
doc_type: exploration
created: "2026-10-30"
classification: CONVENTIONAL_COMPARATOR
target_claim: NONE-NOT-A-KILL
claim_ceiling: conditional mathematics; no native GU or empirical certification
scripts:
  - tests/channel-swings/k2351_mixed_parity_auxiliary_reduction_probe.py
---

# K2351 Mixed-parity auxiliary reduction of the selected first action

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
result: K2351
carrier: even and odd Clifford one-form displacement fields at fixed curved geometry LAYER=toy CHIRALITY=N/A
pairing: nondegenerate scalar Clifford trace and exterior Hodge bilinear form ON=declared_carrier
real_structure: real coefficients with complex Hilbert adjoint only where stated
grading: internal Clifford parity separate from exterior form degree
action_owner: repository-construction -- fixed-geometry selected I1 transgression; not I2 residual square
target: invertible-stratum even-field elimination and retained singular equations MAP-TYPE=evaluation
```

## Result and backward demand

[K2348](k2348-even-distortion-stationarity-boundary-2026-10-30.md) excludes purely even stationary nonzero distortion for nonzero kappa in its selected I1 convention. Its remaining physical-response question demands a genuine mixed stationary action and its Hessian before transporting a growing mode or observed response. Here parity gives an exact NONLINEAR reduction: the even field is algebraic and quadratic after one integration by parts. Wherever its coefficient is invertible it can be eliminated exactly, leaving an odd-field effective action with all coefficient derivatives retained. Singular strata and induced boundary conditions remain part of the original problem.

This is a construction tool, not an existence theorem for a mixed stationary native GU vacuum. SC-ACT-01 ASSERTS the first transgression action; SC-GEO-55 ASSERTS connection displacement; SC-META-53 remains UNCERTAIN. The selected Cl(7,7) Shiab/trace convention, and the restrictions to fixed geometry and unconstrained compactly supported field variations, remain explicit imports. Ledger0.263 and source verdicts do not move. K129 already has a linear T=0 distortion/metric Schur calculation; it is not this nonlinear algebraic even-sector reduction. No ordinary torsion substitution, metric-on-metrics identification or I1/I2 Hessian transfer is made.

## Exact parity polarization

Let P(U,V)=integral tr(U wedge V) and m(U,V)=P(U,*V), with the selected symmetric nondegenerate one-form mass pairing M. B is internally even; S flips internal parity as in K2348; DB preserves it. Write T=E+O, with E even and O odd. In the same normalization,

    I(T)=P(T,S(FB+DB T/2+T wedge T/3))+kappa m(T,T)/2.

Parity and scalar trace eliminate E S(FB), E S(DB E), O S(DB O), E-cubic and E O O terms. The surviving terms are

    I(E,O)= (1/2) A_O(E,E)+ell_O(E)+c(O),                  (1)
    A_O=kappa M+C_O,
    ell_O(E)=[P(E,S(DB O))+P(O,S(DB E))]/2,
    c(O)=P(O,S(FB))+kappa m(O,O)/2+P(O,S(O wedge O))/3,
    C_O(E,F)=[P(E,S(F wedge O+O wedge F))
              +P(F,S(E wedge O+O wedge E))
              +P(O,S(E wedge F+F wedge E))]/3.             (2)

C_O is symmetric bilinear in even fields, linear in O and zero-order in their derivatives. Setting F=E verifies the factor1/2 in(1). This polarization is valid without commuting the Clifford factors or inserting an unproved cyclic identity for S. It is also valid if a particular convention has additional cancellations in C; parity alone does not assert C is nonzero on every field or that its singular locus is nonempty.

The only derivatives of E occur linearly in ell. On compactly supported variations, move them to the coefficients and O, defining ell_O(E)=integral E^T b(O) after retaining the boundary term for any other domain. The mass matrix M and coefficient density are in one local trivialization. For derivative terms

    [E^T P^mu partial_mu O+O^T Q^mu partial_mu E]/2,

one obtains

    b_deriv=[(P^mu-(Q^mu)^T)partial_mu O
               -partial_mu((Q^mu)^T)O]/2.                 (3)

Algebraic DB terms are added. Density, S, pairing and frame derivatives are included in partial Q. Dropping them is not a formal adjoint. In particular b(0)=0. Equations(1)-(3) describe an actual local auxiliary field, not inversion of a differential even-field kinetic operator.

## Invertible stratum and stationary equivalence

A_O maps the even fiber to its dual. If it is invertible, the independent even Euler equation gives

    E*(O)=-A_O^-1 b(O),
    Ieff(O)=c(O)-(1/2)integral b(O)^T A_O^-1 b(O).         (4)

Completing the square proves the identity exactly. Variation of Ieff equals the original odd variation at E*, since the original even derivative vanishes there. Therefore full E/O stationarity and reduced odd stationarity are equivalent ON this stratum, with identical admissible variations/boundary terms. The reduced Lagrangian depends on j1O and its Euler equation is generally second order. This is not a quotient, positivity claim or global solution construction.

For kappa!=0 choose an auxiliary positive norm only to estimate matrices. If R=kappa^-1 M^-1 C_O satisfies ||R||<=rho<1, then

    A_O^-1=(I+R)^-1 kappa^-1 M^-1,
    ||A_O^-1||<=||M^-1||/[|kappa|(1-rho)].                  (5)

Neumann convergence proves this without making the native indefinite M positive. Smooth finite-fiber coefficients give a local neighborhood of O=0; uniformity on a compact chart needs bounded M^-1 and C coefficients. At each fixed base point, det A_O is a polynomial in the odd fiber coordinates with nonzero constant term kappa^n det M, where n is the even fiber dimension. Thus for kappa!=0 the regular locus is nonempty, open and dense; the singular locus, if present, is a proper algebraic subset. This says nothing about whether a stationary field can avoid it globally. At kappa=0 this constant-term argument fails. There is no whole-manifold or closed-PDE-domain inverse in(5). At O=0, E*=0 but the reduced first variation is P(delta O,S(FB)); the curved forcing from K2345 remains. Eliminating one variable does not stationarize the background.

At a full stationary configuration the reduced Hessian is the Schur form

    H_eff=H_OO-H_OE A_O^-1 H_EO.                           (6)

Here H_EO includes derivatives and H_OE its actual formal adjoint, including coefficient derivatives and domain terms. It is not merely the transpose of a frozen pointwise coefficient. Since A_O is affine and b(O) linear, H_OO=c''(O) at fixed E. With L[v]=C_v E*+Db[v], the formal reduced Hessian is c''(O)-L! A_O^-1 L, where ! is the integrated dual. This generally introduces second derivatives without supplying positivity or hyperbolicity. Fixed E boundary values become E*(j1O)|boundary=E_boundary; imposing an unrelated old odd Dirichlet domain loses equivalence. The complete moving-geometry source action requires its geometry/receiver variations in addition to this fixed-geometry reduction.

## Native cubic coefficient consumer

The actual K2348 backend (comm,symi,symi), eta1=-1, gives an exact nonzero coefficient on E0=dx0 gamma01, O0=dx1 gamma1. Here E0 wedge E0=0 and

    E0 wedge O0+O0 wedge E0=-2 dx0 wedge dx1 gamma0,
    P(E0,S(E0 wedge O0+O0 wedge E0))=-4,
    C_O0(E0,E0)=-8/3.

Thus the native selected action really contains the coefficient -4 e²o/3 along T=eE0+oO0; C is not merely a parity-allowed fictional term. The exact probe evaluates these exterior/Clifford products with the pinned backend and checks the cubic by direct addition. This is a local coefficient evaluation, not a full stationary solution or proof that the entire A_O has a singular eigenvalue. Restricting a quadratic form to one line does not prove that line invariant under its full matrix.

## Executed variation, singular and Hessian consumers

Use an explicitly declared one-dimensional polynomial CONTROL, not a claimed selected-Shiab solution:

    L= (kappa+x)u²/2-kappa v²/2+u x'
         +f x+kappa x²/2+x³/3.

M=diag(1,-1), C=diag(x,0), b=(x',0). For kappa!=0 and a=kappa+x!=0, u*=-x'/a,v*=0 and

    Leff=f x+kappa x²/2+x³/3-(x')²/(2a),
    Euler_eff=f+kappa x+x²+x''/a-(x')²/(2a²).              (7)

The exact symbolic probe independently computes both the original odd Euler after substitution and the Euler of Leff; they agree. Its mixed nonlinear term and indefinite even pairing prevent a positivity-based proof by accident. The derivative coefficient term in(7) is essential. A separate two-variable polynomial with nonconstant A checks(6) against the second derivative of the explicitly eliminated action; omitting inverse derivatives fails away from b=0.

There are full stationary singular solutions in this GENERAL control: kappa=1,f=-1/2,x=-1 constant,u=+1 or-1,v=0 solve all three Euler equations while A is singular. Thus a general theorem cannot discard the singular stratum. This does not assert that the actual selected-Shiab C has this singular locus. On a singular native stratum, the even equation remains A_O E+b=0: b must annihilate the kernel and any surviving even freedom must still satisfy the odd Euler equation. Its branches require direct analysis rather than the formula(4).

A variable cross-coefficient control explicitly checks(3); genuine altered equations that omit the integrated derivative, the nonlinear C contribution or coefficient derivatives produce nonzero discrepancies. A rational indefinite-matrix example verifies the Neumann majorant while retaining one positive and one negative mass direction. The written parity/polarization proof is universal under its stated premises; finite probes do not substitute for it.

## Next construction and scope

The reduction supplies a concrete route: evaluate the actual coefficient A_O and b(j1O) on a named curved chart, solve the reduced odd Euler with an admissible common domain, then reconstruct E and retain singular possibilities. A frozen symbol or a polynomial control is not that solution. The source stationarity/receiver/domain dependencies remain open, as do hyperbolicity, stability, positivity and physical response. No external-expert or proof-assistant certification or native GU verdict is claimed.
