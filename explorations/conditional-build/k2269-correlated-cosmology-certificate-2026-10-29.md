---
title: "K2269 A joint uncertainty certificate for shared cosmology"
status: active_research
doc_type: exploration
created: "2026-10-29"
classification: INTERNAL_STRUCTURAL_ONLY
target_claim: NONE-NOT-A-KILL
claim_ceiling: conditional supplied model only; no source or canonical verdict
scripts:
  - tests/channel-swings/k2269_correlated_cosmology_certificate_probe.py
---

# K2269 A joint uncertainty certificate for shared cosmology

> **GU-COMPARATOR-ROUTING — scope before inference.** This artifact contains or borders a conventional particle-physics comparator. Any result about a standard Higgs/VEV, ordinary family index or net chirality, SO(10) `126` Majorana mechanism, anomaly selector, VEV-only breaking or familiar vector-mass route binds only that named model. It is not evidence for or against Weinstein's source-native mechanism without an explicit typed bridge. Read `lab/methods/source-native-comparator-routing.md` and follow its source-native pointers before reusing this result.

Classification: `INTERNAL_STRUCTURAL_ONLY`.

```gu-typed-objects
result: K2269 A joint uncertainty certificate for shared cosmology
carrier: real polynomial reconstruction coefficients and a shared interval action LAYER=toy CHIRALITY=N/A
pairing: real history integration and finite quadratic ellipsoid form ON=declared_carrier
real_structure: real reconstruction coefficients and symmetric matrices
grading: no native chirality or Clifford grading transported
action_owner: repository-construction -- supplied conditional model
target: robust common-coefficient separation with an explicit reconstruction-bias budget MAP-TYPE=evaluation
```

## Result and scope

A finite-dimensional reconstruction carries correlated uncertainties into every weak window through one common coefficient vector. A small positive-semidefinite matrix certificate can then reject ALL common action coefficients in a specified interval and every value of rho/b, without independent fits, nonlinear sampling, or a fabricated chi-square law. The concrete two-parameter example below proves a positive residual margin at reconstruction amplitude10^-4 and retains a rigorous nonpolynomial discrepancy allowance10^-8 in C1.

The fixed flat vacuum metric action, standard redshift/optics and dimensionless normalization are those of [K2265](k2265-shared-cosmology-consistency-2026-10-29.md). This is a supplied model, not the native connection-distortion theory: SC-COS-50/51/54 ASSERTS their source demands, LT-GR2e/ledger0.263 unchanged. No observed data, native prediction, survey confidence, or novelty is claimed. [K2268](k2268-observation-regularity-cosmology-2026-10-29.md) addresses a distinct nonparametric observation class; neither construction authenticates the other's assumptions.

## 1. Exact nonlinear propagation from one reconstruction

Let y_c=sum_k c_k phi_k, with specified real C2 basis on one compact interval. Define K2266's weak residuals q_j,A_j,B_j from windows w_j. There are explicit symmetric matrices Q_j and row vectors a_j such that

    q_j=c^T Q_j c, A_j=a_j c, B_j=-(1/2)integral w_j,
    (Q_j)_kl=integral [(45/4)x²w_j phi_k'phi_l'
                         -(9/2)ell_j phi_k phi_l],
    (a_j)_k=3 integral w_j phi_k,
    ell_j=x²w_j''+6xw_j'+4w_j.                    (1)

The same uncertain c generates both q and A. Plugging q covariance into a fixed-design regression discards that dependence and is not justified here. Specify c=c0+Lu, ||u||2<=1. Choose one FIXED signed window vector v with v·B=0, then put

    Q=sum v_j Q_j, d=sum v_j a_j,
    R(a,u)=u^T H u+2g(a)^T u+k(a),
    H=L^T QL, g(a)=L^T Qc0+(a/2)L^T d^T,
    k(a)=c0^T Qc0+a d c0.                        (2)

Any exact solution must have R=0. A fixed v is enough for a sufficient exclusion; the absence of such a separator is not proof of compatibility.

## 2. Endpoint certificates retain the same action parameters

For each endpoint a=a_minus,a_plus, suppose m>0 and lambda_a>=0 satisfy

    Z_a = [[H+lambda_a I, g(a)],
           [g(a)^T, k(a)-m-lambda_a]] >=0.        (3)

Then R(a,u)-m=[u;1]^T Z_a[u;1]+lambda_a(1-||u||²)>=0 on the ball. For every fixed u the residual is affine in a, so the two endpoint bounds imply R>=m throughout the entire coefficient interval. One common m is used; lambdas may differ. This is the elementary sufficient direction of the established S-procedure, proved here directly. We do not need or claim that the whole cosmology feasibility problem is equivalent to one matrix certificate. PSD can be verified by exact LDL or principal-minor tests; a floating optimizer's status is not a proof.

## 3. An exact two-mode uncertainty example

Use [1,2], y0=1+x³, the three windows and v of K2268, and

    y=1+x³+delta(u1+u2 x), ||u||<=1, delta=1/10000,
    a in [-100,100], r unrestricted.

Let M_n=integral w0(649-870x+287x²)x^n/1806. Exact integration gives

    M0=M3=0, M1=-1/168560, M2=-1/113778,
    M4=83/2085930, M6=7621/18078060.

For t=delta u1,s=delta u2, direct strong-Q substitution independently gives

    R= (81/4)M6 + [(18+3a)M1+(63/2)M4]s
                  +18M1 ts+(81/4)M2 s².          (4)

Thus H=delta²[[0,9M1],[9M1,81M2/4]], g=delta(0,[(18+3a)M1+(63/2)M4]/2), and k=205767/24104080. The two exact matrices (3) with

    m=1/200, lambda_minus=lambda_plus=1/1000     (5)

are positive definite. Their first two leading minors are 1/1000 and
284124735494319999919/284124736000000000000000000. The third minors are respectively
4777328098353873426598050367/1883355475793792000000000000000000000 and
4777328136787828986598050367/1883355475793792000000000000000000000.
The probe recomputes them from integrals, rather than assuming their positivity. All reconstructions have y>0, |y|<10 and |y'|<13. No independent r value can cancel the combined residual because v·B=0 exactly.

This does not claim all uncertainty directions are so harmless. Here constant perturbations cancel linearly; the cross term and slope direction survive. Altering the uncertainty basis, scale or action-coefficient interval requires a fresh certificate.

## 4. Nonpolynomial bias is a separate required input

An exact polynomial ansatz is a modeling assumption, not a consequence of finite nodes. Suppose the actual C3 history yt differs from some y_c above by sup norm tau0 and derivative sup norm tau1, with BOTH histories bounded by M=10,V=13. For |a|<=100, K2266 gives

    |v·(q[yt]+a A[yt])-R(a,u)| <= K0 tau0+K1 tau1,
    K0=sum |v_j|[90 integral |ell_j|+300 integral |w_j|],
    K1=sum |v_j|(585/2) integral |w_j|x².         (6)

For tau0=tau1=tau, the conservative polynomial coefficient bound already checked by K2266 gives K0+K1<=2589985595/7224. At tau=10^-8, this is strictly less than m=1/200. Hence the exact certificate continues to exclude every actual history in that joint reconstruction-plus-bias class. The bias budget is independently supplied; it is not the least-squares residual and is not inferred from finite data. A missing bias bound leaves only the exact reconstruction-class result. Small bias also preserves the stated y/M/V bounds (the displayed reconstruction has strict slack).

## 5. Connecting an actual linear observation model

If supplied measurements are d=E c+e, e^T Sigma^-1 e<=q, Sigma SPD, and E has full column rank, define

    G=E^T Sigma^-1 E,
    chat=G^-1 E^T Sigma^-1 d,
    d0=(d-E chat)^T Sigma^-1(d-E chat).

Completion of the square gives EXACTLY

    (d-Ec)^T Sigma^-1(d-Ec)
       =d0+(c-chat)^T G(c-chat).                 (7)

If d0>q the stipulated observation/reconstruction model is inconsistent; if d0=q it allows a singleton; if d0<q choose L with LL^T=(q-d0)G^-1. A rank-deficient E leaves unbounded directions unless a separate restriction is supplied. Neither a pseudoinverse alone nor discarding d0 fixes that. Correlated Sigma must be used in both terms.

The two-mode example can be realized as an exact toy observation: measure residual y-y0 at x=1,2, with E=[[1,1],[1,2]], d=0, q=1 and Sigma=delta² E E^T. Then chat=0,d0=0,G=delta^-2 I and the coefficient uncertainty ball is exactly the specified one. This is a declared mathematical instrument, not a claim that two real measurements fix a cosmic history. For measurements of an actual history y_c+b, its sampled discrepancy must already be included in the observation error set used to infer the coefficient ellipsoid (or that ellipsoid must be supplied independently). Separately, (6), or another continuous residual-bias bound, is required to transfer separation to the actual history. Enlarging nodal errors alone never controls the off-node residual. The exact-ansatz toy above sets b=0. A fixed H/ruler normalization and standard optics are assumptions here; freely varying rulers or initial-state nuisances need their own common parameter treatment.

## Verification and remaining discriminator

The probe compares strong and weak expressions, exact moments and PSD minors, a correlated GLS identity and genuinely altered-input faults. These establish the displayed finite calculations. The universal robust implication is the written algebraic proof, reviewed internally, not a statistical confidence claim. Background: [Vandenberghe and Boyd, Semidefinite Programming](https://stanford.edu/~boyd/papers/sdp.html) gives the established PSD/S-procedure setting; no new optimization theorem is asserted.

This result turns a supplied joint reconstruction/error class into a usable rejection certificate. It does not produce the actual cosmological data, regularity or model-discrepancy budget. That empirical interface or a rigorously enclosed forward family is the next independent input, rather than another arbitrary ellipsoid refinement. No external-expert, Lean, remote-CI or empirical certification.
