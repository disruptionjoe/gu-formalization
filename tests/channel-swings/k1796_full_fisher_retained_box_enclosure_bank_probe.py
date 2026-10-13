#!/usr/bin/env python3
"""Hostile mutations for K1796's exact retained-box enclosure bank."""
import copy
import importlib.util
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SOURCE = ROOT / "tests/channel-swings/k1796_full_fisher_retained_box_enclosure_bank.py"
spec = importlib.util.spec_from_file_location("k1796_probe_target", SOURCE)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
base = json.loads(module.ARTIFACT.read_text())
got = copy.deepcopy(base["enclosure"])
mutations = [
    (("enclosure", "polynomial_terms"), 1257),
    (("enclosure", "partition_digest"), "0" * 64),
    (("enclosure", "excluded_fraction_of_k1791_area"), "1"),
    (("enclosure", "retained_fraction_of_original_input_area"), "0"),
    (("decision", "fixed_cutoff_exact_inversion_completed"), False),
    (("decision", "strict_retained_area_contraction"), False),
    (("decision", "complete_retained_frontier_excluded"), True),
    (("decision", "retained_leaf_means_below_threshold"), True),
    (("decision", "global_optimizer_proved"), True),
]


def set_path(data, path, value):
    for key in path[:-1]:
        data = data[key]
    data[path[-1]] = value


for index, (path, value) in enumerate(mutations, 1):
    mutant = copy.deepcopy(base)
    set_path(mutant, path, value)
    assert not all(ok for _, ok in module.validate(mutant, got)), path
    print(f"REJECT {index:02d}: {path}")
print(f"RESULT: PASS {len(mutations)}/{len(mutations)}")
