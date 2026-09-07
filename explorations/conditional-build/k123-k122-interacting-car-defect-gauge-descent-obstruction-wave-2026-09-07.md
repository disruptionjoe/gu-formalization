---
title: "K123 K122 interacting CAR-defect gauge-descent obstruction wave"
status: active_research
doc_type: reverse_scaffold_interacting_car_defect_result
created: 2026-09-07
date: 2026-09-07
target_claim: INTERNAL_TARGET:K122_INTERACTING_DEFECT_NET_AND_PHYSICAL_GAUGE_BV_QUOTIENT
claim_ceiling: exact repository-owned defect phase-descent theorem, ten-dimensional cycle obstruction, bounded compactly smeared interacting CAR dynamics, preserved eight-dimensional global fixed-point algebra and degree-zero abelian BRST identification; no source/GU ownership, unsmeared point defect, full interacting Haag-Kastler theory, interacting NESS, local gauge/Gauss-law/BV-BFV quotient, Born derivation, prediction, confirmation or holdout credit follows
manifest: lab/process/k123-k122-interacting-car-defect-gauge-descent-obstruction-wave.json
probe: tests/channel-swings/k123_k122_interacting_car_defect_gauge_descent_obstruction_probe.py
---

# K123 K122 interacting CAR-defect gauge-descent obstruction wave

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
result: exact defect phase-symmetry descent and bounded interacting cutoff CAR dynamics
carrier: nine-state K115 system tensor 18 compactly smeared species of full left-right massless 1+1-dimensional Dirac CAR fields LAYER=observed CHIRALITY=S-FULL-DIRAC
pairing: C-star adjoint and norm, grand-canonical incoming quasifree functionals and finite-system trace/effect pairing ON=repository_owned_interacting_cutoff_control
real_structure: CAR adjoint, complex conjugation of spinor test functions and finite-system matrix adjoint
grading: fermion parity, eight vertex-phase charges and degree-one abelian Chevalley-Eilenberg ghosts; no source BV, BFV or local gauge-field grading
action_owner: repository-construction
target: interaction-compatible phase quotient, cycle obstruction, bounded defect dynamics and invariant effect algebra MAP-TYPE=evaluation
```

Scope: this result binds the repository-selected K115/K122 graph and compactly
smeared CAR defect model. It does not bind Weinstein's action, a GU-native
quantization, an unsmeared point interaction, or a physical gauge quotient.

## Inline preflight bookend

The rebuilt frontier contained five substantial arcs: compute which of K122's
18 free species phases survive the defect; locate K117's affinity obstruction
in the graph-cycle sector; construct the resulting bounded interacting
dynamics; type its global fixed-point/BRST quotient; and test whether detector
effects survive without importing Born semantics. The phase-lift computation
is the cheap route-changing discriminator. Its `8+10` split releases all four
successors, so they form one Big Wave.

The primary route is graph incidence plus bounded CAR perturbation theory. A
declaration that all `U(1)^18` phases survive was rejected because the system
transition operators also transform. A point-defect construction was rejected
because K122 supplies no renormalized boundary field. A physical gauge/BV
claim was rejected because no local connection, Gauss constraint or gauge-
fixing data exist. The fallback, if the phase lift failed, was the parity-even
subnet alone.

Retrieval found K97's CAR KMS state, K99's product-KMS stream, K117's scalar
cycle affinity, K119's collision tape, K120's free Fock continuum, K121's
bosonic boundary net and K122's free `U(1)^18` reservoir subnet. No prior packet
computes the interaction-compatible torus, its ten cycle obstructions, a
bounded interacting cocycle and the global-BRST ceiling together.

## 1. The defect reduces `U(1)^18` to a vertex-potential torus

The K115 states are the nine vertices `v=(x,r)` of `K3 square K3`. Its 18
undirected edges consist of nine base changes at fixed record and nine record
changes at fixed base. Choose one orientation for every edge and let

```text
B : R^18 -> R^9
```

be the oriented incidence matrix. The graph is connected, hence

```text
rank(B)=9-1=8,       dim ker(B)=18-8=10.                 (1)
```

For an oriented edge `e:i->j`, the K122 interaction monomial is

```text
V_e tensor a_e(h_e)^* ,       V_e=|j><i|.               (2)
```

Give the system basis vector `|i>` phase `phi_i`. Then `V_e` has phase
`phi_j-phi_i`. Equation (2) is invariant exactly when the lead creation field
has the opposite phase. Thus a vector of 18 lead phases lifts diagonally to the
nine-state system exactly when it is the coboundary `B^T phi`. The constant
part of `phi` acts trivially, so the connected liftable torus has dimension
eight.

The ten-dimensional quotient of edge phases by vertex potentials is the graph
cycle space. A phase with nonzero period around a cycle cannot be cancelled by
any diagonal system rephasing. Therefore K122's free `U(1)^18` action does not
survive the continuously coupled defect. The exact survivor is the image of
the vertex torus `U(1)^9/U(1)` within the stated diagonal-lift class. This is a
defect symmetry-breaking theorem, not an anomaly calculation.

## 2. Nonequilibrium affinity occupies the same cycle sector, at a different type

For oriented edges define the real modular-affinity cochain

```text
A_e = log(q_e/q_reverse(e)).                              (3)
```

On the square

```text
(0,0) -> (1,0) -> (1,1) -> (0,1) -> (0,0),              (4)
```

the base rates cancel and the two favorable versus unfavorable record rates
give

```text
product_forward/product_reverse=(81/16)^2=6561/256.      (5)
```

Hence the period of (3) around (4) is `log(6561/256)`, not zero. The affinity
is not a vertex potential, which re-expresses K117's detailed-balance
obstruction in the 10-dimensional graph `H^1` sector.

The shared graph location does not identify types. Compact phase angles
govern automorphisms of the field algebra; real modular affinities govern
incoming state ratios and entropy flow. K123 proves that both have cycle
period tests. It does not turn one into the other or derive either from GU.

## 3. A bounded smeared interacting defect dynamics

Let `h_e` be compactly supported `L2` spinor form factors near the defect. CAR
boundedness gives

```text
||a_e(h_e)|| = ||h_e||_2.                                (6)
```

On `M9 tensor CAR(direct-sum_e H_e)`, take the constant perturbation

```text
V = sum_e g_e [V_e tensor a_e(h_e)^*
                  + V_e^* tensor a_e(h_e)].              (7)
```

It is bounded and self-adjoint, with

```text
||V|| <= 2 sum_e |g_e| ||h_e||_2.                        (8)
```

If `alpha_t^0` is the free CAR plus finite-system dynamics, the Dyson cocycle

```text
U_V(t)=1+sum_(n>=1)(-i)^n integral_ordered
                 alpha_t1^0(V)...alpha_tn^0(V) dt...     (9)
```

converges in norm because its `n`th term is at most
`(|t| ||V||)^n/n!`. Then

```text
alpha_t^V(A)=U_V(t)^* alpha_t^0(A) U_V(t)                (10)
```

is a well-defined interacting C-star dynamics. Every summand in (7) is neutral
under the eight-dimensional vertex torus, so (10) commutes with that action
and preserves its fixed-point algebra.

This is the strongest construction licensed by the present inputs. Smearing
is essential: no pointlike boundary operator or renormalized zero-width limit
is supplied. K123 owns neither a complete Poincare-covariant interacting
Haag-Kastler net nor a finite-coupling nonequilibrium stationary state. K115
remains the controlled Davies/white-noise reduced limit inherited from K122.

## 4. Fixed points give a global BRST boundary, not physical gauge BV

Let `delta_a`, `a=1,...,8`, be the commuting infinitesimal derivations of the
vertex torus and let `c^a` be degree-one anticommuting ghosts. The abelian
Chevalley-Eilenberg differential is

```text
s A = sum_a c^a delta_a(A),       s c^a=0.               (11)
```

Commutativity of the `delta_a` and antisymmetry of the ghosts give `s^2=0`.
At degree zero,

```text
H^0(s)=intersection_a ker(delta_a)=A^(U(1)^8).           (12)
```

Equation (12) is a precise global symmetry/BRST statement. It is not a local
gauge theory. There is no spacetime-dependent gauge parameter, connection,
curvature, Gauss-law constraint, gauge fixing, antifield master action or BFV
boundary charge. Calling (12) a physical BV-BFV quotient would add structures
that the model does not contain.

## 5. Invariant effects survive; physical detector semantics do not

Every detector spectral projection `P_i=|i><i|` is neutral under vertex
rephasing. The dressed transition-field monomials in (2) are neutral as well.
The global fixed-point algebra therefore contains both detector propositions
and the interaction that changes them. Positive normalized states restricted
to this algebra pair with `P_i` in `[0,1]`.

This is a mathematical invariant effect algebra. It does not select which
projections a physical detector realizes, construct the interacting incoming
or steady state, or derive why state-on-effect evaluation is nature's
probability law. Born and detector ownership remain open.

## Inline postflight bookend

- **Strongest correction to K122:** the free `U(1)^18` fixed-point subnet is not
  interaction-stable. Only the diagonal-liftable eight-dimensional vertex
  torus survives the defect; ten cycle-phase directions are broken.
- **Strongest structural relation:** phase nonliftability and nonequilibrium
  affinity both live in graph cycle space, but remain different typed objects.
- **Strongest construction:** compact smearing makes the interaction bounded,
  self-adjoint and norm-Dyson integrable while preserving the reduced fixed
  points.
- **Strongest refused overclaim:** global fixed points and degree-zero
  Chevalley-Eilenberg cohomology are not a physical gauge/BV-BFV quotient.
- **Weakest seam:** the certificate checks finite graph, charge, rate and
  majorant identities. The C-star perturbation theorem is invoked at its
  standard bounded scope; no point-limit or interacting NESS theorem is
  machine-certified.

All five admitted arcs completed. The result advances from a free reservoir
net to a controlled interacting cutoff dynamics and determines exactly which
phase quotient survives, while exposing the new local-gauge and point-defect
requirements rather than silently assuming them.

## Next condition

Supply an actual source-owned GU action whose fields and variation select the
lead modular offsets, form factors and defect charges. Then construct local
gauge fields, Gauss law, a physical BV-BFV quotient, an unsmeared interacting
net and its nonequilibrium state before testing detector or Born semantics.

## Reproduction

```bash
python3 tests/channel-swings/k123_k122_interacting_car_defect_gauge_descent_obstruction_probe.py
python3 tests/channel-swings/k123_k122_interacting_car_defect_gauge_descent_obstruction_probe.py --selftest
```
