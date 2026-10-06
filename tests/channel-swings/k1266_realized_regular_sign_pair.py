#!/usr/bin/env python3
"""Exact controls for K1266's realized regular split-D7 sign pair."""
import itertools
import json
import math
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
DATA = json.loads((ROOT / "lab/process/k1266-realized-regular-sign-pair.json").read_text())
passed = 0

def check(name, condition):
    global passed
    assert condition, name
    passed += 1
    print(f"PASS {passed:02d}: {name}")

xp = tuple(DATA["construction"]["positive_coordinates"])
xm = tuple(DATA["construction"]["negative_coordinates"])

def elementary(values, k):
    return sum(math.prod(c) for c in itertools.combinations(values, k))

def regular_d(coords):
    return all(coords[i] != coords[j] and coords[i] != -coords[j]
               for i in range(7) for j in range(i + 1, 7))

def matmul(a, b):
    return [[sum(a[i][k] * b[k][j] for k in range(len(b)))
             for j in range(len(b[0]))] for i in range(len(a))]

def transpose(a):
    return [list(row) for row in zip(*a)]

def add(a, b):
    return [[a[i][j] + b[i][j] for j in range(len(a[0]))] for i in range(len(a))]

def diag(values):
    return [[values[i] if i == j else 0 for j in range(len(values))]
            for i in range(len(values))]

J = [[1 if (i < 7 and j == i + 7) or (i >= 7 and j == i - 7) else 0
      for j in range(14)] for i in range(14)]
Hp = diag((*xp, *[-v for v in xp]))
Hm = diag((*xm, *[-v for v in xm]))
zero = [[0] * 14 for _ in range(14)]
even_p = tuple(elementary([v*v for v in xp], k) for k in range(1, 7))
even_m = tuple(elementary([v*v for v in xm], k) for k in range(1, 7))
p_p = math.prod(xp)
p_m = math.prod(xm)

check("result id", DATA["result_id"] == "K1266-REALIZED-REGULAR-SIGN-PAIR")
check("verified status", DATA["status"] == "working_draft_verified")
check("positive Cartan element lies in so(7,7)", add(matmul(transpose(Hp), J), matmul(J, Hp)) == zero)
check("negative Cartan element lies in so(7,7)", add(matmul(transpose(Hm), J), matmul(J, Hm)) == zero)
check("positive representative is regular", regular_d(xp))
check("negative representative is regular", regular_d(xm))
check("coordinate squares agree as multisets", sorted(v*v for v in xp) == sorted(v*v for v in xm))
check("six even primitive invariants agree", even_p == even_m)
check("positive Pfaffian coordinate", p_p == DATA["construction"]["positive_p"] == 5040)
check("negative Pfaffian coordinate", p_m == DATA["construction"]["negative_p"] == -5040)
check("degree-seven signs oppose", p_p == -p_m)
check("both signs marked realized", DATA["decision"]["both_I7_signs_realized_on_regular_split_Cartan"] is True)
check("not ambient-only", DATA["decision"]["ambient_formal_pair_only"] is False)
check("full orbit image withheld", DATA["decision"]["full_real_orbit_image_classified"] is False)
check("action ownership withheld", DATA["decision"]["source_action_response_owned"] is False)
check("control count declared", DATA["controls"]["controls_passed"] == 16)
assert passed == 16
print("RESULT: PASS 16/16")
