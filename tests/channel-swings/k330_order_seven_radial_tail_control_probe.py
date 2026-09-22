#!/usr/bin/env python3
"""Independent replay and hostile controls for K330."""

from __future__ import annotations

import copy
import importlib.util
import json
import math
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
MODULE = Path(__file__).with_name("k330_order_seven_radial_tail_control.py")
MANIFEST = ROOT / "lab/process/k330-order-seven-radial-tail-control.json"


def load_module():
    spec = importlib.util.spec_from_file_location("k330_probe_backend", MODULE)
    if spec is None or spec.loader is None:
        raise RuntimeError("cannot load K330 module")
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
        raise AssertionError("K330 deterministic replay failed")
    uppers = [float(value) for value in replay["exponential_tail"]["integrated_value_first_second_abs_uppers"]]
    checks = {
        "tail_start": replay["fixed_control"]["tail_start"] == "1",
        "s_cell": replay["fixed_control"]["projective_s_cell"] == ["1/4", "3/4"],
        "d4": replay["polynomial_growth_ledger"]["D4_normalized_determinant_power"] == 16,
        "b5": replay["polynomial_growth_ledger"]["bordered_B5_normalized_value_first_second_powers"] == [11, 12, 13],
        "complete": replay["polynomial_growth_ledger"]["complete_coefficient_value_first_second_powers"] == [29, 30, 31],
        "measure": replay["exponential_tail"]["tail_power_value_first_second"] == [35, 36, 37],
        "reference_radius": replay["polynomial_growth_ledger"]["reference_entry_audit"]["radial_cell"] == ["0", "1"] and replay["polynomial_growth_ledger"]["reference_entry_audit"]["terminal_normalized_entry_rule"] == "r*Phi_m with r<=1; continuous value zero at r=0",
        "finite": all(math.isfinite(value) and value > 0 for value in uppers),
        "infinite_tail": replay["exponential_tail"]["covers_infinite_radial_tail"],
        "annulus": replay["finite_radial_annulus"]["radial_interval"] == ["1/16", "1"],
        "joins": replay["finite_radial_annulus"]["joins_K329_at_one_sixteenth"] and replay["finite_radial_annulus"]["joins_tail_at_one"],
        "post_assembly": replay["assembly_contract"]["shared_normalized_entry_intervals_assembled_before_B5_coefficient_enclosure"],
        "analytic": replay["assembly_contract"]["tail_finiteness_is_analytic_not_sampled"],
        "interior_only": replay["scope_boundary"]["positive_projective_interior_only"],
        "tail": replay["decision"]["finite_exponential_radial_tail_control_implemented"],
        "half_line": replay["decision"]["positive_projective_interior_full_radial_half_line_complete"],
        "no_faces": not replay["decision"]["projective_faces_complete"],
        "no_master": not replay["decision"]["complete_y_master_constant_emitted"],
    }
    if not all(checks.values()):
        raise AssertionError(f"K330 independent checks failed: {checks}")
    mutators = (
        lambda p: p["fixed_control"].__setitem__("tail_start", "2"),
        lambda p: p["fixed_control"].__setitem__("projective_s_cell", ["0", "1"]),
        lambda p: p["polynomial_growth_ledger"].__setitem__("D4_normalized_determinant_power", 15),
        lambda p: p["polynomial_growth_ledger"].__setitem__("bordered_B5_normalized_value_first_second_powers", [11, 12]),
        lambda p: p["polynomial_growth_ledger"].__setitem__("complete_coefficient_value_first_second_powers", [28, 29, 30]),
        lambda p: p["exponential_tail"].__setitem__("tail_power_value_first_second", [34, 35, 36]),
        lambda p: p["polynomial_growth_ledger"]["reference_entry_audit"].__setitem__("radial_cell", ["0", "1/16"]),
        lambda p: p["polynomial_growth_ledger"]["reference_entry_audit"].__setitem__("terminal_normalized_entry_rule", "r*Phi_m with r<=1/16; continuous value zero at r=0"),
        lambda p: p["exponential_tail"].__setitem__("covers_infinite_radial_tail", False),
        lambda p: p["exponential_tail"].__setitem__("integrated_value_first_second_abs_uppers", ["1"]),
        lambda p: p["finite_radial_annulus"].__setitem__("radial_interval", ["1/8", "1"]),
        lambda p: p["finite_radial_annulus"].__setitem__("joins_K329_at_one_sixteenth", False),
        lambda p: p["finite_radial_annulus"].__setitem__("joins_tail_at_one", False),
        lambda p: p["finite_radial_annulus"].__setitem__("integrated_value_first_second_abs_uppers", ["1"]),
        lambda p: p["assembly_contract"].__setitem__("shared_normalized_entry_intervals_assembled_before_B5_coefficient_enclosure", False),
        lambda p: p["assembly_contract"].__setitem__("raw_Bessel_zero_call_used", True),
        lambda p: p["assembly_contract"].__setitem__("tail_finiteness_is_analytic_not_sampled", False),
        lambda p: p["scope_boundary"].__setitem__("positive_projective_interior_only", False),
        lambda p: p["decision"].__setitem__("finite_exponential_radial_tail_control_implemented", False),
        lambda p: p["decision"].__setitem__("finite_radial_annulus_control_implemented", False),
        lambda p: p["decision"].__setitem__("positive_projective_interior_full_radial_half_line_complete", False),
        lambda p: p["decision"].__setitem__("projective_faces_complete", True),
        lambda p: p["decision"].__setitem__("complete_y_master_constant_emitted", True),
    )
    hostile = [rejected(module, expected, mutate) for mutate in mutators]
    if not all(hostile):
        raise AssertionError(f"K330 hostile controls escaped: {hostile}")
    print(f"K330 probe passed {len(checks)}/{len(checks)} checks and rejected {len(hostile)}/{len(hostile)} hostile mutations")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
