#!/usr/bin/env python3
"""Hostile mutations for K1807 (reuses the producer's computed certificate)."""
import copy
import importlib.util
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
PATH = ROOT / "tests/channel-swings/k1807_full_fisher_anchored_score_compact_taylor.py"
SPEC = importlib.util.spec_from_file_location("k1807", PATH)
k = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(k)


def main():
    data = json.loads(k.ARTIFACT.read_text())
    # The producer performs the expensive independent Arb replay.  The hostile
    # probe isolates admission logic so a mutation sweep does not repeat that
    # nine-minute scientific integration.
    got = copy.deepcopy(data["certificate"])
    mutations = []
    for label, mutate in [
        ("claim", lambda d: d.__setitem__("claim_id", "K1806")),
        ("rectangle", lambda d: d["certificate"]["rectangle"]["z"].__setitem__(0, "1/2")),
        ("margin", lambda d: d["certificate"]["compact_bounds"].__setitem__("cross_margin_lower", "0")),
        ("whole-line inflation", lambda d: d["decision"].__setitem__("complete_slab_two_whole_line_witness_certified", True)),
    ]:
        trial = copy.deepcopy(data); mutate(trial)
        mutations.append((label, not all(ok for _, ok in k.validate(trial, got))))
    for index, (label, rejected) in enumerate(mutations, 1):
        assert rejected, label
        print(f"PASS {index:02d}: rejects {label}")
    print(f"RESULT: PASS {len(mutations)}/{len(mutations)}")


if __name__ == "__main__":
    main()
