---
title: "K2281 Thermal preparation with full detector and energy bounds"
status: active_research
doc_type: exploration
created: "2026-10-29"
classification: INTERNAL_STRUCTURAL_ONLY
target_claim: NONE-NOT-A-KILL
claim_ceiling: conditional supplied model only; no native GU or canonical verdict
scripts:
  - tests/channel-swings/k2281_thermal_pump_preparation_probe.py
---

# K2281 Thermal preparation with full detector and energy bounds

> **GU-COMPARATOR-ROUTING — scope before inference.** This artifact contains or borders a conventional particle-physics comparator. Any result about a standard Higgs/VEV, ordinary family index or net chirality, SO(10) `126` Majorana mechanism, anomaly selector, VEV-only breaking or familiar vector-mass route binds only that named model. It is not evidence for or against Weinstein's source-native mechanism without an explicit typed bridge. Read `lab/methods/source-native-comparator-routing.md` and follow its source-native pointers before reusing this result.

Classification: `INTERNAL_STRUCTURAL_ONLY`.

```gu-typed-objects
result: K2281 Thermal preparation with full detector and energy bounds
carrier: fresh two-mode fields, displaced thermal pump, neutral records and external history LAYER=toy CHIRALITY=N/A
pairing: positive complex Hilbert inner product ON=declared_carrier
real_structure: complex Hilbert conjugation and adjoint
grading: no native Clifford or chirality transfer
action_owner: repository-construction -- supplied conditional model
target: phase-sensitive full-instrument and moment control MAP-TYPE=evaluation
```

## Result and preparation model

Replace K2279's exact coherent pump by the explicitly specified displaced thermal state rho_c=D(alpha) tau_n D(alpha)†, alpha=sqrt(mu)>0, with independent thermal occupation n>=0. mu is DISPLACEMENT intensity; the initial mean pump number is mu+n. Its phase is calibrated relative to the target quadrature. This is a preparation model, not an assertion that a device attains it, nor a bound for arbitrary states merely trace-close to it.

The charged trilinear pulses, neutral circuit, full recorded instrument and actual calibration model are precisely [K2278](k2278-calibrated-pump-detector-2026-10-29.md). SC-META-53 stays UNCERTAIN; LT-SM8/LT-GR6b, source and ledger0.263 are unchanged. The supplied positive bosonic Hilbert space is not a constructed native GU quotient.

## 1. Purification proves the retained-pump comparison

Purify tau_n as |T_n>=sum_k sqrt[p_k]|k,k>, p_k=n^k/(1+n)^(k+1), and define |Omega_n>=(D(alpha) tensor I)|T_n>, displacing only the first oscillator. Write d=c-alpha. The vectors d|Omega_n>,d†|Omega_n> have norms sqrt(n),sqrt(n+1), are orthogonal to each other and to |Omega_n>, because <d>=<d²>=0. The physical pump and its inaccessible purifying reference are retained throughout the mathematical comparison.

For A=a1 a2, N=n1+n2, G=N+1, the quantum pump defect on a field vector psi is

    (i/sqrt(mu))[z A† d-conjugate(z) A d†] psi |Omega_n>.

Its squared norm equals |z|²/mu times

    n ||A†psi||²+(n+1)||Apsi||²
      = < (2n+1)n1n2+n(N+1) >.

Using n1n2<=N²/4 proves the sharp uniform G-bound

    C(n)²=max{n,(2n+1)/4},
    defect norm <=|z| C(n)/sqrt(mu) ||Gpsi||.

For n>=1/2 compare the quadratic to n(N+1)²; the difference is nonnegative. For n<=1/2 compare to (2n+1)(N+1)²/4. Vacuum saturates the former, balanced large occupations approach the latter. The coherent n=0 coefficient is1/2, as required.

Thus K2278 equations(4)-(5) hold with

    E_sigma=integral_0^log3 f(t)
       [sqrt2 |z_sigma-sigma|+|z_sigma| C(n)/sqrt(mu)]dt.

The same ideal-prefix/actual-suffix hybrid applies: the comparison pump is unchanged and independent at each ideal prefix, while actual pump correlations need not vanish. Purification followed by partial trace proves the full field/record/history/ORIGINAL mixed-pump guarantee. The displaced thermal purification has finite c,c† moments, so K2278's D(G)-graph-continuous Duhamel comparison is applicable. Controllers must not access the pump. A fixed bounded n gives convergence as mu grows; n=o(mu) suffices for this quantum-defect allowance. If n is proportional to mu, the bound need not vanish; that alone is not an actual error-floor proof.

## 2. Actual moments from the displaced thermal number law

For fixed fresh Nj<=1 inputs and isolated outputs, K2279's weighted-Q shell proof is unchanged. It needs the actual number exponential moment, not a coherent-state label. Let K be the initial pump number, a=4 max Aj, c=a/2, J the number of calls. The displaced thermal generating function is

    E exp(tK) = [1-n v]^-1 exp[mu v/(1-n v)],
    v=exp(t)-1, n v<1.                                  (1)

For n>0, integrate exp(v|alpha+beta|²) over the circular complex Gaussian beta of variance n (the positive coherent-state mixture of tau_n); completing the Gaussian square gives(1). n=0 is its Poisson limit. Differentiation yields mean mu+n and variance mu(2n+1)+n(n+1).

Consequently the actual field moment is bounded by

    E(N_all+1)² <=9J² F_n(mu),
    F_n(mu)=exp[a/2+aJ/(4mu)]
       [1-n v]^-1 exp[mu v/(1-n v)], v=exp(c/mu)-1.       (2)

For fixed n and sufficiently large mu this is uniform: v and mu v decrease as mu increases, denominator1-nv increases, and all positive factors decrease. The proof only uses actual initial independence, charge distribution and bounded field input, not final pump independence. Tonelli over finite shells justifies the unbounded expectation. Arbitrary adaptive energy injection remains outside this consumer.

For n=1,J=10,a<=44/5,mu>=4*10^10, use v<=c/(mu-c), -log(1-v)<=v/(1-v). Then

    log F_1(mu)<=a/2+aJ/(4mu)+(mu+1)c/(mu-2c)<881/100.

K2279's exact integer bound exp(881/100)<7000 gives the SAME actual field second moment<6,300,000. Total pump energy is still unbounded as mu increases.

## 3. Full numerical consumer and depletion

For n=1, C=1. Choosing mu=4*10^10 exactly matches the coherent quantum-defect budget at10^10: K2278's q17,10^-8 amplitude/phase/dispersive/neutral conditions still give full ten-call error<.009791. Choosing mu=4*10^28 matches K2279's q50,10^-17 conditions, giving delta<10^-11 and field-energy error<.008 quanta with the SAME field moment bound. Preparation energy is now mu+1 pump quanta. No unpriced preparation trace error is silently added to the moment theorem.

On ten fresh vacuum inputs, exact charge conservation gives

    E N_all,out=2[(mu+1)-E n_c,out].

The ideal instrument adds25.6 field quanta, hence actual pump depletion from its INITIAL MEAN mu+1 is12.8±.004. This is simultaneous full-state proximity and real energetic consumption, not energy catalysis.

## 4. Same number statistics do not supply phase

Dephase the specified pump in its number basis. This preserves its entire number law, mean, variance and(1), so the FIELD moment bound remains valid. But with vacuum fields and neutral preparations, the input is invariant under weighted-Q phase rotations. Every declared charge-conserving circuit is covariant; after discarding the pump, each recorded field block commutes with N.

The ideal record0 branch is |v><v| with v=E|00> for E=S_r†P0S_r, r=log3. Writing S_r†|00>=sum_k (3/5)(-4/5)^k|kk>, E|00>=(3/5)S_r†|00>. Thus its |00> and |11> amplitudes are9/25 and-36/125 (sign follows squeeze convention), so their coherence is-324/3125. The norm-one witness (|00><11|+|11><00|) tensor |0_record><0_record| has zero expectation for every invariant output and ideal expectation-648/3125. Trace-norm duality therefore gives full instrument half distance at least324/3125=.10368, even after discarding pump. This tests field-plus-record coherence, not just record probabilities.

This is an actual failure example under unchanged number statistics. It identifies a phase-sensitive preparation requirement that energetic tests cannot replace. Arbitrary trace-close preparation still needs its own moment and phase control; the theorem is confined to the declared displaced-thermal family.

## Verification and physical boundary

The probe checks independent two-mode number identities, exact finite diagonal-purification shift sectors, Gaussian MGF derivatives, the full consumer budgets and actual record-block witness. Finite truncations are controls, not proofs of the infinite thermal law. Written purification/Gaussian/direct-sum arguments carry the universal claims. Internal review is not external certification, Lean, hardware viability or novelty. The next physical interface must specify phase-controlled preparation, measured trilinear/resonance and control tolerances; replacing this state by an arbitrary approximate laboratory state requires actual moment evidence.
