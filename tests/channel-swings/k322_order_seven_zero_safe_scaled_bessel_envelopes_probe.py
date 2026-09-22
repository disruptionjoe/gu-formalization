#!/usr/bin/env python3
"""Independent replay and hostile controls for K322."""

from __future__ import annotations

import copy
import importlib.util
from fractions import Fraction
from pathlib import Path


MODULE = Path(__file__).with_name("k322_order_seven_zero_safe_scaled_bessel_envelopes.py")


def load_module():
    spec = importlib.util.spec_from_file_location("k322_backend", MODULE)
    if spec is None or spec.loader is None:
        raise RuntimeError("cannot load K322 module")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def main() -> int:
    module = load_module()
    payload = module.build()
    module.validate_payload(payload)
    rows = payload["analytic_envelope"]["rows"]
    checks = {
        "widths": [row["width"] for row in rows] == ["1/16", "1/4", "1", "4"],
        "zero_values": all(row["zero_values"] == [2, -2, 4] for row in rows),
        "formula_W1": module.exact_bounds(Fraction(1)) == [Fraction(2), Fraction(4), Fraction(8)],
        "controls": all(row["all_controls_inside"] for row in rows),
        "no_raw_zero": not payload["analytic_envelope"]["raw_Bessel_evaluation_at_zero_used"],
        "orders": payload["determinant_adapter"]["orders_covered"] == [0, 1, 2],
        "inside_determinant": payload["determinant_adapter"]["terminal_column_scaling_retained"],
        "no_detached": not payload["determinant_adapter"]["detached_terminal_budget_used"],
        "no_release": not payload["decision"]["complete_y_master_constant_emitted"],
    }
    if not all(checks.values()):
        raise AssertionError(f"K322 independent checks failed: {checks}")

    mutations = []
    for mutate in (
        lambda p: p["analytic_envelope"].__setitem__("raw_Bessel_evaluation_at_zero_used", True),
        lambda p: p["analytic_envelope"].__setitem__("continuous_zero_values_inserted_exactly", False),
        lambda p: p["analytic_envelope"]["rows"][0].__setitem__("all_controls_inside", False),
        lambda p: p["determinant_adapter"].__setitem__("orders_covered", [0, 1]),
        lambda p: p["determinant_adapter"].__setitem__("terminal_column_scaling_retained", False),
        lambda p: p["determinant_adapter"].__setitem__("detached_terminal_budget_used", True),
        lambda p: p["decision"].__setitem__("complete_chart_determinant_uppers_emitted", True),
        lambda p: p["decision"].__setitem__("complete_y_master_constant_emitted", True),
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
        raise AssertionError(f"K322 hostile controls escaped: {mutations}")
    print(f"K322 probe passed {len(checks)}/{len(checks)} checks and rejected {len(mutations)}/{len(mutations)} hostile mutations")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
