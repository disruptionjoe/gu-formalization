#!/usr/bin/env python3
"""Independent replay and hostile controls for K320."""

from __future__ import annotations

import copy
import importlib.util
from pathlib import Path


MODULE = Path(__file__).with_name("k320_order_seven_scaled_endpoint_bessel_bank.py")


def load_module():
    spec = importlib.util.spec_from_file_location("k320_backend", MODULE)
    if spec is None or spec.loader is None:
        raise RuntimeError("cannot load K320 module")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def main() -> int:
    module = load_module()
    payload = module.build()
    module.validate_payload(payload)
    checks = {
        "limits": payload["scaled_bessel_bank"]["zero_limits"] == {"Phi_0": 2, "Phi_1": -2, "Phi_2": 4},
        "four_scales": len(payload["scaled_bessel_bank"]["positive_argument_arb_controls"]) == 4,
        "identities": payload["scaled_bessel_bank"]["every_identity_control_contains_zero"],
        "convergence": payload["scaled_bessel_bank"]["smallest_scale_within_one_mill"],
        "left_scaling": payload["determinant_scaling"]["left_column_scaling_exact"],
        "right_scaling": payload["determinant_scaling"]["right_row_column_scaling_exact"],
        "assembly": payload["determinant_scaling"]["complete_determinant_retained"],
        "all_histogram": payload["terminal_power_census"]["all_orders_exact"] == {"0": 378, "1": 162, "2": 18},
        "second_histogram": payload["terminal_power_census"]["second_family_orders_exact"] == {"0": 288, "1": 144, "2": 18},
        "powers": [row["remaining_endpoint_power"] for row in payload["terminal_power_census"]["rows"]] == [2, 1, 0],
        "zero_safe": not payload["decision"]["raw_Bessel_evaluation_at_zero_required"],
        "no_release": not payload["decision"]["complete_y_master_constant_emitted"],
    }
    if not all(checks.values()):
        raise AssertionError(f"K320 independent checks failed: {checks}")

    mutations = []
    for mutate in (
        lambda p: p["scaled_bessel_bank"].__setitem__("zero_limits", {"Phi_0": 2, "Phi_1": -2, "Phi_2": 2}),
        lambda p: p["scaled_bessel_bank"].__setitem__("every_identity_control_contains_zero", False),
        lambda p: p["scaled_bessel_bank"].__setitem__("smallest_scale_within_one_mill", False),
        lambda p: p["determinant_scaling"].__setitem__("left_column_scaling_exact", False),
        lambda p: p["determinant_scaling"].__setitem__("right_row_column_scaling_exact", False),
        lambda p: p["determinant_scaling"].__setitem__("complete_determinant_retained", False),
        lambda p: p["determinant_scaling"].__setitem__("permutation_or_monomial_absolute_values_used", True),
        lambda p: p["terminal_power_census"].__setitem__("all_orders_exact", {"0": 377, "1": 162, "2": 18}),
        lambda p: p["terminal_power_census"].__setitem__("second_family_orders_exact", {"0": 288, "1": 143, "2": 18}),
        lambda p: p["terminal_power_census"].__setitem__("all_remaining_endpoint_powers_nonnegative", False),
        lambda p: p["decision"].__setitem__("raw_Bessel_evaluation_at_zero_required", True),
        lambda p: p["decision"].__setitem__("radial_projective_weighted_join_complete", True),
        lambda p: p["decision"].__setitem__("complete_y_master_constant_emitted", True),
        lambda p: p["decision"].__setitem__("five_gap_axis_transfer_released", True),
    ):
        candidate = copy.deepcopy(payload)
        mutate(candidate)
        try:
            module.validate_payload(candidate)
        except AssertionError:
            mutations.append(True)
        else:
            mutations.append(False)
    if not all(mutations):
        raise AssertionError(f"K320 hostile controls escaped: {mutations}")
    print(f"K320 probe passed {len(checks)}/{len(checks)} checks and rejected {len(mutations)}/{len(mutations)} hostile mutations")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
