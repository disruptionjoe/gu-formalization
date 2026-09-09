---
title: "K173 two-graph tail obstruction wave"
document_role: active_research
doc_type: conditional_native_K139_K172_same_graph_tail_obstruction_and_fractional_domain_replacement_result
created: 2026-09-09
date: 2026-09-09
claim_ceiling: exact repository-owned topology correction for the K139--K172 signed point control showing that the free-energy graph has no finite G graph norm while the particle-number graph has no finite W graph-to-Hilbert bound, so their constants cannot be combined in K172; a quarter-energy candidate controls the point vector and named one-bath logarithmic multiplier only, while complete Fock constants, all-order action tail, R_ref residual, complement or flux floor and scalar-center left floor remain absent, so no native K152 interval, physical/source selection, Born derivation, prediction or confirmation follows
manifest: lab/process/k173-two-graph-tail-obstruction-wave.json
solver: tests/channel-swings/k173_two_graph_tail_obstruction.py
probe: tests/channel-swings/k173_two_graph_tail_obstruction_probe.py
target_claim: INTERNAL_TARGET:K172_NUMERICAL_GRAPH_CONSTANTS_FROM_EXISTING_K156_TOPOLOGIES
target_claim_verdict: ROUTE_KILLED_AS_FORMULATED_WEIGHTED_OR_ORBIT_SPECIFIC_TAIL_REQUIRED
canon_verdict_change: none
---

# K173 two-graph tail obstruction wave

> **GU-COMPARATOR-ROUTING — scope before inference.** This artifact contains or
> borders a conventional particle-physics comparator. Any result about a
> standard Higgs/VEV, ordinary family index or net chirality, SO(10) `126`
> Majorana mechanism, anomaly selector, VEV-only breaking or familiar vector-
> mass route binds only that named model. It is not evidence for or against
> Weinstein's source-native mechanism without an explicit typed bridge. Read
> `lab/methods/source-native-comparator-routing.md` and follow its source-native
> pointers before reusing this result.

Classification: INTERNAL_STRUCTURAL_ONLY.

Scope: this packet stays on the repository-supplied K139--K172 equal-coupling
two-edge positive particle/hole point control at auxiliary chart `256`. It
tests whether K172's two numerical graph premises coexist on either topology
already proved by the chain. It neither changes the native operator nor
selects a physical extension, polarization, domain, state or scalar center.

```gu-typed-objects
result: the free-energy graph controls the normal-ordered core but is not preserved by the boundary map, while the particle-number graph makes the boundary map contractive but cannot control the logarithmically growing one-bath core; mixing their constants is invalid, and a quarter-energy plus number graph is only a candidate replacement
carrier: hard-core C3 impurity tensor positive particle/hole antisymmetric Fock space over L2(R;C4), in q=(0,0),(1,0),(0,1), with fixed K139 chart and K162 cofinal cells LAYER=observed CHIRALITY=S-FULL-DIRAC
pairing: positive physical Fock Hilbert pairing transported by S=(1-G_256)^-1 to M=S* S; every tail certificate must use one explicitly normalized domain for G:D->D, W:D->H and the seed graph norm ON=repository_signed_point_control
real_structure: CAR adjoint, momentum conjugation, Hermitian normal-ordered bath blocks and the K168 real flavor-symmetric reference shape
grading: conserved incidence charges, hard-core impurity degree, bath-particle number, free-energy and fractional-energy regularity, Neumann word order and K162 level
action_owner: repository-construction -- K156 fixes the normal-ordered core, but no source/GU action or current artifact selects and proves a common weighted graph with complete numerical constants
target: decide whether the existing graph estimates instantiate K172, prove the exact failed premises and expose the minimum replacement certificate MAP-TYPE=intertwiner
```

## Inline preflight bookend

K172 asks for numerical `q_D<1` and `B` after proving the symbolic tail

```text
B c q_D^(N+1)/((1-q_D)(1-q_H)).                       (1)
```

Retrieval changes the work list. K158 already proves that the sharp point
boundary does not preserve `Dom(H0)`, while K139 proves strict contraction on
the particle-number graph. K172 does not check whether the same graph also
makes the normal-ordered core bounded. The first task is therefore a
same-domain compatibility test, not numerical optimization.

The route census compared the free-energy graph, particle-number graph, graph
of `W`, fractional and logarithmic energy weights, coefficient-specific seed
orbits, form-dual summation, Kato residuals, Feshbach complements, and
Lehmann--Goerisch flux bounds. The two existing graphs give opposite failed
premises. The fractional route is the smallest live replacement because K159
already proves the dressed point profile has every energy exponent below
one-half.

`SC-META-53` remains `UNCERTAIN`; `LT-SM8`, `RA-F1` and `AC-F1` remain
`NEEDS`. The source register and v0.263 physics ledger do not move.

## 1. The free-energy graph has no finite boundary contraction

K158 identifies the limiting dressed point profile

```text
h(p)=(2 pi)^(-1/2)/(omega(p)+256).                     (2)
```

It lies in `L2`, but `omega(p)h(p)` tends to the nonzero constant
`(2 pi)^(-1/2)` at large momentum. Hence

```text
omega h notin L2.                                     (3)
```

The vacuum belongs to `Dom(H0)`, while its first boundary image contains
`h`; therefore `G_256` does not map the free-energy graph into itself. In the
topology used by K156's equation (14), the graph operator norm is infinite,
not a missing finite number:

```text
||G_256||_(Dom(H0)->Dom(H0))=infinity.                 (4)
```

Thus no numerical `q_D<1` exists on that graph. This is K158's route kill
replayed against the new K172 premise; it does not kill the singular operator
or the Hilbert-space Neumann chart.

## 2. The particle-number graph has no finite core bound

K139 proves that creation costs at most a factor two under `N+1`. Combining
that with K153's Hilbert bound `||G_256||<=3/8` gives

```text
||G_256||_(Dom(N+1)->Dom(N+1))<=3/4<1.                 (5)
```

This graph supplies the requested contraction. It does not supply `B`.
K172's one-bath normal ordering exposes the diagonal multiplier

```text
W_1=-256+m D_256(omega),       m in {1,2}.             (6)
```

For `e>=257`, restrict the defining integral for `D_256(e)` to
`256<=|k|<=e`. Since `omega(k)<=|k|+1` and the second denominator is at most
`3e`, symmetry gives

```text
D_256(e)>=(1/(3 pi)) log((e+257)/513).                 (7)
```

The right side diverges. Normalized one-particle packets localized at
increasing momentum have constant `(N+1)` graph norm but unbounded image under
(6). Consequently

```text
||W||_(Dom(N+1)->H)=infinity.                          (8)
```

The particle-number graph therefore has finite `q_D` and infinite `B`, the
opposite of the free-energy graph.

## 3. The K172 constants must live on one normalized graph

Equation (1) uses one `D`: `G:D->D`, `W:D->H` and `c=||phi||_D` must share
the same explicitly normalized domain. Taking `q_D=3/4` from the
particle-number graph and a qualitative `W` bound from the free-energy graph
does not prove any inequality. The companion compiler rejects different
domain identifiers and also requires the graph norm identifier, `B` and the
seed graph norm. Its abstract same-graph positive control is accepted; the
native mixed pair is rejected.

This corrects K156's sentence that graph contraction remains below one after
an unspecified “graph enlargement.” K158 already removed the free-energy
reading, and equations (7)--(8) remove the particle-number reading for K172's
tail. The qualitative convergence results remain valid at their stated
topologies; only the attempted numerical all-order action-tail splice is
killed.

## 4. A fractional-energy replacement remains open

K159 proves `h in Dom(omega^s)` exactly for `s<1/2`; choose `s=1/4`. K172's
upper bound and `log(1+t)<=t^s/s` give, because `256^(1/4)=4`,

```text
D_256(e)<=(1/pi)e^(1/4).                               (9)
```

Thus the named one-bath diagonal block is bounded from the quarter-energy
graph to Hilbert space, with conservative constants `256+1/pi` and
`256+2/pi` for the two K172 multiplicities. This is genuine progress over the
two failed graphs, but it is not a complete Fock-space `B`.

The missing certificate must use one fixed graph such as

```text
Dom(dGamma(omega)^(1/4)+N+1),                          (10)
```

and prove both a strict complete-Fock contraction for `G_256` and uniform
graph-to-Hilbert bounds for the diagonal Pauli/spectator term, all four
polarity-exchange blocks and every higher normal-ordered word. A
coefficient-specific sum-norm estimate along the exact K162 seed orbit is an
equally valid alternative. Neither complete proof is serialized here.

## 5. Native release replay

The numerical constants requested by K172 do not exist on either currently
proved graph as a usable pair. The K172 tail therefore cannot be evaluated at
`N=1`, and K171's all-order action column remains open. The complete
`R_ref` form-dual residual, positive complete `M`-orthogonal complement or
flux floor and K152 interval remain closed. K169's `5/2` threshold member is
still a cap rather than the first threshold, and scalar-center selection
remains separate.

## Inline postflight bookend

- **Strongest correction:** K172's two graph premises were available only on different, incompatible domains.
- **Free-energy verdict:** `q_D` is infinite because the boundary image of the vacuum misses `Dom(H0)`.
- **Particle-number verdict:** `q_D<=3/4`, but `B` is infinite because the exact one-bath core grows at least logarithmically.
- **Strongest replacement:** the quarter-energy graph contains the dressed point vector and bounds the named logarithmic one-bath block.
- **Strongest overclaim:** “combine K139's particle-number contraction with K156's free-graph core bound.” Refused because equation (1) requires one domain.
- **Weakest reproducibility seam:** the fractional estimate covers only the named diagonal subblock; all exchange and higher-word commutators remain unevaluated.

All five compatible mathematical arcs were attempted. The two existing-graph
tests, same-domain compiler and one-bath fractional replacement closed. The
complete fractional-Fock or orbit-specific tail, residual and complement
arcs remain dependent on missing uniform block estimates. Physical extension
and scalar-center selection remain authority-excluded. No source, ledger,
Born, prediction, confirmation, canon, paper, release or public-posture truth
moves.

## Next condition

On the explicitly normalized quarter-energy plus number graph, prove a
complete-Fock `q_(1/4)<1` for `G_256` and graph-to-Hilbert bounds for every
normal-ordered `W` block. If that graph is not invariant, derive a direct
coefficient-specific sum-norm tail for `W_nG^n phi` on the exact K162 vacuum
and one-impurity seed orbits. Only a same-domain certificate may enter K172,
K171 and the complete residual compiler.

## Reproduction

```bash
python3 tests/channel-swings/k173_two_graph_tail_obstruction.py --demo
python3 tests/channel-swings/k173_two_graph_tail_obstruction_probe.py
python3 tests/channel-swings/k173_two_graph_tail_obstruction_probe.py --selftest
```
