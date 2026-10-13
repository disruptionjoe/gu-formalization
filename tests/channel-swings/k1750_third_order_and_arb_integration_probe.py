#!/usr/bin/env python3
"""Hostile protected-state and grade mutations for K1750."""
import copy
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
D = json.loads((ROOT / "lab/process/k1750-third-order-and-arb-integration.json").read_text())


def accepts(x):
    c, p, z = x.get("bridge_census", {}), x.get("protected_state", {}), x.get("decision", {})
    return all([
        x.get("claim_id") == "K1750",
        "INTERNAL_STRUCTURAL_ONLY" in x.get("classification", ""),
        c.get("row_count") == 450,
        c.get("satisfied_count") == 371,
        c.get("missing_count") == 4,
        c.get("new_satisfied_rows") == ["K1746", "K1747", "K1748", "K1749", "K1750"],
        "ASSERTS" in p.get("source_claims", ""),
        "UNCERTAIN" in p.get("source_claims", ""),
        not p.get("canon_change", True),
        not p.get("public_posture_change", True),
        z.get("unique_third_order_chart_jet_proved", False),
        z.get("named_q_1_over_1024_finite_strength_ordering_arb_proved", False),
        not z.get("complete_local_branch_identified", True),
        not z.get("whole_two_radius_chart_ordered", True),
        not z.get("global_two_radius_optimizer_identified", True),
        "branch-and-bound" in x.get("next_condition", ""),
    ])


MUTATIONS = []
for path, value in [
    (("claim_id",), "K1749"),
    (("bridge_census", "row_count"), 449),
    (("bridge_census", "satisfied_count"), 370),
    (("bridge_census", "missing_count"), 3),
    (("bridge_census", "new_satisfied_rows"), ["K1750"]),
    (("protected_state", "source_claims"), "proved"),
    (("protected_state", "canon_change"), True),
    (("protected_state", "public_posture_change"), True),
    (("decision", "unique_third_order_chart_jet_proved"), False),
    (("decision", "named_q_1_over_1024_finite_strength_ordering_arb_proved"), False),
    (("decision", "complete_local_branch_identified"), True),
    (("decision", "whole_two_radius_chart_ordered"), True),
    (("decision", "global_two_radius_optimizer_identified"), True),
    (("next_condition",), "continue locally"),
    (("classification",), "PHYSICAL_CONFIRMED")
]:
    x = copy.deepcopy(D)
    cur = x
    for key in path[:-1]:
        cur = cur[key]
    cur[path[-1]] = value
    MUTATIONS.append(x)

assert accepts(D)
for i, item in enumerate(MUTATIONS, 1):
    assert not accepts(item), i
    print(f"PASS {i:02d}: rejected hostile mutation")
print(f"RESULT: PASS {len(MUTATIONS)}/{len(MUTATIONS)}")
