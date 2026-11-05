---
title: "K2566 What finite calibration determines in the actual localized response"
status: active_research
doc_type: exploration
created: "2026-11-05"
classification: CONVENTIONAL_COMPARATOR
target_claim: NONE-NOT-A-KILL
claim_ceiling: local conserved-observation identifiability and explicit bounded-preparation uncertainty; no physical preparation or global boundary theorem
scripts:
  - tests/channel-swings/k2566_finite_observation_preparation_probe.py
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
result: K2566
carrier: K2564 original metric responses on a common local A7 times B7 product tube LAYER=toy CHIRALITY=N/A
pairing: compact conserved smooth metric-test duality ON=declared_carrier
real_structure: real homogeneous solutions and real calibration functionals
grading: source response, homogeneous response, metric gauge and supplied coefficient norm remain distinct
action_owner: repository-construction -- selected comm/symi/symi completion
target: finite-calibration identifiability and residual readout uncertainty MAP-TYPE=evaluation
```

# Finite calibration does not select the entire local response

## Result and scope

K2564 constructs a response to the actual compact radial source times a B point distribution. It also exhibits one homogeneous response that changes a conserved observation. Here that ambiguity is proved infinite dimensional modulo metric gauge on one common local domain. Any finite list of compact conserved measurements leaves infinitely many such responses. At least one further conserved detector can still take every real value at the same source and unchanged previous readings.

A specified future detector is determined **within the exhibited family** exactly when its response functional belongs to the linear span of the previous response functionals. Thus the result does not say every future detector is unpredictable. The executed successor adds a stated finite-dimensional preparation norm and derives the sharp remaining interval, including feasibility and a nonzero-calibration example. It shows exactly what extra assumption converts arbitrary ambiguity into a finite bound.

These are mathematical statements about the supplied K2564 product/action and local response domain, not about responses satisfying fixed complete global boundary data. SC-ACT-01, SC-GEO-03 and SC-GEO-55 remain ASSERTS at their source scope, and SC-META-53 remains UNCERTAIN. The source/Met(X)/physical quotient bridges and ledger0.263 remain unchanged. No physical preparation, unique measured prediction, novelty, or GU verdict is supplied.

## 1. A common domain with infinitely many actual homogeneous modes

Retain K2564's constants and full homogeneous fields:

    (Y+mu-21K)u=0,
    Qfield_u=u R(1), z_u=0,
    h_u=-rE u R(1), e2_u=-A2^-1 BQfield_u,
    E h_u=-(rE/2)(mu-5K)u R(1).                  (1)

Here E is the formally self-adjoint linearized Einstein operator from the selected system. Its linearized Bianchi identity makes E W conserved, and E annihilates metric gauge. The constant rE is nonzero and mu-5K=(67736495/4439232512)kappa^2>0. R(1) is the unchanged nonzero radial tensor. The full equations, including skew and auxiliary rows, are reused at exactly K2558/K2564's hypotheses.

One need not assume arbitrarily many analytic germs share a common domain. Use the actual B completion coordinates from K2564, on a fixed annulus 0<t_-<t<t_+ with theta and omega on S3. In these coordinates

    Y/K=-d_t^2-3(tanh t+coth t)d_t
         -sech^2(t)Ltheta+csch^2(t)Lomega.

For a real spherical harmonic H_l(theta), Ltheta H_l=l(l+2)H_l, choose omega-independent u_l=v_l(t)H_l(theta), where

    v_l''+3(tanh t+coth t)v_l'
       +[l(l+2)sech^2(t)-(mu/K-21)]v_l=0,
    v_l(t0)=1, v_l'(t0)=0.                         (2)

Every l has a unique real analytic solution throughout the same finite annulus: the linear ODE coefficients are analytic and nonsingular there. Finite linear combinations suffice, so no convergence of an infinite harmonic series is required. At t=t0, harmonic independence proves independence of all u_l. They remain independent on any open angular patch by analytic uniqueness. An isometry of the homogeneous B space form places the source point inside such an annular coordinate patch if necessary; the base response is restricted to that patch. No global extension of these added modes is claimed.

Let V be their real algebraic span on a connected common product tube, with compact detector supports inside it. It is infinite dimensional. Equation(1) shows that u maps injectively to the metric gauge class of h_u: a gauge field has E h=0, whereas nonzero u has E h_u nonzero on some open patch. The positive auxiliary companion of K2564 is not a new physical norm on V.

The only general existence input here is ordinary linear ODE existence on a nonsingular interval. The exact probe checks the actual separated differential expression and six independent zonal S3 harmonics using `(1-z^2)H''-3zH'=-l(l+2)H`. Those finite checks support the formula; the arbitrary-l argument above establishes the infinite-dimensional statement.

## 2. Finite calibration and an actual conserved separating detector

Fix N compact conserved smooth tensors F_i, with linear responses

    ell_i(u)=<F_i,h_u>, L:V -> R^N.

The common kernel ker L is infinite dimensional: the quotient V/ker L has dimension at most N. Thus some nonzero u preserves every previous reading of h0+h_u. Since u is analytic and nonzero, equation(1) is nonzero on a patch disjoint from the B source point. There is a compact smooth tensor W supported in that patch with `<W,E h_u> != 0`; distribution/test duality separates a nonzero smooth tensor even though the metric pairing is indefinite. Put F=E W. Then

    div F=0,
    <F,h_u>=<W,E h_u> != 0.                       (3)

This F is a source-disjoint conserved detector. The complete response h0+a h_u has the same source and all N previous readings, while its F reading ranges over R as real a varies. This uses unrestricted amplitude. It does not preserve an extra norm, a complete boundary condition, or any physical preparation not imposed in the theorem. The detector may depend on the previous detector set and surviving mode; it is not a preselected empirical observable.

## 3. Exact criterion for one specified future detector

For a fixed conserved F write ell(u)=<F,h_u>. On V the following are equivalent:

    ell is constant on every fiber of L;
    ell vanishes on ker L;
    ell belongs to span_R{ell_1,...,ell_N}.          (4)

The first equivalence follows by subtracting two modes. For the second, vanishing on ker L makes ell factor through im L; every linear functional on the finite-dimensional im L extends to R^N. This is algebraic and needs neither a closed-range assumption nor a Hilbert norm. Conversely a linear combination plainly vanishes on ker L. If (4) fails, a kernel mode with nonzero ell gives the arbitrary range above for that specified detector.

This is determination only within V. Other homogeneous solutions or unknown preparation changes may add ambiguity. A detector can be fixed, including identically zero on V, even though the full response is not fixed. A finite calibration does not automatically furnish a global boundary-value theorem.

## 4. Executed successor: a stated preparation bound gives a sharp interval

Choose d actual independent modes from V and write their coefficients alpha in R^d. Supply the ADDITIONAL preparation assumption ||alpha||_2<=R, in this named basis. This norm is external to the field equations and is not invariant under arbitrary changes of mode normalization.

Let L be the real N by d calibration response matrix, y the calibration readings after subtracting h0, and f the row vector of a future response. With L^+ the Moore-Penrose inverse, define

    alpha0=L^+ y, P=I-L^+L.

Feasibility holds iff y lies in im L and ||alpha0||<=R. Every compatible coefficient is alpha=alpha0+z with z in ker L and

    ||z||^2<=R^2-||alpha0||^2.

Orthogonality of the minimum-norm solution and kernel proves that the EXACT additional future-reading interval is

    f alpha0 +/- sqrt(R^2-||alpha0||^2) ||P f^T||.   (5)

Cauchy-Schwarz gives the bound, attained by z proportional to P f^T when it is nonzero. If it is zero the interval collapses, agreeing with (4). If feasibility fails there is no response in the supplied preparation class, not a new field-equation contradiction.

This matrix consumer can be realized using actual compact conserved tests on any chosen finite mode subspace. The tensors E h_j are linearly independent on an off-source open patch by (1) and analytic independence. Smooth compact W tests separate their finite-dimensional span; their restrictions therefore span its full dual. Linear combinations of such W produce any prescribed row, with F=E W conserved. This proves realization of the finite coefficient fixture; no arbitrary matrix is being asserted to be a pre-existing detector.

For three modes take

    L=[[1,1,0],[0,1,1]], y=(1,1), f=(1,0,0), R^2=2.
    alpha0=(1/3,2/3,1/3), ker L=span(1,-1,1).

Formula(5) gives center1/3 and radius2/3, hence interval[-1/3,1]. Both endpoints are attained by exact norm-squared2 coefficients. The detector row(1,2,1), the sum of old rows, is fixed at2. Without the norm bound the first reading is unbounded; pretending calibration sets the kernel coefficient to zero would falsely select1/3. The probe also changes y to an inconsistent redundant calibration and verifies infeasibility.

## Verification and next condition

The note proves the common-domain infinite-dimensional family, gauge distinction, detector separation, exact span criterion and general preparation interval. The probe checks separated equations, harmonics, actual nonzero curvature coefficient, exact matrix realizations and counterexamples; it does not label a finite matrix as an infinite-dimensional proof. Internal independent specialist and hostile review are required. No external-expert, Lean, remote-CI, physical, or novelty certificate is claimed.

Next supply an independently justified preparation norm/domain or a specified detector and test its response functional. A useful next construction is a source-owned boundary/observation restriction with a proved finite or controlled residual space. Merely adding more finite calibration numbers cannot replace that missing condition. K2564 existence, all source polarities and ledger dispositions survive.

[K2564 response](k2564-localized-spectral-response-2026-11-05.md), [K2558 homogeneous equations](k2558-distributional-splitter-overlap-2026-11-05.md), [exact probe](../../tests/channel-swings/k2566_finite_observation_preparation_probe.py), [report](../../lab/process/k2566-finite-observation-preparation.json).
