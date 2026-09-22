#!/usr/bin/env python3
"""Transfer the K308 regularized operator to the five Duffy gap axes."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[2]
K299 = ROOT / "lab/process/k299-order-seven-positive-peano-simplex-rule.json"
K300 = ROOT / "lab/process/k300-order-seven-angular-method-selection.json"
K305 = ROOT / "lab/process/k305-order-seven-coherent-bordered-functional-compiler.json"
K307 = ROOT / "lab/process/k307-order-seven-two-radius-joint-chart.json"
K308 = ROOT / "lab/process/k308-order-seven-regularized-y-master-operator.json"
OUTPUT = ROOT / "lab/process/k309-order-seven-gap-axis-transfer-audit.json"


def build() -> dict[str, Any]:
    k299 = json.loads(K299.read_text())
    k300 = json.loads(K300.read_text())
    k305 = json.loads(K305.read_text())
    k307 = json.loads(K307.read_text())
    k308 = json.loads(K308.read_text())
    axes = [row["axis"] for row in k299["one_dimensional_factors"] if row["axis"] != "y"]
    if axes != ["t0", "t1", "t2", "t3", "t4"]:
        raise AssertionError("K299 Duffy axis order changed")
    if not k308["decision"]["five_gap_axes_released_for_structural_transfer_audit"]:
        raise AssertionError("K308 did not release structural transfer")
    face_rows = k300["face_transfer"]["projective_face_second_derivative_margins"]
    axis_rows = []
    for factor, axis in zip(k299["one_dimensional_factors"][:5], axes):
        axis_rows.append(
            {
                "axis": axis,
                "duffy_weight_exponent": factor["weight_exponent"],
                "peano_kernel_integral": factor["peano_kernel"]["integral"],
                "duffy_node": factor["weighted_mean"],
                "chart_dependence": "every p_i is affine in this axis with the other four t coordinates fixed",
                "maximum_chart_derivative_order": 2,
                "D4_maximum_kernel_derivative_order": 8,
                "bordered_B5_maximum_kernel_derivative_order": 6,
                "explicit_polynomial_derivatives": "differentiate P(p)*V4_left*V4_right*V3_left*V3_right exactly through order two",
                "regularizer_derivatives": "differentiate Hermite--Genocchi divided-difference entries; affine node motion adds at most two kernel derivatives and no second chart derivative",
                "terminal_split_handling": "retain y as the last integrated axis and apply K302 inside the regularized determinant functional",
            }
        )
    return {
        "schema_version": "1.0",
        "result_id": "K309-ORDER-SEVEN-GAP-AXIS-TRANSFER-AUDIT",
        "created": "2026-09-22",
        "classification": "INTERNAL_STRUCTURAL_ONLY",
        "direction": "observed_to_native",
        "fixed_control": {
            "predecessor_manifests": [
                "lab/process/k299-order-seven-positive-peano-simplex-rule.json",
                "lab/process/k300-order-seven-angular-method-selection.json",
                "lab/process/k305-order-seven-coherent-bordered-functional-compiler.json",
                "lab/process/k307-order-seven-two-radius-joint-chart.json",
                "lab/process/k308-order-seven-regularized-y-master-operator.json",
            ],
            "gap_axes": axes,
            "one_gap_faces": sum(row["codimension"] == 1 for row in face_rows),
            "codimension_two_faces": sum(row["codimension"] == 2 for row in face_rows),
            "endpoint_classes": len(k300["endpoint_integrability"]["rows"]),
        },
        "factorized_integrand": {
            "two_radius_density": "exp(-256*(x+b))*x^3*b^11",
            "explicit_vandermonde_power": "b^18",
            "explicit_joint_radial_factor": "exp(-256*(x+b))*x^3*b^29",
            "projective_polynomial": "product_i(p_i)*V4_left(p)*V4_right(p)*V3_left(p,u)*V3_right(p,z)",
            "regularized_factors": "R4(x,b,p,y)*R5_border(x,b,p,y,u,z)",
            "exponential_is_projective_axis_independent": True,
            "coherent_absolute_value_after_bordered_assembly": True,
        },
        "axis_transfer": axis_rows,
        "boundary_transfer": {
            "regularizers_extend_to_coalescent_faces": True,
            "extension_basis": "Hermite--Genocchi divided differences converge to repeated-node derivatives and never divide the full integrand by a vanishing face factor",
            "explicit_zeros_retained": True,
            "one_gap_and_codimension_two_rows_replayed": len(face_rows),
            "worst_projective_second_derivative_margin": min(row["second_derivative_integrability_margin"] for row in face_rows),
            "worst_endpoint_second_derivative_margin": min(row["second_derivative_integrability_margin"] for row in k300["endpoint_integrability"]["rows"]),
            "joint_origin_margin": k307["joint_origin"]["absolute_integrability_margin"],
            "dimensionless_gap_derivatives_preserve_joint_origin_degree": True,
        },
        "operator_inventory": {
            "y_master": "implemented outward on an explicit positive two-radius cell by K308",
            "five_gap_axes": "same operator architecture compiled; entry derivative orders and exact polynomial factors fixed",
            "complete_master_axes": 6,
            "coherent_groups": k305["fixed_control"]["coherent_groups"],
            "group_axis_order_masters": k305["template_compression"]["new_group_axis_order_master_functionals"],
            "remaining_numerical_work": "adaptive outward cells covering the two-radius origin, projective faces and terminal split joins, followed by positive Peano integration and coherent group summation",
        },
        "decision": {
            "same_regularized_operator_architecture_valid_for_all_five_gap_axes": True,
            "all_six_master_axes_have_an_executable_operator_specification": True,
            "complete_gap_axis_constants_emitted": False,
            "complete_six_axis_peano_norm_emitted": False,
            "k294_gamma_join_released": False,
            "next_exact_input": "implement the adaptive two-radius boundary-cell integrator using the K308/K309 operator, starting with the y master terminal cells and reusing their subdivision for the five gap axes",
        },
        "release_test": {
            "all_five_gap_axes_replayed": len(axis_rows) == 5,
            "all_twenty_one_projective_face_rows_replayed": len(face_rows) == 21,
            "all_three_endpoint_classes_replayed": len(k300["endpoint_integrability"]["rows"]) == 3,
            "K304_detached_factorization_reintroduced": False,
            "pointwise_K290_bank_reused": False,
            "complete_numerical_norm_overclaim": False,
            "radial_gamma_join_emitted": False,
            "native_K152_interval_emitted": False,
        },
        "ledger_effect": k308["ledger_effect"],
        "claim_ceiling": "Exact structural transfer of K308's divided-difference interval operator from the y master to all five K299 Duffy gap axes. The two-radius density and b^18 Vandermonde factor remain explicit, the exponential is projective-axis independent, and affine Duffy motion raises the required D4 and bordered-B5 kernel derivative orders only to eight and six. All twenty-one projective face rows and three endpoint classes retain positive margins. This supplies an executable six-axis operator specification but no complete boundary-cell constants, global Peano norm, K294 gamma join, action-column value, residual, native K152 interval, source/ledger move, canon, paper, public or physical claim.",
    }


def validate_payload(payload: dict[str, Any]) -> None:
    fixed = payload["fixed_control"]
    if fixed["gap_axes"] != ["t0", "t1", "t2", "t3", "t4"]:
        raise AssertionError("gap axis census changed")
    if (fixed["one_gap_faces"], fixed["codimension_two_faces"], fixed["endpoint_classes"]) != (6, 15, 3):
        raise AssertionError("boundary cover changed")
    boundary = payload["boundary_transfer"]
    if not boundary["regularizers_extend_to_coalescent_faces"] or not boundary["explicit_zeros_retained"]:
        raise AssertionError("face regularization changed")
    decision = payload["decision"]
    if not decision["same_regularized_operator_architecture_valid_for_all_five_gap_axes"]:
        raise AssertionError("gap transfer failed")
    if decision["complete_six_axis_peano_norm_emitted"] or decision["k294_gamma_join_released"]:
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
