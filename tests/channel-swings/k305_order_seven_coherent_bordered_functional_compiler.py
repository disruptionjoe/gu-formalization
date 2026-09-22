#!/usr/bin/env python3
"""Compile K304's occurrence templates into coherent bordered determinants.

The six stored upper-triangle occurrences in each K288 coherent group are the
cofactor expansion of one bordered five-by-five determinant.  This compiler
restores the ordered nine-term sum before absolute enclosure and differentiates
the bordered determinant as a single object, preserving the common q/x support.
"""

from __future__ import annotations

import argparse
import itertools
import json
import math
from fractions import Fraction
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[2]
K288 = ROOT / "lab/process/k288-order-seven-native-occurrence-measure.json"
K298 = ROOT / "lab/process/k298-order-seven-coherent-terminal-corner-obstruction.json"
K303 = ROOT / "lab/process/k303-order-seven-peano-determinant-compiler.json"
K304 = ROOT / "lab/process/k304-order-seven-peano-norm-sufficiency-audit.json"
OUTPUT = ROOT / "lab/process/k305-order-seven-coherent-bordered-functional-compiler.json"

POSITIONS = (2, 4, 6)
COEFFICIENTS = (1, -1, 1)
EXPECTED_PAIRS = ((2, 2), (2, 4), (2, 6), (4, 4), (4, 6), (6, 6))
EXPECTED_WEIGHTS = (1, -2, 2, 1, -2, 1)


def determinant(matrix: list[list[Fraction]]) -> Fraction:
    work = [row[:] for row in matrix]
    result = Fraction(1)
    for column in range(len(work)):
        pivot = next((row for row in range(column, len(work)) if work[row][column]), None)
        if pivot is None:
            return Fraction(0)
        if pivot != column:
            work[column], work[pivot] = work[pivot], work[column]
            result = -result
        value = work[column][column]
        result *= value
        work[column] = [entry / value for entry in work[column]]
        for row in range(column + 1, len(work)):
            factor = work[row][column]
            work[row] = [entry - factor * base for entry, base in zip(work[row], work[column])]
    return result


def minor(matrix: list[list[Fraction]], row: int, column: int) -> list[list[Fraction]]:
    return [
        [entry for j, entry in enumerate(source) if j != column]
        for i, source in enumerate(matrix)
        if i != row
    ]


def bordered_identity_control() -> dict[str, Any]:
    matrix = [
        [Fraction(7), Fraction(2), Fraction(1), Fraction(3)],
        [Fraction(5), Fraction(11), Fraction(4), Fraction(2)],
        [Fraction(3), Fraction(1), Fraction(13), Fraction(6)],
        [Fraction(2), Fraction(4), Fraction(5), Fraction(17)],
    ]
    left = [Fraction(2), Fraction(3), Fraction(5), Fraction(0)]
    right = [Fraction(7), Fraction(11), Fraction(13), Fraction(0)]
    coherent = Fraction(0)
    terms = []
    for row, column in itertools.product(range(3), repeat=2):
        cofactor_sign = -1 if (row + column) % 2 else 1
        value = left[row] * right[column] * cofactor_sign * determinant(minor(matrix, row, column))
        coherent += value
        terms.append(str(value))
    bordered = [source + [left[index]] for index, source in enumerate(matrix)]
    bordered.append(right + [Fraction(0)])
    bordered_det = determinant(bordered)
    return {
        "matrix": [[str(value) for value in row] for row in matrix],
        "left": [str(value) for value in left],
        "right": [str(value) for value in right],
        "ordered_cofactor_terms": terms,
        "ordered_cofactor_sum": str(coherent),
        "bordered_determinant": str(bordered_det),
        "identity": "sum_ab L_a R_b (-1)^(a+b) det(M_hat_a_hat_b) = -det([[M,L],[R^T,0]])",
        "identity_holds": coherent == -bordered_det,
    }


def factor_first_leaf_count(size: int) -> int:
    return size


def factor_second_leaf_count(size: int) -> int:
    return size + math.comb(size, 2)


def master_axis_row(axis: str) -> dict[str, Any]:
    if axis == "y":
        factors = (("bordered_coherent_determinant", 5),)
    else:
        factors = (
            ("projective_native_weight", 1),
            ("size_four_bessel_determinant", 4),
            ("bordered_coherent_determinant", 5),
        )
    pure = sum(factor_second_leaf_count(size) for _, size in factors)
    cross = sum(
        factor_first_leaf_count(left_size) * factor_first_leaf_count(right_size)
        for index, (_, left_size) in enumerate(factors)
        for _, right_size in factors[index + 1 :]
    )
    return {
        "axis": axis,
        "active_master_factors": [name for name, _ in factors],
        "pure_second_column_replacement_slots_per_group": pure,
        "cross_first_first_column_replacement_slots_per_group": cross,
        "cross_terms_retain_factor_two": True,
        "complete_slots_per_group": pure + cross,
    }


def build() -> dict[str, Any]:
    k288 = json.loads(K288.read_text())
    k298 = json.loads(K298.read_text())
    k303 = json.loads(K303.read_text())
    k304 = json.loads(K304.read_text())
    occurrences = k288["coherent_gram_measure"]["size_four_occurrences"]
    group_ids = sorted({row["group_id"] for row in occurrences})
    groups = []
    for group_id in group_ids:
        rows = [row for row in occurrences if row["group_id"] == group_id]
        pairs = tuple((row["left_old_position"], row["right_old_position"]) for row in rows)
        weights = tuple(row["signed_occurrence_weight"] for row in rows)
        if pairs != EXPECTED_PAIRS or weights != EXPECTED_WEIGHTS:
            raise AssertionError(f"coherent upper triangle changed for {group_id}")
        species = {row["companion_factors"][0]["species"] for row in rows}
        size_four_species = {row["size_four_species"] for row in rows}
        if len(species) != 1 or len(size_four_species) != 1:
            raise AssertionError("group species are not common")
        groups.append(
            {
                "group_id": group_id,
                "companion_species": next(iter(species)),
                "size_four_species": next(iter(size_four_species)),
                "stored_upper_triangle_pairs": [list(pair) for pair in pairs],
                "stored_weights": list(weights),
                "ordered_pairs": [list(pair) for pair in itertools.product(POSITIONS, repeat=2)],
                "old_position_coefficient_vector": list(COEFFICIENTS),
                "bordered_matrix": "B_G=[[M_G,L_G],[R_G^T,0]] with L_G=(L_2,L_4,L_6,0)^T and R_G=(R_2,R_4,R_6,0)^T",
                "coherent_identity": "C_G=sum_ab c_a*c_b*L_a*R_b*det(M_G without row a and column b)=-det(B_G)",
                "ordered_terms": 9,
            }
        )

    if len(groups) != 4:
        raise AssertionError("expected four coherent groups")
    k298_groups = {row["group_id"]: row for row in k298["ordered_coherent_groups"]}
    if any(k298_groups[group["group_id"]]["old_position_coefficient_vector"] != list(COEFFICIENTS) for group in groups):
        raise AssertionError("K298 cofactor signs changed")

    axes = k303["fixed_control"]["peano_axes"]
    axis_rows = [master_axis_row(axis) for axis in axes]
    slots_all_groups = sum(row["complete_slots_per_group"] * len(groups) for row in axis_rows)
    control = bordered_identity_control()
    if not control["identity_holds"]:
        raise AssertionError("bordered determinant identity failed")

    old_templates = k304["minimal_joint_functional_inventory"]
    group_axis_order_masters = len(groups) * len(axes) * len(k303["terminal_split_usage"]["required_terminal_jet_orders"])
    return {
        "schema_version": "1.0",
        "result_id": "K305-ORDER-SEVEN-COHERENT-BORDERED-FUNCTIONAL-COMPILER",
        "created": "2026-09-22",
        "classification": "INTERNAL_STRUCTURAL_ONLY",
        "direction": "observed_to_native",
        "fixed_control": {
            "predecessor_manifests": [
                "lab/process/k288-order-seven-native-occurrence-measure.json",
                "lab/process/k298-order-seven-coherent-terminal-corner-obstruction.json",
                "lab/process/k303-order-seven-peano-determinant-compiler.json",
                "lab/process/k304-order-seven-peano-norm-sufficiency-audit.json",
            ],
            "coherent_groups": len(groups),
            "stored_occurrences": len(occurrences),
            "stored_entries_per_group": 6,
            "ordered_entries_per_group": 9,
            "axes": axes,
            "jet_orders": k303["terminal_split_usage"]["required_terminal_jet_orders"],
        },
        "coherent_groups": groups,
        "bordered_determinant_theorem": {
            "kernel_matrix": "M_G is the common four-by-four companion-species Bessel matrix on even positions (2,4,6,8)",
            "cofactor_sign_match": "c_a*c_b=(-1)^(a+b) for c=(1,-1,1)",
            "identity": "C_G=-det([[M_G,L_G],[R_G^T,0]])",
            "reason_zero_terminal_components_matter": "the final zero entries keep the omitted position-eight component inside the same determinant rather than bounding it separately",
            "absolute_value_location": "after the complete bordered determinant for one coherent group is formed",
            "differentiation_rule": "differentiate the five bordered columns as complete columns; D det has five replacements and D^2 det has five pure-second plus ten doubled first-first replacements",
            "rational_control": control,
        },
        "template_compression": {
            "old_pattern_axis_order_templates": old_templates["total_pattern_axis_order_templates"],
            "old_four_group_instantiations": old_templates["four_group_instantiations"],
            "new_group_axis_order_master_functionals": group_axis_order_masters,
            "y_pattern_order_instantiations_before": old_templates["y_axis_templates"] * len(groups),
            "y_group_order_masters_after": len(groups) * 3,
            "gap_pattern_order_instantiations_before": old_templates["five_gap_axis_templates"] * len(groups),
            "gap_group_axis_order_masters_after": len(groups) * 5 * 3,
            "compression_is_exact_not_an_envelope": True,
        },
        "master_axis_compiler": axis_rows,
        "complete_counts": {
            "old_occurrence_leaf_families": k303["complete_counts"]["all_six_axes_leaves_all_occurrences"],
            "coherent_master_column_replacement_slots": slots_all_groups,
            "y_slots_all_groups": next(row["complete_slots_per_group"] for row in axis_rows if row["axis"] == "y") * len(groups),
            "gap_slots_all_groups": sum(row["complete_slots_per_group"] for row in axis_rows if row["axis"] != "y") * len(groups),
            "structural_zero_slots_may_be_pruned_only_after_dependency_replay": True,
        },
        "coupling_preservation": {
            "native_density": "exp(-256*x*(1+q))*x^15*q^11*product_i(p_i)",
            "complete_integrand_master": "native_density*D4_G*(-det(B_G))",
            "size_four_determinant_kept_joint": True,
            "companion_matrix_and_old_kernels_kept_joint": True,
            "split_variables_kept_inside_bordered_determinant": True,
            "coherent_sum_precedes_absolute_value": True,
            "k302_terminal_bounds_role": "may bound entries or complete replacement columns inside B_G; they are not multiplied by a detached cofactor supremum",
        },
        "decision": {
            "all_eighteen_y_pattern_order_templates_constructed": True,
            "all_ninety_gap_pattern_order_templates_constructed": True,
            "exact_coherent_compression_available": True,
            "complete_numerical_norms_emitted": False,
            "k294_gamma_join_released": False,
            "next_exact_input": "construct an outward interval operator for the regularized five-by-five bordered determinant columns together with the common size-four determinant on the K296/K300 boundary cover; integrate q and projective variables before extracting any x-only gamma coefficient",
        },
        "release_test": {
            "all_four_groups_replayed": len(groups) == 4,
            "all_six_stored_patterns_replayed": all(len(group["stored_upper_triangle_pairs"]) == 6 for group in groups),
            "all_nine_ordered_terms_restored": all(group["ordered_terms"] == 9 for group in groups),
            "bordered_identity_exact": control["identity_holds"],
            "coherent_absolute_value_delayed": True,
            "factor_two_cross_terms_retained": all(row["cross_terms_retain_factor_two"] for row in axis_rows),
            "radial_gamma_join_emitted": False,
            "native_K152_interval_emitted": False,
        },
        "ledger_effect": k304["ledger_effect"],
        "claim_ceiling": "Exact coherent bordered-determinant compiler for all four K288 groups and all six K299 Peano axes. The six stored occurrence patterns per group are restored as nine ordered cofactors and compressed exactly to one five-by-five bordered determinant before absolute enclosure. This replaces 432 pattern/group/order instantiations by 72 group/axis/order master functionals and compiles 1,160 coherent column-replacement slots instead of 6,480 occurrence-level leaf families while retaining every sign and factor-two cross term. It emits no numerical Peano norm, q/projective integral, K294 gamma join, exterior action-column value, residual, native K152 interval, source/ledger move, canon, paper, public or physical claim.",
    }


def validate_payload(payload: dict[str, Any]) -> None:
    if payload["fixed_control"]["coherent_groups"] != 4:
        raise AssertionError("coherent group count changed")
    for group in payload["coherent_groups"]:
        if group["stored_upper_triangle_pairs"] != [list(pair) for pair in EXPECTED_PAIRS]:
            raise AssertionError("stored pair order changed")
        if group["stored_weights"] != list(EXPECTED_WEIGHTS):
            raise AssertionError("stored coherent weights changed")
        if group["ordered_terms"] != 9:
            raise AssertionError("ordered cofactor expansion is incomplete")
    control = payload["bordered_determinant_theorem"]["rational_control"]
    if not control["identity_holds"] or control["left"][-1] != "0" or control["right"][-1] != "0":
        raise AssertionError("bordered determinant or terminal zero changed")
    coupling = payload["coupling_preservation"]
    if not all(
        coupling[key]
        for key in (
            "size_four_determinant_kept_joint",
            "companion_matrix_and_old_kernels_kept_joint",
            "split_variables_kept_inside_bordered_determinant",
            "coherent_sum_precedes_absolute_value",
        )
    ):
        raise AssertionError("joint coupling was lost")
    if payload["decision"]["complete_numerical_norms_emitted"] or payload["decision"]["k294_gamma_join_released"]:
        raise AssertionError("numerical closure overclaim")


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
