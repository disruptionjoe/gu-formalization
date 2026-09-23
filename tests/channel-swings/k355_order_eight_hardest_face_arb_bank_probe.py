#!/usr/bin/env python3
"""Independent replay and hostile mutation probe for K355."""

from __future__ import annotations

import copy
import importlib.util
import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
PRODUCER = ROOT / "tests/channel-swings/k355_order_eight_hardest_face_arb_bank.py"
STORED = ROOT / "lab/process/k355-order-eight-hardest-face-arb-bank.json"

spec = importlib.util.spec_from_file_location("k355_probe_target", PRODUCER)
if spec is None or spec.loader is None:
    raise RuntimeError("cannot load K355 producer")
module = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = module
spec.loader.exec_module(module)


def main() -> int:
    stored = json.loads(STORED.read_text())
    rebuilt = module.build()
    module.validate_payload(stored)
    checks = [
        stored == rebuilt,
        len(stored["hardest_face_arb_controls"]) == 18,
        sum(len(row["controls"]) for row in stored["hardest_face_arb_controls"]) == 54,
        stored["fixed_control"]["ordered_descriptor_control_evaluations"] == 129_600,
        all(control["coherent_group_count"] == 23 for row in stored["hardest_face_arb_controls"] for control in row["controls"]),
        all(float(control["minimum_cumulative_argument_lower"]) > 0 for row in stored["hardest_face_arb_controls"] for control in row["controls"]),
        stored["execution_contract"]["all_23_coherent_groups_assembled_before_reported_enclosure"],
        stored["execution_contract"]["controls_are_not_face_intervals"],
        not stored["execution_contract"]["raw_Bessel_evaluation_at_zero_used"],
        all(stored["release_test"].values()),
    ]
    if not all(checks):
        raise AssertionError("K355 independent control failed")
    mutations = [
        lambda p: p["fixed_control"].__setitem__("complete_arb_controls", 53),
        lambda p: p["fixed_control"].__setitem__("ordered_descriptor_control_evaluations", 129_599),
        lambda p: p["hardest_face_arb_controls"].pop(),
        lambda p: p["hardest_face_arb_controls"][0]["controls"].pop(),
        lambda p: p["hardest_face_arb_controls"][0]["controls"][0].__setitem__("coherent_group_count", 22),
        lambda p: p["hardest_face_arb_controls"][0]["controls"][0].__setitem__("minimum_cumulative_argument_lower", "0"),
        lambda p: p["execution_contract"].__setitem__("raw_Bessel_evaluation_at_zero_used", True),
        lambda p: p["execution_contract"].__setitem__("controls_are_not_face_intervals", False),
        lambda p: p["decision"].__setitem__("all_517_faces_numerically_evaluated", True),
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
        raise AssertionError(f"K355 hostile rejection failed: {rejected}/{len(mutations)}")
    print(f"K355 probe passed {len(checks)}/{len(checks)} controls and rejected {rejected}/{len(mutations)} hostile mutations")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
