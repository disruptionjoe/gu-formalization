---
title: "K124 K123 spatial U(1)^8 lattice-gauge BFV completion wave"
status: active_research
doc_type: reverse_scaffold_spatial_lattice_gauge_result
created: 2026-09-07
date: 2026-09-07
target_claim: INTERNAL_TARGET:K123_LOCAL_GAUGE_GAUSS_AND_PHYSICAL_BFV_COMPLETION
claim_ceiling: exact repository-owned finite periodic-spatial-lattice U(1)^8 gauge completion of the K123 defect charges, with local covariance, commuting Gauss constraints, nonempty group-averaged Dirac sector, algebraic BFV differential and self-adjoint electric-plus-bounded Hamiltonian; no source/GU ownership, continuum or unsmeared limit, Lagrangian BV master action, complete interacting AQFT, NESS, Born derivation, prediction, confirmation or holdout credit follows
manifest: lab/process/k124-k123-spatial-u1-8-lattice-gauge-bfv-completion-wave.json
probe: tests/channel-swings/k124_k123_spatial_u1_8_lattice_gauge_bfv_completion_probe.py
---

# K124 K123 spatial `U(1)^8` lattice-gauge BFV completion wave

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
result: exact finite-spatial-lattice gauging of the K123 vertex-charge defect and its Gauss/Dirac/BFV boundary
carrier: nine-state K115 system tensor finite periodic spatial lattice of 18 full left-right Dirac CAR species and eight compact U(1) link rotors LAYER=observed CHIRALITY=S-FULL-DIRAC
pairing: Hilbert adjoint, CAR trace pairing, Haar group average and rotor l2 inner product ON=repository_owned_finite_lattice_control
real_structure: CAR and rotor Hilbert adjoint with integer electric spectrum and complex conjugation of link phases
grading: fermion parity plus degree-one ghosts for 8N commuting local Gauss generators; no source BV grading
action_owner: repository-construction
target: finite-lattice gauge-covariant defect Hamiltonian, Gauss kernel and algebraic BFV/Dirac reduction MAP-TYPE=quotient
```

Scope: this result binds one repository-selected finite periodic spatial
lattice regularization of K123. It promotes the eight surviving vertex-charge
directions to local lattice gauge covariance without promoting the ten broken
transition-graph cycle phases. It does not bind Weinstein's action, a GU-native
gauge group, a continuum theory, or nature's state/effect rule.

## Inline preflight bookend

The rebuilt frontier had five compatible arcs: (1) localize the exact K123
charge lattice; (2) construct link fields, Gauss generators and a nonempty
physical sector; (3) own the Hamiltonian domain; (4) test gauge fixing,
holonomy and parameter selection; and (5) preserve the modular-affinity and
Born ceilings under hostile review. A sixth continuum/AQFT arc depends on a
regulator-removal and constraint-domain theorem not presently supplied. A
source/GU ownership arc remains authority-blocked by the action-root gap.

The primary route is a finite spatial Kogut--Susskind regulator because it
makes locality, compact gauge averaging, charge integrality, the Gauss kernel,
and operator domain explicit. A link model on the 18-edge transition graph was
rejected as the primary route: locality in state space is not locality in
spacetime. A formal continuum declaration was rejected because it would hide
the unsmeared-defect and gauge-domain burdens. The fallback after this finite
control is a separately proved continuum limit, not an interpretation of the
regulator as already continuum.

Retrieval separated this packet from K123's global fixed-point/CE complex,
K77's supplied Maxwell functional control, K91's finite quotient controls, and
the earlier source-native Gauss-law comparators. None couples K123's exact
eight charge vectors to a spatial local gauge regulator and proves its
constraint, domain, holonomy, affinity, and nonselection boundaries together.

## 1. The K123 charge lattice localizes exactly

Choose one of the nine K115 states as root `v_*`. Give the remaining eight
states the standard basis charges

```text
q(v_*)=0,                 q(v_a)=e_a in Z^8.             (1)
```

For every oriented transition `e:u->v`, define

```text
b_e=q(v)-q(u).                                               (2)
```

The 18 vectors span `Z^8`: the transition graph is connected and its incidence
matrix has rank eight. Let the system transition `T_e=|v><u|` carry charge
`b_e`, and let the corresponding CAR creation field carry charge `-b_e`.
At the defect site `x=0`,

```text
D_e=T_e a_e(0)^*                                             (3)
```

is neutral under an independently chosen `U(1)^8` phase at that spatial site.
The adjoint pair `g_e D_e + conjugate(g_e) D_e^*` is therefore both
self-adjoint and locally gauge invariant. Compact smearing may replace the
single lattice field without changing this charge identity.

Equation (3) is a conditional charge assignment. K123 fixes the abstract
incidence charges, but no source or GU action selects the root, normalization,
compact gauge group, lattice, or coupling constants.

## 2. Spatial links, Gauss law and a nonempty physical sector

Take a periodic spatial lattice `Lambda=Z/NZ`, `N>=2`. For every link
`x->x+1` and charge direction `a=1,...,8`, use a compact rotor

```text
U_(x,a) on L2(U(1)),       E_(x,a)=-i d/dphi,
[E_(x,a),U_(x,a)]=U_(x,a).                                (4)
```

If CAR species `e` has charge `c_e=-b_e`, its covariant hop is

```text
a_e(x+1)^* [product_a U_(x,a)^(c_e,a)] a_e(x).             (5)
```

Under `U_(x,a) -> exp(i(theta_(x,a)-theta_(x+1,a)))U_(x,a)`,
the three phases in (5) cancel coefficientwise. With `rho_(x,a)` the CAR
charge density and `Q_a` the finite-system charge, define

```text
G_(x,a)=E_(x,a)-E_(x-1,a)+rho_(x,a)+delta_(x,0) Q_a.        (6)
```

All `8N` generators commute. Their sum over `x` is the total matter charge, so
periodic Gauss solvability requires global neutrality; this is a constraint,
not an automatically supplied background. The root-system/CAR vacuum with
zero electric flux is neutral, so the joint kernel is nonempty. Acting with a
neutral defect pair preserves it.

Integer spectra and compactness give the orthogonal group-average projector

```text
P_phys = integral_[U(1)^(8N)] exp(i sum_(x,a) theta_(x,a)G_(x,a)) dtheta,
im(P_phys)=intersection_(x,a) ker G_(x,a).                 (7)
```

Thus the regulator has an exact Dirac physical sector. For anticommuting
ghosts `c_(x,a)`,

```text
Omega=sum_(x,a)c_(x,a)G_(x,a),             Omega^2=0,       (8)
```

because the constraints are abelian. This is a finite-lattice Hamiltonian
BFV/BRST complex and Dirac quotient. It is not a continuum Lagrangian BV
master action, a boundary BFV charge derived from a source action, or a
physical GU cohomology theorem.

## 3. The regulated interacting Hamiltonian has an owned domain

On the finite lattice let

```text
H_E=(kappa/2) sum_(x,a) E_(x,a)^2,       kappa>0.           (9)
```

The covariant CAR hopping is bounded: the lattice CAR algebra is finite
dimensional and every link monomial is unitary. The compactly smeared defect
term remains bounded by K123's CAR estimate. Hence

```text
H=H_E+H_hop+H_defect                                      (10)
```

is self-adjoint on `D(H_E)` and bounded below by the bounded-perturbation
theorem. Equations (3), (5), and (9) commute with every Gauss generator, so
`H` preserves (7). This closes a real operator-domain gap at finite regulator.

It does not close the continuum limit. Uniform estimates in lattice spacing,
renormalization of the defect, a continuum Gauss-domain theorem, causal local
net, gauge fixing/ghost measure, and an interacting nonequilibrium stationary
state are absent.

## 4. Gauge fixing exposes rather than removes the new imports

On the spatial circle, gauge transformations can set a spanning set of
`N-1` links to identity in each charge direction, but one Wilson holonomy per
`U(1)` remains. There are eight spatial holonomies. They are not K123's ten
transition-graph cycle phases: the former come from the spatial circle and the
latter from `H_1` of the 18-edge state-transition graph.

Freezing every link to identity, selecting zero electric flux, discarding
`H_E`, and fixing the gauge coefficients recovers the algebraic K123 defect
monomials. That is a supplied gauge slice and frozen sector, not a proof that
the lattice theory is equivalent to K123 or that K123 selected its gauge
completion. Gauge symmetry alone fixes none of `kappa`, the hopping
coefficients, boundary condition, theta/electric sector, compact charge
normalization, or interacting state.

## 5. Gauge covariance does not equilibrate the defect or derive Born

The link factors in (5) and local gauge phases have unit modulus. They do not
alter the K117/K123 selected square's rate-modulus ratio

```text
product_forward/product_reverse = 6561/256.                (11)
```

The real modular-affinity period therefore remains nonzero. Local compact
gauge covariance neither turns it into a phase holonomy nor creates a single
equilibrium detailed-balance owner. Likewise, (7) supplies a mathematical
physical subspace for this regulated model, but it does not select an incoming
state, detector effects, or the rule that physical probabilities are state-on-
effect evaluations.

## Inline postflight bookend

- **Strongest construction:** K123's eight incidence charges now act as exact
  local spatial lattice charges with compact links, commuting Gauss law,
  nonempty group-averaged Dirac sector and a Gauss-preserving self-adjoint
  interacting Hamiltonian.
- **Strongest type correction:** eight spacetime gauge directions, ten
  transition-graph cycle directions, eight spatial-circle holonomies and the
  real modular-affinity cochain are four different objects.
- **Strongest nonselection result:** gauge covariance does not choose the
  regulator, charge normalization, electric/hopping coefficients, boundary or
  flux sector, state, effects, or source action.
- **Strongest refused overclaim:** the finite Hamiltonian BFV control is not a
  continuum local gauge/BV-BFV/AQFT theory or a GU-native physical quotient.
- **Weakest seam:** exact finite charge and constraint algebra is
  machine-certified; continuum removal, interacting NESS and physical
  state/effect semantics have no theorem here.

All five admitted arcs completed. The result advances K123 from global
fixed-point symmetry to one exact spatially local regulated gauge completion,
while making the regulator, global-neutrality, holonomy, continuum, source,
and probability imports explicit.

## Next condition

Construct a controlled continuum limit with a renormalized unsmeared defect,
common self-adjoint Gauss domain, local gauge fixing/BV master action, causal
observable net and interacting nonequilibrium state. Independently require an
actual source/GU action to select the charge embedding, coefficients and
boundary sector before any GU-native, detector, Born, prediction or
confirmation claim.

## Reproduction

```bash
python3 tests/channel-swings/k124_k123_spatial_u1_8_lattice_gauge_bfv_completion_probe.py
python3 tests/channel-swings/k124_k123_spatial_u1_8_lattice_gauge_bfv_completion_probe.py --selftest
```
