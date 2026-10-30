---
title: "K2292 Conserved matter and the quadratic cosmology"
status: active_research
doc_type: exploration
created: "2026-10-30"
classification: INTERNAL_STRUCTURAL_ONLY
target_claim: NONE-NOT-A-KILL
claim_ceiling: conditional supplied models only; no native GU, empirical or hardware acceptance
scripts:
  - tests/channel-swings/k2292_conserved_matter_cosmology_probe.py
---

# K2292 Conserved matter and the quadratic cosmology

> **GU-COMPARATOR-ROUTING — scope before inference.** This artifact contains or borders a conventional particle-physics comparator. Any result about a standard Higgs/VEV, ordinary family index or net chirality, SO(10) `126` Majorana mechanism, anomaly selector, VEV-only breaking or familiar vector-mass route binds only that named model. It is not evidence for or against Weinstein's source-native mechanism without an explicit typed bridge. Read `lab/methods/source-native-comparator-routing.md` and follow its source-native pointers before reusing this result.

Classification: `INTERNAL_STRUCTURAL_ONLY`.

```gu-typed-objects
result: K2292 Conserved matter and the quadratic cosmology
carrier: real expanding flat FLRW metric histories with separately conserved nonnegative perfect fluids LAYER=toy CHIRALITY=N/A
pairing: declared real metric scalar quadratic action ON=declared_carrier
real_structure: real metric histories
grading: no native Clifford or chirality transfer
action_owner: repository-construction -- supplied conditional model
target: global positive expansion and constrained matter response MAP-TYPE=evaluation
```

## Result and scope

The positive-expansion theorem of [K2283](k2283-global-quadratic-cosmology-2026-10-30.md) extends to nonnegative conserved dust/radiation and, more generally, finitely many fluids with continuous equations of state -1<=w_i(s)<=1. Positive U persists for every finite past redshift, and the integrating-factor criterion for F>0 survives. This is a theorem about the supplied metric action. It does not preserve the earlier vacuum data fit: nonzero homogeneous matter necessarily changes its exact history. Radiation has zero trace yet changes the full Friedmann constraint, providing a decisive countercontrol to a trace-only transplant.

SC-COS-50/51/54 ASSERTS and LT-GR2e remain unchanged. The connection-distortion action and this metric-f(R) model are not identified. No BAO-transport, matter-spectrum, empirical-confidence or GU result is certified.

## 1. Full constraint before trace-only reasoning

Use signature(-+++), action C/2 integral sqrt(-g) f(R), f=alpha R+R²/2-rho_v, C>0, alpha>0,rho_v>0, and minimally coupled conserved perfect-fluid matter. Choose H_*>0 and write dimensionless alpha/H_*² and rho_v/H_*⁴ as alpha and rho_v below. Let

    s=3log(1+z), H=H_* U^(2/3), p=U_s,
    q_i=kappa rho_i/H_*⁴, q=sum_i q_i, kappa=1/C,
    (q_i)_s=(1+w_i)q_i,
    R/H_*²=12U^(1/3)(U-p), F/H_*²=alpha+R/H_*².

With all subsequent R,F dimensionless, the full00 constraint is

    3FH²/H_*²=q+R²/4+rho_v/2+9(H²/H_*²)F_s.

It is equivalent on U>0 to

    U_s=p,
    p_s=p-alpha/(36U^(1/3))+(rho_v+2q)/(216U^(5/3)).       (1)

Matter conservation and this00 equation imply the remaining homogeneous metric equation through the diffeomorphism identity when H>0. No division by F is needed to write(1); interpreting a healthy positive-F metric branch remains a separate condition. Restoring original dimensional R,alpha,rho_v and stress, the trace is

    3 Box R-alpha R+2rho_v=kappa T,
    T=sum_i(-1+3w_i)rho_i.

In particular radiation w=1/3 changes(1) although its contribution to T vanishes. At the vacuum U,p, the same constants leave full00 residual -q. One cannot append matter to the old fitted vacuum path while calling it the same solution. Changing the initial data to obtain a new solution is allowed, but its distances and perturbations must be tested anew.

## 2. Global positive U by nonautonomous coercivity

For s>=0, q_i>=0 and 0<=q_s<=2q. Define

    E=p²/2+alpha U^(2/3)/24+(rho_v+2q)U^(-2/3)/144.

Differentiating along(1), all force terms cancel:

    E_s=p²+q_s U^(-2/3)/72 <=2E.                         (2)

Thus E(s)<=E(0)exp(2s). On every finite interval[0,S], E has a finite upper bound, giving finite |p|, a finite upper U bound from alpha>0, and a strictly positive lower U bound from rho_v>0. The separately conserved q_i stay finite there. The continuous-time, locally Lipschitz-in-state U>0 ODE therefore extends to every finite s>=0. This is not a theorem about the future s->-infinity, arbitrary negative densities, w>1, bounce solutions or the endpoint at infinite redshift.

For dust+radiation, q=q_d0 exp(s)+q_r0 exp(4s/3). This supplies an explicit smooth finite-time source for(1). Constant-w assumptions are not needed for(2); local regularity and the stated bounds suffice.

## 3. F-crossing classification survives the matter completion

Exact substitution gives

    F_s=A F-B,
    A=p/(3U)+alpha/(36U^(4/3)),
    B=(alpha²+2rho_v+4q)/(36U^(4/3))>0.

Set I(s)=exp[-integral_0^s A(v)dv]>0. Then(IF)_s=-IB<0. With F(0)>0, at most one crossing occurs, always from positive to negative as s increases. For any finite S, F(S)>0 is necessary and sufficient for F>0 on[0,S]. The global positive-U theorem alone is not a global positive-F theorem. For example, choose U=1 and p=1+alpha/12 to give F=0; then F_s=-B<0. This exact boundary test shows why the endpoint check cannot be dropped.

The same identity gives quantitative interior lower bounds once actual U and endpoint intervals for the matter solution exist. K2288's vacuum tube cannot supply those new intervals without a new certificate.

## 4. Matter changes scalar perturbation content

The single canonical Q action in [K2291](k2291-rolling-scalar-applicability-2026-10-30.md) assumes one scalar and vacuum. Conserved background matter is not an extra positive potential term in that action. Fluid density/velocity perturbations and their source terms enter the lapse/shift constraints; sound speeds and entropy data must be specified. Radiation's background T=0 does not remove its metric constraint or perturbations. [K2294](k2294-regular-scalar-transfer-2026-10-30.md) explicitly stays on the old vacuum history and proves a different prepared-wave result.

The concrete next matter calculation is a new full00 history with justified density parameters and coupled perturbation initial data. This note supplies the exact flow, continuation theorem, crossing criterion and residual test, eliminating a redundant trace-only search. It does not supply a new fitted history or the BAO ruler's early-time transport.

## Verification

The probe derives(1) independently from00, differentiates E and F, checks dust/radiation conservation and the exact unchanged-vacuum residual, and rejects actual coefficient/source mistakes. Exact symbolic identities plus the written continuation/integrating-factor argument establish the stated theorem; finite checks do not establish empirical applicability. Standard metric-f(R) background: [De Felice and Tsujikawa](https://arxiv.org/abs/1002.4928). No novelty, Lean or external-expert certification.
