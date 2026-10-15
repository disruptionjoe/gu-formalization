#!/usr/bin/env python3
"""Hostile mutations for K1818's complete whole-line gradient bank."""
import copy
import importlib.util
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
PRODUCER = ROOT / "tests/channel-swings/k1818_full_fisher_slab_three_stationary_cover.py"
spec = importlib.util.spec_from_file_location("k1818_probe_base", PRODUCER)
module = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = module
spec.loader.exec_module(module)
base = json.loads(module.ARTIFACT.read_text())


def corrupt_digest(data):
    data["certificate"]["stationary_rejection_evidence"][0]["checkpoint_digest"] = "0" * 64


mutations = [
    (
        "hide rejected-leaf evidence",
        lambda data: data["certificate"]["stationary_rejection_evidence"].pop(),
    ),
    (
        "promote retention to another stationary point",
        lambda data: data["decision"].__setitem__(
            "retained_leaf_means_additional_stationary_point", True
        ),
    ),
    (
        "invent stationary cover",
        lambda data: data["decision"].__setitem__("complete_stationary_cover", True),
    ),
    (
        "invent global optimizer",
        lambda data: data["decision"].__setitem__("global_optimizer_proved", True),
    ),
    ("corrupt checkpoint digest", corrupt_digest),
]

for index, (name, change) in enumerate(mutations, 1):
    mutated = copy.deepcopy(base)
    change(mutated)
    assert not all(ok for _, ok in module.validate_current(mutated)), name
    print(f"PASS {index:02d}: reject {name}")
print(f"RESULT: PASS {len(mutations)}/{len(mutations)}")
