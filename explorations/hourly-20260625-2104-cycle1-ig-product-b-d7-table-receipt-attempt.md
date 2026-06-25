---
title: "Hourly 20260625 2104 Cycle 1 IG Product B D7 Table Receipt Attempt"
date: "2026-06-25"
run_id: "hourly-20260625-2104"
cycle: 1
lane: "2 IG Product B"
doc_type: product_b_d7_table_receipt_attempt
artifact_id: "ProductBFullD7SummandMultiplicityDimensionTableReceiptAttempt_2104_C1_L2_V1"
verdict: "closed_product_b_table"
owned_path: "explorations/hourly-20260625-2104-cycle1-ig-product-b-d7-table-receipt-attempt.md"
companion_audit: "tests/hourly_20260625_2104_cycle1_receipt_attempts_audit.py"
---

# Hourly 20260625 2104 Cycle 1 IG Product B D7 Table Receipt Attempt

## 1. Verdict

Verdict: **closed for the Product B table receipt; downstream IG remains blocked**.

This lane produced a concrete Product B table candidate for:

```text
ProductBFullD7SummandMultiplicityDimensionTableReceipt_V1
B = V(omega_2) tensor V(omega_6)
```

The candidate table is:

| summand | Dynkin labels | multiplicity | dimension |
|---|---:|---:|---:|
| `V(omega_2 + omega_6)` | `[0,1,0,0,0,1,0]` | 1 | 4928 |
| `V(omega_1 + omega_7)` | `[1,0,0,0,0,0,1]` | 1 | 832 |
| `V(omega_6)` | `[0,0,0,0,0,1,0]` | 1 | 64 |

Dimension check:

```text
4928 + 832 + 64 = 5824 = 91 * 64
```

The coordinator audit independently checks the D7 character arithmetic using
weight characters and the Weyl dimension formula. That is enough to admit the
route-local Product B table receipt for the next cycle.

This does **not** promote any GU physics claim, Shiab uniqueness claim,
finite-control selector, or `K_IG` family identity. It only closes the Product B
table row and moves the next IG blocker to Product A plus the finite-control
and selector-identity gates.

## 2. Specific GU claim/bridge under test

The bridge under test is the IG/Shiab finite representation gate:

```text
ProductBFullD7SummandMultiplicityDimensionTableReceipt_V1
  -> Product A kernel/cokernel/highest-weight packet
  -> FC-IRR / FC-MULT / FC-HW
  -> K_IG selector or family-identity proof restart
```

The Product B receipt must come before Product A, finite-control gates, selector
identity, generation count, or any downstream GU-family proof restart.

The receipt target is not the desired multiplicity. It is the full D7 finite
table for `V(omega_2) tensor V(omega_6)`, including every summand,
multiplicity, dimension, total dimension check, and named rival presence or
absence.

## 3. Owned output path and sources read first

Owned output path:

```text
explorations/hourly-20260625-2104-cycle1-ig-product-b-d7-table-receipt-attempt.md
```

Sources read first:

| source | use |
|---|---|
| `RESEARCH-POSTURE.md` | Applied the no-target-import and constructive obstruction rules. |
| `process/runbooks/five-lane-frontier-run.md` | Used the decision-grade verdict vocabulary. |
| `process/runbooks/three-cycle-fifteen-hole-run.md` | Used the quality-hole fields and no-padding standard. |
| `explorations/hourly-20260625-2028-three-cycle-fifteen-hole-synthesis.md` | Confirmed Product B as the IG next-frontier producer receipt. |
| `explorations/hourly-20260625-2028-cycle3-next-frontier-dependency-dag.md` | Confirmed Product B precedes Product A and finite-control gates. |
| `explorations/hourly-20260625-2028-cycle1-ig-product-b-d7-delta-transcript.md` | Inherited the missing Product B full table target. |
| `explorations/hourly-20260625-1802-cycle2-ig-product-b-first-admission-gate.md` | Inherited the Product B first rule and 5824 dimension check. |
| `explorations/hourly-20260625-1702-cycle2-ig-finite-transcript-admission-matrix.md` | Inherited the finite transcript admission matrix and no-bypass rule. |

Additional context consulted after the required first reads:

| source | use |
|---|---|
| `canon/shiab-existence-cl95.md` | Checked current canon scope: existence only, not uniqueness or selector identity. |
| `explorations/sc1-oq1a-d7-clebsch-gordan-cas-2026-06-23.md` | Located the older chirality exclusion claim that this Product B table candidate contradicts. |

## 4. Strongest positive construction attempt

I used the repo's D7 convention:

```text
omega_1 = vector
omega_2 = two-form / adjoint
omega_6 = positive half-spin
omega_7 = negative half-spin
```

The construction was an exact finite highest-weight computation:

1. Realize D7 in the standard `e_i` basis with positive roots `e_i +/- e_j`.
2. Use `omega_6 = 1/2(e_1 + ... + e_6 - e_7)`.
3. Use `V(omega_2)` as the adjoint representation, whose nonzero weights are
   the D7 roots and whose zero weight has rank multiplicity 7.
4. Add adjoint roots to the spinor highest weight `omega_6`.
5. Keep dominant weights. The only dominant `omega_6 + root` outputs are:

```text
omega_2 + omega_6
omega_1 + omega_7
```

6. Include the adjoint action summand `omega_6` from the zero-weight/action
   component.
7. Compute dimensions by the D7 Weyl dimension formula.
8. Check that the three dimensions sum to the full product dimension `91 * 64`.

Raw computation transcript summary:

```json
{
  "python": "3.14.3",
  "platform": "Windows-11-10.0.26200-SP0",
  "root_system": "D7",
  "product": "V(omega_2) tensor V(omega_6)",
  "input_dimensions": {
    "dim_V_omega2": 91,
    "dim_V_omega6": 64
  },
  "dominant_weights_from_omega6_plus_adjoint_roots": [
    "omega_2 + omega_6",
    "omega_1 + omega_7"
  ],
  "zero_weight_action_summand": "omega_6",
  "summands": [
    {
      "highest_weight": "omega_2 + omega_6",
      "dynkin_labels": [0, 1, 0, 0, 0, 1, 0],
      "multiplicity": 1,
      "dimension": 4928
    },
    {
      "highest_weight": "omega_1 + omega_7",
      "dynkin_labels": [1, 0, 0, 0, 0, 0, 1],
      "multiplicity": 1,
      "dimension": 832
    },
    {
      "highest_weight": "omega_6",
      "dynkin_labels": [0, 0, 0, 0, 0, 1, 0],
      "multiplicity": 1,
      "dimension": 64
    }
  ],
  "dimension_sum": 5824,
  "input_dimension_product": 5824,
  "multiplicity_of_V_omega6": 1,
  "named_rival_rows": {
    "V(omega_7)": "absent from the three-row table",
    "V(omega_1 + omega_7)": "present with multiplicity 1 and dimension 832"
  },
  "target_import_used": false
}
```

This did not use generation count, desired uniqueness, Product A output, or a
downstream selector identity as evidence. The only numerical inputs were the D7
root system, the omega convention, and the Weyl dimension formula.

## 5. First exact obstruction or missing proof/source object

The Product B table obstruction is closed route-locally by the coordinator
audit:

```text
tests/hourly_20260625_2104_cycle1_receipt_attempts_audit.py
```

The first remaining IG obstruction is downstream:

```text
ProductAFullKernelCokernelHighestWeightPacket_V1
```

Product A, the finite-control gates, and selector identity cannot be inferred
from Product B. They now become the next sequential IG objects.

There is also a claim-consistency obstruction. The older narrow positive said
`V(omega_1 + omega_7)` is chirality-excluded from Product B. This computation
puts `V(omega_1 + omega_7)` inside Product B with multiplicity 1. That means the
old chirality screen cannot be used unchanged.

## 6. What would change if the receipt closed

If the Product B receipt closes with this table:

```text
FC-MULT for Product B no longer blocks on missing finite data.
Multiplicity of V(omega_6) in Product B is 1.
V(omega_7) is absent.
V(omega_1 + omega_7) is present, not excluded.
Product A remains next and cannot be bypassed.
```

The most important change is negative for the older uniqueness route: any
argument that used absence of `V(omega_1 + omega_7)` in Product B must be
revised or demoted. If Product A later retains the usual
`V(omega_6) plus V(omega_1 + omega_7)` shape, then Product B shares both rows,
not only `V(omega_6)`. This artifact does not close that Product A comparison,
but it makes the old Product B rival-exclusion claim unsafe.

## 7. Rollback/falsification condition

Rollback this receipt attempt if any independent admissible D7 computation or
formal proof shows one of the following:

```text
dimension(V(omega_2 + omega_6)) != 4928
dimension(V(omega_1 + omega_7)) != 832
Product B omits V(omega_1 + omega_7)
Product B contains V(omega_7)
Product B contains any additional summand
any listed multiplicity is not 1
dimension sum != 5824
the omega_6/omega_7 convention used here is opposite to the repo convention
```

If the omega convention is found reversed, the table should be relabeled under
the corrected convention rather than used as-is.

## 8. Next meaningful computation/proof/source step

The next meaningful step is Product A, not selector restart:

```text
ProductAFullKernelCokernelHighestWeightPacket_V1
```

The Product A packet must decide which of the Product B rows survive or cancel
inside the actual finite-control comparison. In particular, the presence of
`V(omega_1 + omega_7)` in Product B means the older chirality-exclusion shortcut
cannot be used.

## 9. Claim-status consistency result

Claim-status consistency is **triggered**.

No claim ledger was edited by this worker, but the artifact conflicts with a
previous narrow positive:

```text
old: V(omega_1 + omega_7) is excluded from Product B by chirality
new table candidate: V(omega_1 + omega_7) is present in Product B
```

This does not promote the IG selector or any major GU claim. It does require a
coordinator-level consistency pass before using the table downstream.

Current route state:

```text
Product B table receipt: route-locally closed
Product B table admitted to canon/ledger: no canon promotion; artifact/audit only
Product A packet: still not admitted
FC-IRR: still blocked
FC-MULT: conditionally ready only after Product B admission
FC-HW: still blocked
K_IG selector/family identity: not verified
claim promotion allowed: false
```

## 10. Machine-readable JSON summary

```json
{
  "artifact": "ProductBFullD7SummandMultiplicityDimensionTableReceiptAttempt_2104_C1_L2_V1",
  "artifact_path": "explorations/hourly-20260625-2104-cycle1-ig-product-b-d7-table-receipt-attempt.md",
  "run_id": "hourly-20260625-2104",
  "cycle": 1,
  "lane": "2 IG Product B",
  "route": "IG",
  "verdict_class": "closed_product_b_table",
  "accepted_receipt_count": 1,
  "receipt_candidate_count": 1,
  "target_import_used": false,
  "claim_status_consistency_triggered": true,
  "companion_audit": "tests/hourly_20260625_2104_cycle1_receipt_attempts_audit.py",
  "first_obstruction": "ProductAFullKernelCokernelHighestWeightPacket_V1_absent",
  "constructive_next_object": "ProductAFullKernelCokernelHighestWeightPacket_V1",
  "product_b_table_candidate": {
    "expression": "V(omega_2) tensor V(omega_6)",
    "input_dimension_product": 5824,
    "summands": [
      {
        "highest_weight": "omega_2 + omega_6",
        "dynkin_labels": [0, 1, 0, 0, 0, 1, 0],
        "multiplicity": 1,
        "dimension": 4928
      },
      {
        "highest_weight": "omega_1 + omega_7",
        "dynkin_labels": [1, 0, 0, 0, 0, 0, 1],
        "multiplicity": 1,
        "dimension": 832
      },
      {
        "highest_weight": "omega_6",
        "dynkin_labels": [0, 0, 0, 0, 0, 1, 0],
        "multiplicity": 1,
        "dimension": 64
      }
    ],
    "dimension_sum": 5824,
    "multiplicity_of_V_omega6": 1,
    "V_omega7_status": "absent",
    "V_omega1_plus_omega7_status": "present_multiplicity_1"
  },
  "proof_restart_allowed": false,
  "downstream_restart_allowed": false,
  "claim_promotion_allowed": false,
  "product_a_prioritized_next": true
}
```
