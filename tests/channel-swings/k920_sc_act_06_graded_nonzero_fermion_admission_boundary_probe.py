#!/usr/bin/env python3
"""Hostile mutations for K920."""
import copy
import importlib.util
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SOURCE = ROOT / "tests/channel-swings/k920_sc_act_06_graded_nonzero_fermion_admission_boundary.py"
spec = importlib.util.spec_from_file_location("k920", SOURCE)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
baseline = module.build()
module.validate(baseline)

MUTATIONS = [
    ("admission", "ordinary_point_literal_fermions_zero", False),
    ("admission", "literal_odd_L_body_rank", 16384),
    ("admission", "literal_odd_BstarL_body", 1),
    ("admission", "nonzero_body_kappa_salvaged_by_literal_odd_data", True),
    ("admission", "old_body_quotient_dimension_persists", 0),
    ("admission", "old_body_real_type_count_persists", 0),
    ("admission", "old_body_total_real_multiplicity_persists", 0),
    ("admission", "commuting_proxy_requires_category_and_action_receipt", False),
    ("admission", "even_composite_requires_new_stationary_body_and_hessian", False),
    ("admission", "full_supermodule_complex_requires_module_rank_noether_and_domain_data", False),
    ("decision", "k915_ordinary_rank_reopener_applies_unchanged_to_literal_odd_fields", True),
    ("decision", "literal_odd_route_refuted_as_supergeometry", True),
    ("decision", "literal_odd_route_repairs_ordinary_body", True),
    ("decision", "commuting_proxy_constructed", True),
    ("decision", "even_composite_constructed", True),
    ("decision", "SC_ACT_06_proved_or_refuted", True),
    ("decision", "distance_only_cross_budget_route_remains_exhausted", False),
    ("", "classification", "CONVENTIONAL_COMPARATOR"),
    ("controls", "controls_passed", 51),
    ("decision", "next_exact_input", "repeat distance budget"),
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
print("PASS K920 hostile mutations rejected 20/20")
