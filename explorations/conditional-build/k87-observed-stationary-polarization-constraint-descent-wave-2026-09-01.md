---
title: "K87 observed stationary polarization and constraint descent wave"
status: active_research
doc_type: reverse_scaffold_stationary_polarization_constraint_result
created: 2026-09-01
date: 2026-09-01
claim_ceiling: exact positive-frequency complex-structure and quasifree-ground-covariance selection for a positive gapped stationary quadratic reduction of the repository-owned K77/K85/K86 candidate, plus exact finite gauge, constraint and domain descent conditions; no source-owned full action, full interacting polarization, complete BFV complex, continuum Hadamard state, Born rule, prediction, confirmation, or verdict
manifest: lab/process/k87-observed-stationary-polarization-constraint-descent-wave.json
probe: tests/channel-swings/k87_observed_stationary_polarization_constraint_descent_probe.py
---

# K87 observed stationary polarization and constraint descent wave

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
result: exact stationary positive-frequency selector, positive majorant, quasifree covariance and finite quotient-domain descent conditions for the repository-owned K77/K85/K86 candidate
carrier: reduced real Cauchy phase space W960+W960 and an exact finite ambient-plus-gauge control LAYER=observed CHIRALITY=N/A
pairing: K86 even symplectic form and the selected positive compatible majorant ON=repository_owned_reduced_phase_space
real_structure: real classical phase space complexified only after the selected J
grading: even stationary phase space; distinct from BRST ghost and BV antifield grading
action_owner: repository-construction
target: stationary dynamics to complex polarization, covariance and physical quotient conditions MAP-TYPE=quotient
```

## Result first

K86 made compatible complex polarizations available but did not select one.
Stationary positive dynamics closes part of that gap. On a reduced real
symplectic phase space with positive gapped quadratic Hamiltonian, write

```text
A = [ 0       I ],              -A^2 = [ Omega^2    0 ],
    [-Omega^2 0 ]                       [ 0       Omega^2 ] .       (1)
```

For positive `Omega`, the spectral polar formula

```text
J = -A(-A^2)^(-1/2)
  = [ 0          -Omega^(-1) ],                              (2)
    [ Omega       0          ]
```

obeys `J^2=-1`, commutes with `A`, and gives the positive compatible
majorant

```text
g(u,v)=omega(u,Jv),     g = diag(Omega,Omega^(-1)).           (3)
```

The associated pure quasifree ground covariance is

```text
C = (1/2) diag(Omega^(-1),Omega),    (2 C omega)^2=-1.        (4)
```

Thus an owned stationary flow, positive spectral gap, time orientation and
ground-state principle do more than K86's arbitrary Fock choice: they
determine one spectral complex structure and its Gaussian covariance for the
quadratic reduction. They do not turn the full interacting theory into a
quasifree theory. Reversing the time orientation sends `A` to `-A` and `J` to
`-J`; relative to the fixed symplectic orientation the majorant changes sign.
Time orientation is therefore load-bearing, not notation.

## Descent is a separate theorem

The spectral formula lives on the reduced physical carrier only when the
dynamics actually descends. With ambient representatives, quotient map `P`,
gauge image `K`, constraint kernel `Z`, and physical boundary/Green domain
`D`, the finite exact packet checks

```text
P A_ambient = A_reduced P,       A_ambient K subset K,
P J_ambient = J_reduced P,       J_ambient K subset K,        (5)
A Z subset Z,                    J D = D.                     (6)
```

Equations (5)--(6) instantiate the relevant part of VRS-4 rather than citing
its name. A positive two-frequency control satisfies all conditions. Three
independent mutations show why they cannot be collapsed: a generator that
leaks a gauge vector into a physical direction has no quotient evolution; a
generator that leaks the constraint kernel has no physical dynamics; and a
domain that fixes `q` without the conjugate `p` is not `J`-invariant. A zero
frequency separately destroys the inverse square root and the ground
covariance.

The exact probe passes `25/25`; its hostile selftest catches `18/18`
mutations. The finite model certifies the algebraic ownership conditions. It
does not prove closed range, microlocal spectrum, Hadamard form, continuum
constraint propagation or a complete interacting BFV complex on the full
K77 carrier.

## Hostile review and boundary

The strongest overclaim would call (2) a source-selected GU vacuum. It is a
repository-owned spectral selector on a positive stationary quadratic
reduction. The full GU carrier is indefinite and the source-owned complete
action/background is absent. The strongest contrary cases are zero/unstable
spectrum, time reversal at fixed symplectic orientation, and failure of any
commuting square in (5)--(6). The weakest reproducibility seam is the jump
from exact finite quotient controls to closed infinite-dimensional domains.

No Born rule follows from a covariance. No local observable net is selected.
No delayed-choice entanglement-swapping datum is evaluated. No prediction,
confirmation, canon or public posture moves.

## Next condition

Supply an action-owned stationary full-carrier operator with a common closed
constraint/BFV/Green domain and test the spectral selector there. Separately,
even if the selected quadratic state survives, determine whether the causal
action and observation map select the local observable algebras whose
correlations are physically compared.
