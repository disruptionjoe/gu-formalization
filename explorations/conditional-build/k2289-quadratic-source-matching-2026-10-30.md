---
title: "K2289 Finite sources and local endpoint matching"
status: active_research
doc_type: exploration
created: "2026-10-30"
classification: INTERNAL_STRUCTURAL_ONLY
target_claim: NONE-NOT-A-KILL
claim_ceiling: conditional supplied models only; no native GU, empirical or hardware acceptance
scripts:
  - tests/channel-swings/k2289_quadratic_source_matching_probe.py
---

# K2289 Finite sources and local endpoint matching

> **GU-COMPARATOR-ROUTING — scope before inference.** This artifact contains or borders a conventional particle-physics comparator. Any result about a standard Higgs/VEV, ordinary family index or net chirality, SO(10) `126` Majorana mechanism, anomaly selector, VEV-only breaking or familiar vector-mass route binds only that named model. It is not evidence for or against Weinstein's source-native mechanism without an explicit typed bridge. Read `lab/methods/source-native-comparator-routing.md` and follow its source-native pointers before reusing this result.

Classification: `INTERNAL_STRUCTURAL_ONLY`.

```gu-typed-objects
result: K2289 Finite sources and local endpoint matching
carrier: real radial source densities and a frozen weak-field scalar response LAYER=toy CHIRALITY=N/A
pairing: declared real metric scalar pairing ON=declared_carrier
real_structure: real metric histories and perturbations
grading: no native Clifford or chirality transfer
action_owner: repository-construction -- supplied conditional model
target: positive-source Green response MAP-TYPE=evaluation
```

## Result and exact scope

The SAME [K2283](k2283-global-quadratic-cosmology-2026-10-30.md) quadratic model has an explicit finite-radius source response in a declared frozen, weak-field approximation. Positive sources do not suppress its scalar charge by increasing density. More sharply, uniform weak-field spherical environments of compactness at most epsilon cannot equalize its cosmological endpoint coefficients: the endpoint-only ratio remains between Xi/sqrt(1+epsilon) and Xi sqrt(1+epsilon). For epsilon=0.001 and K2286's inherited interval, this lies within (0.6347,0.6355), far from one.

This bounds an endpoint substitution, NOT a complete emitted/detected wave, nonlinear screening, or an empirical standard-siren distance. Background gradients, time derivatives, shell stresses and metric backreaction are omitted by the specified approximation. SC-COS-50/51/54 ASSERTS and LT-GR2e/LT-GR10/11 are unchanged; this supplied metric theory is not the native connection-distortion action. No new GU or survey confidence claim follows.

## 1. Fixed coefficients, source equation and exact Green function

Use signature(-+++), f(R)=alpha R+R²/2-rho_v, and action C/2 integral sqrt(-g) f(R), with C>0 and kappa=1/C. Metric variation gives

    3 Box R-alpha R+2rho_v=kappa T.

For nonrelativistic positive density rho_m, T=-rho_m. A constant-density equilibrium has R_eq=(2rho_v+kappa rho_m)/alpha, so F_eq=alpha+R_eq>0 for alpha,rho_v>0. There is NO high-density positive-F obstruction. The trace mass m²=alpha/3 is independent of density, but this alone is not a nonlinear screening theorem.

Subtract a frozen background and grant the local static Euclidean operator, neglecting the variation of Box on the rolling background. With delta F=delta R, the declared problem is

    (Laplacian-m²)delta F=-kappa rho_m/3,
    delta F regular at r=0 and vanishing at infinity.

The unique decaying solution is kappa/(12pi) times the convolution of rho_m with exp(-m|x-y|)/|x-y|. The approximation must be justified before importing this as a source matched to the rolling metric. [K2291](k2291-rolling-scalar-applicability-2026-10-30.md) explicitly retains rolling metric constraints in its different cosmological problem.

For any radial nonnegative source supported on r<=L, total mass M>0, the exterior is

    delta F(r)=kappa M/(12pi r) A exp(-mr), r>=L,
    A=(1/M) integral_0^L 4pi s² rho_m(s) sinh(ms)/(ms) ds >=1.

Linearity makes A independent of an overall density amplitude. This is not an inverse thin-shell factor. For a uniform sphere, x=mL,

    A(x)=3[x cosh(x)-sinh(x)]/x³,
    delta F_in(r)=kappa rho_m/(3m²)
           [1-(1+x)exp(-x) sinh(mr)/(mr)].

These expressions have continuous value and first derivative at L, solve their respective equations and possess regular m->0 limits. A>=1 follows sinh(y)/y>=1, including y=0 by continuity. It does NOT preclude range suppression: for r>L, A(mL)exp(-mr) tends to zero as mL grows at fixed r/L>1. Large range parameter and high density are different changes. This is the explicit contrary construction.

## 2. Weak environments cannot erase this endpoint mismatch

Green positivity and exp(-md)<=1 give 0<=delta F<=delta F_massless pointwise. For a uniform sphere, the massless maximum is at the center and equals kappa M/(8pi L). Thus with background Fb>0 and Phi=kappa M/(8pi Fb L),

    0<=delta F/Fb<=Phi.

This is a uniform bound for all mL>=0 and every point, including the exterior. Phi is the tensor-normalized compactness parameter; it is not a measured potential imported from an unspecified matter completion.

Take separately specified source and observer environments with background Fe,Fo from K2286 and Phi_e,Phi_o<=epsilon. Then

    sqrt(Fo/Fe)/sqrt(1+epsilon)
      <=sqrt[(Fo+delta Fo)/(Fe+delta Fe)]
      <=sqrt(Fo/Fe)*sqrt(1+epsilon).

K2286 has 0.63506<sqrt(Fo/Fe)<0.63509; epsilon=1/1000 yields the outward bound quoted above. Equality of the local coefficients would require

    Phi_o >= Fe/Fo-1 >1.479,

because delta Fe>=0. This is incompatible with the assumed Phi_o<=0.001. It excludes equalization by this weak spherical positive-source class; it does not exclude a nonlinear environment or a changed action. Overall action normalization changes kappa but cannot evade a bound stated in the same Phi. Overlapping or nonuniform sources need their own potential bound; do not use the uniform-sphere maximum for arbitrary concentrated density at fixed M,L.

For the SAME witness, alpha/H_*²=33.8 and H0/H_*=2^(2/3), hence m/H0=sqrt(33.8/3)/2^(2/3), between2.114 and2.115. For scales declared small compared with H0^-1, density alone cannot make mL large. This conditional dimensional relation is not a measured local range or a cosmological fit with matter included.

## 3. Followthrough beyond spherical environments

The same kernel comparison works for any compact nonnegative density if the actual potential is bounded. Define the tensor-normalized massless potential magnitude

    W(x)=kappa/(8pi Fb) integral rho_m(y)/|x-y| d³y.

Then 0<=delta F(x)/Fb<=2W(x)/3. Thus the endpoint inequality extends to arbitrary geometry with 2W_o/3,2W_e/3<=epsilon. A fixed total mass and outer radius alone do not give this bound: concentrating a uniform mass into radius L/100 increases its massless center value by100. The spherical compactness shortcut must not be exported to arbitrary density.

The precise missing rolling term can also be written. For Newtonian-gauge ds²=-(1+2Psi)dt²+a_c²(1-2Phi)dx² and homogeneous background Rbar,

    delta Box Rbar=2Psi(ddot Rbar+3H dot Rbar)
                        +(dot Psi+3dot Phi)dot Rbar.

It follows by varying (sqrt(-g))^-1 partial_t[sqrt(-g)g^00 dot Rbar]. Consequently the coupled linear trace equation is

    (Box_bar-alpha/3)delta R=kappa delta T/3-delta Box Rbar.

Matter can legitimately perturb a vacuum background when the metric also perturbs. The frozen Green model drops a specified metric term; it does not show such matter response is forbidden. A controlled matching claim must bound that term and its other local approximations in the intended source/detector problem. No frequency hierarchy or waveform transfer is inferred merely from a local radius.

## 4. What this changes and what it does not

Earlier K1864/K1866 own constant-background Yukawa/slip controls. The new consumer is an exact finite-radius positive-source bound tied to the fixed full13-compatible history and its local endpoint mismatch. More point-source formulae or arbitrary fitted coefficients cannot answer the next problem. A full matching construction must retain the coupled metric response, time dependence, admissible stress, tensor preparation and interface reflection; endpoint coefficients alone do not give the complete waveform. The constrained rolling scalar calculation is performed separately rather than inferred from m²>0.

Symbolic PDE/matching identities, positive-kernel proof, exact inequalities and inherited interval hashes are distinguished in the probe. Finite numeric range controls are illustrations. [De Felice and Tsujikawa](https://arxiv.org/abs/1002.4928) provide standard metric-f(R) background; the conditional sphere/endpoint composition above is derived here. No novelty, external-expert, Lean or empirical acceptance is claimed.
