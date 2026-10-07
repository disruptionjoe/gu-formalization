#!/usr/bin/env python3
"""Data-mutation probe for K1351."""
import copy, json
from pathlib import Path

D = json.loads((Path(__file__).resolve().parents[2] / "lab/process/k1351-split-d7-character-obstruction.json").read_text())

def validate(x):
    errors = []
    p, c, q = x["perfectness_control"], x["character_theorem"], x["decision"]
    if "dimension 91" not in p["lie_algebra"]: errors.append("dimension")
    if "42" not in p["cartan_counts"] or "49" not in p["cartan_counts"]: errors.append("cartan counts")
    if "[g,g]=g" not in p["conclusion"]: errors.append("perfectness")
    if "d chi=0" not in c["perfectness_effect"]: errors.append("differential")
    if "identically one" not in c["connectedness_effect"]: errors.append("connectedness")
    if not q["lie_algebra_perfect"]: errors.append("decision perfectness")
    if q["connected_group_nontrivial_u1_character_exists"]: errors.append("character overclaim")
    if q["direct_full_group_abelianization_supplies_k1346_u1"]: errors.append("quotient overclaim")
    if q["u1_subgroup_after_stabilizer_or_compact_selection_excluded"]: errors.append("scope overreach")
    return errors

assert not validate(D), validate(D)
mutations = [
    ("dimension", lambda x: x["perfectness_control"].__setitem__("lie_algebra", "dimension 90")),
    ("compact count", lambda x: x["perfectness_control"].__setitem__("cartan_counts", "41 plus 49")),
    ("perfectness", lambda x: x["perfectness_control"].__setitem__("conclusion", "unknown")),
    ("differential", lambda x: x["character_theorem"].__setitem__("perfectness_effect", "nonzero")),
    ("connectedness", lambda x: x["character_theorem"].__setitem__("connectedness_effect", "unknown")),
    ("decision perfectness", lambda x: x["decision"].__setitem__("lie_algebra_perfect", False)),
    ("character overclaim", lambda x: x["decision"].__setitem__("connected_group_nontrivial_u1_character_exists", True)),
    ("quotient overclaim", lambda x: x["decision"].__setitem__("direct_full_group_abelianization_supplies_k1346_u1", True)),
    ("scope overreach", lambda x: x["decision"].__setitem__("u1_subgroup_after_stabilizer_or_compact_selection_excluded", True)),
]
for i, (label, mutate) in enumerate(mutations, 1):
    x = copy.deepcopy(D); mutate(x); errors = validate(x)
    assert errors, f"mutation escaped: {label}"
    print(f"PASS {i:02d}: rejects {label} via [FAIL] {errors[0]}")
print("RESULT: PASS 9/9")
