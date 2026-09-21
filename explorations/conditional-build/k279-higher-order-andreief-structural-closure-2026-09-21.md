---
title: "K279 higher-order Andréief structural closure"
status: internal_structural_result
date: 2026-09-21
claim_ceiling: exact repository-owned structural reduction and representation decision for all unresolved K179 order-seven-through-twelve coherent Gram families; no time integral, action-column value, complete residual, exterior gap, K152 interval, physical state, source claim, ledger row, canon, paper or public posture is changed
manifest: lab/process/k279-higher-order-andreief-structural-closure.json
producer: tests/channel-swings/k279_higher_order_andreief_structural_closure.py
probe: tests/channel-swings/k279_higher_order_andreief_structural_closure_probe.py
target_claim: INTERNAL_TARGET:K152_COEFFICIENT_COMPLETE_BASE_ACTION_COLUMN
target_claim_verdict: HIGHER_ORDER_STRUCTURAL_REPRESENTATION_CLOSED__NUMERICAL_COLUMN_OPEN
canon_verdict_change: none
---

# K279 higher-order Andréief structural closure

> **GU-COMPARATOR-ROUTING:** This artifact tests a repository-supplied
> conditional Fock construction. Read
> `lab/methods/source-native-comparator-routing.md` and the current source and
> physics ledgers before transferring it to a GU-native physical state.

Classification: `INTERNAL_STRUCTURAL_ONLY`.

Scope: K139--K179 fix a conditional hard-core `C3` impurity/Fock construction,
the K162 zero-bath seed orbits, auxiliary shift `256`, and every normal-ordered
coefficient through order twelve. K279 decides only how the unresolved orders
seven through twelve should be represented before numerical integration.

```gu-typed-objects
result: every unresolved coherent Gram pair has an exact factorial-free species-determinant representation on two positive cumulative-time simplices; literal expansion and exact signature memoization are rejected as primary routes
carrier: hard-core C3 impurity tensor positive particle/hole antisymmetric Fock space over L2(R;C4), restricted to the K162 zero-bath seed orbits LAYER=observed CHIRALITY=S-FULL-DIRAC
pairing: positive Hilbert Gram pairing after complete normalized specieswise exterior projection PAIRING-TYPE=hilbert
real_structure: CAR adjoint, momentum reflection, Hermitian matched finite-cutoff normal ordering and real Bessel kernels
grading: conserved incidence charges, impurity seed, bath species, bath number seven through twelve, K179 contraction identity and ordered momentum provenance
action_owner: repository-construction -- K139 fixes C and G, K156 fixes W, and K179 fixes the coefficient family; no source/GU action selects a physical extension, state, domain, polarization or scalar center
target: close the structural representation gate before any remaining K152 action-column quadrature MAP-TYPE=intertwiner
```

## Preflight bookend

K278 proves strict positivity of the complete order-six scalar but deliberately
does not turn it into an accurate action-column value. K277 ranks the missing
K152 consumer/action-column interface first. Retrieval confirms that K179 has
already serialized all `2,958` signed coefficient records through order twelve;
orders seven through twelve contain `2,816` unresolved paths. The unresolved
question is therefore representation and integration, not another coefficient
enumeration.

The route comparison covered five alternatives. One-order-at-a-time finite-rank
quadrature repeats structural work. Literal determinant expansion preserves the
object but scales factorially. Specieswise Andréief reduction preserves every
coherent cross term and can be proved generically. Exact kernel-signature
memoization is the cheapest possible further compression and is tested rather
than assumed. Switching to SC-ACT-06 is not a substitute: K276 identifies a
separate source-owned Euclidean background/symbol/projector dependency.

The source and physics posture remains unchanged. `SC-META-53` is `UNCERTAIN`;
`LT-SM8`, `LT-GR6b`, `RA-F1` and `AC-F1` remain `NEEDS`. This conditional
positive-Fock object is not the source's interacting physical state.

## Exact reduction theorem

For an order `n` coherent pair, let `m_s` be the multiplicity of species `s`.
Each normalized wedge contributes `1/sqrt(m_s!)`. Specieswise Andréief gives

```text
integral det[f_i(p_j)] det[g_k(p_j)] product_j dp_j
  = m_s! det[integral f_i(p) g_k(p) dp].
```

The factor `m_s!` cancels the two wedge factors exactly for every species.
Thus every Gram pair becomes

```text
c_t c_u (2*pi)^(-(n+2))
integral exp(-256(sum s+sum v))
  [2 K1(T_old)] [2 K1(U_old)]
  product_s det[2 K1(T_i+U_j)] ds dv.                 (1)
```

There are `2(n+1)` positive time variables. With
`rho=sum(s)+sum(v)`, `theta=sum(s)/rho` and two simplex coordinates, the
Jacobian contributes `rho^(2n+1)`. A crude bound on the `n+2` Bessel factors
leaves `rho^(n-1)`. This is integrable at zero for every `n=7,...,12` without
using determinant cancellation. Exact finite-measure Andréief controls pass
for every species multiplicity `1,...,6`.

## Complete workload and decision

| order | paths | groups | Gram entries | literal products | determinant cubic proxy | origin power |
| ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 7 | 96 | 16 | 408 | 7,920 | 14,664 | 6 |
| 8 | 192 | 23 | 1,296 | 58,968 | 61,344 | 7 |
| 9 | 256 | 20 | 2,368 | 313,344 | 158,784 | 8 |
| 10 | 480 | 28 | 6,890 | 2,583,072 | 586,700 | 9 |
| 11 | 640 | 24 | 12,920 | 16,430,400 | 1,461,520 | 10 |
| 12 | 1,152 | 33 | 35,352 | 149,816,160 | 4,930,704 | 11 |

Across all remaining orders there are `59,234` exact Gram entries.
Literal expansion contains `169,209,864` products; the sum-of-cubes
determinant arithmetic proxy is `7,213,716`, a ratio of about `23.4567`.
This is an algebraic representation comparison, not a runtime or quadrature
error estimate.

Canonical signatures include the coherent group, both contracted positions,
coefficient product and every left/right species-time occurrence, modulo pair
transpose. All `59,234` signatures are distinct. Exact memoization therefore
removes zero entries. The selected representation is factorial-free species
determinants with a shared cumulative-time DAG; the next numerical gate is one
shared determinant-valued rule, first validated on the complete order-seven
family with separate `rho`-tail and `theta`/simplex-face errors.

## Postflight bookend

The producer freezes every order/group/path/entry count, proves factorial
cancellation and origin integrability, and passes exact Andréief controls for
multiplicities one through six. The independent replay passes `7/7` checks and
rejects `5/5` hostile changes: deleted order-twelve term, wrong contracted
parity, split coherent group, wrong wedge factorial and contracted-variable
leak.

Strongest overclaim: equation (1) evaluates the action column. It does not;
all time integrals and their rigorous tails/faces remain open. Strongest
contrary route: exact signature memoization could collapse the workload; the
complete signature census rejects that route. Weakest reproducibility seam:
the algebraic cubic proxy does not predict interval-quadrature runtime, so the
order-seven integrator must report actual work and error before extension.

K279 closes the structural representation question for all unresolved orders
in one pass. It does not emit the coefficient-complete base action column,
complete shifted residual, exterior gap, scalar-center floor or K152 interval.
