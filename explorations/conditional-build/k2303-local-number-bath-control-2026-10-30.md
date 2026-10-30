---
title: "K2303 Local number baths during pump control"
status: active_research
doc_type: exploration
created: "2026-10-30"
classification: CONVENTIONAL_COMPARATOR
target_claim: NONE-NOT-A-KILL
claim_ceiling: conditional construction only; no native physical acceptance
scripts:
  - tests/channel-swings/k2303_local_number_bath_control_probe.py
---

# K2303 Local number baths during pump control

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
result: K2303
carrier: twenty field modes, retained pump and twenty-one thermal bath modes LAYER=toy CHIRALITY=N/A
pairing: positive complex Fock Hilbert trace distance ON=declared_carrier
real_structure: real coefficients; complex Fourier or Hilbert representation only where stated
grading: ordinary Fock number grading; conserved Q=N+2K; no Clifford transfer
action_owner: repository-construction -- supplied positive pump circuit and diagonal oscillator baths
target: full field-record-retained-pump instrument MAP-TYPE=evaluation
```

## Local coupling changes the commuting argument

[K2300](k2300-positive-bath-pump-dephasing-2026-10-30.md)'s collective number bath can be replaced by21 independent mode-local baths with a sufficient full-circuit bound. Local means mode/bath coupling, not spatial hardware. Let N=sum(i=1..20)Ni and Q=N+2K. Supply

    H_E=sum(i=0..20) omega_i n_i+2b K n0+a sum(i=1..20) Ni n_i,
    omega_i>0, a,b>=0.                                  (1)

Initially all baths factor from the circuit and each other, each thermal mean1; fields start in vacuum and the pump is one of the same coherent/displaced-thermal inputs. Controls are fixed independently of bath numbers; the bath is discarded in the output comparison. SC-META-53 remains UNCERTAIN and no positive-GU-quotient claim follows from this supplied positive Hilbert model. Source/ledger verdicts unchanged.

Equation(1) is positive and preserves Q and every n_i. It does NOT commute with pair creation A†c:

    [V,A†c]=(a n_a+a n_b-2b n0) A†c.                    (2)

Thus the full reduced dynamics averages fixed bath-number-conditioned interleaved circuits, not one input collective dephasing channel. Successive waits see the same random tuple; they are not iid.

## Full retained-pump bound

Separate V=bn0 Q+R with R=sum_i(a n_i-bn0)Ni. Independence, mean1 and variance2 give the exact operator moment

    E_E R²=(a-b)²N²+2a²sum_i Ni²+2b²N²
           <=(3a²-2ab+3b²)N².                          (3)

For the collective reference trajectory, common phase commutes every field number, so [K2293](k2293-moment-controlled-positive-pump-2026-10-30.md)'s E(N+1)²<6,300,000 is unchanged. Duhamel on a common purification, followed by discarding baths, gives

    D(local,collective)<=T sqrt(6300000) sqrt(3a²-2ab+3b²).

This uses the reference state in the Duhamel integrand and exact unitarity of the perturbed evolution; it does not assume that the local noisy and ideal number trajectories agree. Finite Q/bath-number sectors give propagators and finite moments control the unbounded direct sums. Recorded operations can be purified with neutral registers; all waits and correction pulses count in T.

For pump cumulants k2,k4 and inherited delta<9.272e-12,

    D_full<=delta+2sqrt(k2)bT
      +4(bT)²[k2+sqrt(k4+3k2²)]
      +sqrt(6300000) sqrt(3(aT)²-2(aT)(bT)+3(bT)²).       (4)

Coherent input has mu=10^28,k2=k4=mu. Displaced thermal input nP=1,mu=4*10^28 has k2=3mu+2,k4=75mu+26. At aT<=10^-17,bT<=10^-28, both consumers obey D_full<9.386e-12<10^-11; residual contribution<4.35e-14. For the rectangular parameter bound one may safely drop the negative cross term in(4); choosing tiny couplings is a stated assumption, not achieved isolation.

Local diagonal terms commute every Ni. The original number-moment growth proof therefore survives for each bath tuple. With the common full bound, the sharp field-number inequality gives error<sqrt(6300000*9.386e-12)<.008. Q conservation and ideal field mean25.6 imply pump depletion12.8±.004. Trace closeness is not energetic catalysis.

## Exact fixed-charge countercontrol

Use psi=(|0,0,1>+|1,1,0>)/sqrt2 in Q=2, with independent geometric baths r=1/2, a=b=g and gT=pi, and no pump pulse during this control. The characteristic function is chi(theta)=1/(2-exp(-i theta)). Each of two field baths contributes chi(pi)=1/3, while the pump phase is2pi and contributes1. Coherence becomes1/9 and half trace distance is exactly4/9. Every collective Q channel is identity on this state. Fixed total charge does not protect against independent local number noise; charge conservation has not failed.

An interleaved two-state pump control additionally verifies that noncentral bath phases cannot be moved to circuit input. This numerical fixture tests equation(2), not the universal error bound or a physical device.

## Cost and next condition

Initial free bath expectation is sum omega_i, initial interaction expectation2b EK. Bath free energy remains fixed because every n_i is conserved, while circuit/bath correlations accumulate. This is not total switching work. Positive number coupling removes the oscillator displacement counterterm, but still supplies mode-local cross-Kerr primitives, frequencies, unmeasured extremely weak residual couplings and long-duration isolation. Spatial adjacency, pump locality, calibration, reset and clock errors remain independent costs.

The exact second-moment proof and rational budget are distinguished from the finite numerical interleaving control. Genuine faults alter bath variance/covariance, charge coefficient, coherence law or propagation order. No hardware, empirical, novelty or external-expert certification. Next specify spatial implementation and measured or microscopically bounded coupling/clock errors for the same complete circuit; another freely chosen variance is not that construction.
