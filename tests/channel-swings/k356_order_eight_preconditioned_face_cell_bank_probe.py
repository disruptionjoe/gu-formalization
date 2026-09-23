#!/usr/bin/env python3
"""Independent stored-bank and selected-control probe for K356."""

from __future__ import annotations

import copy
import importlib.util
import json
import sys
from fractions import Fraction
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
PRODUCER = ROOT / "tests/channel-swings/k356_order_eight_preconditioned_face_cell_bank.py"
STORED = ROOT / "lab/process/k356-order-eight-preconditioned-face-cell-bank.json"

spec = importlib.util.spec_from_file_location("k356_probe_target", PRODUCER)
if spec is None or spec.loader is None:
    raise RuntimeError("cannot load K356 producer")
module = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = module
spec.loader.exec_module(module)


def main() -> int:
    stored = json.loads(STORED.read_text())
    module.validate_payload(stored)
    k352 = json.loads(module.K352.read_text())
    singular, confluent = module.template_maps(k352)
    selected = []
    seen = set()
    for row in stored["face_cell_bank"]:
        if row["axis"] not in seen:
            selected.append(row)
            seen.add(row["axis"])
    checks = [
        len(selected) == 16,
        len(stored["face_cell_bank"]) == 517,
        sum(len(row["cells"]) for row in stored["face_cell_bank"]) == 3619,
        stored["fixed_control"]["ordered_descriptor_cell_evaluations"] == 8_685_600,
        stored["bank_summary"]["all_34_singular_templates_executed"],
        stored["bank_summary"]["all_38_confluent_templates_executed"],
        all(row["intervals_overlap"] for row in stored["direct_overlap_controls"]),
        stored["execution_contract"]["equal_normal_chart_is_not_full_projective_normal_cone"],
        not stored["execution_contract"]["raw_Bessel_evaluation_at_zero_used"],
        all(stored["release_test"].values()),
    ]
    # Independently replay one narrow cell on each reachable hybrid.
    for row in selected:
        program = next(item for item in json.loads(module.K354.read_text())["face_programs"] if item["program_id"] == row["program_id"])
        left, right = (Fraction(value) for value in row["cells"][0]["normal_interval"])
        second, groups, _, _, _ = module.complete_second(program, module.interval(left, right), singular, confluent)
        checks.extend([second.is_finite(), len(groups) == 23])
    if not all(checks):
        raise AssertionError("K356 independent control failed")
    mutations = [
        lambda p: p["fixed_control"].__setitem__("reachable_face_programs", 516),
        lambda p: p["fixed_control"].__setitem__("complete_positive_width_cells", 3618),
        lambda p: p["face_cell_bank"].pop(),
        lambda p: p["face_cell_bank"][0]["cells"].pop(),
        lambda p: p["face_cell_bank"][0]["cells"][0].__setitem__("coherent_group_count", 22),
        lambda p: p["face_cell_bank"][0]["cells"][0].__setitem__("minimum_cumulative_argument_lower", "0"),
        lambda p: p["direct_overlap_controls"].pop(),
        lambda p: p["execution_contract"].__setitem__("raw_Bessel_evaluation_at_zero_used", True),
        lambda p: p["execution_contract"].__setitem__("equal_normal_chart_is_not_full_projective_normal_cone", False),
        lambda p: p["decision"].__setitem__("full_projective_normal_cone_complete", True),
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
        raise AssertionError(f"K356 hostile rejection failed: {rejected}/{len(mutations)}")
    print(f"K356 probe passed {len(checks)}/{len(checks)} controls and rejected {rejected}/{len(mutations)} hostile mutations")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
