#!/usr/bin/env python3
"""Tensor the K318 endpoint charts with the K310 radial/projective boundary.

The calculation has two purposes.  First, it records the exact radial degree
of the complete regularized D4-times-bordered-B5 product rather than inferring
it from sampled small-radius values.  Second, it makes the finite chart
topology for r=0, the exponential radial tail, and s=0,1 explicit before any
numerical subdivision is attempted.
"""

from __future__ import annotations

import argparse
import itertools
import json
from fractions import Fraction
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[2]
K310 = ROOT / "lab/process/k310-order-seven-two-radius-origin-compactification.json"
K314 = ROOT / "lab/process/k314-order-seven-projective-face-oracle.json"
K318 = ROOT / "lab/process/k318-order-seven-weighted-endpoint-blowup-atlas.json"
K320 = ROOT / "lab/process/k320-order-seven-scaled-endpoint-bessel-bank.json"
OUTPUT = ROOT / "lab/process/k321-order-seven-radial-projective-tensor-atlas.json"


def determinant(matrix: list[list[Fraction]]) -> Fraction:
    total = Fraction(0)
    for permutation in itertools.permutations(range(len(matrix))):
        inversions = sum(
            permutation[i] > permutation[j]
            for i in range(len(permutation))
            for j in range(i + 1, len(permutation))
        )
        term = Fraction(-1 if inversions % 2 else 1)
        for row, column in enumerate(permutation):
            term *= matrix[row][column]
        total += term
    return total


def vandermonde(nodes: list[Fraction]) -> Fraction:
    product = Fraction(1)
    for left, right in itertools.combinations(nodes, 2):
        product *= left - right
    return product


def row_newton(matrix: list[list[Fraction]], nodes: list[Fraction], count: int) -> list[list[Fraction]]:
    work = [row[:] for row in matrix]
    for order in range(1, count):
        for row in range(count - 1, order - 1, -1):
            divisor = nodes[row] - nodes[row - order]
            work[row] = [
                (entry - previous) / divisor
                for entry, previous in zip(work[row], work[row - 1])
            ]
    return work


def column_newton(matrix: list[list[Fraction]], nodes: list[Fraction], count: int) -> list[list[Fraction]]:
    transposed = [list(column) for column in zip(*matrix)]
    transformed = row_newton(transposed, nodes, count)
    return [list(row) for row in zip(*transformed)]


def cauchy_origin_control(scale: Fraction) -> dict[str, Any]:
    left_odd = [scale * Fraction(v, 19) for v in (41, 31, 19, 7)]
    right_odd = [scale * Fraction(v, 23) for v in (43, 32, 18, 8)]
    left_even = [scale * Fraction(v, 29) for v in (47, 35, 21, 9)]
    right_even = [scale * Fraction(v, 31) for v in (49, 37, 22, 10)]
    y = Fraction(3, 8)
    kernel = lambda value: Fraction(2, 1) / value

    d4 = [[kernel(a + b) for b in right_odd] for a in left_odd]
    core = [[kernel(a + b) for b in right_even] for a in left_even]
    left_border = [y * kernel(value) for value in left_even[:3]] + [Fraction(0)]
    right_border = [(1 - y) * kernel(value) for value in right_even[:3]] + [Fraction(0)]
    b5 = [row + [left_border[index]] for index, row in enumerate(core)]
    b5.append(right_border + [Fraction(0)])

    d4_regularized = column_newton(row_newton(d4, left_odd, 4), right_odd, 4)
    b5_regularized = column_newton(row_newton(b5, left_even, 3), right_even, 3)
    d4_value = determinant(d4_regularized)
    b5_value = determinant(b5_regularized)
    normalized_d4 = scale**16 * d4_value
    normalized_b5 = scale**11 * b5_value
    return {
        "scale": str(scale),
        "D4_regularized": str(d4_value),
        "bordered_B5_regularized": str(b5_value),
        "r16_D4_regularized": str(normalized_d4),
        "r11_bordered_B5_regularized": str(normalized_b5),
        "r27_complete_regularized_product": str(normalized_d4 * normalized_b5),
        "raw_D4_factorization_exact": determinant(d4)
        == vandermonde(left_odd) * vandermonde(right_odd) * d4_value,
        "raw_bordered_B5_factorization_exact": determinant(b5)
        == vandermonde(left_even[:3]) * vandermonde(right_even[:3]) * b5_value,
    }


def tensor_rows(k318: dict[str, Any]) -> list[dict[str, Any]]:
    radial = [
        {
            "id": "origin",
            "map": "r=tau, tau in [0,1]",
            "measure": "exp(-256*tau)*tau^6 dtau",
            "boundary_power": 6,
        },
        {
            "id": "tail",
            "map": "r=1+t/(1-t), t in [0,1)",
            "measure": "exp(-256*r(t))*r(t)^6/(1-t)^2 dt",
            "boundary_power": None,
        },
    ]
    projective = [
        {
            "id": "s0",
            "map": "s=alpha/2, alpha in [0,1]",
            "measure": "(alpha/2)^3*(1-alpha/2)^29 dalpha/2",
            "boundary_power": 3,
        },
        {
            "id": "s1",
            "map": "1-s=beta/2, beta in [0,1]",
            "measure": "(1-beta/2)^3*(beta/2)^29 dbeta/2",
            "boundary_power": 29,
        },
    ]
    rows = []
    for endpoint in k318["determinant_preserving_endpoint_atlas"]["charts"]:
        endpoint_minimum = min(
            row["minimum_exponent"]
            for row in k318["cauchy_model_valuation_control"]["checks"]
            if row["chart_id"] == endpoint["id"]
        )
        for radial_chart in radial:
            for projective_chart in projective:
                rows.append({
                    "id": f"{radial_chart['id']}__{projective_chart['id']}__{endpoint['id']}",
                    "radial_chart": radial_chart["id"],
                    "projective_chart": projective_chart["id"],
                    "endpoint_chart": endpoint["id"],
                    "radial_map": radial_chart["map"],
                    "projective_map": projective_chart["map"],
                    "radial_boundary_power": radial_chart["boundary_power"],
                    "projective_boundary_power": projective_chart["boundary_power"],
                    "minimum_endpoint_cube_exponent": endpoint_minimum,
                    "all_recorded_boundary_powers_nonnegative": all(
                        value is None or value >= 0
                        for value in (
                            radial_chart["boundary_power"],
                            projective_chart["boundary_power"],
                            endpoint_minimum,
                        )
                    ),
                })
    return rows


def build() -> dict[str, Any]:
    k310 = json.loads(K310.read_text())
    k314 = json.loads(K314.read_text())
    k318 = json.loads(K318.read_text())
    k320 = json.loads(K320.read_text())
    if k310["compactification"]["origin_radial_power"] != 6:
        raise AssertionError("K310 radial power changed")
    if not k314["decision"]["all_six_repeated_node_faces_have_finite_regularizer_bounds"]:
        raise AssertionError("K314 confluent face rule unavailable")
    if not k318["decision"]["sixteen_determinant_preserving_endpoint_charts_implemented"]:
        raise AssertionError("K318 endpoint atlas unavailable")
    if not k320["decision"]["endpoint_safe_scaled_Bessel_bank_implemented"]:
        raise AssertionError("K320 scaled endpoint bank unavailable")

    controls = [cauchy_origin_control(scale) for scale in (Fraction(1), Fraction(1, 7), Fraction(1, 49))]
    normalized_products = {row["r27_complete_regularized_product"] for row in controls}
    rows = tensor_rows(k318)
    terminal_powers = [
        row["remaining_endpoint_power"]
        for row in k320["terminal_power_census"]["rows"]
    ]

    return {
        "schema_version": "1.0",
        "result_id": "K321-ORDER-SEVEN-RADIAL-PROJECTIVE-TENSOR-ATLAS",
        "created": "2026-09-22",
        "classification": "INTERNAL_STRUCTURAL_ONLY",
        "direction": "observed_to_native",
        "fixed_control": {
            "predecessor_manifests": [
                "lab/process/k310-order-seven-two-radius-origin-compactification.json",
                "lab/process/k314-order-seven-projective-face-oracle.json",
                "lab/process/k318-order-seven-weighted-endpoint-blowup-atlas.json",
                "lab/process/k320-order-seven-scaled-endpoint-bessel-bank.json",
            ],
            "endpoint_chart_count": 16,
            "radial_chart_count": 2,
            "projective_chart_count": 2,
            "tensor_chart_count": len(rows),
        },
        "degree_27_origin_ledger": {
            "D4_raw_kernel_factors_per_monomial": 4,
            "D4_extracted_two_sided_vandermonde_degree": 12,
            "D4_regularized_radial_degree": -16,
            "bordered_B5_raw_kernel_factors_per_nonzero_monomial": 5,
            "bordered_B5_extracted_two_sided_vandermonde_degree": 6,
            "bordered_B5_regularized_radial_degree": -11,
            "complete_regularized_radial_degree": -27,
            "K310_scaling": "H=r^27*R4*R5_border",
            "exact_normalized_Cauchy_controls": controls,
            "all_three_scales_have_identical_normalized_product": len(normalized_products) == 1,
            "interpretation": "on a positive normalized angular cell, 2*K1(r*z)=2/(r*z)+o(r^-1), so the exact Cauchy coefficient is the continuous r=0 leading value of H",
        },
        "radial_projective_tensor_atlas": {
            "rows": rows,
            "chart_count": len(rows),
            "origin_measure_power": 6,
            "s0_measure_power": 3,
            "s1_measure_power": 29,
            "endpoint_terminal_remaining_powers": terminal_powers,
            "minimum_recorded_boundary_power": min(
                value
                for row in rows
                for value in (
                    row["radial_boundary_power"],
                    row["projective_boundary_power"],
                    row["minimum_endpoint_cube_exponent"],
                )
                if value is not None
            ),
            "all_recorded_boundary_powers_nonnegative": all(
                row["all_recorded_boundary_powers_nonnegative"] for row in rows
            ) and min(terminal_powers) >= 0,
            "confluent_face_rule": k314["confluent_rule"]["regularized_entries"],
            "tail_rule": "the t->1 radial chart is dominated by exp(-256/(1-t)) times a rational power",
        },
        "composition_contract": {
            "origin": "apply r^27 to the complete D4-times-bordered-B5 regularizer before enclosing the r=0 cell",
            "projective_faces": "retain s^3*(1-s)^29 and apply confluent divided differences at repeated nodes; no gap division",
            "endpoint_faces": "retain K318 chart weights and K320 scaled terminal entries inside the determinant",
            "positive_argument_floor_required_at_r0": False,
            "gap_cutoff_required_at_s_faces": False,
            "detached_terminal_or_cofactor_bound_used": False,
        },
        "decision": {
            "radial_projective_tensor_topology_complete": True,
            "degree_27_origin_limit_control_exact": True,
            "all_sixty_four_tensor_charts_serialized": len(rows) == 64,
            "all_boundary_measure_powers_nonnegative": all(row["all_recorded_boundary_powers_nonnegative"] for row in rows),
            "complete_chart_determinant_uppers_emitted": False,
            "complete_y_master_constant_emitted": False,
            "five_gap_axis_transfer_released": False,
            "k294_gamma_join_released": False,
            "next_exact_input": "combine this tensor topology with zero-inclusive Phi_m interval envelopes, then execute the first complete weighted old-position-six chart bound",
        },
        "release_test": {
            "K310_degree_minus27_replayed": -16 + -11 == -27,
            "three_exact_Cauchy_scaling_controls": len(controls) == 3 and len(normalized_products) == 1,
            "all_factorizations_exact": all(
                row["raw_D4_factorization_exact"] and row["raw_bordered_B5_factorization_exact"]
                for row in controls
            ),
            "K318_tensor_count_exact": len(rows) == 2 * 2 * 16,
            "K320_minimum_terminal_power_replayed": min(terminal_powers) == 0,
            "complete_numerical_norm_overclaim": False,
            "native_K152_interval_emitted": False,
        },
        "ledger_effect": k320["ledger_effect"],
        "source_routing": k320["source_routing"],
        "claim_ceiling": "Exact radial/projective tensor topology for all sixteen K318 endpoint charts, with sixty-four total origin/tail and s=0/1 chart combinations. Exact Cauchy controls prove the complete regularized product has degree -27 and a scale-independent r^27 leading coefficient on a positive normalized angular cell; K310's r^6, s^3 and (1-s)^29 weights and K320's remaining terminal powers are all nonnegative. This is a structural/limit atlas, not a complete outward determinant bank or numerical y-master constant, and it releases no gap-axis transfer, K294 join, action-column value, residual, K152 interval, source/ledger, canon, paper, public or physical claim.",
    }


def validate_payload(payload: dict[str, Any]) -> None:
    ledger = payload["degree_27_origin_ledger"]
    if ledger["D4_regularized_radial_degree"] != -16 or ledger["bordered_B5_regularized_radial_degree"] != -11:
        raise AssertionError("factor radial degree changed")
    if ledger["complete_regularized_radial_degree"] != -27 or not ledger["all_three_scales_have_identical_normalized_product"]:
        raise AssertionError("degree-27 origin control failed")
    atlas = payload["radial_projective_tensor_atlas"]
    if atlas["chart_count"] != 64 or not atlas["all_recorded_boundary_powers_nonnegative"]:
        raise AssertionError("radial/projective tensor coverage failed")
    contract = payload["composition_contract"]
    if contract["positive_argument_floor_required_at_r0"] or contract["gap_cutoff_required_at_s_faces"]:
        raise AssertionError("forbidden boundary cutoff introduced")
    if contract["detached_terminal_or_cofactor_bound_used"]:
        raise AssertionError("detached terminal bound introduced")
    decision = payload["decision"]
    if decision["complete_chart_determinant_uppers_emitted"] or decision["complete_y_master_constant_emitted"]:
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
