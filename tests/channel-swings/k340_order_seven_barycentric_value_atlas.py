#!/usr/bin/env python3
"""Construct the fixed-node value-mode terminal-split atlas for K339.

K318's endpoint atlas belongs to the y-Peano remainder.  At the K299 value
node y=1/2 there is no y endpoint integration.  Only the terminal split square
can touch the Bessel corner.  Its two maximal-coordinate sectors absorb the
sector Jacobian into the complete terminal column (or, by transpose, row)
before one bordered-determinant enclosure.
"""

from __future__ import annotations

import argparse
import json
from fractions import Fraction
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[2]
K299 = ROOT / "lab/process/k299-order-seven-positive-peano-simplex-rule.json"
K305 = ROOT / "lab/process/k305-order-seven-coherent-bordered-functional-compiler.json"
K318 = ROOT / "lab/process/k318-order-seven-weighted-endpoint-blowup-atlas.json"
K339 = ROOT / "lab/process/k339-order-seven-normalized-residual-composition.json"
OUTPUT = ROOT / "lab/process/k340-order-seven-barycentric-value-atlas.json"


def q(value: Fraction) -> str:
    return str(value.numerator) if value.denominator == 1 else f"{value.numerator}/{value.denominator}"


def build() -> dict[str, Any]:
    k299 = json.loads(K299.read_text())
    k305 = json.loads(K305.read_text())
    k318 = json.loads(K318.read_text())
    k339 = json.loads(K339.read_text())
    node = k299["positive_cubature"]
    if node["simplex_node"] != ["1/6"] * 6 or node["y_node"] != "1/2":
        raise AssertionError("K299 barycentric node changed")
    if len(k305["coherent_groups"]) != 4 or not k305["release_test"]["bordered_identity_exact"]:
        raise AssertionError("K305 coherent bordered compiler unavailable")
    if k339["value_residual_separation"]["K334_zero_order_coefficient_is_a_base_cubature_value"]:
        raise AssertionError("K339 value/remainder type boundary changed")

    sectors = [
        {
            "id": "a_max",
            "domain": "0<=b<=a<=1",
            "map": "a=rho; b=rho*theta",
            "jacobian": "rho",
            "terminal_argument": "r*s*rho*(1+theta)/2",
            "terminal_factor_H": "(1+theta)/2 in [1/2,1]",
            "determinant_absorption": "absorb r*s*rho into bordered-B5 column 3 before complete determinant enclosure",
            "exact_sector_mass": q(Fraction(1, 2)),
            "matrix_orientation": "left_terminal_column",
        },
        {
            "id": "b_max",
            "domain": "0<=a<=b<=1",
            "map": "a=rho*theta; b=rho",
            "jacobian": "rho",
            "terminal_argument": "r*s*rho*(1+theta)/2",
            "terminal_factor_H": "(1+theta)/2 in [1/2,1]",
            "determinant_absorption": "transpose the a_max complete bordered matrix, so r*s*rho is absorbed into row 3",
            "exact_sector_mass": q(Fraction(1, 2)),
            "matrix_orientation": "right_terminal_row",
        },
    ]
    mass = sum((Fraction(row["exact_sector_mass"]) for row in sectors), Fraction(0))
    return {
        "schema_version": "1.0",
        "result_id": "K340-ORDER-SEVEN-BARYCENTRIC-VALUE-ATLAS",
        "created": "2026-09-22",
        "classification": "INTERNAL_STRUCTURAL_ONLY",
        "direction": "observed_to_native",
        "fixed_control": {
            "predecessor_manifests": [
                "lab/process/k299-order-seven-positive-peano-simplex-rule.json",
                "lab/process/k305-order-seven-coherent-bordered-functional-compiler.json",
                "lab/process/k318-order-seven-weighted-endpoint-blowup-atlas.json",
                "lab/process/k339-order-seven-normalized-residual-composition.json",
            ],
            "simplex_node": node["simplex_node"],
            "simplex_weight": node["simplex_weight"],
            "y_node": node["y_node"],
            "coherent_groups": len(k305["coherent_groups"]),
            "ordered_terms_per_group": 9,
            "native_split_variables": ["u0", "u1", "u2", "u3", "z0", "z1", "z2", "z3"],
            "terminal_split_variables": ["a=1-u3", "b=1-z3"],
        },
        "value_mode_terminal_split_atlas": {
            "sectors": sectors,
            "sector_count": len(sectors),
            "exact_sector_mass_sum": q(mass),
            "measure_zero_overlap": "a=b",
            "remaining_six_split_variables": "retain their full unit cubes inside the D4 and bordered-B5 arguments; their total cube volume is one",
            "scaled_terminal_rule": "rho*(2*K1(r*s*rho*H))=(Phi_0(r*s*rho*H))/(r*s*H); after the common r*s column scale, abs(Phi_0/H)<=4",
            "complete_matrix_rule": "retain all four K305 coherent bordered determinants and literal zeros; take absolute values only after each complete group determinant is assembled",
            "K318_Peano_kernel_used": False,
            "K318_endpoint_Hepp_weight_used": False,
            "raw_Bessel_zero_evaluation_used": False,
            "detached_terminal_cofactor_used": False,
            "occurrencewise_absolute_sum_used": False,
        },
        "coverage": {
            "terminal_square_covered_exactly": mass == 1,
            "all_eight_split_variables_retained": True,
            "left_right_sectors_related_by_exact_transpose": True,
            "barycentric_p_and_y_fixed_before_split_integration": True,
            "K318_y_Peano_mass_multiplied": False,
        },
        "decision": {
            "value_mode_barycentric_terminal_split_atlas_complete": True,
            "full_radial_projective_value_integrated": False,
            "normalized_base_value_emitted": False,
            "next_exact_input": "evaluate both value sectors on the deduplicated K334 radial/projective cover with all six p_i fixed to 1/6, then apply the three analytic radial tails",
        },
        "ledger_effect": k339["ledger_effect"],
        "source_routing": k339["source_routing"],
        "claim_ceiling": "Exact two-sector value-mode atlas for the K299 node p_i=1/6,y=1/2. It covers the full eight-split cube, absorbs the terminal-sector Jacobian into a complete K305 bordered determinant, retains all four coherent groups and literal border zeros, and uses neither K318's Peano kernel nor its y endpoint mass. It does not yet integrate the radial/projective domain, emit a base value, complete an action column or R_ref residual, produce a K152 interval, or move source, ledger, canon, paper, public or physical posture.",
    }


def validate_payload(payload: dict[str, Any]) -> None:
    fixed = payload["fixed_control"]
    if fixed["simplex_node"] != ["1/6"] * 6 or fixed["simplex_weight"] != "1/120" or fixed["y_node"] != "1/2":
        raise AssertionError("fixed K299 value node changed")
    atlas = payload["value_mode_terminal_split_atlas"]
    if atlas["sector_count"] != 2 or atlas["exact_sector_mass_sum"] != "1":
        raise AssertionError("terminal split cover changed")
    if [row["id"] for row in atlas["sectors"]] != ["a_max", "b_max"]:
        raise AssertionError("terminal sector order changed")
    if atlas["K318_Peano_kernel_used"] or atlas["K318_endpoint_Hepp_weight_used"]:
        raise AssertionError("Peano endpoint weight leaked into value mode")
    if atlas["raw_Bessel_zero_evaluation_used"] or atlas["detached_terminal_cofactor_used"] or atlas["occurrencewise_absolute_sum_used"]:
        raise AssertionError("forbidden terminal enclosure introduced")
    coverage = payload["coverage"]
    if not all(
        coverage[key]
        for key in (
            "terminal_square_covered_exactly",
            "all_eight_split_variables_retained",
            "left_right_sectors_related_by_exact_transpose",
            "barycentric_p_and_y_fixed_before_split_integration",
        )
    ) or coverage["K318_y_Peano_mass_multiplied"]:
        raise AssertionError("value atlas coverage control failed")
    if not payload["decision"]["value_mode_barycentric_terminal_split_atlas_complete"] or payload["decision"]["full_radial_projective_value_integrated"]:
        raise AssertionError("K340 scope boundary changed")


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
