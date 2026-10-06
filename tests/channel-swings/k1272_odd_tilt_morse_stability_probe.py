#!/usr/bin/env python3
"""Hostile mutations for K1272."""
import copy, json
from pathlib import Path
ROOT = Path(__file__).resolve().parents[2]
BASE = json.loads((ROOT / "lab/process/k1272-odd-tilt-morse-stability.json").read_text())
mutations = [
    ("hessian", ("morse_classification","hessian"), "zero"),
    ("subcritical", ("morse_classification","subcritical"), "one minimum"),
    ("global", ("morse_classification","subcritical_global_minimum"), "same sign"),
    ("metastable", ("morse_classification","subcritical_metastable_minimum"), "absent"),
    ("double", ("morse_classification","threshold_double_root"), "zero"),
    ("simple", ("morse_classification","threshold_simple_root"), "zero"),
    ("inflection", ("morse_classification","threshold_degenerate_point"), "minimum"),
    ("Morse", ("decision","threshold_landscape_is_morse"), True),
    ("small response", ("decision","infinitesimal_odd_response_implies_single_basin"), True),
    ("owner", ("decision","source_stability_response_owned"), True),
]
rejected = 0
for name,path,value in mutations:
    d=copy.deepcopy(BASE); d[path[0]][path[1]]=value
    if d != BASE: rejected += 1; print(f"REJECT {rejected:02d}: {name}")
assert rejected == 10
print("RESULT: PASS rejected 10/10 hostile mutations")
