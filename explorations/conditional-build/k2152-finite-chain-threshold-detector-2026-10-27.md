---
title: "K2152: A finite-chain threshold instrument with conditional resources"
status: active_research
doc_type: exploration
created: "2026-10-27"
classification: INTERNAL_STRUCTURAL_ONLY
target_claim: NONE-NOT-A-KILL
claim_ceiling: conditional internal mathematics; no full raw rigidity, continuum apparatus or GU recovery
scripts:
  - tests/channel-swings/k2152_finite_chain_threshold_detector_probe.py
---

# K2152: A finite-chain threshold instrument with conditional resources

> **GU-COMPARATOR-ROUTING — scope before inference.** This artifact contains or
> borders a conventional particle-physics comparator. Any result about a
> standard Higgs/VEV, ordinary family index or net chirality, SO(10) `126`
> Majorana mechanism, anomaly selector, VEV-only breaking or familiar vector-
> mass route binds only that named model. It is not evidence for or against
> Weinstein's source-native mechanism without an explicit typed bridge. Read
> `lab/methods/source-native-comparator-routing.md` and follow its source-native
> pointers before reusing this result.

Classification: `INTERNAL_STRUCTURAL_ONLY`.

```gu-typed-objects
result: K2152: A finite-chain threshold instrument with conditional resources
carrier: M-site oscillator Fock space and independent qubit record LAYER=toy CHIRALITY=N/A
pairing: positive H_W ground-state form and site-number quadratic form ON=declared_carrier
real_structure: real coordinates or complex Hilbert adjoint as declared
grading: supplied oscillator number threshold
action_owner: repository-construction -- supplied conditional objects below
target: complete recorded threshold instrument, duration and field-energy bounds MAP-TYPE=intertwiner
```

## 1. Reuse the funnel, supply the missing finite-model resources

[K2145](k2145-parity-causal-duration-2026-10-27.md) already constructs adjacent
Givens gather, endpoint parity and inverse on a finite chain. We REUSE that
construction, replacing parity with [K2151](k2151-optimal-local-mode-discrimination-2026-10-27.md)'s
optimal count threshold and adding conditional durations and field-energy form
bounds. This is a finite number of sites, with INFINITE oscillator Hilbert spaces;
no occupation cutoff or truncated CCR is assumed in the theorem.

Let q,p be M real canonical pairs, W=W^T real symmetric positive definite with eigenvalues between
w_min>0 and w_max, and physical free Hamiltonian

    H_W=(p^T p+q^T W² q)/2-Z, Z=tr(W)/2.

Freeze real unit f, common site scale nu>0, site annihilators
c_j=(sqrt(nu)q_j+i p_j/sqrt(nu))/sqrt2, N_nu=sum c_j†c_j and b_f=sum f_j c_j.
For the K2151 vacuum/signal use a_j=f^T W^j f and nu=sqrt(a_1/a_-1).
Other positive nu realizes the corresponding oscillator effect but not that
thermal diagonalization automatically.

Assume externally supplied controllable adjacent beam splitters, onsite threshold
coupling, independent prepared qubit, and compensation of free drift throughout
the control sequence. This last premise means the effective total Hamiltonian
is exactly the stated control Hamiltonian; the interaction-picture label alone
cannot make an uncompensated physical drift disappear. Preparation, compensation,
readout, reset and switching costs are not supplied or bounded here.

## 2. Exact complete instrument and conditional duration

Eliminate f from the far end toward site1 using at most M-1 adjacent real rotations.
Angles in[-pi/2,pi/2] suffice to send f to ±e1; the endpoint sign is irrelevant
for number. Let B be the Fock implementation, with B† n1 B=b_f†b_f. Beam-splitter
Hamiltonians i g(c_j†c_(j+1)-c_(j+1)†c_j), with either sign and fixed available
g>0, implement each angle in time |theta|/g. They are selfadjoint number-conserving
operators. The full Fock generator is UNBOUNDED; g bounds its one-particle coupling,
not its full operator norm.

Define P_k(n)=1_[k,infinity)(n), with integer k>=1. At the endpoint couple the record by H_c=λ P_k(n1) tensor X, λ>0, for
τ=pi/(2λ). Its unitary is (I-P_k)tensor I-i P_k tensor X. Prepare |0>, apply B,
this coupling, and B†, then read the complete binary record. Kraus operators are

    K0=I-P_k(b_f†b_f), K1=-i P_k(b_f†b_f).                     (1)

Thus the full cq instrument, including arbitrary entangled references and all
field excitations, is EXACTLY the supplied Lüders threshold instrument. Outcome
phase has no effect on its cq channel. The endpoint projector is a supplied bounded
non-Gaussian control on all occupations; it is not derived from linear optics.

The explicit conditional duration obeys

    T <= pi(M-1)/g + pi/(2λ),                                 (2)

including gather and undo; classical readout/reset time is outside(2). Gate count
is at most2(M-1)+1. Circuit support can advance at most one graph edge per adjacent
gate layer. This is NOT an exact continuous-time velocity cone: a two-site gate
spreads support across its edge at every positive duration. No claim of speed g,
relativistic causality, continuum limit or optimal duration follows.

## 3. Unconditional field-energy budget at every stage

Each control commutes with N_nu. The endpoint controlled projection does so too,
and its record measurement preserves expected N_nu. Define

    C=max(1/nu, nu/w_min²), D=max(nu,w_max²/nu).

Positive quadratic-form ordering gives

    N_nu+M/2 <= C(H_W+Z), H_W+Z <= D(N_nu+M/2).               (3)

These hold on the common oscillator form domain, and extend to all finite-energy
states by closure. Since the actual effective controls preserve N_nu, every
intermediate reduced field state and the unread final output obey

    E_t <= DC(E_in+Z)-Z.                                     (4)

This remains true with arbitrary reference entanglement. It is an unconditional
mean FREE FIELD energy bound, not full controller work, Hamiltonian norm or a
uniform conditional branch bound. For a branch of probability p>0, the bound is E_branch<=
[DC(E_in+Z)-Z]/p; saturation is not asserted. Even the physical vacuum has

    <N_nu>_Omega=tr(W/nu+nu W^-1-2I)/4,                       (5)

so passive site-mode gates need not be passive for H_W and need not preserve
its entangled ground state. For vacuum inputs the sharper direct estimate is
E_t<=D(<N_nu>_Omega+M/2)-Z. Equations(3)--(5) retain zero-point shifts; omitting
Z falsely predicts zero output energy for every vacuum input.

## 4. What this settles and what survives

This gives an exact finite-chain implementation of K2151's discriminator with
specified gate strength assumptions, all-record output and finite unconditional
field-energy control. It advances K2145's previously unpriced finite-chain control;
it does not claim construction of a continuum local counter, a fixed physical
signal preparation, an autonomous controller or total work budget. The constants
can diverge with regulator, frequency range and M; no cutoff-independent passage
is proved. K2108's separating-vacuum obstruction and K2145's continuum causal
necessity survive. Finite-chain modes and their vacuum restrictions are the exact
objects here, not replacements for a relativistic local net.

The adjacent exact probe independently checks an adjacent gather on real unit f,
its induced two-particle representation, threshold Kraus maps on the invariant
total-number<=2 sector, a reference-entangled recorded output, and the energy
quadratic forms with a non-diagonal W. Restriction is a finite control, not the
basis of the all-Fock theorem. Changing gather order/sign, dropping undo,
replacing threshold by parity, or dropping zero-point terms must fail actual checks.

## Evidence and inference boundary

The proofs and finite exact controls are separate evidence kinds. Independent internal
specialists review the actual statements and probe seams. No external certification,
proof assistant, novelty or GU recovery is claimed. SC-OP-04 ASSERTS candidate
four-field grammar; SC-OP-05 and SC-META-53 remain UNCERTAIN; SC-META-56 DISAVOWS
requiring an odd action as a prerequisite. LT-SM8/LT-GR6b, ledger0.263, source
register and canon are unchanged. The scalar positive Hilbert model is imported;
it is not the source-selected GU quotient, fermionic grading or observed2+1.
