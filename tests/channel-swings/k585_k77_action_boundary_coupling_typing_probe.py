#!/usr/bin/env python3
"""Independent checks and hostile mutations for K585."""

from __future__ import annotations

import argparse
import copy
import importlib.util
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
SOLVER = Path(__file__).with_name("k585_k77_action_boundary_coupling_typing.py")
MANIFEST = ROOT / "lab/process/k585-k77-action-boundary-coupling-typing.json"


def load_solver():
    spec = importlib.util.spec_from_file_location("k585_probe_solver", SOLVER)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


K585 = load_solver()


def checks(payload):
    block = payload.get("actual_action_block", {})
    attempt = payload.get("typed_map_attempt", {})
    decision = payload.get("decision", {})
    return [
        ("result id", payload.get("result_id") == "K585-K77-ACTION-BOUNDARY-COUPLING-TYPING"),
        ("routing", payload.get("classification") == "BRIDGE_OR_SEMANTIC_BOUNDARY" and payload.get("target_claim") == "NONE-NOT-A-KILL"),
        ("shape", block.get("shape") == [1470, 91]),
        ("rank", block.get("rank") == 91),
        ("support", block.get("nonzero_entries") == 182 and block.get("column_support_set") == [2]),
        ("receiver grading", block.get("nonzero_receiver_rows") == 182 and block.get("all_live_receivers_are_grade_one") is True),
        ("grade dimensions", block.get("grade_one_receiver_dimension") == 196 and block.get("grade_two_receiver_dimension") == 1274),
        ("digest", str(block.get("sparse_content_digest", "")).startswith("sha256:") and len(block.get("sparse_content_digest", "")) == 71),
        ("KT base", attempt.get("kt_base_dimensions") == [21, 91, 70]),
        ("boundary rank", attempt.get("corrected_boundary_rank") == 512),
        ("source match only", attempt.get("actual_source_matches_middle_base_dimension") is True and attempt.get("actual_receiver_matches_degree_zero_base_dimension") is False),
        ("no direct arrow", attempt.get("actual_block_directly_types_as_K444_D1_or_D2") is False),
        ("no identity lift", attempt.get("tensor_with_identity_512_matches_D1") is False and attempt.get("tensor_with_identity_512_matches_D2") is False),
        ("dimension coincidence fenced", attempt.get("dimension_coincidence_1470_equals_21_times_70") is True and attempt.get("dimension_coincidence_is_typed_factorization") is False),
        ("missing owned maps", attempt.get("owner_authenticated_1470_to_70_reduction_present") is False and attempt.get("owner_authenticated_21_to_91_adjacent_block_present") is False),
        ("block reconstructed", decision.get("actual_action_block_reconstructed") is True),
        ("K444 not instantiated", decision.get("actual_action_block_instantiates_K444") is False),
        ("source not rejected", decision.get("source_action_rejected") is False),
        ("no ledger move", payload.get("source_and_ledger_context", {}).get("ledger_effect") == "none"),
    ]


def selftest(payload):
    mutations = [
        ("change shape", lambda p: p["actual_action_block"].__setitem__("shape", [70, 91])),
        ("drop rank", lambda p: p["actual_action_block"].__setitem__("rank", 70)),
        ("change support", lambda p: p["actual_action_block"].__setitem__("nonzero_entries", 181)),
        ("mistype receiver", lambda p: p["actual_action_block"].__setitem__("all_live_receivers_are_grade_one", False)),
        ("invent direct arrow", lambda p: p["typed_map_attempt"].__setitem__("actual_block_directly_types_as_K444_D1_or_D2", True)),
        ("invent lift", lambda p: p["typed_map_attempt"].__setitem__("tensor_with_identity_512_matches_D1", True)),
        ("promote coincidence", lambda p: p["typed_map_attempt"].__setitem__("dimension_coincidence_is_typed_factorization", True)),
        ("invent reduction", lambda p: p["typed_map_attempt"].__setitem__("owner_authenticated_1470_to_70_reduction_present", True)),
        ("claim K444", lambda p: p["decision"].__setitem__("actual_action_block_instantiates_K444", True)),
        ("reject source", lambda p: p["decision"].__setitem__("source_action_rejected", True)),
    ]
    caught = []
    for name, mutate in mutations:
        mutant = copy.deepcopy(payload)
        mutate(mutant)
        caught.append((name, not all(ok for _, ok in checks(mutant))))
    for name, ok in caught:
        print(f"[{'PASS' if ok else 'FAIL'}] hostile mutation {name}")
    print(f"K585 HOSTILE SELFTEST: {sum(ok for _, ok in caught)}/{len(caught)} caught")
    return 0 if all(ok for _, ok in caught) else 1


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--selftest", action="store_true")
    args = parser.parse_args()
    payload = json.loads(MANIFEST.read_text(encoding="utf-8"))
    results = checks(payload)
    results.append(("deterministic rebuild", payload == K585.build()))
    for name, ok in results:
        print(f"[{'PASS' if ok else 'FAIL'}] {name}")
    print(f"K585 controls: {sum(ok for _, ok in results)}/{len(results)}")
    if not all(ok for _, ok in results):
        return 1
    return selftest(payload) if args.selftest else 0


if __name__ == "__main__":
    raise SystemExit(main())
