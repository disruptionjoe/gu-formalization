#!/usr/bin/env python3
"""Exact controls for K1267's connected D7 Weyl-orbit separation."""
import itertools
import json
import math
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
DATA = json.loads((ROOT / "lab/process/k1267-connected-d7-weyl-orbit-separation.json").read_text())
K1266 = json.loads((ROOT / "lab/process/k1266-realized-regular-sign-pair.json").read_text())
passed = 0

def check(name, condition):
    global passed
    assert condition, name
    passed += 1
    print(f"PASS {passed:02d}: {name}")

xp = tuple(K1266["construction"]["positive_coordinates"])
xm = tuple(K1266["construction"]["negative_coordinates"])
patterns = [s for s in itertools.product((-1, 1), repeat=7) if math.prod(s) == 1]
orbit = set()
for perm in itertools.permutations(range(7)):
    base = tuple(xp[i] for i in perm)
    for signs in patterns:
        orbit.add(tuple(signs[i] * base[i] for i in range(7)))

check("result id", DATA["result_id"] == "K1267-CONNECTED-D7-WEYL-ORBIT-SEPARATION")
check("verified status", DATA["status"] == "working_draft_verified")
check("64 even sign patterns", len(patterns) == DATA["weyl_theorem"]["sign_patterns"] == 64)
check("D7 Weyl order", math.factorial(7) * len(patterns) == DATA["weyl_theorem"]["order"] == 322560)
check("regular distinct-absolute orbit has full order", len(orbit) == 322560)
check("positive representative belongs to orbit", xp in orbit)
check("negative representative excluded from orbit", xm not in orbit)
check("coordinate product invariant on orbit", {math.prod(v) for v in orbit} == {math.prod(xp)})
check("theorem records product invariance", DATA["weyl_theorem"]["coordinate_product_invariant"] is True)
check("opposite product same orbit rejected", DATA["weyl_theorem"]["opposite_nonzero_product_same_orbit"] is False)
check("pair not Weyl conjugate", DATA["decision"]["positive_and_negative_pair_Weyl_conjugate"] is False)
check("connected Spin identification rejected", DATA["decision"]["connected_Spin77_identifies_pair"] is False)
check("physical distinctness withheld", DATA["decision"]["physical_distinctness_proved"] is False)
check("outer identification retained", DATA["decision"]["outer_or_boundary_identification_remains_possible"] is True)
check("source claim unchanged", DATA["decision"]["SC_ACT_06_proved_or_refuted"] is False)
assert passed == 15
print("RESULT: PASS 15/15")
