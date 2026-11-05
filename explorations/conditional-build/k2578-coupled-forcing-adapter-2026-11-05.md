---
title: "K2578 Paired forcing in the complete TT response module"
status: active_research
doc_type: exploration
created: "2026-11-05"
classification: CONVENTIONAL_COMPARATOR
target_claim: NONE-NOT-A-KILL
claim_ceiling: full selected linear equations on the fixed R(1) TT source sector; no arbitrary tensor source or physical preparation
scripts:
  - tests/channel-swings/k2578_coupled_forcing_adapter_probe.py
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
result: K2578
carrier: fixed R(1) radial TT module of the selected curved seven-plus-seven system LAYER=toy CHIRALITY=N/A
pairing: indefinite tensor-test duality and auxiliary positive Sobolev norms ON=declared_carrier
real_structure: real data; complex impedance explicitly represents two real quadratures
grading: scalar amplitudes, TT tensor, shifted and original metric, auxiliary grade2 kept distinct
action_owner: repository-construction -- stated conditional model
target: paired forced response and original metric observation MAP-TYPE=evaluation
```

# A scalar force needs a second response

## Result and scope

K2576's forced scalar inverse alone is insufficient to answer the selected coupled system. This note supplies the missing Einstein scalar inverse and composes both into a response to every smooth supplied source j=s(B)R(1) on the fixed annulus. It retains the original metric and auxiliary fields, and executes a nonzero constant-source fixture plus a conserved observation formula. The fixed R(1) TT source is a precisely stated sector, not K2531's arbitrary compact radial-pressure source. No physical boundary law is derived.

SC-ACT-01 ASSERTS the first-order action, SC-GEO-03 ASSERTS Met(X), SC-GEO-55 ASSERTS gauge-rotated-Levi-Civita displacement, and SC-META-53 remains UNCERTAIN about indefinite spectra. The product and selected completion remain repository constructions. Ledger0.263 LT-GR6b/10/11 and LT-SM8, source polarities and canon are unchanged. Auxiliary norms and supplied controls confer no physical positivity, causal propagation, native GU recovery or novelty claim.

## 1. Start from every coupled row

Use K2552 §§3–6, with kappa nonzero:

    K=35 kappa²/3624192, a0=−5kappa/2288, rE=1/(6a0),
    c=970112/(13395kappa), mu=611557655 kappa²/39953092608.

Here c is the Schur coefficient, NOT the dimensionless mu/K−21 denoted c in K2568. The radial tensor R(1) has mixed eigenvalues, in observer4/radial1/angular2 order,

    (−3/4+7KS(r)²/4, 1, 1−7KS(r)²/2).

Its trace and divergence vanish, it is smooth at the center, and Box_A R(1)=−14K R(1). Multiplying by arbitrary B scalar s preserves full conservation because there is no B or mixed tensor component. Define Y=Box_B and

    D_Q=Y+mu−21K, D_E=Y−16K,
    D_Q u=−rE s/c, D_E v=rE s.                    (1)

Then Q=uR(1), z=vR(1), h=z−rE Q, e2=−A2^-1 B_aux Q. The auxiliary B_aux is K2535's first-order coupling, not the B manifold. All other grades vanish at this linearized scope. Indeed K2552 gives L_Q Q=c D_Q u R(1)=−rE j and E z=−D_E v R(1)/2=−rE j/2. Both tensors are TT; w=11(div Q−d tr Q)+13div Kskew=0 with Kskew=0. The skew, mixed and BB rows therefore vanish; the auxiliary row is A2 e2+B_aux Q=0. The unchanged invertible auxiliary elimination and h=z−rE Q return the original equations. This is an all-row reduction on this module, not a claim to solve all possible source modules.

For s nonzero, setting z=0 fails the Einstein source equation. A homogeneous reconstruction cannot simply be reused after forcing Q.

## 2. Derive both inhomogeneous Liouville maps

Fix t0=asinh1,t1=asinh2, zeta=sinh²t in[1,4],

    x=log[tanh(t/2)/tanh(t0/2)], 0<=x<=d,
    J=sinh t cosh(t)^(3/2), y=J u,
    L=ell(ell+2), n=m+1, nu²=1+n²+L.

For a mode U(t), the actual operator is

    Y U=−K[U_tt+3(tanh t+coth t)U_t
                      +L sech²t U−(n²−1)csch²t U].

Direct differentiation for ANY real beta yields

    (Y+beta)U=−K/(J zeta) [y_xx−P_beta y],
    P_beta=n²+(beta/K+35/4)zeta−(L+3/4)zeta/(1+zeta).       (2)

Consequently the two forced equations are

    y_Q''−P_Q y_Q=f_Q=(rE/(cK))J zeta s,
    y_E''−P_E y_E=f_E=−(rE/K)J zeta s=−c f_Q,
    P_Q=P_(mu−21K),
    P_E=n²−(29/4)zeta−(L+3/4)zeta/(1+zeta).              (3)

Every scalar f_Q corresponds to s=cK f_Q/(rE J zeta). These multipliers and their inverses are smooth and bounded on the fixed closed annulus. The relative minus sign in f_E is forced by (1).

## 3. The second inverse has no exceptional angular class

Reuse k²=nu²+D, D=606773239/96460 and K2576's Q estimate. For E,

    dP_E/dzeta=−29/4−(L+3/4)/(1+zeta)²<0.

Also |P_E|<=n²+L+148/5<k², since zeta<=4 and zeta/(1+zeta)<=4/5 and D>148/5. Thus every E mode belongs to K2576's monotone case. On the nonpositive suffix its shifted energy F=|y'|²+(1−P_E)|y|² obeys F'>=−F; integrating backward controls the turning jet. On the positive prefix convexity of |y|² and monotone energy control the interior. If no turn occurs, use the corresponding whole-interval case. The endpoint flux identity for the same opposite complex impedances

    y'(0)+iky(0)=k g0, y'(d)−iky(d)=k gd

gives uniqueness and homogeneous bound sup|(y,y'/k)|<=C_E k||(g0,gd)|| with C_E=max(sqrt6 exp(d/2),2+d). The Green comparison of K2576 then supplies sup|G_E|<=C'_E k and the same polynomial derivative bound. Unlike Q, no finite-exception exponential constant is needed. This explicitly checks the inherited theorem's hypotheses on the second ACTUAL operator.

Choose supplied boundary data independently for Q and E, using the same k normalization. The two unique scalar solutions give the coupled fields of §1. Angular H^(s+1) boundary data and L1_x H^(s+1) source give u,v in C_x H^s and normal derivatives in C_x H^(s−1), summing all multiplicities. This is the inherited uniform estimate and density argument applied twice; smooth data yield smooth fields. Auxiliary reconstruction costs its first differential order. For low regularity, source and equations are interpreted distributionally; do not assert that the second derivatives are continuous for merely L1 source. There is uniqueness within this module and these four prescribed boundary data, not uniqueness across all coupled homogeneous sectors or gauge conventions. The impedance rule is two coupled real quadratures; taking real fields changes its interpretation, not the equations.

## 4. Execute the original-metric observation consumer

Set delta=mu−5K. Since D_E=D_Q−delta, equations(1) imply

    E h=−(rE/2)(1+rE/c)sR(1)−(rE delta/2)uR(1).          (4)

The direct source term is mandatory; the homogeneous formula alone fails on the source support. For any fixed smooth compact tensor W, F=E W is conserved by the Einstein Bianchi identity, and formal self-adjointness gives <F,h>=<W,E h> with no boundary term. This supplies the actual finite test readout as a direct source functional plus the Q resolvent functional. Its continuity follows from the proved source/solution bounds and smooth compact test. It is a mathematical observation supplied by W, not an independently calibrated detector.

A useful consequence is that the E-channel homogeneous boundary preparation drops out of every such interior conserved test: varying v at fixed source solves D_E Delta v=0, so E Delta h=0. This does NOT make Delta h pure gauge or invisible to every conserved detector, since not every conserved tensor is proved to be E of a compact W. It isolates exactly this detector class. Varying the Q boundary data may still change(4), so preparing only the E channel cannot select the readout.

## 5. Execute a nonzero source and reject altered reconstructions

For s=1 constant on B, take

    u*=−rE/[c(mu−21K)], v*=−rE/(16K).

The denominators are nonzero, Y annihilates constants, and both equations(1) hold exactly. For ell=m=0 (n=1), set y_Q=J u*,y_E=J v* and choose their endpoint g values from the displayed impedance operators divided by k. They are generally NONZERO; this fixture makes no false zero-boundary assertion. Differentiation proves the forced equations and the original metric result

    E h*=8K(v*−rE u*)R(1),

which equals(4). A compact W pairing nontrivially with R(1) executes a nonzero conserved observation when this coefficient is nonzero. The exact probe checks that nonzero coefficient at kappa=1, with general rational identities retained.

Contrary controls drop v, reverse the forcing sign, omit the direct source term, confuse the Schur c with mu/K−21, or use z as the original metric. Each changes a calculated source residual or readout. The proof remains the tensor identities, differentiated map, uniform estimates and composition above; finite tests support those identities.

## Remaining frontier

This closes the paired forcing adapter on the fixed R(1) module. Extending it to arbitrary radial TT b(r,B) requires a common inverse for D5+Y and regular-center/domain bounds; the scalar complement still has its separate matrix-cofactor operator. Existing compact-profile spectral constructions remain evidence, but a common all-signature/angular physical preparation is not supplied. Independently justified physical boundary/control and sharper usable constants remain open. General Helmholtz impedance estimates, for example [Baskin–Spence–Wunsch](https://arxiv.org/abs/1504.01037), concern different domain/operator hypotheses and are background rather than an automatic proof of this coupled construction.

[K2552 full rows](k2552-localized-source-domain-2026-11-04.md), [K2576 scalar estimate](k2576-polynomial-impedance-control-2026-11-05.md), [probe](../../tests/channel-swings/k2578_coupled_forcing_adapter_probe.py), [report](../../lab/process/k2578-coupled-forcing-adapter.json).
