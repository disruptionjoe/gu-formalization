---
title: "Hourly 20260625 2104 Cycle 2 IG Product A Finite Control Packet"
date: "2026-06-25"
run_id: "hourly-20260625-2104"
cycle: 2
lane: "2 IG Product A"
doc_type: ig_product_a_finite_control_packet
artifact_id: "ProductAFullKernelCokernelHighestWeightPacket_2104_C2_L2_V1"
verdict: "PRODUCT_A_PACKET_CLOSED_SELECTOR_BLOCKED_BY_RETAINED_RIVAL_ROW"
owned_path: "explorations/hourly-20260625-2104-cycle2-ig-product-a-finite-control-packet.md"
---

# Hourly 20260625 2104 Cycle 2 IG Product A Finite Control Packet

## 1. Verdict

Verdict: **closed for Product A; blocked for selector identity**.

The Product A packet can be admitted route-locally:

```text
A = V(omega_1) tensor V(omega_7)
  = V(omega_1 + omega_7) oplus V(omega_6)
```

with multiplicities one and dimension check:

```text
832 + 64 = 896 = 14 * 64
```

For the gamma-trace / Clifford multiplication map

```text
c: V(omega_1) tensor V(omega_7) -> V(omega_6),
```

the packet is:

```text
image(c) = V(omega_6)
cokernel(c) = 0
ker(c) = V(omega_1 + omega_7)
highest_weight(ker(c)) = omega_1 + omega_7
```

This closes `FC-IRR` and `FC-HW` for Product A. It also consumes the cycle-1
Product B receipt, so `FC-MULT` no longer blocks on the missing Product B
`V(omega_6)` multiplicity: Product B has `V(omega_6)` with multiplicity one.

But the finite-control comparison does **not** produce a selector identity.
The admitted Product B table is:

```text
B = V(omega_2) tensor V(omega_6)
  = V(omega_2 + omega_6) oplus V(omega_1 + omega_7) oplus V(omega_6)
```

Therefore the Product A/Product B common rows are:

```text
V(omega_1 + omega_7)
V(omega_6)
```

Product A retains `V(omega_1 + omega_7)` as the kernel of `c`; it does not
eliminate that row from the finite representation comparison. The map `c`
eliminates `V(omega_1 + omega_7)` only after one has already selected the
gamma-trace projection. That selected projection is precisely the missing
source-natural selector object, so it cannot be inferred from Product B or from
the Product A packet alone.

Current gate state:

```text
Product B receipt consumed: yes
Product A packet admitted: yes
FC-IRR: closed for Product A
FC-MULT: closed for Product B V(omega_6) multiplicity, but not a uniqueness selector
FC-HW: closed for Product A
finite common-row uniqueness: fails, two common rows
selector identity: blocked
selector restart allowed: false
target import used: false
```

## 2. Specific claim/bridge under test

The bridge under test is:

```text
ProductBFullD7SummandMultiplicityDimensionTableReceipt_V1
  -> ProductAFullKernelCokernelHighestWeightPacket_V1
  -> finite-control comparison
  -> FC-IRR / FC-MULT / FC-HW
  -> K_IG selector or family-identity proof restart
```

This artifact tests the second and third arrows. The Product B receipt is
consumed as an upstream finite table, not as selector evidence. The exact
question is whether Product A can remove the two Product B rows that matter for
the Shiab Hom-space comparison:

```text
V(omega_1 + omega_7)
V(omega_6)
```

Decision:

```text
V(omega_6): retained in Product A and retained in Product B; it is the image of c.
V(omega_1 + omega_7): retained in Product A as ker(c) and retained in Product B.
```

So Product A classifies the two rows, but it does not eliminate the rival row at
the representation-comparison level.

## 3. Sources read first

| source | use |
|---|---|
| `RESEARCH-POSTURE.md` | Applied no-target-import and constructive obstruction rules. |
| `process/runbooks/five-lane-frontier-run.md` | Used decision-grade verdict vocabulary and no compatibility-as-derivation rule. |
| `process/runbooks/three-cycle-fifteen-hole-run.md` | Used quality-hole fields and exact blocker requirement. |
| `explorations/hourly-20260625-2104-cycle1-ig-product-b-d7-table-receipt-attempt.md` | Consumed the admitted Product B table and its downstream blocker statement. |
| `tests/hourly_20260625_2104_cycle1_receipt_attempts_audit.py` | Checked the independent character arithmetic audit for Product B. |
| `explorations/sc1-oq1a-d7-clebsch-gordan-cas-2026-06-23.md` | Used the corrected Product A skeleton and the supersession note for the old Product B chirality exclusion. |
| `explorations/hourly-20260625-1802-cycle2-ig-product-b-first-admission-gate.md` | Inherited the dependency order: Product B, then Product A, then FC gates, then selector identity. |

Additional live-status context consulted after those first reads:

| source | use |
|---|---|
| `RESEARCH-STATUS.md` | Confirmed current SC1-OQ1A status is open after the Product B correction. |
| `process/runbooks/claim-status-consistency-quality-workflow.md` | Checked the status-change trigger rule. |
| `explorations/hourly-20260625-1503-cycle2-ig-d7-proof-object-admission.md` | Reused the prior FC-IRR/FC-MULT/FC-HW proof-object criteria. |
| `explorations/hourly-20260625-1802-cycle1-ig-raw-formal-d7-branching-transcript.md` | Confirmed Product A was the second missing packet before Product B closed. |
| `explorations/hourly-20260625-1802-cycle3-claim-promotion-firewall.md` | Confirmed family identity is downstream of Product B, Product A, FC gates, and rival elimination. |

## 4. Strongest positive construction attempt

Use the repo D7 convention:

```text
omega_1 = vector
omega_2 = two-form / adjoint
omega_6 = positive half-spin
omega_7 = negative half-spin
```

Product A is a vector times half-spin product. The vector representation
`V(omega_1)` is minuscule, so tensoring `V(omega_7)` by it is multiplicity-free;
the candidate highest weights are the dominant elements among:

```text
omega_7 + weights(V(omega_1)).
```

In doubled `e_i` coordinates, the two dominant candidates are:

| highest weight | doubled coordinates | Dynkin labels | dimension |
|---|---:|---:|---:|
| `omega_1 + omega_7` | `[3,1,1,1,1,1,1]` | `[1,0,0,0,0,0,1]` | 832 |
| `omega_6` | `[1,1,1,1,1,1,-1]` | `[0,0,0,0,0,1,0]` | 64 |

The Weyl dimensions sum to the full product dimension:

```text
dim V(omega_1 + omega_7) + dim V(omega_6)
  = 832 + 64
  = 896
  = dim V(omega_1) * dim V(omega_7)
```

The Clifford multiplication map `c` is a nonzero D7-equivariant map from
Product A to `V(omega_6)`. Since `V(omega_6)` occurs with multiplicity one, the
map is surjective up to scalar and its kernel is the remaining irreducible:

```text
ker(c) = V(omega_1 + omega_7)
cokernel(c) = 0
```

This gives the strongest positive Product A result. It is enough to close the
Product A packet, `FC-IRR`, and `FC-HW` route-locally.

Now compare with the admitted Product B receipt:

| row | Product A | Product B | comparison result |
|---|---:|---:|---|
| `V(omega_2 + omega_6)` | absent | present, mult 1 | not common |
| `V(omega_1 + omega_7)` | present, mult 1 as `ker(c)` | present, mult 1 | retained rival |
| `V(omega_6)` | present, mult 1 as `image(c)` | present, mult 1 | retained desired row |

Thus the finite D7 comparison gives two common rows, not one. The constructive
positive result is therefore a clean Product A packet plus a clean obstruction
to the old uniqueness shortcut.

## 5. First exact obstruction/missing object

The first missing object after this packet is:

```text
SourceNaturalProductABRivalProjectorIdentity_V1
```

It must show, without target import, that the actual IG source map or Bianchi
operator factors through the `V(omega_6)` row and annihilates the shared
`V(omega_1 + omega_7)` row.

The obstruction is exact:

```text
Hom_D7(B, A) has two representation rows available:
  V(omega_1 + omega_7) -> V(omega_1 + omega_7)
  V(omega_6) -> V(omega_6)
```

Product A alone cannot decide that the first row is forbidden. It only says the
row is the kernel of the chosen gamma-trace projection. Selecting that projection
as the physically/source-relevant finite-control map is the missing selector
identity, not a consequence of the finite character table.

Rejected shortcuts:

```text
Product B alone:
  rejected; Product B lists rows but does not choose the Product A projection.

Product A alone:
  rejected; Product A retains V(omega_1 + omega_7) as ker(c).

dimension preference:
  rejected; smaller dimension or desired uniqueness is not source evidence.

target generation count:
  rejected; generation count is downstream target data.

calling c "the" selector:
  rejected unless a source-natural identity proves this exact projection is forced.
```

## 6. What would change if closed

If `SourceNaturalProductABRivalProjectorIdentity_V1` closed, the IG route would
move from finite representation receipt work to selector-family identity work.
The finite-control state would become:

```text
Product B: closed
Product A: closed
FC-IRR: closed
FC-MULT: closed for the V(omega_6) row
FC-HW: closed
shared V(omega_1 + omega_7) rival: eliminated by source-natural identity
selector restart: conditionally allowed after no-target-import and rival-matrix checks
```

Without that object, this artifact changes the route in a different way: the old
single-common-summand path is not available. Product A does not rescue the
Product B correction; it confirms that the rival row is present on both sides.

## 7. Rollback/falsification condition

Rollback this packet if any independent admissible D7 computation or formal
proof shows one of the following:

```text
V(omega_1) tensor V(omega_7) has a summand beyond V(omega_1 + omega_7) and V(omega_6).
V(omega_1 + omega_7) is not the kernel of the gamma-trace map c.
V(omega_6) is not the image of c or c is not surjective.
cokernel(c) is nonzero.
the omega_6 / omega_7 convention is reversed relative to the repo convention.
the cycle-1 Product B receipt is overturned.
Product B does not retain V(omega_1 + omega_7).
target generation count or desired uniqueness was used as evidence for any finite row.
```

If a later source-natural identity annihilates the shared
`V(omega_1 + omega_7)` row, do not rollback Product A. Update the downstream
selector state instead: the representation row is present, but the source map
kills it.

## 8. Next meaningful computation/proof step

Construct:

```text
D7IntertwinerProjectorMatrixForProductBToProductA_V1
```

or the stronger:

```text
SourceNaturalProductABRivalProjectorIdentity_V1
```

The useful computation is not another product decomposition. It is an explicit
intertwiner/projector calculation for the two common rows:

```text
B -> A -> V(omega_6)
```

The calculation must answer:

```text
Does the actual source-defined IG operator kill the B-side V(omega_1 + omega_7) row?
Does it select the V(omega_6) row for a source reason rather than because that row
is the desired one?
Is the selected projection identical to the claimed K_IG family selector?
```

If the `V(omega_1 + omega_7)` component survives any source-natural map, the
uniqueness-based selector route fails. If it is killed by a source-natural
identity, the selector route can restart at the family-identity and full
rival-eliminator stage.

## 9. Claim-status consistency result

Claim-status consistency is **triggered but not edited by this worker**.

This artifact changes the IG route state from:

```text
Product A packet missing
```

to:

```text
Product A packet admitted, but finite comparison has two common rows.
```

That is a substantial re-scope of the local finite-control gate, but this lane
owns only the assigned exploration file. No `RESEARCH-STATUS.md`, canon,
roadmap, paper draft, or audit file was edited.

Consistency check against live status:

```text
RESEARCH-STATUS.md already marks SC1-OQ1A D7 common-summand / Product B
chirality exclusion as OPEN after the 2104 Product B correction.
```

This artifact is consistent with that status. It does not promote Shiab
uniqueness, `K_IG`, generation count, or any major GU claim.

## 10. Machine-readable JSON summary

```json
{
  "artifact": "ProductAFullKernelCokernelHighestWeightPacket_2104_C2_L2_V1",
  "artifact_path": "explorations/hourly-20260625-2104-cycle2-ig-product-a-finite-control-packet.md",
  "run_id": "hourly-20260625-2104",
  "cycle": 2,
  "lane": "2 IG Product A",
  "route": "IG",
  "verdict_class": "closed_product_a_packet_selector_blocked",
  "product_b_receipt_consumed": true,
  "product_a_packet_admitted": true,
  "accepted_receipt_count": 2,
  "target_import_used": false,
  "claim_status_consistency_triggered": true,
  "v_omega1_plus_omega7_decided": "retained_in_Product_A_as_kernel_and_retained_in_Product_B_as_common_rival_row",
  "v_omega6_decided": "retained_in_Product_A_as_image_of_c_and_retained_in_Product_B_as_common_desired_row",
  "selector_restart_allowed": false,
  "first_obstruction": "SourceNaturalProductABRivalProjectorIdentity_V1_absent_two_common_rows_remain",
  "constructive_next_object": "D7IntertwinerProjectorMatrixForProductBToProductA_V1_or_SourceNaturalProductABRivalProjectorIdentity_V1",
  "product_a": {
    "expression": "V(omega_1) tensor V(omega_7)",
    "total_dimension": 896,
    "dimension_check": "832 + 64 = 896 = 14 * 64",
    "summands": [
      {
        "highest_weight": "omega_1 + omega_7",
        "dynkin_labels": [1, 0, 0, 0, 0, 0, 1],
        "multiplicity": 1,
        "dimension": 832,
        "role_under_c": "kernel"
      },
      {
        "highest_weight": "omega_6",
        "dynkin_labels": [0, 0, 0, 0, 0, 1, 0],
        "multiplicity": 1,
        "dimension": 64,
        "role_under_c": "image"
      }
    ],
    "kernel": "V(omega_1 + omega_7)",
    "cokernel": "0",
    "image": "V(omega_6)",
    "kernel_highest_weight": "omega_1 + omega_7"
  },
  "product_b_consumed_table": {
    "expression": "V(omega_2) tensor V(omega_6)",
    "total_dimension": 5824,
    "summands": [
      "V(omega_2 + omega_6)",
      "V(omega_1 + omega_7)",
      "V(omega_6)"
    ],
    "multiplicity_of_V_omega6": 1,
    "V_omega1_plus_omega7_status": "present_multiplicity_1"
  },
  "finite_control_status": {
    "FC_IRR": "closed_for_Product_A_kernel_irreducibility",
    "FC_MULT": "closed_for_Product_B_V_omega6_multiplicity_but_not_a_unique_common_row_selector",
    "FC_HW": "closed_for_Product_A_kernel_highest_weight",
    "common_row_count": 2,
    "common_rows": [
      "V(omega_1 + omega_7)",
      "V(omega_6)"
    ],
    "finite_common_row_uniqueness": false,
    "selector_identity": "blocked"
  },
  "selector_identity_status": {
    "K_IG_family_identity_verified": false,
    "source_natural_projection_to_V_omega6_verified": false,
    "V_omega1_plus_omega7_rival_eliminated": false,
    "proof_restart_allowed": false
  },
  "rollback_conditions": [
    "Product_A_decomposition_has_additional_summands",
    "ker_c_is_not_V_omega1_plus_omega7",
    "cokernel_c_is_nonzero",
    "Product_B_receipt_overturned",
    "omega_6_omega_7_convention_reversed",
    "target_generation_count_or_desired_uniqueness_used_as_D7_evidence"
  ]
}
```
