---
title: "K2278 Calibrated errors for the complete pump detector"
status: active_research
doc_type: exploration
created: "2026-10-29"
classification: INTERNAL_STRUCTURAL_ONLY
target_claim: NONE-NOT-A-KILL
claim_ceiling: conditional supplied model only; no native GU or canonical verdict
scripts:
  - tests/channel-swings/k2278_calibrated_pump_detector_probe.py
---

# K2278 Calibrated errors for the complete pump detector

> **GU-COMPARATOR-ROUTING — scope before inference.** This artifact contains or borders a conventional particle-physics comparator. Any result about a standard Higgs/VEV, ordinary family index or net chirality, SO(10) `126` Majorana mechanism, anomaly selector, VEV-only breaking or familiar vector-mass route binds only that named model. It is not evidence for or against Weinstein's source-native mechanism without an explicit typed bridge. Read `lab/methods/source-native-comparator-routing.md` and follow its source-native pointers before reusing this result.

Classification: `INTERNAL_STRUCTURAL_ONLY`.

```gu-typed-objects
result: K2278 Calibrated errors for the complete pump detector
carrier: two bosonic field modes, coherent pump, neutral registers and arbitrary external history LAYER=toy CHIRALITY=N/A
pairing: positive complex Hilbert inner product ON=declared_carrier
real_structure: complex Hilbert conjugation and adjoint
grading: declared oscillator charge where used; no native Clifford or chirality transfer
action_owner: repository-construction -- supplied conditional model
target: full recorded instrument with original pump retained MAP-TYPE=intertwiner
```

## Result and boundary

[K2276](k2276-structured-detector-implementation-2026-10-29.md) supplies a finite trilinear/neutral detector but leaves an implementation allowance unspecified. This result connects explicit complex pump calibration, dispersive pulse-area errors and bounded neutral-gate errors to the COMPLETE field/record/history/original-pump trace error. It is a theorem for a declared error model, not a hardware calibration measurement, an autonomous clock construction or a GU physical quotient. SC-META-53 remains UNCERTAIN; LT-SM8/LT-GR6b and ledger0.263 are unchanged.

Keep A=a1 a2, N=n1+n2, G=N+1, r=log3, target E=S_r†P0(n1)S_r and the correctly labeled K2276 Lüders circuit. The pump starts in the exact independent coherent state |alpha>, alpha=sqrt(mu)>0. Its phase is calibrated against the intended field quadrature. The actual pulse generator is

    H_z(t)=i[ z(t) A† c - conjugate(z(t)) A c† ]/sqrt(mu), (1)

over t in[0,r]. The ideal sign is sigma=+1 or-1. Assume bounded piecewise-continuous z(t). Each fixed weighted-Q shell, Q=N+2n_c, is finite; time-dependent Hermitian block propagation defines the unitary direct sum. A complex phase error preserves this Q. Unknown leakage, extra charged couplings, unbounded neutral perturbations and nonconserving noise are outside(1).

The middle finite register circuit computes n1 mod D, D=2^q, flips the output record (initialized in|1>) on zero, and uncomputes its workspace. It approximates the vacuum predicate, as in K2276. Actual dispersive gates are exp[-i(theta+delta_theta)n1 P_bit]. Actual neutral gates are unitary on neutral space, each within eta_l in operator norm of its ideal gate. Number-phase errors and neutral gates preserve N; their precision is a requirement, not evidence that a device meets it.

## 1. Generator error on the actual comparison domain

For psi in D(G), K2276 proves

    ||G S_t psi|| <= f(|t|)||Gpsi||,
    f(t)=cosh(2t)+sqrt2 sinh(2t),
    I=integral_0^r f(t)dt=(20+16sqrt2)/9<5,
    f=f(r)=(41+40sqrt2)/9<11.                       (2)

On a coherent-product orbit, (c-alpha)|alpha>=0 and ||(c†-alpha)|alpha>||=1. Therefore the defect from sigma Hs is exactly the sum of the systematic field term i[(z-sigma)A†-(conjugate(z)-sigma)A] and the orthogonal pump-fluctuation term -i conjugate(z) A(c†-alpha)/sqrt(mu). Bounding the two terms by the triangle inequality gives

    ||defect|| <= [sqrt2 |z-sigma|+|z|/(2sqrt(mu))]
                 ||G S_(sigma t)psi||.             (3)

Indeed ||Apsi||<=||Gpsi||/2, and ||A†psi||+||Apsi||<=sqrt2||Gpsi|| follows from the number-basis inequalities. No scalar substitution for c in the actual dynamics is made. Duhamel on these graph-continuous product curves, first for finite-particle inputs then by D(G) closure, yields

    E_sigma=integral_0^r f(t)[sqrt2 |z_sigma(t)-sigma|
                            +|z_sigma(t)|/(2sqrt(mu))]dt,
    pulse vector error <=E_sigma ||Gpsi||.          (4)

The finite-shell propagators and locally bounded coefficients justify this nonautonomous comparison; external spectator spaces pass through unchanged.

## 2. Circuit errors and the full instrument

For a dispersive error, spectral calculus gives

    ||(e^(-i delta_theta n1 P)-I)phi||
       <=|delta_theta| ||n1 phi||<=|delta_theta| ||Gphi||.

An ideal circuit prefix preserves N, even when work qubits are entangled with the field. The summed dispersive area error d_theta=sum|delta_theta| therefore costs at most f sqrt(M2)d_theta at the middle circuit, with M2=Tr(G²rho) before the detector. Neutral gate errors cost sum eta_l. This circuit hybrid does not assert that imperfect workspace returns exactly to zero: any residual correlation is already in the full error estimate before workspace is discarded.

Combining forward pump, finite-predicate alias, middle-circuit calibration and reverse pump by an ideal-prefix/actual-suffix hybrid gives

    e_call <= sqrt(M2)[E_plus+f E_minus
                     +2f/(D+1)+f d_theta] +sum eta_l.  (5)

The reverse error is evaluated on the IDEAL C0 S_r state; the actual pump need not remain coherent or independent between pulses. Half trace distance after recording/dephasing is no greater than this vector bound. Arbitrary external history and the original pump remain retained in the comparison target.

For J adaptive calls, sum(5) using each ideal unconditional input M2_j, provided controllers do not access the pump. Subsequent actual channels contract trace distance. This is an averaged history guarantee, not uniform normalized rare postselection. A preparation trace error epsilon_prep can be added for this CHANNEL statement only; it supplies no energetic moment guarantee.

If |z_sigma-sigma|<=kappa and |z_sigma|<=Z, then E_sigma<=I(sqrt2 kappa+Z/(2sqrt(mu))). For z_sigma=sigma(1+e)exp(i phi), |e|<=epsilon_a, |phi|<=epsilon_phi, the exact decomposition (1+e)exp(i phi)-1=e exp(i phi)+(exp(i phi)-1) gives kappa<=epsilon_a+epsilon_phi and Z<=1+epsilon_a.

## 3. A concrete calibration budget

Take the K2276 fresh-register or other qualifying J=10, M2_j<=4 consumer, mu=10^10, q=17. Require BOTH pump amplitude and phase errors <=10^-8 on every pulse, every one of340 dispersive areas within10^-8 radians, and each of at most32400 neutral gates within10^-8 in operator norm. Exact coherent preparation, fixed addressed modes, and the declared resonance/rotating-frame control model are assumed. Then

    delta <600(1+10^-8)/sqrt(mu) +440/(2^17+1)
            +1200 sqrt2*(2*10^-8)
            +22*(340*10^-8)+32400*10^-8
          <0.009791.                                (6)

This includes the quantum pump approximation and finite-modulus alias, not just calibration. It budgets detector cores only; actual routing errors require their own full-channel bounds. The numerical precision demands are stringent supplied conditions, not practical control claims. Signed pump pulses and phase reference preparation remain external resources.

The original mean-only input class can still use K2276's subnormalized truncation proof, replacing its coefficient by the bracket in(5). We do not infer finite second moments from that extension or claim the numerical M2<=4 budget for arbitrary mean-only inputs.

## 4. Energy is an independent successor

All operations in this declared error model preserve weighted Q, but its naive total moment grows with mu². That fact alone does not make channel convergence imply energetic convergence. [K2279](k2279-uniform-pump-energy-2026-10-29.md) proves a stronger, pump-uniform actual FIELD moment for fixed fresh inputs and isolated outputs, then composes a finite energy-accuracy consumer. Its stronger preparation/routing/input assumptions are essential; arbitrary trace-close preparation or adaptive energy injection cannot inherit it.

## Verification and remaining requirements

The companion probe verifies coherent fluctuation and number-pair bounds, exact conservative budget arithmetic, circuit phase inequalities on finite number states, actual Hermitian weighted-shell matrices and charge conservation, and changed input/phase/covariance-free control faults. Written domain and adaptive hybrid proofs are separate from these finite checks. Independent internal review is not Lean, external-expert, novelty, hardware or remote-CI certification.

A physical implementation still must supply the trilinear coupling/resonance, clock and phase source, stable pulse signs or compensated positive controls, preparation and routing, and measured calibration at the displayed tolerances. This closes the mathematical coefficient-to-channel transfer for(1), not that engineering task.
