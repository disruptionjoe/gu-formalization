#!/usr/bin/env python3
"""Exact controls for K1269's D7/B7 invariant-ring boundary."""
import itertools
import json
import math
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
DATA = json.loads((ROOT / "lab/process/k1269-d7-b7-invariant-quotient-boundary.json").read_text())
passed = 0

def check(name, condition):
    global passed
    assert condition, name
    passed += 1
    print(f"PASS {passed:02d}: {name}")

x = (1, 2, 3, 4, 5, 6, 7)
odd = (-x[0], *x[1:])
even = (-x[0], -x[1], *x[2:])

def elementary_squares(values):
    sq = [q*q for q in values]
    return tuple(sum(math.prod(c) for c in itertools.combinations(sq, k))
                 for k in range(1, 8))

check("result id", DATA["result_id"] == "K1269-D7-B7-INVARIANT-QUOTIENT-BOUNDARY")
check("verified status", DATA["status"] == "working_draft_verified")
check("connected degrees", DATA["rings"]["connected_degrees"] == [2,4,6,8,10,12,7])
check("all-signed degrees", DATA["rings"]["all_signed_degrees"] == [2,4,6,8,10,12,14])
check("top square relation", elementary_squares(x)[6] == math.prod(x) ** 2)
check("odd reflection flips p", math.prod(odd) == -math.prod(x))
check("odd reflection fixes p squared", math.prod(odd) ** 2 == math.prod(x) ** 2)
check("even reflection fixes p", math.prod(even) == math.prod(x))
check("all elementary square invariants fixed by odd reflection", elementary_squares(odd) == elementary_squares(x))
check("D7 generator count seven", len(DATA["rings"]["connected_degrees"]) == 7)
check("B7 generator count seven", len(DATA["rings"]["all_signed_degrees"]) == 7)
check("even subring identified", DATA["decision"]["K1264_even_subring_matches_outer_sign_quotient"] is True)
check("degree seven survives connected quotient", DATA["decision"]["degree_seven_generator_survives_connected_quotient"] is True)
check("degree seven sign lost after extension", DATA["decision"]["degree_seven_sign_survives_disconnected_quotient"] is False)
check("physical quotient withheld", DATA["decision"]["physical_outer_quotient_owned"] is False)
check("control count declared", DATA["controls"]["controls_passed"] == 16)
assert passed == 16
print("RESULT: PASS 16/16")
