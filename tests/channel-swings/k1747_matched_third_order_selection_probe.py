#!/usr/bin/env python3
"""Hostile order, center, uniqueness and promotion mutations for K1747."""
import copy
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
DATA = json.loads((ROOT / "lab/process/k1747-matched-third-order-selection.json").read_text())


def accepts(data):
    pre = data.get("pre_flight", {})
    comp = data.get("matched_composition", {})
    boundary = data.get("selection_boundary", {})
    decision = data.get("decision", {})
    post = data.get("post_flight", {})
    return all([
        data.get("claim_id") == "K1747",
        data.get("classification") == "INTERNAL_STRUCTURAL_ONLY",
        "K1747 is not assumed" in pre.get("rederived_inputs", ""),
        "independent of delta=r_4 and theta=x_3" in comp.get("thirteen_halves_selection", ""),
        "(delta-delta_*)^2/120" in comp.get("seven_completed_square", ""),
        "(theta-theta_*)^2/5040" in comp.get("seven_completed_square", ""),
        "361.098949224460002" in comp.get("delta_star", ""),
        "-11274.244832460378296" in comp.get("theta_star", ""),
        "q^7 is the first" in boundary.get("first_theta_selector", ""),
        "x_4" in boundary.get("fourth_order", ""),
        decision.get("q_thirteen_halves_selects_theta") is False,
        decision.get("q_seven_is_first_theta_selector") is True,
        decision.get("third_order_invariant_jet_unique") is True,
        decision.get("complete_local_analytic_branch_unique") is False,
        decision.get("finite_strength_branch_certified") is False,
        decision.get("remote_or_singular_boundaries_excluded") is False,
        "Arbitrary x_4 paths" in post.get("counterexample_seam", ""),
        "u=q singular face" in data.get("scope_guard", ""),
    ])


mutations = []
for path, value in [
    (("claim_id",), "K1742"),
    (("classification",), "SOURCE_NATIVE_ROUTE"),
    (("pre_flight", "rederived_inputs"), "Assume K1747."),
    (("matched_composition", "thirteen_halves_selection"), "q^(13/2) selects theta"),
    (("matched_composition", "seven_completed_square"), "flat"),
    (("matched_composition", "delta_star"), "delta=0"),
    (("matched_composition", "theta_star"), "theta=0"),
    (("selection_boundary", "first_theta_selector"), "q^(13/2) is first"),
    (("selection_boundary", "fourth_order"), "complete branch"),
    (("decision", "q_thirteen_halves_selects_theta"), True),
    (("decision", "q_seven_is_first_theta_selector"), False),
    (("decision", "complete_local_analytic_branch_unique"), True),
    (("decision", "finite_strength_branch_certified"), True),
    (("decision", "remote_or_singular_boundaries_excluded"), True),
    (("post_flight", "counterexample_seam"), "No contrary path."),
    (("scope_guard",), "global all-seed finite-strength theorem"),
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
