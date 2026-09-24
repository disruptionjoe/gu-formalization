#!/usr/bin/env python3
"""Evaluate the complete K405 order-ten coherent one-node rule in Arb."""

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
K405 = ROOT / "lab/process/k405-order-ten-gauss-laguerre-face-atlas.json"
K376 = ROOT / "lab/process/k376-orders-nine-ten-rank-five-transfer.json"
OUTPUT = ROOT / "lab/process/k406-order-ten-group-interval-evaluator.json"

ORDER = 10
SHIFT = 256
SIDE_COUNT = 11
EXPECTED = (480, 28, 6890, 13300)

ctx.dps = 180
ctx.threads = 1


def load_k179():
    spec = importlib.util.spec_from_file_location("k179_for_k406", K179_PATH)
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
    return {position: arb(SIDE_COUNT + 1 - position) / SHIFT for position in range(1, SIDE_COUNT + 1)}


def gram_entry(left: dict[str, Any], right: dict[str, Any], cumulative: dict[int, arb]) -> arb:
    value = 2 * cumulative[int(left["old_position"])].bessel_k(1)
    value *= 2 * cumulative[int(right["old_position"])].bessel_k(1)
    left_occurrences = occurrences(left)
    right_occurrences = occurrences(right)
    if left_occurrences.keys() != right_occurrences.keys():
        raise AssertionError("species support changed inside a coherent group")
    for species in left_occurrences:
        rows = left_occurrences[species]
        columns = right_occurrences[species]
        matrix = [[2 * (cumulative[row] + cumulative[column]).bessel_k(1) for column in columns] for row in rows]
        value *= determinant(matrix)
    return value


def group_terms() -> dict[tuple[int, str], list[dict[str, Any]]]:
    groups: dict[tuple[int, str], list[dict[str, Any]]] = defaultdict(list)
    for term in K179.coefficient_family():
        if int(term["order"]) == ORDER:
            groups[(int(term["seed_impurity"]), str(term["output_signature"]))].append(term)
    return dict(sorted(groups.items()))


def build() -> dict[str, Any]:
    k405 = json.loads(K405.read_text())
    k376 = json.loads(K376.read_text())
    order_interface = next(row for row in k376["order_interfaces"] if row["order"] == ORDER)
    groups = group_terms()
    paths = sum(len(rows) for rows in groups.values())
    entries = sum(len(rows) * (len(rows) + 1) // 2 for rows in groups.values())
    ordered_expected = sum(len(rows) ** 2 for rows in groups.values())
    if (paths, len(groups), entries, ordered_expected) != EXPECTED:
        raise AssertionError("order-ten evaluator census changed")
    if not k405["decision"]["native_order_ten_positive_value_rule_emitted"]:
        raise AssertionError("K405 native rule unavailable")
    if k405["fixed_control"]["K376_complete_entry_interface_sha256"] != order_interface["complete_entry_interface_sha256"]:
        raise AssertionError("K376/K405 interface mismatch")

    cumulative = cumulative_times()
    complete_total = arb(0)
    ordered_total = arb(0)
    group_rows = []
    all_entry_intervals: list[dict[str, Any]] = []
    symmetry_checks = 0
    strictly_positive = 0
    ordered_count = 0
    for (seed, signature), terms in groups.items():
        group_id = f"order{ORDER}:seed{seed}:{signature}"
        values: dict[tuple[int, int], arb] = {}
        entry_rows = []
        upper_total = arb(0)
        for left_index, left in enumerate(terms):
            for right_index in range(left_index, len(terms)):
                right = terms[right_index]
                value = gram_entry(left, right, cumulative)
                transposed = gram_entry(right, left, cumulative)
                if not (value - transposed).contains(0):
                    raise AssertionError("Gram symmetry failed")
                symmetry_checks += 1
                values[(left_index, right_index)] = value
                values[(right_index, left_index)] = transposed
                if value.lower() > 0:
                    strictly_positive += 1
                coefficient = int(left["exact_operator_coefficient"]) * int(right["exact_operator_coefficient"])
                weighted = coefficient * value
                upper_total += weighted if left_index == right_index else 2 * weighted
                entry_rows.append({
                    "left": str(left["contraction_id"]),
                    "right": str(right["contraction_id"]),
                    "coefficient_product": coefficient,
                    "gram_lower": lower_text(value),
                    "gram_upper": upper_text(value),
                })
        full_ordered = arb(0)
        for left_index, left in enumerate(terms):
            for right_index, right in enumerate(terms):
                full_ordered += int(left["exact_operator_coefficient"]) * int(right["exact_operator_coefficient"]) * values[(left_index, right_index)]
                ordered_count += 1
        if not (upper_total - full_ordered).contains(0):
            raise AssertionError("upper-triangle reconstruction lost an ordered cross term")
        if upper_total.lower() < 0:
            raise AssertionError("coherent node Gram form is not positive")
        complete_total += upper_total
        ordered_total += full_ordered
        all_entry_intervals.extend({"group_id": group_id, **row} for row in entry_rows)
        group_rows.append({
            "group_id": group_id,
            "path_count": len(terms),
            "upper_triangle_entries": len(entry_rows),
            "ordered_quadratic_terms": len(terms) ** 2,
            "coherent_node_value_lower": lower_text(upper_total),
            "coherent_node_value_upper": upper_text(upper_total),
            "entry_interval_sha256": digest(entry_rows),
        })

    if not (complete_total - ordered_total).contains(0):
        raise AssertionError("complete ordered replay differs")
    product_weight = arb(SHIFT) ** -22
    native_prefactor = (2 * arb.pi()) ** -12
    rule_value = complete_total * product_weight * native_prefactor
    if not math.isfinite(float(rule_value.upper())) or rule_value.lower() <= 0:
        raise AssertionError("order-ten rule value is not finite positive")

    return {
        "schema_version": "1.0",
        "result_id": "K406-ORDER-TEN-GROUP-INTERVAL-EVALUATOR",
        "created": "2026-09-24",
        "classification": "INTERNAL_NUMERICAL_CONTROL_ONLY",
        "direction": "observed_to_native",
        "fixed_control": {
            "predecessor_manifests": ["lab/process/k376-orders-nine-ten-rank-five-transfer.json", "lab/process/k405-order-ten-gauss-laguerre-face-atlas.json"],
            "order": ORDER,
            "arb_decimal_digits": 180,
            "threads": 1,
            "paths": paths,
            "coherent_groups": len(groups),
            "upper_triangle_gram_entries": entries,
            "ordered_quadratic_terms": ordered_count,
            "maximum_species_determinant_rank": 5,
            "native_time_node": ["1/256"] * 22,
            "native_product_weight": k405["positive_product_gauss_laguerre_rule"]["product_weight"],
            "native_prefactor": "(2*pi)^-12",
            "K376_complete_entry_interface_sha256": order_interface["complete_entry_interface_sha256"],
            "K405_face_atlas_sha256": k405["cumulative_time_face_atlas"]["atlas_sha256"],
        },
        "coherent_group_values": group_rows,
        "complete_node_evaluation": {
            "all_entry_interval_sha256": digest(all_entry_intervals),
            "raw_complete_quadratic_form_lower": lower_text(complete_total),
            "raw_complete_quadratic_form_upper": upper_text(complete_total),
            "native_product_weight": k405["positive_product_gauss_laguerre_rule"]["product_weight"],
            "native_prefactor_interval_lower": lower_text(native_prefactor),
            "native_prefactor_interval_upper": upper_text(native_prefactor),
            "normalized_one_node_rule_lower": lower_text(rule_value),
            "normalized_one_node_rule_upper": upper_text(rule_value),
            "symmetric_enclosure_if_sign_is_discarded": [f"-{upper_text(rule_value)}", upper_text(rule_value)],
            "signed_rule_value_is_strictly_positive": rule_value.lower() > 0,
        },
        "assembly_contract": {
            "all_6890_upper_triangle_entries_evaluated": entries == 6890,
            "all_13300_ordered_terms_replayed": ordered_count == 13300,
            "all_6890_transpose_symmetry_checks_pass": symmetry_checks == 6890,
            "strictly_positive_individual_gram_entries": strictly_positive,
            "all_coefficients_retained": True,
            "all_contracted_positions_retained": True,
            "all_coherent_cross_terms_retained": True,
            "off_diagonal_terms_doubled_exactly_once": True,
            "complete_group_quadratic_form_precedes_enclosure": True,
            "occurrencewise_absolute_value_used": False,
            "raw_Bessel_zero_evaluation_used": False,
            "order_eight_weight_or_prefactor_reused": False,
        },
        "remainder_boundary": {
            "K405_positive_Peano_axes": 22,
            "K405_face_atlas_consumed_for_node_evaluation": True,
            "global_second_derivative_integrals_computed": False,
            "complete_order_ten_remainder_radius_emitted": False,
            "one_node_rule_value_is_not_the_full_order_ten_integral": True,
            "next_exact_input": "compile and evaluate the complete ordered group jets on all twenty-two axes, then bind global second derivatives to K405's positive Peano kernels on a zero-safe whole-orthant cover",
        },
        "decision": {
            "all_6890_order_ten_gram_entries_validated": True,
            "complete_group_level_interval_evaluator_emitted": True,
            "normalized_order_ten_one_node_value_emitted": True,
            "complete_order_ten_integral_emitted": False,
            "complete_base_action_column_evaluated": False,
            "complete_R_ref_residual_evaluated": False,
            "native_K152_interval_emitted": False,
        },
        "release_test": {
            "all_480_paths_replayed": paths == 480,
            "all_28_groups_replayed": len(groups) == 28,
            "all_6890_upper_triangle_entries_evaluated": entries == 6890,
            "all_13300_ordered_terms_replayed": ordered_count == 13300,
            "upper_triangle_equals_full_ordered_replay": (complete_total - ordered_total).contains(0),
            "every_gram_entry_is_strictly_positive_at_the_native_node": strictly_positive == 6890,
            "normalized_rule_value_is_finite_positive": math.isfinite(float(rule_value.upper())) and rule_value.lower() > 0,
            "complete_order_ten_integral_emitted": False,
            "native_K152_interval_emitted": False,
        },
        "ledger_effect": k405["ledger_effect"],
        "source_routing": k405["source_routing"],
        "claim_ceiling": f"Rigorous 180-digit Arb interval evaluation of the complete K405 order-ten positive one-node rule. All {entries} upper-triangle Gram entries and {ordered_count} ordered coefficient terms are replayed in {len(groups)} coherent groups; the native product weight 256^-22 and prefactor (2*pi)^-12 give a strictly positive rule value in [{lower_text(rule_value)},{upper_text(rule_value)}]. The twenty-two positive Peano remainder integrals are not yet bounded, so this is not an enclosure of the complete order-ten integral and supplies no complete action column, R_ref residual, K152 interval, source/ledger move, canon, paper, public or physical claim.",
    }


def validate_payload(payload: dict[str, Any]) -> None:
    fixed = payload["fixed_control"]
    if (fixed["paths"], fixed["coherent_groups"], fixed["upper_triangle_gram_entries"], fixed["ordered_quadratic_terms"], fixed["maximum_species_determinant_rank"]) != (480, 28, 6890, 13300, 5):
        raise AssertionError("K406 census changed")
    if fixed["native_time_node"] != ["1/256"] * 22 or fixed["native_prefactor"] != "(2*pi)^-12":
        raise AssertionError("K406 node or prefactor changed")
    value = payload["complete_node_evaluation"]
    if not value["signed_rule_value_is_strictly_positive"] or not (0 < float(value["normalized_one_node_rule_lower"]) <= float(value["normalized_one_node_rule_upper"])):
        raise AssertionError("K406 rule interval invalid")
    assembly = payload["assembly_contract"]
    required = ["all_6890_upper_triangle_entries_evaluated", "all_13300_ordered_terms_replayed", "all_6890_transpose_symmetry_checks_pass", "all_coefficients_retained", "all_contracted_positions_retained", "all_coherent_cross_terms_retained", "off_diagonal_terms_doubled_exactly_once", "complete_group_quadratic_form_precedes_enclosure"]
    if not all(assembly[key] for key in required):
        raise AssertionError("K406 assembly contract failed")
    if assembly["occurrencewise_absolute_value_used"] or assembly["raw_Bessel_zero_evaluation_used"] or assembly["order_eight_weight_or_prefactor_reused"]:
        raise AssertionError("K406 forbidden shortcut introduced")
    decision = payload["decision"]
    if not decision["normalized_order_ten_one_node_value_emitted"] or decision["complete_order_ten_integral_emitted"] or decision["native_K152_interval_emitted"]:
        raise AssertionError("K406 decision boundary changed")
    release = payload["release_test"]
    required_release = [
        "all_480_paths_replayed",
        "all_28_groups_replayed",
        "all_6890_upper_triangle_entries_evaluated",
        "all_13300_ordered_terms_replayed",
        "upper_triangle_equals_full_ordered_replay",
        "every_gram_entry_is_strictly_positive_at_the_native_node",
        "normalized_rule_value_is_finite_positive",
    ]
    if not all(release[key] for key in required_release) or release["complete_order_ten_integral_emitted"] or release["native_K152_interval_emitted"]:
        raise AssertionError("K406 release test failed")


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
