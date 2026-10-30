---
title: "K2282 Centered positive controls and their phase cost"
status: active_research
doc_type: exploration
created: "2026-10-29"
classification: INTERNAL_STRUCTURAL_ONLY
target_claim: NONE-NOT-A-KILL
claim_ceiling: conditional supplied model only; no native GU or canonical verdict
scripts:
  - tests/channel-swings/k2282_centered_positive_control_probe.py
---

# K2282 Centered positive controls and their phase cost

> **GU-COMPARATOR-ROUTING — scope before inference.** This artifact contains or borders a conventional particle-physics comparator. Any result about a standard Higgs/VEV, ordinary family index or net chirality, SO(10) `126` Majorana mechanism, anomaly selector, VEV-only breaking or familiar vector-mass route binds only that named model. It is not evidence for or against Weinstein's source-native mechanism without an explicit typed bridge. Read `lab/methods/source-native-comparator-routing.md` and follow its source-native pointers before reusing this result.

Classification: `INTERNAL_STRUCTURAL_ONLY`.

```gu-typed-objects
result: K2282 Centered positive controls and their phase cost
carrier: ordinary bosonic fields, coherent pump and supplied global charge controls LAYER=toy CHIRALITY=N/A
pairing: positive complex Hilbert inner product ON=declared_carrier
real_structure: complex Hilbert conjugation and adjoint
grading: no native Clifford or chirality transfer
action_owner: repository-construction -- supplied conditional model
target: positive-generator implementation and retained-pump phase-error budget MAP-TYPE=evaluation
```

## Result and supplied alphabet

K2279 correctly warns that an uncentered quadratic compensator has phase-error sensitivity of order mu^(3/2). A NEW supplied positive-control alphabet replaces it by a centered charge polynomial and lowers that sensitivity to order mu on a vacuum consumer. It also supplies a complete semibounded version of the earlier signed detector under explicit additional calibration assumptions. This is not synthesis from the old alphabet or an affordable/autonomous apparatus result. A global function of total charge is a nonlocal resource.

Use Q=N_all+2n_c, the entire fixed set of logical fields (including earlier outputs), and the K2278 H_z acting on an addressed pair. Neutral/dispersive operations commute with Q. Supply an integer m>=0, h=ceil sqrt(m+2), d=2h(m+2)+1 and

    C_m=(Q-m)², gamma=4/sqrt(mu),
    B_z=gamma(C_m+d)+H_z, |z|<=2.

Opposite pulse signs are implemented by opposite nominal z, not negative time. C_m and B_z are independently SUPPLIED physical primitives. Although C_m is positive, its expanded polynomial Q²-2mQ+m² contains a negative linear coefficient. Existing positive Q² and positive Q controls do not by themselves realize it.

This conditional oscillator construction leaves SC-META-53 UNCERTAIN and LT-SM8/LT-GR6b/source/ledger0.263 unchanged. It does not construct native GU positivity.

## 1. Positive on every shell, not just the populated ones

K2276's finite-shell row bound gives ||H_z|| on Q=t at most2|z|(t+2)^(3/2)/sqrt(mu). Let a=m+2 and w=|t-m|. Since t+2<=a+w,

    (t+2)^(3/2)<=sqrt2[a^(3/2)+w^(3/2)]
       <=w²+sqrt2 a^(3/2)+27/64 < (t-m)²+d.

The middle inequality follows by maximizing sqrt2 w^(3/2)-w² at w=9/8. h>=sqrt(a) gives d>=2a^(3/2)+1. Hence B_z>=0 for every integer t>=0 and every |z|<=2, including the calibrated time-dependent pulses. Finite Hermitian shell dynamics have canonical selfadjoint direct sums and positive quadratic forms; no global bounded-operator assumption is made. The scalar polynomial strongly commutes with every H_z, including at different times.

## 2. One positive compensator cancels the entire known shift

Twenty pump pulses have duration r=log3 each. Their total added centered area is80r/sqrt(mu), with irrelevant scalar area d times that. Because C_m has integer eigenvalues, exp(-2pi i C_m)=I. Append ONE positive C_m pulse with area theta in[0,2pi) such that

    theta+80r/sqrt(mu)=0 mod 2pi.

The shifts commute through every intervening charged and neutral operation, so this implements the entire calibrated K2278 circuit exactly, up to a global phase, when the centered areas are exact. Actual pulse generators remain B_z>=0. No inverse of unknown error is assumed. A finite duration realizing theta requires a supplied control strength/clock; any free Q drift must be tracked or included in the linear phase budget below. This adds20 positive pump pulses in place of20 signed ones and one compensator, not twenty unknown-error cancellations.

## 3. Unknown errors act in the new centered primitive

Suppose the aggregate net area error of the actual centered generators is epsilon, and an independent uncompensated linear area error is xi. The residual is exp[-i(epsilon C_m+xi Q)]. The calibration contract is about these INTRINSIC errors, not a post hoc estimate of the old uncentered error. A center error Delta_m in a compensator of area tau adds linear area -2 tau Delta_m (and a scalar); it belongs in xi. Exact integer m is represented with integer arithmetic for periodicity, never a floating rounded square root. Scalar phase is irrelevant. For the explicit semibounded implementation, assign independent linear error to the final compensator: its integrated generator is a C_m+xi Q+c0 I, with a>=a0>0 and |xi|<=X. The supplied scalar offset c0=X*m+X²/(4a0) makes it positive by completing the square in Q-m, using the KNOWN bound X rather than unknown xi. In the numerical example the compensator area is near2pi, so a0=1 suffices. The explicit realization keeps the pump shifts exactly gamma and places net centered error epsilon in the final positive compensator. A wider per-stage error model would require lower-rate and scalar-offset positivity bounds of its own. Additional signed linear perturbations during pump pulses are not covered by this instantaneous-positivity certificate and require separate per-stage bounds. Scalar offsets leave the channel unchanged but are supplied control resources. For any initial pure state and its retained purification, spectral calculus gives the vector bound

    |epsilon| sqrt(Var C_m)+|xi| sqrt(Var Q).

All ideal and actual charged controls conserve Q; the variances may therefore be evaluated at preparation. For vacuum fields, Q=2K, K Poisson(mu). With delta=2mu-m,

    Var C_m=16[2mu²+mu(delta+1)²], Var Q=4mu.

The real optimum is m=2mu+1, reflecting Poisson skewness. Choose a nearest nonnegative integer: variance<=32mu²+4mu. For integer mu we can take m=2mu+1 exactly, variance32mu². The phase-error contribution is then at most4sqrt2 mu |epsilon|+2sqrt(mu)|xi|. These bounds retain the pump, not just field statistics.

For nonvacuum initial Nj<=1, one must include random N_all=n0 in[0,J]. Conditional on n0 put delta_n=2mu+n0-m; then

    Var C_m=E 16[2mu²+mu(delta_n+1)²]
             +Var(4mu+delta_n²).

Also Var Q=4mu+Var(n0)<=4mu+J²/4 for the independent linear-error term. Coherences in N_all do not alter polynomial spectral moments. The simple vacuum coefficient must not be reused silently; a conservative bound with m=2mu+1 is32mu²+16mu J²+max(1,(J-1)²)². The K2279 field moment bound itself still holds: all added Q functions commute with each Nj. In fact these final commuting phases leave field-number moments exactly equal to those of the corresponding calibrated signed core.

An attempted repair of the OLD residual epsilon(Q+2)² by applying a compensating linear phase based on an estimate epsilon_hat is different. Its remaining unknown linear coefficient is proportional to epsilon-epsilon_hat times m+2, retaining an order mu^(3/2)|epsilon-epsilon_hat| burden. Exact algebraic cancellation using the unknown true error is not a control protocol. The new alphabet makes the centered shape intrinsic but imposes its own coefficient calibration, including xi.

## 4. Complete strong-precision consumer

Use ten fresh vacuum fields, exact coherent mu=10^28, q50 and K2279's10^-17 calibrated pump/dispersive/neutral conditions. They imply |z|<2. Choose m=2mu+1. Require AGGREGATE |epsilon|<=10^-42 in the final compensator (pump shifts exact), and |xi|<=10^-28, in the same rotating-frame convention. These add less than8*10^-14 to the exact existing channel budget, which remains below10^-11. The actual field second moment stays below6,300,000; therefore field-energy error remains<.008 and pump depletion12.8±.004 quanta. The comparator is the whole target recorded instrument with original pump retained, not the signed implementation alone.

The counts are20 positive pump pulses, one positive global-charge compensator,1000 dispersive pulses, at most260100 neutral gates and102 neutral qubits per core, plus20 field modes. Compensator timing errors enter epsilon; its linear drift enters xi; pump shifts are exact in this fixture. No cost is silently removed by taking theta modulo2pi. At the coherent vacuum input E C_m=4mu+1 and d=O(mu^(3/2)), so initial positive B_z expectation is O(mu) under this normalization; compensator mean action is also O(mu). These are control-resource costs, not uniform total energy or minimum physical work. Exact number conservation preserves real field/pump energy transfer.

## Verification and remaining construction

The probe checks actual small-shell H_z positivity with the shifted operator, centered Poisson moments, integral-spectrum periodicity, residual-error decomposition and the composed full budget. Whole-shell positivity/direct-sum and retained-channel arguments are written proofs, separate from finite checks. New primitives, global coupling, coefficient precision and finite clocks remain supplied; no external-expert, Lean, hardware or novelty certification is claimed. A useful successor must synthesize/calibrate these specific primitives or provide a concrete lower-cost physical alternative, not merely reassert abstract controllability or rename the negative linear term.

Dependencies: [K2276](k2276-structured-detector-implementation-2026-10-29.md), [K2278](k2278-calibrated-pump-detector-2026-10-29.md), [K2279](k2279-uniform-pump-energy-2026-10-29.md).
