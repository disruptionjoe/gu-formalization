---
title: "K128 K127 axial Coulomb reduced gauge Fock domain wave"
status: active_research
doc_type: reverse_scaffold_reduced_gauge_fock_domain_result
created: 2026-09-07
date: 2026-09-07
target_claim: INTERNAL_TARGET:K127_DYNAMICAL_GAUSS_FOCK_DOMAIN_POINT_NESS_SUCCESSOR
claim_ceiling: exact repository-owned continuum finite-interval axial/Coulomb reduction of the U(1)^8 Gauss law on the K127 impurity/Klein/CAR carrier, with operator-valued electric fields, a nonempty neutral reduced physical sector, electric-string response for every neutral defect transition, and a semibounded self-adjoint Hamiltonian from one common positive closed form domain carrying the bounded fixed-width defect; no kinematic connection Hilbert representation, nontrivial local gauge implementer or Haar projector, equality with K127's signed Dirac operator domain, singular point-Fock extension, thermodynamic scattering, interacting NESS/current, source/GU ownership, Born derivation, prediction, confirmation or holdout credit follows
manifest: lab/process/k128-k127-axial-coulomb-reduced-gauge-fock-domain-wave.json
probe: tests/channel-swings/k128_k127_axial_coulomb_reduced_gauge_fock_domain_probe.py
---

# K128 K127 axial/Coulomb reduced-gauge Fock-domain wave

> **GU-COMPARATOR-ROUTING — scope before inference.** This artifact contains or
> borders a conventional particle-physics comparator. Any result about a
> standard Higgs/VEV, ordinary family index or net chirality, SO(10) `126`
> Majorana mechanism, anomaly selector, VEV-only breaking or familiar vector-
> mass route binds only that named model. It is not evidence for or against
> Weinstein's source-native mechanism without an explicit typed bridge. Read
> `lab/methods/source-native-comparator-routing.md` and follow its source-native
> pointers before reusing this result.

Classification: `INTERNAL_STRUCTURAL_ONLY`

```gu-typed-objects
result: continuum finite-interval axial/Coulomb solution of eight Abelian Gauss laws with reduced electric operators and one positive closed Fock form carrying the fixed-width K127 defect
carrier: charge-neutral sector of C9 impurity tensor irreducible Cl_18(C) module C512 tensor antisymmetric Fock space over eighteen full Dirac species on a finite interval LAYER=observed CHIRALITY=S-FULL-DIRAC
pairing: positive-energy Dirac/Fock quadratic form plus reduced electric L2 form and Hilbert adjoint ON=repository_owned_continuum_interval_reduced_gauge_control
real_structure: CAR adjoint, complex spinor conjugation, Hermitian Clifford-Klein generators and eight real electric distributions reconstructed from charge
grading: total fermion parity and total Z8 charge; local gauge redundancy is solved rather than represented kinematically
action_owner: repository-construction
target: reduced Gauss/electric physical sector and common semibounded form domain, with connection, point, thermodynamic and source boundaries MAP-TYPE=quotient
```

Scope: this packet uses an equivalent reduced representation of 1+1-dimensional
Abelian gauge theory on one finite interval in an explicitly selected trivial-
open-holonomy sector. It quantizes the charged
impurity/CAR degrees of freedom and reconstructs the electric field from Gauss
law after axial gauge fixing. It does not construct a Hilbert-space connection
operator, a nontrivial representation of the unreduced local gauge group, or
an infinite-volume reservoir theory.

## Inline preflight bookend

The rebuilt frontier contained seven substantial arcs. Axial/Coulomb reduction
is independently constructive. Its success releases the electric-field,
nonempty-physical-sector and common-form-domain arcs. A kinematic connection
and local-group-averaging arc remains an independent discriminator because a
reduced quotient is not its unreduced parent. The singular point-Fock and
thermodynamic NESS arcs are independent successors. Source/action ownership is
excluded because no qualified source packet selects the imported data.

Mechanism retrieval separates K128 from K124's finite spatial lattice, K125's
weak-Gauss consistency and linear-mollifier obstruction, K126's formal BV-BFV
and finite-regulator Wilson/Klein theorem, and K127's continuum CAR theory in
a fixed external connection. The new content is an exact continuum reduced
electric operator and positive physical form, not another lattice or external-
background declaration.

The route-changing lens census covered constrained Hamiltonian reduction,
1+1-dimensional Maxwell theory, CAR Fock forms, fermionic eigenvalue counting,
Wilson/electric duality, local and large gauge transformations, KLMN form
sums, IBC and resolvent theory, finite-volume recurrence, scattering/NESS,
source fidelity, representation typing and hostile philosophy of science. The
axial route is primary because it makes the constraint and form domain exact.
An unreduced connection representation, a singular extension and an infinite-
volume scattering construction remain genuine successor routes.

## 1. Gauss law is solved exactly on a finite interval

Let `Sigma=[0,L]`, choose a defect point `x_0` in its interior, restrict gauge
transformations to be the identity at both endpoints, and select the sector
whose open Wilson holonomy is trivial. Only in that selected sector may the
connection be put globally in axial gauge `A_x=0` by an endpoint-trivial gauge
transformation. Give the nine
impurity states K124's charges `q_v in Z^8`, and give the eighteen CAR species
the corresponding opposite transition charges. On an `n`-particle
configuration `X=(x_1,e_1;...;x_n,e_n)` define

```text
rho_a(X;x)=q_imp,a delta(x-x_0)+sum_j c_(e_j,a) delta(x-x_j),
E_a(X;x)=eta_a+q_imp,a 1_[x_0,L](x)
                 +sum_j c_(e_j,a) 1_[x_j,L](x).             (1)
```

Then `partial_x E_a=rho_a` distributionally and `E_a(0)=eta_a`. Fixing the
same electric flux at the right endpoint imposes

```text
q_imp+sum_j c_(e_j)=0.                                    (2)
```

The direct sum of the sectors satisfying (2) is a closed charge-neutral Fock
subspace. It is nonempty: the root impurity state, CAR vacuum and zero boundary
flux lie in it. For real `g in L2(Sigma)`, `E_a(g)` is the maximal multiplication
operator by `integral gE_a`; it is self-adjoint. Thus the electric field is a
genuine quantum operator in this reduced representation, but it is a function
of matter charge rather than an independent canonical coordinate.

For a test function `alpha` vanishing at the boundary, integration by parts
gives

```text
G(alpha)=sum_a integral alpha(partial_x E_a-rho_a)=0        (3)
```

on the finite-particle core. The Gauss generators therefore vanish after the
constraint is solved, and local gauge transformations act trivially on the
reduced physical Hilbert space. This is the reduced Dirac quotient. It is not
a nontrivial kinematic connection/electric representation, a normalized Haar
average over the infinite-dimensional continuum gauge group, or a proof about
large gauge transformations on a circle.

## 2. Neutral defect transitions carry the exact electric string

For an edge `e:u->v`, write `b_e=q_v-q_u`. A neutral impurity/CAR transition
changes the local charge distribution by

```text
Delta rho_a(x)=b_(e,a) delta(x-x_0)-b_(e,a) delta(x-y).
```

Equation (1) gives

```text
Delta E_a(x)=b_(e,a)(1_[x_0,L](x)-1_[y,L](x)),             (4)
```

which is supported exactly on the interval between the defect and the created
or annihilated reservoir excitation. Its electric energy is finite and equals

```text
sum_a integral |Delta E_a|^2 dx
  = |b_e|^2 |y-x_0|.                                      (5)
```

This is the electric-flux dual of K126/K127's open Wilson string. In axial
gauge the Wilson multiplier is one, but its physical string has not vanished:
it is stored in the changed electric field. The defect preserves total charge
and maps the reduced sector to itself. Its one odd CAR factor and one odd
Klein factor still make it even.

## 3. One positive closed form carries the fixed-width defect

Let `h_D=(1+D^*D)^(1/2)` for one self-adjoint finite-interval Dirac boundary
condition, and let

```text
q_D[Psi]=<Psi,dGamma(h_D)Psi>,
q_E[Psi]=(1/2)sum_a g_a^2 integral_0^L ||E_a(x)Psi||^2 dx. (6)
```

Both forms are positive. On every finite-particle sector, (1) gives
`q_E <= C(N+1)^2`. Because the interval is compact and the internal
multiplicity is finite, the positive Dirac eigenvalue counting function grows
linearly. The Pauli principle therefore gives

```text
(N+1)^2 <= C'(q_D+||Psi||^2).                              (7)
```

Consequently `q_E` is continuous in the `q_D` form norm, and
`q_0=q_D+q_E` is positive and closed on `Q(q_D)`. K127's fixed-width
Wilson/Klein defect `V` is bounded and symmetric. In axial gauge its Wilson
factor is trivial, and

```text
q=q_0+<Psi,V Psi>                                         (8)
```

is closed and semibounded on exactly `Q(q_0)`. The first representation
theorem gives a unique self-adjoint physical Hamiltonian. Charge neutrality
and total parity reduce it, so the neutral even sector is invariant.

This is a common **quadratic-form domain** theorem. It does not prove that the
operator domain equals K127's `Dom(dGamma(D_A))`: (6) deliberately uses the
positive-energy operator `(1+D^*D)^(1/2)`, whereas K127's earlier bounded-
perturbation statement used a signed self-adjoint Dirac generator. Nor does it
construct an unreduced `A,E` canonical pair, a continuum BV Laplacian or a
quantum master equation.

## 4. The finite interval exposes the boundary-sector import

The trivial open-holonomy sector, boundary flux `eta`, endpoint gauge
convention, interval length, Dirac boundary condition, positive kinetic form,
charge normalization and couplings are all selected by this repository
construction. If both endpoint fluxes are
fixed equal, total neutrality is mandatory. If a boundary reservoir may absorb
flux, charged sectors reappear, but that is a different boundary theory.

An arbitrary interval holonomy would likewise remain as boundary data rather
than being gauged to zero under the declared endpoint convention. On a circle
axial gauge leaves eight holonomies and large-gauge spectral flow;
K128 does not identify the finite-interval quotient with that circle theory.
Likewise, because the local gauge redundancy has already been divided out,
the identity implementer in (3) cannot be advertised as the nontrivial anomaly-
free local implementation requested of an unreduced connection Hilbert space.
The vectorlike K125 anomaly cancellation remains a necessary compatibility
control, not a construction of that parent representation.

## 5. Point unsmearing and finite-coupling NESS remain open

The electric-string energy (5) tends to zero as `y->x_0`; it does not cancel
the CAR point-field divergence. K125's delta-normalized smearing still has
`||f_epsilon||_2=epsilon^(-1/2)`. A nonzero point interaction therefore still
requires an IBC, counterterm, closed singular form or resolvent construction;
(8) owns only fixed nonzero width.

The finite interval is also not a reservoir thermodynamic limit. For any
bounded polarization observable `A` whose current is `J=dA/dt`, unitary
dynamics gives

```text
(1/T) integral_0^T <J(t)>dt
  = (<A(T)>-<A(0)>)/T,
abs(...) <= 2||A||/T -> 0.                                (9)
```

This exact bound excludes a persistent irreversible flux represented as the
derivative of a bounded finite-volume storage observable. It does not exclude
all persistent currents, and it is not a return-to-NESS theorem. Infinite
leads plus a Moller/Ruelle construction, asymptotic normality or another
thermodynamic scattering framework remain necessary before comparing a field
current with K115's reduced affinity `6561/256`.

## Inline postflight bookend

The axial/Coulomb, electric-sector and common-form arcs completed. Every
neutral defect transition carries the exact finite electric string, and the
root/CAR vacuum proves the reduced sector nonempty. The kinematic connection
arc returned a precise type boundary: reduction supplies identity Gauss action,
not a nontrivial local gauge representation or continuum Haar projector. The
point arc retained the `L2` divergence, and the NESS arc reached the exact
finite-volume Cesaro boundary rather than a thermodynamic construction.

- **Strongest construction:** a genuine continuum reduced electric operator
  and one semibounded self-adjoint physical Hamiltonian from a common positive
  form domain carrying the fixed-width defect.
- **Strongest overclaim caught:** solving Gauss law is not the same as building
  the unreduced connection/electric representation and then proving its
  physical kernel nonempty.
- **Strongest contrary route:** a circle Hilbert bundle with holonomy spectral
  flow or an unreduced constructive gauge representation could add the missing
  connection and large-gauge data; an IBC/resolvent model could add the point
  interaction.
- **Weakest reproducibility seam:** the analytic closure uses the compact-
  interval positive Dirac counting bound. The probe checks its exact finite-
  multiplicity skeleton but is not a substitute for a source-selected Dirac
  boundary condition.

No source action, physical preparation, detector effect, Born rule, held-out
score, prediction, confirmation, canon, paper, release or public-posture
status changes.

## Next condition

Construct the unreduced continuum `U(1)^8` connection/electric Hilbert
representation, nontrivial anomaly-free local and large gauge implementers,
and prove that its Dirac/BRST physical space is unitarily equivalent to (or
corrects) K128's axial/Coulomb quotient on a common operator domain. Independently
construct the singular number-changing Fock IBC/counterterm/form/resolvent
limit. Then take an infinite-lead thermodynamic limit and prove finite-coupling
scattering or return to an interacting NESS before identifying a microscopic
current. Separately require an actual source/GU action selecting the gauge
group, boundary sector, charges, carrier, kinetic form, couplings and state.

## Reproduction

```bash
python3 tests/channel-swings/k128_k127_axial_coulomb_reduced_gauge_fock_domain_probe.py
python3 tests/channel-swings/k128_k127_axial_coulomb_reduced_gauge_fock_domain_probe.py --selftest
```
