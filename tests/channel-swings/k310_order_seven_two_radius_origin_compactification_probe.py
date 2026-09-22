#!/usr/bin/env python3
"""Independent replay and hostile controls for K310."""

from __future__ import annotations

import copy
import importlib.util
import math
from fractions import Fraction
from pathlib import Path


MODULE = Path(__file__).with_name("k310_order_seven_two_radius_origin_compactification.py")


def load_module():
    spec = importlib.util.spec_from_file_location("k310_probe_target", MODULE)
    if spec is None or spec.loader is None:
        raise RuntimeError("cannot load K310 module")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def main() -> int:
    module = load_module()
    payload = module.build()
    masses = payload["exact_reference_masses"]
    checks = [
        payload["compactification"]["origin_radial_power"] == 6,
        payload["compactification"]["origin_absolute_integrability_margin"] == 7,
        payload["compactification"]["x_face_power"] == 3,
        payload["compactification"]["b_face_power"] == 29,
        Fraction(masses["radial_r6"]["fraction"]) == Fraction(math.factorial(6), 256**7),
        Fraction(masses["projective_s3_one_minus_s29"]["fraction"]) == Fraction(math.factorial(3)*math.factorial(29), math.factorial(33)),
        payload["operator_contract"]["origin_cell_requires_positive_argument_floor"] is False,
        payload["decision"]["complete_y_master_constant_emitted"] is False,
        payload["decision"]["k294_gamma_join_released"] is False,
    ]
    if not all(checks):
        raise AssertionError("K310 independent replay failed")
    hostile = []
    mutations = (
        ("radial_power", lambda d: d["compactification"].__setitem__("origin_radial_power", 5)),
        ("margin", lambda d: d["compactification"].__setitem__("origin_absolute_integrability_margin", 6)),
        ("scaling", lambda d: d["compactification"].__setitem__("scaled_regularizer", "r^9*R4*R5")),
        ("detach_q", lambda d: d["compactification"].__setitem__("detached_q_integration_used", True)),
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
        raise AssertionError(f"K310 hostile controls escaped: {hostile}")
    print(f"K310 probe passed {len(checks)}/{len(checks)} checks and rejected {len(hostile)}/{len(mutations)} hostile mutations")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
