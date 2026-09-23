#!/usr/bin/env python3
"""Independent replay and hostile mutation probe for K388."""

from __future__ import annotations

import copy
import importlib.util
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
PRODUCER = ROOT / "tests/channel-swings/k388_order_nine_mask_native_preconditioner_compiler.py"
STORED = ROOT / "lab/process/k388-order-nine-mask-native-preconditioner-compiler.json"


spec = importlib.util.spec_from_file_location("k388_probe_target", PRODUCER)
if spec is None or spec.loader is None:
    raise RuntimeError("cannot load K388 producer")
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


def main() -> int:
    stored = json.loads(STORED.read_text())
    rebuilt = module.build()
    module.validate_payload(stored)
    checks = [
        stored == rebuilt,
        stored["fixed_control"]["determinant_matrix_face_uses_replayed"] == 12_320_960,
        stored["template_summary"]["rank_histogram"] == {"1": 2, "2": 5, "3": 10, "4": 17, "5": 26},
        stored["fixed_control"]["unique_confluent_templates"] == 75,
        stored["template_summary"]["all_strong_duality_checks_pass"],
        stored["template_summary"]["all_uses_reduce_to_finite_template_bank"],
        stored["determinant_scaling_contract"]["determinant_assembled_after_row_column_scaling"],
        not stored["determinant_scaling_contract"]["permutationwise_absolute_enclosure_used_for_numerical_value"],
        stored["primitive_scaling_contract"]["zero_limits"] == ["2", "2", "4"],
        not stored["primitive_scaling_contract"]["raw_Bessel_evaluation_at_zero_used"],
        all(stored["release_test"].values()),
    ]
    if not all(checks):
        raise AssertionError("K388 independent control failed")

    mutations = [
        lambda p: p["fixed_control"].__setitem__("ordered_descriptors", 4479),
        lambda p: p["fixed_control"].__setitem__("reachable_face_instances", 694),
        lambda p: p["preconditioner_templates"].pop(),
        lambda p: p["preconditioner_templates"][0].__setitem__("dual_sum", 99),
        lambda p: p["preconditioner_templates"][0]["row_scaling_powers"].__setitem__(0, 2),
        lambda p: p["preconditioner_templates"][1]["zero_entry_matrix"][0].__setitem__(0, 0),
        lambda p: p["confluent_divided_difference_contract"].__setitem__("template_count", 74),
        lambda p: p["decision"].__setitem__("complete_face_normal_integrability_emitted", True),
        lambda p: p["decision"].__setitem__("recursive_numerical_cover_complete", True),
        lambda p: p["release_test"].__setitem__("raw_zero_bessel_calls_absent", False),
        lambda p: p["release_test"].__setitem__("native_K152_interval_not_emitted", False),
        lambda p: p["release_test"].__setitem__("exactly_60_unique_templates", False),
    ]
    rejected = 0
    for mutate in mutations:
        candidate = copy.deepcopy(stored)
        mutate(candidate)
        try:
            module.validate_payload(candidate)
        except AssertionError:
            rejected += 1
    if rejected != len(mutations):
        raise AssertionError(f"K388 hostile rejection failed: {rejected}/{len(mutations)}")
    print(f"K388 probe passed {len(checks)}/{len(checks)} controls and rejected {rejected}/{len(mutations)} hostile mutations")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
