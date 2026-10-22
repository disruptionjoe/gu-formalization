---
title: "K1933: Energy coherence is unnecessary for this covariant minimax task"
status: active_research
doc_type: exploration
created: "2026-10-22"
classification: INTERNAL_STRUCTURAL_ONLY
target_claim: NONE-NOT-A-KILL
claim_ceiling: supplied finite quantum models; analytic proof with internal controls, no native GU or novelty claim
scripts:
  - tests/channel-swings/k1933_covariant_catalyst_dephasing_reduction.py
  - tests/channel-swings/k1933_covariant_catalyst_dephasing_reduction_probe.py
---

# K1933: Energy coherence is unnecessary for this covariant minimax task

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
result: preparation pinching preserves or improves covariant channel error and uniform return
carrier: finite positive Hilbert system, invariant bath and catalyst LAYER=toy CHIRALITY=N/A
pairing: trace norm and completely bounded trace norm ON=product_input
real_structure: complex adjoint and spectral energy pinching
grading: energy eigenspaces; no source chirality
action_owner: repository-construction -- fixed total-energy-conserving unitary
target: covariant channel and worst-case catalyst return MAP-TYPE=intertwiner
```

## 1. Exact statement

Let S,B,A be finite-dimensional, with fixed Hamiltonians and an initial
product state rho_S tensor tau_B tensor sigma_A. Require [tau_B,H_B]=0
and [U,H_S+H_B+H_A]=0. Write Phi_sigma for the S output channel,
Psi_sigma for the A output channel, and Lambda_sigma for the joint SA
output after tracing B. Let Phi be a FIXED time-translation-covariant target.
Set D(X,Y)=||X-Y||_1/2 and

    epsilon(sigma)=||Phi_sigma-Phi||_diamond/2,
    r(sigma)=sup_rho D(Psi_sigma(rho),sigma),
    delta(sigma)=||Lambda_sigma-[rho -> Phi(rho) tensor sigma]||_diamond/2.

Replace sigma by its energy pinching sigma_bar=sum_E P_E sigma P_E.
For the SAME U, bath, dimensions and Hamiltonians,

    epsilon(sigma_bar)<=epsilon(sigma),
    r(sigma_bar)<=r(sigma),    delta(sigma_bar)<=delta(sigma).       (1)

The completely bounded marginal-return distance from
rho -> Tr(rho)sigma obeys the same inequality. Thus any simultaneous
upper-bound feasibility problem for these errors, with a convex invariant
preparation constraint, has a block-diagonal solution whenever it has one.
For nondegenerate H_A, optimize over ordinary diagonal probabilities.
This is an optimization reduction, not permission to replace a prescribed
state, preserve its spectrum/purity, or erase coherence without accounting for
how an actual laboratory prepares the replacement.

## 2. Proof without replacing a physical output by a purifier

Write T_X(t)(a)=exp(-itH_X)a exp(itH_X), sigma_t=T_A(t)sigma.
Invariance of tau_B and exact conservation imply, for every operator rho,

    Phi_sigma_t(rho)=T_S(t) Phi_sigma(T_S(-t)rho),
    Psi_sigma_t(rho)=T_A(t) Psi_sigma(T_S(-t)rho),
    Lambda_sigma_t(rho)=(T_S(t) tensor T_A(t))
                         Lambda_sigma(T_S(-t)rho).                (2)

These identities follow by moving the product time unitary through U and
then taking the indicated physical partial trace. They do not assume global
controlled-U form or a diagonal system input. Reference systems are left
untouched, so the channel identities and norm invariance hold with arbitrary
entanglement.

Covariance of Phi makes epsilon(sigma_t)=epsilon(sigma). The supremum over
ALL input states makes r(sigma_t)=r(sigma). For the joint criterion, transform
Phi(rho) tensor sigma_t using covariance; delta is also constant on the orbit.
Every channel displayed is linear in sigma; the comparison channel for r or
delta is likewise linear in sigma. Convexity of trace/diamond norms therefore
bounds each error of every finite orbit average by the original error.
The Cesaro average of sigma_t converges to sigma_bar in finite dimensions:
off-diagonal blocks carry exp(-it(E-F)), whose average vanishes for E!=F.
Continuity yields (1). Irrational energy spacings need no finite period.
For degeneracy, coherences INSIDE an energy eigenspace survive.

This proof applies to any covariant channel, not only a Schur multiplier or
an extreme point. In particular the four-state target in
[K1932](k1932-four-level-bath-catalyst-return-2026-10-22.md) is covariant for
any diagonal H_S, so coherence is removed from its global optimization burden.
The remaining probability/support/unitary optimization is not thereby solved.

## 3. Resources and inherited constraints

Pinching preserves every diagonal energy probability, hence every energy
moment, mean energy, maximum occupied energy and support inside a fixed
spectral subspace. It leaves dimensions, bath and allowed U unchanged.
For finite positive-temperature tau_A, convexity and unitary invariance give

    D_relative(sigma_bar || tau_A) <= D_relative(sigma || tau_A).

Equivalently, energy stays fixed while entropy cannot decrease. A mean-energy,
bandwidth, Gibbs-relative-entropy or invariant convex preparation budget
therefore survives the reduction. Fixed eigenvalues, fixed purity, an exactly
specified coherent preparation or a nonconvex preparation family need not.
No cost-free implementation of the pinching operation is asserted: this is
an existence comparison between initial preparations.

The diamond PRODUCT criterion in (1) is stronger than marginal return.
Its reduction does not prove a product-return protocol exists whenever a
marginal-return protocol exists. Likewise it does not guarantee exact reuse
of a changed catalyst on a second invocation.

## 4. Controls and a necessary exception

For H_S=H_A=diag(0,1), trivial bath, U=CZ and sigma=|+><+|, the
system channel is exactly complete dephasing. Its worst catalyst disturbance
is1 (input |1> sends |+> to |->). Replacing sigma by I/2 gives the SAME
channel and zero catalyst disturbance. This target is nonextreme in the
relevant correlation set; it does not evade the extreme rank-two information
cost in K1925.

Covariance of the TARGET is essential. With U=SWAP and sigma=|+><+|,
the induced channel resets S to |+>. Pinching changes it to reset I/2;
the error from the original reset target goes from0 to1/2. That target is
not covariant. A state-conversion problem with one fixed asymmetric input
also lacks the all-input invariance used in (2). Correlated initial S/A
resources are outside the product-input hypothesis.

The producer checks a rational energy-shell rotation with coherent complex
sigma, all four matrix units, channel/return orbit identities and the
Cesaro finite-spectrum analogue. The separate probe reconstructs phase
selection and component contractions, including degenerate spectra.
Universal inequalities follow from the proof, not these finite controls.

## 5. Scope, prior work and reproduction

Time-translation covariance and energy modes are established background:
[Lostaglio et al.](https://arxiv.org/abs/1410.4572). Catalytic coherence and
fixed-state transformations can have different benefits; (1) does not
contradict them. [Ng et al.](https://arxiv.org/abs/1405.3039) treat catalyst
limitations and resource constraints. This note derives the particular joint
error/return preparation reduction directly; no general novelty claim.

Run the two frontmatter scripts with Python3/SymPy1.14.0; producer --write
refreshes its JSON. The probe verifies a green baseline before genuine
conservation/target faults and separately labels report/pin consistency.
No external expert or formal proof acceptance is claimed.

SC-META-53 remains UNCERTAIN; it supplies none of these positive Hilbert,
Hamiltonian, bath or observable inputs. LT-SM8/LT-GR6b/AC-F1, source register,
physics ledger and canon remain unchanged. The native paired full20/K-C/domain
adapter and finite-T scalar cuts remain distinct research constructions.
