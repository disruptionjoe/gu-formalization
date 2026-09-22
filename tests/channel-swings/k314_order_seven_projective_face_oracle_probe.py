#!/usr/bin/env python3
"""Independent replay and hostile controls for K314."""

from __future__ import annotations

import copy
import importlib.util
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
MODULE = Path(__file__).with_name("k314_order_seven_projective_face_oracle.py")
MANIFEST = ROOT / "lab/process/k314-order-seven-projective-face-oracle.json"


def load_module():
    spec = importlib.util.spec_from_file_location("k314_probe_backend", MODULE)
    if spec is None or spec.loader is None:
        raise RuntimeError("cannot load K314 module")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def rejected(module, payload, mutate) -> bool:
    candidate = copy.deepcopy(payload)
    mutate(candidate)
    try:
        module.validate_payload(candidate)
    except AssertionError:
        return True
    return False


def main() -> int:
    module = load_module()
    expected = json.loads(MANIFEST.read_text())
    replay = module.build()
    if replay != expected:
        raise AssertionError("K314 deterministic replay failed")
    checks = {
        "six_faces": len(replay["one_gap_face_oracle"]) == 6,
        "gap_order": replay["fixed_control"]["projective_gap_order"] == list(module.GAPS),
        "no_gap_division": not replay["confluent_rule"]["gap_division_used"],
        "polynomial_retained": replay["confluent_rule"]["native_projective_polynomial_retained"],
        "finite_regularizers": replay["release_test"]["all_face_regularizer_bounds_finite_positive"],
        "contracting_slabs": replay["release_test"]["all_face_complete_bounds_contract"],
        "zero_exact_faces": replay["release_test"]["exact_face_bounds_zero"],
        "no_cutoff": not replay["release_test"]["positive_gap_floor_required"],
        "no_detached_cofactor": not replay["release_test"]["detached_cofactor_used"],
        "no_master_overclaim": not replay["decision"]["complete_y_master_constant_emitted"],
    }
    if not all(checks.values()):
        raise AssertionError(f"K314 independent checks failed: {checks}")
    mutations = [
        lambda x: x["fixed_control"].__setitem__("projective_gap_order", list(reversed(module.GAPS))),
        lambda x: x["one_gap_face_oracle"].pop(),
        lambda x: x["confluent_rule"].__setitem__("gap_division_used", True),
        lambda x: x["confluent_rule"].__setitem__("native_projective_polynomial_retained", False),
        lambda x: x["decision"].__setitem__("all_six_repeated_node_faces_have_finite_regularizer_bounds", False),
        lambda x: x["decision"].__setitem__("gap_cutoff_required", True),
        lambda x: x["decision"].__setitem__("complete_y_master_constant_emitted", True),
    ]
    hostile = [rejected(module, expected, mutation) for mutation in mutations]
    if not all(hostile):
        raise AssertionError(f"K314 hostile controls escaped: {hostile}")
    print(f"K314 probe passed {len(checks)}/{len(checks)} checks and rejected {len(hostile)}/{len(mutations)} hostile mutations")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
