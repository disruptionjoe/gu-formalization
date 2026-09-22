#!/usr/bin/env python3
"""Independent replay and hostile controls for K332."""

from __future__ import annotations

import copy
import importlib.util
import json
import math
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
MODULE = Path(__file__).with_name("k332_order_seven_projective_face_evaluator.py")
MANIFEST = ROOT / "lab/process/k332-order-seven-projective-face-evaluator.json"


def load_module():
    spec = importlib.util.spec_from_file_location("k332_probe_backend", MODULE)
    if spec is None or spec.loader is None:
        raise RuntimeError("cannot load K332 module")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def main() -> int:
    module = load_module()
    stored = json.loads(MANIFEST.read_text())
    replay = module.build()
    module.validate_payload(replay)
    if replay != stored:
        raise AssertionError("K332 deterministic replay failed")
    faces = stored["projective_face_bank"]["faces"]
    checks = {
        "two_faces": [row["face"] for row in faces] == ["s0", "s1"],
        "s0_powers": faces[0]["reduced_projective_powers"] == [1, 1, 1],
        "s1_powers": faces[1]["reduced_projective_powers"] == [26, 25, 24],
        "six_finite": all(math.isfinite(float(value)) and float(value) > 0 for row in faces for value in row["origin_integrated_value_first_second_abs_uppers"]),
        "literal_zeros": all(row["B5_audit"]["literal_zero_slots"] == [[3, 4], [4, 3], [4, 4]] for row in faces),
        "post_assembly": stored["composition_contract"]["shared_entry_substitution_precedes_complete_determinant_enclosure"],
        "no_cutoff": not stored["composition_contract"]["projective_cutoff_used"],
        "no_raw_zero": not stored["composition_contract"]["raw_Bessel_evaluation_at_zero_used"],
    }
    if not all(checks.values()):
        raise AssertionError(f"K332 independent checks failed: {checks}")
    mutations = [
        lambda p: p["fixed_control"].__setitem__("radial_cell", ["1/16", "1"]),
        lambda p: p["fixed_control"].__setitem__("endpoint_chart_count", 15),
        lambda p: p["projective_face_bank"]["faces"].__setitem__(0, copy.deepcopy(p["projective_face_bank"]["faces"][1])),
        lambda p: p["projective_face_bank"]["faces"][0].__setitem__("reduced_projective_powers", [-1, 1, 1]),
        lambda p: p["composition_contract"].__setitem__("projective_cutoff_used", True),
        lambda p: p["composition_contract"].__setitem__("raw_Bessel_evaluation_at_zero_used", True),
        lambda p: p["composition_contract"].__setitem__("familywise_absolute_summation_used", True),
        lambda p: p["decision"].__setitem__("both_projective_origin_face_cells_bounded", False),
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
        raise AssertionError(f"K332 hostile controls rejected {rejected}/{len(mutations)}")
    print(f"K332 probe passed {len(checks)}/{len(checks)} checks and rejected {rejected}/{len(mutations)} hostile mutations")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
