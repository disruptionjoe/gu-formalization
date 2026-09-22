#!/usr/bin/env python3
"""Independent replay and hostile controls for K313."""

from __future__ import annotations

import copy
import importlib.util
import math
from pathlib import Path


MODULE = Path(__file__).with_name("k313_order_seven_scaled_radial_shell_oracle.py")


def load_module():
    spec = importlib.util.spec_from_file_location("k313_probe_target", MODULE)
    if spec is None or spec.loader is None:
        raise RuntimeError("cannot load K313 module")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def main() -> int:
    module = load_module()
    payload = module.build()
    spines = payload["radial_spine_controls"]["rows"]
    shells = payload["dyadic_shell_oracle"]["rows"]
    checks = [
        len(spines) == 5,
        len(shells) == 4,
        all(len(row["scaled_y_jet_abs_upper"]) == 3 for row in [*spines, *shells]),
        all(math.isfinite(float(value)) and float(value) > 0 for row in [*spines, *shells] for value in row["scaled_y_jet_abs_upper"]),
        all(float(value) < 1.01 for value in payload["radial_spine_controls"]["last_to_first_component_ratios"]),
        all(float(value) < 1.01 for value in payload["dyadic_shell_oracle"]["last_to_first_component_ratios"]),
        all(row["multiplier"] == str(module.Fraction(row["radius_max"]) ** 27) for row in shells),
        payload["decision"]["scaled_interior_shell_oracle_implemented"],
        payload["decision"]["continuous_origin_oracle_implemented"] is False,
        payload["decision"]["projective_face_oracle_implemented"] is False,
        payload["decision"]["complete_y_master_constant_emitted"] is False,
        payload["decision"]["k294_gamma_join_released"] is False,
    ]
    if not all(checks):
        raise AssertionError("K313 independent replay failed")

    hostile = []
    mutations = (
        ("degree", lambda d: d["fixed_control"].__setitem__("scaled_regularizer_degree", 26)),
        ("spine", lambda d: d["radial_spine_controls"]["rows"].pop()),
        ("shell", lambda d: d["dyadic_shell_oracle"]["rows"].pop()),
        ("finite", lambda d: d["release_test"].__setitem__("all_scaled_bounds_finite_positive", False)),
        ("stability", lambda d: d["release_test"].__setitem__("shell_ratios_below_1_01", False)),
        ("origin_overclaim", lambda d: d["decision"].__setitem__("continuous_origin_oracle_implemented", True)),
        ("face_overclaim", lambda d: d["decision"].__setitem__("projective_face_oracle_implemented", True)),
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
        raise AssertionError(f"K313 hostile controls escaped: {hostile}")
    print(f"K313 probe passed {len(checks)}/{len(checks)} checks and rejected {len(hostile)}/{len(mutations)} hostile mutations")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
