---
artifact_type: exact_construction_and_scope_result
created: 2026-08-10
status: RANK594_OBSERVATION_STABILIZER_INVARIANT__CONDITIONAL_ASSOCIATED_SUBBUNDLE__LOWER_ORDER_OPEN
lane: "1"
functional_channels: [BUILD, COMPOSE, SOURCE, VERIFY]
ledger_rows: [LT-GR1, LT-GR2b, LT-GR2c, LT-GR3, LT-GR5, LT-GR6]
claim_status_change: none
canon_verdict_change: none
public_posture_change: none
---

# Selected-K77 observation-stabilizer subbundle

## Result in plain English

The rank-`594` extension from v0.126 is not an accidental coordinate span. All
`51` infinitesimal generators of the complete connected observation stabilizer

```text
so(1,3) + so(6,4)
```

preserve it exactly. It therefore defines a rank-`594` associated vector
subbundle once the GU observation reduction is supplied. Together with the
already-selected `321` fields, this gives a source-natural **local-principal**
rank-`915` tangent bundle candidate.

The construction is not invariant under the full ambient `so(7,7)`: one mixed
horizontal/normal generator expands rank `594` to `727`. That is useful rather
than a defect. It proves the extension belongs to the observed split and
cannot be asserted upstairs before the observation/soldering reduction.

## Exact natural decomposition

Write the observed split as `V = H + N`, with dimensions `4+10` and signatures
`(1,3)+(6,4)`. The omitted grade-two connection space is the complement of
`H* tensor Lambda2(H)` in `V* tensor Lambda2(V)`. The exact extension is

```text
S_594 = H* tensor (H wedge N)                         [160]
      + H* tensor Lambda2(N)                         [180]
      + N* tensor Lambda2(H)                         [ 60]
      + H  tensor (R id_N + so(6,4))                [184]
      + c(N),  c(v)=sum_a theta^a tensor (v wedge e_a) [10]
                                                        ---
                                                        594
```

The first three blocks occur in full. In
`N* tensor (H wedge N) = H tensor End(N)`, the extension retains precisely the
scalar plus `so(6,4)` endomorphisms and excludes the `54`-dimensional symmetric
trace-free normal block for each horizontal factor. In
`N* tensor Lambda2(N)`, it retains exactly the canonical ten-dimensional
contraction copy. Exact projection/intersection dimensions are

| block | ambient | projection | intersection |
|---|---:|---:|---:|
| `H* tensor (H wedge N)` | 160 | 160 | 160 |
| `H* tensor Lambda2(N)` | 180 | 180 | 180 |
| `N* tensor Lambda2(H)` | 60 | 60 | 60 |
| `N* tensor (H wedge N)` | 400 | 184 | 184 |
| `N* tensor Lambda2(N)` | 450 | 10 | 10 |

Because every projection rank equals the intersection rank, this is a direct
block decomposition, not a graph between isomorphic pieces. It is rational and
branch-independent even though the producer's convenient echelon basis lives
over `QQ(sqrt(3))`.

## Layer 0

| phrase | object proved here | object kept distinct |
|---|---|---|
| invariant fiber | one rank-594 subrepresentation of the selected grade-two source fiber | a coordinate span in one frame |
| associated subbundle | `P_obs times_G S_594` after a `G=Spin(1,3) times Spin(6,4)` reduction is supplied | existence of that global reduction or a trivial bundle |
| naturality | exact simultaneous action on the covector and adjoint-bivector slots | covector-only transport or spatial relabelling |
| observed covariance | invariance under the block observation stabilizer | full ambient `Spin(7,7)` invariance |
| local-principal tangent | rank `321+594=915` at principal-symbol grade | lower-order/derivative-jet Hessian closure |

## Durable exact bank

The v0.126 echelon basis has only `1,850` nonzero coefficients. It is now
serialized in a 59,230-byte, dependency-hashed bank. Ordinary consumers load
it through `k77_minimal_tangent_bank_api.py` without executing the two-minute
producer. Mutation, staleness, rank and pivot-canonicality checks fail closed.

## Source return

```text
SOURCE-CONFIRMS:
  the full adjoint-valued connection one-form and the observed
  (1,3)+(6,4) split printed in draft equation (12.19).

REPO-DERIVES:
  the invariant rank-594 fiber, its five-block natural decomposition, and
  the associated subbundle conditional on the observation reduction.

SOURCE-SILENT:
  the rank 594/915 selection, lower-order closure, a global observation
  reduction, a BV quotient, and either unitary-parent port.
```

## Efficient inline specialist assessment

1. **Layer-0 semantics — ACTUAL MATH, very high confidence.** The key split is
   invariant fiber versus associated subbundle versus global reduction. The
   mixed ambient generator is the cheapest scope control.
2. **Prior art — ACTUAL MATH, very high.** v0.126 supplies the fiber; draft
   (12.19) supplies the observed split. Neither alone supplied this theorem.
3. **Clifford/representation theory — ACTUAL MATH, very high.** The action is
   the simultaneous dual-vector plus adjoint-bivector representation, checked
   on all 51 generators.
4. **Differential geometry — ACTUAL MATH, high.** A stabilizer subrepresentation
   gives an associated bundle after reduction, not before it.
5. **Invariant theory — ACTUAL MATH, very high.** The `160+180+60+184+10`
   formula identifies the fiber without its branch-dependent echelon basis.
6. **Exact sparse algebra — ACTUAL MATH, very high.** Python rational-quadratic
   and independent Sage/FLINT routes agree, including the rank-727 cross plant.
7. **Variational bicomplex — ACTUAL MATH, high.** This identifies the field
   tangent's principal fiber but says nothing yet about lower-order closure.
8. **PDE/microlocal — ACTUAL MATH, high.** Principal-symbol naturality is a
   prerequisite for an operator bundle; domains and hyperbolicity remain open.
9. **Symplectic/BV-BFV — ACTUAL MATH, very high.** No gauge distribution or
   quotient is inferred from an invariant field subbundle.
10. **Operator/Krein — ACTUAL MATH, high.** The representation preserves the
    indefinite structure but does not supply a positive majorant or domain.
11. **Source fidelity — ACTUAL MATH, high.** The source owns the split and full
    connection; the rank-594 selection remains a repository construction.
12. **Adversarial process — ACTUAL MATH, very high.** The versioned basis bank
    prevents the successor from paying the producer cost or silently drifting.

## Hostile disposition

Verdict:
`CANDIDATE_SURVIVES__OBSERVATION_STABILIZER_INVARIANT594__CONDITIONAL_ASSOCIATED_SUBBUNDLE`.

The phrase “global source-natural subbundle” is narrowed: the associated
subbundle exists globally only on a supplied global observation reduction.
The result is not ambient-`Spin(7,7)` invariant and does not construct the
reduction itself. Those are the strongest surviving fences.

## Progress and next gate

```text
Ledger v0.127 — 82/82 mapped (100%)
32 SAME · 19 DIFFERS · 26 NEEDS · 5 OVER-DETERMINED
Residue 84; conditional action-parent range 84..86
Scoped quotients 5

headline_delta: none
conditions_closed: 2
  - exact rank-594 fiber has a source-natural stabilizer decomposition
  - conditional associated subbundle and nonrecursive basis bank are built
conditions_opened: 0
remaining_named_conditions: 1
```

Next construct the lower-order and derivative-jet first-action Hessian on the
natural `915` tangent and test whether it closes. Use the five-block formula as
the field definition and the serialized bank as an exact coordinate oracle.
Do not widen to `1,571` or define a quotient unless the action itself forces it.

Evidence:

- primary exact probe: `78/78 PASS`;
- independent Sage/FLINT: `12/12 PASS`;
- P1/P2/P3 unchanged and unused.
