---
title: "K1905: A causal finite-memory realization with explicit controls and energy"
status: active_research
doc_type: exploration
created: "2026-10-21"
classification: INTERNAL_STRUCTURAL_ONLY
target_claim: NONE-NOT-A-KILL
claim_ceiling: supplied finite quantum and controlled-environment mathematics; no native GU or continuum bath identification
scripts:
  - tests/channel-swings/k1905_causal_quantum_memory_realization.py
  - tests/channel-swings/k1905_causal_quantum_memory_realization_probe.py
---

# K1905: A causal finite-memory realization with explicit controls and energy

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
result: smooth ordered occupation-controlled Pauli gates with memory transport
carrier: four-mode fermionic Fock space tensor one memory qubit LAYER=toy CHIRALITY=N/A
pairing: positive complex Hilbert inner product and state expectation ON=conditional_target
real_structure: complex conjugation and CAR star; no native K/C identification
grading: finite occupation sectors and even fermion parity
action_owner: repository-construction -- supplied finite interactions or quantum channels
target: conditional coherence, causal implementation and memory demands MAP-TYPE=intertwiner
```

## Construction and consuming question

K1904 excludes a single commuting local bath layer for K1903's target.
Construct a different, explicitly ordered finite system: four fermion modes,
a memory qubit initially |0>, and sequential visits to sites2,3,4. Mode1
requires no gate. The positive Hilbert/CAR algebra, memory, preparation,
transport schedule and controls are supplied, not derived from GU.

Use the same branch unitaries as K1903, but now specify their generators:

    U1=I,
    U2=X=exp[-i G2],                G2=pi(I-X)/2,
    U3=(I-iY)/sqrt2=exp[-i G3],    G3=pi Y/4,
    U4=(I-iX)/sqrt2=exp[-i G4],    G4=pi X/4.                  (1)

For each visit choose a nonnegative smooth pulse f_j(t), compactly supported
in its visit interval, with integral1. Let

    H_j(t)=f_j(t) n_j tensor G_j.                              (2)

Supports are ordered and disjoint. These are bounded self-adjoint operators
on the full32-dimensional Fock-memory Hilbert space; no domain extension is
needed. Every H_j preserves all mode occupations and fermion parity. Its
integrated gate is

    W_j=(1-n_j) tensor I+n_j tensor U_j,
    W=W4 W3 W2.                                               (3)

On a general occupation string n, the bath branch is
U4^(n4) U3^(n3) U2^(n2). This fixes the whole-Fock extension rather than
silently extending the one-particle operation by identity. On the one-particle
sector only one U_j acts, hence the bath vectors are conjugate(v_j) from
K1903. The reduced coefficient is
<conjugate(v_k),conjugate(v_j)>=C_jk. Thus this actual bounded generator
implements the entire target exactly, including the zero12 entry and the
nonclassical phase witness, without a limiting construction.

## Causality is an explicit circuit assumption

Each gate is local to the mode and the memory while they are co-located.
The memory travels between the visits. If positions are x2,x3,x4 and its
allowed speed is v, schedule gaps at least |x3-x2|/v and |x4-x3|/v.
For visit durations tau_j, the elapsed gate-and-travel window obeys

    T >= tau2+tau3+tau4+(|x3-x2|+|x4-x3|)/v.                 (4)

Readout and mode recombination occur in the common future. This is a causal
quantum circuit with a supplied transport channel, not a continuum PDE proof,
a Lorentz-invariant Hamiltonian, or an assertion that arbitrary nonlocal
projectors are local densities. There is no backwards signal: a later
trace-preserving operation on memory plus later sites cannot change the
reduced state of an earlier site whose interaction has ended. Forward
communication is allowed and is the resource missing from K1904's model.
The finite-dimensional gate norm does not prove a physical propagation speed;
the speed and spatial implementation are explicit assumptions of the circuit.

## Control budget and a specified energy interface

The operator norms of G2,G3,G4 are pi,pi/4,pi/4, so this particular protocol
has integrated interaction norm3pi/2. If ||H_j(t)||<=M, then
M tau_j>=||G_j||. Smooth compact pulses attain arbitrarily close to this
bound from above; strict slack M tau_j>||G_j|| suffices by a smoothed almost
constant positive pulse. This is a resource certificate for(1), not a global
optimal-control theorem over all dilations or available compensating phases.
A common clock profile on the visits leaves the exact final channel unchanged.

Choose a physical memory energy H_E=omega |1><1|, omega>=0, and system
energy H_S=sum_j e_j n_j. Implement(2) in the interaction picture of H_E,
i.e. use exp(-i H_E t) G_j exp(i H_E t) in the laboratory control.
The controls have the same norm. All n_j, and hence H_S, are conserved.
For a one-particle input with populations p_j, the final memory energy is

    E_E=omega [p2+(p3+p4)/2],   0<=E_E<=omega.              (5)

For equal populations it is omega/2. Free memory evolution after the gates
is common to every branch and leaves C unchanged. If the interaction
vanishes at the endpoints and the full finite system is closed apart from
these prescribed time-dependent controls, the mean work supplied by the
controls equals the endpoint total energy change, here(5). This is the
finite Hamiltonian definition integral Tr(rho dH/dt); it does not include
transport, preparation, resetting, apparatus or any continuum sea energy.
Taking omega=0 gives a degenerate memory energy without eliminating those
unpriced resources. Finite memory energy is not K1897's field-energy theorem.

## Released error budget and experiment

Duhamel's estimate bounds each gate-unitary error by the integral of the
Hamiltonian perturbation norm. If those errors are e2,e3,e4, telescoping the
whole ordered product gives ||W_actual-W||<=E=sum e_j. For an identical
initial bath state, trace-norm error of the output on any input (including
an ancillary reference) is at most2E. The H witness on the equal input
therefore changes by at most2(4+sqrt2)E. The strict sufficient condition

    E < (6-4sqrt2)/[8(4+sqrt2)]                              (6)

keeps the observed output below the classical threshold delta/4. This is a
conservative gate error budget, not the exact distance to the classical set.
It releases a specified finite test of quantum memory with locality, timing,
energy and error assumptions on the same construction. It does not recover a
microscopic GU bath. K1906 tests why its exact endpoint is incompatible with
continuous CP-divisible dephasing, independently of finite memory recurrence.

## Source ceiling and validation

SC-OP-04 ASSERTS candidate four-field operator grammar; SC-MAS-01 and
SC-CHI-02 ASSERT a stylized curvature-mass toy; SC-META-53 remains UNCERTAIN.
These supplied positive-Hilbert constructions identify none of their missing
native full20 injection, separate K/C forms, accessibility or physical state.
LT-SM8, LT-GR6b and AC-F1, source polarities, physics-ledger and canon verdicts
remain unchanged. The result has independent quantum-mathematical scope.
No novelty, external expert acceptance, formal proof, continuum field energy,
microscopic bath selection, GU prediction or GU falsification is claimed.

The analytic proof carries general statements. Exact producer controls and a
separate probe rederive finite matrices, partial traces, generator identities
and bounds. Mathematical input faults are tested after a passing baseline;
report and dependency-pin faults are counted separately. Inline hostile review
checks the strongest overclaim, a contrary construction and the weakest
transfer/reproducibility seam. A finite control does not establish the general
spectral, tensor-factorization or continuity argument by itself.
