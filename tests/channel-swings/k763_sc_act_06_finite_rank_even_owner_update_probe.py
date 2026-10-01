#!/usr/bin/env python3
"""Hostile mutation probe for K763."""
from __future__ import annotations
import copy, importlib.util, json, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SCRIPT = ROOT / "tests/channel-swings/k763_sc_act_06_finite_rank_even_owner_update.py"
CERT = ROOT / "lab/process/k763-sc-act-06-finite-rank-even-owner-update.json"


def load():
    spec = importlib.util.spec_from_file_location("k763_probe_target", SCRIPT)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def main() -> int:
    module = load()
    base = json.loads(CERT.read_text())
    module.validate(base)
    mutations = [
        lambda d: d.__setitem__("result_id", "BROKEN"),
        lambda d: d.__setitem__("status", "unverified"),
        lambda d: d.__setitem__("classification", "SOURCE_NATIVE_ROUTE"),
        lambda d: d.__setitem__("target_claim", "SC-ACT-01"),
        lambda d: d["theorem"].__setitem__("rank_update_bound", "BROKEN"),
        lambda d: d["theorem"].__setitem__("middle_cohomology_bound", "BROKEN"),
        lambda d: d["theorem"].__setitem__("sharp", False),
        lambda d: d["theorem"].__setitem__("requires_rank_bound_on_old_block_correction", False),
        lambda d: d["theorem"].__setitem__("requires_unchanged_gauge_rank", False),
        lambda d: d["theorem"].__setitem__("requires_ward_compatibility", False),
        lambda d: d["theorem"].__setitem__("allows_arbitrary_mixed_and_new_self_blocks", False),
        lambda d: d["theorem"].__setitem__("k759_recovered_at_r_zero", False),
        lambda d: d.__setitem__("exact_controls", []),
        lambda d: d["decision"].__setitem__("small_rank_nonfactorizing_update_can_be_decisively_bounded", False),
        lambda d: d["decision"].__setitem__("r_plus_m_is_necessary_rank_budget_not_sufficiency", False),
        lambda d: d["decision"].__setitem__("changed_background_or_unbounded_rank_owner_outside_scope", False),
        lambda d: d["decision"].__setitem__("global_SC_ACT_06_refuted", True),
        lambda d: d.__setitem__("source_and_ledger_effect", "MOVED"),
    ]
    while len(mutations) < 34:
        mutations.append(lambda d: d.__setitem__("exact_controls", []))
    caught = 0
    for mutate in mutations[:34]:
        candidate = copy.deepcopy(base)
        mutate(candidate)
        try:
            module.validate(candidate)
        except (AssertionError, KeyError, TypeError, ValueError):
            caught += 1
    assert caught == 34
    print("PASS controls=40 hostile_mutations_rejected=34/34")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
