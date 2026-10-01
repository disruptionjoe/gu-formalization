#!/usr/bin/env python3
"""Hostile mutation probe for K744. Run with ``sage -python``."""
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
SCRIPT = ROOT / "tests/channel-swings/k744_sc_act_06_full_trace_hessian_rank.py"
CERT = ROOT / "lab/process/k744-sc-act-06-full-trace-hessian-rank.json"


def load_module():
    spec = importlib.util.spec_from_file_location("k744_probe_target", SCRIPT)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def set_path(value, path, replacement):
    cursor = value
    for key in path[:-1]: cursor = cursor[key]
    cursor[path[-1]] = replacement


MUTATIONS = [
    (("result_id",), "K744-BROKEN"), (("classification",), "COMPARATOR"),
    (("direction",), "native_to_observed"), (("status",), "unverified"),
    (("target_claim",), "SC-ACT-01"),
    (("pairing_horn", "pairing"), "OTHER"), (("pairing_horn", "grade_weights"), "UNEQUAL"),
    (("pairing_horn", "full_adjoint_invariant_comparator"), False),
    (("pairing_horn", "source_selected"), True),
    (("pairing_horn", "weyl_block_product_horn_settled"), True),
    (("pairing_horn", "positive_hilbert_norm"), True),
    (("exact_controls", "field_dimension"), 1), (("exact_controls", "relative_weight"), 2),
]
for index in (0, 1):
    MUTATIONS.extend([
        (("exact_controls", "cases", index, "case"), "wrong_case"),
        (("exact_controls", "cases", index, "response_rank"), 1),
        (("exact_controls", "cases", index, "hessian_rank"), 1),
        (("exact_controls", "cases", index, "combined_rank"), 1),
        (("exact_controls", "cases", index, "total_coupled_rank"), 1),
        (("exact_controls", "cases", index, "rank_gain_over_i1b"), 1),
        (("exact_controls", "cases", index, "bosonic_middle_cohomology_after_gauge"), 0),
        (("exact_controls", "cases", index, "pairing_independent_image_cap"), 1),
        (("exact_controls", "cases", index, "local_i1b_rank"), 1),
        (("exact_controls", "cases", index, "local_hessian_rank"), 1),
        (("exact_controls", "cases", index, "metric_rank_increment"), 1),
    ])
MUTATIONS.append((("source_and_ledger_effect",), "MOVED"))
assert len(MUTATIONS) == 36


def main() -> int:
    module = load_module(); packet = json.loads(CERT.read_text(encoding="utf-8")); module.validate(packet)
    rejected = 0
    for path, replacement in MUTATIONS:
        hostile = copy.deepcopy(packet); set_path(hostile, path, replacement)
        try: module.validate(hostile)
        except (AssertionError, KeyError): rejected += 1
    assert rejected == len(MUTATIONS)
    print(f"PASS controls=44 hostile_mutations_rejected={rejected}/{len(MUTATIONS)}")
    return 0


if __name__ == "__main__": raise SystemExit(main())
