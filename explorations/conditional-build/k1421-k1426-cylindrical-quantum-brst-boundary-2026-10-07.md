---
title: "K1421--K1426 finite-cylindrical quantum BRST boundary"
status: active_research
doc_type: conditional-build-result
classification: SOURCE_NATIVE_ROUTE
direction: observed_to_native
target_claim: SC-META-53
created: "2026-10-07"
updated_at: "2026-10-07"
---

# K1421--K1426 finite-cylindrical quantum BRST boundary

> **GU-COMPARATOR-ROUTING — scope before inference.** This artifact contains or
> borders a conventional particle-physics comparator. Any result about a
> standard Higgs/VEV, ordinary family index or net chirality, SO(10) `126`
> Majorana mechanism, anomaly selector, VEV-only breaking or familiar vector-
> mass route binds only that named model. It is not evidence for or against
> Weinstein's source-native mechanism without an explicit typed bridge. Read
> `lab/methods/source-native-comparator-routing.md` before reuse.

Classification: `SOURCE_NATIVE_ROUTE` only because the packet tests the
positive-physical-Hilbert requirement under SC-META-53. Every coordinate,
measure, compact generator, gauge fixing and Hamiltonian below is a
repository-owned finite-cylindrical control, not released GU data.

```gu-typed-objects
result: finite-cylindrical Schrödinger representation, compact invariant projector, noncompact gauge-volume obstruction, Gaussian gauge-fixed BRST Hilbert complex and positive finite-block Hamiltonian
carrier: finite Coulomb/Gauss-reduced coordinate blocks tensored with based-gauge coordinates and a finite ghost exterior algebra LAYER=toy BRIDGE=maximal-compact-charge-reduction CHIRALITY=N/A
pairing: positive L2 pairing from invariant Gaussian measures, with Gaussian gauge-fixing measure on based-gauge coordinates ON=repository_owned_finite_cylindrical_control
real_structure: real reduced coordinates plus complex integer-charge matter coordinates and complex ghost exterior algebra
grading: ghost degree, residual integer charge and finite cylindrical block index
action_owner: repository-construction -- no released source action or quantum measure
target: SC-META-53 finite-cylindrical positive quantum-control boundary MAP-TYPE=restriction
```

## K1421 — finite-cylindrical Schrödinger representation

Fix finitely many Coulomb/Gauss-reduced real coordinates `y` and complex
matter coordinates `z_j` with integer charges `q_j`. On the finite-dimensional
configuration space use the centered Gaussian measure whose quadratic form is
constant on each charge subspace. The residual circle acts unitarily by

```text
(U(theta)Psi)(y,z)=Psi(y,exp(-i theta q)z).
```

Invariant polynomial cylinder functions are dense, complex conjugation gives
the real structure, and bounded invariant cylinder observables act by bounded
multiplication. This is a positive Schrödinger representation for each fixed
block. It is not a preferred continuum measure or a quantization of every
classical observable.

## K1422 — compact averaging respects orbit types

Normalized Haar averaging

```text
P0 Psi=(2 pi)^(-1) integral_0^(2 pi) U(theta)Psi dtheta
```

is an orthogonal norm-one projection onto the closed invariant subspace. On a
charge monomial it retains exactly total charge zero. The construction uses
compactness, not freeness: a support with gcd `d` retains stabilizer `Z_d`,
neutral support retains all of `U(1)`, and gcd-one support is free. All enter
the same invariant Hilbert space without flattening the classical orbit-type
stratification.

## K1423 — bare based BRST has a gauge-volume obstruction

For `m` based-gauge coordinates `chi`, the translation-invariant Hilbert
representation is `L2(R^m,dchi)`. The bare degree-zero BRST equation is
`partial_chi_j Psi=0` for every `j`. Its only solutions are functions constant
in `chi`, and no nonzero constant is square integrable. Hence bare degree-zero
state cohomology is zero. Moreover momentum has no spectral gap: normalized
Fourier packets supported in balls of radius `1/n` satisfy
`||p Psi_n||<=1/n`. The range is not closed. Dividing by the noncompact based
gauge volume therefore cannot be implemented by naive invariant `L2`
vectors.

## K1424 — Gaussian gauge fixing gives a closed Hilbert complex

Replace the based-gauge factor by normalized Gaussian measure `gamma_m` and
take the closed differential

```text
d_gamma=sum_j partial_chi_j wedge e_j
```

on the Gaussian Sobolev domain. Its adjoint is
`d_gamma*=sum_j(-partial_chi_j+chi_j) contraction e_j`. The Hodge operator is
the Ornstein--Uhlenbeck number operator. It has kernel the constants in degree
zero and spectrum at least one on the orthogonal complement. Thus every range
is closed and

```text
H0(d_gamma tensor 1)=H_reduced^U(1),       Hk=0 for k>0.
```

The induced cohomology pairing is positive and nonzero whenever the invariant
reduced block is nonzero. This is a gauge-fixed Hilbert complex. Gaussian
measure is not translation invariant, so it is not a unitary realization of
the bare noncompact gauge group and does not derive the Faddeev--Popov measure
from the source action.

## K1425 — positive finite-block interacting Hamiltonian

On each reduced block use the closed semibounded form

```text
h_N[Psi]=1/2||grad Psi||^2+integral V_N |Psi|^2,
V_N=m^2|y,z|^2+mu|Qz|^2+lambda|z|^4,  m,mu,lambda>0.
```

The polynomial potential is circle invariant and coercive. The Friedrichs
operator is self-adjoint, bounded below and has compact resolvent in finite
dimension. It commutes with `P0`, so its restriction to the invariant Hilbert
space is self-adjoint and positive. This is an interacting quantum Hamiltonian
for the declared finite block.

No continuum conclusion follows. Projecting a quartic field interaction to a
larger block changes lower-block effective terms, Gaussian reference measures
are not supplied as a compatible infinite-dimensional family, and K1413's
two PDE leakage terms remain uncontrolled. A compatible inductive/projective
Hilbert limit, renormalized Hamiltonian, closed continuum quantum BRST
operator and global nonlinear evolution are separate missing data.

## K1426 — admission replay

The bridge census has 92 rows: 65 satisfied, seven conditional, sixteen
excluded and four missing. New satisfied rows record the finite cylindrical
positive representation, compact Haar projector, closed Gaussian BRST
cohomology and finite-block Friedrichs Hamiltonian. One conditional row records
the absent compatible continuum limit. One excluded row records the failure of
bare translation-invariant `L2` BRST states.

The same four physical/source rows remain missing: source selection and
normalization, source-action identification, cutoff-uniform completed global
PDE evolution with continuum quantum physical Hilbert cohomology, and a
source-owned observed-state/export map. K1145/K1150 remain `0/7`; protected
source, ledger, canon, paper and public-posture states do not move.

## Exact next input

The quantum wake is now a compatible continuum construction: specify a
cutoff-consistent measure or representation, renormalized interacting
Hamiltonian and closed continuum BRST operator whose positive cohomology is
stable under block refinement. The analytic wake remains a full-PDE estimate
controlling both K1413 leakage terms. Source admission still requires an
action-owned observed-carrier selector and normalization for `Q`.
