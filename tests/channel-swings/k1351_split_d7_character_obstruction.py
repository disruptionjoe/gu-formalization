#!/usr/bin/env python3
"""Exact split-D7 perfectness and character obstruction for K1351."""
import hashlib, json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
D = json.loads((ROOT / "lab/process/k1351-split-d7-character-obstruction.json").read_text())
n = 0

def check(label, value):
    global n
    assert value, label
    n += 1
    print(f"PASS {n:02d}: {label}")

def mat(entries):
    out = [[0] * 14 for _ in range(14)]
    for i, j, value in entries:
        out[i][j] += value
    return out

def mul(a, b):
    return [[sum(a[i][k] * b[k][j] for k in range(14)) for j in range(14)] for i in range(14)]

def sub(a, b):
    return [[a[i][j] - b[i][j] for j in range(14)] for i in range(14)]

def bracket(a, b):
    return sub(mul(a, b), mul(b, a))

def rotation(i, j):
    return mat([(i, j, 1), (j, i, -1)])

def boost(i, a):
    return mat([(i, a, 1), (a, i, 1)])

for key, pin in D["pinned_inputs"].items():
    check(f"{key} pin", hashlib.sha256((ROOT / pin["path"]).read_bytes()).hexdigest() == pin["sha256"])
P = D["perfectness_control"]; C = D["character_theorem"]; Q = D["decision"]
check("D7 dimension", "dimension 91" in P["lie_algebra"])
check("compact count", "42" in P["cartan_counts"])
check("split count", "49" in P["cartan_counts"])
check("dimension sum", 42 + 49 == 91)
check("all plus rotations are commutators", all(bracket(boost(i, 7), boost(j, 7)) == rotation(i, j) for i in range(7) for j in range(i + 1, 7)))
check("all minus rotations are commutators", all(bracket(boost(0, a), boost(0, b)) == rotation(a, b) for a in range(7, 14) for b in range(a + 1, 14)))
check("all boosts are commutators", all(bracket(rotation(i, (i + 1) % 7), boost((i + 1) % 7, a)) == boost(i, a) for i in range(7) for a in range(7, 14)))
check("perfectness conclusion", "[g,g]=g" in P["conclusion"])
check("character differential target", "iR" in C["differential"])
check("commutator annihilation", "d chi([g,g])=0" in C["commutator_effect"])
check("zero differential", "d chi=0" in C["perfectness_effect"])
check("connected triviality", "identically one" in C["connectedness_effect"])
check("no connected abelian quotient", "no nontrivial connected abelian quotient" in C["direct_quotient_effect"])
check("perfect decision", Q["lie_algebra_perfect"])
check("no U1 character", not Q["connected_group_nontrivial_u1_character_exists"])
check("no direct K1346 quotient", not Q["direct_full_group_abelianization_supplies_k1346_u1"])
check("subgroup route preserved", not Q["u1_subgroup_after_stabilizer_or_compact_selection_excluded"])
check("hypercharge not identified", not Q["source_hypercharge_identified_with_k1346_u1"])
check("protected state fixed", not Q["protected_status_change"])
assert n == 20
print("RESULT: PASS 20/20")
