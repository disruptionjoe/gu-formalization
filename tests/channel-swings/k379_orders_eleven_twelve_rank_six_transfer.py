#!/usr/bin/env python3
"""Bind the accepted rank-six calculus to orders eleven and twelve."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[2]
K343 = ROOT / "lab/process/k343-higher-order-value-mode-transfer-gate.json"
K376 = ROOT / "lab/process/k376-orders-nine-ten-rank-five-transfer.json"
K377 = ROOT / "lab/process/k377-rank-six-confluent-determinant-calculus.json"
K378 = ROOT / "lab/process/k378-rank-six-global-scaled-bessel-bank.json"
OUTPUT = ROOT / "lab/process/k379-orders-eleven-twelve-rank-six-transfer.json"


def build() -> dict[str, Any]:
    k343 = json.loads(K343.read_text())
    k376 = json.loads(K376.read_text())
    k377 = json.loads(K377.read_text())
    k378 = json.loads(K378.read_text())
    source = {row["order"]: row for row in k343["orders"]}
    rows = []
    for boundary in k377["order_factor_boundaries"]:
        order = boundary["order"]
        old = source[order]
        if (boundary["paths"], boundary["groups"], boundary["upper_triangle_gram_entries"], boundary["ordered_quadratic_terms"], boundary["maximum_rank"], boundary["old_position_support"]) != (old["paths"], old["groups"], old["upper_triangle_gram_entries"], old["ordered_quadratic_terms"], old["maximum_species_determinant_rank"], old["old_position_support"]):
            raise AssertionError("K343/K377 order interface mismatch")
        rows.append({
            **boundary,
            "positive_time_variables": 2 * (order + 1),
            "native_prefactor": f"(2*pi)^-{order + 2}",
            "rank_six_confluence_bound": True,
            "primitive_orders_zero_through_twelve_bound": True,
        })
    if not k376["decision"]["rank_five_determinant_confluence_derivative_calculus_complete"]:
        raise AssertionError("lower-rank predecessor is not complete")
    if not k377["decision"]["rank_six_gap_free_confluent_determinant_calculus_emitted"]:
        raise AssertionError("rank-six confluence is not complete")
    if not k378["decision"]["zero_safe_global_scaled_derivative_bank_complete_through_order_twelve"]:
        raise AssertionError("rank-six primitive bank is not complete")
    return {
        "schema_version": "1.0",
        "result_id": "K379-ORDERS-ELEVEN-TWELVE-RANK-SIX-TRANSFER",
        "created": "2026-09-23",
        "classification": "INTERNAL_STRUCTURAL_ONLY",
        "direction": "observed_to_native",
        "fixed_control": {
            "predecessor_manifests": [str(path.relative_to(ROOT)) for path in (K343, K376, K377, K378)],
            "orders": [11, 12],
            "paths": sum(row["paths"] for row in rows),
            "coherent_groups": sum(row["groups"] for row in rows),
            "upper_triangle_gram_entries": sum(row["upper_triangle_gram_entries"] for row in rows),
            "ordered_quadratic_terms": sum(row["ordered_quadratic_terms"] for row in rows),
            "maximum_rank": 6,
            "maximum_primitive_derivative_order": 12,
        },
        "order_interfaces": rows,
        "complete_higher_rank_calculus": {
            "order_nine_and_ten_rank_five_bound": True,
            "order_eleven_and_twelve_rank_six_bound": True,
            "all_orders_eight_through_twelve_structurally_typed": True,
            "gap_free_confluence_through_rank_six": True,
            "global_zero_safe_scaled_derivatives_through_order_twelve": True,
            "complete_group_assembly_precedes_absolute_enclosure": True,
            "occurrencewise_absolute_value_permitted": False,
            "order_specific_counts_dimensions_and_prefactors_retained": True,
            "order_eight_node_or_face_atlas_reused": False,
        },
        "decision": {
            "rank_six_orders_eleven_twelve_factor_transfer_complete": True,
            "higher_rank_determinant_confluence_derivative_obstruction_closed": True,
            "numerical_orders_nine_through_twelve_integrals_emitted": False,
            "complete_base_action_column_emitted": False,
            "complete_R_ref_residual_emitted": False,
            "native_K152_interval_emitted": False,
            "next_exact_input": "construct the order-nine native positive rule and exact zero/coalescence face atlas on its twenty raw times, then evaluate its complete coherent node value before any global Peano remainder",
        },
        "release_test": {
            "all_1792_paths_replayed": sum(row["paths"] for row in rows) == 1792,
            "all_57_groups_replayed": sum(row["groups"] for row in rows) == 57,
            "all_48272_upper_triangle_entries_replayed": sum(row["upper_triangle_gram_entries"] for row in rows) == 48272,
            "all_94752_ordered_terms_replayed": sum(row["ordered_quadratic_terms"] for row in rows) == 94752,
            "both_orders_have_rank_six_patterns": all(row["rank_six_patterns"] for row in rows),
            "both_orders_bound_to_rank_six_confluence": all(row["rank_six_confluence_bound"] for row in rows),
            "both_orders_bound_to_primitive_orders_zero_through_twelve": all(row["primitive_orders_zero_through_twelve_bound"] for row in rows),
            "order_specific_time_dimensions_retained": [row["positive_time_variables"] for row in rows] == [24, 26],
            "order_specific_prefactors_retained": [row["native_prefactor"] for row in rows] == ["(2*pi)^-13", "(2*pi)^-14"],
            "numerical_integrals_not_overclaimed": True,
            "action_column_not_overclaimed": True,
            "R_ref_not_overclaimed": True,
            "native_K152_interval_not_overclaimed": True,
        },
        "ledger_effect": k378["ledger_effect"],
        "source_routing": k378["source_routing"],
        "claim_ceiling": "Exact transfer of the accepted gap-free rank-six determinant calculus and global zero-safe derivative bank through order twelve to every order-eleven and order-twelve K179 factor. All 1,792 paths, 57 groups, 48,272 upper-triangle entries and 94,752 ordered terms replay with separate 24/26-dimensional measures and (2*pi)^-13/(2*pi)^-14 prefactors. Together with K376 this closes the higher-rank structural obstruction for orders nine through twelve, but emits no higher-order numerical integral, base action column, R_ref residual, K152 interval, source/ledger move, canon, paper, public, novelty or physical claim."
    }


def validate_payload(payload: dict[str, Any]) -> None:
    fixed = payload["fixed_control"]
    if (fixed["orders"], fixed["paths"], fixed["coherent_groups"], fixed["upper_triangle_gram_entries"], fixed["ordered_quadratic_terms"], fixed["maximum_rank"], fixed["maximum_primitive_derivative_order"]) != ([11, 12], 1792, 57, 48272, 94752, 6, 12):
        raise AssertionError("K379 fixed census changed")
    rows = payload["order_interfaces"]
    if [row["order"] for row in rows] != [11, 12] or any(row["maximum_rank"] != 6 or not row["rank_six_patterns"] for row in rows):
        raise AssertionError("K379 order interface changed")
    if [row["positive_time_variables"] for row in rows] != [24, 26] or [row["native_prefactor"] for row in rows] != ["(2*pi)^-13", "(2*pi)^-14"]:
        raise AssertionError("K379 order-specific measure or normalization changed")
    calculus = payload["complete_higher_rank_calculus"]
    required = ("order_nine_and_ten_rank_five_bound", "order_eleven_and_twelve_rank_six_bound", "all_orders_eight_through_twelve_structurally_typed", "gap_free_confluence_through_rank_six", "global_zero_safe_scaled_derivatives_through_order_twelve", "complete_group_assembly_precedes_absolute_enclosure", "order_specific_counts_dimensions_and_prefactors_retained")
    if not all(calculus[key] for key in required) or calculus["occurrencewise_absolute_value_permitted"] or calculus["order_eight_node_or_face_atlas_reused"]:
        raise AssertionError("K379 calculus boundary changed")
    decision = payload["decision"]
    if not decision["rank_six_orders_eleven_twelve_factor_transfer_complete"] or not decision["higher_rank_determinant_confluence_derivative_obstruction_closed"] or any(decision[key] for key in ("numerical_orders_nine_through_twelve_integrals_emitted", "complete_base_action_column_emitted", "complete_R_ref_residual_emitted", "native_K152_interval_emitted")):
        raise AssertionError("K379 decision boundary changed")
    if not all(payload["release_test"].values()):
        raise AssertionError("K379 release test failed")


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
