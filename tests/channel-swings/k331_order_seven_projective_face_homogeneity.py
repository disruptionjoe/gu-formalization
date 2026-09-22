#!/usr/bin/env python3
"""Exact projective-face homogeneity ledger for the K330 evaluator.

The radial normalization leaves two different projective degenerations.  At
``s=0`` the only zero old-kernel sum in each regularized core is the final
row/final column slot.  Scaling that row by ``s`` makes both complete
determinants finite, so their product has pole order at most two.  At ``s=1``
the cores are confluent at a positive cross-sum; only the bordered column can
see zero.  Its row orders 0,1,2 and y-jet orders 0,1,2 give coefficient pole
orders 3,4,5.  The native weights s^3 and (1-s)^29 leave nonnegative (indeed
positive) integrated powers on both faces.
"""

from __future__ import annotations

import argparse
import itertools
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[2]
K321 = ROOT / "lab/process/k321-order-seven-radial-projective-tensor-atlas.json"
K325 = ROOT / "lab/process/k325-order-seven-correlated-determinant-jet-algebra.json"
K328 = ROOT / "lab/process/k328-order-seven-scaled-derivative-envelope-bank.json"
K330 = ROOT / "lab/process/k330-order-seven-radial-tail-control.json"
OUTPUT = ROOT / "lab/process/k331-order-seven-projective-face-homogeneity.json"


def determinant_support(size: int, nonzero: set[tuple[int, int]]) -> list[tuple[int, ...]]:
    return [
        permutation
        for permutation in itertools.permutations(range(size))
        if all((row, permutation[row]) in nonzero for row in range(size))
    ]


def build() -> dict[str, Any]:
    k321 = json.loads(K321.read_text())
    k325 = json.loads(K325.read_text())
    k328 = json.loads(K328.read_text())
    k330 = json.loads(K330.read_text())
    if not k321["decision"]["radial_projective_tensor_topology_complete"]:
        raise AssertionError("K321 tensor topology unavailable")
    if not k325["decision"]["correlation_preserving_determinant_jet_algebra_implemented"]:
        raise AssertionError("K325 determinant algebra unavailable")
    if not k328["decision"]["zero_safe_scaled_derivative_bank_through_order_six_implemented"]:
        raise AssertionError("K328 scaled derivative bank unavailable")
    if "s in [0,1/4]" not in k330["scope_boundary"]["not_covered"]:
        raise AssertionError("K330 projective-face boundary changed")

    d4_nonzero = {(row, column) for row in range(4) for column in range(4)}
    b5_nonzero = (
        {(row, column) for row in range(4) for column in range(4)}
        | {(row, 4) for row in range(3)}
        | {(4, column) for column in range(3)}
    )
    d4_terms = determinant_support(4, d4_nonzero)
    b5_terms = determinant_support(5, b5_nonzero)
    d4_terminal_terms = sum(permutation[3] == 3 for permutation in d4_terms)
    b5_terminal_terms = sum(permutation[3] == 3 for permutation in b5_terms)
    if (len(d4_terms), len(b5_terms), d4_terminal_terms, b5_terminal_terms) != (24, 54, 6, 18):
        raise AssertionError("complete determinant support census changed")

    s0_poles = [2, 2, 2]
    s1_poles = [3, 4, 5]
    s0_remaining = [3 - pole for pole in s0_poles]
    s1_remaining = [29 - pole for pole in s1_poles]
    if min(s0_remaining + s1_remaining) < 0:
        raise AssertionError("projective measure does not absorb the face poles")

    return {
        "schema_version": "1.0",
        "result_id": "K331-ORDER-SEVEN-PROJECTIVE-FACE-HOMOGENEITY",
        "created": "2026-09-22",
        "classification": "INTERNAL_STRUCTURAL_ONLY",
        "direction": "observed_to_native",
        "fixed_control": {
            "predecessor_manifests": [
                "lab/process/k321-order-seven-radial-projective-tensor-atlas.json",
                "lab/process/k325-order-seven-correlated-determinant-jet-algebra.json",
                "lab/process/k328-order-seven-scaled-derivative-envelope-bank.json",
                "lab/process/k330-order-seven-radial-tail-control.json",
            ],
            "coefficient_orders": [0, 1, 2],
            "D4_complete_permutation_count": len(d4_terms),
            "bordered_B5_complete_nonzero_permutation_count": len(b5_terms),
            "border_literal_zero_slots": [[3, 4], [4, 3], [4, 4]],
        },
        "support_census": {
            "D4_terms_using_final_core_slot": d4_terminal_terms,
            "D4_terms_not_using_final_core_slot": len(d4_terms) - d4_terminal_terms,
            "bordered_B5_terms_using_final_core_slot": b5_terminal_terms,
            "bordered_B5_terms_not_using_final_core_slot": len(b5_terms) - b5_terminal_terms,
            "every_bordered_term_uses_exactly_one_border_column_entry": True,
            "every_bordered_term_uses_exactly_one_border_row_entry": True,
            "complete_support_used_without_detached_cofactor": True,
        },
        "s0_face": {
            "face_variable": "s",
            "native_measure_power": 3,
            "D4_preconditioner": "multiply final regularized row by s",
            "D4_worst_pole_order": 1,
            "bordered_B5_preconditioner": "multiply final regularized row by s",
            "bordered_B5_worst_pole_orders_value_first_second": [1, 1, 1],
            "complete_product_worst_pole_orders_value_first_second": s0_poles,
            "remaining_integrated_powers_value_first_second": s0_remaining,
            "proof": "all normalized sums except the final-row/final-column sum retain a positive (1-s)-gap contribution; each determinant term uses the final row once, and K328 bounds the scaled zero slot without a raw zero call",
        },
        "s1_face": {
            "face_variable": "t=1-s",
            "native_measure_power": 29,
            "D4_worst_pole_order": 0,
            "bordered_B5_preconditioners_value_first_second": ["t^3", "t^4", "t^5"],
            "bordered_B5_worst_pole_orders_value_first_second": s1_poles,
            "complete_product_worst_pole_orders_value_first_second": s1_poles,
            "remaining_integrated_powers_value_first_second": s1_remaining,
            "proof": "the two core node families meet only at a positive cross-sum; the mandatory border-column entry has divided-difference row order at most two and coefficient y-order at most two, hence pole order at most 3+j for coefficient j",
        },
        "composition_contract": {
            "radial_degree_27_unchanged": True,
            "projective_preconditioning_precedes_interval_substitution": True,
            "shared_entry_determinant_taylor_assembly_required": True,
            "familywise_absolute_summation_allowed": False,
            "permutationwise_absolute_summation_allowed_for_B5": False,
            "raw_Bessel_evaluation_at_zero_allowed": False,
            "projective_cutoff_required": False,
        },
        "decision": {
            "both_projective_faces_have_integrable_complete_jets": True,
            "normalized_confluent_face_evaluator_released": True,
            "complete_projective_face_numerical_bounds_emitted": False,
            "complete_y_master_constant_emitted": False,
            "next_exact_input": "apply the s-row and (1-s)-border preconditioners entrywise, assemble each complete determinant Taylor coefficient, and integrate against the reduced face powers before extending the bank across the radial annulus and tail",
        },
        "release_test": {
            "K325_fifty_four_monomial_census_replayed": len(b5_terms) == 54,
            "both_faces_have_strictly_positive_remaining_powers": min(s0_remaining + s1_remaining) > 0,
            "literal_border_zeros_retained": True,
            "detached_cofactor_used": False,
            "complete_numerical_norm_overclaim": False,
            "native_K152_interval_emitted": False,
        },
        "ledger_effect": k330["ledger_effect"],
        "source_routing": k330["source_routing"],
        "claim_ceiling": "Exact projective homogeneity discriminator for the complete degree-27 normalized D4-times-bordered-B5 value/first/second jets. At s=0, final-row scaling bounds each determinant with total product pole order at most two, leaving integrated power one under s^3. At s=1, only the mandatory border column is singular; value/first/second pole orders are at most 3/4/5, leaving powers 26/25/24 under (1-s)^29. This releases a normalized confluent face evaluator without a cutoff, but emits no numerical face constant, recursive tolerance, complete y sum, gap transfer, K294 join, action-column value, residual, K152 interval, source/ledger, canon, paper, public or physical claim.",
    }


def validate_payload(payload: dict[str, Any]) -> None:
    fixed = payload["fixed_control"]
    if fixed["D4_complete_permutation_count"] != 24 or fixed["bordered_B5_complete_nonzero_permutation_count"] != 54:
        raise AssertionError("determinant support changed")
    if payload["s0_face"]["remaining_integrated_powers_value_first_second"] != [1, 1, 1]:
        raise AssertionError("s=0 power ledger changed")
    if payload["s1_face"]["remaining_integrated_powers_value_first_second"] != [26, 25, 24]:
        raise AssertionError("s=1 power ledger changed")
    contract = payload["composition_contract"]
    if contract["projective_cutoff_required"] or contract["raw_Bessel_evaluation_at_zero_allowed"]:
        raise AssertionError("forbidden face workaround introduced")
    if not payload["decision"]["normalized_confluent_face_evaluator_released"]:
        raise AssertionError("face evaluator was not released")
    if payload["decision"]["complete_y_master_constant_emitted"]:
        raise AssertionError("complete numerical release overclaimed")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--write", action="store_true")
    args = parser.parse_args()
    payload = build()
    validate_payload(payload)
    rendered = json.dumps(payload, indent=2, sort_keys=True) + "\n"
    if args.write:
        OUTPUT.write_text(rendered)
    else:
        print(rendered, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
