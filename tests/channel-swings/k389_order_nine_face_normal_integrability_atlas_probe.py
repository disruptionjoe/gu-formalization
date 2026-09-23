#!/usr/bin/env python3
"""Independent replay and hostile mutation probe for K389."""

from __future__ import annotations

import copy
import importlib.util
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
PRODUCER = ROOT / "tests/channel-swings/k389_order_nine_face_normal_integrability_atlas.py"
STORED = ROOT / "lab/process/k389-order-nine-face-normal-integrability-atlas.json"


spec = importlib.util.spec_from_file_location("k389_probe_target", PRODUCER)
if spec is None or spec.loader is None:
    raise RuntimeError("cannot load K389 producer")
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


def main() -> int:
    stored = json.loads(STORED.read_text())
    rebuilt = module.build()
    module.validate_payload(stored)
    all_zero = next((row for row in stored["face_normal_atlas"] if row["axis"] == "s1" and len(row["zeroed_axes"]) == 20), None)
    if all_zero is None:
        raise AssertionError("K389 all-zero control missing")
    checks = [
        stored == rebuilt,
        stored["fixed_control"]["descriptor_face_replays"] == 3_113_600,
        len(stored["hybrid_summary"]) == 20,
        all(row["all_faces_locally_integrable"] for row in stored["hybrid_summary"]),
        stored["atlas_summary"]["global_minimum_face_normal_power"] == 0,
        all_zero["maximum_value_first_second_singular_powers"] == [11, 12, 13],
        all_zero["minimum_second_derivative_face_normal_power"] == 8,
        not stored["face_normal_chart_contract"]["coalescence_cancellation_required_for_integrability"],
        stored["face_normal_chart_contract"]["coalescence_preconditioning_still_required_for_interval_contraction"],
        all(stored["release_test"].values()),
    ]
    if not all(checks):
        raise AssertionError("K389 independent control failed")

    mutations = [
        lambda p: p["fixed_control"].__setitem__("ordered_descriptors_per_face", 4479),
        lambda p: p["fixed_control"].__setitem__("reachable_face_instances", 694),
        lambda p: p["fixed_control"].__setitem__("descriptor_face_replays", 3_113_599),
        lambda p: p["face_normal_atlas"].pop(),
        lambda p: p["face_normal_atlas"][0].__setitem__("minimum_second_derivative_face_normal_power", -1),
        lambda p: p["face_normal_atlas"][0].__setitem__("locally_integrable", False),
        lambda p: p["atlas_summary"].__setitem__("global_minimum_face_normal_power", -1),
        lambda p: p["decision"].__setitem__("recursive_positive_interior_cover_complete", True),
        lambda p: p["decision"].__setitem__("analytic_radial_tails_complete", True),
        lambda p: p["decision"].__setitem__("complete_hybrid_integrals_emitted", True),
        lambda p: p["release_test"].__setitem__("complete_order_nine_remainder_not_overclaimed", False),
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
        raise AssertionError(f"K389 hostile rejection failed: {rejected}/{len(mutations)}")
    print(f"K389 probe passed {len(checks)}/{len(checks)} controls and rejected {rejected}/{len(mutations)} hostile mutations")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
