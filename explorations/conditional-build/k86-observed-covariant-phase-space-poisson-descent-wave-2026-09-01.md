---
title: "K86 observed covariant phase-space Poisson descent wave"
status: active_research
doc_type: reverse_scaffold_repository_owned_covariant_phase_space_result
created: 2026-09-01
date: 2026-09-01
claim_ceiling: exact covariant presymplectic-current and reduced even-Poisson-bracket descent for the repository-owned K77/K85 interacting quotient candidate on compact or zero-flux Cauchy support; no source-owned GU or gimmel action, global nonlinear solution-space theorem, Peierls construction, gauge fixing, quantum algebra, prediction, confirmation, or verdict
manifest: lab/process/k86-observed-covariant-phase-space-poisson-descent-wave.json
probe: tests/channel-swings/k86_observed_covariant_phase_space_poisson_descent_probe.py
---

# K86 observed covariant phase-space Poisson descent wave

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
result: exact covariant presymplectic current, gauge radical and nondegenerate quotient Poisson bracket for the repository-owned K77/K85 interacting candidate
carrier: ambient Cauchy variations in V1920+V1920 with physical quotient Cauchy data in W960+W960 on a compact or zero-flux hypersurface LAYER=observed CHIRALITY=N/A
pairing: positive internal form H on W960 and its induced canonical symplectic form on quotient Cauchy data ON=repository_owned_candidate_phase_space
real_structure: real scalar quotient multiplet with real canonical Cauchy data
grading: even classical covariant phase space; distinct from the odd BV antibracket and ghost grading
action_owner: repository-construction
target: action-derived presymplectic current, exact ambient radical and reduced Poisson bracket MAP-TYPE=quotient
```

## Action-derived current

Retain the K85 repository-owned matter action, with `psi=P Phi`, positive
internal form `H`, and arbitrary smooth potential `V(psi)`:

```text
S_m[Phi,e] = integral e [1/2 H_AB g^munu d_mu psi^A d_nu psi^B - V(psi)]. (1)
```

The first variation supplies the matter presymplectic potential current

```text
theta^mu(delta psi) = H_AB d^mu psi^B delta psi^A.       (2)
```

Antisymmetrizing a second variation gives

```text
omega^mu(delta_1,delta_2)
 = H_AB [delta_1 psi^A d^mu delta_2 psi^B
        -delta_2 psi^A d^mu delta_1 psi^B].             (3)
```

The potential contributes a symmetric Hessian to the linearized Euler
operator and therefore cancels from (3). For background solutions and
linearized solutions, the standard Green identity gives
`nabla_mu omega^mu=0`. On `T3`, compact support, or any admitted boundary
condition with zero symplectic flux, the integral of (3) is independent of the
Cauchy hypersurface. A nonzero open-boundary flux is an explicit control and
is not silently discarded.

## Exact radical and reduced bracket

Pull (3) back to the ambient representative by `delta psi=P delta Phi`. On a
Cauchy surface with momentum `pi=H d_n psi`,

```text
Omega_ambient((delta Phi,delta dotPhi),(delta' Phi,delta' dotPhi))
 = integral [H(P delta Phi,P delta' dotPhi)
            -H(P delta' Phi,P delta dotPhi)].           (4)
```

Every `K960` variation in either Cauchy slot lies in the radical. Conversely,
positivity and nondegeneracy of `H` imply that a radical vector has both
projected slots zero. Hence

```text
rad Omega_ambient = K960 direct-sum K960,
(V/K) direct-sum (V/K) = W960 direct-sum W960,           (5)
```

and the reduced form is nondegenerate. For `H`-orthonormal mode coordinates,

```text
{q_a,q_b}=0,  {p_a,p_b}=0,  {q_a,p_b}=delta_ab.         (6)
```

With general `H`, the last matrix is `H^{-1}`. The mass and quartic coupling
change the Hamiltonian but not (2)--(6). Thus the missing even bracket is now
owned for this candidate; it is not manufactured by the earlier odd minimal
BV pairing.

## Boundary and ownership controls

Three premises are load-bearing. A degenerate `H` leaves additional physical
radicals. Nonzero boundary flux makes the hypersurface integral evolve. A
representative-dependent potential destroys the `K960` gauge radical. The
exact probe exercises each failure and verifies the rank schedule
`3840 -> radical 1920 -> reduced 1920` on the full carrier, using a finite
rank model only for exact arithmetic.

The strongest overclaim would call (1) Weinstein's source action or call (6)
the physical GU quantum commutator. The strongest contrary cases are a
degenerate internal form and an open symplectic boundary. The weakest seam is
the absence of a source-owned full action and of a selected analytic
quantization/state. No prediction, confirmation, held-out score, canon or
public posture moves.

## Next condition

Quantize at least one explicitly selected finite set of reduced modes in a
stated representation and domain, construct a noncommutative bounded
observable algebra and normalized positive states, and test the classical,
intermediate and Tsirelson correlation faces. Keep existence of a
repository-selected quantization separate from source selection of a physical
state or measurement map.
