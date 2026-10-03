#!/usr/bin/env python3
"""Hostile mutations for K916."""
import copy
import importlib.util
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SOURCE = ROOT / "tests/channel-swings/k916_sc_act_06_ordinary_point_fermion_parity_boundary.py"
spec = importlib.util.spec_from_file_location("k916", SOURCE)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
baseline = module.build()
module.validate(baseline)

MUTATIONS = [
    ("theorem", "ordinary_point_odd_coordinate", "psi may be nonzero"),
    ("theorem", "nonzero_literal_odd_field_requires_super_base", False),
    ("theorem", "nonzero_commuting_spinor_is_literal_odd_field", True),
    ("theorem", "category_change_requires_new_action_typing", False),
    ("theorem", "source_fermionic_label_alone_selects_category", True),
    ("theorem", "ordinary_zero_fermion_germ_is_not_a_truncation_error", False),
    ("theorem", "parity_body_result_preexisted_in_K751_K752", False),
    ("decision", "k915_reopener_requires_category_refinement", False),
    ("decision", "literal_odd_superpoint_route_closed", True),
    ("decision", "commuting_spinor_proxy_constructed", True),
    ("decision", "SC_ACT_06_proved_or_refuted", True),
    ("", "classification", "CONVENTIONAL_COMPARATOR"),
    ("", "target_claim", "SC-ACT-01"),
    ("", "status", "accepted"),
    ("controls", "controls_passed", 39),
    ("controls", "hostile_mutations_rejected", 21),
    ("gu_typed_objects", "ordinary_base", "graded field"),
    ("gu_typed_objects", "literal_fermion", "ordinary vector"),
    ("proof", "proxy_fence", "same category"),
    ("decision", "next_exact_input", "repeat cross budget"),
    ("decision", "new_scientific_theorem_claimed", True),
    ("decision", "k915_successor_wording_needs_correction", False),
]

rejected = 0
for section, key, value in MUTATIONS:
    candidate = copy.deepcopy(baseline)
    (candidate[section] if section else candidate)[key] = value
    try:
        module.validate(candidate)
    except AssertionError:
        rejected += 1
assert rejected == 22
print("PASS K916 hostile mutations rejected 22/22")
