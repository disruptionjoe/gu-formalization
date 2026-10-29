---
title: "K2270 Conserved charge removes the detector hardwalls"
status: active_research
doc_type: exploration
created: "2026-10-29"
classification: INTERNAL_STRUCTURAL_ONLY
target_claim: NONE-NOT-A-KILL
claim_ceiling: conditional supplied model only; no source or canonical verdict
scripts:
  - tests/channel-swings/k2270_untruncated_detector_control_probe.py
---

# K2270 Conserved charge removes the detector hardwalls

> **GU-COMPARATOR-ROUTING — scope before inference.** This artifact contains or borders a conventional particle-physics comparator. Any result about a standard Higgs/VEV, ordinary family index or net chirality, SO(10) `126` Majorana mechanism, anomaly selector, VEV-only breaking or familiar vector-mass route binds only that named model. It is not evidence for or against Weinstein's source-native mechanism without an explicit typed bridge. Read `lab/methods/source-native-comparator-routing.md` and follow its source-native pointers before reusing this result.

Classification: `INTERNAL_STRUCTURAL_ONLY`.

```gu-typed-objects
result: K2270 Conserved charge removes the detector hardwalls
carrier: finite-mode ordinary bosonic Fock space with finite neutral workspace LAYER=toy CHIRALITY=N/A
pairing: positive complex Hilbert inner product and operator norm ON=declared_carrier
real_structure: complex conjugation and Hilbert adjoint
grading: no native chirality or Clifford grading transported
action_owner: repository-construction -- supplied conditional model
target: full-instrument synthesis and projected leakage under untruncated conserving controls MAP-TYPE=intertwiner
```

## Result and scope

The detector construction in [K2267](k2267-nearest-neighbor-detector-2026-10-29.md) can use ordinary untruncated bosonic ladders. Finite total-charge subspaces are exactly invariant, so its finite compiler can be reconstructed there with ZERO ideal leakage. The global dynamics exists through selfadjoint direct sums of finite charge blocks. A projected Duhamel estimate then supplies an honest perturbation/leakage budget without assuming the perturbation is bounded on all Fock space.

This removes the supplied local hardwalls; it does not make the apparatus affordable, autonomous, positive-energy under arbitrary signed controls, or source-owned. Coherent stock, nonlinear interactions, a huge finite neutral workspace and external timing remain supplied. SC-META-53 remains UNCERTAIN; ledger0.263/native physical-quotient claims are unchanged. Ordinary positive Fock space here is a conditional apparatus, not a solution of GU's interacting state-space problem.

## 1. Genuine full-Fock primitives and domains

For N finite charged modes on a path and a finite neutral space C^a, use the usual Fock space with number operators n_i and untruncated ladders a_i,a_i^dagger. Allowed real signed controls are

    n_i, n_i², n_i n_(i+1),
    X_i=a_i^dagger a_(i+1)+a_(i+1)^dagger a_i,
    neutral P_l,Y_l and endpoint n_1 P_l.        (1)

Every generator preserves total number Ntot=sum n_i. The eigenspace H_n has finite dimension a binomial(n+N-1,N-1). A real linear combination on the finite-particle core restricts to a finite Hermitian matrix A_n on each H_n. Its canonical closure is

    A=direct_sum A_n,
    D(A)={psi: sum ||A_n psi_n||²<infinity}.     (2)

This operator is selfadjoint: (A±i)^-1 is the direct sum of finite resolvents, uniformly bounded by1 and onto D(A). Cutting a vector off in total number converges in the graph norm, proving that the algebraic finite-particle sum is a core. This proof does not require a lower spectral bound. In particular a negative n_i² pulse is selfadjoint but unbounded below.

For the finite sequential pulse list, integrated-angle unitaries exp(-i theta A) are globally defined and strongly continuous. Smooth scalar pulse envelopes generate them exactly. More general time-varying finite combinations with integrable real coefficient functions can be solved block by block; this construction supplies strong unitary evolution, but no common differentiability domain for all full-Fock states is inferred. Number probabilities and a finite mean number are conserved under the ideal controls.

## 2. Exact global routing, finite-sector compilation

The phase-corrected two-mode beam splitter

    S_i=exp(+i pi(n_i+n_(i+1))/2) exp(-i pi X_i/2)

is an exact SWAP on the ENTIRE ordinary Fock space: its creation-operator action gives (-i)^(p+q)|q,p>, canceled by the number phase. K2267's cube-cutoff counterexample no longer applies because |K+1> has not been removed. For example charge3 hopping starting at |2,1> includes |3,0> and |0,3>. This is not an approximation by a larger local cutoff.

Exact adjacent SWAP conjugation synthesizes remote n_i n_j and n_i P_l, restoring mode labels and spectators. K2267's routing count L_route=6N-5 remains a safe bound. Global routing is exact; the subsequent Fourier edge selector is ONLY a statement on

    H_<=K=direct_sum_(n=0)^K H_n,
    d=a binomial(K+N,N).                        (3)

This subspace reduces all genuine generators. Their restrictions coincide with the common-cap K matrices on this SIMPLEX, so reapply K2267's reconstructed compiler to the embedded target, never transplant the old unequal-cap pulse list. Feature-gap separation, shell graph connectivity, determinant adjustment on spare neutral directions and product-formula estimates are unchanged on (3). Higher-sector Fourier aliases do not affect (3); no global edge isolation or uniform full-Fock approximation is claimed.

The finite comparison parameters and neutral-memory size remain: K=2R+H=100015567999991 for the comparison inputs, a=256000016000002, N=3, L_route=13 and the enormous finite gate list from K2267. K is now a total-number comparison threshold, NOT a physical local hardwall. The initialized coherent packet is unchanged. The charged Hilbert spaces now have infinite dimension; finite comparison charge is not finite hardware capacity. A known common drift omega Ntot is retained in an explicit rotating-frame comparison or corrected by supplied onsite number phases, as in K2267; uncontrolled nonuniform drift requires its own perturbation analysis. This is an actual change in the declared dynamics, with the same desired low-sector instrument and error, not a claim of cheaper synthesis.

## 3. Projected perturbations and leakage

Let U(t,s) be the ideal conserving propagator, P=P_<=K and U~ the actual propagator. Assume a valid variation-of-constants identity on finite-particle vectors: for example those vectors lie in the actual generator domains, U~ solves the indicated perturbed evolution there, and measurable DeltaH(t)P has integrable norm. Existence of an arbitrary unitary U~ alone is insufficient. With

    eta=integral_0^T ||DeltaH(t)P|| dt,

Duhamel on the ideal finite-dimensional orbit gives

    (U~(T,0)-U(T,0))P
      =-i integral U~(T,t)DeltaH(t)U(t,0)P dt,
    ||(U~-U)P||<=eta,
    ||(1-P)U~P||<=eta.                          (4)

The norm here includes OUTGOING transitions: ||P DeltaH P|| alone is insufficient. Leakage probability on any low-supported density matrix is at most min(1,eta²). The channel half trace-distance error, with arbitrary external reference, is at most min(1,eta). These conclusions use Stinespring/isometry norm control; they are not a bound on leaked mean energy.

For a concrete bounded rank-two perturbation DeltaH=epsilon(|M><0|+|0><M|), M>K, ideal identity, the low input vacuum evolves to cos(epsilon T)|0>-i sin(epsilon T)|M>. Its leakage probability is sin²(epsilon T)<=epsilon²T² and mean number is M sin²(epsilon T), arbitrarily large at fixed epsilon,T. Thus arbitrarily small channel leakage does not imply small mean-energy leakage. This also shows why only P DeltaH P would miss the effect entirely.

## 4. Complete adaptive detector composition and energy limits

Reuse K2253's ideal-prefix comparison, with the same supplied coherent state and input mean-number bound. At each insertion the truncated ideal component is supported in (3); the discarded ideal input tail is already priced in its base per-call error e. Subsequent actual channels contract trace distance, even if the actual battery is outside (3). Controller isolation and retained external histories remain exactly as in K2267. Therefore

    full_calls_error <= calls*e + sum zeta_j + sum eta_j,

where zeta_j is low-sector compilation error and eta_j the projected bound (4). Initial joint preparation error adds once. Ten calls retain the previous base<.00914, compilation total.0001 and perturbation total.0001, giving error<.00934. This is a complete field+record+reference comparison, not just output probabilities or independent marginals. No new tail penalty is added merely for removing walls, since ideal low-sector invariance is exact. No global diamond norm claim for unrestricted input energy follows.

On H_<=K, ||n_i||<=K, ||n_i²||<=K², ||n_i n_j||<=floor(K²/4), ||X_i||<=K and neutral norms<=1. The signed C1 pulse timing/precision bounds apply with these supported norms. They are NOT global full-Fock peak-power or slew bounds: n_i² is unbounded, and an input with finite first moment may have infinite second moment. For example p_n=1/[n(n+1)(n+2)] for n>=1, with remaining probability at0, has finite mean but divergent second moment. Its Kerr unitary is defined spectrally, but finite Kerr Hamiltonian expectation/variance is not supplied. A demand for finite control-energy moments requires additional hypotheses.

The old finite-battery restoration lower bound using ||N_battery||<=H cannot be imported as a global statement now that the battery is untruncated. It remains valid only under its original actual bounded-output/charge assumptions. Small trace distance alone cannot control an unbounded charge observable, as (4)'s counterexample shows. Source asymmetry and finite-stock results keep their own hypotheses; no general no-catalysis or perpetual-service conclusion is introduced.

## Verification and next independent input

The probe uses COMPLETE finite total-number shells of genuine bosons, checks exact charge3 routing, charge conservation, no off-sector matrix elements, phase and matrix-element faults, a projected outgoing perturbation, and exact channel/resource arithmetic. Finite shell checks supplement the written direct-sum, routing, compilation and Duhamel proofs. Independent internal specialist review is not external-expert, proof-assistant, hardware or remote-CI certification.

Number-sector block decomposition is established Bose-Hubbard methodology; see the explicit direct-sum discussion in [Symmetry-Enhanced Lieb–Robinson Bounds for a Class of Bose–Hubbard Type Hamiltonians](https://link.springer.com/article/10.1007/s00023-026-01733-9). We use the elementary finite-mode proof above, not that paper's propagation conclusions.

The next substantive apparatus question is a fixed physically supplied coherent-stock/control model with uniform energy moments or an affordable restricted synthesis. Repeating abstract finite controllability or asserting a global norm from these sector bounds cannot answer it. The mathematical construction has removed hardwalls while exposing, rather than resolving, its energetic and preparation costs.
