#!/usr/bin/env python3
"""K287 two-node tensor Gauss--Jacobi remainder on the K284 tube."""

from __future__ import annotations

import argparse
import json
from decimal import Decimal, getcontext
from fractions import Fraction
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[2]
K284_MANIFEST = ROOT / "lab/process/k284-order-seven-transverse-shape-atlas.json"
K286_MANIFEST = ROOT / "lab/process/k286-order-seven-mixed-shape-derivative-bank.json"
OUTPUT = ROOT / "lab/process/k287-order-seven-tensor-jacobi-remainder.json"
getcontext().prec = 100


def build() -> dict[str, Any]:
    tube = json.loads(K284_MANIFEST.read_text())
    bank = json.loads(K286_MANIFEST.read_text())
    radius = Fraction(tube["fixed_control"]["transverse_shape_radius"])
    fourth = Decimal(str(
        bank["mixed_shape_derivative_bank"]
        ["global_componentwise_mixed_derivative_abs_upper"]["4"]
    ))
    # For the normalized average 1/2 int_{-1}^1, the two-node
    # Gauss-Legendre/Jacobi(0,0) remainder coefficient is 1/270.  The affine
    # map eta=h*x contributes h^4.  A positive tensor-product telescoping sum
    # over six axes therefore contributes at most 6*h^4*M4/270.
    h = Decimal(radius.numerator) / Decimal(radius.denominator)
    one_axis = h ** 4 * fourth / Decimal(270)
    tensor = Decimal(6) * one_axis
    lower = Decimal(str(tube["transverse_shape_atlas"]["minimum_R_lower"]))
    upper = Decimal(str(tube["transverse_shape_atlas"]["maximum_R_upper"]))
    return {
        "schema_version": "1.0",
        "result_id": "K287-ORDER-SEVEN-TENSOR-JACOBI-REMAINDER",
        "created": "2026-09-21",
        "classification": "INTERNAL_STRUCTURAL_ONLY",
        "direction": "observed_to_native",
        "fixed_control": {
            "tube_manifest": "lab/process/k284-order-seven-transverse-shape-atlas.json",
            "derivative_manifest": "lab/process/k286-order-seven-mixed-shape-derivative-bank.json",
            "transverse_shape_radius": str(radius),
            "shape_coordinate_count": 6,
            "jacobi_alpha": "0",
            "jacobi_beta": "0",
            "nodes_per_axis": 2,
            "tensor_node_count": 64,
        },
        "rule": {
            "name": "two-node Gauss-Jacobi with alpha=beta=0 (Gauss-Legendre special case)",
            "normalized_one_dimensional_average_remainder": "h^4 sup|d^4 f/deta_i^4| / 270",
            "six_axis_positive_tensor_telescope": "sum the six one-axis errors because every remaining integral and quadrature operator is positive with norm one",
            "determinant_preserving": True,
            "common_chart": "K284 complete center-preconditioned determinant ratio",
        },
        "remainder": {
            "global_componentwise_fourth_derivative_abs_upper": str(fourth),
            "one_axis_normalized_average_abs_upper": str(one_axis),
            "six_axis_normalized_tube_average_abs_upper": str(tensor),
            "tube_regularizer_lower": str(lower),
            "tube_regularizer_upper": str(upper),
            "remainder_to_positive_lower_ratio_upper": str(tensor / lower),
            "numerically_resolving_on_normalized_tube": tensor < lower * Decimal("1e-6"),
        },
        "measure_boundary": {
            "certified_measure": "normalized uniform product measure on each bounded K284 transverse shape box",
            "native_K179_occurrence_measure_serialized": False,
            "scale_radial_measure_serialized": False,
            "occurrence_weights_serialized": False,
            "decision": "The tensor rule is resolving for the normalized local tube proxy if the reported ratio is below 1e-6, but it is not a native action-column error until the K179 occurrence, scale, radial, and exterior-domain measures are composed.",
        },
        "decision": {
            "tensor_jacobi_remainder_serialized": True,
            "normalized_tube_proxy_resolved": tensor < lower * Decimal("1e-6"),
            "native_action_column_ready": False,
            "domain_widening_authorized": False,
            "next_exact_input": "compose the native K179 occurrence weights and scale/radial measure with this local tube rule, then bound the exterior arbitrary-gap domain before emitting an action-column interval",
        },
        "release_test": {
            "k286_fourth_derivative_bank_consumed": True,
            "determinant_preserving_tensor_jacobi_remainder_serialized": True,
            "normalized_uniform_tube_measure_only": True,
            "native_K179_occurrence_measure_serialized": False,
            "complete_arbitrary_gap_ratio_domain_covered": False,
            "complete_base_action_column_evaluated": False,
            "native_K152_interval_emitted": False,
        },
        "ledger_effect": bank["ledger_effect"],
        "physical_or_source_selection": False,
        "canon_paper_release_or_public_posture_move": False,
        "claim_ceiling": "Two-node tensor Gauss-Jacobi remainder for the normalized uniform six-dimensional K284 shape tube only; no native K179 occurrence or scale/radial measure, exterior arbitrary-gap domain, action-column value, residual, native K152 interval, physical state, source/ledger move, canon, paper or public claim.",
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--write", action="store_true")
    args = parser.parse_args()
    result = build()
    if args.write:
        OUTPUT.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(json.dumps(result["remainder"], indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
