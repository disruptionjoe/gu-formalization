#!/usr/bin/env python3
"""Exact controls for K1281."""
import json
from pathlib import Path

D = json.loads((Path(__file__).resolve().parents[2] / "lab/process/k1281-weighted-d7-parity-semigroup.json").read_text())
n = 0

def c(label, value):
    global n
    assert value, label
    n += 1
    print(f"PASS {n:02d}: {label}")

def monomials(weight):
    out = []
    for j in range(weight // 7 + 1):
        def walk(rem, parts, exps):
            if not parts:
                if rem == 0:
                    out.append((*exps, j))
                return
            w = parts[0]
            for a in range(rem // w + 1):
                walk(rem - a * w, parts[1:], (*exps, a))
        walk(weight - 7 * j, (2, 4, 6, 8, 10, 12), ())
    return out

c("id", D["result_id"] == "K1281-WEIGHTED-D7-PARITY-SEMIGROUP")
c("weights", D["theorem"]["generator_weights"] == [2, 4, 6, 8, 10, 12, 7])
for w in (7, 14, 21, 28, 35, 42):
    ms = monomials(w)
    c(f"weight {w} populated", bool(ms))
    c(f"weight {w} parity", all(m[-1] % 2 == w % 2 for m in ms))
c("weight 28 even", D["theorem"]["weight28_is_outer_even"] is True)
c("weight 21 odd", D["theorem"]["weight21_is_outer_odd"] is True)
assert n == 16
print("RESULT: PASS 16/16")
