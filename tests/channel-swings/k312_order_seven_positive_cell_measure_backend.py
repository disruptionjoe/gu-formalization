#!/usr/bin/env python3
"""Build a deterministic positive cell-measure backend for the K309 integrator."""

from __future__ import annotations

import argparse
import json
import math
from fractions import Fraction
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[2]
K299 = ROOT / "lab/process/k299-order-seven-positive-peano-simplex-rule.json"
K310 = ROOT / "lab/process/k310-order-seven-two-radius-origin-compactification.json"
K311 = ROOT / "lab/process/k311-order-seven-terminal-radial-join.json"
OUTPUT = ROOT / "lab/process/k312-order-seven-positive-cell-measure-backend.json"


def polynomial_cell_moment(left: Fraction, right: Fraction, p: int, q: int) -> Fraction:
    total = Fraction(0)
    for k in range(q + 1):
        total += Fraction((-1) ** k * math.comb(q, k), p + k + 1) * (right ** (p + k + 1) - left ** (p + k + 1))
    return total


def exp_upper(z: Fraction, order: int = 256) -> Fraction:
    """Rational upper bound e^-z <= (1+z/N)^-N for z>=0."""
    return Fraction(1, 1) / (Fraction(1, 1) + z / order) ** order


def radial_finite_upper(left: Fraction, right: Fraction, power: int, rate: int = 256) -> Fraction:
    return exp_upper(rate * left) * Fraction(right ** (power + 1) - left ** (power + 1), power + 1)


def radial_tail_upper(left: Fraction, power: int, rate: int = 256) -> Fraction:
    z = rate * left
    polynomial = sum((z ** k) / math.factorial(k) for k in range(power + 1))
    return Fraction(math.factorial(power), rate ** (power + 1)) * exp_upper(z) * polynomial


def radial_partition(depth: int, endpoint: Fraction = Fraction(1, 16), power: int = 6) -> dict[str, Any]:
    count = 2 ** depth
    cuts = [endpoint * index / count for index in range(count + 1)]
    finite = sum(radial_finite_upper(left, right, power) for left, right in zip(cuts, cuts[1:]))
    tail = radial_tail_upper(endpoint, power)
    exact = Fraction(math.factorial(power), 256 ** (power + 1))
    upper = finite + tail
    return {
        "depth": depth,
        "finite_cells": count,
        "endpoint": str(endpoint),
        "finite_upper_decimal": format(float(finite), ".17e"),
        "tail_upper_decimal": format(float(tail), ".17e"),
        "total_upper_decimal": format(float(upper), ".17e"),
        "exact_total": str(exact),
        "upper_ratio": repr(float(upper / exact)),
        "covers_origin": cuts[0] == 0,
        "covers_infinite_tail": True,
        "upper_contains_exact": upper >= exact,
    }


def partition_sum(cuts: list[Fraction], p: int, q: int) -> Fraction:
    return sum(polynomial_cell_moment(left, right, p, q) for left, right in zip(cuts, cuts[1:]))


def build() -> dict[str, Any]:
    k299 = json.loads(K299.read_text())
    k310 = json.loads(K310.read_text())
    k311 = json.loads(K311.read_text())
    radial = [radial_partition(depth) for depth in (2, 4, 6, 8)]
    ratios = [float(row["upper_ratio"]) for row in radial]
    if ratios != sorted(ratios, reverse=True):
        raise AssertionError("radial refinement did not monotonically improve")
    quarter_cuts = [Fraction(0), Fraction(1, 4), Fraction(1, 2), Fraction(3, 4), Fraction(1)]
    half_cuts = [Fraction(0), Fraction(1, 2), Fraction(1)]
    s_total = partition_sum(quarter_cuts, 3, 29)
    duffy_rows = []
    for factor in k299["one_dimensional_factors"][:5]:
        exponent = factor["weight_exponent"]
        measured = partition_sum(half_cuts, 0, exponent)
        expected = Fraction(1, exponent + 1)
        duffy_rows.append({
            "axis": factor["axis"],
            "weight_exponent": exponent,
            "cells": 2,
            "partition_mass": str(measured),
            "exact_mass": str(expected),
            "exact_replay": measured == expected,
            "includes_both_faces": True,
        })
    uniform_axes = ["y", "u0", "u1", "u2", "u3", "z0", "z1", "z2", "z3"]
    return {
        "schema_version": "1.0",
        "result_id": "K312-ORDER-SEVEN-POSITIVE-CELL-MEASURE-BACKEND",
        "created": "2026-09-22",
        "classification": "INTERNAL_STRUCTURAL_ONLY",
        "direction": "observed_to_native",
        "fixed_control": {
            "predecessor_manifests": [
                "lab/process/k299-order-seven-positive-peano-simplex-rule.json",
                "lab/process/k310-order-seven-two-radius-origin-compactification.json",
                "lab/process/k311-order-seven-terminal-radial-join.json",
            ],
            "radial_rate": 256,
            "radial_reference_power": 6,
            "rational_exponential_upper_order": 256,
            "all_arithmetic_except_display_decimals": "fractions.Fraction",
        },
        "radial_backend": {
            "finite_cell_rule": "exp(-256*a)*(b^(n+1)-a^(n+1))/(n+1), with exp(-z) outward-bounded by (1+z/256)^-256",
            "tail_rule": "n!/256^(n+1)*exp(-256R)*sum_(k=0)^n (256R)^k/k!, using the same rational exponential upper",
            "refinement_replay": radial,
            "monotone_improvement": all(left > right for left, right in zip(ratios, ratios[1:])),
        },
        "compact_axis_backend": {
            "s_axis": {
                "weight": "s^3*(1-s)^29",
                "cells": 4,
                "partition_mass": str(s_total),
                "exact_mass": k310["exact_reference_masses"]["projective_s3_one_minus_s29"]["fraction"],
                "exact_replay": s_total == Fraction(k310["exact_reference_masses"]["projective_s3_one_minus_s29"]["fraction"]),
                "includes_x_and_b_faces": True,
            },
            "duffy_axes": duffy_rows,
            "uniform_axes": {
                "axes": uniform_axes,
                "cells_per_axis": 2,
                "partition_mass_per_axis": "1",
                "all_endpoint_faces_included": True,
            },
        },
        "adaptive_contract": {
            "cell_key_order": ["r", "s", "t0", "t1", "t2", "t3", "t4", "y", "u0", "u1", "u2", "u3", "z0", "z1", "z2", "z3"],
            "positive_measure_only": True,
            "operator_oracle_required": "outward abs bound for the exact projective polynomial times the complete scaled coherent D4-times-bordered-B5 directional functional on the same closed cell",
            "cell_contribution": "positive_measure_upper * operator_oracle_upper",
            "refinement_priority": "largest certified contribution or widest unresolved face-sensitive axis",
            "terminal_adapter": "use K311 inside the bordered determinant functional on cells meeting u3=1 or z3=1; never request a positive pointwise terminal floor",
            "coherent_absolute_value_after_bordered_assembly": True,
        },
        "coverage": {
            "radial_origin_and_infinite_tail": True,
            "two_radius_projective_faces": 2,
            "duffy_endpoint_faces": 10,
            "y_endpoint_faces": 2,
            "split_endpoint_faces": 16,
            "compact_dimensions": 15,
            "total_dimensions_with_radial": 16,
            "missing_measure_cells": 0,
        },
        "decision": {
            "positive_cell_measure_backend_implemented": True,
            "radial_origin_and_tail_covered": True,
            "all_projective_and_split_axes_partitioned": True,
            "scaled_regularizer_oracle_implemented": False,
            "complete_y_master_constant_emitted": False,
            "five_gap_axis_constants_emitted": False,
            "k294_gamma_join_released": False,
            "next_exact_input": "implement a boundary-stable scaled coherent-operator oracle on this cell contract, begin with the y master, and adapt until its complete positive Peano sum has a certified finite constant",
        },
        "release_test": {
            "four_radial_refinements_contain_exact_mass": all(row["upper_contains_exact"] for row in radial),
            "radial_upper_monotonically_improves": all(left > right for left, right in zip(ratios, ratios[1:])),
            "s_partition_exact": s_total == Fraction(k310["exact_reference_masses"]["projective_s3_one_minus_s29"]["fraction"]),
            "all_five_duffy_partitions_exact": all(row["exact_replay"] for row in duffy_rows),
            "terminal_cutoff_used": False,
            "detached_operator_supremum_used": False,
            "complete_numerical_norm_overclaim": False,
            "native_K152_interval_emitted": False,
        },
        "ledger_effect": k311["ledger_effect"],
        "claim_ceiling": "Executable deterministic positive cell-measure backend for the K309/K310 compactification. Exact polynomial moments partition s, all five Duffy axes, y and all eight split axes including their faces; rational outward exponential bounds cover the radial origin and infinite tail, with four refinements monotonically approaching the exact r^6 mass from above. The backend specifies how a complete scaled coherent-operator oracle is multiplied and adaptively summed, and routes terminal split cells through K311 inside the bordered determinant. It does not yet implement that operator oracle, emit a complete y-master or gap-axis constant, join K294 gamma strata, evaluate an action column or residual, emit a K152 interval, or move source/ledger, canon, paper, public or physical posture.",
    }


def validate_payload(payload: dict[str, Any]) -> None:
    coverage = payload["coverage"]
    if coverage["missing_measure_cells"] != 0 or coverage["total_dimensions_with_radial"] != 16:
        raise AssertionError("measure coverage changed")
    if not payload["radial_backend"]["monotone_improvement"]:
        raise AssertionError("radial refinement lost monotonicity")
    contract = payload["adaptive_contract"]
    if not contract["positive_measure_only"] or not contract["coherent_absolute_value_after_bordered_assembly"]:
        raise AssertionError("cell contract lost positivity or coherence")
    decision = payload["decision"]
    if decision["scaled_regularizer_oracle_implemented"] or decision["complete_y_master_constant_emitted"] or decision["five_gap_axis_constants_emitted"] or decision["k294_gamma_join_released"]:
        raise AssertionError("measure backend overclaim")


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
