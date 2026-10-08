#!/usr/bin/env python3
"""Hostile mutations for K1483."""
import copy, importlib.util
from pathlib import Path

P = Path(__file__).with_name("k1483_wick_third_moment_triangle_bound.py")
S = importlib.util.spec_from_file_location("k1483", P); M = importlib.util.module_from_spec(S); S.loader.exec_module(M)
mutations = [
    ("claim_id", "K0000"),
    ("third_moment_triangle.unique_contraction_graph", "one edge"),
    ("third_moment_triangle.contraction_count", "1"),
    ("third_moment_triangle.exact_formula", "zero"),
    ("third_moment_triangle.positivity", "unknown"),
    ("third_moment_triangle.young_bound", "none"),
    ("third_moment_triangle.ratio_bound", "none"),
    ("third_moment_triangle.three_dimensional_order", "none"),
    ("decision.unique_triangle_contraction_proved", False),
    ("decision.exact_contraction_coefficient", 0),
    ("decision.third_moment_nonnegative", False),
    ("decision.third_moment_order_upper", "N^7"),
    ("decision.third_moment_to_variance_ratio_order_upper", "N^2"),
    ("decision.matching_third_moment_asymptotic_proved", True),
    ("decision.protected_status_change", True),
]
for i, (path, value) in enumerate(mutations, 1):
    d = copy.deepcopy(M.D); node = d
    bits = path.split(".")
    for key in bits[:-1]: node = node[key]
    node[bits[-1]] = value
    assert not all(M.validate(d)), path
    print(f"PASS {i:02d}: rejected {path}")
print(f"RESULT: PASS {len(mutations)}/{len(mutations)}")
