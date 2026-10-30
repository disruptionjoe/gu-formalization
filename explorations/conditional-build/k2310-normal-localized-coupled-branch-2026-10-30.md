---
title: "K2310 Normal localized coupled branch"
status: active_research
doc_type: exploration
created: "2026-10-30"
classification: CONVENTIONAL_COMPARATOR
target_claim: NONE-NOT-A-KILL
claim_ceiling: conditional mathematics only; no native physical acceptance
scripts:
  - tests/channel-swings/k2310_normal_localized_coupled_branch_probe.py
---

# K2310 Normal localized coupled branch

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
result: K2310
carrier: flat K77 full distortion and horizontal-supported metric coefficients depending on all14 coordinates LAYER=ambient CHIRALITY=N/A
pairing: native K77 bilinear coefficient pairing; positive coordinate Sobolev norm only for localization ON=declared_carrier
real_structure: real fields from conjugate complex Fourier patches
grading: native odd and even Clifford distortion grades; horizontal metric tensor slots
action_owner: repository-construction -- K128/K2304 constant-coefficient I1B Hessian with explicitly enlarged coefficient dependence
target: normal localization and exact variation-space boundary MAP-TYPE=evaluation
```

## Object and first failed extension

[K2307](k2307-spatial-coupled-native-mode-2026-10-30.md) solves ten horizontal metric equations and every distortion equation. It does not solve all105 ambient metric variations. Its coefficients are independent of the ten normals. Here we explicitly allow horizontal-supported metric coefficients h_mu_nu(x,y) to depend on the normals. This is a conditional extension of that PDE carrier: a strict pullback h=pi*h(x) does not have this freedom. Neither carrier is selected as the complete source geometry by this calculation.

The demand is a growing solution with finite positive coordinate Sobolev norms in all13 non-time coordinates. A normal boost of K2307 fails: its transverse distortion weights are5 on three horizontal spatial indices and-1 on ten normals. The unselected normal metric row is nonzero and a time-normal boost mixes it into a selected horizontal row. The exact bank checks this failure. Conservation, covariance of the unrestricted algebra and a ten-row solution cannot remove this restriction.

SC-ACT-01/02 and SC-GEO-55 retain ASSERTS; SC-META-53 retains UNCERTAIN. Current ledger0.263 LT-GR1b/6b/10/11 remains unchanged. Physical source/readout, positive energy, global geometry and a source-selected causal domain remain open.

## A different root with an exact native witness

Use eta=(+,-,-,-,+,+,+,+,+,+,-,-,-,-), kappa!=0, b=|kappa|sqrt(5/29), and normal index10. In the thirteen transverse coordinates let P project onto indices1,2,3,10. Start with metric seed h_ii=1 on these four indices and

    T_odd=(5kappa/36)(4P-I13),
    T_even=(5b/36)(8P-5I13).                         (1)

These diagonal coefficient matrices abbreviate the same native form/Clifford bases as K2304: odd dx^i gamma_i and even dx^i gamma_0 gamma_i. The signature factors in the exact bank are retained. The temporal derivative block is B=J13-2I13. After factoring kappa from T_odd and b from T_even, the dimensionless odd coefficients x are5/12 on P and-5/36 off P; even coefficients are -Bx, namely5/12 on P and-25/36 off P. Thus the even companion closes. The odd equation uses b²/kappa²=5/29. Selected active metric rows have sum of other odd weights3(5/12)+9(-5/36)=0. This is the changed rank-four root, not the old17/113 root.

On the0,10 plane apply the complex Lorentz matrix with c=3/5,s=4i/5 to covectors and its inverse transpose to Clifford generators. It fixes the soldering form and hence the exact Shiab/Hodge/pairing operations. The covector becomes xi=b(3/5,0,...,4i/5,...). Boost (1), and adjust only the metric by q tensor v+v tensor q, where q=xi/b,

    v0=-123/160, v10=9i/40.

The final metric has h00=-25/16, h11=h22=h33=1 and every other component zero. The adjustment has zero linearized curvature, so the distortion companion is unchanged. The probe evaluates both full companion rows, all ten horizontal metric rows and the zero-curvature adjustment against the native coefficient bank. It also verifies a nonzero extra normal metric row: this is not a full105 solution. Its ambient linear scalar curvature is4b² times the exponential amplitude, so it is not a pure metric gauge mode.

The rank change can also be seen from the transverse response. With s0=xi², its tracefree coefficient is alpha=-kappa*s0²/(kappa²-4s0), while the thirteen-dimensional trace eigenvalue is sigma=-144kappa*s0²/(kappa²-121s0). Here H is the transverse mixed eta-self-adjoint tensor, with trace in the induced metric. Writing the map as alpha H+beta tr(H)I gives beta/alpha=(11kappa²-35s0)/(kappa²-121s0). Restriction to a nondegenerate rank-m image sets alpha+m beta=0 and gives s0/kappa²=(1+11m)/(121+35m). m=3 recovers17/113; m=4 gives5/29. Neither companion denominator vanishes there. This decomposition is an explanation of the explicit witness, not a classification of all characteristic branches or null normal momenta.

## Released continuation: real full-coordinate packets

Write real Fourier momenta as p_H in the three horizontal spatial directions and p_N in the ten normal directions. Define

    r=sum_{10..13}p_n²-sum_{4..9}p_n²,
    lambda=sqrt(b²-|p_H|²-r).

Take a small full13-dimensional open patch around p10=4b/5, every other momentum zero. On a compact subpatch r>0 and lambda>0 have positive lower bounds. Smooth real O(6,4) changes of normal frame reduce p_N to sqrt(r)e10; smooth complex horizontal Lorentz transformations reduce (lambda,i p_H) to (sqrt(b²-r),0,0,0). Both preserve horizontal tensor support. In that frame the construction above works for general c=sqrt(b²-r)/b,s=i sqrt(r)/b; the gauge-adjusted metric is h00=-b²/r, H=I3. Undo these frame changes. The coefficients are smooth because the patch avoids r=0 and lambda=0.

The companion equations are covariant. For the metric rows the point is stronger than covariance alone: the seed metric Euler tensor vanishes on the active four-plane; its boosted0,10 block therefore remains zero. The only nonzero rows lie in the unused transverse complement. Horizontal/normal frame changes then preserve the selected horizontal zero rows. This supplies the continuous family, not just its sampled witness.

Multiply by an arbitrary nonzero smooth compact Fourier amplitude on that patch and exp(lambda(p)t), then inverse Fourier transform in all13 coordinates. Every field is Schwartz at each finite t; add the conjugate patch to make it real. Ambient scalar curvature is4b² times the amplitude under the same transformation. Plancherel gives its positive-coordinate L2 norm growth at least exp(lambda_min t) for t>=0. The finite norms are not a native physical energy, and the gauge adjustment does not assert physical quotient descent.

## Scope, verification and next discriminant

The strict-pullback sector cannot obtain normal localization this way. The enlarged horizontal-supported PDE can, on a changed root. A full ambient-metric theory must add95 equations and recompute its kernel; it cannot inherit this solution. A source-owned induced metric/connection variation may differ from both. No global Met(X) geometry, closed causal Green realization, physical matter/readout, nonlinear instability, GU falsification or novelty is claimed.

Exact Gaussian-rational checks establish the displayed native witness and genuine corrupted-input failures. The continuous packet conclusion uses the written covariance, variation-space and Fourier proof. Next construct the source-owned metric-dependence/normal-jet rule or physical source/readout that decides whether this enlarged carrier is admissible; do not merely repeat the two known roots.
