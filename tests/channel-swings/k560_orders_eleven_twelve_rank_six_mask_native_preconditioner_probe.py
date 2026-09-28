#!/usr/bin/env python3
"""Replay K560 and reject determinant-preconditioner mutations."""

from __future__ import annotations

import copy
import importlib.util
import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
PRODUCER = Path(__file__).with_name("k560_orders_eleven_twelve_rank_six_mask_native_preconditioner.py")
STORED = ROOT / "lab/process/k560-orders-eleven-twelve-rank-six-mask-native-preconditioner.json"


def load():
    spec = importlib.util.spec_from_file_location("k560_probe_target", PRODUCER)
    if spec is None or spec.loader is None:
        raise RuntimeError("cannot load K560 producer")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def main() -> int:
    module = load()
    stored = json.loads(STORED.read_text())
    rebuilt = module.build()
    checks = [
        rebuilt == stored,
        stored["fixed_control"]["combined_ordered_descriptors"] == 94752,
        stored["fixed_control"]["combined_reachable_face_instances"] == 2733,
        stored["fixed_control"]["logical_determinant_matrix_face_uses"] == 546846560,
        stored["fixed_control"]["unique_preconditioner_templates"] == 97,
        stored["fixed_control"]["unique_confluent_templates"] == 131,
        stored["template_summary"]["rank_histogram"] == {"1": 2, "2": 5, "3": 10, "4": 17, "5": 26, "6": 37},
        stored["template_summary"]["all_strong_duality_checks_pass"],
        stored["confluent_divided_difference_contract"]["maximum_row_divided_difference_order"] == 5,
        stored["confluent_divided_difference_contract"]["maximum_column_divided_difference_order"] == 5,
        stored["primitive_scaling_contract"]["raw_Bessel_evaluation_at_zero_used"] is False,
        not stored["decision"]["complete_face_normal_integrability_emitted"],
    ]
    mutations = [
        lambda p: p["fixed_control"].__setitem__("combined_ordered_descriptors", 94751),
        lambda p: p["fixed_control"].__setitem__("combined_reachable_face_instances", 2732),
        lambda p: p["fixed_control"].__setitem__("maximum_species_determinant_rank", 5),
        lambda p: p["preconditioner_templates"].pop(),
        lambda p: p["preconditioner_templates"][0].__setitem__("dual_sum", 7),
        lambda p: p["preconditioner_templates"][0]["row_scaling_powers"].__setitem__(0, 9),
        lambda p: p["release_test"].__setitem__("rank_six_templates_present", False),
        lambda p: p["release_test"].__setitem__("raw_zero_bessel_calls_absent", False),
        lambda p: p["decision"].__setitem__("complete_face_normal_integrability_emitted", True),
        lambda p: p["decision"].__setitem__("whole_domain_hybrid_majorants_emitted", True),
        lambda p: p["release_test"].__setitem__("native_K152_interval_not_emitted", False),
    ]
    rejected = 0
    for mutate in mutations:
        candidate = copy.deepcopy(stored)
        mutate(candidate)
        try:
            module.validate_payload(candidate)
        except AssertionError:
            rejected += 1
    if not all(checks) or rejected != len(mutations):
        raise AssertionError("K560 probe failed")
    print(f"K560 probe passed {sum(checks)}/{len(checks)} controls and rejected {rejected}/{len(mutations)} hostile mutations")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
