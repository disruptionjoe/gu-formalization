#!/usr/bin/env python3
"""Hostile mutations for K917."""
import copy
import importlib.util
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SOURCE = ROOT / "tests/channel-swings/k917_sc_act_06_superpoint_gauge_body_reduction.py"
spec = importlib.util.spec_from_file_location("k917", SOURCE)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
baseline = module.build()
module.validate(baseline)

MUTATIONS = [
    ("theorem", "body_of_odd_background", 1),
    ("theorem", "body_of_fermionic_gauge_tangent", 1),
    ("theorem", "body_augmented_gauge_map", "(G,L)"),
    ("theorem", "ordinary_rank_of_L_body", 16384),
    ("theorem", "ordinary_injectivity_of_L_body", True),
    ("theorem", "k912_rank_16384_transfers_to_body", True),
    ("theorem", "supermodule_injectivity_requires_separate_definition", False),
    ("theorem", "zero_body_excludes_nonzero_superpoint", True),
    ("decision", "literal_odd_background_supplies_ordinary_injective_L", True),
    ("decision", "k912_ordinary_stabilizer_test_satisfied", True),
    ("decision", "supergeometric_route_refuted", True),
    ("decision", "SC_ACT_06_proved_or_refuted", True),
    ("", "classification", "CONVENTIONAL_COMPARATOR"),
    ("", "target_claim", "SC-ACT-01"),
    ("controls", "controls_passed", 41),
    ("controls", "hostile_mutations_rejected", 19),
    ("gu_typed_objects", "body_gauge_map", "identity"),
    ("proof", "body", "odd survives body"),
    ("proof", "rank_fence", "ordinary rank transfers"),
    ("decision", "next_exact_input", "repeat cross budget"),
]

rejected = 0
for section, key, value in MUTATIONS:
    candidate = copy.deepcopy(baseline)
    (candidate[section] if section else candidate)[key] = value
    try:
        module.validate(candidate)
    except AssertionError:
        rejected += 1
assert rejected == 20
print("PASS K917 hostile mutations rejected 20/20")
