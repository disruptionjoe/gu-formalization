---
title: "K2100: Reference decoupling and the two meanings of local reset"
status: active_research
doc_type: exploration
created: "2026-10-26"
classification: INTERNAL_STRUCTURAL_ONLY
target_claim: NONE-NOT-A-KILL
claim_ceiling: conditional mathematics; no local apparatus, source selection, GU verdict, novelty or external certification
scripts:
  - tests/channel-swings/k2100_reference_decoupling_reset_probe.py
---

# K2100: Reference decoupling and the two meanings of local reset

Classification: `INTERNAL_STRUCTURAL_ONLY`.

> **GU-COMPARATOR-ROUTING — scope before inference.** This artifact contains or
> borders a conventional particle-physics comparator. Any result about a
> standard Higgs/VEV, ordinary family index or net chirality, SO(10) `126`
> Majorana mechanism, anomaly selector, VEV-only breaking or familiar vector-
> mass route binds only that named model. It is not evidence for or against
> Weinstein's source-native mechanism without an explicit typed bridge. Read
> `lab/methods/source-native-comparator-routing.md` and follow its source-native
> pointers before reusing this result.

```gu-typed-objects
result: conditional operational theorem with supplied representation and controls
carrier: free massive sea excitation CAR and finite memory with ordinary tensor reference LAYER=toy CHIRALITY=S-FULL-DIRAC
pairing: positive Hilbert metric ON=declared_complex_completion
real_structure: CAR adjoint and explicit particle-hole split, not source-selected reality
grading: fermion parity with energy sign and charge kept distinct
action_owner: repository-construction -- supplied free dynamics and smeared controls
target: conditional operational state and instrument constraints MAP-TYPE=intertwiner
```

[Conditional mathematics accepted after independent internal specialist review and exact finite controls. No external or proof-assistant certification.]

## Source and Layer0 boundary

SC-OP-04 ASSERTS candidate four-field operator grammar; SC-OP-05 and
SC-META-53 remain UNCERTAIN; SC-META-56 DISAVOWS a mandatory odd action.
These supplied positive CAR models are not source operator9.16. K2021 already
constructs local R0/R1 but does not source-select these dynamics, observations
or states. LT-SM8/LT-GR6b retain action/observation/quotient/positivity debts.
Source-register, physics-ledger and canon verdicts remain unchanged. No new
substrate pathway or source mechanism is asserted. The results supply scoped
reverse-scaffold constraints and conditional mathematical constructions.


## 1. Fixed excitation modes and a reference-uniform estimate

Use exactly K2098's free massive sea excitation Fock representation. Fix a
finite-dimensional excitation subspace L, put its Fock factor first, and let
R be an arbitrary ordinary tensor-factor quantum reference. A fermionic
reference requires the specified graded ordering; disjoint full CAR algebras
must not silently be treated as commuting tensor factors. Let rho be any
joint normal density on Fock(K) tensor R, and evolve only the field by the
free dynamics. Write rho_LR(t) for its restriction and rho_R for its unchanged
reference marginal. Define

    epsilon(t)=1-Tr rho_L(t)|0_L><0_L|.

**Theorem.** For every such joint normal state,

    T(rho_LR(t), |0_L><0_L| tensor rho_R)
      <=min(1, epsilon+sqrt(epsilon(1-epsilon))) ->0.    (1)

T is half trace norm. The bound depends only on the system marginal and is
uniform over all its normal extensions and all reference dimensions. It is
pointwise in that system marginal, not diamond convergence over all inputs.

Proof: write the reduced density in blocks relative to vacuum versus its
orthogonal complement as [[A,B],[B*,C]], identifying the vacuum block with R.
Tr C=epsilon, Tr A=1-epsilon and rho_R=A+Tr_L C; the off-diagonal blocks have
zero partial trace. The difference from the product in(1) has diagonal blocks
[-Tr_L C,C], with half trace norm epsilon. Positivity yields
B=A^(1/2) K C^(1/2), ||K||<=1, hence ||B||_1<=sqrt(epsilon(1-epsilon)).
The off-diagonal matrix has half trace norm ||B||_1. Triangle inequality and
the universal T<=1 prove the bound, including trace-class infinite R by
finite-rank approximation or the trace-class factorization directly.

K2098's PROOF, for an arbitrary fixed finite excitation L, gives epsilon->0:
for finite mean number gamma is trace class and

    epsilon(t)<=q_L(t)=sum_j <exp(it h)e_j,gamma exp(it h)e_j> ->0.  (2)

The massive spectrum makes exp(it h) weakly tend to zero. General normal
states are approximated in trace norm by number-truncated densities, uniformly
under dynamics. This uses the excitation statement proved before physical
CAR restriction, not an invalid assumption that physical sea modes are pure.
Thus(1) also holds for nonquasifree states and infinite mean number/energy.

The available K2098 derivative budget C_L gives q_L(t)<=C_L/t² and therefore

    T_joint(t)<=min(1, C_L/t²+sqrt(C_L)/|t|).             (3)

No rate follows without its actual regularity/summability assumptions. Its
bounded-energy time-shift counterfamily still excludes a common energy-only
clock. The reference estimate is a consequence of nearly pure marginal
structure, not erasure of globally preserved unitary information.

## 2. Sharp order and actual reference correlation

For the two-register pure state

    psi=sqrt(1-e)|00>+sqrt(e)|11>, 0<=e<=1,

the distance to |0><0| tensor diag(1-e,e) is exactly

    (e+sqrt(4e-3e²))/2.                                (4)

The difference matrix has eigenvalues -e,0,(e±sqrt(4e-3e²))/2. Hence no
universal O(e) estimate can replace the sqrt(e) term in(1). This is a total-
parity-even state if both registers are fermionic. A diagonal correlated
mixture has distance e; forgetting that coherent cross block would give a
false stronger theorem. The bound(1) itself is not claimed sharp.

## 3. Pure excitation reset versus mixed physical reset

A supplied even fermionic swap of L with an equal finite memory, including
its known number phases, transfers the excitation vacuum and its decoupling.
Put L and the receiving memory in adjacent ordered fermionic blocks, L first,
and keep any further R an ordinary tensor reference. For arbitrary original
memory data, apply the block estimate with the receiving memory included in
the reference factor before the swap. After relabelling the old memory as
outgoing L, the ideal output is a vacuum memory with that relabelled remaining
marginal, up to the swap's error.
This is a state-preparation resource in the supplied free representation.
It requires access to the excitation modes and an implemented swap. It is not
provided by passive waiting of a stationary isolated memory or by a local
laboratory coupling that has not been constructed.

For fixed physical test space F, put
L=span{Pf,conjugate(Qf): f in F} in the separate excitation summands. K2098
embeds CAR(F) in CAR(L). Restriction is a finite-matrix CP channel, also when
tensored with R. Equation(1) therefore implies

    T(rho_FR(t), tau_F tensor rho_R) ->0,

where tau_F is the physical sea restriction. It may be mixed even though the
excitation vacuum on L is pure. If nu_j are eigenvalues of Q compressed to F,
the gauge-invariant quasifree sea restriction has product eigenvalues from
nu_j and 1-nu_j. Therefore

    lambda_max(tau_F)=product_j max(nu_j,1-nu_j).
    min_(pure psi) T(tau_F,|psi><psi|)=1-lambda_max(tau_F). (5)

Measuring the projector onto psi proves the lower bound; its largest-eigenvalue
eigenvector attains it. Arbitrary register unitaries cannot change the spectrum.
If a fixed vacuum target and only parity-even unitaries are permitted, the
optimum instead uses the largest eigenvalue WITHIN THE VACUUM PARITY BLOCK;
(5) remains a lower bound but need not be achievable. A one-mode state with
nu=3/4 has unrestricted minimum1/4, while even unitaries cannot convert its
occupied eigenvector into vacuum, whose error is3/4. An auxiliary entropy sink
or selection measurement is a new resource, not a unitary purification.

Thus physical local return does erase correlations with a fixed external
reference asymptotically, but it need not prepare a pure physical-mode register.
This strengthens K2098 without contradicting its warning about pure memory.
The memory resource must be specified as excitation or physical CAR.

## 4. Verification, controls and continued obligation

The exact probe diagonalizes the actual correlated state difference, checks
full two-mode Fock reset by a signed even swap, compares a coherent pair and
diagonal mixture, and computes mixed-sea spectra including the parity-block
countercontrol. Faults change state data or the swap, not the validation
predicate. The analytic proof, not those finite controls, proves general
normal-state/continuum/reference convergence. The next test is access to these
excitation modes through a local interaction, or decay for a source-selected
observed interacting algebra; neither follows from free global normality.

The nearly pure marginal argument uses standard gentle-measurement reasoning;
see [Aaronson and Rothblum, Gentle Measurement of Quantum States and Differential
Privacy (2019)](https://arxiv.org/abs/1904.08747) for adjacent background.
No novelty is claimed. Here the exact block proof states the norm, reference,
representation and reset limits directly.
