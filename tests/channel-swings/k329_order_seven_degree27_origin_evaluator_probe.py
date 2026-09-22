#!/usr/bin/env python3
"""Independent replay and hostile controls for K329."""

from __future__ import annotations

import copy
import importlib.util
import json
import math
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
MODULE = Path(__file__).with_name("k329_order_seven_degree27_origin_evaluator.py")
MANIFEST = ROOT / "lab/process/k329-order-seven-degree27-origin-evaluator.json"


def load_module():
    spec = importlib.util.spec_from_file_location("k329_probe_backend", MODULE)
    if spec is None or spec.loader is None:
        raise RuntimeError("cannot load K329 module")
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
        raise AssertionError("K329 deterministic replay failed")
    uppers = [float(value) for value in replay["origin_measure"]["integrated_value_first_second_abs_uppers"]]
    checks = {
        "origin_cell": replay["fixed_control"]["radial_cell"] == ["0", "1/16"],
        "s_cell": replay["fixed_control"]["projective_s_cell"] == ["1/4", "3/4"],
        "six_gaps": len(replay["fixed_control"]["six_gap_cells"]) == 6,
        "sixteen_charts": replay["fixed_control"]["endpoint_chart_count"] == 16,
        "degree16": "total 16" in replay["normalized_entry_audit"]["D4_entry_radial_exponent"],
        "degree11": "totals 11" in replay["normalized_entry_audit"]["B5_entry_radial_exponent"],
        "no_zero_call": not replay["normalized_entry_audit"]["raw_Bessel_evaluation_at_zero_used"],
        "post_assembly": replay["degree_27_complete_determinant"]["shared_entry_interval_substitution_precedes_determinant_enclosure"],
        "finite": all(math.isfinite(value) and value > 0 for value in uppers),
        "covers_zero": replay["origin_measure"]["covers_r_zero"],
        "interior_only": replay["scope_boundary"]["positive_projective_interior_only"],
        "origin": replay["decision"]["continuous_degree27_origin_evaluator_implemented"],
        "no_faces": not replay["decision"]["projective_faces_complete"],
        "no_master": not replay["decision"]["complete_y_master_constant_emitted"],
    }
    if not all(checks.values()):
        raise AssertionError(f"K329 independent checks failed: {checks}")
    mutators = (
        lambda p: p["fixed_control"].__setitem__("radial_cell", ["1/100", "1/16"]),
        lambda p: p["fixed_control"].__setitem__("projective_s_cell", ["0", "1"]),
        lambda p: p["normalized_entry_audit"].__setitem__("raw_Bessel_evaluation_at_zero_used", True),
        lambda p: p["normalized_entry_audit"].__setitem__("literal_zero_slots", []),
        lambda p: p["degree_27_complete_determinant"].__setitem__("shared_entry_interval_substitution_precedes_determinant_enclosure", False),
        lambda p: p["degree_27_complete_determinant"].__setitem__("familywise_absolute_summation_used", True),
        lambda p: p["degree_27_complete_determinant"].__setitem__("permutationwise_absolute_summation_used_for_B5", True),
        lambda p: p["degree_27_complete_determinant"].__setitem__("sixteen_chart_normalized_value_first_second_abs_uppers", ["1"]),
        lambda p: p["origin_measure"].__setitem__("covers_r_zero", False),
        lambda p: p["origin_measure"].__setitem__("raw_zero_call_required", True),
        lambda p: p["scope_boundary"].__setitem__("positive_projective_interior_only", False),
        lambda p: p["decision"].__setitem__("continuous_degree27_origin_evaluator_implemented", False),
        lambda p: p["decision"].__setitem__("projective_faces_complete", True),
        lambda p: p["decision"].__setitem__("complete_y_master_constant_emitted", True),
    )
    hostile = [rejected(module, expected, mutate) for mutate in mutators]
    if not all(hostile):
        raise AssertionError(f"K329 hostile controls escaped: {hostile}")
    print(f"K329 probe passed {len(checks)}/{len(checks)} checks and rejected {len(hostile)}/{len(hostile)} hostile mutations")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
