#!/usr/bin/env python3
"""Independent replay and hostile controls for K333."""

from __future__ import annotations

import copy
import importlib.util
import json
import math
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
MODULE = Path(__file__).with_name("k333_order_seven_projective_face_radial_closure.py")
MANIFEST = ROOT / "lab/process/k333-order-seven-projective-face-radial-closure.json"


def load_module():
    spec = importlib.util.spec_from_file_location("k333_probe_backend", MODULE)
    if spec is None or spec.loader is None:
        raise RuntimeError("cannot load K333 module")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def main() -> int:
    module = load_module()
    stored = json.loads(MANIFEST.read_text())
    replay = module.build()
    module.validate_payload(replay)
    if replay != stored:
        raise AssertionError("K333 deterministic replay failed")
    faces = stored["face_radial_closure"]
    checks = {
        "two_faces": [row["face"] for row in faces] == ["s0", "s1"],
        "radial_partition": stored["fixed_control"]["radial_partition"] == [["0", "1/16"], ["1/16", "1"], ["1", "infinity"]],
        "projective_partition": stored["fixed_control"]["projective_partition"] == [["0", "1/4"], ["1/4", "3/4"], ["3/4", "1"]],
        "tail_powers": stored["fixed_control"]["tail_powers_value_first_second"] == [35, 36, 37],
        "six_face_tails": all(math.isfinite(float(value)) and float(value) > 0 for row in faces for value in row["tail_integrated_value_first_second_abs_uppers"]),
        "three_complete": all(math.isfinite(float(value)) and float(value) > 0 for value in stored["complete_projective_partition_value_first_second_abs_uppers"]),
        "analytic_tail": stored["growth_contract"]["tail_finiteness_is_analytic_not_sampled"],
        "closure": stored["decision"]["complete_three_cell_projective_partition_finite"],
    }
    if not all(checks.values()):
        raise AssertionError(f"K333 independent checks failed: {checks}")
    mutations = [
        lambda p: p["fixed_control"].__setitem__("radial_partition", [["0", "1"]]),
        lambda p: p["fixed_control"].__setitem__("projective_partition", [["1/4", "3/4"]]),
        lambda p: p["fixed_control"].__setitem__("tail_powers_value_first_second", [34, 35, 36]),
        lambda p: p["face_radial_closure"].__setitem__(0, copy.deepcopy(p["face_radial_closure"][1])),
        lambda p: p["growth_contract"].__setitem__("projective_preconditioners_are_radial_degree_zero", False),
        lambda p: p["growth_contract"].__setitem__("tail_finiteness_is_analytic_not_sampled", False),
        lambda p: p["decision"].__setitem__("both_projective_faces_full_radial_half_line_complete", False),
        lambda p: p["decision"].__setitem__("complete_three_cell_projective_partition_finite", False),
        lambda p: p["decision"].__setitem__("complete_y_master_constant_emitted", True),
    ]
    rejected = 0
    for mutate in mutations:
        hostile = copy.deepcopy(stored)
        mutate(hostile)
        try:
            module.validate_payload(hostile)
        except AssertionError:
            rejected += 1
    if rejected != len(mutations):
        raise AssertionError(f"K333 hostile controls rejected {rejected}/{len(mutations)}")
    print(f"K333 probe passed {len(checks)}/{len(checks)} checks and rejected {rejected}/{len(mutations)} hostile mutations")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
