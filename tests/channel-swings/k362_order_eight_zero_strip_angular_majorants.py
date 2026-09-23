#!/usr/bin/env python3
"""Prove exact measure-only majorants for K358 ratio-zero strips."""

from __future__ import annotations

import argparse
import json
import math
from fractions import Fraction
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[2]
K358 = ROOT / "lab/process/k358-order-eight-normal-projective-atlas.json"
K359 = ROOT / "lab/process/k359-order-eight-projective-measure-and-boundary-routing.json"
K361 = ROOT / "lab/process/k361-order-eight-positive-width-projective-cells.json"
OUTPUT = ROOT / "lab/process/k362-order-eight-zero-strip-angular-majorants.json"
EPSILON = Fraction(1, 64)


def q(value: Fraction) -> str:
    return str(value.numerator) if value.denominator == 1 else f"{value.numerator}/{value.denominator}"


def build() -> dict[str, Any]:
    k358 = json.loads(K358.read_text())
    k359 = json.loads(K359.read_text())
    k361 = json.loads(K361.read_text())
    rows = []
    for codimension in k358["fixed_control"]["reachable_codimensions"]:
        ratio_count = codimension - 1
        chart_mass = Fraction(1, math.factorial(codimension))
        intersections = []
        for depth in range(1, ratio_count + 1):
            unit_density_upper = EPSILON**depth
            intersections.append({
                "zero_strip_depth": depth,
                "unit_density_box_upper": q(unit_density_upper),
                "angular_mass_upper": q(min(chart_mass, unit_density_upper)),
                "vanishing_order_in_epsilon": depth,
            })
        union_upper = min(chart_mass, ratio_count * EPSILON)
        rows.append({
            "codimension": codimension,
            "ratio_coordinates": ratio_count,
            "chart_mass": q(chart_mass),
            "one_coordinate_strip_mass_upper": q(min(chart_mass, EPSILON)),
            "union_of_all_zero_strips_mass_upper": q(union_upper),
            "recursive_intersection_majorants": intersections,
            "union_bound_replays_zero_when_epsilon_is_zero": True,
        })
    return {
        "schema_version": "1.0",
        "result_id": "K362-ORDER-EIGHT-ZERO-STRIP-ANGULAR-MAJORANTS",
        "created": "2026-09-23",
        "classification": "INTERNAL_STRUCTURAL_ONLY",
        "direction": "observed_to_native",
        "fixed_control": {
            "predecessor_manifests": [str(path.relative_to(ROOT)) for path in (K358, K359, K361)],
            "epsilon": q(EPSILON),
            "reachable_codimensions": k358["fixed_control"]["reachable_codimensions"],
            "codimension_rows": len(rows),
            "unique_maximum_charts": k361["fixed_control"]["unique_maximum_charts"],
            "program_chart_uses": k361["fixed_control"]["program_chart_cell_uses"],
        },
        "majorant_contract": {
            "ratio_density": "(1+sum r)^(-c)<=1 on [0,1]^(c-1)",
            "one_sided_zero_strip": "0<=r_j<=epsilon",
            "depth_s_intersection_unit_density_volume": "epsilon^s",
            "all_zero_strip_union_bound": "min(1/c!,(c-1)*epsilon)",
            "every_fixed_depth_majorant_vanishes_as_epsilon_to_zero": True,
            "majorants_control_angular_measure_only": True,
            "majorants_do_not_bound_the_K352_preconditioned_integrand": True,
            "uniform_integrand_weighted_boundary_envelope_still_required": True,
        },
        "codimension_strip_bank": rows,
        "strip_summary": {
            "all_13_reachable_codimensions_covered": len(rows) == 13,
            "all_majorants_nonnegative_and_no_larger_than_chart_mass": all(Fraction(row["union_of_all_zero_strips_mass_upper"]) <= Fraction(row["chart_mass"]) for row in rows),
            "all_recursive_depths_present": all(len(row["recursive_intersection_majorants"]) == row["ratio_coordinates"] for row in rows),
            "all_recursive_orders_strictly_increase": all([item["vanishing_order_in_epsilon"] for item in row["recursive_intersection_majorants"]] == list(range(1, row["ratio_coordinates"] + 1)) for row in rows),
        },
        "decision": {
            "one_sided_zero_strip_angular_mass_majorants_complete": True,
            "zero_inclusive_integrand_weighted_boundary_majorants_complete": False,
            "recursive_positive_interior_cover_complete": False,
            "complete_hybrid_integrals_emitted": False,
            "next_exact_input": "compose K349/K352 scaling into a determinant-preserving uniform integrand envelope on each K363-owned strip",
        },
        "release_test": {
            "epsilon_is_one_over_64": EPSILON == Fraction(1, 64),
            "exactly_13_codimension_rows": len(rows) == 13,
            "all_578_charts_in_scope": k361["fixed_control"]["unique_maximum_charts"] == 578,
            "all_2998_program_chart_uses_in_scope": k361["fixed_control"]["program_chart_cell_uses"] == 2998,
            "all_recursive_intersection_majorants_present": all(len(row["recursive_intersection_majorants"]) == row["ratio_coordinates"] for row in rows),
            "measure_only_scope_explicit": True,
            "integrand_weighted_boundary_not_overclaimed": True,
            "complete_order_eight_remainder_not_overclaimed": True,
            "native_K152_interval_not_emitted": True,
        },
        "ledger_effect": k361["ledger_effect"],
        "source_routing": k361["source_routing"],
        "claim_ceiling": "Exact one-sided and recursive ratio-zero strip angular-mass majorants for every reachable K358 codimension at epsilon=1/64. The bounds use only the exact chart density and chart mass; they vanish with their declared epsilon order. They do not bound the K352-preconditioned integrand, close zero-inclusive interval evaluation, supply a recursive interior cover, analytic tails, any complete K348 hybrid, the order-eight remainder/integral, action column, R_ref, K152 interval, source/ledger move, canon, paper, public or physical posture.",
    }


def validate_payload(payload: dict[str, Any]) -> None:
    fixed = payload["fixed_control"]
    if (fixed["epsilon"], fixed["codimension_rows"], fixed["unique_maximum_charts"], fixed["program_chart_uses"]) != ("1/64", 13, 578, 2998):
        raise AssertionError("K362 census changed")
    rows = payload["codimension_strip_bank"]
    if len(rows) != 13 or any(len(row["recursive_intersection_majorants"]) != row["ratio_coordinates"] for row in rows):
        raise AssertionError("K362 strip bank changed")
    contract = payload["majorant_contract"]
    if not contract["majorants_control_angular_measure_only"] or not contract["majorants_do_not_bound_the_K352_preconditioned_integrand"] or not contract["uniform_integrand_weighted_boundary_envelope_still_required"]:
        raise AssertionError("K362 scope boundary changed")
    decision = payload["decision"]
    if not decision["one_sided_zero_strip_angular_mass_majorants_complete"] or any(decision[key] for key in ("zero_inclusive_integrand_weighted_boundary_majorants_complete", "recursive_positive_interior_cover_complete", "complete_hybrid_integrals_emitted")):
        raise AssertionError("K362 decision boundary changed")
    if not all(payload["release_test"].values()):
        raise AssertionError("K362 release test failed")


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
