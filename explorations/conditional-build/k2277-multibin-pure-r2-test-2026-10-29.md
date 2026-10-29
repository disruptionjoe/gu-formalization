---
title: "K2277 A shared multi-bin test of every positive pure-R2 initial state"
status: active_research
doc_type: exploration
created: "2026-10-29"
classification: INTERNAL_STRUCTURAL_ONLY
target_claim: NONE-NOT-A-KILL
claim_ceiling: conditional supplied model only; no native GU or canonical verdict
scripts:
  - tests/channel-swings/k2277_multibin_pure_r2_test_probe.py
---

# K2277 A shared multi-bin test of every positive pure-R2 initial state

> **GU-COMPARATOR-ROUTING — scope before inference.** This artifact contains or borders a conventional particle-physics comparator. Any result about a standard Higgs/VEV, ordinary family index or net chirality, SO(10) `126` Majorana mechanism, anomaly selector, VEV-only breaking or familiar vector-mass route binds only that named model. It is not evidence for or against Weinstein's source-native mechanism without an explicit typed bridge. Read `lab/methods/source-native-comparator-routing.md` and follow its source-native pointers before reusing this result.

Classification: `INTERNAL_STRUCTURAL_ONLY`.

```gu-typed-objects
result: K2277 A shared multi-bin test of every positive pure-R2 initial state
carrier: real positive flat cosmology histories and correlated distance vectors LAYER=toy CHIRALITY=N/A
pairing: positive real observation covariance ON=declared_carrier
real_structure: real histories and real observation vectors
grading: none; no oscillator, native Clifford or chirality grading
action_owner: repository-construction -- supplied conditional model
target: all-initial-data correlated-distance certificate MAP-TYPE=evaluation
```

## Result and scope

The one-bin escape in [K2274](k2274-desi-fixed-family-test-2026-10-29.md) fails a shared three-observable test: every expanding flat vacuum pure-R² history with positive F on 0<=z<=1 lies outside the declared squared-radius4 ellipsoid of selected DESI DR2 compressed distances. The proof covers all allowed initial slopes and all positive common ruler scales. It does not choose initial data by fitting a prior.

This is a deterministic discrepancy statement, CONDITIONAL on standard redshift/flat optics and valid BAO template/effective-redshift likelihood transport. It is not a calibrated confidence level or p-value. The target is the supplied metric action f(R)=R²/2, not general alpha R+R²/2-rho, matter/curvature extensions, contracting or singular histories, F<=0, or the source-native connection action. SC-COS-50/51/54 ASSERTS their separate source demands; LT-GR2e and ledger0.263 remain unchanged. In particular there is no GU falsification or revival of radiative screening.

## 1. Eliminate the initial-amplitude nuisance honestly

Use [K2271](k2271-forward-cosmology-domain-2026-10-29.md)'s exact positive-H chart y=H², U=y^(3/4), t=x³, x=1+z. The full pure-R² vacuum constraint reduces to U_tt=0; its solutions are U=A0+B0t. Since

    F=12 U^(1/3)(U-t U_t)=12 A0 U^(1/3),

positive F requires A0>0. Normalize U(1) to2 by multiplying U by2/U(1). The common positive distance amplitude lambda absorbs this change, so no observable family is lost. Every allowed history is represented by

    U_s(t)=2+s(t-1),   -2/7<s<2,   lambda>0,       (1)
    h(x)=D_H/r_d=lambda U_s(x³)^(-2/3),
    m(x)=D_M/r_d=lambda integral_1^x U_s(w³)^(-2/3)dw.

The lower slope bound is U_s(8)>0; the upper is A0=2-s>0. Negative slopes are included. The boundary s=2 has F=0 and is not silently added. Constant curvature s=0 is included with no division by s. Thus U(1)=2 is a scale convention, unlike fixing the slope in K2274.

## 2. Two inequalities cover the whole slope line

Let x1=151/100, x3=967/500 and s0=3/8. For positive U,

    d_s log[U_s(x1³)/U_s(w³)]^(2/3)
      =4(x1³-w³)/(3 U_s(x1³) U_s(w³))>=0,
    d_s log[h(x3)/h(x1)]
      =4(x1³-x3³)/(3 U_s(x1³) U_s(x3³))<0.         (2)

The first derivative is strictly positive for w<x1 and zero at w=x1; its integral is strictly increasing. Hence the low-slope branch satisfies m1/h1<=m1(s0)/h1(s0), and the high-slope branch satisfies h3/h1<=h3(s0)/h1(s0). The following exact rational bounds suffice:

    s<=3/8:  m1/h1 <293/500,
    s>=3/8:  h3/h1 <96/125.                        (3)

For the first, the integrand at s0 is decreasing in w. At the128 LEFT endpoints w_i=1+(51/100)i/128, i=0,...,127, choose the least integer b_i with

    b_i³ U_s0(w_i³)² >= 10^18 U_s0(x1³)².

The probe generates these integers by exact binary search, then verifies both their defining inequality and minimality. Their sum is146996588. The upper Riemann sum is

    (51/12800) sum_i b_i/10^6
       =1874206497/3200000000 <293/500.              (4)

This bounds the continuous integral, not merely sampled parameters. For the second inequality in(3), cube both positive sides and check exactly

    (96/125)³ U_s0(x3³)² > U_s0(x1³)².              (5)

## 3. Released data, original covariance and all-ruler separation

The original joint mean/covariance files are pinned to immutable revision `bb0c1c9009dc76d1391300e169e8df38fd1096db` of [CobayaSampler/bao_data](https://github.com/CobayaSampler/bao_data/tree/bb0c1c9009dc76d1391300e169e8df38fd1096db/desi_bao_dr2). The companion report embeds the two complete text inputs and SHA-256 hashes. The [DESI DR2 paper](https://arxiv.org/html/2503.14738v3) defines the compressed distances and their inference assumptions. Here the new inputs are LRG1 z=.510 and LRG3+ELG1 z=.934; no private or reconstructed covariance is substituted.

Select coordinates (m1,h1,h3) by observable label and redshift, rather than guessing row positions:

    d=(13.58758434,21.86294686,17.64149464),
    C=[[.0283473742,-.0326062007,0],
       [-.0326062007,.183928040,0],
       [0,0,.0404183878]].                          (6)

These input decimals are exact for the algebra, not exact physical constants. Define vL=(1,-293/500,0), vH=(0,-96/125,1). Each slope belongs to a branch whose v·f<0, whereas the data have positive g=v·d:

| branch | g | V=v^T C v | g²/V lower bound |
|---|---:|---:|---:|
| low | .77589748004 | .12972199464424 | >4.6408 |
| high | .85075145152 | .14890356006496 | >4.8607 |

C is positive definite. For Q=(f-d)^T C^-1(f-d), metric Cauchy gives

    Q >= [v·(f-d)]²/(v^T C v) >g²/V >4.            (7)

The common scale cancels in(3), so(7) covers every positive lambda. The full released covariance is positive definite as checked by exact LDL pivots. For any joint prediction vector extending these three components, extend v by zeros to obtain the identical lower bound for the full released quadratic discrepancy; this is an algebraic embedding, not a supplied history beyond x=2 even though the full data extend farther. cross-bin independence is not assumed. Equivalently, minimizing a full quadratic over the unselected residuals yields the marginal covariance subblock. Never apply the original Gaussian covariance to the nonlinear transformed coordinates h^(-3/2).

## 4. Useful successor: explicit transport tolerance

Suppose an additive model/observation discrepancy e obeys BOTH

    |vL·e|<=1/20, |vH·e|<=1/20.                    (8)

Then replace g in(7) by g-1/20. The two exact ratios exceed4.0619 and4.3061, preserving squared-radius4 separation. Coordinatewise |e_i|<=1/40 suffices. This is a required tolerance for the chosen transport model, not a measured bound on DESI systematics. Even the nominal ellipsoid is only the declared distance-error shape; statistical coverage and physical template validity remain separate.

## 5. Contrary construction and next model

For general shared coefficients a=alpha/b,r=rho/b, K2271 gives

    216 t² U^(5/3) U_tt=6a U^(4/3)-r.               (9)

Thus (1) is not a generic metric f(R) solution. A nonconstant affine U solves(9) only if a=r=0; a constant U instead permits r=6a U^(4/3). This exact applicability control prevents extending the present exclusion to all quadratic f(R). Conversely K2274's free-slope single-bin fit remains correct: the current constraint uses a transverse/radial pair AND an additional radial bin. Independent per-bin rulers or slopes would invalidate(3) and are not repairs of this common family.

The next useful cosmology test must treat shared nonzero coefficients, initial data and likelihood transport together. More rounding of this certificate or refitting the single bin adds no predictive information. Matter/light action/observation and physical initial-state selection remain native debts.

## Verification

The probe checks actual source labels/hashes, positive covariance, all128 rational integral cells, minimal cube ceilings, support and discrepancy bounds, symbolic monotonicity and full-equation applicability, plus changed-input controls that genuinely defeat a certificate. These are finite exact controls supporting the written continuous argument. Independent internal review is not external-expert, Lean, empirical-transport, novelty or remote-CI certification.
