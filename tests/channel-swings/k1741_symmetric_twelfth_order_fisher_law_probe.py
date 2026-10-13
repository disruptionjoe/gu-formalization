#!/usr/bin/env python3
"""Hostile coefficient, normalization and scope mutations for K1741."""
import copy
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
DATA = json.loads((ROOT / "lab/process/k1741-symmetric-twelfth-order-fisher-law.json").read_text())


def accepts(data):
    law, decision = data.get("hermite_law", {}), data.get("decision", {})
    return all([
        data.get("claim_id") == "K1741",
        data.get("classification") == "INTERNAL_STRUCTURAL_ONLY",
        data.get("target_claim") == "NONE-NOT-A-KILL",
        "h_12/479001600" in law.get("density_ratio", ""),
        "-11[" in law.get("eleventh_coefficient", ""),
        "/302400" in law.get("eleventh_coefficient", ""),
        "h_12^2" in law.get("twelfth_coefficient", ""),
        "/39916800" in law.get("twelfth_coefficient", ""),
        "probabilists' Hermite" in law.get("normalization", ""),
        decision.get("new_moment_first_enters_at_twelfth_order") == "h_12",
        not decision.get("uniform_remainder_for_moving_or_growing_seeds", True),
        not decision.get("finite_strength_optimizer_identified", True),
        "singular chart boundaries" in data.get("scope_guard", ""),
    ])


mutations = []
for path, value in [
    (("claim_id",), "K1736"),
    (("classification",), "SOURCE_NATIVE_ROUTE"),
    (("target_claim",), "SC-META-53"),
    (("hermite_law", "density_ratio"), "through H_10"),
    (("hermite_law", "eleventh_coefficient"), "0"),
    (("hermite_law", "twelfth_coefficient"), "h_12"),
    (("hermite_law", "normalization"), "physicists' Hermite"),
    (("decision", "new_moment_first_enters_at_twelfth_order"), "h_10"),
    (("decision", "uniform_remainder_for_moving_or_growing_seeds"), True),
    (("decision", "finite_strength_optimizer_identified"), True),
    (("scope_guard",), "global all-seed theorem"),
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
