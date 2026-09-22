#!/usr/bin/env python3
"""Compactify the K309 joint two-radius origin before interval enclosure."""

from __future__ import annotations

import argparse
import json
import math
from fractions import Fraction
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[2]
K307 = ROOT / "lab/process/k307-order-seven-two-radius-joint-chart.json"
K309 = ROOT / "lab/process/k309-order-seven-gap-axis-transfer-audit.json"
OUTPUT = ROOT / "lab/process/k310-order-seven-two-radius-origin-compactification.json"


def beta_integer(left: int, right: int) -> Fraction:
    """Integral_0^1 s^left (1-s)^right ds."""
    return Fraction(math.factorial(left) * math.factorial(right), math.factorial(left + right + 1))


def gamma_mass(power: int, rate: int) -> Fraction:
    """Integral_0^infinity exp(-rate*r) r^power dr."""
    return Fraction(math.factorial(power), rate ** (power + 1))


def build() -> dict[str, Any]:
    k307 = json.loads(K307.read_text())
    k309 = json.loads(K309.read_text())
    determinant_degree = -9
    vandermonde_degree = 18
    regularizer_degree = determinant_degree - vandermonde_degree
    radial_power = 3 + 29 + 1 + regularizer_degree
    radial = gamma_mass(radial_power, 256)
    projective = beta_integer(3, 29)
    combined = radial * projective
    if radial_power != k307["joint_origin"]["two_radius_polar_exponent"]:
        raise AssertionError("joint-origin exponent no longer matches K307")
    return {
        "schema_version": "1.0",
        "result_id": "K310-ORDER-SEVEN-TWO-RADIUS-ORIGIN-COMPACTIFICATION",
        "created": "2026-09-22",
        "classification": "INTERNAL_STRUCTURAL_ONLY",
        "direction": "observed_to_native",
        "fixed_control": {
            "predecessor_manifests": [
                "lab/process/k307-order-seven-two-radius-joint-chart.json",
                "lab/process/k309-order-seven-gap-axis-transfer-audit.json",
            ],
            "joint_radial_factor": k309["factorized_integrand"]["explicit_joint_radial_factor"],
            "determinant_product_simultaneous_degree": determinant_degree,
            "extracted_vandermonde_degree": vandermonde_degree,
            "regularized_product_simultaneous_degree": regularizer_degree,
        },
        "compactification": {
            "forward": {"r": "x+b", "s": "x/(x+b)"},
            "inverse": {"x": "r*s", "b": "r*(1-s)"},
            "domain": "r in [0,infinity), s in [0,1]",
            "jacobian": "dx db = r dr ds",
            "explicit_weight": "exp(-256*r)*r^33*s^3*(1-s)^29 dr ds",
            "scaled_regularizer": "H(r,s,angles)=r^27*R4*R5_border",
            "complete_scaled_weight": "exp(-256*r)*r^6*s^3*(1-s)^29*H(r,s,angles) dr ds",
            "origin_radial_power": radial_power,
            "origin_absolute_integrability_margin": radial_power + 1,
            "x_face_power": 3,
            "b_face_power": 29,
            "detached_q_integration_used": False,
        },
        "exact_reference_masses": {
            "radial_r6": {"fraction": str(radial), "decimal": repr(float(radial))},
            "projective_s3_one_minus_s29": {"fraction": str(projective), "decimal": repr(float(projective))},
            "product_before_angular_operator": {"fraction": str(combined), "decimal": repr(float(combined))},
        },
        "operator_contract": {
            "cell_oracle_input": "one closed r,s,Duffy,y,split cell",
            "cell_oracle_output": "an outward upper bound for abs(H) or the required scaled directional jet on that cell",
            "composition": "multiply the oracle bound by the positive exact/outward cell measure, then sum cells; take coherent-group absolute values only after bordered assembly",
            "origin_cell_requires_positive_argument_floor": False,
            "reason": "the r^27 scaling absorbs the complete determinant-product homogeneity before the origin is enclosed",
        },
        "decision": {
            "joint_origin_compactified": True,
            "origin_cell_measure_finite": True,
            "positive_argument_floor_required_at_origin": False,
            "terminal_join_composed": False,
            "complete_y_master_constant_emitted": False,
            "k294_gamma_join_released": False,
            "next_exact_input": "compose K302 terminal weighted jets with the compactified radial measure, then implement the positive cell-measure backend and its scaled-regularizer oracle contract",
        },
        "release_test": {
            "k307_margin_replayed": radial_power + 1 == 7,
            "regularizer_scaling_uses_extracted_b18": regularizer_degree == -27,
            "both_projective_radial_faces_integrable": 3 > -1 and 29 > -1,
            "fixed_x_q_extraction_reintroduced": False,
            "complete_numerical_norm_overclaim": False,
            "native_K152_interval_emitted": False,
        },
        "ledger_effect": k309["ledger_effect"],
        "claim_ceiling": "Exact radial blow-up of the K309 factored integrand. With r=x+b and s=x/(x+b), x^3*b^29*dx*db becomes r^33*s^3*(1-s)^29 dr ds. The extracted b^18 Vandermonde leaves the divided-difference product at simultaneous degree -27, so H=r^27*R4*R5_border and the complete origin weight is exp(-256r)*r^6*s^3*(1-s)^29. This gives an exact finite origin measure and a cell-oracle contract, not a complete operator supremum, y-master Peano constant, six-axis norm, K294 gamma join, action-column value, residual, K152 interval, source/ledger, canon, paper, public or physical claim.",
    }


def validate_payload(payload: dict[str, Any]) -> None:
    compact = payload["compactification"]
    if compact["origin_radial_power"] != 6 or compact["origin_absolute_integrability_margin"] != 7:
        raise AssertionError("origin exponent changed")
    if compact["scaled_regularizer"] != "H(r,s,angles)=r^27*R4*R5_border":
        raise AssertionError("regularizer scaling changed")
    if compact["detached_q_integration_used"]:
        raise AssertionError("detached q integration reintroduced")
    decision = payload["decision"]
    if decision["complete_y_master_constant_emitted"] or decision["k294_gamma_join_released"]:
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
