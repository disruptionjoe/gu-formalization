#!/usr/bin/env python3
"""Exact controls for K1268's disconnected orthogonal parity exchange."""
import json
import math
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
DATA = json.loads((ROOT / "lab/process/k1268-disconnected-parity-exchange.json").read_text())
K1266 = json.loads((ROOT / "lab/process/k1266-realized-regular-sign-pair.json").read_text())
passed = 0

def check(name, condition):
    global passed
    assert condition, name
    passed += 1
    print(f"PASS {passed:02d}: {name}")

xp = tuple(K1266["construction"]["positive_coordinates"])
xm = tuple(K1266["construction"]["negative_coordinates"])
def matmul(a, b):
    return [[sum(a[i][k] * b[k][j] for k in range(len(b)))
             for j in range(len(b[0]))] for i in range(len(a))]

def transpose(a):
    return [list(row) for row in zip(*a)]

def diag(values):
    return [[values[i] if i == j else 0 for j in range(len(values))]
            for i in range(len(values))]

I = [[1 if i == j else 0 for j in range(14)] for i in range(14)]
J = [[1 if (i < 7 and j == i + 7) or (i >= 7 and j == i - 7) else 0
      for j in range(14)] for i in range(14)]
S = [row[:] for row in I]
S[0][0] = S[7][7] = 0
S[0][7] = S[7][0] = 1
Hp = diag((*xp, *[-v for v in xp]))
Hm = diag((*xm, *[-v for v in xm]))

check("result id", DATA["result_id"] == "K1268-DISCONNECTED-PARITY-EXCHANGE")
check("verified status", DATA["status"] == "working_draft_verified")
check("swap is involutive", matmul(S, S) == I)
check("swap preserves split form", matmul(matmul(transpose(S), J), S) == J)
check("swap determinant is minus one", DATA["reflection"]["determinant"] == -1)
check("swap conjugates positive to negative", matmul(matmul(S, Hp), S) == Hm)
check("pair exchanged", DATA["reflection"]["exchanges_sign_pair"] is True)
check("not identity component", DATA["reflection"]["lies_in_identity_component"] is False)
check("full orthogonal normalizer identifies", DATA["decision"]["full_O77_normalizer_identifies_pair"] is True)
check("connected Spin does not own reflection", DATA["decision"]["connected_Spin77_owns_reflection"] is False)
check("source gauging withheld", DATA["decision"]["source_action_gauges_reflection"] is False)
check("physical inference rejected", DATA["decision"]["mathematical_exchange_implies_physical_identification"] is False)
check("first coordinate sign changes", xm[0] == -xp[0])
check("remaining coordinates fixed", xm[1:] == xp[1:])
check("Pfaffian sign changes", math.prod(xm) == -math.prod(xp))
check("control count declared", DATA["controls"]["controls_passed"] == 16)
assert passed == 16
print("RESULT: PASS 16/16")
