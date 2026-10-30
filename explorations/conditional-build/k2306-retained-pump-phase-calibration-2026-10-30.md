---
title: "K2306 Retained-pump phase calibration"
status: active_research
doc_type: exploration
created: "2026-10-30"
classification: CONVENTIONAL_COMPARATOR
target_claim: NONE-NOT-A-KILL
claim_ceiling: conditional construction only; no native physical acceptance
scripts:
  - tests/channel-swings/k2306_retained_pump_phase_calibration_probe.py
---

# K2306 Retained-pump phase calibration

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
result: K2306
carrier: same twenty field modes and retained coherent pump plus independent coherent pilot modes LAYER=toy CHIRALITY=N/A
pairing: positive Fock Hilbert form and half trace distance ON=declared_carrier
real_structure: real coefficients with complex Fourier or Hilbert representation where stated
grading: explicitly stated native Clifford or ordinary scalar/number grades; no transfer between them
action_owner: repository-construction -- K2303 fixed circuit plus unknown common phase and explicitly supplied calibration instrument
target: calibration resource required for full recorded field/pump accuracy MAP-TYPE=evaluation
```

## The operational requirement behind a tiny drift bound

[K2303](k2303-local-number-bath-control-2026-10-30.md) bounds the same complete recorded circuit by delta<9.386e-12 under its stated local-bath assumptions. Its coherent pump has mean mu=10^28 and the reference output retains the ORIGINAL independent coherent pump. Add a fixed unknown common drift phi Q, Q=N+2K, commuting with every conserving control and number-diagonal bath. It may be moved through the whole circuit and its invariant recorded measurement. The output is compared to that same unrotated reference, including the pump.

For residual phase e after an explicitly supplied correction exp(+i phi_hat Q), the coherent-pump marginal distance is

    d_mu(e)=sqrt(1-exp[-4mu sin² e]),                    (1)

with phase modulo pi. Contractivity and the triangle inequality imply

    d_mu(e)-delta <= D_full(e) <= d_mu(e)+delta.         (2)

The lower uses the retained pump marginal and drift-free product-reference closeness, not a pure-state formula applied to the mixed complete output. The upper moves the common phase to the coherent input and uses data processing. A known phase and an exact inverse control are different resources from a bath with unobserved independent local numbers. This calibration cannot cancel K2303's independent tuple noise.

Freeze epsilon=10^-11 and a pointwise, at-least95%-confidence requirement D_full<=epsilon for every unknown phase modulo pi, or in a known local interval containing two phases separated by2*10^-25. A narrower prior may permit zero-pilot calibration and is excluded from the lower-bound claim. This is a per-calibration-run guarantee. It is NOT an averaged channel-error claim; rare bad estimates must be charged separately for that stronger goal.

## Necessary coherent-pilot resource, even with optimal joint readout

Allow independent coherent pilot pumps with means mu_j, exposed for durations T_j to the SAME unknown common frequency as the apparatus duration T. Permit arbitrary joint measurement, classical processing and an ideal inverse phase pulse. Pilot j has phase 2(T_j/T)phi. No further phase-dependent query is available. Define

    M_eff=sum_j mu_j (T_j/T)².                         (3)

For two hypotheses separated by Delta_phi, the pilot squared overlap is

    F12=exp[-4 sum_j mu_j sin²((T_j/T)Delta_phi)]
        >=exp[-4 M_eff Delta_phi²].                    (4)

Equal-duration pilots have M_eff equal to total mean photon count. Long pilot exposure is explicitly a resource, not a free way to evade the statement.

At residual distance at least r0=10^-25 modulo pi, (1) exceeds epsilon+delta: its value is greater than1.9386e-11. Thus successful output demands residual less than r0. Choose phases0 and2r0. Their success neighborhoods are disjoint, so a uniform95% successful calibration would distinguish them with average error at most alpha=1/20. The optimal equal-prior pure-state discrimination error is (1-sqrt(1-F12))/2; hence F12<=4alpha(1-alpha)=19/100 is necessary. But if M_eff<=10^49,

    F12>=exp(-8/5)>1/5>19/100.                         (5)

Therefore M_eff>10^49 is necessary in this coherent-pilot class. The exact bound from any disjoint-neighborhood separation also survives; (5) is a conservative simple certificate. The baseline pump mean10^28 alone is insufficient for this uniform high-confidence specification by over21 orders of magnitude in equal-duration coherent pilot stock. This is a calibration architecture/resource result, not a universal quantum-metrology lower bound or a hardware impossibility theorem.

## Constructive upper and its additional apparatus

Use equal-duration coherent pilots with total M=10^53, a supplied independent optical phase reference, ideal combining/heterodyne readout, and exact inverse feedforward. Heterodyne gives

    Z=sqrt(M) exp(-2i phi)+W,
    density(W)=pi^-1 exp(-|W|²), phi_hat=-arg(Z)/2 mod pi.

For 0<r<pi/4, the disk |W|<sqrt(M)sin(2r) lies inside the phase-error wedge. Therefore

    Pr(|phi_hat-phi|_pi>r)<=exp[-M sin²(2r)].            (6)

Take r=3*10^-27. The failure probability is below1/20, and on success d_mu(e)<=2sqrt(mu)r=6*10^-13. Equation(2) yields D_full<9.986e-12. This is an explicit achievable success guarantee in the stated ideal measurement/correction architecture; pilot energy is sum hbar omega_j mu_j, with no free frequency choice claimed. It does not price the independent phase reference, heterodyne detector, correction error, clock or recycling hardware.

The stronger averaged-output requirement changes the cost. With failure alpha, convexity gives D_averaged<=delta+6e-13+alpha. Choosing alpha=10^-15 and M=10^54 in (6) gives failure<exp(-35)<10^-15 and D_averaged<9.987e-12. This is sufficient under the SAME fixed unknown phase, independent pilots, and ideal feedforward assumptions. It is not obtained by interpreting the95% guarantee as10^-11 average accuracy. The pilot resource is consumed or separately renewed; no energy-catalysis conclusion follows.

## Controls, claim ceiling and next condition

Exact overlap/Helstrom algebra and rational exponential/sine bounds certify the resource statements. Controls include known phase with exact inverse (zero residual), modulo-pi alias, unequal exposure accounting and failure-budget composition. Faults omit the pump charge2, confuse squared overlap with overlap, drop duration weights, or use the95% failure budget for the averaged-channel claim. None is a Boolean manifest flip.

SC-META-53 remains UNCERTAIN; the positive Hilbert pilots do not derive a GU physical quotient. Ledger0.263 and all source claims remain unchanged. Displaced-thermal pump inputs, squeezed/entangled/nonclassical pilots, adaptive repeated phase queries, drift varying between calibration and use, and spatial microscopic realization are outside the bound. This result converts one supplied tiny-drift assumption into an explicit operational resource; next construct a reference/clock/correction architecture with its own error and renewal budget, or test a specified nonclassical pilot class. Further freely chosen tiny phase variances do not address that obligation.
