#!/usr/bin/env python3
"""Hostile mutations for K1818's corrected anchor-hull bank."""
import copy
import hashlib
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


def forge_gradient_exclusion(data):
    row = data["certificate"]["stationary_rejection_evidence"][0]
    row["certificate"]["whole_line_gradient"]["t"] = "[-1 +/- 2]"
    row["certificate"]["whole_line_gradient"]["z"] = "[-1 +/- 2]"
    canonical = dict(row)
    canonical.pop("checkpoint_digest")
    encoded = json.dumps(canonical, sort_keys=True, separators=(",", ":")).encode()
    row["checkpoint_digest"] = hashlib.sha256(encoded).hexdigest()

mutations = [
    (
        "drop rejection evidence",
        lambda data: data["certificate"]["stationary_rejection_evidence"].pop(),
    ),
    (
        "misstate stationary exclusions",
        lambda data: data["decision"].__setitem__(
            "stationary_rejected_leaf_count",
            data["decision"]["stationary_rejected_leaf_count"] + 1,
        ),
    ),
    ("forge gradient exclusion", forge_gradient_exclusion),
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
    assert not all(ok for _, ok in module.validate_current(mutated)), name
    print(f"PASS {index:02d}: reject {name}")
print(f"RESULT: PASS {len(mutations)}/{len(mutations)}")
