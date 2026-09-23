#!/usr/bin/env python3
"""Independent replay and hostile mutation probe for K390."""

from __future__ import annotations

import copy
import importlib.util
import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
PRODUCER = ROOT / "tests/channel-swings/k390_order_nine_face_program_compiler.py"
STORED = ROOT / "lab/process/k390-order-nine-face-program-compiler.json"

spec = importlib.util.spec_from_file_location("k390_probe_target", PRODUCER)
if spec is None or spec.loader is None:
    raise RuntimeError("cannot load K390 producer")
module = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = module
spec.loader.exec_module(module)


def main() -> int:
    stored = json.loads(STORED.read_text())
    rebuilt = module.build()
    module.validate_payload(stored)
    checks = [
        stored == rebuilt,
        len(stored["face_programs"]) == 695,
        stored["fixed_control"]["descriptor_face_programs"] == 3_113_600,
        stored["fixed_control"]["determinant_matrix_face_programs"] == 12_320_960,
        len(stored["selected_boundary_or_interior_program_per_hybrid"]) == 20,
        [row["axis"] for row in stored["positive_interior_fallback_programs"]] == ["v9", "v10"],
        set(stored["program_summary"]["global_singular_template_histogram"]) == {f"S{i:02d}" for i in range(60)},
        set(stored["program_summary"]["global_confluent_template_histogram"]) == {f"C{i:02d}" for i in range(75)},
        stored["approach_chart_contract"]["complete_coherent_assembly_required"],
        not stored["approach_chart_contract"]["raw_Bessel_evaluation_at_zero_used"],
        all(stored["release_test"].values()),
    ]
    if not all(checks):
        raise AssertionError("K390 independent control failed")
    mutations = [
        lambda p: p["fixed_control"].__setitem__("reachable_face_instances", 694),
        lambda p: p["fixed_control"].__setitem__("descriptor_face_programs", 3_113_599),
        lambda p: p["fixed_control"].__setitem__("determinant_matrix_face_programs", 12_320_959),
        lambda p: p["face_programs"].pop(),
        lambda p: p["face_programs"][0].__setitem__("ordered_descriptor_programs", 4479),
        lambda p: p["face_programs"][0].__setitem__("minimum_second_derivative_face_normal_power", -1),
        lambda p: p["selected_boundary_or_interior_program_per_hybrid"].pop(),
        lambda p: p["positive_interior_fallback_programs"].pop(),
        lambda p: p["approach_chart_contract"].__setitem__("raw_Bessel_evaluation_at_zero_used", True),
        lambda p: p["decision"].__setitem__("recursive_positive_interior_cover_complete", True),
        lambda p: p["decision"].__setitem__("complete_hybrid_integrals_emitted", True),
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
    if rejected != len(mutations):
        raise AssertionError(f"K390 hostile rejection failed: {rejected}/{len(mutations)}")
    print(f"K390 probe passed {len(checks)}/{len(checks)} controls and rejected {rejected}/{len(mutations)} hostile mutations")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
