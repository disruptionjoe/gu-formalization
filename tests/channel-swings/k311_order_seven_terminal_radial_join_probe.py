#!/usr/bin/env python3
"""Independent replay and hostile controls for K311."""

from __future__ import annotations

import copy
import importlib.util
import math
from fractions import Fraction
from pathlib import Path


MODULE = Path(__file__).with_name("k311_order_seven_terminal_radial_join.py")


def load_module():
    spec = importlib.util.spec_from_file_location("k311_probe_target", MODULE)
    if spec is None or spec.loader is None:
        raise RuntimeError("cannot load K311 module")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def main() -> int:
    module = load_module()
    payload = module.build()
    rows = {row["jet"]: row for row in payload["terminal_weighted_radial_budgets"]}
    m = module.two_radius_moment
    checks = [
        Fraction(rows["B0"]["upper_fraction"]) == m(2, 29),
        Fraction(rows["B1"]["upper_fraction"]) == Fraction(1, 4)*m(3, 29) + 2*m(2, 29),
        Fraction(rows["B2"]["upper_fraction"]) == Fraction(3, 8)*m(4, 29) + 6*m(2, 29),
        m(2, 29) == Fraction(math.factorial(2)*math.factorial(29), 256**33),
        payload["boundary_audit"]["minimum_polar_radial_power"] == 32,
        payload["boundary_audit"]["minimum_s_power"] == 2,
        payload["boundary_audit"]["minimum_one_minus_s_power"] == 29,
        payload["composition_contract"]["detached_cofactor_bound_licensed"] is False,
        payload["decision"]["complete_y_master_constant_emitted"] is False,
        payload["decision"]["k294_gamma_join_released"] is False,
    ]
    if not all(checks):
        raise AssertionError("K311 independent replay failed")
    hostile = []
    mutations = (
        ("radial_power", lambda d: d["boundary_audit"].__setitem__("minimum_polar_radial_power", -1)),
        ("s_power", lambda d: d["boundary_audit"].__setitem__("minimum_s_power", -1)),
        ("detach", lambda d: d["composition_contract"].__setitem__("detached_cofactor_bound_licensed", True)),
        ("bordered_overclaim", lambda d: d["decision"].__setitem__("complete_bordered_determinant_constant_emitted", True)),
        ("norm_overclaim", lambda d: d["decision"].__setitem__("complete_y_master_constant_emitted", True)),
        ("gamma_overclaim", lambda d: d["decision"].__setitem__("k294_gamma_join_released", True)),
    )
    for name, mutate in mutations:
        candidate = copy.deepcopy(payload)
        mutate(candidate)
        try:
            module.validate_payload(candidate)
        except AssertionError:
            hostile.append(name)
    if len(hostile) != len(mutations):
        raise AssertionError(f"K311 hostile controls escaped: {hostile}")
    print(f"K311 probe passed {len(checks)}/{len(checks)} checks and rejected {len(hostile)}/{len(mutations)} hostile mutations")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
