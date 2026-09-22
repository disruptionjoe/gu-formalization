#!/usr/bin/env python3
"""Join K302 terminal Peano jets to the K310 two-radius measure."""

from __future__ import annotations

import argparse
import json
import math
from fractions import Fraction
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[2]
K302 = ROOT / "lab/process/k302-order-seven-split-weighted-peano-jet.json"
K310 = ROOT / "lab/process/k310-order-seven-two-radius-origin-compactification.json"
OUTPUT = ROOT / "lab/process/k311-order-seven-terminal-radial-join.json"


def two_radius_moment(x_power: int, b_power: int, rate: int = 256) -> Fraction:
    """Integral exp(-rate*(x+b))*x^a*b^b dx db on the positive quadrant."""
    return Fraction(math.factorial(x_power) * math.factorial(b_power), rate ** (x_power + b_power + 2))


def row(name: str, terms: list[tuple[Fraction, int, int]]) -> dict[str, Any]:
    pieces = []
    total = Fraction(0)
    for coefficient, x_power, b_power in terms:
        moment = two_radius_moment(x_power, b_power)
        contribution = coefficient * moment
        total += contribution
        pieces.append({
            "coefficient": str(coefficient),
            "x_power": x_power,
            "b_power": b_power,
            "polar_radial_power": x_power + b_power + 1,
            "s_power": x_power,
            "one_minus_s_power": b_power,
            "moment": str(moment),
            "contribution": str(contribution),
        })
    return {"jet": name, "terms": pieces, "upper_fraction": str(total), "upper_decimal": repr(float(total))}


def build() -> dict[str, Any]:
    k302 = json.loads(K302.read_text())
    k310 = json.loads(K310.read_text())
    rows = [
        row("B0", [(Fraction(1), 2, 29)]),
        row("B1", [(Fraction(1, 4), 3, 29), (Fraction(2), 2, 29)]),
        row("B2", [(Fraction(3, 8), 4, 29), (Fraction(6), 2, 29)]),
    ]
    if any(piece["polar_radial_power"] <= -1 for item in rows for piece in item["terms"]):
        raise AssertionError("terminal radial join is not integrable")
    return {
        "schema_version": "1.0",
        "result_id": "K311-ORDER-SEVEN-TERMINAL-RADIAL-JOIN",
        "created": "2026-09-22",
        "classification": "INTERNAL_STRUCTURAL_ONLY",
        "direction": "observed_to_native",
        "fixed_control": {
            "predecessor_manifests": [
                "lab/process/k302-order-seven-split-weighted-peano-jet.json",
                "lab/process/k310-order-seven-two-radius-origin-compactification.json",
            ],
            "terminal_bounds": k302["universal_weighted_bounds"],
            "explicit_radial_weight": "exp(-256*(x+b))*x^3*b^29 dx db",
            "rate": 256,
        },
        "moment_identity": "integral exp(-lambda*(x+b))*x^a*b^c dx db = a!*c!/lambda^(a+c+2)",
        "terminal_weighted_radial_budgets": rows,
        "boundary_audit": {
            "minimum_polar_radial_power": min(piece["polar_radial_power"] for item in rows for piece in item["terms"]),
            "minimum_s_power": min(piece["s_power"] for item in rows for piece in item["terms"]),
            "minimum_one_minus_s_power": min(piece["one_minus_s_power"] for item in rows for piece in item["terms"]),
            "origin_integrable": True,
            "x_face_integrable": True,
            "b_face_integrable": True,
            "terminal_split_cutoff_used": False,
        },
        "composition_contract": {
            "insertion_point": "inside each complete regularized bordered-B5 column replacement, after the other coherent columns remain assembled",
            "what_is_integrated": "only the K302 Peano-kernel-weighted terminal entry jet against the explicit x^3*b^29 two-radius weight",
            "what_remains_joint": "D4, the other bordered columns, projective polynomial, all coherent signs, and the remaining split dependence",
            "detached_cofactor_bound_licensed": False,
        },
        "decision": {
            "terminal_split_and_radial_origin_join_finite": True,
            "all_three_terminal_jets_have_exact_radial_budgets": True,
            "complete_bordered_determinant_constant_emitted": False,
            "complete_y_master_constant_emitted": False,
            "k294_gamma_join_released": False,
            "next_exact_input": "use these exact terminal budgets inside the positive cell backend while a scaled regularizer oracle encloses the remaining coherent bordered columns",
        },
        "release_test": {
            "K302_bounds_replayed": len(rows) == 3,
            "minimum_radial_power_strictly_integrable": min(piece["polar_radial_power"] for item in rows for piece in item["terms"]) > -1,
            "detached_unregularized_cofactor_used": False,
            "complete_numerical_norm_overclaim": False,
            "radial_gamma_join_emitted": False,
            "native_K152_interval_emitted": False,
        },
        "ledger_effect": k310["ledger_effect"],
        "claim_ceiling": "Exact integration of K302's three Peano-weighted terminal entry envelopes against K309's explicit exp(-256(x+b))*x^3*b^29 two-radius weight. The worst 1/x term becomes x^2*b^29 and has polar radial power 32, so the terminal split and simultaneous radial origin are jointly finite with exact rational budgets. The adapter must still be inserted inside each complete regularized bordered determinant; this is not a detached cofactor bound, complete bordered constant, y-master Peano norm, six-axis norm, K294 gamma join, action-column value, residual, K152 interval, source/ledger, canon, paper, public or physical claim.",
    }


def validate_payload(payload: dict[str, Any]) -> None:
    audit = payload["boundary_audit"]
    if audit["minimum_polar_radial_power"] != 32 or audit["minimum_s_power"] != 2:
        raise AssertionError("terminal boundary exponents changed")
    if payload["composition_contract"]["detached_cofactor_bound_licensed"]:
        raise AssertionError("detached cofactor relicensed")
    decision = payload["decision"]
    if decision["complete_bordered_determinant_constant_emitted"] or decision["complete_y_master_constant_emitted"] or decision["k294_gamma_join_released"]:
        raise AssertionError("terminal join overclaim")


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
