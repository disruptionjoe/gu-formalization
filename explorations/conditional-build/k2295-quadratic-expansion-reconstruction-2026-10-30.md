---
title: "K2295 Exact matter expansion and positive designer reconstruction"
status: active_research
doc_type: exploration
created: "2026-10-30"
classification: INTERNAL_STRUCTURAL_ONLY
target_claim: NONE-NOT-A-KILL
claim_ceiling: supplied metric models only; no empirical or GU verdict
scripts:
  - tests/channel-swings/k2295_quadratic_expansion_reconstruction_probe.py
---

# K2295 Exact matter expansion and positive designer reconstruction

Classification: `INTERNAL_STRUCTURAL_ONLY`.

```gu-typed-objects
result: K2295 Exact matter expansion and positive designer reconstruction
carrier: real flat expanding FLRW metric histories with conserved real stress LAYER=toy CHIRALITY=N/A
pairing: real metric contraction and scalar action integral ON=declared_carrier
real_structure: real metric and coefficient functions
grading: no native Clifford transfer
action_owner: repository-construction -- supplied metric f(R)
target: full homogeneous field equation reconstruction MAP-TYPE=evaluation
```

## Result and scope

Adding conserved dust and radiation does not rescue an EXACT dust-bearing LCDM-shaped history in the fixed nonzero-quadratic metric family. For a positive quadratic coefficient, the full constraint requires additional negative stiff and, with radiation, super-stiff source terms. Radiation plus a constant expansion term and the Einstein limit are valid controls. A constructive nonquadratic f(R) with F>0 and f_RR>0 on every finite past interval realizes the same dust/radiation history, so the exclusion cannot be extended to all metric f(R).

[K2265](k2265-shared-cosmology-consistency-2026-10-29.md) already excluded the corresponding vacuum shape. [K2292](k2292-conserved-matter-cosmology-2026-10-30.md) supplied the matter flow. This note tests a prescribed history against its actual required stress and follows the obstruction through a changed-action repair. It neither fits observations nor excludes approximate fits. SC-COS-50/51/54 ASSERTS their native connection-distortion demands; this metric construction is not that object. LT-GR2e and ledger0.263 stay unchanged. No novelty or external-expert certification.

## 1. Full00 coefficient test

Use (-+++), x=1+z (NOT K2283's t=x³), E=H²/H_*², and dimensionless curvature R/H_*² denoted R. The action is C/2 integral sqrt(-g) f(R), C>0. Scaled density q and pressure P include 1/C and H_* units as in K2292. Set

    E=M x³+N x⁴+L, M>0,N,L>=0,
    f=alpha R+beta R²/2-rho_v, F=alpha+beta R,
    R=12E-3xE'=3M x³+12L.

The full00 equation gives, without division by F,

    q_req=3FE-(FR-f)/2-3ExF'
         =3alpha M x³+3N(alpha+12beta L)x⁴
          -(81/4)beta M²x⁶-18beta MNx⁷+3alpha L-rho_v/2.   (1)

Equality to q=d x³+r x⁴ throughout any open x interval is a polynomial identity. Its necessary and sufficient coefficient conditions are

    beta M²=0, d=3alpha M,
    r=3N(alpha+12beta L), rho_v=6alpha L.                 (2)

The x⁷ condition beta MN=0 follows from beta M²=0 over the reals. With beta=1 and M>0, there is no such identity, even after tuning all constant action/dust/radiation coefficients. With alpha,beta>0, F is already positive on x>0; this is a field-equation obstruction, not a sign failure.

For beta>0 the x⁶ term requires negative-density w=1 matter. The x⁷ term, when N>0, requires negative-density w=4/3 matter. Such algebraic repairs lie outside K2292's nonnegative, -1<=w<=1 fluid assumptions. The statement classifies these power-law coefficients; it does not exclude arbitrary interacting, nonminimal or changed-pressure sources.

Controls: M=0,N,L>0 admits radiation plus Lambda with rho_v=6alpha L and r=3N(alpha+12beta L). This expansion is nonconstant although R is constant. beta=0 admits the ordinary Einstein dust/radiation values d=3alpha M,r=3alpha N,rho_v=6alpha L. Neither control belongs to the excluded beta M²!=0 class.

## 2. Full spatial/trace and integrability controls

For arbitrary smooth E>0,F,f,q,P with R=12E-3xE', define

    C00=3FE-(FR-f)/2-q-3ExF',
    L_F=x²EF''+x(2E+xE'/2)F'-xE'F+q+P,
    Box F=-Ex²F''+x(2E-xE'/2)F',
    S=F(3E-xE'/2)-f/2-Ex²F''+x(E-xE'/2)F'-P.

Direct identities give S=-L_F-C00 and

    FR-2f+3Box F+q-3P=-4C00-3L_F.                       (3)

These are the spatial covariant and trace equations with declared signs. Conservation is q'=3(q+P)/x. Defining

    f_rec=RF-6EF+2q+6ExF'

makes C00 identically zero and yields

    f_rec'-F R'=6L_F/x+2[q'-3(q+P)/x].                 (4)

Thus solving L_F=0 with conservation ensures both genuine f_R=F integrability and ALL homogeneous metric equations. Choosing an arbitrary F and solving00 alone does not establish a metric f(R) theory.

## 3. Constructive positive nonquadratic repair

Fix M>0,N,L>=0,alpha,epsilon>0 and the same E on x>=1. Keep ordinary positive sources

    q=3alpha(Mx³+Nx⁴), P=alpha N x⁴.

Let u solve the linear ODE

    x²E u''+x(2E+xE'/2)u'-xE'u=0,
    u(1)=u'(1)=1.                                     (5)

Continuous coefficients with x²E>0 give existence and uniqueness on every finite interval [1,X]. The quadrant u,u'>0 is forward invariant: while u'>0, u increases from1; at a first zero of u', (5) gives u''=E'u/(xE)>0, contradicting arrival at zero from above. Hence u,u'>0 throughout every finite past interval.

Set F=alpha+epsilon u and use f_rec above. Since q+P=alpha xE', (5) is exactly L_F=0. R'=9Mx²>0 permits inversion x(R), so this defines one single-valued f(R) for R>=R(1), smooth at every finite point. Equations(3)-(4) show full background consistency and

    f_R=F>0, f_RR=epsilon u'/(9Mx²)>0.                  (6)

This f cannot be a nonzero quadratic by(1)-(2). It cannot be linear because f_RR>0. The construction supplies an initial-value-defined function, not a source-selected action or a measured parameter. It makes no uniform boundedness or regular asymptotic-endpoint claim as x tends to infinity, and positivity alone does not prove perturbative/local-gravity viability. The M=0 constant-R case must use the explicit radiation control, not divide by R'.

## 4. The constructed repair fails a finite-F high-curvature asymptote

This is an independent requirement on the SAME designer branch, not another fit. Let s=log x, y=u_s=xu', and n=xE'/E. Then(5) is

    y_s=n u-(1+n/2)y.

Take x0=max(1,(L/M)^(1/3)), with x0=1 when L=0. For x>=x0, 3/2<=n<=4: Mx³>=L, N>=0. Since u>=1,y>0, y_s>=3/2-3y. For tau=log(x/x0)>=0, scalar comparison gives

    y>= (1-exp(-3tau))/2,
    u(x)>=u(x0)+tau/2-(1-exp(-3tau))/6.                 (7)

Thus F=alpha+epsilon u diverges as R tends to infinity. Positivity on every finite interval did not supply finite-F recovery at high curvature. If an independently specified GR-recovery condition demands F approach a finite positive constant, this particular positive initial-data designer branch fails it. Other initial conditions, action functions, finite-redshift observations and source-native GU remain outside that exclusion. The Einstein countercontrol has constant F but epsilon=0, outside the nonlinear branch.

## What this settles and what remains

An exact quadratic dust-bearing LCDM transplant is unavailable; further attempts at that identity need not be numerically fitted. Other quadratic matter histories, their initial conditions, coupled perturbations and held-out distance/BAO transport remain meaningful. A free nonquadratic function can repair this particular background, demonstrating why a successful background reconstruction alone cannot select the gravitational action. The next discriminant requires an independently specified matter/source/perturbation demand on the SAME candidate, or a controlled approximate quadratic data test with justified inputs.

## Verification

The probe independently derives(1), checks coefficient sufficiency, both exception classes, equation(3), integrability(4), and the designer reduction. Actual coefficient/sign/source mutations must fail the same predicates. The positive-quadrant and global finite-interval existence proof is analytic above, not a numerical trajectory claim. Standard background equations: [De Felice and Tsujikawa, f(R) theories](https://arxiv.org/abs/1002.4928). No Lean or external-expert certification.
