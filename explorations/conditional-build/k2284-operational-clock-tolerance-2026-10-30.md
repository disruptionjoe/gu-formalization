---
title: "K2284 Operational centered-phase tolerance and clock scope"
status: active_research
doc_type: exploration
created: "2026-10-30"
classification: INTERNAL_STRUCTURAL_ONLY
target_claim: NONE-NOT-A-KILL
claim_ceiling: conditional supplied model only; no native GU or canonical verdict
scripts:
  - tests/channel-swings/k2284_operational_clock_tolerance_probe.py
---

# K2284 Operational centered-phase tolerance and clock scope

> **GU-COMPARATOR-ROUTING — scope before inference.** This artifact contains or borders a conventional particle-physics comparator. Any result about a standard Higgs/VEV, ordinary family index or net chirality, SO(10) `126` Majorana mechanism, anomaly selector, VEV-only breaking or familiar vector-mass route binds only that named model. It is not evidence for or against Weinstein's source-native mechanism without an explicit typed bridge. Read `lab/methods/source-native-comparator-routing.md` and follow its source-native pointers before reusing this result.

Classification: `INTERNAL_STRUCTURAL_ONLY`.

```gu-typed-objects
result: K2284 Operational centered-phase tolerance and clock scope
carrier: bosonic fields, retained coherent pump, classical detector records and a specified clock LAYER=toy CHIRALITY=N/A
pairing: positive complex Hilbert inner product ON=declared_carrier
real_structure: complex conjugation and Hilbert adjoint
grading: no native Clifford or chirality transfer
action_owner: repository-construction -- supplied conditional model
target: necessary duration accuracy for a specified centered-charge pulse MAP-TYPE=evaluation
```

## The question and the measured channel

[K2282](k2282-centered-positive-control-2026-10-29.md) gives a sufficient aggregate area tolerance for the supplied C_m=(Q-m)² control. We prove a local operational lower bound on the COMPLETE ten-call recorded instrument with the original coherent pump retained. It identifies actual duration sensitivity; it is not a universal lower bound on finite clocks, actuator energy or hardware complexity. The supplied positive Hilbert model does not construct GU's physical quotient: SC-META-53 stays UNCERTAIN; LT-SM8/LT-GR6b and ledger0.263 remain unchanged.

Take ten fresh vacuum field pairs and a coherent pump of mean mu, integer mu>=10000. Q=N_all+2K, m=2mu+1. Let sigma be the ideal recorded instrument output tensor the unchanged coherent pump, and rho0 the implemented signed core, with half trace distance D(rho0,sigma)<=delta_core as in K2279. A final commuting residual is U_e=exp(-i epsilon C_m). Set xi=0 initially. All neutral workspace has already been treated by the channel bound. A pure dilation distance alone would NOT be a lower bound after discarding workspace.

## 1. Exact pump moments and local sensitivity

For vacuum field charge, K is Poisson(mu), C=(2K-m)². Let C' be an independent copy. Direct moment calculation gives

    EC=4mu+1, Var C=32mu²,
    E(C-EC)^4=2048mu²+36864mu³+15360mu⁴,
    E(C-C')^4=4096mu²+73728mu³+36864mu⁴.

For a pure coherent pump,

    Dpump(epsilon)²=1-|E exp(-i epsilon C)|²
       =E[1-cos(epsilon(C-C'))].

Use x²/2-x⁴/24<=1-cos x<=x²/2, valid for every real x. Thus the pump upper bound is4sqrt2 mu|epsilon|; the lower is this quantity times sqrt(max(0,1-epsilon²(48mu²+96mu+16/3))). This proves local order mu sensitivity, but is not yet the recorded-instrument lower bound.

## 2. Pass through the actual record/discard map

Pinch the field output into total-number blocks N=n while retaining records and pump. Pinching contracts trace distance, and its blocks are orthogonal. In the ideal output each block factors from the same pure coherent pump; its weight is p_n. On block n the residual pump generator is (2K+n-m)². Consequently

    D(U_e sigma U_e†,sigma) >= sum_n p_n D_n(epsilon).

The ideal field-number mean is25.6 for ten vacuum calls (K2279). Hence Pr[N<=100]>=1-25.6/101=377/505, without any normalized postselection. For Y=K-mu, the centered generator on block n is Z_n=Z_0+4nY. Its variance is32mu²+16mu n², at least32mu². For independent copies, (a+b)^4<=8(a^4+b^4) and E(Y-Y')^4=2mu+12mu² give

    E(Z_n-Z_n')^4 <=8[4096mu²+73728mu³+36864mu⁴
                                     +256n⁴(2mu+12mu²)]
                         <=946176mu⁴

when mu>=10000 and0<=n<=100 (using n⁴<=mu² and mu>=1). With x=mu|epsilon|<=1/50,

    D_n²>=32x²-39424x⁴>=16x².

Triangle inequality and unitary invariance for rho0 then establish the actual full-instrument bound

    D(U_e rho0 U_e†,sigma) >= (1508/505)mu|epsilon|-delta_core.       (1)

A negative right side is vacuous. An additional commuting linear residual xi Q reduces this lower bound by at most2sqrt(mu)|xi|: within each number block its n phase is scalar and pump Q variance is4mu. Do not turn the Poisson result into a mixed thermal lower bound.

## 3. A duration-controlled pulse consumer

For the SPECIFIED constant-strength compensator H=h C_m, h>0 known, an unknown duration error deltaT yields epsilon=h deltaT after exact nominal cancellation. In the local region mu|h deltaT|<=1/50, a necessary condition for actual full error<=eta is

    |h deltaT| <=505(eta+delta_core)/(1508mu),

when xi=0. At mu=10^28 and eta=delta_core=10^-11 this is below6.70*10^-40. K2282's sufficient10^-42 allowance satisfies it; the gap is real, so the sufficient fixture is not an optimized clock cost. At epsilon=10^-42 the lower bound after subtracting delta_core is vacuous. For unknown bounded duration jitter, this is a worst-case deterministic guarantee, not an inference from timing variance alone. Near revivals use the actual local residual: integral-spectrum periodicity prevents a global monotone lower bound in |epsilon|.

## 4. A finite-clock countercontrol prevents universalization

Reuse the supplied-unitary history-clock idea of [K2238](k2238-finite-clock-thermal-circuit-2026-10-29.md). For ANY supplied U_theta=exp(-i theta C_m), define the one-qubit clock Hamiltonian

    H=g[I+|1><0| tensor U_theta+|0><1| tensor U_theta†], g>0.

The off-diagonal involution squares to identity, so H is bounded, positive and has spectrum {0,2g}, even on the infinite oscillator space. Clock initial |0> yields exactly |1> tensor U_theta psi up to global phase at T=pi/(2g). At T+deltaT, discarding the clock gives

    cos²(g deltaT) Ad(U_theta)+sin²(g deltaT) Id,

with full data/pump/record half-distance error at most sin²(g deltaT), independent of mu. This does not contradict(1): its timing error is a mixture, not an unknown area of C_m. It HIDES the entire exact nonlinear unitary in the clock coupling. It is neither synthesis of C_m nor an inexpensive device. The example shows why duration bounds cannot be generalized to every autonomous finite clock without specifying accessible interactions and readout resources.

## 5. Released consequence: shorter supported positive compensation

The vacuum consumer has EVEN total Q=2K at preparation, and the actual conserving circuit preserves that support. For integer mu and m=2mu+1 odd, C_m=(even-odd)² is1 modulo8. Therefore exp(-i pi C_m/4) is a scalar on the entire occupied charge support. K2282's universal2pi period is valid but unnecessarily long for this consumer. Choose the final positive compensator area theta=pi/4-80log3/sqrt(mu) at mu=10^28. It cancels the accumulated shift up to a scalar and reduces the near-revival area by almost eightfold. All actual support is retained, not a numerical number cutoff. The unknown area/linear-error budget is unchanged.

The earlier a0=1 positivity certificate cannot be inherited because theta<1. Here theta>1/2 even after |epsilon|<=10^-42. Use a0=1/2 and the known scalar offset c0=Xm+X²/(4a0) for |xi|<=X; this makes the actual final generator positive. The scalar has no channel effect but remains a supplied resource. Mean compensator action theta EC_m is reduced; pump shifted-control action, intrinsic coefficient accuracy and physical synthesis are not removed. Outside the even-Q support, the shorter period need not implement the target. This exact consequence also makes the local-versus-global timing qualification operational.

## Reproducibility and successor

Exact moments, finite clock matrix controls and real formula/parameter faults accompany the proof. The pinching argument is the crucial channel transfer; no manifest assertion or finite truncation proves it. A useful next physical test must specify accessible Hamiltonians and clock coupling/calibration costs, or measure the actual centered pulse error. Larger clocks alone do not answer that question. No external-expert, Lean, hardware or novelty certification is claimed.
