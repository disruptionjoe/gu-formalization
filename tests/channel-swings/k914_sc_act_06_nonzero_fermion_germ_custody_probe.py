#!/usr/bin/env python3
"""Hostile mutations for K914."""
import copy
import importlib.util
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SOURCE = ROOT / "tests/channel-swings/k914_sc_act_06_nonzero_fermion_germ_custody.py"
spec = importlib.util.spec_from_file_location("k914", SOURCE)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
baseline = module.build()
module.validate(baseline)

MUTATIONS = [
    ("custody", "source_displays_fermion_operator_candidate", False),
    ("custody", "source_displays_mixed_euler_architecture", False),
    ("custody", "source_supplies_nonzero_fermion_stationary_solution", True),
    ("custody", "repository_owns_nonzero_fermion_stationary_solution", True),
    ("custody", "repository_has_computed_nonzero_background_L", True),
    ("custody", "repository_has_complete_nonzero_background_hessian", True),
    ("custody", "repository_has_common_domain_green_preboundary_packet", True),
    ("custody", "k717_zero_fermion_results_transfer_automatically", True),
    ("decision", "nonzero_fermion_branch_closed", True),
    ("decision", "nonzero_fermion_branch_currently_instantiable", True),
    ("decision", "absence_is_source_disproof", True),
    ("", "classification", "CONVENTIONAL_COMPARATOR"),
    ("", "target_claim", "SC-ACT-01"),
    ("", "status", "accepted"),
    ("controls", "controls_passed", 41),
    ("controls", "hostile_mutations_rejected", 19),
    ("gu_typed_objects", "current_fermion_background", "nonzero"),
    ("evidence", "source_ceiling", "source supplies solution"),
    ("decision", "next_exact_input", "none"),
    ("gu_typed_objects", "required_new_object", "already complete"),
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
print("PASS K914 hostile mutations rejected 20/20")
