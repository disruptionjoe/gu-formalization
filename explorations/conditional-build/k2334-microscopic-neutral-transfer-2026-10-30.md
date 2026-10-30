---
title: "K2334 Microscopic dressed-state transfer and recorded readout"
status: active_research
doc_type: exploration
created: "2026-10-30"
classification: CONVENTIONAL_COMPARATOR
target_claim: NONE-NOT-A-KILL
claim_ceiling: conditional mathematics; no empirical, hardware or native GU acceptance
scripts:
  - tests/channel-swings/k2334_microscopic_neutral_transfer_probe.py
---

# K2334 Microscopic dressed-state transfer and recorded readout

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
result: K2334
carrier: full finite JC pilot-reference-mediator excitation carrier Q<=N with neutral qubit line, initial lower-dressed Q=N LAYER=toy CHIRALITY=N/A
pairing: positive Hilbert norm and half-diamond channel distance ON=declared_carrier
real_structure: complex adjoint, independent neutral qubits
grading: conserved total excitation Q, local JC excitation L, and neutral binary record
action_owner: repository-construction -- exact rotating-wave JC plus supplied matched bare dispersive and neutral local gates
target: coherent unknown-state transfer and unconditional finite recorded instrument MAP-TYPE=evaluation
```

## Result and alphabet that actually changes

[K2332](k2332-exact-jc-selective-control-2026-10-30.md) prepares a KNOWN lower-dressed state. This note constructs an isometry for EVERY unknown state in that same lower-dressed fixed-N shell, retaining external entanglement, by adding a specifically declared coupling. It compiles number-copy, record-controlled parking and a finite Fourier measurement/reset channel. It does not claim the original hopping-only alphabet already did this.

Keep K2332's exact rotating-wave JC H0=Delta P_e+g(a_P sigma_++a_P†sigma_-), reference R, Q=n_P+n_R+P_e<=N, bare hopping B=a_R†a_P and programmable complex I/Q tones. Delta,g>0,N>=1. Add a neutral qubit at a single optical contact with signed matched interactions

    H_d(t)=chi(t)(n_P+P_e) Z_f=chi(t)L Z_f,
    |chi(t)|<=chi_d, [L,H0]=0, [L,B]=-B.                 (1)

This requires BOTH bare photon-number/neutral and mediator-population/neutral couplings at equal coefficients. It is not a free dressed projector. Also supply arbitrary one-qubit and adjacent two-qubit neutral unitaries with Hamiltonian norm cap g_q and known phases; a unitary logarithm implements each in time at most pi/g_q. Single-qubit rotations alone do not provide entangling neutral gates. Contact and hopping are off during neutral routing. Reference protection, fresh pure neutral registers, clock and the rotating-wave/Markov descriptions remain assumptions. No microscopic device model here derives these additional resources.

Source SC-ACT-01/GEO-55/COS-50/51/54 ASSERTS and SC-META-53 UNCERTAIN, ledger0.263 and all native verdicts remain unchanged. This is positive-Hilbert conventional apparatus mathematics, not a physical GU quotient, hardware feasibility or a source mechanism test.

## Exact dressed-number copy and its phase

Write |n> for |n,->_(P,atom)|N-n>_R, n=0..N. L|n>=n|n>. Choose d=2^q>N, alpha_j=2pi 2^j/d, j=0..q-1, S=sum alpha_j=2pi(1-1/d). Prepare q neutral bits B in |+>, then route each to the contact and apply exp(-i alpha_j L Z_j/2). On input n the register is

    exp(-inS/2) d^(-1/2) sum_(b=0)^(d-1) exp(2pi i nb/d)|b>.

Apply inverse Fourier and the q actual one-bit gates diag(1,exp[i(S/2)2^j]). This removes the scalar exp(-inS/2) exactly and copies n coherently. Without those gates relative phases of an unknown state are wrong even if number-readout probabilities pass. Total contact time is S/(2chi_d)<pi/chi_d. Neutral gates and physical drift consume time; they are not free.

The copy is an isometry, not cloning: sum c_n|n>|0> becomes sum c_n|n>|n>. No measurement or decoherence occurs before parking.

## Exact conditional selective swap from two half pulses

Reuse the full-carrier spectrum and primitive bound in K2332. The lower edge k has b_k=alpha_k^(JC)sqrt(N-k+1)>=sqrt(N)/2 and omega_k=E_k^--E_(k-1)^-. Keep all upper/cross-branch couplings and resonant copies on Q<N. Their nonselected frequencies have the held gap delta_N=2g^4/(Delta²+4g²N)^(3/2).

Let A=exp[-i(pi/2)LZ_f]. Then A B A†=i Z_f B. A selected complex tone with downward coefficient h b_k=iJ has ideal selected Hamiltonian H_h. The tone ih satisfies A H_(ih) A†=-Z_f H_h. Consequently with tau=pi/(2J),

    E_k=U_h(tau/2) A U_(ih)(tau/2) A†                  (2)

equals I on f=0 and exp(-iH_h tau) on f=1 in the ideal resonant model. Its downward transfer amplitude is+1. Chronological order is A†, second-phase half pulse, A, first-phase half pulse. Each contact takes pi/(2chi_d). This is two full selective halves, not an unpriced infinitely fast echo or a nominal Kerr revival. Comparing each physical half to its resonant ideal first makes the contact gaps harmless to the composition bound.

All tones use absolute lab phase omega_k t+phi across every contact and neutral gate. Every neutral gate and matched contact commutes with H0. Thus the full evolution is exp(-iH0 T) times the interaction-picture gate product, despite finite gaps. At the parked endpoint |0,g;N> the exact H0 energy is zero. Its final drift is identity. No n-dependent free terminal phase gate or approximate quadratic spectrum is needed. Resetting the carrier clock at each pulse breaks this argument.

## Explicit threshold logic and unknown-state parking

For k=N,N-1,...,1, reversibly compute f=[B>=k]. A concrete circuit adds the classical constant d-k to B into fresh carry bits, preserving B. If c_j is bit j of d-k and a0=0, set the clean carry a_(j+1) by:

    c_j=0: a_(j+1)=b_j a_j;
    c_j=1: a_(j+1)=b_j xor a_j xor (b_j a_j).

Use one Toffoli in the first case, two CNOT plus one Toffoli in the second. The final carry is exactly[B>=k]. A Toffoli uses at most15 elementary one-/two-qubit gates, so compute plus uncompute costs at most34q. Route the flag to the contact, execute(2), restore its location, then uncompute all carries.

For original label n, stages k>n are identity. Stage k=n lowers n to n-1; each remaining stage lowers once. Induction yields the coherent isometry

    sum c_n |n>|0>_B -> |0,g;N> sum c_n|n>_B.           (3)

Linearity includes an arbitrary entangled reference system. The retained neutral label prevents the unitarity obstruction to erasing an unknown optical state. Input is the lower-dressed Q=N shell; an arbitrary bare optical state or unknown upper-branch input is a different target. Full Q<=N operators are used for the error comparison, but calibrated swaps are not exact swaps in every smaller shell.

## Finite recorded instrument and honest reset cost

For phase measurement choose q=ceil(log2(N+2)), so d>=N+2. After(3) apply F_d with entries exp(2pi i rn/d)/sqrt d to B, copy its q computational bits into fresh outcome register E, and SWAP B into fresh blank register F. Trace the consumed F. This dephases E, retains its classical result, resets B to0, and leaves the carry scratch0. Fresh E/F purity and discarded F are explicit resources: this is a local reset channel, not a thermodynamic erasure bound or a restored environment.

On the fixed-N input its effects are

    E_r=(1/d)|eta_r><eta_r|,
    |eta_r>=sum_(n=0)^N exp(-2pi i rn/d)|n>, r=0..d-1. (4)

They sum to identity on the declared shell. For normalized sine coefficients a_n=sqrt[2/(N+2)]sin[(n+1)pi/(N+2)], input c_n=a_n exp(-2in phi), and estimate phi_hat=pi r/d modulo pi, the mean circular loss4sin²(phi_hat-phi) is exactly

    2[1-cos(pi/(N+2))].                                (5)

Discrete Fourier orthogonality leaves only adjacent n,n+1 terms when d>=N+2, and sum a_n a_(n+1)=cos(pi/(N+2)). With d=N+1 an additional wraparound endpoint term generally survives, so the minimal copy register is not always enough for(5). The test checks this changed physical dimension, not merely a declared bound.

There is NO exact loss-herald flag in this alphabet. A measurement of L does not measure Q because it omits n_R. The actual noisy instrument is compared unconditionally with(4); loss trajectories are included in its error. Reference-number sensing or another total-Q measurement is an additional construction. No error bound is silently reused after postselection.

## Uniform time, leakage, mismatch and noise budget

Each selective half is covered by K2332's full-operator averaging proof. The two half errors per edge sum to

    e_k <= 8(N+1)J/(delta_N b_k)
           *[1+(pi/4)(3+N/b_k)].
    e_sel <= A'_N J,
    A'_N=16N(N+1)/(delta_N sqrt N)
         *[1+(pi/4)(3+2sqrt N)].                       (6)

The ideal full-carrier resonant direct sums are retained in this comparison. For fixed-N input they realize(3); loss to other shells is controlled separately by channel perturbation. Total hopping time is B_N/J, B_N=Npi/2. Copy and the two contacts per edge cost

    T_d=pi(N+1-1/d)/chi_d.                             (7)

Allocate a neutral line of M=4q+2 sites for B, q+1 carries, contact spare, E and F. Any nonlocal two-qubit gate is routed and undone with at most2M SWAPs plus its gate. A conservative complete count, including two Fourier transforms, copy correction, final copying/reset and contact routing, is

    G <= (2M+1)(34Nq+2q²+8q)+2M(N+q),
    T <= B_N/J + T_d + pi G/g_q.                       (8)

A standard QFT has q Hadamards,q(q-1)/2 controlled phases and at most q/2 reversals; twice this plus initial Hadamards, q phase corrections, q outcome CNOTs and q reset SWAPs fits2q²+8q. Flag and copy-bit contact routing is explicitly in the last term. G is a conservative supplied-gate count, not a pulse count measured on a device. Physical hopping cap also requires J/b_k<=g_BS for every k.

If the contact is chi n_P Z+(chi+delta)P_e Z, the perturbation is delta P_e Z, norm|delta|, giving e_mismatch<=integral_contacts |delta|dt. A common coefficient error eta additionally costs N integral|eta|dt. Photon-only contact does NOT commute with JC drift, because[n_P,H0]!=0; omitting the mediator coupling cannot be dismissed as a phase convention. These bounds tolerate the resulting branch transitions without pretending the perturbed copy is exact.

For physical jumps sqrt(kappa)a_P,sqrt(Gamma)sigma_-,sqrt(kappa_R)a_R and a supplied neutral generator bound lambda_neutral, use lambda=kappa N+Gamma+kappa_R N+lambda_neutral. Duhamel/contractivity and product telescoping give half-diamond error

    epsilon_inst <= epsilon_in + A'_N J + lambda T
                    + integral ||Delta H(t)||dt.        (9)

Delta H includes actual clock, coupling and drift errors on the full retained carrier; exact controls do not certify those inputs. Subtract fixed overhead lambda(T_d+piG/g_q), known mismatch and input errors from tolerance epsilon. If the remaining epsilon_rem>0 and lambda>0, the sufficient pulse budget has a nonempty amplitude interval exactly when

    epsilon_rem² >= 4A'_N lambda B_N,
    J in [(epsilon_rem-sqrt(epsilon_rem²-4A'_N lambda B_N))/(2A'_N),
          (epsilon_rem+sqrt(epsilon_rem²-4A'_N lambda B_N))/(2A'_N)], (10)

intersected with the available hopping range. At lambda=0 any sufficiently small positive J works if the fixed budget leaves room. This is feasibility of a conservative certificate, not a hardware impossibility theorem. A fixed-amplitude mismatch bound cannot be optimized away by slowing hopping. Neutral memory noise accrues during ALL pulse/contact/gate time.

The output measurement/reset is CPTP, so(9) bounds any outcome probability change by epsilon_inst and the[0,4]-valued risk change by4epsilon_inst. This completes a coherent demand-to-instrument calculation under one declared alphabet, while preserving the real missing resources.

## Verification and remaining physical problem

Universal results use the written commutator, phase-estimation, threshold, interaction-frame and norm proofs. The probe checks reversible logic exhaustively at finite q, algebraic Fourier copy phases with the exact matched-contact commutation proof, all fixed-shell basis columns of the physical JC propagator with all dressed branches and nonzero gaps, actual changed coupling/tone/clock faults, and the finite POVM/reset/risk identities. The finite JC propagator controls use Q=N with all its dressed branches; the full Q<=N direct-sum estimate rests on the written predecessor proof. The mismatched contact is simulated during parking, while the exact copy uses the matched commutation identity. Finite60-digit controls are not interval or proof-assistant certificates. Known-state synthesis and generic quantum phase estimation are established techniques; no novelty is asserted for them. [Vogel, Akulin and Schleich](https://doi.org/10.1103/PhysRevLett.71.1816) is the held JC state-control comparator, not evidence for the new coupling's hardware availability.

Next derive or characterize matched photon/mediator neutral contacts and adjacent entangling gates for ONE device together with loss, reference protection, clock, pure-register supply and reset costs. If those inputs satisfy(9)-(10), evaluate that physical feasibility; if not, identify the actual limiting term or alternative alphabet. Native quantization, a physical observed state/domain and a GU action bridge remain separate. Repeating abstract controllability or this conditional compiler would not supply those inputs.
