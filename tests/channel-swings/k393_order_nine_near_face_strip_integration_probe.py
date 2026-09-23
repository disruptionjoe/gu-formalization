#!/usr/bin/env python3
"""Independent replay and hostile mutation probe for K393."""

from __future__ import annotations

import copy
import importlib.util
import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
PRODUCER = ROOT / "tests/channel-swings/k393_order_nine_near_face_strip_integration.py"
STORED = ROOT / "lab/process/k393-order-nine-near-face-strip-integration.json"

spec = importlib.util.spec_from_file_location("k393_probe_target", PRODUCER)
if spec is None or spec.loader is None:
    raise RuntimeError("cannot load K393 producer")
module = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = module
spec.loader.exec_module(module)


def main() -> int:
    stored = json.loads(STORED.read_text())
    rebuilt = module.build()
    module.validate_payload(stored)
    checks = [
        stored == rebuilt,
        len(stored["face_strip_bank"]) == 695,
        sum(len(row["cells"]) for row in stored["face_strip_bank"]) == 4865,
        stored["fixed_control"]["exact_partition_width"] == "3/4096",
        stored["strip_summary"]["global_minimum_K389_normal_power"] == 0,
        stored["strip_summary"]["hybrids_with_reachable_faces"] == 18,
        stored["strip_summary"]["hybrids_without_reachable_faces"] == ["v9", "v10"],
        stored["integration_contract"]["face_rows_overlap_and_are_not_summed_into_hybrid_integrals"],
        stored["integration_contract"]["equal_normal_strip_is_not_full_projective_normal_cone"],
        all(stored["release_test"].values()),
    ]
    if not all(checks):
        raise AssertionError("K393 independent control failed")
    mutations = [
        lambda p: p["fixed_control"].__setitem__("integrated_face_cells", 4864),
        lambda p: p["fixed_control"].__setitem__("exact_partition_width", "1/1024"),
        lambda p: p["face_strip_bank"].pop(),
        lambda p: p["face_strip_bank"][0]["cells"].pop(),
        lambda p: p["face_strip_bank"][0].__setitem__("K389_normal_power", -1),
        lambda p: p["integration_contract"].__setitem__("unit_projective_angular_density_only", False),
        lambda p: p["integration_contract"].__setitem__("face_rows_overlap_and_are_not_summed_into_hybrid_integrals", False),
        lambda p: p["decision"].__setitem__("full_projective_normal_cone_complete", True),
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
        raise AssertionError(f"K393 hostile rejection failed: {rejected}/{len(mutations)}")
    print(f"K393 probe passed {len(checks)}/{len(checks)} controls and rejected {rejected}/{len(mutations)} hostile mutations")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
