---
title: "K2267 A routed nearest-neighbor compiler for the full detector"
status: active_research
doc_type: exploration
created: "2026-10-29"
classification: INTERNAL_STRUCTURAL_ONLY
target_claim: NONE-NOT-A-KILL
claim_ceiling: conditional supplied model only; no source or canonical verdict
scripts:
  - tests/channel-swings/k2267_nearest_neighbor_detector_probe.py
---

# K2267 A routed nearest-neighbor compiler for the full detector

> **GU-COMPARATOR-ROUTING — scope before inference.** This artifact contains or borders a conventional particle-physics comparator. Any result about a standard Higgs/VEV, ordinary family index or net chirality, SO(10) `126` Majorana mechanism, anomaly selector, VEV-only breaking or familiar vector-mass route binds only that named model. It is not evidence for or against Weinstein's source-native mechanism without an explicit typed bridge. Read `lab/methods/source-native-comparator-routing.md` and follow its source-native pointers before reusing this result.

Classification: `INTERNAL_STRUCTURAL_ONLY`.

```gu-typed-objects
result: K2267 A routed nearest-neighbor compiler for the full detector
carrier: common-cap charged oscillators on a finite path and one neutral workspace at its end LAYER=toy CHIRALITY=N/A
pairing: positive tensor Hilbert inner product, operator norm and half trace distance ON=declared_carrier
real_structure: complex conjugation and Hilbert adjoint
grading: occupation and neutral record labels; no native chirality transported
action_owner: repository-construction -- supplied conditional model
target: finite-range control construction with full-instrument resource and error bounds MAP-TYPE=intertwiner
```

## Result and exact change of assumptions

[K2264](k2264-restricted-detector-control-2026-10-29.md) required all-pair number nonlinearities. On a supplied finite charged path, its finite shell synthesis can instead be constructed from onsite terms, adjacent hopping and adjacent number products, with neutral controls at one endpoint. Routing restores labels and external-reference correlations after each simulated interaction. This is spatial nearest-neighbor locality on the DECLARED finite graph, with huge hard walls, phase stock, neutral memory and external timing still supplied.

There is a material resource change: enlarge every charged local cap to a common K that bounds the entire compared total-charge carrier. Do not apply a truncated beam splitter as a SWAP on the whole cutoff tensor cube, and do not reuse the old unequal-cap compiler pulse list after changing its matrices. Reconstruct the compiler on the new invariant total-charge simplex.

This conditional apparatus result supplies no native GU action, physical quotient or cosmological prediction. Source/canon/ledger0.263 and SC-META-53 UNCERTAIN are unchanged.

## 1. The actual invariant carrier and local alphabet

Let N charged registers occupy a path 1,...,N, with common cap K>=1. Put a neutral workspace of dimension a>=2 at endpoint1. The comparison space is

    H_K = span{|n1,...,nN,l>: sum n_i<=K},
    d=a binomial(K+N,N).                         (1)

Each local ladder/occupation is its finite block on levels0,...,K, extended by zero on higher Fock levels; tensor identities on spectators remain. This is a local bounded extension. Each generator conserves physical total number, and H_K is reducing. It is a simplex inside the larger tensor box, not an all-sites projector inserted into every generator.

Allowed signed, independently timed controls:

- onsite N_i,N_i²;
- adjacent N_iN_(i+1) and X_i=a_i†a_(i+1)+a_(i+1)†a_i;
- neutral projectors P_l and neighbor flips Y_l at the endpoint;
- endpoint N_1 P_l only.

No remote primitive interaction or arbitrary shell projector is assumed. Number is conserved; unequal-frequency physical energy conservation is not asserted. The neutral workspace is one onsite high-dimensional subsystem, so this does not bound local Hilbert dimension or claim a few-qubit hardware realization.

## 2. Exact adjacent SWAP and its boundary

On H_K the local pair occupancy is <=K. The entire pair charge shell is present, so truncated hopping agrees there with ordinary two-mode hopping. In each such shell,

    S_i=exp(+i pi(N_i+N_(i+1))/2) exp(-i pi X_i/2) (2)

sends |p,q> to |q,p> exactly. The hopping sends creation operators to -i times the exchanged creation operators; the two onsite phases cancel (-i)^(p+q). Three permitted primitive pulses implement S_i, including identity on arbitrary spectators and external references. No phase is silently discarded.

The claim fails on the full cap-K tensor cube: at K=1, |1,1> is hopping-blocked, but the number phase is -1, whereas SWAP fixes |1,1>. This is why a common TOTAL charge bound is essential. It is not merely a notation change.

Move mode i to j-1 using j-i-1 adjacent swaps, apply the adjacent diagonal N_(j-1)N_j pulse, then undo all swaps. This realizes the desired remote N_iN_j interaction with <=2N-4 swaps. Moving any mode to site1 similarly realizes N_iP_l with <=2N-2 swaps. Therefore every virtual feature pulse costs at most

    L_route=6N-5                               (3)

local primitive pulses; local/neutral-only features cost one. Every route is uncomputed before the next feature, so spectator states and labels return exactly. Arbitrary intermediate entanglement is allowed. This replaces a missing spectral-separation premise by actual interaction synthesis, rather than claiming nearest-neighbor diagonal gaps alone distinguish spectators.

## 3. Rebuild, rather than transplant, the compiler

Take the SAME desired old K2253/K2264 shell isometry and complete it to determinant-one unitaries using spare neutral directions. If its old charged caps are c_i, choose K=sum c_i. The old tensor box lies in H_K. On each shell embed the completed old unitary as U_old direct-sum identity on the extra states. Its determinant remains one and its prescribed field+record action is unchanged. This embeds the target, not the old pulse sequence: the old hardwall hopping differs from the new hopping near the old individual caps.

Reapply K2264's argument on H_K. Its diagonal features N_i,N_i²,N_iN_j,P_l,N_iP_l still separate every directed primitive edge: restricting a separating list to a subset preserves uniqueness. Each fixed-charge simplex graph is connected by adjacent hopping (move all quanta toward site1); neutral flips connect labels. Edge coefficients are >=1 and ||X_i||<=2K is a safe bound. With

    F_count=2N+N(N-1)/2+a+Na,
    C=K², base=4C+1,
    D0=sum base^k f_k, Lambda=max_HK D0,
    M=2Lambda+1,

all directed gaps remain distinct modulo M. K2264's exact Fourier edge isolation and unitary product-formula bound therefore apply to these NEW matrices. D0 factors into commuting feature pulses; route each factor by (3). A Fourier summand costs at most 2F_count L_route+1 local pulses instead of 2F_count+1. The sum may use astronomical integers; finiteness does not imply feasibility.

Let J<=100 d³ bound the edge rotations for all relevant shell completions, and allocate total operator error zeta. Taking edge angles <=2pi,

    repeats=ceil(64(22/7)² K² J/zeta),
    P_local <= J repeats M (2F_count L_route+1). (4)

The construction is entirely finite and gives error<=zeta on H_K. Using all independent shell phases would require more than SU; determinant adjustment on unprescribed neutral directions is retained explicitly. No enormous matrix or full pulse list has been built by the finite probe.

## 4. Time, drift, precision and the actual detector

Use the signed C1 pulses of K2264. For a primitive A of integrated angle theta, any positive peak J0 and slew S0 are met with duration

    T>=max(2|theta| ||A||/J0,
           sqrt(2pi|theta| ||A||/S0)).            (5)

For each adjacent swap use three pulses of |theta|=pi/2; ||X_i||<=2K and ||N_i||<=K, so three pulses each of duration

    T_swap_pulse=max(2pi K/J0, 2pi sqrt(K/S0))

suffice. Total duration is the sum over the explicit local list, with at most P_local terms; giant diagonal angles and routing costs must be retained. A common drift omega N_total contributes a known rotation over this duration, corrected by local number phases or retained in an explicit rotating-frame comparison. Nonuniform uncontrolled drift is outside this proof. A small integrated Hamiltonian perturbation contributes its norm integral; no imaginary perfect-control tolerance is hidden.

For K2253's two field modes and one battery, old caps are R,R,H, hence N=3 and

    K=2R+H=100015567999991,
    a=256000016000002,
    d=a binomial(K+3,3), F_count=9+4a,
    L_route=13.                                 (6)

This enlarges each local hardwall, including battery capacity, to K. The initialized coherent packet remains the SAME supplied packet; capacity is not occupied or mean charge. Each ideal-prefix comparison insertion has its independent ideal reference and truncated low-input component inside the simplex. Actual intermediate batteries after approximate calls need not stay inside that comparison simplex; the local block extensions define channels everywhere and subsequent physical suffixes contract trace distance. General field inputs use K2253's existing tail estimate at each insertion, not a uniform full-Fock norm bound. Released outputs/spent reservoirs are not routed back into the controller; routing uses only the current controlled registers.

If old base per-call error is e(B0;Q,R,L), the complete adaptive field+record+reference comparison satisfies

    error_calls <= calls*e + sum zeta_j
                             + sum integral ||Delta H_j||dt. (7)

Contractivity and telescoping give this for arbitrary external history; controllers still cannot access the retained battery. The new compiler approximates the exact same target on the relevant embedded inputs, so no new ideal input-tail penalty is needed. For the prior ten-call example, base error<.00914, total compilation.0001 and total perturbation.0001 give error<.00934. Initial joint preparation error adds once. A coherent stock preparation/transport/renewal mechanism is still missing; number-invariant donors and conserving controls cannot create it.

## 5. Meaningful controls and remaining endpoint

The finite probe checks exact charge-one and charge-two beam-splitter matrices, the cap2 charge-three occupation failure, number-phase omission, actual three-site permutation conjugation of remote diagonal/neutral operators, shell graph connectivity and gap separation, the explicit enlarged resource numbers and exact full-channel budget. These controls supplement the universal shell/graph/unitary proof, not an empirical apparatus certification.

This closes finite-range existence for a supplied nearest-neighbor graph AFTER paying for enlarged hard walls and a reconstructed compiler. It does not show that merely replacing the old all-pair diagonal Hamiltonian by nearest-neighbor terms preserves its frequency discrimination. It does not establish efficient synthesis, bounded local workspace dimension, untruncated leakage control, autonomous scheduling, phase-stock creation or source physicalization. The next useful apparatus endpoint is a bounded-resource or ordinary-untruncated implementation with measured/derived leakage and coherent supply, not another abstract controllability restatement. Independent internal review is distinct from external experts, Lean and remote CI. Run the listed probe; --write regenerates the hash-bound report.
