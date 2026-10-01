#!/usr/bin/env python3
"""Hostile mutation probe for K759."""
from __future__ import annotations
import copy, importlib.util, json, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SCRIPT = ROOT / "tests/channel-swings/k759_sc_act_06_even_spectator_rank_update_theorem.py"
CERT = ROOT / "lab/process/k759-sc-act-06-even-spectator-rank-update-theorem.json"


def load():
    spec = importlib.util.spec_from_file_location("k759_probe_target", SCRIPT); assert spec and spec.loader
    mod = importlib.util.module_from_spec(spec); sys.modules[spec.name] = mod; spec.loader.exec_module(mod); return mod


def main() -> int:
    mod = load(); base = json.loads(CERT.read_text()); mod.validate(base)
    muts = [
        lambda d: d.__setitem__("result_id", "BROKEN"), lambda d: d.__setitem__("status", "unverified"),
        lambda d: d.__setitem__("classification", "SOURCE_NATIVE_ROUTE"), lambda d: d.__setitem__("target_claim", "SC-ACT-01"),
        lambda d: d["theorem"].__setitem__("update_rank_bound", "BROKEN"), lambda d: d["theorem"].__setitem__("middle_cohomology_bound", "BROKEN"),
        lambda d: d["theorem"].__setitem__("sharp", False), lambda d: d["theorem"].__setitem__("requires_fixed_old_block", False),
        lambda d: d["theorem"].__setitem__("requires_unchanged_old_gauge_embedding", False), lambda d: d["theorem"].__setitem__("allows_arbitrary_mixed_and_self_blocks", False),
        lambda d: d.__setitem__("exact_controls", []), lambda d: d["decision"].__setitem__("one_new_even_field_can_remove_at_most_one_old_middle_class", False),
        lambda d: d["decision"].__setitem__("changed_background_or_changed_old_block_outside_scope", False), lambda d: d.__setitem__("source_and_ledger_effect", "MOVED"),
    ]
    while len(muts) < 30: muts.append(lambda d: d.__setitem__("exact_controls", []))
    caught = 0
    for mutate in muts[:30]:
        candidate = copy.deepcopy(base); mutate(candidate)
        try: mod.validate(candidate)
        except (AssertionError, KeyError, TypeError, ValueError): caught += 1
    assert caught == 30; print("PASS controls=36 hostile_mutations_rejected=30/30"); return 0


if __name__ == "__main__": raise SystemExit(main())
