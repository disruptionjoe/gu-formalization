#!/usr/bin/env python3
"""Exact controls for K1256's invariant-channel Hessian rank theorem."""
import json
from pathlib import Path
import sympy as sp

ROOT = Path(__file__).resolve().parents[2]
DATA = json.loads((ROOT / "lab/process/k1256-invariant-channel-hessian-rank-bound.json").read_text())
passed = 0

def check(name, condition):
    global passed
    assert condition, name
    passed += 1
    print(f"PASS {passed:02d}: {name}")

check("result id", DATA["result_id"] == "K1256-INVARIANT-CHANNEL-HESSIAN-RANK-BOUND")
check("verified status", DATA["status"] == "working_draft_verified")

for m in range(1, 8):
    P = sp.zeros(m, 7)
    for i in range(m):
        P[i, i] = i + 1
    B = sp.diag(*range(1, m + 1))
    H = P.T * B * P
    check(f"m={m} Hessian rank is m", H.rank() == m)
    check(f"m={m} nullity is 7-m", 7 - H.rank() == 7 - m)

# Nonlinear-chain-rule control at a critical outer function.
x = sp.symbols("x0:7")
Pnl = sp.Matrix([x[0] + x[1] ** 2, x[2] * x[3]])
F = sp.Rational(1, 2) * sum(p ** 2 for p in Pnl)
H0 = sp.hessian(F, x).subs({v: 0 for v in x})
J0 = Pnl.jacobian(x).subs({v: 0 for v in x})
check("nonlinear Hessian equals pullback at outer critical point", H0 == J0.T * J0)
check("nonlinear control respects channel-rank ceiling", H0.rank() <= J0.rank())
check("full rank requires at least seven channels", DATA["theorem"]["full_rank_requirement"] == "m>=7")
check("the theorem does not construct source ownership", DATA["decision"]["seven_channels_are_sufficient_without_source_ownership"] is False)

assert passed == 20
print("RESULT: PASS 20/20")
