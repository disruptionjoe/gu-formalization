#!/usr/bin/env python3
"""Independent replay and hostile controls for K312."""

from __future__ import annotations

import copy
import importlib.util
from fractions import Fraction
from pathlib import Path


MODULE = Path(__file__).with_name("k312_order_seven_positive_cell_measure_backend.py")


def load_module():
    spec = importlib.util.spec_from_file_location("k312_probe_target", MODULE)
    if spec is None or spec.loader is None:
        raise RuntimeError("cannot load K312 module")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def main() -> int:
    module = load_module()
    payload = module.build()
    radial = payload["radial_backend"]["refinement_replay"]
    compact = payload["compact_axis_backend"]
    checks = [
        len(radial) == 4,
        all(row["covers_origin"] and row["covers_infinite_tail"] and row["upper_contains_exact"] for row in radial),
        all(float(left["upper_ratio"]) > float(right["upper_ratio"]) for left, right in zip(radial, radial[1:])),
        compact["s_axis"]["exact_replay"],
        all(row["exact_replay"] and row["includes_both_faces"] for row in compact["duffy_axes"]),
        compact["uniform_axes"]["axes"] == ["y", "u0", "u1", "u2", "u3", "z0", "z1", "z2", "z3"],
        payload["coverage"]["total_dimensions_with_radial"] == 16,
        payload["coverage"]["missing_measure_cells"] == 0,
        payload["adaptive_contract"]["coherent_absolute_value_after_bordered_assembly"],
        payload["decision"]["scaled_regularizer_oracle_implemented"] is False,
        payload["decision"]["complete_y_master_constant_emitted"] is False,
        payload["decision"]["k294_gamma_join_released"] is False,
        module.polynomial_cell_moment(Fraction(0), Fraction(1), 3, 29) == Fraction(compact["s_axis"]["exact_mass"]),
    ]
    if not all(checks):
        raise AssertionError("K312 independent replay failed")
    hostile = []
    mutations = (
        ("missing_cell", lambda d: d["coverage"].__setitem__("missing_measure_cells", 1)),
        ("dimension", lambda d: d["coverage"].__setitem__("total_dimensions_with_radial", 15)),
        ("monotonicity", lambda d: d["radial_backend"].__setitem__("monotone_improvement", False)),
        ("signed_measure", lambda d: d["adaptive_contract"].__setitem__("positive_measure_only", False)),
        ("early_absolute", lambda d: d["adaptive_contract"].__setitem__("coherent_absolute_value_after_bordered_assembly", False)),
        ("oracle_overclaim", lambda d: d["decision"].__setitem__("scaled_regularizer_oracle_implemented", True)),
        ("norm_overclaim", lambda d: d["decision"].__setitem__("complete_y_master_constant_emitted", True)),
        ("gap_overclaim", lambda d: d["decision"].__setitem__("five_gap_axis_constants_emitted", True)),
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
        raise AssertionError(f"K312 hostile controls escaped: {hostile}")
    print(f"K312 probe passed {len(checks)}/{len(checks)} checks and rejected {len(hostile)}/{len(mutations)} hostile mutations")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
