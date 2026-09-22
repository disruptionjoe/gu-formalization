#!/usr/bin/env python3
"""Prove K299 face legality and select it against terminal subtraction."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[2]
K296 = ROOT / "lab/process/k296-order-seven-coalescent-face-valuation-atlas.json"
K297 = ROOT / "lab/process/k297-order-seven-endpoint-corner-integrability.json"
K298 = ROOT / "lab/process/k298-order-seven-coherent-terminal-corner-obstruction.json"
K299 = ROOT / "lab/process/k299-order-seven-positive-peano-simplex-rule.json"
OUTPUT = ROOT / "lab/process/k300-order-seven-angular-method-selection.json"


def endpoint_rows(k297: dict[str, Any]) -> list[dict[str, Any]]:
    rows = []
    for row in k297["corner_table"]:
        derivative = row["derivative_orders"][2]
        third = row["derivative_orders"][3]
        rows.append(
            {
                "old_position": row["old_position"],
                "corner_variables": row["variables"],
                "second_derivative_homogeneous_degree": derivative["homogeneous_degree"],
                "second_derivative_integrability_margin": derivative["radial_integrability_margin"],
                "second_derivative_absolutely_integrable": derivative["absolutely_integrable"],
                "third_derivative_integrability_margin_control": third["radial_integrability_margin"],
                "fourth_derivative_verdict": row["derivative_orders"][4]["divergence"],
            }
        )
    return rows


def build() -> dict[str, Any]:
    k296 = json.loads(K296.read_text())
    k297 = json.loads(K297.read_text())
    k298 = json.loads(K298.read_text())
    k299 = json.loads(K299.read_text())
    rows = endpoint_rows(k297)
    worst_endpoint = min(row["second_derivative_integrability_margin"] for row in rows)
    one_gap_faces = [
        row for row in k296["projective_face_atlas"] if row["codimension"] == 1
    ]
    projective_face_margins = [
        {
            "face": row["face"],
            "codimension": row["codimension"],
            "minimum_native_cauchy_companion_valuation": row[
                "minimum_native_cauchy_companion_valuation"
            ],
            "second_derivative_integrability_margin": row[
                "minimum_native_cauchy_companion_valuation"
            ]
            - 2
            + row["codimension"],
        }
        for row in k296["projective_face_atlas"]
    ]
    worst_projective = min(
        row["second_derivative_integrability_margin"]
        for row in projective_face_margins
    )
    worst_complete = min(worst_endpoint, worst_projective)
    return {
        "schema_version": "1.0",
        "result_id": "K300-ORDER-SEVEN-ANGULAR-METHOD-SELECTION",
        "created": "2026-09-22",
        "classification": "INTERNAL_STRUCTURAL_ONLY",
        "direction": "observed_to_native",
        "fixed_control": {
            "predecessor_manifests": [
                "lab/process/k296-order-seven-coalescent-face-valuation-atlas.json",
                "lab/process/k297-order-seven-endpoint-corner-integrability.json",
                "lab/process/k298-order-seven-coherent-terminal-corner-obstruction.json",
                "lab/process/k299-order-seven-positive-peano-simplex-rule.json",
            ],
            "duffy_gap_order": ["r0", "r1", "r2", "c0", "c1", "c2"],
            "tensor_remainder_order": ["t0", "t1", "t2", "t3", "t4", "y"],
            "y_integrated_after_every_gap_error": True,
            "maximum_derivative_order": 2,
        },
        "face_transfer": {
            "projective_one_gap_faces_replayed": len(one_gap_faces),
            "every_one_gap_native_plus_cauchy_valuation": sorted(
                {
                    row["native_gap_product_valuation"]
                    + row["common_size_four_cauchy_valuation"]
                    for row in one_gap_faces
                }
            ),
            "left_terminal_gap": {"gap": "r2", "duffy_face": "t2=0", "peano_kernel_zero_order": 2},
            "right_terminal_gap": {"gap": "c2", "duffy_face": "t4=1 after earlier means are fixed", "peano_kernel_zero_order": 2},
            "duffy_jacobian_effect": "nonnegative polynomial face powers only; it adds vanishing and never divides out a K296 native or determinant zero",
            "directional_derivative_effect": "each Duffy axis is affine with other axes fixed; its second derivative is a linear combination of pure and mixed projective Hessian entries with the same or better K297 face degree",
            "higher_codimension_effect": "K297 positions 4 and 2 already include the three- and four-variable nested endpoint joins; additional Duffy Jacobian powers cannot worsen them",
            "projective_face_second_derivative_margins": projective_face_margins,
            "worst_projective_face_second_derivative_margin": worst_projective,
        },
        "endpoint_integrability": {
            "rows": rows,
            "worst_endpoint_second_derivative_margin": worst_endpoint,
            "worst_complete_face_second_derivative_margin": worst_complete,
            "all_second_directional_derivatives_locally_absolutely_integrable": all(row["second_derivative_absolutely_integrable"] for row in rows),
            "terminal_old_position_six_second_derivative_model": "d_g^2[g^2*y/(y+a*g)]=2*y^3/(y+a*g)^3, homogeneous degree zero for fixed positive split parameter a",
            "terminal_old_position_six_y_second_derivative_model": "d_y^2[g^2*y/(y+a*g)]=-2*a*g^3/(y+a*g)^3, homogeneous degree zero for fixed positive split parameter a",
            "third_derivative_spare_margin_at_terminal_corner": next(row["third_derivative_integrability_margin_control"] for row in rows if row["old_position"] == 6),
            "fourth_derivative_obstruction_preserved": not k298["decision"]["global_fourth_derivative_jacobi_route_legal"],
        },
        "global_legality": {
            "interior": "smooth because every cumulative time is strictly positive",
            "boundary_cover": "K296 one-gap/codimension-two atlas plus K297 nested old-position endpoint corners",
            "finite_cover": True,
            "peano_remainder_locally_absolutely_integrable_on_complete_angular_domain": True,
            "qualitative_global_remainder_finite": True,
            "numerical_global_remainder_enclosed": False,
            "reason_numerical_bound_open": "the six complete coherent second-directional Peano norms still require a uniform interval enclosure over q,x,u,z and the remaining angular cross-sections",
        },
        "method_comparison": {
            "positive_peano": {
                "terminal_local_models": 0,
                "cutoff_or_partition_functions": 0,
                "overlap_counterterms": 0,
                "global_norm_obligations": 6,
                "maximum_derivative_order": 2,
                "positive_nodes": 1,
                "status": "selected_structural_route",
            },
            "analytic_subtraction": {
                "minimum_terminal_sector_models": 8,
                "sector_count_basis": "four coherent groups times left/right terminal corners",
                "required_global_coefficient_functions": 8,
                "required_additional_proofs": [
                    "construct compatible cutoffs or a partition of unity on overlapping terminal faces",
                    "integrate every coefficient-weighted singular model on the exact simplex",
                    "prove the subtracted residual has an integrable fourth derivative across sector overlaps",
                ],
                "maximum_residual_derivative_order": 4,
                "status": "dominated_fallback_not_executed",
            },
            "selection": "positive_peano",
            "selection_basis": "K299 gives an exact positive one-node rule and K296/K297 prove its six second-directional Peano terms finite without cutoffs; subtraction introduces eight coefficient functions, overlap ownership and a fourth-derivative residual proof before providing a bound",
        },
        "decision": {
            "positive_rule_face_legal": True,
            "positive_rule_selected_over_analytic_subtraction": True,
            "analytic_subtraction_killed_globally": False,
            "complete_global_second_directional_norms_computed": False,
            "k294_low_middle_high_gamma_strata_joined": False,
            "next_exact_input": "construct a determinant-preserving interval enclosure for the six complete coherent second-directional Peano norms, first on the q/projective angular domain at fixed x and then with explicit q and x scaling, before composing K294's gamma strata",
        },
        "release_test": {
            "all_six_one_gap_faces_replayed": len(one_gap_faces) == 6,
            "all_three_endpoint_classes_replayed": len(rows) == 3,
            "worst_second_derivative_margin_strictly_positive": worst_complete > 0,
            "terminal_fourth_derivative_obstruction_not_reused": k299["peano_remainder"]["maximum_derivative_order"] == 2,
            "complete_exterior_integrand_bound_emitted": False,
            "complete_base_action_column_evaluated": False,
            "native_K152_interval_emitted": False,
        },
        "ledger_effect": k298["ledger_effect"],
        "claim_ceiling": "Exact transfer of the K299 positive Peano rule through the complete K296/K297 face atlas. All six required second-directional remainder terms are locally absolutely integrable; the worst pure projective-face margin is one and the worst terminal endpoint margin is two, while K298's fourth-derivative logarithm remains excluded. This proves a finite qualitative angular remainder and selects the positive rule over an eight-sector analytic-subtraction construction, but it does not numerically enclose the six global derivative norms, join K294's radial gamma strata, evaluate an exterior action column or residual, emit a native K152 interval, or move source, ledger, canon, paper or public posture.",
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
