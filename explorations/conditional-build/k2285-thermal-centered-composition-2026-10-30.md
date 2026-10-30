---
title: "K2285 Thermal centered controls with complete energy accounting"
status: active_research
doc_type: exploration
created: "2026-10-30"
classification: INTERNAL_STRUCTURAL_ONLY
target_claim: NONE-NOT-A-KILL
claim_ceiling: conditional supplied model only; no native GU or canonical verdict
scripts:
  - tests/channel-swings/k2285_thermal_centered_composition_probe.py
---

# K2285 Thermal centered controls with complete energy accounting

> **GU-COMPARATOR-ROUTING — scope before inference.** This artifact contains or borders a conventional particle-physics comparator. Any result about a standard Higgs/VEV, ordinary family index or net chirality, SO(10) `126` Majorana mechanism, anomaly selector, VEV-only breaking or familiar vector-mass route binds only that named model. It is not evidence for or against Weinstein's source-native mechanism without an explicit typed bridge. Read `lab/methods/source-native-comparator-routing.md` and follow its source-native pointers before reusing this result.

Classification: `INTERNAL_STRUCTURAL_ONLY`.

```gu-typed-objects
result: K2285 Thermal centered controls with complete energy accounting
carrier: fresh vacuum field pairs, displaced thermal pump and positive global charge controls LAYER=toy CHIRALITY=N/A
pairing: positive complex Hilbert inner product ON=declared_carrier
real_structure: complex conjugation and Hilbert adjoint
grading: no native Clifford or chirality transfer
action_owner: repository-construction -- supplied conditional model
target: mixed-preparation centered-control instrument and energy bound MAP-TYPE=evaluation
```

## Result and scope

We compose [K2281](k2281-thermal-pump-preparation-2026-10-29.md)'s displaced thermal preparation with [K2282](k2282-centered-positive-control-2026-10-29.md)'s supplied global positive controls. The coherent variance cannot be reused: thermal occupation n=1 and displacement mu require center m=2mu+6 and Var C_m=288mu²+688mu+288. With mu=4*10^28, aggregate centered error10^-42 and linear error10^-28, the complete recorded instrument error remains below10^-11, actual field energy error below.008 quanta, and pump depletion12.8±.004 from its initial mean mu+1.

This closes a concrete composition gap, not hardware synthesis or energy catalysis. The pump is the specified phase-calibrated displaced thermal state, not an arbitrary trace-close preparation. The positive-control alphabet and its global nonlocal charge dependence remain supplied. SC-META-53 UNCERTAIN and LT-SM8/LT-GR6b/source/ledger0.263 remain unchanged. No native GU positivity is obtained.

## 1. Mixed number moments determine the center

Let rho=D(sqrt(mu))tau_nD†, with mu>0,n>=0, and K the number observable. Its cumulant generator is

    log E exp(tK)=-log[1-n(e^t-1)]+mu(e^t-1)/[1-n(e^t-1)].

Differentiation at zero gives kappa1=mu+n and

    kappa2=mu(1+2n)+n(n+1),
    kappa3=mu(1+6n+6n²)+n(n+1)(2n+1),
    kappa4=mu(1+14n+36n²+24n³)+n(n+1)(1+6n+6n²).

For vacuum fields Q=2K, delta=2(mu+n)-m and C_m=(Q-m)²,

    Var C_m=16[kappa4+2kappa2²+2delta kappa3+delta² kappa2].

The optimal REAL center is m*=2(mu+n)+kappa3/kappa2, from completing the square. Choosing the nearest nonnegative integer adds at most4kappa2 to the optimum variance16[kappa4+2kappa2²-kappa3²/kappa2]. Integer centering is needed by K2282's exact2pi periodicity. For n=1 and integer mu>=1, kappa3/kappa2=(13mu+6)/(3mu+2) lies between3.8 and13/3, so m=2mu+6 is nearest. Here delta=-4, giving

    Var C_m=288mu²+688mu+288, Var Q=12mu+8,
    EC_m=12mu+24.

At n=0 the formula recovers the coherent skewness correction m=2mu+1 and Var C=32mu². At n=1 neither that center nor that variance may be carried over.

## 2. Purification upper bound and positive implementation

For any purification Omega of rho and the initial field vacuum, spectral calculus and subtraction of scalar means imply

    ||[exp(-i(epsilon C_m+xi Q))-phase]Omega||
        <=|epsilon|sqrt(Var C_m)+|xi|sqrt(Var Q).

Partial trace bounds the actual mixed-state channel by this pure-vector bound; it supplies an UPPER bound, not the pure-state lower bound of K2284. All charged and neutral controls commute with Q, so moments can be computed at preparation, including retained pump and inaccessible purifier. Initial field vacuum is essential for the displayed exact moments; nonvacuum fields require their own joint charge cumulants.

Use K2282's B_z=4(C_m+d)/sqrt(mu)+H_z, d=2 ceil(sqrt(m+2))(m+2)+1, |z|<=2. Its all-shell positivity proof holds for this new integer m. Twenty exact shifted pump pulses plus one positive compensator cancel the known shift80log3/sqrt(mu) modulo2pi. Aggregate epsilon and independent xi occur only in the final compensator as before. With actual integrated generator a C_m+xi Q+c0I, a>=a0=1, |xi|<=X, the known scalar c0=Xm+X²/(4a0) certifies positivity. Pump shifts remain exact in this fixture; distributed unknown shift errors would require new per-stage bounds. No unknown error is canceled using its unknown value.

## 3. Complete numerical consumer, including energy

Take n=1,mu=4*10^28,J=10 vacuum calls,q=50 and K2279's10^-17 calibrated amplitude/phase/dispersive/neutral errors. K2281's quantum defect is identical to the coherent mu=10^28 core. Its conservative full error bound is

    Bcore=600(1+10^-17)/10^14 +440/(2^50+1)
                         +(3600+22000+260100)10^-17.

Add

    Bphase=10^-42 sqrt(288mu²+688mu+288)+10^-28 sqrt(12mu+8).

The companion uses exact rational upper bounds sqrt(Var C)<17mu+100 and sqrt(Var Q)<7*10^14 at this mu; Bcore+Bphase<10^-11. The signed core guarantee, phase correction, classical records and original mixed pump are composed before tracing anything out. Ancilla/pulse counts remain K2282's supplied circuit, including its extra positive global compensator.

K2281 proves actual E(N_all+1)²<6,300,000 for this fixed fresh-input consumer. Added Q functions commute with every field number, so these moments are exactly unchanged relative to the calibrated signed core. The ideal bound and the actual one imply |E N_actual-E N_ideal|<.008 by [K2273](k2273-positive-control-energy-2026-10-29.md)'s sharp bound sqrt(M2 delta), with no extra factor two, at total error10^-11. Exact Q conservation gives E N_out=2[(mu+1)-E K_out], and the ideal field increment is25.6. Pump depletion is12.8±.004. The pump's total energy grows with mu; returning its density matrix closely is not returning all its energy.

Preparation phase, number moments, centered-control calibration and conserved charge play different roles. Number-dephased preparation with the same number law still fails the full instrument as K2281 proves. The new calculation fixes mixed variance and composes existing conditional controls; it does not synthesize preparation, centered coupling or a finite laboratory clock. Those are the next concrete physical inputs, with K2284 supplying a control-model-specific diagnostic.

## 4. Supported compensation and remaining preparation cost

The thermal number mixture still has total Q=2K even, while m=2mu+6 is even. C_m is4 times an integer square, so exp(-i pi C_m/2)=I on this support. The final area may be theta=pi/2-80log3/sqrt(mu), a nearly fourfold reduction from the universal2pi implementation. At mu=4*10^28, theta>1 even with the stated error, so a0=1 and the scalar positivity offset remain valid. Unknown errors and full instrument/moment bounds are identical. The mean compensator action is theta(12mu+24); it remains order mu. This support-specific improvement does not apply to arbitrary odd-charge inputs and does not turn trace restoration into energy restoration.

## Verification

The companion differentiates the generating function independently, derives the variance from raw moments, checks coherent/thermal limits, integer center and exact full error/energy bounds, and tests actual wrong-center/coherent-variance/rate/charge formulas with the same predicates. The analytic purification and conserving-shell arguments carry the unbounded claims. Internal review is not external-expert, Lean, novelty or hardware certification.
