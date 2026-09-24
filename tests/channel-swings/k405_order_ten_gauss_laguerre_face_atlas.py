#!/usr/bin/env python3
"""Construct the native order-ten one-node rule and cumulative-time face atlas."""

from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
import math
import sys
from collections import Counter, defaultdict
from fractions import Fraction
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[2]
HERE = Path(__file__).resolve().parent
K179_PATH = HERE / "k179_matched_normal_order_coefficient_family.py"
K376 = ROOT / "lab/process/k376-orders-nine-ten-rank-five-transfer.json"
OUTPUT = ROOT / "lab/process/k405-order-ten-gauss-laguerre-face-atlas.json"

ORDER = 10
SIDE_COUNT = 11
AXIS_COUNT = 22
SHIFT = 256
EXPECTED = (480, 28, 6890)


def load_k179():
    spec = importlib.util.spec_from_file_location("k179_for_k405", K179_PATH)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {K179_PATH}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


K179 = load_k179()


def q(value: Fraction) -> str:
    return str(value.numerator) if value.denominator == 1 else f"{value.numerator}/{value.denominator}"


def digest(payload: Any) -> str:
    encoded = json.dumps(payload, sort_keys=True, separators=(",", ":")).encode()
    return "sha256:" + hashlib.sha256(encoded).hexdigest()


def occurrences(term: dict[str, Any]) -> dict[str, list[int]]:
    result: dict[str, list[int]] = defaultdict(list)
    for position, species in zip(term["output_variable_provenance"], term["output_letters"], strict=True):
        result[str(species)].append(int(position))
    return dict(sorted(result.items()))


def suffix_mask(side: str, position: int) -> tuple[str, ...]:
    return tuple(f"{side}{index}" for index in range(position, SIDE_COUNT + 1))


def interval_mask(side: str, first: int, second: int) -> tuple[str, ...]:
    lower, upper = sorted((first, second))
    return tuple(f"{side}{index}" for index in range(lower, upper))


def group_terms() -> dict[tuple[int, str], list[dict[str, Any]]]:
    groups: dict[tuple[int, str], list[dict[str, Any]]] = defaultdict(list)
    for term in K179.coefficient_family():
        if int(term["order"]) == ORDER:
            groups[(int(term["seed_impurity"]), str(term["output_signature"]))].append(term)
    return dict(sorted(groups.items()))


def support_atlas(groups: dict[tuple[int, str], list[dict[str, Any]]]) -> dict[str, Any]:
    zero_usage: Counter[tuple[str, ...]] = Counter()
    row_coalescence: Counter[tuple[str, ...]] = Counter()
    column_coalescence: Counter[tuple[str, ...]] = Counter()
    entry_count = 0
    determinant_entry_uses = 0
    for paths in groups.values():
        for left_index, left in enumerate(paths):
            left_occurrences = occurrences(left)
            for right in paths[left_index:]:
                right_occurrences = occurrences(right)
                if left_occurrences.keys() != right_occurrences.keys():
                    raise AssertionError("species support changed inside a coherent group")
                entry_count += 1
                zero_usage[suffix_mask("s", int(left["old_position"]))] += 1
                zero_usage[suffix_mask("v", int(right["old_position"]))] += 1
                for species in left_occurrences:
                    left_positions = left_occurrences[species]
                    right_positions = right_occurrences[species]
                    if len(left_positions) != len(right_positions):
                        raise AssertionError("Andreief determinant is not square")
                    for left_position in left_positions:
                        for right_position in right_positions:
                            zero_usage[suffix_mask("s", left_position) + suffix_mask("v", right_position)] += 1
                            determinant_entry_uses += 1
                    for index, first in enumerate(left_positions):
                        for second in left_positions[index + 1 :]:
                            row_coalescence[interval_mask("s", first, second)] += 1
                    for index, first in enumerate(right_positions):
                        for second in right_positions[index + 1 :]:
                            column_coalescence[interval_mask("v", first, second)] += 1

    def rows(counter: Counter[tuple[str, ...]], kind: str) -> list[dict[str, Any]]:
        return [
            {"face_kind": kind, "zeroed_axes": list(mask), "codimension": len(mask), "usage_count": counter[mask]}
            for mask in sorted(counter, key=lambda item: (len(item), item))
        ]

    zero_rows = rows(zero_usage, "bessel_argument_zero")
    row_rows = rows(row_coalescence, "determinant_row_coalescence")
    column_rows = rows(column_coalescence, "determinant_column_coalescence")
    payload = zero_rows + row_rows + column_rows
    return {
        "kernel_zero_faces": zero_rows,
        "row_coalescence_faces": row_rows,
        "column_coalescence_faces": column_rows,
        "unique_kernel_zero_masks": len(zero_rows),
        "unique_row_coalescence_masks": len(row_rows),
        "unique_column_coalescence_masks": len(column_rows),
        "upper_triangle_entries_covered": entry_count,
        "old_kernel_uses": 2 * entry_count,
        "determinant_kernel_entry_uses": determinant_entry_uses,
        "atlas_sha256": digest(payload),
    }


def build() -> dict[str, Any]:
    k376 = json.loads(K376.read_text())
    groups = group_terms()
    paths = sum(len(rows) for rows in groups.values())
    entries = sum(len(rows) * (len(rows) + 1) // 2 for rows in groups.values())
    if (paths, len(groups), entries) != EXPECTED:
        raise AssertionError("order-ten K376 census changed")
    fixed = next(row for row in k376["order_interfaces"] if row["order"] == ORDER)
    if fixed["maximum_rank"] != 5:
        raise AssertionError("order-ten rank-five boundary changed")

    atlas = support_atlas(groups)
    axis_weight = Fraction(1, SHIFT)
    product_weight = axis_weight**AXIS_COUNT
    radial_weight = Fraction(math.factorial(AXIS_COUNT - 1), SHIFT**AXIS_COUNT)
    angular_weight = Fraction(1, math.factorial(AXIS_COUNT - 1))
    peano_mass = Fraction(1, 2 * SHIFT**3)
    if radial_weight * angular_weight != product_weight:
        raise AssertionError("radial/angular replay changed")

    return {
        "schema_version": "1.0",
        "result_id": "K405-ORDER-TEN-GAUSS-LAGUERRE-FACE-ATLAS",
        "created": "2026-09-24",
        "classification": "INTERNAL_STRUCTURAL_ONLY",
        "direction": "observed_to_native",
        "fixed_control": {
            "predecessor_manifests": [
                "lab/process/k374-rank-five-confluent-determinant-calculus.json",
                "lab/process/k375-rank-five-global-scaled-bessel-bank.json",
                "lab/process/k376-orders-nine-ten-rank-five-transfer.json",
            ],
            "order": ORDER,
            "positive_time_variables": AXIS_COUNT,
            "laplace_shift": SHIFT,
            "paths": paths,
            "coherent_groups": len(groups),
            "upper_triangle_gram_entries": entries,
            "ordered_quadratic_terms": fixed["ordered_quadratic_terms"],
            "maximum_species_determinant_rank": fixed["maximum_rank"],
            "K376_complete_entry_interface_sha256": fixed["complete_entry_interface_sha256"],
        },
        "positive_product_gauss_laguerre_rule": {
            "measure": "product_{a=1}^11 exp(-256*s_a) ds_a product_{b=1}^11 exp(-256*v_b) dv_b",
            "axis_rule": "integral_0^infinity exp(-256*x) h(x) dx = h(1/256)/256 + integral_0^infinity K_256(t) h''(t) dt",
            "axis_node": "1/256",
            "axis_weight": "1/256",
            "node": ["1/256"] * AXIS_COUNT,
            "product_weight": q(product_weight),
            "node_count": 1,
            "all_weights_strictly_positive": True,
            "separately_affine_exact": True,
            "multiaffine_exact": True,
            "peano_kernel": {
                "for_0_le_t_le_1_over_256": "exp(-256*t)/256^2-(1/256-t)/256",
                "for_t_ge_1_over_256": "exp(-256*t)/256^2",
                "nonnegative": True,
                "zero_order_at_t_0": 2,
                "integral": q(peano_mass),
                "maximum_derivative_order": 2,
            },
        },
        "radial_angular_replay": {
            "rho": "sum(s_1..s_11)+sum(v_1..v_11)",
            "radial_density": "exp(-256*rho)*rho^21",
            "radial_node": q(Fraction(AXIS_COUNT, SHIFT)),
            "radial_weight": q(radial_weight),
            "theta_node": "1/2",
            "left_simplex_node": ["1/11"] * SIDE_COUNT,
            "right_simplex_node": ["1/11"] * SIDE_COUNT,
            "combined_angular_weight": q(angular_weight),
            "node_replays_all_twenty_two_times_at_1_over_256": True,
            "radial_times_angular_weight_equals_product_weight": True,
        },
        "cumulative_time_face_atlas": {
            **atlas,
            "kernel_support_rule": "T_j=sum_{a=j}^10 s_a and U_j=sum_{b=j}^10 v_b; 2*K1(T_j+U_k) reaches zero exactly when its recorded suffix mask vanishes",
            "coalescence_rule": "T_i=T_j exactly when the intervening s axes vanish, and likewise for U; equal determinant rows or columns then give an exact zero",
            "scaled_zero_safe_entry_rule": "use K374 gap-free confluence and K375 scaled primitives before division; never evaluate raw K1 at a zero face",
            "complete_group_quadratic_form_precedes_absolute_enclosure": True,
            "occurrencewise_absolute_value_permitted": False,
        },
        "remainder_interface": {
            "tensor_identity": "I_1...I_22-Q_1...Q_22=sum_j Q_1...Q_(j-1)(I_j-Q_j)I_(j+1)...I_22",
            "pure_second_derivative_axes": AXIS_COUNT,
            "mixed_derivatives_required": False,
            "positive_kernel_all_axes": True,
            "face_atlas_complete_for_kernel_zeros_and_determinant_coalescences": True,
            "global_second_derivative_integrals_computed": False,
        },
        "decision": {
            "native_order_ten_positive_value_rule_emitted": True,
            "all_6890_gram_entry_faces_classified": True,
            "group_level_node_evaluator_emitted": False,
            "complete_order_ten_remainder_emitted": False,
            "complete_order_ten_integral_emitted": False,
            "next_exact_input": "evaluate every order-ten upper-triangle Gram entry at the native 1/256 node and restore each complete coherent quadratic form before compiling the twenty-two-axis Peano interface",
        },
        "release_test": {
            "all_480_order_ten_paths_replayed": paths == 480,
            "all_28_order_ten_groups_replayed": len(groups) == 28,
            "all_6890_order_ten_entries_covered": atlas["upper_triangle_entries_covered"] == 6890,
            "all_13300_ordered_terms_retained": fixed["ordered_quadratic_terms"] == 13300,
            "positive_one_node_rule_exactly_normalized": radial_weight * angular_weight == product_weight,
            "all_zero_and_coalescence_faces_have_exact_support_masks": all(
                row["codimension"] > 0
                for key in ("kernel_zero_faces", "row_coalescence_faces", "column_coalescence_faces")
                for row in atlas[key]
            ),
            "complete_order_ten_integral_emitted": False,
            "native_K152_interval_emitted": False,
        },
        "ledger_effect": {"SC-ACT-01": "ASSERTS_UNCHANGED", "SC-ACT-02": "ASSERTS_UNCHANGED", "SC-ACT-06": "ASSERTS_UNCHANGED", "SC-META-53": "UNCERTAIN_UNCHANGED", "LT-SM8": "NEEDS_UNCHANGED", "LT-GR6b": "NEEDS_UNCHANGED", "RA-F1": "NEEDS_UNCHANGED", "AC-F1": "NEEDS_UNCHANGED"},
        "source_routing": {"classification": "INTERNAL_STRUCTURAL_ONLY", "source_native_GU_mechanism_tested": False, "conditional_repository_Fock_construction_only": True},
        "claim_ceiling": "Exact order-ten positive one-node Gauss--Laguerre value rule and cumulative-time zero/coalescence face atlas for all 480 K179 paths, 28 coherent groups and 6,890 upper-triangle Gram entries. The rule uses twenty-two native positive Laplace times, node 1/256 on every axis and total weight 256^-22. It freezes twenty-two positive pure-second Peano terms but does not integrate them, evaluate a group value, enclose the complete order-ten integral, complete an action column or R_ref, emit a K152 interval, or move source, ledger, canon, paper, public or physical posture.",
    }


def validate_payload(payload: dict[str, Any]) -> None:
    fixed = payload["fixed_control"]
    if (fixed["paths"], fixed["coherent_groups"], fixed["upper_triangle_gram_entries"], fixed["ordered_quadratic_terms"], fixed["maximum_species_determinant_rank"]) != (480, 28, 6890, 13300, 5):
        raise AssertionError("K405 fixed census changed")
    rule = payload["positive_product_gauss_laguerre_rule"]
    if rule["axis_node"] != "1/256" or rule["axis_weight"] != "1/256" or not rule["peano_kernel"]["nonnegative"]:
        raise AssertionError("K405 positive rule changed")
    atlas = payload["cumulative_time_face_atlas"]
    if atlas["upper_triangle_entries_covered"] != 6890 or not atlas["complete_group_quadratic_form_precedes_absolute_enclosure"] or atlas["occurrencewise_absolute_value_permitted"]:
        raise AssertionError("K405 face contract changed")
    if payload["remainder_interface"]["pure_second_derivative_axes"] != 22 or payload["remainder_interface"]["mixed_derivatives_required"]:
        raise AssertionError("K405 Peano interface changed")
    release = payload["release_test"]
    required = [
        "all_480_order_ten_paths_replayed",
        "all_28_order_ten_groups_replayed",
        "all_6890_order_ten_entries_covered",
        "all_13300_ordered_terms_retained",
        "positive_one_node_rule_exactly_normalized",
        "all_zero_and_coalescence_faces_have_exact_support_masks",
    ]
    if not all(release[key] for key in required) or release["complete_order_ten_integral_emitted"] or release["native_K152_interval_emitted"]:
        raise AssertionError("K405 release test failed")


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
