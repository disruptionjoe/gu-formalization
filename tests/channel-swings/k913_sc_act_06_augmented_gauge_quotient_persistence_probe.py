#!/usr/bin/env python3
"""Hostile mutations for K913."""
import copy
import importlib.util
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SOURCE = ROOT / "tests/channel-swings/k913_sc_act_06_augmented_gauge_quotient_persistence.py"
spec = importlib.util.spec_from_file_location("k913", SOURCE)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
baseline = module.build()
module.validate(baseline)

MUTATIONS = [
    ("theorem", "inclusion", "zero map"),
    ("theorem", "inclusion_is_injective_for_every_L", False),
    ("theorem", "proof_hypothesis", "H_old=im(G)"),
    ("theorem", "surviving_lower_bound_dimension", 0),
    ("theorem", "surviving_real_type_count", 0),
    ("theorem", "surviving_total_real_multiplicity", 0),
    ("theorem", "augmented_gauge_can_change_ward_cancellation", False),
    ("theorem", "augmented_gauge_alone_erases_old_tangential_classes", True),
    ("decision", "changed_gauge_removes_k879_old_obstruction_by_quotienting", True),
    ("decision", "changed_gauge_may_still_change_hessian_on_old_classes", False),
    ("decision", "old_typewise_repair_obligation_persists", False),
    ("", "classification", "CONVENTIONAL_COMPARATOR"),
    ("", "target_claim", "SC-ACT-01"),
    ("", "status", "accepted"),
    ("controls", "controls_passed", 41),
    ("controls", "hostile_mutations_rejected", 19),
    ("gu_typed_objects", "quotient", "zero"),
    ("proof", "independence_from_L", "L must be injective"),
    ("proof", "scope_fence", "ellipticity follows"),
    ("decision", "next_exact_input", "repeat target distance"),
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
print("PASS K913 hostile mutations rejected 20/20")
