#!/usr/bin/env python3
"""Independent replay and hostile controls for K309."""

from __future__ import annotations

import copy
import importlib.util
from pathlib import Path


MODULE = Path(__file__).with_name("k309_order_seven_gap_axis_transfer_audit.py")


def load_module():
    spec = importlib.util.spec_from_file_location("k309_probe_target", MODULE)
    if spec is None or spec.loader is None:
        raise RuntimeError("cannot load K309 module")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def main() -> int:
    module = load_module()
    payload = module.build()
    checks = [
        payload["fixed_control"]["gap_axes"] == ["t0", "t1", "t2", "t3", "t4"],
        payload["fixed_control"]["one_gap_faces"] == 6,
        payload["fixed_control"]["codimension_two_faces"] == 15,
        payload["fixed_control"]["endpoint_classes"] == 3,
        payload["factorized_integrand"]["explicit_joint_radial_factor"] == "exp(-256*(x+b))*x^3*b^29",
        payload["factorized_integrand"]["exponential_is_projective_axis_independent"],
        payload["boundary_transfer"]["regularizers_extend_to_coalescent_faces"],
        payload["boundary_transfer"]["worst_projective_second_derivative_margin"] > 0,
        payload["boundary_transfer"]["worst_endpoint_second_derivative_margin"] > 0,
        payload["operator_inventory"]["complete_master_axes"] == 6,
        payload["decision"]["complete_six_axis_peano_norm_emitted"] is False,
        payload["decision"]["k294_gamma_join_released"] is False,
    ]
    if not all(checks):
        raise AssertionError("K309 independent replay failed")

    hostile = []
    mutations = (
        ("axes", lambda d: d["fixed_control"].__setitem__("gap_axes", ["t0", "t1"])),
        ("faces", lambda d: d["fixed_control"].__setitem__("one_gap_faces", 5)),
        ("extension", lambda d: d["boundary_transfer"].__setitem__("regularizers_extend_to_coalescent_faces", False)),
        ("zeros", lambda d: d["boundary_transfer"].__setitem__("explicit_zeros_retained", False)),
        ("transfer", lambda d: d["decision"].__setitem__("same_regularized_operator_architecture_valid_for_all_five_gap_axes", False)),
        ("norm_overclaim", lambda d: d["decision"].__setitem__("complete_six_axis_peano_norm_emitted", True)),
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
        raise AssertionError(f"K309 hostile controls escaped: {hostile}")
    print(f"K309 probe passed {len(checks)}/{len(checks)} checks and rejected {len(hostile)}/{len(mutations)} hostile mutations")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
