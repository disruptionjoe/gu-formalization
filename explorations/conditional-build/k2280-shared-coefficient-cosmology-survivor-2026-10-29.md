---
title: "K2280 Shared-coefficient cosmology survives a seven-coordinate test"
status: active_research
doc_type: exploration
created: "2026-10-29"
classification: INTERNAL_STRUCTURAL_ONLY
target_claim: NONE-NOT-A-KILL
claim_ceiling: conditional supplied model only; no native GU or canonical verdict
scripts:
  - tests/channel-swings/k2280_shared_coefficient_cosmology_survivor_probe.py
---

# K2280 Shared-coefficient cosmology survives a seven-coordinate test

> **GU-COMPARATOR-ROUTING — scope before inference.** This artifact contains or borders a conventional particle-physics comparator. Any result about a standard Higgs/VEV, ordinary family index or net chirality, SO(10) `126` Majorana mechanism, anomaly selector, VEV-only breaking or familiar vector-mass route binds only that named model. It is not evidence for or against Weinstein's source-native mechanism without an explicit typed bridge. Read `lab/methods/source-native-comparator-routing.md` and follow its source-native pointers before reusing this result.

Classification: `INTERNAL_STRUCTURAL_ONLY`.

```gu-typed-objects
result: K2280 Shared-coefficient cosmology survives a seven-coordinate test
carrier: positive real smooth vacuum expansion histories on redshift zero to2.33, with subset and neighborhood results through redshift one LAYER=toy CHIRALITY=N/A
pairing: real covariance quadratic pairing ON=declared_carrier
real_structure: real coefficients, histories and observation vectors
grading: no native Clifford or chirality transfer
action_owner: repository-construction -- supplied conditional model
target: validated common-domain and common-ruler compatibility MAP-TYPE=evaluation
```

## Result and scope

The pure-R2 exclusion in [K2277](k2277-multibin-pure-r2-test-2026-10-29.md) does not extend to the full shared-coefficient quadratic metric family. We construct a positive-F history with one fixed pair of nonzero coefficients, one initial slope and one ruler, whose SEVEN selected DESI DR2 coordinates have deterministic quadratic discrepancy below 16/5. A small simultaneous parameter box also survives below that threshold. The same witness, extended without coefficient refitting, fails the full13-coordinate snapshot even after its common ruler is optimized (section4). This is a certified fitted existence witness, not a globally optimal fit, a prior selected independently of data, a confidence statement or a held-out prediction.

The action is the supplied flat vacuum metric f(R)=alpha R-b R²/2-rho, b=-1. It is not Weinstein's connection-distortion construction. SC-COS-50/51/54 remain ASSERTS, LT-GR2e remains unaltered, and ledger0.263/source/canon do not move. Standard redshift, flat optical distances and transporting a BAO-derived covariance to this vacuum model remain assumptions. No early-universe sound-horizon computation, template calibration, matter/radiation fit, perturbative viability or GU recovery follows.

## 1. Fixed initial-value problem and data

Reuse [K2271](k2271-forward-cosmology-domain-2026-10-29.md): x=1+z, t=x³, U=(H/H_*)^(3/2), U(1)=2, V=U_t, and

    U_t=V,
    V_t=g=a/(36t²U^(1/3))-r/(216t²U^(5/3)),
    M_t=k=1/[3(tU)^(2/3)], M(1)=0,
    F/H_*²=12U^(1/3)(U-tV)-a.

Here a=alpha/(b H_*²), r=rho/(b H_*⁴). Both are shared across [1,8]. Fix the exact decimals

    a=-258.39, r=-5000, V(1)=-0.39968, lambda=44.1733.

lambda=(H_* r_d)^(-1)>0 is common to ALL coordinates. The predictor is lambda M for DM/r_d, lambda U^(-2/3) for DH/r_d, and lambda[z M² U^(-2/3)]^(1/3) for DV/r_d. A positive H_* restores dimensions; changing it rescales dimensionful coefficients, not the normalized history.

Use precisely the first seven rows of K2277's immutable mean/covariance snapshot, commit bb0c1c9009dc76d1391300e169e8df38fd1096db: BGS DV(z=.295); LRG1 DM,DH(z=.510); LRG2 DM,DH(z=.706); LRG3+ELG1 DM,DH(z=.934). The complete 7x7 principal covariance is used, including within-bin cross terms. The principal submatrix defines a selected marginal deterministic ellipsoid. It is NOT a claim that the remaining six coordinates are fitted. The stored source hashes and row identities are independently checked before evaluation.

A numerical search suggested the coefficients and reached its chosen lower search boundary r=-5000. That boundary has no physical or optimization significance. Only the rational witness and the following validated forward calculation are accepted.

## 2. A reproducible full-interval enclosure

All arithmetic uses Arb balls at120 bits, exact rational cell endpoints and outward enclosures for fractional powers on positive intervals. Split at every observed t and8. Each segment uses n=floor(2000 length)+1 equal rational steps, so h<1/2000. For incoming balls U,V,M at t0 set

    T=t0+[0,h], Ubox=U+[-4h,4h], Vbox=V+[-20h,20h].

On EVERY cell verify Ubox>1, -4<Vbox<4, -20<g(T,Ubox)<20, and the full interval expression for F is positive. Local IVP existence and a first-exit argument keep the solution inside these boxes: |U'|<4, |V'|<20 give strict inward bounds through time h. Positivity excludes the only RHS singularity, so induction proves continuation over the whole domain. The derivative and quadrature enclosures are

    g_t=-2g/t,
    g_U=-a/(108t²U^(4/3))+5r/(648t²U^(8/3)),
    k' = -(2/3)k(1/t+V/U),
    U_next = U+hV+(h²/2)g(T,Ubox),
    V_next = V+h g(t0,U)+(h²/2)[g_t(T,Ubox)+g_U(T,Ubox)Vbox],
    M_next = M+h k(t0,U)+(h²/2)k'(T,Ubox,Vbox).

The right sides use OLD incoming balls simultaneously. Integral Taylor remainder inclusion, not sampled equality, proves the recurrence. M integrates from the fixed distance origin; its independent remainder is essential. Strict per-cell F checks certify the full interval, not merely observation nodes. K2271's exact substitution satisfies the full00 constraint; K2265's off-shell identity then supplies trace and spatial equations. No trace-only fit is used.

The native probe reruns all14003 cells, certifies the covariance is positive definite by exact leading principal minors, and encloses (prediction-data)^T C^(-1)(prediction-data). It proves 3<Q7<16/5<4. This leaves a nonzero margin inside the chosen squared-radius4 ellipsoid. The numerical enclosure is deliberately broad enough for reproduction; more digits are not the result.

## 3. Follow-through: simultaneous neighborhood and earlier discriminator

Repeat the SAME certified recurrence with each of a,r,V(1),lambda replaced by a real interval of radius10^-8 about the displayed value, retaining U(1)=2. Interval arithmetic contains all fixed parameter choices, even though dependency overestimation permits more variation inside the enclosure. Every cell still has U>1,F>0, and Q7<16/5. Thus compatibility is not a single floating-point accident or a per-node coefficient fit. This is a data-selected neighborhood, not a physically justified prior.

For comparison, the simpler rational a=-69,r=0,V(1)=37/25,lambda=543/10 passes the ORIGINAL three-coordinate test with Q3<1/50, but its seven-coordinate discrepancy is >17. The same validated solver establishes both facts. In this special case g<0 and W=U-tV has W'=-tg>0, W(1)=13/25, hence F>69 analytically. Additional jointly used observables therefore genuinely discriminate among shared histories even though the general family has a seven-coordinate survivor. Neither passing witness removes K2277's correctly scoped pure-R2 exclusion.

## 4. Released follow-through: the same history fails the full snapshot

Extend the SAME rational seven-coordinate witness, without any refit, through every remaining observed redshift to z=2.33, t=(333/100)^3. The same cell induction and whole-cell F checks certify its positive domain on this larger interval (71857 cells). Use all13 rows, including ELG2/LRG-QSO and Ly-alpha entries with their stored labels and full13x13 covariance; exact principal minors certify positivity. The fixed witness now has Q13>10000. Profiling the ONE positive common ruler via K2271's quadratic formula still gives inf_lambda>0 Q13>7000; the positive cross product proves its minimizer is physical. Thus even a ruler refit cannot rescue this fixed normalized history on the full snapshot.

This is a held-out numerical confrontation for one data-selected witness under the extended vacuum/optics/template assumptions, not a held-out GU prediction or rejection of the full shared-coefficient family. The earlier seven-coordinate survival remains true. A fresh joint coefficient/initial-data fit could change the answer and would be a new data-selected construction; no global optimization, family exhaustion or observational-confidence law is claimed. This follow-through supplies an actual next-observable test instead of silently treating the seven-coordinate subset as all available data.

## Verification and next discriminant

The companion distinguishes symbolic full-equation/derivative checks, exact data/covariance checks, whole-domain interval certificates and changed-input faults. Internal specialist review is not Lean, external-expert certification, a novelty assessment or a survey likelihood analysis. Metric f(R) background: [De Felice and Tsujikawa](https://arxiv.org/abs/1002.4928); data interpretation: [DESI DR2 cosmology](https://arxiv.org/abs/2503.14738).

The next substantive observational question is a common physically justified coefficient/initial-data and BAO-transport domain across further observables, with all coefficients and ruler shared. The demonstrated fixed witness has now been extended and rejected against the full snapshot; a different shared history needs its own common-domain certificate and vacuum/template applicability assessment. Do not repeat the subset fit or infer that no shared-coefficient repair exists. A single surviving fit prevents blanket transfer of the restricted exclusion; it does not predict the held-out data.
