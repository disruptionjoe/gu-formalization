#!/usr/bin/env python3
"""Independent controls and hostile mutations for K582."""

from __future__ import annotations

import argparse
import copy
import importlib.util
import json
from fractions import Fraction
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
SOLVER = Path(__file__).with_name("k582_k579_group_rank_adaptive_complete_uppers.py")
MANIFEST = ROOT / "lab/process/k582-k579-group-rank-adaptive-complete-uppers.json"


def load_solver():
    spec = importlib.util.spec_from_file_location("k582_probe_solver", SOLVER)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


K582 = load_solver()


def checks(payload: dict) -> list[tuple[str, bool]]:
    rows = payload.get("group_complete_upper_bank", [])
    fixed = payload.get("fixed_control", {})
    decision = payload.get("decision", {})
    theorem = payload.get("rank_adaptive_theorem", {})
    return [
        ("result id", payload.get("result_id") == "K582-K579-GROUP-RANK-ADAPTIVE-COMPLETE-UPPERS"),
        ("routing", payload.get("classification") == "INTERNAL_CONDITIONAL_MATHEMATICS" and payload.get("target_claim") == "NONE-NOT-A-KILL"),
        ("23 groups", len(rows) == 23 and fixed.get("groups") == 23),
        ("2400 descriptors", fixed.get("ordered_descriptors") == 2400),
        ("517 faces", fixed.get("face_programs") == 517),
        ("18 hybrids", fixed.get("hybrids_per_group") == 18 and all(len(row.get("hybrid_bank", [])) == 18 for row in rows)),
        ("second conservation", Fraction(fixed.get("group_second_sum_exact", "0")) == Fraction(fixed.get("complete_second_exact", "1"))),
        ("remainder monotonic", Fraction(fixed.get("new_group_raw_remainder_sum_exact", "1")) <= Fraction(fixed.get("old_K579_raw_remainder_exact", "0"))),
        ("no enlarged group", all(Fraction(row["normalized_complete_integral_abs_upper_exact"]) <= Fraction(row["K579_complete_upper_exact"]) for row in rows)),
        ("rank sets present", all(row.get("determinant_ranks_present") for row in rows)),
        ("transition bounded", all(Fraction(row["group_transition_constant_exact"]) <= Fraction(row["global_transition_constant_exact"]) for row in rows)),
        ("improvement count", decision.get("groups_strictly_improved_over_K579", -1) == sum(row.get("strictly_improves_K579") is True for row in rows)),
        ("unchanged count", decision.get("groups_unchanged_from_K579", -1) == sum(row.get("strictly_improves_K579") is False for row in rows)),
        ("target count", decision.get("K577_targets_met", -1) == sum(row.get("K577_target_met") is True for row in rows)),
        ("target disposition", decision.get("K577_targets_met", -1) + decision.get("K577_targets_failed", -1) == 23),
        ("owner cover", theorem.get("owner_cover_unchanged") is True),
        ("cross terms", theorem.get("cross_terms_retained") is True),
        ("complete uppers", decision.get("all_complete_noncompact_group_uppers_preserved") is True),
        ("no K152", decision.get("native_K152_interval_emitted") is False),
        ("no source move", payload.get("source_and_ledger_effect") == "none"),
    ]


def selftest(payload: dict) -> int:
    mutations = [
        ("drop group", lambda p: p["group_complete_upper_bank"].pop()),
        ("change census", lambda p: p["fixed_control"].__setitem__("ordered_descriptors", 2399)),
        ("break conservation", lambda p: p["fixed_control"].__setitem__("group_second_sum_exact", "0")),
        ("enlarge remainder", lambda p: p["fixed_control"].__setitem__("new_group_raw_remainder_sum_exact", str(Fraction(p["fixed_control"]["old_K579_raw_remainder_exact"]) + 1))),
        ("enlarge group", lambda p: p["group_complete_upper_bank"][0].__setitem__("normalized_complete_integral_abs_upper_exact", str(Fraction(p["group_complete_upper_bank"][0]["K579_complete_upper_exact"]) + 1))),
        ("erase ranks", lambda p: p["group_complete_upper_bank"][0].__setitem__("determinant_ranks_present", [])),
        ("inflate transition", lambda p: p["group_complete_upper_bank"][0].__setitem__("group_transition_constant_exact", str(Fraction(p["group_complete_upper_bank"][0]["global_transition_constant_exact"]) + 1))),
        ("fake improvement count", lambda p: p["decision"].__setitem__("groups_strictly_improved_over_K579", 23)),
        ("fake target count", lambda p: p["decision"].__setitem__("K577_targets_met", 23)),
        ("erase owner cover", lambda p: p["rank_adaptive_theorem"].__setitem__("owner_cover_unchanged", False)),
        ("erase cross terms", lambda p: p["rank_adaptive_theorem"].__setitem__("cross_terms_retained", False)),
        ("invent K152", lambda p: p["decision"].__setitem__("native_K152_interval_emitted", True)),
    ]
    caught = []
    for name, mutate in mutations:
        mutant = copy.deepcopy(payload)
        mutate(mutant)
        caught.append((name, not all(ok for _, ok in checks(mutant))))
    for name, ok in caught:
        print(f"[{'PASS' if ok else 'FAIL'}] hostile mutation {name}")
    print(f"K582 HOSTILE SELFTEST: {sum(ok for _, ok in caught)}/{len(caught)} caught")
    return 0 if all(ok for _, ok in caught) else 1


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--selftest", action="store_true")
    args = parser.parse_args()
    payload = json.loads(MANIFEST.read_text())
    rebuilt = K582.build()
    results = checks(payload)
    results.append(("deterministic rebuild", payload == rebuilt))
    for name, ok in results:
        print(f"[{'PASS' if ok else 'FAIL'}] {name}")
    print(f"K582 controls: {sum(ok for _, ok in results)}/{len(results)}")
    if not all(ok for _, ok in results):
        return 1
    return selftest(payload) if args.selftest else 0


if __name__ == "__main__":
    raise SystemExit(main())
