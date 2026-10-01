#!/usr/bin/env python3
"""Hostile mutation probe for K746."""
from __future__ import annotations

import copy
import importlib.util
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SCRIPT = ROOT / "tests/channel-swings/k746_sc_act_06_residual_square_full_symbol_obstruction.py"
CERT = ROOT / "lab/process/k746-sc-act-06-residual-square-full-symbol-obstruction.json"


def load_module():
    spec = importlib.util.spec_from_file_location("k746_probe_target", SCRIPT); assert spec and spec.loader
    module = importlib.util.module_from_spec(spec); sys.modules[spec.name] = module; spec.loader.exec_module(module); return module


def set_path(value, path, replacement):
    cursor = value
    for key in path[:-1]: cursor = cursor[key]
    cursor[path[-1]] = replacement


MUTATIONS = [
    (("result_id",), "K746-BROKEN"), (("classification",), "COMPARATOR"),
    (("direction",), "native_to_observed"), (("status",), "unverified"),
    (("target_claim",), "SC-ACT-01"),
    (("composition_theorem", "mixed_boson_fermion_principal_blocks_vanish"), False),
    (("composition_theorem", "displayed_fermion_candidate_is_exact"), False),
    (("composition_theorem", "middle_cohomology_is_direct_sum"), False),
    (("composition_theorem", "same_response_residual_pairing_can_repair_full_symbol"), True),
    (("composition_theorem", "source_global_SC_ACT_06_refuted"), True),
    (("exact_controls", "fermion_two_block_rank"), 1919),
]
for index in (0, 1):
    MUTATIONS.extend([
        (("exact_controls", "cases", index, "case"), "wrong_case"),
        (("exact_controls", "cases", index, "universal_bosonic_middle_cohomology_lower"), 0),
        (("exact_controls", "cases", index, "full_trace_bosonic_middle_cohomology"), 0),
        (("exact_controls", "cases", index, "fermion_middle_cohomology_dimension"), 1),
        (("exact_controls", "cases", index, "universal_full_symbol_middle_cohomology_lower"), 0),
        (("exact_controls", "cases", index, "full_trace_full_symbol_middle_cohomology"), 0),
        (("exact_controls", "cases", index, "full_symbol_exact"), True),
    ])
MUTATIONS.extend([
    (("decision", "k742_full_carrier_threshold_survivor_is_closed_for_same_response_residual_squares"), False),
    (("decision", "displayed_full_symbol_realization_is_elliptic"), True),
    (("decision", "different_action_owned_principal_response_or_background_remains_open"), False),
    (("source_and_ledger_effect",), "MOVED"),
])
assert len(MUTATIONS) == 29


def main() -> int:
    module = load_module(); packet = json.loads(CERT.read_text(encoding="utf-8")); module.validate(packet)
    rejected = 0
    for path, replacement in MUTATIONS:
        hostile = copy.deepcopy(packet); set_path(hostile, path, replacement)
        try: module.validate(hostile)
        except (AssertionError, KeyError): rejected += 1
    assert rejected == len(MUTATIONS)
    print(f"PASS controls=34 hostile_mutations_rejected={rejected}/{len(MUTATIONS)}")
    return 0


if __name__ == "__main__": raise SystemExit(main())
