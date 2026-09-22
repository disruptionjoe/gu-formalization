#!/usr/bin/env python3
"""Independent replay and hostile controls for K299."""

from __future__ import annotations

import copy
import json
from fractions import Fraction
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
MANIFEST = ROOT / "lab/process/k299-order-seven-positive-peano-simplex-rule.json"


def frac(value: str) -> Fraction:
    return Fraction(value)


def errors(data: dict) -> list[str]:
    out = []
    factors = data.get("one_dimensional_factors", [])
    if [row.get("axis") for row in factors] != ["t0", "t1", "t2", "t3", "t4", "y"]:
        out.append("axis order")
    if data.get("fixed_control", {}).get("gap_order") != ["r0", "r1", "r2", "c0", "c1", "c2"]:
        out.append("gap order")
    if data.get("positive_cubature", {}).get("simplex_node") != ["1/6"] * 6:
        out.append("barycenter")
    if data.get("positive_cubature", {}).get("angular_weight") != "1/120":
        out.append("weight")
    if data.get("positive_cubature", {}).get("y_node") != "1/2":
        out.append("y node")
    if data.get("peano_remainder", {}).get("maximum_derivative_order") != 2:
        out.append("derivative order")
    if data.get("peano_remainder", {}).get("mixed_derivatives_required") is not False:
        out.append("mixed derivative")
    expected_n = [5, 4, 3, 2, 1, 1]
    for row, n in zip(factors, expected_n):
        expected = Fraction(1, 2 * (n + 1) ** 2 * (n + 2))
        if frac(row.get("peano_kernel", {}).get("integral", "0")) != expected:
            out.append(f"kernel mass {row.get('axis')}")
        if row.get("peano_kernel", {}).get("nonnegative") is not True:
            out.append(f"kernel sign {row.get('axis')}")
    controls = data.get("controls", {})
    if frac(controls.get("sum_p_squared_integral", "0")) - frac(controls.get("sum_p_squared_rule_value", "0")) != Fraction(1, 1008):
        out.append("simplex quadratic")
    if frac(controls.get("y_squared_times_simplex_integral", "0")) - frac(controls.get("y_squared_rule_value", "0")) != Fraction(1, 1440):
        out.append("y quadratic")
    decision = data.get("decision", {})
    if decision.get("complete_global_derivative_norm_computed") is not False or decision.get("radial_gamma_composition_released") is not False:
        out.append("claim ceiling")
    return out


def main() -> int:
    data = json.loads(MANIFEST.read_text())
    checks = 10
    assert not errors(data), errors(data)
    mutations = []
    for mutate in (
        lambda d: d["fixed_control"].update(gap_order=["c2", "c1", "c0", "r2", "r1", "r0"]),
        lambda d: d["positive_cubature"].update(simplex_node=["1/5"] * 6),
        lambda d: d["positive_cubature"].update(angular_weight="1/60"),
        lambda d: d["positive_cubature"].update(y_node="1/3"),
        lambda d: d["peano_remainder"].update(maximum_derivative_order=4),
        lambda d: d["peano_remainder"].update(mixed_derivatives_required=True),
        lambda d: d["one_dimensional_factors"][0]["peano_kernel"].update(integral="1/2"),
        lambda d: d["one_dimensional_factors"][4]["peano_kernel"].update(nonnegative=False),
        lambda d: d["decision"].update(complete_global_derivative_norm_computed=True),
        lambda d: d["decision"].update(radial_gamma_composition_released=True),
    ):
        changed = copy.deepcopy(data)
        mutate(changed)
        mutations.append(changed)
    rejected = sum(bool(errors(changed)) for changed in mutations)
    assert rejected == len(mutations), (rejected, len(mutations))
    print(f"k299_positive_peano_simplex_rule_probe: {checks}/{checks} checks pass; hostile {rejected}/{len(mutations)} rejected")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
