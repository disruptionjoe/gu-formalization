#!/usr/bin/env python3
"""Hostile mutations for K912."""
import copy
import importlib.util
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SOURCE = ROOT / "tests/channel-swings/k912_sc_act_06_torsion_salvage_stabilizer_necessity.py"
spec = importlib.util.spec_from_file_location("k912", SOURCE)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
baseline = module.build()
module.validate(baseline)

MUTATIONS = [
    ("theorem", "first_ward_equation", "kappa KG=0"),
    ("theorem", "nonzero_kappa_implies_composite_identity", "B*L=0"),
    ("theorem", "rank_KG", 8191),
    ("theorem", "nonzero_kappa_implies_rank_BstarL", 8191),
    ("theorem", "nonzero_kappa_implies_L_injective", False),
    ("theorem", "nonzero_kappa_implies_trivial_infinitesimal_stabilizer", False),
    ("theorem", "nonzero_kappa_implies_Bstar_injective_on_imL", False),
    ("theorem", "minimum_new_gauge_carrier_dimension", 8191),
    ("theorem", "nontrivial_kernel_L_forces_kappa_zero", False),
    ("decision", "changed_gauge_automatically_rescues_torsion", True),
    ("decision", "trivial_stabilizer_is_sufficient_for_full_repair", True),
    ("decision", "trivial_stabilizer_is_necessary_for_nonzero_kappa", False),
    ("", "classification", "CONVENTIONAL_COMPARATOR"),
    ("", "target_claim", "SC-ACT-01"),
    ("", "status", "accepted"),
    ("controls", "controls_passed", 39),
    ("controls", "hostile_mutations_rejected", 19),
    ("gu_typed_objects", "gauge_parameter", "U, dimension 8191"),
    ("proof", "source_reading", "stabilizer irrelevant"),
    ("decision", "next_exact_input", "repeat target budget"),
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
print("PASS K912 hostile mutations rejected 20/20")
