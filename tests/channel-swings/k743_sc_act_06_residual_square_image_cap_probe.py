#!/usr/bin/env python3
"""Hostile mutation probe for K743. Run with ``sage -python``."""
from __future__ import annotations

import copy
import importlib.util
import json
import os
import sys
from pathlib import Path

try:
    import sage.all  # noqa: F401
except ModuleNotFoundError:
    os.execvp("sage", ["sage", "-python", *sys.argv])

ROOT = Path(__file__).resolve().parents[2]
SCRIPT = ROOT / "tests/channel-swings/k743_sc_act_06_residual_square_image_cap.py"
CERT = ROOT / "lab/process/k743-sc-act-06-residual-square-image-cap.json"


def load_module():
    spec = importlib.util.spec_from_file_location("k743_probe_target", SCRIPT)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def set_path(value, path, replacement):
    cursor = value
    for key in path[:-1]:
        cursor = cursor[key]
    cursor[path[-1]] = replacement


MUTATIONS = [
    (("result_id",), "K743-BROKEN"), (("classification",), "COMPARATOR"),
    (("direction",), "native_to_observed"), (("status",), "unverified"),
    (("target_claim",), "SC-ACT-01"),
    (("image_theorem", "hessian_form"), "H=J"),
    (("image_theorem", "universal_inclusion"), "FALSE"),
    (("image_theorem", "combined_inclusion"), "FALSE"),
    (("image_theorem", "pairing_selection_required_for_cap"), True),
    (("image_theorem", "relative_weight_required_for_cap"), True),
    (("image_theorem", "complete_invariant_block_enumeration"), False),
    (("exact_controls", "field_dimension"), 229385),
    (("exact_controls", "owned_metric_diffeomorphism_rank"), 5),
]
for index in (0, 1):
    MUTATIONS.extend([
        (("exact_controls", "cases", index, "case"), "wrong_case"),
        (("exact_controls", "cases", index, "distortion_i1b_euler_rank"), 1),
        (("exact_controls", "cases", index, "full_residual_response_rank"), 1),
        (("exact_controls", "cases", index, "distortion_universal_image_cap_rank"), 1),
        (("exact_controls", "cases", index, "total_coupled_image_cap_rank"), 1),
        (("exact_controls", "cases", index, "metric_rank_increment"), 1),
        (("exact_controls", "cases", index, "bosonic_middle_cohomology_lower_bound"), 0),
        (("exact_controls", "cases", index, "gauge_rank"), 5),
        (("exact_controls", "cases", index, "euler_times_gauge_rank"), 1),
        (("exact_controls", "cases", index, "redundancy_times_euler_rank"), 1),
        (("exact_controls", "cases", index, "local_label_count"), 1),
    ])
MUTATIONS.extend([
    (("decision", "every_same_response_residual_pairing_fails_middle_exactness"), False),
    (("decision", "full_carrier_rank_threshold_survival_reversed_by_exact_image_overlap"), False),
    (("decision", "unitary_pairing_fork_selected"), True),
    (("source_and_ledger_effect",), "MOVED"),
    (("exact_controls", "cases", 0, "block_types", 0, "multiplicity"), 0),
])
assert len(MUTATIONS) == 40


def main() -> int:
    module = load_module()
    packet = json.loads(CERT.read_text(encoding="utf-8"))
    module.validate(packet)
    rejected = 0
    for path, replacement in MUTATIONS:
        hostile = copy.deepcopy(packet)
        set_path(hostile, path, replacement)
        try:
            module.validate(hostile)
        except (AssertionError, KeyError):
            rejected += 1
    assert rejected == len(MUTATIONS)
    print(f"PASS controls=48 hostile_mutations_rejected={rejected}/{len(MUTATIONS)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
