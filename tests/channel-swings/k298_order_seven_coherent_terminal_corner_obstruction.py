#!/usr/bin/env python3
"""Restore the ordered coherent sum and resolve the K297 terminal corner."""

from __future__ import annotations

import argparse
import itertools
import json
from fractions import Fraction
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[2]
K280 = ROOT / "lab/process/k280-order-seven-bessel-vandermonde-face-atlas.json"
K296 = ROOT / "lab/process/k296-order-seven-coalescent-face-valuation-atlas.json"
K297 = ROOT / "lab/process/k297-order-seven-endpoint-corner-integrability.json"
OUTPUT = ROOT / "lab/process/k298-order-seven-coherent-terminal-corner-obstruction.json"


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


def coherent_groups() -> list[dict[str, Any]]:
    k296 = json.loads(K296.read_text())
    rows = k296["occurrence_census"]
    group_ids = sorted({row["group_id"] for row in rows})
    groups = []
    for group_id in group_ids:
        group = [row for row in rows if row["group_id"] == group_id]
        pairs = [
            [int(row["left_old_position"]), int(row["right_old_position"])]
            for row in group
        ]
        weights = [int(row["signed_occurrence_weight"]) for row in group]
        expected_pairs = [[2, 2], [2, 4], [2, 6], [4, 4], [4, 6], [6, 6]]
        expected_weights = [1, -2, 2, 1, -2, 1]
        if pairs != expected_pairs or weights != expected_weights:
            raise AssertionError("coherent upper triangle changed")
        coefficients = [1, -1, 1]
        ordered = []
        for i, j in itertools.product(range(3), repeat=2):
            ordered.append(
                {
                    "left_old_position": 2 * (i + 1),
                    "right_old_position": 2 * (j + 1),
                    "coefficient_product": coefficients[i] * coefficients[j],
                    "cofactor_sign": -1 if (i + j) % 2 else 1,
                    "signs_match": coefficients[i] * coefficients[j] == (-1 if (i + j) % 2 else 1),
                }
            )
        groups.append(
            {
                "group_id": group_id,
                "stored_upper_triangle_entries": len(group),
                "stored_pairs": pairs,
                "stored_integral_weights": weights,
                "old_position_coefficient_vector": coefficients,
                "ordered_pointwise_entries": ordered,
                "ordered_entry_count": len(ordered),
                "all_coefficient_products_equal_cofactor_signs": all(row["signs_match"] for row in ordered),
            }
        )
    return groups


def exact_cauchy_control() -> dict[str, Any]:
    left = [Fraction(7), Fraction(5), Fraction(2), Fraction(0)]
    right = [Fraction(11), Fraction(7), Fraction(3), Fraction(1)]
    matrix = [[Fraction(2, l + r) for r in right] for l in left]
    full_zero_node_row = [Fraction(2, r) for r in right]
    truncated = full_zero_node_row[:3] + [Fraction(0)]
    replaced = [row[:] for row in matrix]
    replaced[2] = truncated
    minor = [[matrix[i][j] for j in (0, 1, 2)] for i in (0, 1, 3)]
    replaced_det = determinant(replaced)
    minor_det = determinant(minor)
    omitted_component = full_zero_node_row[3]
    return {
        "left_nodes": [str(value) for value in left],
        "right_nodes": [str(value) for value in right],
        "terminal_row_replacement_determinant": str(replaced_det),
        "omitted_position_eight_kernel": str(omitted_component),
        "positive_size_three_minor": str(minor_det),
        "exact_identity": "det(M with row 6 replaced by [K(U2),K(U4),K(U6),0]) = K(U8)*det(M rows 2,4,8 and columns 2,4,6)",
        "identity_holds": replaced_det == omitted_component * minor_det,
        "strictly_positive": replaced_det > 0 and omitted_component > 0 and minor_det > 0,
        "role": "exact rational Cauchy control of the kernel-independent cofactor algebra; Bessel positivity uses K280 Andreief",
    }


def build() -> dict[str, Any]:
    k280 = json.loads(K280.read_text())
    k297 = json.loads(K297.read_text())
    groups = coherent_groups()
    control = exact_cauchy_control()
    return {
        "schema_version": "1.0",
        "result_id": "K298-ORDER-SEVEN-COHERENT-TERMINAL-CORNER-OBSTRUCTION",
        "created": "2026-09-22",
        "classification": "INTERNAL_STRUCTURAL_ONLY",
        "direction": "observed_to_native",
        "fixed_control": {
            "predecessor_manifests": [
                "lab/process/k280-order-seven-bessel-vandermonde-face-atlas.json",
                "lab/process/k296-order-seven-coalescent-face-valuation-atlas.json",
                "lab/process/k297-order-seven-endpoint-corner-integrability.json",
            ],
            "coherent_groups": len(groups),
            "old_positions": [2, 4, 6],
            "stored_entries_per_group": 6,
            "ordered_entries_per_group": 9,
            "terminal_old_position": 6,
        },
        "ordered_coherent_groups": groups,
        "cofactor_theorem": {
            "kernel_matrix": "M_ab=2*K1(T_(2a)+U_(2b)) on even positions (2,4,6,8)",
            "ordered_sum": "sum_{a,b=1}^3 c_a*c_b*L_a*R_b*det(M with row a and column b deleted), c=(1,-1,1)",
            "cofactor_sign_identity": "c_a*c_b=(-1)^(a+b), so the ordered sum is a truncated adjugate bilinear form",
            "terminal_singular_coefficient": "L_6 times det(M with row 6 replaced by [R_2,R_4,R_6,0])",
            "terminal_limit": "at T_6=T_8=0 the full row [K(U_2),K(U_4),K(U_6),K(U_8)] equals row 8; subtracting the omitted K(U_8) component leaves K(U_8) times the rows-(2,4,8), columns-(2,4,6) minor",
            "bessel_minor_strictly_positive": True,
            "positivity_basis": k280["factorization_certificate"]["strict_positivity"],
            "terminal_leading_coefficient_cancels": False,
        },
        "exact_cauchy_control": control,
        "integrability_consequence": {
            "k297_terminal_homogeneous_degree": -2,
            "corner_dimension": 2,
            "fourth_derivative_absolute_integrability_margin": 0,
            "divergence": "logarithmic",
            "each_coherent_group_has_nonzero_positive_leading_coefficient": True,
            "complete_four_group_fourth_derivative_locally_absolutely_integrable": False,
            "integrand_itself_locally_integrable": True,
            "integrand_or_integral_divergence_proved": False,
        },
        "decision": {
            "ordered_pointwise_sum_restored": True,
            "upper_triangle_integral_compression_used_for_pointwise_cancellation": False,
            "coherent_cancellation_repairs_fourth_order_terminal_corner": False,
            "global_fourth_derivative_jacobi_route_legal": False,
            "required_method_switch": "use a positive rule whose remainder requires at most third shape derivatives, or subtract/integrate the explicit terminal singular model before bounding a smooth remainder",
            "k294_radial_gamma_composition_released": False,
            "next_exact_input": "construct and compare a third-derivative positive cubature remainder with an analytic terminal-singularity subtraction on the K294 simplex, retaining the ordered coherent group and exact radial gamma weight",
        },
        "release_test": {
            "all_four_groups_replayed": len(groups) == 4,
            "all_groups_restore_nine_ordered_entries": all(group["ordered_entry_count"] == 9 for group in groups),
            "all_ordered_signs_match_cofactors": all(group["all_coefficient_products_equal_cofactor_signs"] for group in groups),
            "exact_cauchy_control_positive": control["identity_holds"] and control["strictly_positive"],
            "complete_integrand_divergence_claimed": False,
            "complete_exterior_integrand_bound_emitted": False,
            "complete_base_action_column_evaluated": False,
            "native_K152_interval_emitted": False,
        },
        "ledger_effect": k297["ledger_effect"],
        "claim_ceiling": "Exact ordered-coherent cofactor theorem for the four K288 size-four groups and proof that the terminal old-position-six leading coefficient is a strictly positive omitted-position-eight kernel times a positive size-three Bessel minor. Coherent cancellation therefore does not repair the logarithmically nonintegrable fourth shape derivative. The integrand itself remains locally integrable; no divergence of its value or native integral, complete exterior bound, action-column value, residual, native K152 interval, source/ledger move, canon, paper or public claim is established.",
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--write", action="store_true")
    args = parser.parse_args()
    rendered = json.dumps(build(), indent=2, sort_keys=True) + "\n"
    if args.write:
        OUTPUT.write_text(rendered)
    else:
        print(rendered, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
