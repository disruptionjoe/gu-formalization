#!/usr/bin/env python3
"""Hostile mutations for K919."""
import copy
import importlib.util
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SOURCE = ROOT / "tests/channel-swings/k919_sc_act_06_body_quotient_persistence.py"
spec = importlib.util.spec_from_file_location("k919", SOURCE)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
baseline = module.build()
module.validate(baseline)

MUTATIONS = [
    ("theorem", "body_old_quotient_dimension", 0),
    ("theorem", "body_old_real_type_count", 0),
    ("theorem", "body_old_total_real_multiplicity", 0),
    ("theorem", "body_graph_removes_old_complement", True),
    ("theorem", "body_injection", "zero"),
    ("theorem", "kernel_of_body_injection", 1),
    ("theorem", "nilpotent_gauge_components_change_body_quotient", True),
    ("theorem", "changed_super_hessian_response_computed", True),
    ("decision", "literal_odd_superpoint_erases_old_body_deficit", True),
    ("decision", "old_typewise_body_repair_still_required", False),
    ("decision", "supermodule_cohomology_classified", True),
    ("decision", "SC_ACT_06_proved_or_refuted", True),
    ("", "classification", "CONVENTIONAL_COMPARATOR"),
    ("", "target_claim", "SC-ACT-01"),
    ("controls", "controls_passed", 41),
    ("controls", "hostile_mutations_rejected", 19),
    ("gu_typed_objects", "body_gauge_graph", "lambda maps to (G,L)"),
    ("proof", "intersection", "nonzero intersection"),
    ("", "claim_ceiling", "full cohomology classified"),
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
print("PASS K919 hostile mutations rejected 20/20")
