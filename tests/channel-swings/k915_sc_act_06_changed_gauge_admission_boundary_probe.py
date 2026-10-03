#!/usr/bin/env python3
"""Hostile mutations for K915."""
import copy
import importlib.util
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SOURCE = ROOT / "tests/channel-swings/k915_sc_act_06_changed_gauge_admission_boundary.py"
spec = importlib.util.spec_from_file_location("k915", SOURCE)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
baseline = module.build()
module.validate(baseline)

MUTATIONS = [
    ("admission", "requires_stationary_nonzero_fermion_germ", False),
    ("admission", "requires_action_owned_full_hessian", False),
    ("admission", "requires_both_augmented_ward_equations", False),
    ("admission", "nonzero_torsion_requires_L_injective", False),
    ("admission", "nonzero_torsion_requires_trivial_infinitesimal_stabilizer", False),
    ("admission", "nonzero_torsion_requires_rank_BstarL", 8191),
    ("admission", "old_tangential_lower_bound_persists_in_field_quotient", 0),
    ("admission", "old_real_type_count_persists", 0),
    ("admission", "old_total_real_multiplicity_persists", 0),
    ("admission", "current_custody_satisfies_admission", True),
    ("decision", "changed_gauge_alone_removes_old_quotient", True),
    ("decision", "released_torsion_parent_reopened_on_current_germ", True),
    ("decision", "nonzero_fermion_branch_refuted", True),
    ("decision", "nonzero_fermion_completion_constructed", True),
    ("decision", "SC_ACT_06_proved_or_refuted", True),
    ("decision", "distance_only_cross_budget_route_remains_exhausted", False),
    ("", "classification", "CONVENTIONAL_COMPARATOR"),
    ("", "target_claim", "SC-ACT-01"),
    ("controls", "controls_passed", 45),
    ("decision", "next_exact_input", "repeat cross distance"),
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
print("PASS K915 hostile mutations rejected 20/20")
