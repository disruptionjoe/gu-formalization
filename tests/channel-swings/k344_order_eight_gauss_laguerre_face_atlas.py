#!/usr/bin/env python3
"""Construct the native order-eight one-node rule and cumulative-time face atlas.

K343 freezes 1,296 order-eight Gram entries but deliberately emits no value.
This packet works directly in the eighteen positive Laplace-time variables.
The product one-node Gauss--Laguerre rule has node 1/256 on every axis and
weight 256^-18.  Its Peano kernel is positive.  Exact support masks record
every Bessel zero face and every determinant row/column coalescence face before
the numerical group evaluator is allowed to run.
"""

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
K343_PATH = HERE / "k343_higher_order_value_mode_transfer_gate.py"
K343 = ROOT / "lab/process/k343-higher-order-value-mode-transfer-gate.json"
OUTPUT = ROOT / "lab/process/k344-order-eight-gauss-laguerre-face-atlas.json"

ORDER = 8
TIME_COUNT_PER_SIDE = ORDER + 1
AXIS_COUNT = 2 * TIME_COUNT_PER_SIDE
SHIFT = 256
EXPECTED_PATHS = 192
EXPECTED_GROUPS = 23
EXPECTED_ENTRIES = 1296


def load_module(path: Path, name: str):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {path}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


K179 = load_module(K179_PATH, "k179_for_k344")
K343_MODULE = load_module(K343_PATH, "k343_for_k344")


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
    return tuple(f"{side}{index}" for index in range(position, TIME_COUNT_PER_SIDE + 1))


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
                            mask = suffix_mask("s", left_position) + suffix_mask("v", right_position)
                            zero_usage[mask] += 1
                            determinant_entry_uses += 1
                    for index, first in enumerate(left_positions):
                        for second in left_positions[index + 1 :]:
                            row_coalescence[interval_mask("s", first, second)] += 1
                    for index, first in enumerate(right_positions):
                        for second in right_positions[index + 1 :]:
                            column_coalescence[interval_mask("v", first, second)] += 1

    def rows(counter: Counter[tuple[str, ...]], face_kind: str) -> list[dict[str, Any]]:
        return [
            {
                "face_kind": face_kind,
                "zeroed_axes": list(mask),
                "codimension": len(mask),
                "usage_count": counter[mask],
            }
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
    k343 = json.loads(K343.read_text())
    groups = group_terms()
    paths = sum(len(rows) for rows in groups.values())
    entries = sum(len(rows) * (len(rows) + 1) // 2 for rows in groups.values())
    if (paths, len(groups), entries) != (EXPECTED_PATHS, EXPECTED_GROUPS, EXPECTED_ENTRIES):
        raise AssertionError("order-eight K343 census changed")
    k343_order = next(row for row in k343["orders"] if row["order"] == ORDER)
    if k343_order["maximum_species_determinant_rank"] != 4:
        raise AssertionError("order-eight rank-four boundary changed")
    rebuilt_group_rows = K343_MODULE.group_rows(ORDER, K179.coefficient_family())
    if K343_MODULE.digest(rebuilt_group_rows) != k343_order["group_interface_sha256"]:
        raise AssertionError("K343 order-eight coherence interface changed")

    atlas = support_atlas(groups)
    axis_weight = Fraction(1, SHIFT)
    node = Fraction(1, SHIFT)
    product_weight = axis_weight**AXIS_COUNT
    radial_node = Fraction(AXIS_COUNT, SHIFT)
    radial_weight = Fraction(math.factorial(AXIS_COUNT - 1), SHIFT**AXIS_COUNT)
    angular_weight = Fraction(1, math.factorial(AXIS_COUNT - 1))
    peano_mass = Fraction(1, 2 * SHIFT**3)
    if radial_weight * angular_weight != product_weight:
        raise AssertionError("radial/angular replay changed")

    return {
        "schema_version": "1.0",
        "result_id": "K344-ORDER-EIGHT-GAUSS-LAGUERRE-FACE-ATLAS",
        "created": "2026-09-22",
        "classification": "INTERNAL_STRUCTURAL_ONLY",
        "direction": "observed_to_native",
        "fixed_control": {
            "predecessor_manifests": [
                "lab/process/k279-higher-order-andreief-structural-closure.json",
                "lab/process/k343-higher-order-value-mode-transfer-gate.json",
            ],
            "order": ORDER,
            "positive_time_variables": AXIS_COUNT,
            "laplace_shift": SHIFT,
            "paths": paths,
            "coherent_groups": len(groups),
            "upper_triangle_gram_entries": entries,
            "maximum_species_determinant_rank": k343_order["maximum_species_determinant_rank"],
            "K343_group_interface_sha256": k343_order["group_interface_sha256"],
        },
        "positive_product_gauss_laguerre_rule": {
            "measure": "product_{a=1}^9 exp(-256*s_a) ds_a product_{b=1}^9 exp(-256*v_b) dv_b",
            "axis_rule": "integral_0^infinity exp(-256*x) h(x) dx = h(1/256)/256 + integral_0^infinity K_256(t) h''(t) dt",
            "axis_node": q(node),
            "axis_weight": q(axis_weight),
            "node": [q(node)] * AXIS_COUNT,
            "product_weight": q(product_weight),
            "node_count": 1,
            "all_weights_strictly_positive": product_weight > 0,
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
            "rho": "sum(s_1..s_9)+sum(v_1..v_9)",
            "radial_density": "exp(-256*rho)*rho^17",
            "radial_node": q(radial_node),
            "radial_weight": q(radial_weight),
            "theta_node": "1/2",
            "left_simplex_node": ["1/9"] * 9,
            "right_simplex_node": ["1/9"] * 9,
            "combined_angular_weight": q(angular_weight),
            "node_replays_all_eighteen_times_at_1_over_256": True,
            "radial_times_angular_weight_equals_product_weight": True,
        },
        "cumulative_time_face_atlas": {
            **atlas,
            "kernel_support_rule": "T_j=sum_{a=j}^9 s_a and U_j=sum_{b=j}^9 v_b; 2*K1(T_j+U_k) reaches zero exactly when its recorded suffix mask vanishes",
            "coalescence_rule": "T_i=T_j exactly when the intervening s axes vanish, and likewise for U; equal determinant rows or columns then give an exact zero",
            "scaled_zero_safe_entry_rule": "evaluate Phi_1(z)=2*z*K1(z) with the recorded support scale before division; never evaluate raw K1 at a zero face",
            "complete_group_quadratic_form_precedes_absolute_enclosure": True,
            "occurrencewise_absolute_value_permitted": False,
        },
        "remainder_interface": {
            "tensor_identity": "I_1...I_18-Q_1...Q_18=sum_j Q_1...Q_(j-1)(I_j-Q_j)I_(j+1)...I_18",
            "pure_second_derivative_axes": AXIS_COUNT,
            "mixed_derivatives_required": False,
            "positive_kernel_all_axes": True,
            "face_atlas_complete_for_kernel_zeros_and_determinant_coalescences": True,
            "global_second_derivative_integrals_computed": False,
        },
        "decision": {
            "native_order_eight_positive_value_rule_emitted": True,
            "all_1296_gram_entry_faces_classified": True,
            "group_level_node_evaluator_emitted": False,
            "complete_order_eight_remainder_emitted": False,
            "complete_order_eight_integral_emitted": False,
            "next_exact_input": "evaluate every K343 order-eight upper-triangle Gram entry at the native 1/256 node, restore each complete c_G^T K_G c_G, and only then integrate the eighteen positive Peano second-derivative terms over this face atlas",
        },
        "release_test": {
            "all_192_order_eight_paths_replayed": paths == EXPECTED_PATHS,
            "all_23_order_eight_groups_replayed": len(groups) == EXPECTED_GROUPS,
            "all_1296_order_eight_entries_covered": atlas["upper_triangle_entries_covered"] == EXPECTED_ENTRIES,
            "K343_interface_digest_replayed": True,
            "positive_one_node_rule_exactly_normalized": radial_weight * angular_weight == product_weight,
            "all_zero_and_coalescence_faces_have_exact_support_masks": all(
                row["codimension"] > 0
                for key in ("kernel_zero_faces", "row_coalescence_faces", "column_coalescence_faces")
                for row in atlas[key]
            ),
            "complete_order_eight_integral_emitted": False,
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
        "claim_ceiling": "Exact order-eight positive one-node Gauss--Laguerre value rule and cumulative-time zero/coalescence face atlas for all 192 K179 paths, 23 coherent groups and 1,296 upper-triangle Gram entries. The rule uses the eighteen native positive Laplace times, node 1/256 on every axis and total weight 256^-18. It freezes eighteen positive pure-second Peano remainder terms but does not integrate them, evaluate a group value, enclose the complete order-eight integral, complete an action column or R_ref, emit a K152 interval, or move source, ledger, canon, paper, public or physical posture.",
    }


def validate_payload(payload: dict[str, Any]) -> None:
    fixed = payload["fixed_control"]
    if (fixed["paths"], fixed["coherent_groups"], fixed["upper_triangle_gram_entries"]) != (
        EXPECTED_PATHS,
        EXPECTED_GROUPS,
        EXPECTED_ENTRIES,
    ):
        raise AssertionError("order-eight fixed census changed")
    rule = payload["positive_product_gauss_laguerre_rule"]
    if rule["axis_node"] != "1/256" or rule["axis_weight"] != "1/256":
        raise AssertionError("native Gauss--Laguerre node changed")
    if rule["product_weight"] != q(Fraction(1, SHIFT) ** AXIS_COUNT):
        raise AssertionError("product rule weight changed")
    if not rule["all_weights_strictly_positive"] or not rule["peano_kernel"]["nonnegative"]:
        raise AssertionError("positive rule contract changed")
    atlas = payload["cumulative_time_face_atlas"]
    if atlas["upper_triangle_entries_covered"] != EXPECTED_ENTRIES:
        raise AssertionError("face atlas lost Gram entries")
    if not atlas["complete_group_quadratic_form_precedes_absolute_enclosure"] or atlas["occurrencewise_absolute_value_permitted"]:
        raise AssertionError("coherent enclosure boundary changed")
    remainder = payload["remainder_interface"]
    if remainder["pure_second_derivative_axes"] != AXIS_COUNT or remainder["mixed_derivatives_required"]:
        raise AssertionError("Peano derivative interface changed")
    decision = payload["decision"]
    if not decision["native_order_eight_positive_value_rule_emitted"] or not decision["all_1296_gram_entry_faces_classified"]:
        raise AssertionError("K344 release decision failed")
    if decision["group_level_node_evaluator_emitted"] or decision["complete_order_eight_remainder_emitted"] or decision["complete_order_eight_integral_emitted"]:
        raise AssertionError("K344 downstream result overclaimed")


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
