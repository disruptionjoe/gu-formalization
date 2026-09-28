#!/usr/bin/env python3
"""Independent replay and hostile mutations for K603."""

from __future__ import annotations

import copy
import importlib.util
import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
HERE = Path(__file__).resolve().parent
MANIFEST = ROOT / "lab/process/k603-k500-all-order-signature-sparsity.json"


def load():
    spec = importlib.util.spec_from_file_location("k603_probe_target", HERE / "k603_k500_all_order_signature_sparsity.py")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def verify(payload):
    assert payload["result_id"] == "K603-K500-ALL-ORDER-SIGNATURE-SPARSITY"
    assert payload["target_claim"] == "NONE-NOT-A-KILL"
    theorem = payload["theorem"]
    assert theorem["surviving_pair_is_not_evaluated"] and theorem["coefficient_signs_and_within_block_determinants_remain_required"]
    rows = payload["seed_order_rows"]
    assert len(rows) == 33
    assert [(row["seed_impurity"], row["order"]) for row in rows] == [(seed, order) for order in range(2, 13) for seed in (0, 1, 2)]
    assert all(row["cyclic_action_pairs_total"] == row["cyclic_action_pairs_surviving"] + row["cyclic_action_exact_zero_pairs"] for row in rows)
    assert [row["cyclic_action_pairs_surviving"] for row in rows[:3]] == [2, 1, 1]
    orders = payload["order_summary"]
    assert [row["order"] for row in orders] == list(range(2, 13))
    census = payload["complete_census"]
    assert census["seed_order_blocks"] == 33
    assert census["cyclic_paths"] == 626 and census["action_terms"] == 2958
    assert census["cyclic_action_pairs_total"] == 131076
    assert census["cyclic_action_pairs_surviving"] == 21344
    assert census["cyclic_action_exact_zero_pairs"] == 109732
    assert census["all_2958_action_terms_retained"]
    decision = payload["decision"]
    assert decision["order_two_through_twelve_signature_sparsity_complete"]
    assert decision["exact_zero_cyclic_action_products_removed_before_quadrature"]
    assert not decision["surviving_higher_order_moments_numerically_evaluated"]
    assert not decision["complete_finite_K456_moments_emitted"]
    assert not decision["complete_K500_uniform_leakage_emitted"]
    assert not decision["native_noncyclic_floor_emitted"]
    assert not decision["K473_released"] and not decision["native_K152_interval_emitted"]
    assert payload["source_and_ledger_effect"] == "none"
    assert "removes only products forced to zero" in payload["claim_ceiling"]


def main() -> int:
    module = load()
    stored = json.loads(MANIFEST.read_text())
    replay = module.build()
    assert replay == stored
    checks = [
        stored["complete_census"]["action_terms"] == 2958,
        stored["complete_census"]["cyclic_paths"] == 626,
        stored["complete_census"]["cyclic_action_exact_zero_pairs"] == 109732,
        stored["decision"]["order_two_through_twelve_signature_sparsity_complete"],
        stored["theorem"]["surviving_pair_is_not_evaluated"],
    ]
    mutations = [
        ("result", lambda p: p.__setitem__("result_id", "wrong")),
        ("target", lambda p: p.__setitem__("target_claim", "SC-META-53")),
        ("evaluation", lambda p: p["theorem"].__setitem__("surviving_pair_is_not_evaluated", False)),
        ("signs", lambda p: p["theorem"].__setitem__("coefficient_signs_and_within_block_determinants_remain_required", False)),
        ("rows", lambda p: p.__setitem__("seed_order_rows", p["seed_order_rows"][:-1])),
        ("row partition", lambda p: p["seed_order_rows"][0].__setitem__("cyclic_action_exact_zero_pairs", 0)),
        ("order-two base", lambda p: p["seed_order_rows"][0].__setitem__("cyclic_action_pairs_surviving", 1)),
        ("orders", lambda p: p.__setitem__("order_summary", p["order_summary"][:-1])),
        ("blocks", lambda p: p["complete_census"].__setitem__("seed_order_blocks", 32)),
        ("cyclic", lambda p: p["complete_census"].__setitem__("cyclic_paths", 625)),
        ("terms", lambda p: p["complete_census"].__setitem__("action_terms", 2957)),
        ("total", lambda p: p["complete_census"].__setitem__("cyclic_action_pairs_total", 1)),
        ("surviving", lambda p: p["complete_census"].__setitem__("cyclic_action_pairs_surviving", 1)),
        ("zeros", lambda p: p["complete_census"].__setitem__("cyclic_action_exact_zero_pairs", 1)),
        ("retention", lambda p: p["complete_census"].__setitem__("all_2958_action_terms_retained", False)),
        ("complete", lambda p: p["decision"].__setitem__("order_two_through_twelve_signature_sparsity_complete", False)),
        ("numeric overclaim", lambda p: p["decision"].__setitem__("surviving_higher_order_moments_numerically_evaluated", True)),
        ("uniform overclaim", lambda p: p["decision"].__setitem__("complete_K500_uniform_leakage_emitted", True)),
        ("floor overclaim", lambda p: p["decision"].__setitem__("native_noncyclic_floor_emitted", True)),
        ("ledger", lambda p: p.__setitem__("source_and_ledger_effect", "changed")),
        ("ceiling", lambda p: p.__setitem__("claim_ceiling", "all moments evaluated")),
    ]
    caught = 0
    for _, mutate in mutations:
        candidate = copy.deepcopy(stored)
        mutate(candidate)
        try:
            verify(candidate)
        except AssertionError:
            caught += 1
    verify(stored)
    assert all(checks) and caught == len(mutations)
    print(f"K603 EXACT CONTROL: {len(checks)}/{len(checks)} pass")
    print(f"K603 HOSTILE SELFTEST: {caught}/{len(mutations)} mutations caught")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
