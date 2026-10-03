#!/usr/bin/env python3
"""Hostile mutations for K895."""
from __future__ import annotations
import copy, importlib.util
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SOURCE = ROOT / "tests/channel-swings/k895_sc_act_06_helmholtz_symmetry_obstruction.py"
spec = importlib.util.spec_from_file_location("k895", SOURCE); module = importlib.util.module_from_spec(spec); spec.loader.exec_module(module)
base = module.build(); module.validate(base)

mutations = [
    ("exact_helmholtz_test", "representative_block_count", 55), ("exact_helmholtz_test", "representative_multiplicity", 8191),
    ("exact_helmholtz_test", "connection_field_dimension", 229375), ("exact_helmholtz_test", "selected_action_rank", 130911),
    ("exact_helmholtz_test", "radial_gauge_restriction_rank", 8190), ("exact_helmholtz_test", "helmholtz_symmetry_defect_rank", 130911),
    ("structural_theorem", "formal_euler_rule", "A=R"), ("structural_theorem", "formal_adjoint_identity", "A^T=A"),
    ("structural_theorem", "selected_map_is_nonzero", False), ("structural_theorem", "selected_map_is_helmholtz_integrable_as_standalone_hessian", True),
    ("structural_theorem", "exact_selected_map_rank", 0), ("structural_theorem", "exact_symmetry_defect_rank", 0),
    ("structural_theorem", "radial_defect_is_strict_subtest", False), ("decision", "selected_i1b_formal_euler_map_is_action_hessian", True),
    ("decision", "k891_radial_cancellation_is_sufficient_for_action_ownership", True), ("decision", "same_domain_variational_completion_still_possible", False),
    ("decision", "quotient_ranks_now_admissible", True), ("controls", "controls_passed", 39),
    ("controls", "hostile_mutations_rejected", 19), ("", "classification", "CONVENTIONAL_COMPARATOR"),
]
rejected = 0
for section, key, value in mutations:
    packet = copy.deepcopy(base)
    (packet[section] if section else packet)[key] = value
    try:
        module.validate(packet)
    except AssertionError:
        rejected += 1
assert rejected == 20
print("PASS K895 hostile mutations rejected 20/20")
