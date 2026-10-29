---
title: "K2274 An actual BAO test and its initial-data escape"
status: active_research
doc_type: exploration
created: "2026-10-29"
classification: INTERNAL_STRUCTURAL_ONLY
target_claim: NONE-NOT-A-KILL
claim_ceiling: conditional supplied model only; no native GU or canonical verdict
scripts:
  - tests/channel-swings/k2274_desi_fixed_family_test_probe.py
---

# K2274 An actual BAO test and its initial-data escape

> **GU-COMPARATOR-ROUTING — scope before inference.** This artifact contains or borders a conventional particle-physics comparator. Any result about a standard Higgs/VEV, ordinary family index or net chirality, SO(10) `126` Majorana mechanism, anomaly selector, VEV-only breaking or familiar vector-mass route binds only that named model. It is not evidence for or against Weinstein's source-native mechanism without an explicit typed bridge. Read `lab/methods/source-native-comparator-routing.md` and follow its source-native pointers before reusing this result.

Classification: `INTERNAL_STRUCTURAL_ONLY`.

```gu-typed-objects
result: K2274 An actual BAO test and its initial-data escape
carrier: positive smooth real cosmology histories and two correlated distances LAYER=toy CHIRALITY=N/A
pairing: real symmetric positive definite observation form ON=declared_carrier
real_structure: real histories and real observation vectors
grading: no oscillator charge or native Clifford or chirality grading transferred
action_owner: repository-construction -- supplied conditional model
target: all-coefficient observable separation with explicit initial-data scope MAP-TYPE=evaluation
```

## Result and inference boundary

The entire previously fixed [K2271](k2271-forward-cosmology-domain-2026-10-29.md) family lies outside a squared-radius23 ellipsoid of a released DESI DR2 radial/transverse distance pair. The certificate covers all its shared coefficients and all positive common rulers, without sampling ODE solutions. Releasing its one fixed initial slope restores an exact fit to that same pair; a constructive proof below shows why this cannot exclude the whole metric family.

The target remains flat vacuum f(R)=alpha R-b R²/2-rho, b=-1, standard redshift/optics, |a|,|r|<=1, U(1)=2,U_t(1)=1 on x=1+z in[1,2], t=x³, U=y^(3/4). K2271 proves a positive F domain. These arbitrary initial data were inherited unchanged before this comparison, not physically justified or preregistered. The model is not the source-native connection-distortion action. SC-COS-50/51/54 ASSERTS their own source demands; LT-GR2e stays NEEDS and ledger0.263 is unchanged. No radiative-screening revival, native GU exclusion, or source-derived prediction follows.

## 1. Released data and the transport assumption

The [DESI DR2 paper](https://arxiv.org/html/2503.14738v3), Table3 and sectionsIII.1, III.3 and X, defines its compressed distances and links the public likelihood inputs. LRG2 covers0.6<z<0.8 with effective z=0.706, within the existing domain. In order (D_M/r_d,D_H/r_d), the actual released files give

    d=(17.35069094,19.45534918),
    C=[[0.0323752442,-0.0237445646],
       [-0.0237445646,0.111469198]].                   (1)

The off-diagonal is retained. These decimals are exact input data for the algebraic certificate, not exact cosmological constants. The companion probe embeds and hashes the original text. Immutable source snapshots:

- [Mean input](https://raw.githubusercontent.com/CobayaSampler/bao_data/bb0c1c9009dc76d1391300e169e8df38fd1096db/desi_bao_dr2/desi_gaussian_bao_LRG_GCcomb_z0.6-0.8_mean.txt), SHA-256 `6d2f38d0727b2aefcd82fdd5a1c6df5a7d34ad8459437c195d575b5ad0c6ab32`.
- [Covariance input](https://raw.githubusercontent.com/CobayaSampler/bao_data/bb0c1c9009dc76d1391300e169e8df38fd1096db/desi_bao_dr2/desi_gaussian_bao_LRG_GCcomb_z0.6-0.8_cov.txt), SHA-256 `16fa8c323f54139ef1249a24f8f9c8663dbac7890d5a6d9c3b97e84ee89847ae`.

Repository snapshot `bb0c1c9009dc76d1391300e169e8df38fd1096db`, retrieved 2026-10-29T21:12:35.671289+00:00.

This is explicitly CONDITIONAL LIKELIHOOD TRANSPORT: the measured BAO template, tracer physics, fiducial-to-model distance reduction and effective-redshift compression must remain valid for the tested histories. A vacuum late-time ODE supplies none of BAO formation, matter growth or template validity. The paper's covariance is used as a joint error shape; no sigma, p-value, coverage or look-elsewhere correction is inferred here. The result is an exact lower bound on this declared compressed quadratic discrepancy. It is not a fit to the full DESI data set. No future data or generic latest-release claim is needed.

## 2. A finite rational certificate for every background

K2271's full equation and common-domain result give

    |U(t)-(t+1)| <= (7/216)(t-1-log t)
                 <= (7/216)(t-1), 1<=t<=8.           (2)

Put x=853/500, T=x³,

    A=T+1-(7/216)(T-1),
    B(s)=s³+1+(7/216)(s³-1).

Since U(T)>=A>0 and U(s³)<=B(s), and the SAME ruler cancels,

    D_M/D_H = integral_1^x [U(T)/U(s³)]^(2/3) ds
       >= integral_1^x [A/B(s)]^(2/3) ds.              (3)

B increases, so the integrand on the right decreases. For s_i=1+(353/500)i/32, i=1,...,32, use the following integer b_i, divided by10000:

    19959 19504 19055 18614 18181 17757 17340 16933
    16534 16145 15764 15392 15030 14676 14332 13996
    13670 13352 13042 12741 12448 12163 11886 11616
    11354 11100 10853 10612 10379 10151 9931 9716.

Every exact rational inequality (b_i/10000)^3 B(s_i)^2<=A² holds; the probe verifies them without floating roots. The decreasing-integrand right sum then proves

    D_M/D_H >= (353/16000)(454226/10000)
              =1.0021361125>1.                       (4)

This finite quadrature certificate bounds the entire continuous integral and the whole parameter family; it is not a parameter-grid test or an approximate ODE integration. Changing the initial conditions voids (2), which is the explicit dependency tested in section4.

## 3. Correlated separation and discrepancy tolerance

Let v=(-1,1). Every allowed f=(m,h) has v^T f<0. The data have

    g=v^T d=2.10465824,
    V=v^T C v=0.1913335714>0.

C is positive definite. Cauchy-Schwarz in its metric yields, for all allowed f,

    (f-d)^T C^-1(f-d) >= [v^T(f-d)]²/V
                        >g²/V >23.15111914>23.       (5)

Thus even squared-radius23 is separated. This bound is not the optimized likelihood minimum and is not assigned a statistical significance. Arbitrarily small common amplitude does not restore a fit; independent rulers would change the model.

A useful robustness successor is available without claiming a supplied calibration. If an additive model/measurement discrepancy e obeys |v^T e|<=eta<g, replace g by g-eta. In particular eta<=1/3 still leaves (g-eta)²/V>16. Thus the radius16 ellipsoid remains separated under that explicitly bounded projected discrepancy. This is a tolerance requirement on transport, not evidence that actual survey systematics satisfy it. Independent errors |e_M|,|e_H|<=1/6 suffice. The full two-dimensional covariance, including its negative cross term, is essential to the numerical values.

## 4. Constructive escape when one initial slope is released

Keep the same action with a=r=0,b=-1 and fix U(1)=2, but allow

    U_s(t)=2+s(t-1), 0<=s<=1.                         (6)

U_tt=0 solves the exact full constraint. U>=2 and U-tU_t=2-s>=1, so F=12 U^(1/3)(2-s)>0 on the complete interval. Define

    Aobs(s)=integral_1^x [U_s(T)/U_s(w³)]^(2/3)dw.

This is continuous and strictly increasing: the logarithmic derivative of its integrand is

    (4/3)(T-w³)/(U_s(T)U_s(w³))>0 for w<x.            (7)

Aobs(0)=353/500, whereas Aobs(1)>1 by (4). The exact observed ratio is

    d_M/d_H=867534547/972767459 in(353/500,1).

The intermediate-value theorem and strict monotonicity give a UNIQUE s* in(0,1) that fits this ratio. Set the common amplitude lambda=d_H U_s*(T)^(2/3)>0. Then h=d_H and m=d_M simultaneously, with one ruler and unchanged distance origin. No numerical root is required for existence/uniqueness.

The case s=0 is the valid constant-curvature pure-R² control; no division by s or U_t was used. This is an exact counterexample to extending the fixed-IVP exclusion to all initial data. It neither fits other bins nor establishes perturbative stability, physical initial-data selection or BAO transport. The slope was now adjusted using these data, so it earns no independent predictive credit.

## Verification and next decision

The probe checks all32 cubic certificate inequalities, covariance/support algebra, exact discrepancy bounds, the pure-R² full equation and slope derivative, plus altered redshift, endpoint, quadrature, covariance, observation-order, action and slope faults. Universal existence and likelihood-transport assumptions remain in the written argument; a finite check cannot validate survey applicability. Internal independent review is not external-expert, proof-assistant, novelty or remote-CI certification.

A useful next test keeps an independently specified shared initial-data/coefficient domain and confronts additional jointly valid bins, with the actual template/growth transport assessed. The one-bin free-slope fit is a constructive survival result, not grounds to repeat arbitrary synthetic tubes or to proclaim this conditional vacuum family viable.
