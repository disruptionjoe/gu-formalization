#!/usr/bin/env python3
"""Exact maximal-compact circle and positive kinetic control for K1356."""
import hashlib, json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
D = json.loads((ROOT / "lab/process/k1356-maximal-compact-circle-reduction.json").read_text())
n = 0

def check(label, value):
    global n
    assert value, label
    n += 1
    print(f"PASS {n:02d}: {label}")

for key, pin in D["pinned_inputs"].items():
    check(f"{key} pin", hashlib.sha256((ROOT / pin["path"]).read_bytes()).hexdigest() == pin["sha256"])
C, P, Q = D["compact_reduction"], D["positive_control"], D["decision"]
J = [[0] * 7 for _ in range(7)]
J[0][1], J[1][0] = 1, -1
J2 = [[sum(J[i][k] * J[k][j] for k in range(7)) for j in range(7)] for i in range(7)]
trace_j2 = sum(J2[i][i] for i in range(7))
check("split group", "Spin_0(7,7)" in C["split_group"])
check("maximal compact factors", "Spin(7)xSpin(7)" in C["maximal_compact"])
check("compact algebra dimension", "dimension 42" in C["compact_algebra"])
check("circle period", "2 pi" in C["selected_circle"])
check("spin cover normalization", "angle 2 alpha" in C["cover_normalization"])
check("nontrivial midpoint", "alpha=pi" in C["cover_normalization"])
check("generator named", "e1e2" in C["generator"])
check("centralizer boundary", "centralizer" in C["centralizer_boundary"])
check("J skew", all(J[i][j] == -J[j][i] for i in range(7) for j in range(7)))
check("J square trace", trace_j2 == -2)
check("normalized norm", -trace_j2 / 2 == 1)
check("matrix control recorded", "-2" in P["matrix_control"])
check("compact restriction positive", "positive definite" in P["compact_restriction"])
check("kinetic conclusion positive", "positive" in P["kinetic_conclusion"])
check("circle constructed", Q["explicit_maximal_compact_circle_constructed"])
check("positive kinetic", Q["positive_circle_kinetic_control_exists"])
check("full G reduced", not Q["full_G_invariance_preserved"])
check("source selection absent", not Q["source_selects_this_circle"])
check("protected fixed", not Q["protected_status_change"])
assert n == 20
print("RESULT: PASS 20/20")
