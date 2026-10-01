#!/usr/bin/env python3
"""Hostile mutation probe for K745."""
from __future__ import annotations

import copy
import importlib.util
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SCRIPT = ROOT / "tests/channel-swings/k745_sc_act_06_gauge_redundancy_obstruction.py"
CERT = ROOT / "lab/process/k745-sc-act-06-gauge-redundancy-obstruction.json"


def load_module():
    spec = importlib.util.spec_from_file_location("k745_probe_target", SCRIPT); assert spec and spec.loader
    module = importlib.util.module_from_spec(spec); sys.modules[spec.name] = module; spec.loader.exec_module(module); return module


def set_path(value, path, replacement):
    cursor = value
    for key in path[:-1]: cursor = cursor[key]
    cursor[path[-1]] = replacement


MUTATIONS = [
    (("result_id",), "K745-BROKEN"), (("classification",), "COMPARATOR"),
    (("direction",), "native_to_observed"), (("status",), "unverified"),
    (("target_claim",), "SC-ACT-01"), (("complex", "gauge_parameter_dimension"), 5),
    (("complex", "composition_zero"), False), (("complex", "independent_distortion_gauge_owned_at_T0"), True),
    (("complex", "distortion_radical_relabelled_as_gauge"), True), (("exact_controls", "field_dimension"), 1),
]
for index in (0, 1):
    MUTATIONS.extend([
        (("exact_controls", "cases", index, "case"), "wrong_case"),
        (("exact_controls", "cases", index, "gauge_rank"), 5),
        (("exact_controls", "cases", index, "distortion_gauge_columns_at_T0"), 1),
        (("exact_controls", "cases", index, "redundancy_rank"), 5),
        (("exact_controls", "cases", index, "i1b_euler_times_gauge_rank"), 1),
        (("exact_controls", "cases", index, "redundancy_times_i1b_euler_rank"), 1),
        (("exact_controls", "cases", index, "residual_hessian_times_gauge_rank"), 1),
        (("exact_controls", "cases", index, "universal_coupled_euler_rank_upper"), 1),
        (("exact_controls", "cases", index, "universal_middle_cohomology_lower"), 0),
        (("exact_controls", "cases", index, "full_trace_middle_cohomology"), 0),
    ])
MUTATIONS.append((("source_and_ledger_effect",), "MOVED"))
assert len(MUTATIONS) == 31


def main() -> int:
    module = load_module(); packet = json.loads(CERT.read_text(encoding="utf-8")); module.validate(packet)
    rejected = 0
    for path, replacement in MUTATIONS:
        hostile = copy.deepcopy(packet); set_path(hostile, path, replacement)
        try: module.validate(hostile)
        except (AssertionError, KeyError): rejected += 1
    assert rejected == len(MUTATIONS)
    print(f"PASS controls=38 hostile_mutations_rejected={rejected}/{len(MUTATIONS)}")
    return 0


if __name__ == "__main__": raise SystemExit(main())
