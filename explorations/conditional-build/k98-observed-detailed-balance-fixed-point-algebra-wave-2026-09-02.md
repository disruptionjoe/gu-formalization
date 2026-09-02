---
title: "K98 observed detailed-balance fixed-point algebra wave"
status: active_research
doc_type: reverse_scaffold_detailed_balance_fixed_point_algebra_result
created: 2026-09-02
date: 2026-09-02
target_claim: INTERNAL_TARGET:K97_GIBBS_REVERSIBLE_DYNAMICS_RECORD_RANGE_SELECTOR
target_claim_verdict: EXPLICIT_REVERSIBLE_FAMILY_FIXED_ALGEBRA_CLASSIFIED_GRAPH_SELECTION_OPEN
claim_ceiling: exact fixed-point algebra, GNS detailed balance, energy covariance and semigroup-limit theorem for one explicit finite-dimensional pure-dephasing plus reversible-jump family, with a complete n=3 partition census; no classification of all quantum detailed-balance semigroups and no derivation of the Hamiltonian, Gibbs state, dephasing, graph, energy basis, classicality, Born rule, physical record selection, source dynamics, continuum theory, prediction or verdict
manifest: lab/process/k98-observed-detailed-balance-fixed-point-algebra-wave.json
probe: tests/channel-swings/k98_observed_detailed_balance_fixed_point_algebra_probe.py
---

# K98 observed detailed-balance fixed-point algebra wave

> **GU-COMPARATOR-ROUTING — scope before inference.** This artifact contains or
> borders a conventional particle-physics comparator. Any result about a
> standard Higgs/VEV, ordinary family index or net chirality, SO(10) `126`
> Majorana mechanism, anomaly selector, VEV-only breaking or familiar vector-
> mass route binds only that named model. It is not evidence for or against
> Weinstein's source-native mechanism without an explicit typed bridge. Read
> `lab/methods/source-native-comparator-routing.md` and follow its source-native
> pointers before reusing this result.

Classification: `BRIDGE_OR_SEMANTIC_BOUNDARY`

```gu-typed-objects
result: explicit Gibbs-reversible dephasing-plus-jump semigroup realizes every K97 energy-partition expectation as its exact long-time map
carrier: M_n(C), exactly censused at n=3 with rho=diag(4,2,1)/7 LAYER=observed CHIRALITY=N/A
pairing: imported GNS pairing <A,B>_rho=Tr(rho A*B) and imported state/Born reading ON=repository_owned_reversible_semigroup_control
real_structure: matrix adjoint and standard complex conjugation
grading: energy spectral projections and imported graph-component partition; no source BV, BFV, ghost or CAR grading
action_owner: repository-construction
target: K97 conditional energy-partition expectation as a fixed-point and asymptotic map MAP-TYPE=evaluation
```

Scope: this theorem covers one explicit finite-dimensional Heisenberg-picture
Lindblad family. It proves detailed balance, covariance, fixed points and the
norm limit for that family. It does **not** classify all quantum detailed-
balance semigroups or derive any physical graph or record interpretation.

## Inline preflight bookend

The route-changing census covered K97 energy-partition expectations, quantum
detailed balance, GNS symmetry, Davies-style reversible jumps, graph
Laplacians, decoherence-free and fixed-point algebras, covariance, isolated
components and primitive versus reducible semigroups. The smallest exact test
is constructive: ask whether one reversible Lindblad family realizes all K97
partition maps and whether detailed balance itself chooses among them.

Retrieval found K97's complete abelian conditional-expectation classification,
K96's degenerate `Z/X` dephasing ambiguity, K95's supplied amplitude-damping
stabilizer and K97's local CAR asymptotic instrument. It found no repository
artifact proving that a single Gibbs-reversible graph family realizes every
K97 `E_pi` with sharp connected/no-edge/intermediate fixed algebras. Standard
finite Markov reversibility and Lindblad facts receive no literature-novelty
claim. The delayed-choice holdout remains reserved and unscored.

## Explicit reversible family

Import a simple Hamiltonian and faithful Gibbs density

```text
H=sum_i epsilon_i P_i,            rho=sum_i r_i P_i,
r_i>0, sum_i r_i=1,               Delta_H(A)=sum_i P_i A P_i.       (1)
```

Let `G` be an imported undirected graph on the energy labels, with connected
components `pi`. Give every edge a symmetric positive conductance
`c_ij=c_ji>0`, define

```text
k_ij=c_ij/r_i,                    L_ij=sqrt(k_ij)|j><i|,             (2)
r_i k_ij=c_ij=r_j k_ji,                                                   (3)
```

and include both orientations of every edge. For an imported `kappa>0`, set

```text
L_G(A)=kappa(Delta_H(A)-A)
      +sum_(i->j) [L_ij* A L_ij-(1/2){L_ij*L_ij,A}].                (4)
```

Equation (4) is a unital completely positive Markov generator in the
Heisenberg picture. The pure energy-dephasing term is load-bearing when graph
vertices are isolated: if `G` has no edges, it makes the limit `Delta_H`;
without it the generator is zero and the whole `M_n(C)` remains fixed.

## GNS detailed balance and energy covariance

Use the imported GNS inner product

```text
<A,B>_rho=Tr(rho A*B).                                                (5)
```

On diagonal matrices, (4) is the classical generator

```text
(Kf)_i=sum_j k_ij(f_j-f_i).                                          (6)
```

Equation (3) makes `K` self-adjoint in `l2(r)`. On every off-diagonal matrix
unit `E_ab`, the jump gain terms vanish and

```text
L_G(E_ab)=-[kappa+(q_a+q_b)/2]E_ab,   q_i=sum_j k_ij.                 (7)
```

The diagonal and off-diagonal sectors are GNS orthogonal, and (7) has real
coefficients. Therefore the full dissipative generator is GNS self-adjoint:
this family satisfies GNS detailed balance with respect to `rho`.

For `alpha_t(A)=exp(itH)Aexp(-itH)`, each `L_ij` acquires only the phase
`exp(it(epsilon_j-epsilon_i))`. Its Lindblad term is phase invariant, and
`Delta_H` is covariant. Hence

```text
L_G alpha_t=alpha_t L_G                                                    (8)
```

for every real `t`. No energy-gap nonresonance is required.

## Fixed-point algebra theorem

Let `Q_B=sum_(i in B)P_i` and

```text
N_pi={sum_(B in pi) a_B Q_B}.                                          (9)
```

**Theorem.** The fixed algebra of `exp(tL_G)` is exactly `N_pi`.

**Proof.** GNS symmetry gives a nonpositive Dirichlet form. Its dephasing
part vanishes only on energy-diagonal matrices. Restricted to that diagonal,
the graph part vanishes exactly when `f_i=f_j` on every edge, hence exactly
when `f` is constant on each connected component. Thus the kernel is (9),
and in finite dimension the generator and semigroup have the same fixed
space. Conversely every `Q_B` is visibly killed by (4). This also proves that
the fixed space is an original-product C-star algebra, not merely an operator
system.

The endpoints are sharp:

- connected `G` gives `Fix=C I`;
- no edges gives `Fix=D_H`, with the dephasing term eliminating every energy
  off-diagonal;
- intermediate components give a proper coarse partition algebra.

## Exact K97 semigroup limit

For the complete graph inside each component, choose

```text
c_ij=r_i r_j,                    k_ij=r_j.                             (10)
```

If `r_B=sum_(i in B)r_i` and
`a_B=sum_(i in B)r_i A_ii/r_B`, then (6) becomes

```text
(Kf)_i=r_B(a_B-f_i),
A_ii(t)=a_B+exp(-r_B t)(A_ii-a_B).                                    (11)
```

Equation (7) kills every off-diagonal exponentially because `kappa>0`.
Consequently the norm limit is exactly

```text
lim_(t->infinity) exp(tL_G)(A)
 =sum_(B in pi) [Tr(rho Q_B A Q_B)/r_B]Q_B
 =E_pi(A),                                                               (12)
```

the K97 Gibbs-preserving partition expectation—not merely a map with the same
range.

## Exact three-level census

Take the K97 weights `(r_0,r_1,r_2)=(4,2,1)/7`. The possible conductances are

```text
c_01=8/49,                 c_02=4/49,                 c_12=2/49,       (13)
```

and every active rate is `k_ij=r_j`. All five partitions occur:

| `pi` | active component cliques | `Fix` | dimension | limit |
| --- | --- | --- | ---: | --- |
| `{{0,1,2}}` | `012` | `C I` | 1 | `phi_rho(A)I` |
| `{{0},{1,2}}` | `12` | `span{P_0,P_1+P_2}` | 2 | K97 `E_0|12` |
| `{{1},{0,2}}` | `02` | `span{P_1,P_0+P_2}` | 2 | K97 `E_1|02` |
| `{{2},{0,1}}` | `01` | `span{P_2,P_0+P_1}` | 2 | K97 `E_2|01` |
| `{{0},{1},{2}}` | none | `D_H` | 3 | `Delta_H` |

For example, `E_0|12(P_1)=(2/3)(P_1+P_2)`. The exact probe checks every
matrix unit, all five kernel dimensions, GNS symmetry, Gibbs invariance,
Bohr-block covariance and the full spectral-projection identity.

## Sharp nonselection

Holding `H`, `rho` and `kappa` fixed while changing only the imported graph
produces scalar, three distinct coarse and fully diagonal fixed algebras. Thus
GNS detailed balance and continuous energy covariance do not select a record
algebra. They transmit the graph's connected-component choice into the fixed
algebra. This is the constructive counterpart of K97's partition
classification, not a physical graph selector.

## Owner accounting and fences

Repository-owned here are the explicit family (4), its GNS detailed-balance
and covariance proof, `Fix=N_pi`, the exact limit (12), the five-partition
census and the sharp nonselection theorem. Imported are `H`, the Gibbs state,
pure energy dephasing, graph and conductances, energy basis, classical-record
interpretation and state/Born pairing. The source-selected owner count is
zero.

No claim is made to classify all QDB semigroups, derive `H` or the Gibbs
principle, select the dephasing or graph, derive an energy basis or
classicality, derive the Born rule, construct a source dynamics or continuum
AQFT/microlocal state, score a holdout, make a prediction, confirm GU or
combine this packet with another packet as though their imported owners were
shared.

## Maximum licensed conclusion

One explicit finite Gibbs-reversible Lindblad family realizes every K97
partition expectation as its exact asymptotic map, and its fixed algebra is
exactly the graph-component algebra. Connected, edgeless and intermediate
graphs give respectively scalar, energy-diagonal and coarse fixed algebras.
Detailed balance and covariance therefore do not select among them; the graph
and pure dephasing remain supplied owners.

## Inline postflight bookend

- Strongest overclaim: saying quantum detailed balance selects classical
  records. This family only maps an imported graph and energy dephasing into a
  fixed algebra.
- Strongest contrary construction: the same `H`, `rho` and `kappa` support all
  five `n=3` partition limits, from `C I` through three coarse algebras to
  `D_H`.
- Weakest reproducibility seam: the general theorem is an exact matrix-unit
  proof; the exhaustive three-level probe is regression evidence, not a
  classification of arbitrary QDB generators.

The probe runs positive controls before result checks. Its hostile selftest
plants missing partitions, zero dephasing, broken reversibility, one-way
edges, wrong fixed dimensions, wrong limits, broken covariance, all-QDB
promotion, owner theft, classicality/Born promotion and holdout leakage. No
source, continuum, prediction, confirmation, canon, paper or held-out status
moves.

## Next condition

Derive the graph and dephasing structure from a source-owned local interaction
or reservoir, rather than stipulating them, and show that the resulting
physical reduced instrument retains the fixed algebra and K97 limit on one
common domain.
