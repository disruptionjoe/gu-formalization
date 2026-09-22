#!/usr/bin/env python3
"""Independent replay and hostile controls for K328."""

from __future__ import annotations

import copy
import importlib.util
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
MODULE = Path(__file__).with_name("k328_order_seven_scaled_derivative_envelope_bank.py")
MANIFEST = ROOT / "lab/process/k328-order-seven-scaled-derivative-envelope-bank.json"


def load_module():
    spec = importlib.util.spec_from_file_location("k328_probe_backend", MODULE)
    if spec is None or spec.loader is None:
        raise RuntimeError("cannot load K328 module")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def rejected(module, payload, mutate) -> bool:
    candidate = copy.deepcopy(payload)
    mutate(candidate)
    try:
        module.validate_payload(candidate)
    except (AssertionError, ValueError):
        return True
    return False


def main() -> int:
    module = load_module()
    expected = json.loads(MANIFEST.read_text())
    replay = module.build()
    if replay != expected:
        raise AssertionError("K328 deterministic replay failed")
    checks = {
        "max_order": replay["fixed_control"]["maximum_derivative_order"] == 6,
        "four_widths": len(replay["analytic_envelope"]["rows"]) == 4,
        "seven_orders": all(len(row["Phi_abs_uppers"]) == 7 for row in replay["analytic_envelope"]["rows"]),
        "zero_limits": replay["analytic_envelope"]["continuous_zero_limits"][:3] == ["2", "2", "4"],
        "exact": replay["analytic_envelope"]["all_bounds_exact_rational"],
        "no_zero_call": not replay["analytic_envelope"]["raw_Bessel_evaluation_at_zero_used"],
        "controls": all(row["contained"] for row in replay["positive_argument_controls"]),
        "d4": replay["order_census"]["D4_maximum_mixed_derivative_order"] == 6,
        "b5": replay["order_census"]["bordered_B5_maximum_value_first_second_order"] == 6,
        "released": replay["decision"]["degree_27_origin_evaluator_released"],
        "no_master": not replay["decision"]["complete_y_master_constant_emitted"],
    }
    if not all(checks.values()):
        raise AssertionError(f"K328 independent checks failed: {checks}")
    mutators = (
        lambda p: p["fixed_control"].__setitem__("maximum_derivative_order", 5),
        lambda p: p["fixed_control"].__setitem__("widths", ["1"]),
        lambda p: p["analytic_envelope"].__setitem__("raw_Bessel_evaluation_at_zero_used", True),
        lambda p: p["analytic_envelope"].__setitem__("all_bounds_exact_rational", False),
        lambda p: p["analytic_envelope"]["rows"].pop(),
        lambda p: p["analytic_envelope"]["rows"][0].__setitem__("orders", [0, 1]),
        lambda p: p["analytic_envelope"]["rows"][0]["Phi_abs_uppers"].pop(),
        lambda p: p["analytic_envelope"].__setitem__("continuous_zero_limits", ["0", "2", "4"]),
        lambda p: p["positive_argument_controls"][0].__setitem__("contained", False),
        lambda p: p["order_census"].__setitem__("all_required_orders_covered", False),
        lambda p: p["decision"].__setitem__("complete_y_master_constant_emitted", True),
    )
    hostile = [rejected(module, expected, mutate) for mutate in mutators]
    if not all(hostile):
        raise AssertionError(f"K328 hostile controls escaped: {hostile}")
    print(f"K328 probe passed {len(checks)}/{len(checks)} checks and rejected {len(hostile)}/{len(hostile)} hostile mutations")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
