#!/usr/bin/env python3
"""Data-mutation probe for K1356."""
import copy, json
from pathlib import Path
D = json.loads((Path(__file__).resolve().parents[2] / "lab/process/k1356-maximal-compact-circle-reduction.json").read_text())

def validate(x):
    c, p, q = x["compact_reduction"], x["positive_control"], x["decision"]
    e = []
    if "dimension 42" not in c["compact_algebra"]: e.append("dimension")
    if "2 pi" not in c["selected_circle"]: e.append("period")
    if "angle 2 alpha" not in c["cover_normalization"]: e.append("cover")
    if "-2" not in p["matrix_control"]: e.append("trace")
    if not q["explicit_maximal_compact_circle_constructed"]: e.append("construction")
    if not q["positive_circle_kinetic_control_exists"]: e.append("positivity")
    if q["full_G_invariance_preserved"]: e.append("symmetry overclaim")
    if q["source_selects_this_circle"]: e.append("source overclaim")
    if q["protected_status_change"]: e.append("protected movement")
    return e

assert not validate(D), validate(D)
mutations = [
    ("dimension", lambda x: x["compact_reduction"].__setitem__("compact_algebra", "dimension 41")),
    ("period", lambda x: x["compact_reduction"].__setitem__("selected_circle", "aperiodic")),
    ("cover", lambda x: x["compact_reduction"].__setitem__("cover_normalization", "unknown")),
    ("trace", lambda x: x["positive_control"].__setitem__("matrix_control", "zero")),
    ("construction", lambda x: x["decision"].__setitem__("explicit_maximal_compact_circle_constructed", False)),
    ("positivity", lambda x: x["decision"].__setitem__("positive_circle_kinetic_control_exists", False)),
    ("symmetry overclaim", lambda x: x["decision"].__setitem__("full_G_invariance_preserved", True)),
    ("source overclaim", lambda x: x["decision"].__setitem__("source_selects_this_circle", True)),
    ("protected movement", lambda x: x["decision"].__setitem__("protected_status_change", True)),
]
for i, (label, mutate) in enumerate(mutations, 1):
    x = copy.deepcopy(D); mutate(x); errors = validate(x)
    assert errors, label
    print(f"PASS {i:02d}: rejects {label} via [FAIL] {errors[0]}")
print("RESULT: PASS 9/9")
