---
title: "K1427--K1432 Gaussian continuum BRST boundary"
status: active_research
doc_type: conditional-build-result
classification: SOURCE_NATIVE_ROUTE
direction: observed_to_native
target_claim: SC-META-53
created: "2026-10-08"
updated_at: "2026-10-08"
---

# K1427--K1432 Gaussian continuum BRST boundary

> **GU-COMPARATOR-ROUTING — scope before inference.** This artifact contains or
> borders a conventional particle-physics comparator. Any result about a
> standard Higgs/VEV, ordinary family index or net chirality, SO(10) `126`
> Majorana mechanism, anomaly selector, VEV-only breaking or familiar vector-
> mass route binds only that named model. It is not evidence for or against
> Weinstein's source-native mechanism without an explicit typed bridge. Read
> `lab/methods/source-native-comparator-routing.md` before reuse.

Classification: `SOURCE_NATIVE_ROUTE` only because the packet tests the
positive-physical-Hilbert requirement under SC-META-53. The Gaussian tower,
charge sequence, gauge fixing, frequencies and Wick ordering are repository-
owned controls, not released GU data.

```gu-typed-objects
result: compatible product-Gaussian continuum representation, refinement-stable closed Gaussian BRST cohomology, free second-quantized Hamiltonian and exact quartic renormalization boundary
carrier: countable Gaussian coordinate product and symmetric/fermionic Fock completion of finite reduced and based-gauge cylinder blocks LAYER=toy BRIDGE=maximal-compact-charge-reduction CHIRALITY=N/A
pairing: positive product-Gaussian L2 and Fock pairing ON=repository_owned_continuum_control
real_structure: coordinatewise conjugation on the real Gaussian and charged complex mode planes
grading: boson number, ghost number, residual integer charge and cutoff filtration
action_owner: repository-construction -- no released source action, measure or renormalization prescription
target: SC-META-53 continuum positive-quantum-control boundary MAP-TYPE=restriction
```

## K1427 — compatible product-Gaussian tower

Let `gamma_N` be the normalized product Gaussian on the first `N`
coordinates, with each charged complex mode represented by a real two-plane.
For `M>=N`, the coordinate projection pushes `gamma_M` exactly to `gamma_N`.
The projections compose, so the finite marginals define the countable product
measure `gamma_infinity`. Conditional expectation onto the first `N`
coordinates is an orthogonal contraction, and the martingale convergence
theorem makes finite-coordinate cylinders dense in `L2(gamma_infinity)`.

This is an actual compatible continuum probability representation. It is not
translation invariant, a measure on a specified nonlinear distributional
field space, or a source-derived path-integral measure.

## K1428 — inductive Hilbert and Haar compatibility

Pullback along coordinate projection gives isometries

```text
J_NM : L2(gamma_N) -> L2(gamma_M),    J_NM f=f o pi_MN.
```

Their adjoints integrate the new coordinates. The completed inductive limit is
canonically `L2(gamma_infinity)`. An integer charge on each complex mode plane
acts coordinatewise by rotations. The action is strongly continuous on the
continuum Hilbert space because it is strongly continuous on dense cylinder
functions and all operators are unitary. Charge-stable cutoffs intertwine the
action, hence normalized Haar projections obey

```text
J_NM P_N=P_M J_NM,        E_N P_infinity=P_N E_N.
```

The compact invariant sector therefore survives refinement without assuming a
free residual action. The charge sequence and its normalization remain
repository choices.

## K1429 — closed continuum Gaussian BRST complex

Use the symmetric Gaussian Fock realization for countably many based-gauge
coordinates and exterior Fock for their ghosts. On the algebraic finite-
particle core set

```text
d=sum_j a_j tensor c_j^*,       d^2=0.
```

The closure is a densely defined closed differential. Its Hodge operator is
the total boson-plus-fermion number operator. The joint vacuum is its only
zero mode and the positive-number sector has gap one. Consequently all
degreewise ranges are closed, `d^* N^{-1}` contracts the positive sector,
and, after tensoring with the K1428 compact-invariant reduced factor,

```text
H^0 = H_reduced,infinity^U(1),       H^k=0 for k>0.
```

Finite-block embeddings are chain maps and preserve the vacuum harmonic
representatives, so this positive nonzero degree-zero cohomology is stable
under the declared refinement tower. This remains Gaussian gauge-fixed
cohomology, not an interacting source BRST charge or a unitary realization of
bare noncompact gauge translations.

## K1430 — compatible free continuum Hamiltonian

Let `omega` be a positive diagonal one-particle operator with
`omega_j>=omega_0>0`, diagonal also in the residual charge decomposition. Its
second quantization `H_0=dGamma(omega)` is positive self-adjoint, essentially
self-adjoint on finite particles and gapped above its vacuum. Spectral cutoffs
commuting with `omega` and charge satisfy the exact core intertwining relation,
and their resolvents converge strongly to the continuum resolvent. `H_0`
commutes with residual Haar projection and with the separate Gaussian gauge
differential, so it descends to K1429's degree-zero cohomology.

This closes only the free continuum operator layer. It does not contain the
quartic interaction or prove K1413's full nonlinear PDE estimate.

## K1431 — quartic counterterms and Wick martingale

For a three-dimensional massive free-field cutoff, let
`C_N=E(phi_N(x)^2)`. The positive mode sum `C_N` diverges, and

```text
E integral phi_N^4 = 3 Vol C_N^2.
```

If `phi_M=phi_N+eta` and the new modes have variance `Delta C`, exact Gaussian
moments give

```text
E(phi_M^4 | F_N)=phi_N^4+6 Delta C phi_N^2+3(Delta C)^2.
```

Thus the bare quartic forms are not projectively compatible: mode elimination
forces quadratic and vacuum counterterms. The Wick polynomial

```text
:phi_N^4: = phi_N^4-6 C_N phi_N^2+3 C_N^2
```

does satisfy the martingale relation
`E(:phi_M^4:|F_N)=:phi_N^4:`. This is a precise renormalized interaction
candidate, not a continuum Hamiltonian theorem. Wick ordering destroys
pointwise nonnegativity, and this packet proves no uniform lower bound,
closability of a limiting form, resolvent convergence, or need/sufficiency of
further counterterms.

## K1432 — admission replay

The bridge census has 97 rows: 68 satisfied, eight conditional, seventeen
excluded and four missing. New satisfied rows record the compatible continuum
Gaussian representation, closed refinement-stable positive Gaussian BRST
cohomology and free second-quantized Hamiltonian. The Wick interaction remains
conditional, while the unrenormalized quartic cutoff family is excluded.

The same four physical/source rows remain missing: source selection and
normalization, source-action identification, cutoff-uniform completed global
PDE evolution with interacting continuum positive physical Hilbert
cohomology, and a source-owned observed-state/export map. K1145/K1150 remain
`0/7`; protected source, ledger, canon, paper and public-posture states do not
move.

## Exact next input

Advance the interacting quantum arc only with uniform lower bounds and
closability for the Wick/counterterm forms, convergence to a self-adjoint
continuum Hamiltonian, and a closed interacting BRST charge preserving its
positive cohomology. The analytic wake remains a full-PDE estimate controlling
both K1413 leakage terms. Source admission still requires an action-owned
observed-carrier selector and normalization for `Q`.
