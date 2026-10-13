#!/usr/bin/env python3
"""Hostile order, normalization and scope mutations for K1746."""
import copy
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
DATA = json.loads((ROOT / "lab/process/k1746-symmetric-fourteenth-order-fisher-law.json").read_text())


def accepts(data):
    law, decision = data.get("hermite_law", {}), data.get("decision", {})
    return all([
        data.get("claim_id") == "K1746",
        data.get("classification") == "INTERNAL_STRUCTURAL_ONLY",
        data.get("target_claim") == "NONE-NOT-A-KILL",
        "h_14/87178291200" in law.get("density_ratio", ""),
        "/5443200" in law.get("thirteenth_coefficient", ""),
        "h_14^2" in law.get("fourteenth_coefficient", ""),
        "/6227020800" in law.get("fourteenth_coefficient", ""),
        "probabilists' Hermite" in law.get("normalization", ""),
        decision.get("h_14_absent_at_thirteenth_order") is True,
        decision.get("new_moment_first_enters_at_fourteenth_order") == "h_14",
        not decision.get("uniform_remainder_for_moving_or_growing_seeds", True),
        not decision.get("finite_strength_optimizer_identified", True),
        "no complete branch" in data.get("scope_guard", ""),
    ])


mutations = []
for path, value in [
    (("claim_id",), "K1741"),
    (("classification",), "SOURCE_NATIVE_ROUTE"),
    (("target_claim",), "SC-META-53"),
    (("hermite_law", "density_ratio"), "through H_12"),
    (("hermite_law", "thirteenth_coefficient"), "0"),
    (("hermite_law", "fourteenth_coefficient"), "h_14"),
    (("hermite_law", "normalization"), "physicists' Hermite"),
    (("decision", "h_14_absent_at_thirteenth_order"), False),
    (("decision", "new_moment_first_enters_at_fourteenth_order"), "h_12"),
    (("decision", "uniform_remainder_for_moving_or_growing_seeds"), True),
    (("decision", "finite_strength_optimizer_identified"), True),
    (("scope_guard",), "complete global branch theorem"),
]:
    mutant = copy.deepcopy(DATA)
    cursor = mutant
    for key in path[:-1]:
        cursor = cursor[key]
    cursor[path[-1]] = value
    mutations.append(mutant)

assert accepts(DATA)
for i, mutant in enumerate(mutations, 1):
    assert not accepts(mutant), i
    print(f"PASS {i:02d}: rejected hostile mutation")
print(f"RESULT: PASS {len(mutations)}/{len(mutations)}")
