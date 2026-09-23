#!/usr/bin/env python3
"""Evaluate K343's complete order-eight one-node coherent value in Arb.

Every one of the 1,296 upper-triangle Gram entries is assembled from the two
old-position K1 factors and the factorial-free species determinants.  The
complete coefficient quadratic form is restored group by group before any
enclosure.  K344's product Gauss--Laguerre weight and the native (2*pi)^-10
prefactor are then applied exactly once.  The result is the value of the
positive one-node rule, not an enclosure of the full order-eight integral.
"""

from __future__ import annotations

import argparse
import hashlib
import importlib.util
import itertools
import json
import math
import sys
from collections import defaultdict
from pathlib import Path
from typing import Any

from flint import arb, ctx


ROOT = Path(__file__).resolve().parents[2]
HERE = Path(__file__).resolve().parent
K179_PATH = HERE / "k179_matched_normal_order_coefficient_family.py"
K344 = ROOT / "lab/process/k344-order-eight-gauss-laguerre-face-atlas.json"
K343 = ROOT / "lab/process/k343-higher-order-value-mode-transfer-gate.json"
OUTPUT = ROOT / "lab/process/k345-order-eight-group-interval-evaluator.json"

ORDER = 8
SHIFT = 256
TIME_COUNT_PER_SIDE = 9
EXPECTED_PATHS = 192
EXPECTED_GROUPS = 23
EXPECTED_ENTRIES = 1296

ctx.dps = 180
ctx.threads = 1


def load_k179():
    spec = importlib.util.spec_from_file_location("k179_for_k345", K179_PATH)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {K179_PATH}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


K179 = load_k179()


def digest(payload: Any) -> str:
    encoded = json.dumps(payload, sort_keys=True, separators=(",", ":")).encode()
    return "sha256:" + hashlib.sha256(encoded).hexdigest()


def lower_text(value: arb) -> str:
    return repr(math.nextafter(float(value.lower()), -math.inf))


def upper_text(value: arb) -> str:
    return repr(math.nextafter(float(value.upper()), math.inf))


def determinant(matrix: list[list[arb]]) -> arb:
    total = arb(0)
    for permutation in itertools.permutations(range(len(matrix))):
        inversions = sum(
            permutation[left] > permutation[right]
            for left in range(len(permutation))
            for right in range(left + 1, len(permutation))
        )
        term = arb(-1 if inversions % 2 else 1)
        for row, column in enumerate(permutation):
            term *= matrix[row][column]
        total += term
    return total


def occurrences(term: dict[str, Any]) -> dict[str, list[int]]:
    result: dict[str, list[int]] = defaultdict(list)
    for position, species in zip(term["output_variable_provenance"], term["output_letters"], strict=True):
        result[str(species)].append(int(position))
    return dict(sorted(result.items()))


def cumulative_times() -> dict[int, arb]:
    return {position: arb(TIME_COUNT_PER_SIDE + 1 - position) / SHIFT for position in range(1, TIME_COUNT_PER_SIDE + 1)}


def gram_entry(left: dict[str, Any], right: dict[str, Any], cumulative: dict[int, arb]) -> arb:
    value = 2 * cumulative[int(left["old_position"])].bessel_k(1)
    value *= 2 * cumulative[int(right["old_position"])].bessel_k(1)
    left_occurrences = occurrences(left)
    right_occurrences = occurrences(right)
    if left_occurrences.keys() != right_occurrences.keys():
        raise AssertionError("species support changed inside a coherent group")
    for species in left_occurrences:
        left_positions = left_occurrences[species]
        right_positions = right_occurrences[species]
        matrix = [
            [2 * (cumulative[row] + cumulative[column]).bessel_k(1) for column in right_positions]
            for row in left_positions
        ]
        value *= determinant(matrix)
    return value


def group_terms() -> dict[tuple[int, str], list[dict[str, Any]]]:
    groups: dict[tuple[int, str], list[dict[str, Any]]] = defaultdict(list)
    for term in K179.coefficient_family():
        if int(term["order"]) == ORDER:
            groups[(int(term["seed_impurity"]), str(term["output_signature"]))].append(term)
    return dict(sorted(groups.items()))


def build() -> dict[str, Any]:
    k344 = json.loads(K344.read_text())
    k343 = json.loads(K343.read_text())
    groups = group_terms()
    paths = sum(len(rows) for rows in groups.values())
    entries = sum(len(rows) * (len(rows) + 1) // 2 for rows in groups.values())
    if (paths, len(groups), entries) != (EXPECTED_PATHS, EXPECTED_GROUPS, EXPECTED_ENTRIES):
        raise AssertionError("order-eight evaluator census changed")
    if not k344["decision"]["native_order_eight_positive_value_rule_emitted"]:
        raise AssertionError("K344 native rule unavailable")
    k343_order = next(row for row in k343["orders"] if row["order"] == ORDER)
    if k344["fixed_control"]["K343_group_interface_sha256"] != k343_order["group_interface_sha256"]:
        raise AssertionError("K343/K344 interface mismatch")

    cumulative = cumulative_times()
    group_rows = []
    complete_total = arb(0)
    ordered_total = arb(0)
    all_entry_intervals: list[dict[str, Any]] = []
    symmetry_checks = 0
    strictly_positive_gram_entries = 0
    ordered_entry_count = 0
    for (seed, signature), terms in groups.items():
        group_id = f"order{ORDER}:seed{seed}:{signature}"
        upper_total = arb(0)
        entry_rows = []
        for left_index, left in enumerate(terms):
            for right_index in range(left_index, len(terms)):
                right = terms[right_index]
                value = gram_entry(left, right, cumulative)
                transposed = gram_entry(right, left, cumulative)
                if not (value - transposed).contains(0):
                    raise AssertionError("Gram symmetry failed")
                symmetry_checks += 1
                if value.lower() > 0:
                    strictly_positive_gram_entries += 1
                coefficient = int(left["exact_operator_coefficient"]) * int(right["exact_operator_coefficient"])
                weighted = value * coefficient
                upper_total += weighted if left_index == right_index else 2 * weighted
                entry_rows.append(
                    {
                        "left": str(left["contraction_id"]),
                        "right": str(right["contraction_id"]),
                        "coefficient_product": coefficient,
                        "gram_lower": lower_text(value),
                        "gram_upper": upper_text(value),
                    }
                )
        full_ordered = arb(0)
        for left in terms:
            for right in terms:
                full_ordered += (
                    int(left["exact_operator_coefficient"])
                    * int(right["exact_operator_coefficient"])
                    * gram_entry(left, right, cumulative)
                )
                ordered_entry_count += 1
        if not (upper_total - full_ordered).contains(0):
            raise AssertionError("upper-triangle reconstruction lost an ordered cross term")
        if upper_total.lower() < 0:
            raise AssertionError("coherent node Gram form is not positive")
        complete_total += upper_total
        ordered_total += full_ordered
        all_entry_intervals.extend({"group_id": group_id, **row} for row in entry_rows)
        group_rows.append(
            {
                "group_id": group_id,
                "path_count": len(terms),
                "upper_triangle_entries": len(entry_rows),
                "ordered_quadratic_terms": len(terms) ** 2,
                "coherent_node_value_lower": lower_text(upper_total),
                "coherent_node_value_upper": upper_text(upper_total),
                "entry_interval_sha256": digest(entry_rows),
            }
        )

    if not (complete_total - ordered_total).contains(0):
        raise AssertionError("complete ordered replay differs")
    product_weight = arb(SHIFT) ** -18
    native_prefactor = (2 * arb.pi()) ** -10
    rule_value = complete_total * product_weight * native_prefactor
    if not math.isfinite(float(rule_value.upper())) or rule_value.lower() <= 0:
        raise AssertionError("order-eight rule value is not finite positive")

    return {
        "schema_version": "1.0",
        "result_id": "K345-ORDER-EIGHT-GROUP-INTERVAL-EVALUATOR",
        "created": "2026-09-22",
        "classification": "INTERNAL_NUMERICAL_CONTROL_ONLY",
        "direction": "observed_to_native",
        "fixed_control": {
            "predecessor_manifests": [
                "lab/process/k343-higher-order-value-mode-transfer-gate.json",
                "lab/process/k344-order-eight-gauss-laguerre-face-atlas.json",
            ],
            "order": ORDER,
            "arb_decimal_digits": 180,
            "threads": 1,
            "paths": paths,
            "coherent_groups": len(groups),
            "upper_triangle_gram_entries": entries,
            "ordered_quadratic_terms": ordered_entry_count,
            "maximum_species_determinant_rank": 4,
            "native_time_node": ["1/256"] * 18,
            "native_product_weight": k344["positive_product_gauss_laguerre_rule"]["product_weight"],
            "native_prefactor": "(2*pi)^-10",
            "K343_group_interface_sha256": k343_order["group_interface_sha256"],
            "K344_face_atlas_sha256": k344["cumulative_time_face_atlas"]["atlas_sha256"],
        },
        "coherent_group_values": group_rows,
        "complete_node_evaluation": {
            "all_entry_interval_sha256": digest(all_entry_intervals),
            "raw_complete_quadratic_form_lower": lower_text(complete_total),
            "raw_complete_quadratic_form_upper": upper_text(complete_total),
            "native_product_weight": k344["positive_product_gauss_laguerre_rule"]["product_weight"],
            "native_prefactor_interval_lower": lower_text(native_prefactor),
            "native_prefactor_interval_upper": upper_text(native_prefactor),
            "normalized_one_node_rule_lower": lower_text(rule_value),
            "normalized_one_node_rule_upper": upper_text(rule_value),
            "symmetric_enclosure_if_sign_is_discarded": [f"-{upper_text(rule_value)}", upper_text(rule_value)],
            "signed_rule_value_is_strictly_positive": rule_value.lower() > 0,
        },
        "assembly_contract": {
            "all_1296_upper_triangle_entries_evaluated": entries == EXPECTED_ENTRIES,
            "all_2400_ordered_terms_independently_replayed": ordered_entry_count == 2400,
            "all_1296_transpose_symmetry_checks_pass": symmetry_checks == EXPECTED_ENTRIES,
            "strictly_positive_individual_gram_entries": strictly_positive_gram_entries,
            "all_coefficients_retained": True,
            "all_contracted_positions_retained": True,
            "all_coherent_cross_terms_retained": True,
            "off_diagonal_terms_doubled_exactly_once": True,
            "complete_group_quadratic_form_precedes_enclosure": True,
            "occurrencewise_absolute_value_used": False,
            "raw_Bessel_zero_evaluation_used": False,
            "K299_weight_reused": False,
            "K341_normalization_reused": False,
        },
        "remainder_boundary": {
            "K344_positive_Peano_axes": 18,
            "K344_face_atlas_consumed_for_node_evaluation": True,
            "global_second_derivative_integrals_computed": False,
            "complete_order_eight_remainder_radius_emitted": False,
            "one_node_rule_value_is_not_the_full_order_eight_integral": True,
            "next_exact_input": "differentiate the complete group quadratic forms twice along each of K344's eighteen Gauss--Laguerre axes, use the exact zero/coalescence masks for scaled face limits, and integrate the positive Peano kernels before joining this node value",
        },
        "decision": {
            "all_1296_order_eight_gram_entries_validated": True,
            "complete_group_level_interval_evaluator_emitted": True,
            "normalized_order_eight_one_node_value_emitted": True,
            "complete_order_eight_integral_emitted": False,
            "complete_base_action_column_evaluated": False,
            "complete_R_ref_residual_evaluated": False,
            "native_K152_interval_emitted": False,
        },
        "release_test": {
            "all_192_paths_replayed": paths == EXPECTED_PATHS,
            "all_23_groups_replayed": len(groups) == EXPECTED_GROUPS,
            "all_1296_upper_triangle_entries_evaluated": entries == EXPECTED_ENTRIES,
            "all_2400_ordered_terms_replayed": ordered_entry_count == 2400,
            "upper_triangle_equals_full_ordered_replay": (complete_total - ordered_total).contains(0),
            "every_gram_entry_is_strictly_positive_at_the_native_node": strictly_positive_gram_entries == EXPECTED_ENTRIES,
            "normalized_rule_value_is_finite_positive": math.isfinite(float(rule_value.upper())) and rule_value.lower() > 0,
            "complete_order_eight_integral_emitted": False,
            "native_K152_interval_emitted": False,
        },
        "ledger_effect": k344["ledger_effect"],
        "source_routing": k344["source_routing"],
        "claim_ceiling": f"Rigorous Arb interval evaluation of the complete K344 order-eight positive one-node rule. All {entries} upper-triangle Gram entries and {ordered_entry_count} ordered coefficient terms are replayed in {len(groups)} coherent groups; the native product weight 256^-18 and prefactor (2*pi)^-10 give a strictly positive rule value in [{lower_text(rule_value)},{upper_text(rule_value)}]. The eighteen positive Peano remainder integrals are not yet bounded, so this is not an enclosure of the complete order-eight integral and supplies no complete action column, R_ref residual, K152 interval, source/ledger move, canon, paper, public or physical claim.",
    }


def validate_payload(payload: dict[str, Any]) -> None:
    fixed = payload["fixed_control"]
    if (fixed["paths"], fixed["coherent_groups"], fixed["upper_triangle_gram_entries"], fixed["ordered_quadratic_terms"]) != (
        EXPECTED_PATHS,
        EXPECTED_GROUPS,
        EXPECTED_ENTRIES,
        2400,
    ):
        raise AssertionError("order-eight evaluator census changed")
    if fixed["native_time_node"] != ["1/256"] * 18 or fixed["native_prefactor"] != "(2*pi)^-10":
        raise AssertionError("native node or prefactor changed")
    value = payload["complete_node_evaluation"]
    lower = float(value["normalized_one_node_rule_lower"])
    upper = float(value["normalized_one_node_rule_upper"])
    if not (3.0e-35 < lower <= upper < 3.2e-35) or not value["signed_rule_value_is_strictly_positive"]:
        raise AssertionError("order-eight rule interval changed or is invalid")
    assembly = payload["assembly_contract"]
    required = [
        "all_1296_upper_triangle_entries_evaluated",
        "all_2400_ordered_terms_independently_replayed",
        "all_1296_transpose_symmetry_checks_pass",
        "all_coefficients_retained",
        "all_contracted_positions_retained",
        "all_coherent_cross_terms_retained",
        "off_diagonal_terms_doubled_exactly_once",
        "complete_group_quadratic_form_precedes_enclosure",
    ]
    if not all(assembly[key] for key in required):
        raise AssertionError("complete group assembly contract failed")
    if assembly["occurrencewise_absolute_value_used"] or assembly["raw_Bessel_zero_evaluation_used"] or assembly["K299_weight_reused"] or assembly["K341_normalization_reused"]:
        raise AssertionError("forbidden order-seven transfer introduced")
    remainder = payload["remainder_boundary"]
    if remainder["K344_positive_Peano_axes"] != 18 or remainder["global_second_derivative_integrals_computed"] or remainder["complete_order_eight_remainder_radius_emitted"]:
        raise AssertionError("order-eight remainder boundary changed")
    decision = payload["decision"]
    if not decision["all_1296_order_eight_gram_entries_validated"] or not decision["complete_group_level_interval_evaluator_emitted"] or not decision["normalized_order_eight_one_node_value_emitted"]:
        raise AssertionError("K345 release decision failed")
    if decision["complete_order_eight_integral_emitted"] or decision["complete_base_action_column_evaluated"] or decision["complete_R_ref_residual_evaluated"] or decision["native_K152_interval_emitted"]:
        raise AssertionError("K345 downstream result overclaimed")


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
