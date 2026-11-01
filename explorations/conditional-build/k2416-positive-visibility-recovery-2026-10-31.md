---
title: "K2416 Positive visibility, full-error brackets and scalar recovery optimum"
status: active_research
doc_type: exploration
created: "2026-10-31"
classification: CONVENTIONAL_COMPARATOR
target_claim: NONE-NOT-A-KILL
claim_ceiling: conditional mathematics; no native GU or empirical verdict
scripts:
  - tests/channel-swings/k2416_positive_visibility_recovery_probe.py
---

# K2416 Positive visibility, full-error brackets and scalar recovery optimum

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
result: K2416
carrier: flagged positive-Hilbert qubit sign instrument with planar clock moments LAYER=toy CHIRALITY=N/A
pairing: complete channel half-diamond distance ON=declared_carrier
real_structure: rational and algebraic Bloch channels
grading: good/bad flags, signs and planar/perpendicular blocks
action_owner: repository-construction -- K2398 physical sign blocks and K2410 norm
target: positive-visibility recovery and a declared family optimum MAP-TYPE=evaluation
```

## Result and selection

The exact visibility-zero optimum in [K2413](k2413-joint-recovery-optimum-2026-10-31.md) does not extend unchanged to positive visibility. A single physical affine decoder strictly improves every positive-visibility endpoint preserving that fixture's means. The original complete instrument is checked, and a discounted all-channel lower bound brackets the new optimum. Follow-through solves the entire nonnegative scalar affine decoder family, for arbitrary fixed proper planar good rotation and translation.

These are conditional quantum-channel results. SC-META-53 remains UNCERTAIN; positive Hilbert qubits, physical moments and the supplied uncertainty set do not construct a GU quotient or device. Ledger0.263 and source polarities are unchanged. Selection preferred the original-channel contraction and monotonicity arguments over a larger numerical search. Neither a norm lower bound nor a restricted family optimum is an unrestricted optimum.

## 1. The affine decoder and the complete norm

For s=tr(rho), planar Bloch vector r, mean m=E[n], h=E[v n], Q=E[v n n^T], the ORIGINAL sign blocks are

    J_z(rho)=[(s+z m^T r)I+(h s+z Qr).sigma]/4.

Here n is a unit planar axis and0<=v<=1. Thus Q is PSD, q=tr Q<=1; these are necessary moments of a physical law, not a sufficient independent specification of arbitrary m,Q. The common sign/real symmetry leaves an affine bad decoder R(r)=t+Ar. Pairing its two signs by Y conjugation cancels h and translation in the COMPOSED channel, giving B=t m^T+A Q and perpendicular multiplier zero. The decoder itself is generally nonunital.

With good planar block G and perpendicular multiplier g,

    C=I-(1-w)G-wB, d=1-(1-w)g,
    L²=(tr C)²+(C12-C21)²,
    H²=(C11-C22)²+(C12+C21)²,
    E=max(d+L,L+H,2d)/4.

This is K2410's complete half-diamond norm under its physical simultaneous symmetry, not an entanglement-fidelity proxy. Direct original Choi/Bell calculations reproduce its two blocks with eigenvalues(d±L)/2 and(-d±H)/2. The physical channel ensures d>=0, det C>=0 and L>=H. Replacing AQ by vA loses the moment matrix and gives the wrong channel.

## 2. A uniform gain over the zero-visibility optimum

Keep K2413's algebraic good rotation P*, g=1 and translation t*. It proves ||t*||²<13/20, hence ||t*||<81/100. Set epsilon=19/100 and

    R_epsilon(r)=t*+epsilon r
      =epsilon Id+(1-epsilon)Prepare[t*/(1-epsilon)].

This is CPTP. For any physical Q_i with the same two means and positive q_i=tr Q_i, C_i(epsilon)=C_i(0)-epsilon w_i Q_i. Symmetry of Q leaves the skew part unchanged:

    L_i(epsilon)²=L_i(0)²-2epsilon w_i q_i tr C_i(0)
                     +epsilon² w_i² q_i².

The original trace exceeds119 w_i/100. The original optimum E0* lies between0.5194114591 and0.5194114592; L_i(0)=4E0*-w_i<2. Moreover H_i(epsilon)<w_i and L_i(epsilon)>w_i, from H<=w_i(.81+.19) and L>=L0-.19w_i. The original complete norm therefore remains(w_i+L_i)/4.

Since w_i>7/10 and q_i<=1,

    L_i(0)²-L_i(epsilon)²
      > epsilon*(2*1.19-epsilon)*w_i²*q_i,
    E0*-E_i(epsilon) > q_i/100.

The last inequality divides by4(L_i(0)+L_i(epsilon))<16 and uses
(.19)(2.38-.19)(.7)²/16>.01. Thus the SAME controller satisfies
max E_i<E0*-min(q_i)/100. This compares with the old zero-visibility optimum, not a freshly optimized good-identity strategy or the new unrestricted optimum.

The probe also uses K2410's rounded rational controller, epsilon=.19, and actual ±axis laws of visibility1/2. Original instrument CP/TP, composition and full norm certify both errors below.51, an improvement exceeding.005 over E0*. This rational fixture is distinct from the algebraic universal construction. Convex mixtures of the complete flagged endpoint instruments preserve the upper bound by channel convexity; conditional means must not be mixed without their loss weights.

## 3. Follow-through: exact optimum in the full scalar affine family

This conclusion no longer needs K2413's particular constants. Fix any proper planar good rotation P (g=1), any planar t with ||t||<=1, and a physical law with w>0. Among decoders R_epsilon(r)=t+epsilon r with epsilon>=0, complete positivity holds EXACTLY for

    0<=epsilon<=1-||t||.

An aligned pure Bloch input proves necessity; the identity/preparation mixture proves sufficiency, with the t=0,epsilon=1 endpoint understood as identity.

Throughout this interval,

    H<=w(||t||||m||+epsilon q)<=w,
    tr C>=w(2-||t||||m||-epsilon q)>=w,
    L>=tr C>=w.

The proper rotation contributes no anticonformal part, while tr P<=2. Hence the complete norm stays E=(w+L)/4, and for q>0,

    dE/depsilon=-w q tr(C)/(4L)<0.

The exact optimum in this family is epsilon*=1-||t||, simultaneously for every physical law. The maximum of finitely many strictly improving positive-visibility endpoint errors also strictly improves. For arbitrary uncertainty sets including q=0, only nonincrease is guaranteed. If ||t||=1 the feasible interval is a singleton. This theorem neither optimizes P,t nor covers general anisotropic affine A.

## 4. All-channel lower certificate and remaining gap

Retain K2413's balancing weights p_i, h,k,B and good-channel conformal radius r. For any averaged physical bad decoder, opposite pure inputs imply ||A||op<=1 even when t is nonzero. Conformal projection gives

    L_i(Q_i)>=L_i(0)-w_i||A Q_i||_* >=L_i(0)-w_i q_i.

One way to see the first norm inequality is that the conformal length of a real2x2 matrix X has square ||X||F²+2det X, at most its nuclear norm squared ||X||F²+2|det X|. Combining with the unchanged zero-visibility contraction argument gives

    max E_i >= E0*+[(1-g)h+k(1-r)||B||-sum p_i w_i q_i]/4.

Dropping the nonnegative penalties gives a controller-independent lower bound. The first rational fixture has a nontrivial bracket with lower endpoint above.4 and upper endpoint.51; the anisotropic successor below lowers the upper endpoint to.487. This lower bound need not be attained. The positive-visibility all-CPTP optimization remains open, now with actual physical upper witnesses and a whole-channel lower certificate.

## 5. Anisotropy beats the entire fixed-translation scalar family

Independent final review identified a concrete competing channel, so the calculation continued beyond the scalar theorem. Fix the SAME rounded good rotation from K2410, set t=(4/5,0), and use the rational decoder

    (r_x,r_y,r_z) -> (4/5+r_x/5, 2r_y/5, 2r_z/5).

This is a physical anisotropic damping channel, confirmed by its ORIGINAL Choi matrix and trace preservation. It can also be viewed as an X-axis amplitude-damping channel followed by a compatible transverse dephasing. Keep the same two original axis laws and visibility1/2. Direct original sign composition and Bell blocks give complete errors below487/1000 for BOTH laws. The squared L values are622548413293/421213000000 and8255421173737/5475769000000; the saved report retains H and all exact comparisons.

At this same translation and good rotation, the scalar theorem makes epsilon=1/5 the exact best scalar decoder. Its complete error is above1/2 for BOTH laws, verified by the exact squared-radius inequalities and the other norm branches. Therefore anisotropy strictly outperforms the entire nonnegative scalar affine family at these fixed t,G. This is stronger than just beating one scalar parameter, but does not optimize translation, rotation or general affine channels.

If the full recovered implementation differs from the ideal channel by less than1/1000 in half-diamond distance, the triangle inequality leaves error below.488, hence still below the IDEAL same-t,G scalar baseline of.5. Comparing implemented devices would require both implementation budgets. This is a formal complete-channel allowance, not supplied hardware accuracy or costs. Convex mixtures of the complete endpoint instruments inherit the upper bound with one controller. The original unrestricted lower certificate remains valid, so the all-CPTP optimum is now bracketed between the saved lower endpoint above.4 and.487.

A structural refinement for the next dual is ||A||op<=sqrt(1-||t||²). Positivity sends both opposite pure Bloch inputs to the ball; averaging ||t+Ax||² and ||t-Ax||² bounds ||Ax||² by1-||t||². Thus the visibility discount can retain this translation-dependent factor, along with the exact center distances. It does not independently improve the global numeric lower bound when t is also optimized. A certificate saturating the CP constraints and complete norm remains absent.

## Verification and continuation

The exact probe freshly replays inherited CP/TP/norm evidence, checks the changed original positive-visibility instrument and Bell characteristic polynomials, and tests nonphysical excess mixing, omitted moment anisotropy and preparation-only controls. Finite fixtures support the analytic uniform gain and scalar-family proof; they do not substitute for those arguments. Independent quantum review accepted the affine cancellation, branch bounds, contraction inequality and family optimum; its anisotropic challenge was then executed on the original instrument. Next useful work is a full joint-channel primal/dual theorem or a justified physical uncertainty family, retaining the current complete-channel gap. No novelty, empirical advantage or external certification is asserted.
