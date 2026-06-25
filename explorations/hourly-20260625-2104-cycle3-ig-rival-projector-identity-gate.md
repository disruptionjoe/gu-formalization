---
title: "Hourly 20260625 2104 Cycle 3 IG Rival Projector Identity Gate"
date: "2026-06-25"
run_id: "hourly-20260625-2104"
cycle: 3
lane: "1 IG"
doc_type: ig_rival_projector_identity_gate
artifact_id: "SourceNaturalProductABRivalProjectorIdentityGate_2104_C3_L1_V1"
verdict: "BLOCKED_SOURCE_NATURAL_PROJECTOR_IDENTITY_ABSENT"
owned_path: "explorations/hourly-20260625-2104-cycle3-ig-rival-projector-identity-gate.md"
---

# Hourly 20260625 2104 Cycle 3 IG Rival Projector Identity Gate

## 1. Verdict

Verdict: **blocked**.

The repo has enough admitted finite D7 data to build the two-row Product A/Product
B comparison, but it does not have enough source-native data to instantiate:

```text
SourceNaturalProductABRivalProjectorIdentity_V1
```

The finite comparison cannot be upgraded into a source-natural selector by row
matching alone. Product A and Product B share two irreducible rows:

```text
V(omega_1 + omega_7)
V(omega_6)
```

The desired selector would have to prove, from a source-defined operator or
projector identity, that the common `V(omega_1 + omega_7)` row is killed and the
common `V(omega_6)` row is retained. The current repo sources name that object
as missing; they do not supply the source row or proof object.

This is not a global no-go. It is a precise route-local block at the first
missing source-native selector identity.

## 2. What Was Derived Directly From Repo Sources

Required sources read first:

| source | direct use |
|---|---|
| `RESEARCH-POSTURE.md` | Applied no-target-import and no compatibility-as-derivation rules. |
| `process/runbooks/five-lane-frontier-run.md` | Used the blocked/conditional/no-go verdict vocabulary and exact-obstruction standard. |
| `process/runbooks/three-cycle-fifteen-hole-run.md` | Used the quality-hole requirement: identify the missing object, not a summary-only next step. |
| `explorations/hourly-20260625-2104-cycle1-ig-product-b-d7-table-receipt-attempt.md` | Consumed the admitted Product B table. |
| `explorations/hourly-20260625-2104-cycle2-ig-product-a-finite-control-packet.md` | Consumed the admitted Product A packet and its selector blocker. |
| `tests/hourly_20260625_2104_cycle2_frontier_gates_audit.py` | Checked that the cycle 2 audit asserts two common rows and proof restart false. |
| `explorations/sc1-oq1a-d7-clebsch-gordan-cas-2026-06-23.md` | Used the 2026-06-25 supersession note: old one-row common-summand conclusion is no longer current. |

Additional consistency context checked after the required first reads:

| source | direct use |
|---|---|
| `RESEARCH-STATUS.md` | Confirms SC1-OQ1A Product A is closed route-locally, selector identity is open, and proof restart is blocked pending `SourceNaturalProductABRivalProjectorIdentity_V1`. |
| `NEXT-STEPS.md` | Confirms the next IG object is a source-natural rival-projector identity. |
| `DERIVATION-PROGRESS.md` | Confirms the Product B correction and Product A packet leave two common rows. |
| `explorations/hourly-20260625-0803-cycle2-ig-representation-natural-rival-eliminator-matrix.md` | Confirms older broader K_IG rival-eliminator work built a blocking inventory, not an accepted selector. |
| `explorations/hourly-20260625-1302-cycle1-ig-selector-theorem.md` | Confirms earlier selector-theorem work was conditional and not closed; its old chirality eliminations are superseded by the Product B correction. |

Direct finite data admitted from Product B:

```text
B = V(omega_2) tensor V(omega_6)
  = V(omega_2 + omega_6)
    plus V(omega_1 + omega_7)
    plus V(omega_6)
```

with multiplicities one and dimensions:

```text
4928 + 832 + 64 = 5824 = 91 * 64
```

Direct finite data admitted from Product A:

```text
A = V(omega_1) tensor V(omega_7)
  = V(omega_1 + omega_7) plus V(omega_6)
```

with multiplicities one and dimension check:

```text
832 + 64 = 896 = 14 * 64
```

For the Product A gamma-trace / Clifford multiplication map:

```text
c: V(omega_1) tensor V(omega_7) -> V(omega_6)
```

the admitted packet gives:

```text
ker(c) = V(omega_1 + omega_7)
image(c) = V(omega_6)
cokernel(c) = 0
```

Therefore the source-native finite comparison currently available in the repo is:

| row | Product A status | Product B status | finite comparison |
|---|---|---|---|
| `V(omega_2 + omega_6)` | absent | present, mult 1 | not common |
| `V(omega_1 + omega_7)` | present, mult 1 as `ker(c)` | present, mult 1 | common rival row |
| `V(omega_6)` | present, mult 1 as `image(c)` | present, mult 1 | common desired row |

This is enough to derive:

```text
common_row_count = 2
finite_common_row_uniqueness = false
```

It is not enough to derive a source-natural selector.

## 3. Strongest Positive Result

The strongest positive result is a narrowed two-slot projector problem.

Since both common rows occur with multiplicity one in Product A and Product B,
the D7-equivariant row-level comparison has only two possible shared slots:

```text
R = V(omega_1 + omega_7)
S = V(omega_6)
```

At the representation-table level, any D7-equivariant Product B to Product A
comparison is constrained to the form:

```text
T_D7 = alpha * id_R + beta * id_S
```

where `alpha` is the coefficient on the rival row and `beta` is the coefficient
on the desired spinor row. The `V(omega_2 + omega_6)` Product B row has no
Product A target row.

This is useful because the next proof object is no longer vague. A successful
source-natural selector must prove:

```text
alpha = 0
beta != 0
```

or an equivalent normalized projector identity:

```text
T_src = 0 * id_{V(omega_1 + omega_7)} + 1 * id_{V(omega_6)}
```

with `T_src` derived from the GU source structure, not from generation count,
desired uniqueness, downstream physics, or repo preference.

Thus the finite work gives a clean target for `SourceNaturalProductABRivalProjectorIdentity_V1`.
It also shows exactly why the old one-row selector route cannot restart: the
rival row is not absent; it is present in both products.

## 4. First Exact Obstruction Or Missing Proof Object

The first exact obstruction is the absence of a source-defined row matrix:

```text
ProductABSourceOperatorTwoRowProjectorMatrixReceipt_V1
```

or equivalently the stronger closure object:

```text
SourceNaturalProductABRivalProjectorIdentity_V1
```

The missing receipt must contain all of the following:

| required field | why it is required |
|---|---|
| a source-defined operator or projector `T_src` with domain/codomain matching the Product A/Product B comparison | Without an actual source operator, the row matrix is only an abstract Hom-space coordinate system. |
| D7 or Spin(9,5) equivariance of `T_src` under the repo omega convention | Otherwise Schur row reduction does not justify the two-slot comparison. |
| the row coefficients on `V(omega_1 + omega_7)` and `V(omega_6)` | These are the exact data needed to decide rival survival. |
| a proof that the rival coefficient is zero | This is the missing selector step. |
| a proof that the `V(omega_6)` coefficient is nonzero, or a source normalization making it one | Otherwise the selector may kill both common rows. |
| identity to the claimed `K_IG` family selector | Otherwise the row selector is not yet the IG operator needed downstream. |
| target-import screen | Otherwise target physics or desired generation count could be smuggled in as selection evidence. |

What is present now:

```text
Product A finite packet: present
Product B finite table: present
two common rows: present
abstract two-slot Hom coordinate system: present
source-defined coefficient row alpha=0: absent
source-defined coefficient row beta!=0: absent
family identity to K_IG: absent
```

Therefore the selector remains blocked.

## 5. Constructive Next Object

Construct:

```text
ProductABSourceOperatorTwoRowProjectorMatrixReceipt_V1
```

Minimal acceptance contents:

```json
{
  "source_operator_id": "T_src",
  "source_operator_definition": "explicit formula or recovered source row",
  "domain": "V(omega_2) tensor V(omega_6)",
  "codomain": "V(omega_1) tensor V(omega_7)",
  "row_basis": [
    "V(omega_1 + omega_7)",
    "V(omega_6)"
  ],
  "row_coefficients": {
    "V(omega_1 + omega_7)": "proved_zero_or_nonzero",
    "V(omega_6)": "proved_zero_or_nonzero"
  },
  "rival_row_killed_by_source": true,
  "desired_row_retained_by_source": true,
  "identity_to_K_IG_selector": "proved_or_separately_blocked",
  "target_import_used": false
}
```

This object would either close the current obstruction or turn it into a scoped
fail. If it proves `alpha = 0` and `beta != 0` from source structure, the
selector route can restart conditionally at the `K_IG` family-identity and
full-rival-eliminator gates. If it proves `alpha != 0`, the uniqueness-based
selector route fails for this Product A/Product B comparison. If no source
operator can be defined, the route remains blocked rather than failed.

## 6. What This Means For SC1-OQ1A, K_IG, And Proof Restart

For SC1-OQ1A:

```text
Product B table: admitted route-locally
Product A packet: admitted route-locally
old one-common-row uniqueness route: superseded
current common-row count: 2
SC1-OQ1A uniqueness/common-summand gate: OPEN
```

The two-row finite comparison is a real improvement, but it is not a selector.
The Product A gamma-trace map `c` kills `V(omega_1 + omega_7)` only after one
has chosen the Product A gamma-trace projection. It does not prove that the
actual source-defined Product B to Product A comparison has zero coefficient on
the shared rival row.

For `K_IG`:

```text
K_IG family identity verified: false
SourceForcedCodomainSelectorForK_IG accepted: false
SourceNaturalProductABRivalProjectorIdentity_V1 admitted: false
```

The repo can now state the exact `K_IG` finite selector demand: identify the
source-defined operator whose two-row matrix is zero on `V(omega_1 + omega_7)`
and nonzero on `V(omega_6)`, then prove this operator is the `K_IG` selector
family member.

For proof restart:

```text
selector_restart_allowed: false
proof_restart_allowed: false
```

No GU proof restart should cite the Product A/Product B packets as a
source-natural selector until the missing two-row source operator receipt is
filed and passes the target-import screen.

## 7. Rollback Or Falsification Condition

Rollback this artifact if any of the following is admitted:

```text
Product B table is overturned.
Product A packet is overturned.
The omega_6 / omega_7 convention used by the Product A or Product B packets is reversed.
The common row count is recomputed as not equal to 2.
An already-existing source-native proof object was missed and actually instantiates SourceNaturalProductABRivalProjectorIdentity_V1.
```

Demote the selector route from blocked to scoped fail if an admitted
source-defined row matrix proves:

```text
alpha != 0
```

for the `V(omega_1 + omega_7)` row, with no additional source identity killing
that component.

Reject, rather than promote, any attempted selector receipt if it chooses
`alpha = 0` because of target generation count, desired uniqueness, downstream
phenomenology, or repo preference.

## 8. Claim-Status Consistency Result

Claim-status consistency was checked and no ledger edit is made by this worker.

This artifact is consistent with current status:

```text
SC1-OQ1A D7 common-summand / Product B chirality exclusion: OPEN
SC1-OQ1A Product A finite-control packet: CLOSED route-locally for Product A; selector identity OPEN
Shiab existence: unaffected, existence only
K_IG selector: not accepted
proof restart: blocked
```

No claim-status consistency workflow is triggered by this lane because the
artifact does not promote, demote, or re-scope a live repo claim beyond the
already-recorded 2104 Product B/Product A corrections. It records the next
blocked source object in the assigned owned artifact only.

## 9. Machine-Readable JSON Summary

```json
{
  "run_id": "hourly-20260625-2104",
  "cycle": 3,
  "lane": "1 IG",
  "artifact_path": "explorations/hourly-20260625-2104-cycle3-ig-rival-projector-identity-gate.md",
  "verdict_class": "blocked",
  "target_import_used": false,
  "claim_status_consistency_triggered": false,
  "accepted_receipt_count": 2,
  "product_a_admitted": true,
  "product_b_admitted": true,
  "common_row_count": 2,
  "rival_projector_identity_admitted": false,
  "selector_restart_allowed": false,
  "proof_restart_allowed": false,
  "first_obstruction": "source_defined_Product_A_Product_B_two_row_projector_matrix_absent_no_proof_alpha_equals_zero_for_V_omega1_plus_omega7",
  "constructive_next_object": "ProductABSourceOperatorTwoRowProjectorMatrixReceipt_V1"
}
```
