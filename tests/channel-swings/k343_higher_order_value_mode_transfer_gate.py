#!/usr/bin/env python3
"""Audit K341 transfer and compile the exact order-eight--twelve coherence interface.

K341 is a validated order-seven value enclosure, not a dimension-free rule.
This gate replays every K179 path at orders eight through twelve, preserves the
complete coherent quadratic forms, and identifies the first genuinely new
determinant ranks before any numerical value is attempted.
"""

from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
import sys
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[2]
K179_PATH = Path(__file__).with_name("k179_matched_normal_order_coefficient_family.py")
K279 = ROOT / "lab/process/k279-higher-order-andreief-structural-closure.json"
K305 = ROOT / "lab/process/k305-order-seven-coherent-bordered-functional-compiler.json"
K341 = ROOT / "lab/process/k341-order-seven-complete-barycentric-value.json"
OUTPUT = ROOT / "lab/process/k343-higher-order-value-mode-transfer-gate.json"
ORDERS = tuple(range(8, 13))
EXPECTED = {
    8: (192, 23, 1296, 2400, 4, (1, 3, 5, 7)),
    9: (256, 20, 2368, 4480, 5, (2, 4, 6, 8)),
    10: (480, 28, 6890, 13300, 5, (1, 3, 5, 7, 9)),
    11: (640, 24, 12920, 25200, 6, (2, 4, 6, 8, 10)),
    12: (1152, 33, 35352, 69552, 6, (1, 3, 5, 7, 9, 11)),
}


def load_k179():
    spec = importlib.util.spec_from_file_location("k179_for_k343", K179_PATH)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {K179_PATH}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


K179 = load_k179()


def canonical_path(term: dict[str, Any]) -> dict[str, Any]:
    return {
        "contraction_id": str(term["contraction_id"]),
        "old_position": int(term["old_position"]),
        "coefficient": int(term["exact_operator_coefficient"]),
        "output_letters": list(term["output_letters"]),
        "output_variable_provenance": [int(value) for value in term["output_variable_provenance"]],
        "species_multiplicities": {
            str(key): int(value)
            for key, value in sorted(term["antisymmetrizer_normalization"]["species_multiplicities"].items())
        },
    }


def digest(payload: Any) -> str:
    encoded = json.dumps(payload, sort_keys=True, separators=(",", ":")).encode()
    return "sha256:" + hashlib.sha256(encoded).hexdigest()


def group_rows(order: int, terms: list[dict[str, Any]]) -> list[dict[str, Any]]:
    groups: dict[tuple[int, str], list[dict[str, Any]]] = defaultdict(list)
    for term in terms:
        if int(term["order"]) == order:
            groups[(int(term["seed_impurity"]), str(term["output_signature"]))].append(term)
    rows = []
    for (seed, signature), paths in sorted(groups.items()):
        canonical = [canonical_path(path) for path in paths]
        pair_interface = [
            {
                "left": left["contraction_id"],
                "right": right["contraction_id"],
                "coefficient_product": left["coefficient"] * right["coefficient"],
            }
            for index, left in enumerate(canonical)
            for right in canonical[index:]
        ]
        multiplicities = canonical[0]["species_multiplicities"]
        if any(row["species_multiplicities"] != multiplicities for row in canonical):
            raise AssertionError("coherent group changed species multiplicity")
        size = len(paths)
        rows.append({
            "group_id": f"order{order}:seed{seed}:{signature}",
            "seed_impurity": seed,
            "output_signature": signature,
            "path_count": size,
            "old_position_support": sorted({row["old_position"] for row in canonical}),
            "coefficient_histogram": {
                str(key): value for key, value in sorted(Counter(row["coefficient"] for row in canonical).items())
            },
            "species_multiplicities": multiplicities,
            "maximum_species_determinant_rank": max(multiplicities.values()),
            "upper_triangle_gram_entries": size * (size + 1) // 2,
            "ordered_quadratic_terms": size * size,
            "off_diagonal_ordered_cross_terms": size * (size - 1),
            "coherent_quadratic_form": "c_G^T K_G c_G; form the complete group value before absolute enclosure",
            "path_interface_sha256": digest(canonical),
            "upper_triangle_pair_interface_sha256": digest(pair_interface),
        })
    return rows


def build() -> dict[str, Any]:
    k279 = json.loads(K279.read_text())
    k305 = json.loads(K305.read_text())
    k341 = json.loads(K341.read_text())
    terms = K179.coefficient_family()
    orders = []
    all_groups = []
    for order in ORDERS:
        rows = group_rows(order, terms)
        all_groups.extend(rows)
        path_count = sum(row["path_count"] for row in rows)
        upper = sum(row["upper_triangle_gram_entries"] for row in rows)
        ordered = sum(row["ordered_quadratic_terms"] for row in rows)
        max_rank = max(row["maximum_species_determinant_rank"] for row in rows)
        positions = tuple(sorted({position for row in rows for position in row["old_position_support"]}))
        expected = EXPECTED[order]
        if (path_count, len(rows), upper, ordered, max_rank, positions) != expected:
            raise AssertionError(f"order {order} K179 transfer census changed")
        orders.append({
            "order": order,
            "paths": path_count,
            "groups": len(rows),
            "upper_triangle_gram_entries": upper,
            "ordered_quadratic_terms": ordered,
            "off_diagonal_ordered_cross_terms": ordered - path_count,
            "old_position_support": list(positions),
            "maximum_species_determinant_rank": max_rank,
            "native_prefactor": f"(2*pi)^-{order + 2}",
            "positive_time_variables": 2 * (order + 1),
            "radial_jacobian_power": 2 * order + 1,
            "crude_origin_power_after_bessel_factors": order - 1,
            "K280_rank_at_most_four_calculus_suffices": max_rank <= 4,
            "new_rank_calculus_required": [] if max_rank <= 4 else list(range(5, max_rank + 1)),
            "group_interface_sha256": digest(rows),
        })

    higher_entries = sum(row["upper_triangle_gram_entries"] for row in orders)
    if higher_entries != k279["totals"]["gram_entries"] - 408:
        raise AssertionError("K279 higher-order Gram total changed")
    if k305["fixed_control"]["coherent_groups"] != 4 or k341["fixed_control"]["coherent_group_count"] != 4:
        raise AssertionError("order-seven transfer control changed")

    return {
        "schema_version": "1.0",
        "result_id": "K343-HIGHER-ORDER-VALUE-MODE-TRANSFER-GATE",
        "created": "2026-09-22",
        "classification": "INTERNAL_STRUCTURAL_ONLY",
        "direction": "observed_to_native",
        "fixed_control": {
            "predecessor_manifests": [
                "lab/process/k179-matched-normal-order-coefficient-family-wave.json",
                "lab/process/k279-higher-order-andreief-structural-closure.json",
                "lab/process/k305-order-seven-coherent-bordered-functional-compiler.json",
                "lab/process/k341-order-seven-complete-barycentric-value.json",
            ],
            "orders": list(ORDERS),
            "higher_order_paths": sum(row["paths"] for row in orders),
            "higher_order_groups": sum(row["groups"] for row in orders),
            "higher_order_upper_triangle_gram_entries": higher_entries,
            "higher_order_ordered_quadratic_terms": sum(row["ordered_quadratic_terms"] for row in orders),
            "complete_group_interface_sha256": digest(all_groups),
        },
        "orders": orders,
        "exact_generic_coherence_interface": {
            "group_records": all_groups,
            "coherent_value_rule": "for each group G evaluate c_G^T K_G c_G with K_G the factorial-free species-determinant Gram kernel, then sum groups before the declared outer enclosure",
            "upper_triangle_reconstruction": "diagonal entries once and off-diagonal entries twice; equivalently retain every ordered path pair",
            "all_K179_coefficients_retained": True,
            "all_contracted_positions_retained": True,
            "all_coherent_cross_terms_retained": True,
            "occurrencewise_absolute_value_permitted": False,
            "canonical_interface_is_deterministic": True,
        },
        "transfer_audit": {
            "K341_is_dimension_free_integrator": False,
            "literal_K341_extension_to_orders_8_through_12_is_valid": False,
            "reusable": [
                "factorial-free species-determinant kernel from K279",
                "complete coherent group assembly before absolute enclosure",
                "rho-tail versus simplex-face error separation",
                "scaled zero-safe Bessel entry calculus through determinant rank four",
            ],
            "order_seven_specific_inputs_not_reusable_as_if_generic": [
                "K305 four-group D4-times-bordered-B5 compiler",
                "K299 six-axis barycentric/Peano weights",
                "K340 eight-split two-sector terminal atlas",
                "K334 twelve-cell radial/projective cover and checksum",
                "K341 (2*pi)^-9 normalization and order-seven tail powers",
            ],
            "first_new_rank_obstruction": "order nine requires species determinants of rank five; orders eleven and twelve require rank six",
            "order_eight_status": "algebraically within the existing rank-four Bessel calculus, but still lacks an order-eight native cubature/face atlas and group-level interval evaluator",
            "orders_nine_through_twelve_status": "require new zero-safe scaled rank-five/rank-six determinant face calculus before numerical cubature",
        },
        "decision": {
            "direct_reuse_route_rejected": True,
            "exact_higher_order_coherence_interface_emitted": True,
            "numerical_order_eight_value_emitted": False,
            "orders_eight_through_twelve_action_column_emitted": False,
            "complete_R_ref_residual_emitted": False,
            "native_K152_interval_emitted": False,
            "next_exact_input": "construct the order-eight native value cubature and group-level interval evaluator on this exact coherence interface; validate it against all 1,296 order-eight Gram entries before building the rank-five calculus required at order nine",
        },
        "release_test": {
            "all_2720_higher_order_paths_replayed": sum(row["paths"] for row in orders) == 2720,
            "all_128_higher_order_groups_replayed": sum(row["groups"] for row in orders) == 128,
            "all_58826_higher_order_upper_triangle_entries_replayed": higher_entries == 58826,
            "all_coefficients_positions_and_cross_terms_retained": True,
            "order_eight_rank_four_boundary_proved": orders[0]["maximum_species_determinant_rank"] == 4,
            "order_nine_rank_five_boundary_proved": orders[1]["maximum_species_determinant_rank"] == 5,
            "order_eleven_rank_six_boundary_proved": orders[3]["maximum_species_determinant_rank"] == 6,
            "false_numeric_extension_rejected": True,
            "native_K152_interval_emitted": False,
        },
        "ledger_effect": {
            "SC-ACT-01": "ASSERTS_UNCHANGED",
            "SC-ACT-02": "ASSERTS_UNCHANGED",
            "SC-ACT-06": "ASSERTS_UNCHANGED",
            "SC-META-53": "UNCERTAIN_UNCHANGED",
            "LT-SM8": "NEEDS_UNCHANGED",
            "LT-GR6b": "NEEDS_UNCHANGED",
            "RA-F1": "NEEDS_UNCHANGED",
            "AC-F1": "NEEDS_UNCHANGED",
        },
        "source_routing": {
            "classification": "INTERNAL_STRUCTURAL_ONLY",
            "source_native_GU_mechanism_tested": False,
            "conditional_repository_Fock_construction_only": True,
        },
        "claim_ceiling": "Exact transfer gate and coherence interface for all K179 orders eight through twelve. It replays 2,720 paths, 128 coherent groups and 58,826 upper-triangle Gram entries, preserving every coefficient, contracted position and cross term. K341 is not a dimension-free integrator: order eight remains within rank four but needs a native order-eight cubature/face atlas, order nine first requires rank-five determinant calculus, and orders eleven and twelve require rank six. No higher-order numerical value, complete action column, R_ref residual, K152 interval, source/ledger move, canon, paper, public or physical claim is emitted.",
    }


def validate_payload(payload: dict[str, Any]) -> None:
    fixed = payload["fixed_control"]
    if fixed["higher_order_paths"] != 2720 or fixed["higher_order_groups"] != 128:
        raise AssertionError("higher-order path/group census changed")
    if fixed["higher_order_upper_triangle_gram_entries"] != 58826:
        raise AssertionError("higher-order Gram census changed")
    rows = {int(row["order"]): row for row in payload["orders"]}
    for order, expected in EXPECTED.items():
        row = rows[order]
        actual = (
            row["paths"], row["groups"], row["upper_triangle_gram_entries"],
            row["ordered_quadratic_terms"], row["maximum_species_determinant_rank"],
            tuple(row["old_position_support"]),
        )
        if actual != expected:
            raise AssertionError(f"order {order} transfer row changed")
    interface = payload["exact_generic_coherence_interface"]
    if not all(interface[key] for key in (
        "all_K179_coefficients_retained", "all_contracted_positions_retained",
        "all_coherent_cross_terms_retained", "canonical_interface_is_deterministic",
    )) or interface["occurrencewise_absolute_value_permitted"]:
        raise AssertionError("coherence interface weakened")
    audit = payload["transfer_audit"]
    if audit["K341_is_dimension_free_integrator"] or audit["literal_K341_extension_to_orders_8_through_12_is_valid"]:
        raise AssertionError("false K341 transfer accepted")
    if rows[8]["new_rank_calculus_required"] or rows[9]["new_rank_calculus_required"] != [5] or rows[11]["new_rank_calculus_required"] != [5, 6]:
        raise AssertionError("determinant-rank boundary changed")
    decision = payload["decision"]
    if not decision["direct_reuse_route_rejected"] or not decision["exact_higher_order_coherence_interface_emitted"]:
        raise AssertionError("transfer decision changed")
    if decision["numerical_order_eight_value_emitted"] or decision["orders_eight_through_twelve_action_column_emitted"] or decision["complete_R_ref_residual_emitted"] or decision["native_K152_interval_emitted"]:
        raise AssertionError("downstream numerical result overclaimed")
    release = payload["release_test"]
    positives = [key for key, value in release.items() if key != "native_K152_interval_emitted" and isinstance(value, bool)]
    if not all(release[key] for key in positives) or release["native_K152_interval_emitted"]:
        raise AssertionError("K343 release test failed")


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
