---
title: "K2271 A common forward cosmology domain and ruler test"
status: active_research
doc_type: exploration
created: "2026-10-29"
classification: INTERNAL_STRUCTURAL_ONLY
target_claim: NONE-NOT-A-KILL
claim_ceiling: conditional supplied model only; no source or canonical verdict
scripts:
  - tests/channel-swings/k2271_forward_cosmology_domain_probe.py
---

# K2271 A common forward cosmology domain and ruler test

> **GU-COMPARATOR-ROUTING — scope before inference.** This artifact contains or borders a conventional particle-physics comparator. Any result about a standard Higgs/VEV, ordinary family index or net chirality, SO(10) `126` Majorana mechanism, anomaly selector, VEV-only breaking or familiar vector-mass route binds only that named model. It is not evidence for or against Weinstein's source-native mechanism without an explicit typed bridge. Read `lab/methods/source-native-comparator-routing.md` and follow its source-native pointers before reusing this result.

Classification: `INTERNAL_STRUCTURAL_ONLY`.

```gu-typed-objects
result: K2271 A common forward cosmology domain and ruler test
carrier: positive real smooth expansion histories on a compact redshift interval LAYER=toy CHIRALITY=N/A
pairing: real scalar histories and real symmetric finite observation pairing ON=declared_carrier
real_structure: real histories and real observation vectors
grading: no native chirality or Clifford grading transported
action_owner: repository-construction -- supplied conditional model
target: uniform shared-coefficient background existence and observable separation MAP-TYPE=evaluation
```

## Result and scope

The conditional flat vacuum metric family of [K2265](k2265-shared-cosmology-consistency-2026-10-29.md) has a nontrivial two-parameter set of solutions on the SAME redshift interval, with fixed initial data and a uniform strictly positive Ricci coefficient F. A power substitution permits a rigorous contraction proof, rather than sampled ODE integration. Its successor is a whole-family, common-ruler observable separation with correlated errors. No continuous reconstruction-bias assumption is needed for this FORWARD model test.

This is the supplied f(R)=alpha R-b R²/2-rho metric action, not the source-native connection-distortion action. SC-COS-50/51/54 ASSERTS their source demands; LT-GR2e and ledger0.263 remain unchanged. Standard redshift/optics, vacuum, flatness and initial data are assumptions. The test below uses synthetic observations, not DESI or survey confidence. It does not revive the local horn's failed radiative screening.

## 1. Remove the derivative-square term before integrating

Use dimensionless x=1+z in [1,2], y=H²>0, a=alpha/b, r=rho/b. K2265's full 00 constraint is

    18xyy'+(9/4)x²(y')²-9x²yy''+3ay-r/2=0.

Set t=x³ and U=y^(3/4). Here t is a REDSHIFT COORDINATE, not cosmic time. Direct chain rule cancels both the first-derivative and derivative-square terms:

    Q=-108t² U^(5/3) U_tt,
    U_tt=g(t,U)=a/(36t² U^(1/3))-r/(216t² U^(5/3)),     (1)
    R=12U^(1/3)(U-tU_t).

No division by y' or F occurs. Positivity of U is essential; singular y=0 branches are outside this chart. K2265's off-shell identity then supplies the trace and spatial equations from the full constraint on these smooth positive histories. Its degenerate F=0 branches remain separate.

## 2. One entire parameter box, one interval and one initial state

Fix |a|,|r|<=1, b=-1, U(1)=2 and U_t(1)=1. Let U0=t+1 and consider the complete closed sup-norm tube

    B={U in C[1,8]: ||U-U0||infinity<=1/4}.

Every member obeys U>=7/4>1. The Volterra map is

    (TU)(t)=t+1+integral_1^t (t-s)g(s,U(s))ds.

On B, use the conservative bounds |g|<=7/(216t²), |g_U|<=11/(648t²), and integral_1^t(t-s)/s² ds=t-1-log t<=7. Therefore

    ||TU-U0||<=49/216<1/4,
    ||TU-TV||<=q||U-V||, q=77/648<1.                    (2)

Banach's theorem proves a unique fixed point in B, smooth by (1). Ordinary local IVP uniqueness on U>0 prevents another positive solution with the same initial data from separating while both exist. This proves a common domain for the WHOLE parameter box, not a numerical grid.

Put W=U-tU_t. Then W'=-t g and W(1)=1, so

    W>=1-(7/216)log8>65/72,
    F=R-a>12*(65/72)-1=59/6.                           (3)

We used log8<3 and U^(1/3)>1. The background is nonempty for every shared coefficient pair. For a=r=0, U=t+1 recovers K2265's known pure-R² control. For a=1,r=0, U<=37/4<27 gives g>1/(108t²), hence

    U(8)-9>(7-log8)/108>1/27.                          (4)

This is a genuinely different nonzero-coefficient solution. Positive F is NOT perturbative stability: the trace mass coefficient is -a/3, negative for that example. Choosing a=-1 changes that sign but does not establish full perturbative viability either.

## 3. Certified approximation and parameter cells

Exact Picard iterates U_n=T^n U0 have

    ||U-U_n||<= (49/216) q^n/(1-q).                    (5)

For any continuous V in B with a RIGOROUS residual bound ||TV-V||<=delta, the a posteriori error is delta/(1-q). These statements do not certify floating quadrature or an approximate nonlinear evaluation: their errors must enter delta. For two parameter pairs with the same initial data, the direct difference of g and (2) give

    ||U(a,r)-U(ahat,rhat)||
      <=(126|a-ahat|+21|r-rhat|)/571.                   (6)

Thus a validated parameter-cell calculation can cover a continuum. No finite mesh alone proves rejection. The tube itself already gives the uniform example in section5 without quadrature.

## 4. One shared ruler, radial and integrated observables

Restore H=H_* U(x³)^(2/3) and c=1. The normalized ratios in (1) correspond to physical a_phys=H_*² a and r_phys=H_*⁴ r; free scale is not an extra solution with fixed dimensionful coefficients. For b=-1 the restored bound is F_phys>H_*²(59/6). Let rho_d=H_* r_d>0, the ONE shared ruler. Then

    h(x)=D_H/r_d=rho_d^-1 U(x³)^(-2/3),
    m(x)=D_M/r_d=rho_d^-1 integral_1^x U(s³)^(-2/3)ds. (7)

The distance origin is fixed at x=1. No independent distance offsets or pointwise rulers are permitted. On U,V>=1, derivative magnitude of u^(-2/3) is at most2/3. A history error epsilon therefore gives radial error<=2epsilon/(3rho_d) and transverse error<=2(x-1)epsilon/(3rho_d), plus an independently bounded quadrature error. Parameter variation (6) can be composed with this bound.

For any fixed nonzero real shape vector f from both observables, data d and SPD weight matrix M, minimizing over the common amplitude lambda=1/rho_d>=0 yields

    q(f)=d^T M d-max(0,f^T M d)^2/(f^T M f).            (8)

This is completion of the square, including covariance cross terms. For the physical lambda>0, a nonpositive cross term gives an infimum at zero that is not attained. It must not be called an allowed best fit. Equation (8) is a deterministic distance; a statistical confidence law needs its own justified measurement model and parameter treatment.

## 5. A complete interval and all-ruler rejection

The fixed initial value and tube imply U(1)=2 and U(8)>=35/4>8. Consequently, for EVERY pair (a,r) in the box and every common rho_d>0,

    h(2)/h(1)=(2/U(8))^(2/3)<1/2,                    (9)

since U(8)²>32. Take synthetic radial observations d=(1,1), error shape C=[[1,1/2],[1/2,1]] and simultaneous deterministic squared radius1/16. Let v=(-1,2). Every model vector f has v^T f<0, but v^T d=1 and v^T C v=3. Ellipsoid support would require

    |v^T(f-d)|<=sqrt(3)/4<1,

a contradiction. This excludes the entire specified initial-state/coefficient/ruler family at once, without sampled solutions or independent nuisance fits. Pure-R² generated data (1,(2/9)^(2/3)) have zero residual with an appropriate common ruler and are the positive control. Giving each point its own ruler would falsely fit (1,1) exactly; that changes the model. Additional transverse coordinates and full covariance may be used: the same radial separator remains valid if its covariance subblock is unchanged.

The selected initial data are material: this is not a rejection of all initial states of the metric family, much less GU. Allowing them to vary requires a new uniform domain and observable family. Nor are the synthetic errors a calibrated survey product.

## Verification and remaining input

The exact companion probe independently checks the chain-rule equation, curvature, contraction constants, nonzero-coefficient separation, shared-amplitude profile, correlated ellipsoid and wrong-ruler countercontrol. Universal existence and whole-family implications are written proofs subject to independent internal review, not inferred from sampled checks. No Lean, external-expert, empirical, novelty or remote-CI certificate is claimed. Metric f(R) equations are established background; see [De Felice and Tsujikawa](https://arxiv.org/abs/1002.4928).

The next observational calculation needs an actual jointly calibrated radial/transverse likelihood and an initial-data/coefficient domain selected independently of the comparison. This result supplies an explicit certified forward-domain example and a usable deterministic discriminator; it does not provide those empirical inputs. Repeating an arbitrary smaller tube would not supply them.
