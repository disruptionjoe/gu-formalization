#!/usr/bin/env python3
"""Compose K291's derivative ceiling over the complete K292 native tube."""

from __future__ import annotations

import argparse
import json
from decimal import Decimal, getcontext
from fractions import Fraction
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[2]
K291 = ROOT / "lab/process/k291-order-seven-native-interior-remainder.json"
K292 = ROOT / "lab/process/k292-order-seven-disjoint-native-tube-atlas.json"
OUTPUT = ROOT / "lab/process/k293-order-seven-complete-native-tube-remainder.json"
getcontext().prec = 110


def dec(value: Any) -> Decimal:
    if isinstance(value, str) and "/" in value:
        q = Fraction(value)
        return Decimal(q.numerator) / Decimal(q.denominator)
    return Decimal(str(value))


def build() -> dict[str, Any]:
    k291 = json.loads(K291.read_text())
    k292 = json.loads(K292.read_text())
    m4 = dec(k291["native_density_remainder"]["complete_four_group_fourth_shape_derivative_abs_upper"])
    h = dec(k292["fixed_control"]["transverse_shape_radius"])
    x_width = dec(k291["native_density_remainder"]["x_interval_width"])
    start_volume = dec(k292["strata"]["start_box"]["exact_native_volume"])
    start_normalized = Decimal(6) * h**4 * m4 / Decimal(270)
    start_integral = start_volume * start_normalized
    faces = []
    swept_total = Decimal(0)
    face_normalized = Decimal(5) * h**4 * m4 / Decimal(270)
    for source in k292["strata"]["swept_faces"]:
        volume = dec(source["exact_native_volume"])
        bound = volume * face_normalized
        swept_total += bound
        faces.append(
            {
                "stratum_id": source["stratum_id"],
                "advancing_coordinate": source["advancing_coordinate"],
                "native_jacobian": source["native_jacobian"],
                "free_shape_axes": 5,
                "normalized_shape_remainder_abs_upper": str(face_normalized),
                "native_shape_integral_remainder_abs_upper": str(bound),
            }
        )
    total_shape = start_integral + swept_total
    full = x_width * total_shape
    return {
        "schema_version": "1.0",
        "result_id": "K293-ORDER-SEVEN-COMPLETE-NATIVE-TUBE-REMAINDER",
        "created": "2026-09-21",
        "classification": "INTERNAL_STRUCTURAL_ONLY",
        "direction": "observed_to_native",
        "fixed_control": {
            "derivative_manifest": "lab/process/k291-order-seven-native-interior-remainder.json",
            "atlas_manifest": "lab/process/k292-order-seven-disjoint-native-tube-atlas.json",
            "complete_four_group_fourth_shape_derivative_abs_upper": str(m4),
            "transverse_shape_radius": k292["fixed_control"]["transverse_shape_radius"],
            "x_interval_width": str(x_width),
            "y_u_z_domain_volume": "1",
            "nodes_per_free_shape_axis": 2,
        },
        "remainder_rule": {
            "one_axis_normalized_two_node_gauss_legendre": "h^4*M4/270",
            "start_box": "six-axis positive telescope times exact start-box volume",
            "swept_faces": "five-axis positive telescope times exact face volume including b_k Jacobian",
            "scale_coordinate": "t is integrated against the uniform M4 supremum; no t-quadrature error is introduced",
            "coherent_measure_scope": "M4 already sums the four K288 coherent groups after groupwise enclosure and includes the K290 native density",
        },
        "start_box": {
            "free_shape_axes": 6,
            "normalized_shape_remainder_abs_upper": str(start_normalized),
            "native_shape_integral_remainder_abs_upper": str(start_integral),
        },
        "swept_faces": faces,
        "complete_native_tube_remainder": {
            "start_box_contribution": str(start_integral),
            "swept_faces_contribution": str(swept_total),
            "native_shape_integral_abs_upper": str(total_shape),
            "x_y_u_z_integrated_abs_upper": str(full),
            "complete_k284_interior_tube_serialized": True,
            "radial_or_projective_exterior_serialized": False,
        },
        "decision": {
            "interior_geometry_blocker_closed": True,
            "complete_native_tube_remainder_serialized": True,
            "action_column_ready": False,
            "next_exact_input": "construct a radial/projective exterior atlas and compatible complete-integrand bounds before joining the interior result to an action-column enclosure",
        },
        "release_test": {
            "all_seven_disjoint_strata_composed": len(faces) == 6,
            "all_face_jacobians_included": True,
            "complete_four_group_native_density_derivative_ceiling_used": True,
            "complete_k284_interior_tube_remainder_serialized": True,
            "complete_arbitrary_gap_ratio_domain_covered": False,
            "complete_base_action_column_evaluated": False,
            "native_K152_interval_emitted": False,
        },
        "ledger_effect": k291["ledger_effect"],
        "claim_ceiling": "Rigorous complete native-density-weighted two-node tensor remainder ceiling over the disjoint K284 interior tube, uniform in y,u,z and integrated over the K284 x cell; no radial/projective exterior bound, action-column value, complete residual, native K152 interval, physical state, source/ledger move, canon, paper or public claim.",
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
