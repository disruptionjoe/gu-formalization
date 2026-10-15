#!/usr/bin/env python3
"""Hostile mutations for K1818's anchor-hull correction boundary."""
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

mutations = [
    (
        "hide invalidated bank",
        lambda data: data["certificate"].__setitem__("invalidated_checkpoint_count", 0),
    ),
    (
        "reuse withdrawn exclusions",
        lambda data: data["decision"].__setitem__("stationary_rejected_leaf_count", 10),
    ),
    (
        "invent stationary cover",
        lambda data: data["decision"].__setitem__("complete_stationary_cover", True),
    ),
    (
        "invent global optimizer",
        lambda data: data["decision"].__setitem__("global_optimizer_proved", True),
    ),
]

for index, (name, change) in enumerate(mutations, 1):
    mutated = copy.deepcopy(base)
    change(mutated)
    assert not all(ok for _, ok in module.validate_correction(mutated)), name
    print(f"PASS {index:02d}: reject {name}")
print(f"RESULT: PASS {len(mutations)}/{len(mutations)}")
