---
title: "K2332 Exact JC selective control and noisy state synthesis"
status: active_research
doc_type: exploration
created: "2026-10-30"
classification: CONVENTIONAL_COMPARATOR
target_claim: NONE-NOT-A-KILL
claim_ceiling: conditional mathematics; no empirical, hardware or native GU acceptance
scripts:
  - tests/channel-swings/k2332_exact_jc_selective_control_probe.py
---

# K2332 Exact JC selective control and noisy state synthesis

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
result: K2332
carrier: full finite pilot-reference-mediator excitation carrier Q<=N, target fixed lower shell Q=N LAYER=toy CHIRALITY=N/A
pairing: positive complex Hilbert norm and full-channel trace distance ON=declared_carrier
real_structure: complex state vectors with Hermitian adjoint; no Fourier reality identification
grading: total excitation including mediator; lower and upper dressed branches retained
action_owner: repository-construction -- rotating-wave Jaynes-Cummings drift, supplied complex bare hopping, physical Markov loss
target: finite-shell selective synthesis with explicit phase, leakage and duration bounds MAP-TYPE=evaluation
```

## Result and limits

[K2330](k2330-microscopic-kerr-validity-2026-10-30.md)'s nominal Kerr compiler suffers accumulated nonquadratic drift and transformed-control error. Here the SAME microscopic JC spectrum is used exactly. A finite-shell all-branch separation theorem, the full bare hopping matrix and an explicit averaging bound give constructive preparation of any known LOWER-DRESSED state in a fixed excitation shell. Exact lab-phase programming accounts for the entire duration without a Kerr revival or a free terminal correction. The resulting same-device control/noise inequality has a solvable amplitude window.

This does NOT complete [K2328](k2328-local-neutral-readout-compiler-2026-10-30.md)'s unknown-state neutral-memory readout: number-copy, conditional parking, neutral measurement/reset and their microscopic rates remain separate. A unitary cannot map every unknown optical state to one fixed optical state without another record. The target here includes the dressed mediator; it is not automatically a pure optical state. Source SC-ACT-01/GEO-55/COS-50/51/54 ASSERTS, SC-META-53 UNCERTAIN and ledger0.263/native GU verdicts remain unchanged. Positive Hilbert space, JC rotating-wave model, complex hopping and Markov noise are supplied conventional inputs, not native quantization or a feasible device. State control in JC systems is established prior art; e.g. [Vogel, Akulin and Schleich](https://doi.org/10.1103/PhysRevLett.71.1816). No novelty is asserted for generic state synthesis.

## Exact spectrum, carrier and all transition blocks

Take Delta,g>0, hbar=1, H0=Delta|e><e|+g(a_P sigma_++a_P†sigma_-), protected reference mode R, conserved Q=n_P+n_R+|e><e|<=N, N>=1. Keep K2330's exact dressed vectors c_n|n,g>-s_n|n-1,e> and s_n|n,g>+c_n|n-1,e>, theta_n=(1/2)atan(2g sqrt(n)/Delta), c_n=cos theta_n,s_n=sin theta_n. Put

    R_n=sqrt(Delta²+4g²n), E_n^-=(Delta-R_n)/2,
    E_n^+=(Delta+R_n)/2, d_n=(R_n-R_(n-1))/2.

The vacuum has E0=0 and only a lower label. In fixed shell Q, the physical B=a_R†a_P has edge block from excitation n to n-1 equal to sqrt(Q-n+1) times

    [[alpha_n, gamma_n], [beta_n, eta_n]],
    alpha_n=sqrt(n)c_n c_(n-1)+sqrt(n-1)s_n s_(n-1),
    beta_n=sqrt(n)c_n s_(n-1)-sqrt(n-1)s_n c_(n-1),
    gamma_n=sqrt(n)s_n c_(n-1)-sqrt(n-1)c_n s_(n-1),
    eta_n=sqrt(n)s_n s_(n-1)+sqrt(n-1)c_n c_(n-1).          (1)

At n=1 retain only the first row and set c0=1,s0=0. This is the actual unitary conjugation of the bare lowering operator, not a branch-preserving approximation. c_n>1/sqrt2 gives alpha_n>=sqrt(n)/2. Every edge magnitude is <=sqrt[n(Q-n+1)]<=(N+1)/2, by the norm of its bare block.

## Spectral separation: no upper-branch collision

For downward B edges define omega_ab=E_n^b-E_(n-1)^a. The lower frequencies are omega_n=-d_n<0, strictly increasing in n. Upper intrabranch frequencies are+d_n for n>=2. Cross frequencies are ±(R_n+R_(n-1))/2; at n=1 the upper-to-vacuum frequency is(Delta+R1)/2. Select omega_k=-d_k. On a fixed n range0..N, every nonselected frequency differs from omega_k by at least

    delta_N=2g^4/(Delta²+4g²N)^(3/2)>0.                   (2)

Proof: E_-''(x)=2g^4/(Delta²+4g²x)^(3/2). Integrating this over the unit-square second-difference representation proves consecutive lower spacings >=delta_N; further spacings only increase. Positive intrabranch edges are separated by at least d_N. Also d_N=2g²/(R_N+R_(N-1))>g²/R_N>delta_N, since R_N²>2g². The negative cross edge with n>=2 has magnitude at least(R2+R1)/2, exceeding d1 by(R2+Delta)/2; the positive ones are farther. Vacuum upper is positive. This proves(2) without finite numerical gap sampling.

There IS an exact cross-shell degeneracy: the SAME lower edge k has omega_k in EVERY shell Q>=k, with coupling b_(Q,k)=alpha_k sqrt(Q-k+1). No detuning claim separates these. The whole-carrier ideal resonant Hamiltonian retains their direct sum; a swap calibrated on shell N is not a swap on every Q. Loss can populate smaller shells, so this distinction survives error accounting.

## Complex physical tone and rigorous averaging

Assume an independently programmable COMPLEX hopping

    C(t)=u exp[i(omega_k t+phi)] B + conjugate.             (3)

Both quadratures are a hardware assumption. In the interaction picture of the exact H0, the selected lower edges are stationary with phase phi. A real cosine would also supply the opposite-frequency tone and resonate with upper intrabranch+d_k; it cannot be silently given the same whole-carrier ideal. All upper states are retained in the following comparison even for lower input.

For shell N set b_k=alpha_k sqrt(N-k+1)>=sqrt(N)/2, u=J/b_k, J>0. The resonant direct sum Hsel has norm J (smaller shells have smaller couplings). Write HI=Hsel+V(t). The full physical drive has norm<=N|u|, so ||V||<=N|u|+J. Each node has at most four dressed neighbours and an off-resonant integral contributes at most2 times its coefficient/detuning. Therefore its primitive F(t)=integral_(t0)^t V(s)ds obeys

    ||F|| <= f_k=4(N+1)|u|/delta_N.                      (4)

Starting phases do not change this norm. Duhamel followed by integration by parts in Usel† F Uexact yields

    ||Uexact_I-Usel|| <= f_k[1+tau_k(3J+N|u|)].           (5)

The endpoint term is <=f_k and the differentiated unitaries cost ||Hsel||+||HI||<=2J+||V||. This is a universal operator-norm bound on the FULL Q<=N carrier for the declared ideal resonant direct sum. It also bounds half-diamond distance of unitary channels. It is valid when numerically uninformative; an error bound above1 does not prove failure.

For the pulse-only schedule with NO additional idles, at most N adjacent rotations with angles0<=theta_k<=pi/2, tau_k=theta_k/J, product telescoping and b_k>=sqrt(N)/2 give

    e_control <= A_N J,
    A_N=8N(N+1)/(delta_N sqrt(N)) *[1+(pi/2)(3+2sqrt(N))],
    T<=B_N/J, B_N=Npi/2.                                (6)

Thus for fixed finite N the lossless error tends to zero with J, while time diverges. No quadratic energy approximation, nominal revival, free dressed control or offbranch omission enters(5).

## Constructive successor: arbitrary known lower-shell state

Start in |0,g>_P,atom |N>_R, which is exactly the n=0 lower state. Given normalized z0..zN, prepare sum z_n |n,->|N-n> with the reference/mode basis kept fixed. Compute residual weights r_k²=sum_(j=k)^N |z_j|². For k=1..N choose theta_k=atan2(r_k,|z_(k-1)|), taking0 if both vanish. Each selected adjacent rotation leaves |z_(k-1)| in level k-1 and sends residual r_k to k. Zero amplitudes simply skip or fully transfer; no division by a zero target amplitude occurs.

The durations depend only on magnitudes. Compute their total T FIRST. In the interaction picture target tilde_z_n=exp(iE_n^- T)z_n; program phases recursively so the new amplitude -i exp(-i phi_k) times the old amplitude has the phase of tilde_z_k. If an intermediate target coefficient vanishes, its arbitrary phase can be chosen to set the later nonzero coefficient. Overall global phase is irrelevant. Equation(3) uses absolute laboratory time, so pulses do not silently reset their carrier phase. Exact final drift exp(-iH0T) then gives z. Any declared additional idle duration is included in T and in this phase program. No free final phase gate is assumed.

The finite probe constructs a genuinely nontrivial complex target at N=3, implements its sequence using exact full JC matrices and the exact time-dependent-tone propagator, and compares it with the ideal synthesis. For one tone let L=n_P+|e><e|, D=H0-omega_k L and R(t)=exp(-i omega_k L t). Then

    U_lab(t1,t0)=R(t1) exp[-i(D+C_phi)(t1-t0)] R(t0)†.     (7)

This is an exact finite-matrix rotating-frame identity, not a numerical time-step approximation. The derivative -iR†Rdot=-omega_k L fixes its sign. It provides high-precision finite controls; the universal guarantee remains(1)-(6). Omitting beta/gamma, reversing the tone, losing absolute phase, or correcting only nominal Kerr phases changes the physical propagator and is tested as a real fault where applicable.

## Same-device noise and nonempty amplitude window

Keep K2330's physical jumps sqrt(kappa)a_P and sqrt(Gamma)sigma_- on Q<=N. Their half-diamond generator bounds sum to lambda=kappa N+Gamma; reference or neutral noise adds its actual bound. Loss compares to the IDEAL LOSSLESS preparation, with no exact heralding or commuted no-jump claim. Contractivity gives

    e_total <= e_input+e_other + A_N J + lambda B_N/J.    (8)

The initial reference stock, complex drive, known parameters/clock and endpoint measurement are supplied. Equations(8)-(9) use the pulse-only schedule of(6). Additional idle time T_idle still accrues physical noise: add lambda T_idle to(8), include its exact drift in the phase program, and subtract that cost from the remaining epsilon before(9). More generally use lambda times the actual total duration. Errors in those inputs contribute e_input/e_other; drift uncertainty costs its integrated Hamiltonian norm. Bare optical-only output is a different target and owes the mediator/encoding comparison.

For remaining tolerance epsilon>0 and lambda>0, this sufficient certificate is achievable iff

    epsilon² >= 4 A_N lambda B_N,
    J_- <= J <= J_+,
    J_±=[epsilon ± sqrt(epsilon²-4A_N lambda B_N)]/(2A_N), (9)

intersected with the physically allowed positive drive range. The unconstrained minimum is at J=sqrt(lambda B_N/A_N), value2sqrt(A_N lambda B_N). If lambda=0, every sufficiently small positive J works; J=0 itself never performs the preparation. This is feasibility of a CONSERVATIVE SUFFICIENT BOUND, not a physical no-go when(9) fails. Actual pulse angles and edge amplitudes can sharpen it; unspecified device rates do not establish its satisfaction.

The microscopic g,Delta,N determine delta_N together. Increasing detuning reduces spectral selectivity approximately as Delta^-3 at fixed finite N, even though it makes eigenvectors more nearly bare. The exact-frequency repair removes the Kerr Taylor phase debt but does not grant arbitrarily fast, low-noise control. This executed successor prices the same device's time/noise tradeoff instead of repeating abstract controllability.

## Verification and next question

Written proofs cover the all-shell detunings, full transformed carrier, norm/primitive/averaging bounds, constructive synthesis and positive-amplitude inequality. The companion probe separately labels exact algebraic checks and finite high-precision matrix controls, with baseline-first changed-input faults. Internal independent review is not external-expert, Lean or hardware certification.

The next microscopic obstruction is number-copy and neutral conditioned readout with an explicitly available spatial alphabet and rate/clock/noise law. A supplied ideal projector onto n or an arbitrary dressed unitary does not answer it. A physical implementation might use this selective lower-shell gate family, but must synthesize the record-preserving isometry and price its actual couplings, measurement and reset. Cosmological seed/tracer/observer selection and curved native source/receiver/domain remain independent research obligations.
