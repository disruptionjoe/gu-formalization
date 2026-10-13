#!/usr/bin/env python3
"""Hostile mutations for K1806."""
import copy
import importlib.util
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
PATH = ROOT / "tests/channel-swings/k1806_full_fisher_anchored_score_variational.py"
SPEC = importlib.util.spec_from_file_location("k1806", PATH)
k = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(k)


def main():
    data = json.loads(k.ARTIFACT.read_text())
    mutations = []
    for label, mutate in [
        ("claim", lambda d: d.__setitem__("claim_id", "K1805")),
        ("cancellation", lambda d: d["certificate"].__setitem__("varying_denominator_cancels_from_A", False)),
        ("linearity", lambda d: d["certificate"].__setitem__("varying_denominator_linear_in_B", False)),
        ("equality inflation", lambda d: d["decision"].__setitem__("witness_equals_full_fisher_off_anchor", True)),
    ]:
        trial = copy.deepcopy(data); mutate(trial)
        mutations.append((label, not all(ok for _, ok in k.validate(trial))))
    for index, (label, rejected) in enumerate(mutations, 1):
        assert rejected, label
        print(f"PASS {index:02d}: rejects {label}")
    print(f"RESULT: PASS {len(mutations)}/{len(mutations)}")


if __name__ == "__main__":
    main()
