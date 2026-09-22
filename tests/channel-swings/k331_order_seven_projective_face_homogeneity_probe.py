#!/usr/bin/env python3
"""Independent replay and hostile controls for K331."""

from __future__ import annotations

import copy
import importlib.util
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
MODULE = Path(__file__).with_name("k331_order_seven_projective_face_homogeneity.py")
MANIFEST = ROOT / "lab/process/k331-order-seven-projective-face-homogeneity.json"


def load_module():
    spec = importlib.util.spec_from_file_location("k331_probe_backend", MODULE)
    if spec is None or spec.loader is None:
        raise RuntimeError("cannot load K331 module")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def main() -> int:
    module = load_module()
    stored = json.loads(MANIFEST.read_text())
    replay = module.build()
    module.validate_payload(replay)
    if replay != stored:
        raise AssertionError("K331 deterministic replay failed")
    checks = {
        "d4_support": stored["fixed_control"]["D4_complete_permutation_count"] == 24,
        "b5_support": stored["fixed_control"]["bordered_B5_complete_nonzero_permutation_count"] == 54,
        "s0_margin": stored["s0_face"]["remaining_integrated_powers_value_first_second"] == [1, 1, 1],
        "s1_margin": stored["s1_face"]["remaining_integrated_powers_value_first_second"] == [26, 25, 24],
        "no_cutoff": not stored["composition_contract"]["projective_cutoff_required"],
        "no_raw_zero": not stored["composition_contract"]["raw_Bessel_evaluation_at_zero_allowed"],
        "complete_support": stored["support_census"]["complete_support_used_without_detached_cofactor"],
        "face_release": stored["decision"]["normalized_confluent_face_evaluator_released"],
    }
    if not all(checks.values()):
        raise AssertionError(f"K331 independent checks failed: {checks}")
    mutations = [
        lambda p: p["fixed_control"].__setitem__("D4_complete_permutation_count", 23),
        lambda p: p["fixed_control"].__setitem__("bordered_B5_complete_nonzero_permutation_count", 53),
        lambda p: p["s0_face"].__setitem__("remaining_integrated_powers_value_first_second", [-1, 1, 1]),
        lambda p: p["s1_face"].__setitem__("remaining_integrated_powers_value_first_second", [26, 25, -1]),
        lambda p: p["composition_contract"].__setitem__("projective_cutoff_required", True),
        lambda p: p["composition_contract"].__setitem__("raw_Bessel_evaluation_at_zero_allowed", True),
        lambda p: p["decision"].__setitem__("normalized_confluent_face_evaluator_released", False),
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
        raise AssertionError(f"K331 hostile controls rejected {rejected}/{len(mutations)}")
    print(f"K331 probe passed {len(checks)}/{len(checks)} checks and rejected {rejected}/{len(mutations)} hostile mutations")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
