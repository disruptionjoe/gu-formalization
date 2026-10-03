#!/usr/bin/env python3
"""Hostile mutations for K918."""
import copy
import importlib.util
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SOURCE = ROOT / "tests/channel-swings/k918_sc_act_06_nilpotent_ward_cancellation_obstruction.py"
spec = importlib.util.spec_from_file_location("k918", SOURCE)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
baseline = module.build()
module.validate(baseline)

MUTATIONS = [
    ("theorem", "body_of_BstarL", 1),
    ("theorem", "body_ward_equation", "0=0"),
    ("theorem", "KG_rank", 0),
    ("theorem", "nonzero_body_kappa_allowed", True),
    ("theorem", "nilpotent_kappa_changes_ordinary_torsion_coefficient", True),
    ("theorem", "literal_odd_background_salvages_ordinary_torsion", True),
    ("theorem", "independent_body_old_old_correction_remains_possible", False),
    ("theorem", "even_condensate_background_change_remains_possible", False),
    ("decision", "k915_changed_gauge_reopens_nonzero_body_torsion_on_literal_odd_route", True),
    ("decision", "changed_gauge_superpoint_branch_fully_refuted", True),
    ("decision", "new_body_level_action_parent_required_for_ordinary_torsion", False),
    ("decision", "SC_ACT_06_proved_or_refuted", True),
    ("", "classification", "CONVENTIONAL_COMPARATOR"),
    ("", "target_claim", "SC-ACT-01"),
    ("controls", "controls_passed", 43),
    ("controls", "hostile_mutations_rejected", 19),
    ("gu_typed_objects", "ward_equation", "SG=0"),
    ("proof", "parity_product", "nonzero body"),
    ("proof", "rank", "KG zero"),
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
print("PASS K918 hostile mutations rejected 20/20")
