#!/usr/bin/env python3
"""Independent replay and hostile controls for K307."""

from __future__ import annotations

import copy
import importlib.util
from pathlib import Path


MODULE = Path(__file__).with_name("k307_order_seven_two_radius_joint_chart.py")


def load_module():
    spec = importlib.util.spec_from_file_location("k307_probe_target", MODULE)
    if spec is None or spec.loader is None:
        raise RuntimeError("cannot load K307 module")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def main() -> int:
    module = load_module()
    payload = module.build()
    checks = [
        payload["joint_change_of_variables"]["jacobian"] == "dq=db/x",
        "x^3*b^11" in payload["joint_change_of_variables"]["density_identity"],
        payload["joint_origin"]["D4_simultaneous_degree"] == -4,
        payload["joint_origin"]["bordered_B5_simultaneous_degree"] == -5,
        payload["joint_origin"]["exact_cauchy_scaling_control"]["all_exact"],
        payload["joint_origin"]["two_radius_polar_exponent"] == 6,
        payload["joint_origin"]["absolute_integrability_margin"] == 7,
        payload["factorization_target"]["explicit_b_power"] == 18,
        payload["terminal_split_boundary"]["pointwise_terminal_bound_required"] is False,
        payload["decision"]["complete_numerical_norms_emitted"] is False,
        payload["decision"]["k294_gamma_join_released"] is False,
    ]
    if not all(checks):
        raise AssertionError("K307 independent replay failed")

    hostile = []
    mutations = (
        ("jacobian", lambda d: d["joint_change_of_variables"].__setitem__("jacobian", "dq=db")),
        ("x_power", lambda d: d["joint_change_of_variables"].__setitem__("density_identity", "x^4*b^11")),
        ("d4_degree", lambda d: d["joint_origin"].__setitem__("D4_simultaneous_degree", -3)),
        ("b5_degree", lambda d: d["joint_origin"].__setitem__("bordered_B5_simultaneous_degree", -4)),
        ("origin_claim", lambda d: d["decision"].__setitem__("joint_origin_absolutely_integrable", False)),
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
        raise AssertionError(f"K307 hostile controls escaped: {hostile}")
    print(f"K307 probe passed {len(checks)}/{len(checks)} checks and rejected {len(hostile)}/{len(mutations)} hostile mutations")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
