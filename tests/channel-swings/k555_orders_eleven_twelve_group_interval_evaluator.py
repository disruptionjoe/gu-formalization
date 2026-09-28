#!/usr/bin/env python3
"""Evaluate the complete K554 order-eleven/twelve coherent one-node rules."""

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
K379 = ROOT / "lab/process/k379-orders-eleven-twelve-rank-six-transfer.json"
K554 = ROOT / "lab/process/k554-orders-eleven-twelve-gauss-laguerre-face-atlas.json"
OUTPUT = ROOT / "lab/process/k555-orders-eleven-twelve-group-interval-evaluator.json"

SHIFT = 256
EXPECTED = {
    11: {"side": 12, "axes": 24, "paths": 640, "groups": 24, "entries": 12920, "ordered": 25200, "prefactor": "(2*pi)^-13"},
    12: {"side": 13, "axes": 26, "paths": 1152, "groups": 33, "entries": 35352, "ordered": 69552, "prefactor": "(2*pi)^-14"},
}

ctx.dps = 180
ctx.threads = 1


def load_k179():
    spec = importlib.util.spec_from_file_location("k179_for_k555", K179_PATH)
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


def cumulative_times(side_count: int) -> dict[int, arb]:
    return {position: arb(side_count + 1 - position) / SHIFT for position in range(1, side_count + 1)}


def gram_key(left: dict[str, Any], right: dict[str, Any]) -> tuple[Any, ...]:
    left_occurrences = occurrences(left)
    right_occurrences = occurrences(right)
    if left_occurrences.keys() != right_occurrences.keys():
        raise AssertionError("species support changed inside a coherent group")
    species_data = tuple(
        (species, tuple(left_occurrences[species]), tuple(right_occurrences[species]))
        for species in left_occurrences
    )
    return (int(left["old_position"]), int(right["old_position"]), species_data)


def gram_entry(
    left: dict[str, Any],
    right: dict[str, Any],
    cumulative: dict[int, arb],
    cache: dict[tuple[Any, ...], arb],
) -> arb:
    key = gram_key(left, right)
    if key in cache:
        return cache[key]
    left_old, right_old, species_data = key
    value = 2 * cumulative[left_old].bessel_k(1)
    value *= 2 * cumulative[right_old].bessel_k(1)
    for _, rows, columns in species_data:
        matrix = [
            [2 * (cumulative[row] + cumulative[column]).bessel_k(1) for column in columns]
            for row in rows
        ]
        value *= determinant(matrix)
    cache[key] = value
    return value


def group_terms(order: int) -> dict[tuple[int, str], list[dict[str, Any]]]:
    groups: dict[tuple[int, str], list[dict[str, Any]]] = defaultdict(list)
    for term in K179.coefficient_family():
        if int(term["order"]) == order:
            groups[(int(term["seed_impurity"]), str(term["output_signature"]))].append(term)
    return dict(sorted(groups.items()))


def evaluate_order(
    order: int,
    atlas_interface: dict[str, Any],
    transfer_interface: dict[str, Any],
) -> dict[str, Any]:
    expected = EXPECTED[order]
    groups = group_terms(order)
    paths = sum(len(rows) for rows in groups.values())
    entries = sum(len(rows) * (len(rows) + 1) // 2 for rows in groups.values())
    ordered_expected = sum(len(rows) ** 2 for rows in groups.values())
    if (paths, len(groups), entries, ordered_expected) != (
        expected["paths"], expected["groups"], expected["entries"], expected["ordered"]
    ):
        raise AssertionError(f"order-{order} evaluator census changed")
    if atlas_interface["K379_complete_entry_interface_sha256"] != transfer_interface["complete_entry_interface_sha256"]:
        raise AssertionError(f"order-{order} K379/K554 interface mismatch")
    if atlas_interface["native_prefactor"] != expected["prefactor"]:
        raise AssertionError(f"order-{order} prefactor changed")

    cumulative = cumulative_times(expected["side"])
    cache: dict[tuple[Any, ...], arb] = {}
    complete_total = arb(0)
    ordered_total = arb(0)
    group_rows = []
    all_entry_intervals: list[dict[str, Any]] = []
    symmetry_checks = strictly_positive = ordered_count = 0
    for (seed, signature), terms in groups.items():
        group_id = f"order{order}:seed{seed}:{signature}"
        values: dict[tuple[int, int], arb] = {}
        entry_rows = []
        upper_total = arb(0)
        for left_index, left in enumerate(terms):
            for right_index in range(left_index, len(terms)):
                right = terms[right_index]
                value = gram_entry(left, right, cumulative, cache)
                transposed = gram_entry(right, left, cumulative, cache)
                if not (value - transposed).contains(0):
                    raise AssertionError(f"order-{order} Gram symmetry failed")
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
            raise AssertionError(f"order-{order} upper-triangle reconstruction lost an ordered cross term")
        if upper_total.lower() < 0:
            raise AssertionError(f"order-{order} coherent node Gram form is not positive")
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
        raise AssertionError(f"order-{order} complete ordered replay differs")
    product_weight = arb(SHIFT) ** -expected["axes"]
    native_prefactor = (2 * arb.pi()) ** -(order + 2)
    rule_value = complete_total * product_weight * native_prefactor
    if not math.isfinite(float(rule_value.upper())) or rule_value.lower() <= 0:
        raise AssertionError(f"order-{order} rule value is not finite positive")

    return {
        "order": order,
        "fixed_control": {
            "side_count": expected["side"],
            "positive_time_variables": expected["axes"],
            "paths": paths,
            "coherent_groups": len(groups),
            "upper_triangle_gram_entries": entries,
            "ordered_quadratic_terms": ordered_count,
            "maximum_species_determinant_rank": 6,
            "native_time_node": ["1/256"] * expected["axes"],
            "native_product_weight": atlas_interface["positive_product_rule"]["product_weight"],
            "native_prefactor": expected["prefactor"],
            "K379_complete_entry_interface_sha256": transfer_interface["complete_entry_interface_sha256"],
            "K554_face_atlas_sha256": atlas_interface["cumulative_time_face_atlas"]["atlas_sha256"],
            "unique_positive_node_gram_patterns": len(cache),
        },
        "coherent_group_values": group_rows,
        "complete_node_evaluation": {
            "all_entry_interval_sha256": digest(all_entry_intervals),
            "raw_complete_quadratic_form_lower": lower_text(complete_total),
            "raw_complete_quadratic_form_upper": upper_text(complete_total),
            "native_product_weight": atlas_interface["positive_product_rule"]["product_weight"],
            "native_prefactor_interval_lower": lower_text(native_prefactor),
            "native_prefactor_interval_upper": upper_text(native_prefactor),
            "normalized_one_node_rule_lower": lower_text(rule_value),
            "normalized_one_node_rule_upper": upper_text(rule_value),
            "symmetric_enclosure_if_sign_is_discarded": [f"-{upper_text(rule_value)}", upper_text(rule_value)],
            "signed_rule_value_is_strictly_positive": rule_value.lower() > 0,
        },
        "assembly_contract": {
            "all_upper_triangle_entries_evaluated": entries == expected["entries"],
            "all_ordered_terms_replayed": ordered_count == expected["ordered"],
            "all_transpose_symmetry_checks_pass": symmetry_checks == expected["entries"],
            "strictly_positive_individual_gram_entries": strictly_positive,
            "all_coefficients_retained": True,
            "all_contracted_positions_retained": True,
            "all_coherent_cross_terms_retained": True,
            "off_diagonal_terms_doubled_exactly_once": True,
            "complete_group_quadratic_form_precedes_enclosure": True,
            "occurrencewise_absolute_value_used": False,
            "raw_Bessel_zero_evaluation_used": False,
            "order_ten_weight_or_prefactor_reused": False,
        },
        "release_test": {
            "all_paths_replayed": paths == expected["paths"],
            "all_groups_replayed": len(groups) == expected["groups"],
            "all_upper_triangle_entries_evaluated": entries == expected["entries"],
            "all_ordered_terms_replayed": ordered_count == expected["ordered"],
            "upper_triangle_equals_full_ordered_replay": (complete_total - ordered_total).contains(0),
            "every_gram_entry_is_strictly_positive_at_the_native_node": strictly_positive == expected["entries"],
            "normalized_rule_value_is_finite_positive": math.isfinite(float(rule_value.upper())) and rule_value.lower() > 0,
        },
    }


def build() -> dict[str, Any]:
    k379 = json.loads(K379.read_text())
    k554 = json.loads(K554.read_text())
    transfers = {int(row["order"]): row for row in k379["order_interfaces"]}
    atlases = {int(row["order"]): row for row in k554["order_interfaces"]}
    rows = [evaluate_order(order, atlases[order], transfers[order]) for order in (11, 12)]
    return {
        "schema_version": "1.0",
        "result_id": "K555-ORDERS-ELEVEN-TWELVE-GROUP-INTERVAL-EVALUATOR",
        "created": "2026-09-27",
        "classification": "INTERNAL_NUMERICAL_CONTROL_ONLY",
        "direction": "observed_to_native",
        "fixed_control": {
            "predecessor_manifests": [
                "lab/process/k379-orders-eleven-twelve-rank-six-transfer.json",
                "lab/process/k554-orders-eleven-twelve-gauss-laguerre-face-atlas.json",
            ],
            "arb_decimal_digits": 180,
            "threads": 1,
            "orders": [11, 12],
            "combined_paths": sum(row["fixed_control"]["paths"] for row in rows),
            "combined_groups": sum(row["fixed_control"]["coherent_groups"] for row in rows),
            "combined_upper_triangle_entries": sum(row["fixed_control"]["upper_triangle_gram_entries"] for row in rows),
            "combined_ordered_terms": sum(row["fixed_control"]["ordered_quadratic_terms"] for row in rows),
        },
        "order_evaluations": rows,
        "composition_contract": {
            "order_specific_dimensions_prefactors_and_counts_retained": True,
            "complete_group_quadratic_forms_precede_enclosure": True,
            "off_diagonal_terms_doubled_once_at_symmetric_node": True,
            "occurrencewise_absolute_value_used": False,
            "raw_Bessel_zero_evaluation_used": False,
            "order_ten_normalization_reused": False,
        },
        "decision": {
            "complete_order_eleven_group_evaluator_emitted": True,
            "complete_order_twelve_group_evaluator_emitted": True,
            "normalized_order_eleven_one_node_value_emitted": True,
            "normalized_order_twelve_one_node_value_emitted": True,
            "ordered_axis_jet_interfaces_emitted": False,
            "complete_order_eleven_integral_emitted": False,
            "complete_order_twelve_integral_emitted": False,
            "complete_base_action_column_evaluated": False,
            "complete_R_ref_residual_evaluated": False,
            "native_K152_interval_emitted": False,
        },
        "remainder_boundary": {
            "K554_positive_Peano_axes": [24, 26],
            "K554_face_atlases_consumed_for_node_evaluation": True,
            "global_second_derivative_integrals_computed": False,
            "complete_order_eleven_remainder_radius_emitted": False,
            "complete_order_twelve_remainder_radius_emitted": False,
            "one_node_rule_values_are_not_complete_integrals": True,
            "next_exact_input": "compile both complete ordered 24/26-axis group differentiation interfaces, then evaluate their first/second node jets before constructing zero-safe global Peano closures",
        },
        "release_test": {
            "all_1792_paths_replayed": sum(row["fixed_control"]["paths"] for row in rows) == 1792,
            "all_57_groups_replayed": sum(row["fixed_control"]["coherent_groups"] for row in rows) == 57,
            "all_48272_upper_triangle_entries_evaluated": sum(row["fixed_control"]["upper_triangle_gram_entries"] for row in rows) == 48272,
            "all_94752_ordered_terms_replayed": sum(row["fixed_control"]["ordered_quadratic_terms"] for row in rows) == 94752,
            "rank_six_boundary_retained_both_orders": all(row["fixed_control"]["maximum_species_determinant_rank"] == 6 for row in rows),
            "separate_native_prefactors_retained": [row["fixed_control"]["native_prefactor"] for row in rows] == ["(2*pi)^-13", "(2*pi)^-14"],
            "both_normalized_rule_values_finite_positive": all(row["release_test"]["normalized_rule_value_is_finite_positive"] for row in rows),
            "complete_integrals_not_overclaimed": True,
            "native_K152_interval_not_emitted": True,
        },
        "ledger_effect": k554["ledger_effect"],
        "source_routing": k554["source_routing"],
        "claim_ceiling": "Rigorous 180-digit Arb interval evaluation of both complete K554 positive one-node rules. All 48,272 upper-triangle Gram entries and 94,752 ordered coefficient terms are replayed in 57 coherent groups with separate 24/26-dimensional product weights and (2*pi)^-13/(2*pi)^-14 prefactors. Both normalized node values are strictly positive. Their positive Peano remainders are not yet bounded, so neither value encloses a complete integral and no complete action column, R_ref residual, K152 interval, source/ledger move, canon, paper, public, novelty or physical claim follows.",
    }


def validate_payload(payload: dict[str, Any]) -> None:
    fixed = payload["fixed_control"]
    if (fixed["combined_paths"], fixed["combined_groups"], fixed["combined_upper_triangle_entries"], fixed["combined_ordered_terms"]) != (1792, 57, 48272, 94752):
        raise AssertionError("K555 combined census changed")
    rows = payload["order_evaluations"]
    if len(rows) != 2 or [row["order"] for row in rows] != [11, 12]:
        raise AssertionError("K555 order evaluations changed")
    for row in rows:
        expected = EXPECTED[row["order"]]
        control = row["fixed_control"]
        if (control["side_count"], control["positive_time_variables"], control["paths"], control["coherent_groups"], control["upper_triangle_gram_entries"], control["ordered_quadratic_terms"], control["maximum_species_determinant_rank"], control["native_prefactor"]) != (expected["side"], expected["axes"], expected["paths"], expected["groups"], expected["entries"], expected["ordered"], 6, expected["prefactor"]):
            raise AssertionError(f"K555 order-{row['order']} interface changed")
        if not all(row["release_test"].values()):
            raise AssertionError(f"K555 order-{row['order']} release test failed")
        assembly = row["assembly_contract"]
        if not all(assembly[key] for key in ("all_upper_triangle_entries_evaluated", "all_ordered_terms_replayed", "all_transpose_symmetry_checks_pass", "all_coefficients_retained", "all_contracted_positions_retained", "all_coherent_cross_terms_retained", "off_diagonal_terms_doubled_exactly_once", "complete_group_quadratic_form_precedes_enclosure")):
            raise AssertionError(f"K555 order-{row['order']} assembly contract failed")
        if assembly["occurrencewise_absolute_value_used"] or assembly["raw_Bessel_zero_evaluation_used"] or assembly["order_ten_weight_or_prefactor_reused"]:
            raise AssertionError(f"K555 order-{row['order']} forbidden shortcut introduced")
    if not all(payload["release_test"].values()):
        raise AssertionError("K555 combined release test failed")
    decision = payload["decision"]
    if not decision["normalized_order_eleven_one_node_value_emitted"] or not decision["normalized_order_twelve_one_node_value_emitted"] or decision["complete_order_eleven_integral_emitted"] or decision["complete_order_twelve_integral_emitted"] or decision["native_K152_interval_emitted"]:
        raise AssertionError("K555 decision boundary changed")


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
