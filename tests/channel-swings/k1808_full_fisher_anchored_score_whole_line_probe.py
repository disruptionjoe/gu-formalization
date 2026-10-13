#!/usr/bin/env python3
"""Hostile mutations for K1808."""
import copy
import importlib.util
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
PATH = ROOT / "tests/channel-swings/k1808_full_fisher_anchored_score_whole_line.py"
SPEC = importlib.util.spec_from_file_location("k1808", PATH)
k = importlib.util.module_from_spec(SPEC); sys.modules[SPEC.name] = k; SPEC.loader.exec_module(k)


def main():
    data = json.loads(k.ARTIFACT.read_text()); got = k.compute()
    mutations = []
    for label, mutate in [
        ("claim", lambda d: d.__setitem__("claim_id", "K1807")),
        ("tail start", lambda d: d["certificate"].__setitem__("tail_start", "10")),
        ("J tail", lambda d: d["certificate"]["absolute_two_tail_bounds"].__setitem__("J", "0")),
        ("margin", lambda d: d["certificate"].__setitem__("whole_line_cross_margin_lower", "0")),
        ("global inflation", lambda d: d["decision"].__setitem__("global_optimizer_proved", True)),
    ]:
        trial = copy.deepcopy(data); mutate(trial)
        mutations.append((label, not all(ok for _, ok in k.validate(trial, got))))
    for index, (label, rejected) in enumerate(mutations, 1):
        assert rejected, label
        print(f"PASS {index:02d}: rejects {label}")
    print(f"RESULT: PASS {len(mutations)}/{len(mutations)}")


if __name__ == "__main__": main()
