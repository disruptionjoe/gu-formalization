#!/usr/bin/env python3
"""Hostile mutations for K911."""
import copy
import importlib.util
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SOURCE = ROOT / "tests/channel-swings/k911_sc_act_06_augmented_gauge_ward_splitting.py"
spec = importlib.util.spec_from_file_location("k911", SOURCE)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
baseline = module.build()
module.validate(baseline)

MUTATIONS = [
    ("theorem", "ward_product", "T(G,L)=0"),
    ("theorem", "ward_iff", "S G+B G=0"),
    ("theorem", "old_supported_special_case", "L=0 allows cancellation"),
    ("theorem", "cross_cancellation_possible_only_when_L_nonzero", False),
    ("theorem", "D_enters_gauge_restriction_when_L_nonzero", False),
    ("theorem", "converse", False),
    ("theorem", "stationarity_required_for_hessian_zero_mode", False),
    ("decision", "k903_noncancellation_extends_to_changed_gauge", True),
    ("decision", "changed_gauge_route_is_algebraically_distinct", False),
    ("decision", "nonzero_fermion_stationary_germ_still_required", False),
    ("", "classification", "CONVENTIONAL_COMPARATOR"),
    ("", "target_claim", "SC-ACT-01"),
    ("", "status", "accepted"),
    ("controls", "controls_passed", 37),
    ("controls", "hostile_mutations_rejected", 19),
    ("gu_typed_objects", "field_split", "X"),
    ("gu_typed_objects", "augmented_gauge_map", "unknown"),
    ("gu_typed_objects", "source_fermion_specialization", "none"),
    ("proof", "source_specialization", "no source"),
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
print("PASS K911 hostile mutations rejected 20/20")
