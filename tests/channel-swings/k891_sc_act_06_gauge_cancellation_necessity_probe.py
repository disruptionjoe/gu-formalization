#!/usr/bin/env python3
"""Hostile mutations for K891."""
import copy
from k891_sc_act_06_gauge_cancellation_necessity import build, validate

def main():
    base = build(); mutations = []
    for key, value in [("selected_i1b_defect_rank", 8190), ("minimum_completion_restriction_rank", 8190), ("required_total_dimension", 8190), ("required_real_type_count", 15), ("required_total_real_multiplicity", 54)]:
        m = copy.deepcopy(base); m["cancellation_theorem"][key] = value; mutations.append(m)
    for key in ["zero_restriction_completion_can_restore_descent", "rank_below_8191_can_restore_descent", "matching_rank_alone_proves_action_ownership", "matching_character_alone_proves_variational_ownership", "quotient_ranks_now_admissible"]:
        m = copy.deepcopy(base); m["decision"][key] = True; mutations.append(m)
    m = copy.deepcopy(base); m["cancellation_theorem"]["forced_restriction"] = "CG=HG"; mutations.append(m)
    m = copy.deepcopy(base); m["cancellation_theorem"]["equivariant_rows"][0]["required_cancellation_multiplicity"] = 4; mutations.append(m)
    m = copy.deepcopy(base); m["cancellation_theorem"]["equivariant_rows"][1]["required_cancellation_dimension"] += 1; mutations.append(m)
    m = copy.deepcopy(base); m["claim_ceiling"] = "constructs the missing action"; mutations.append(m)
    m = copy.deepcopy(base); m["source_and_ledger_effect"] = "SC-ACT-06_CONFIRMED"; mutations.append(m)
    m = copy.deepcopy(base); m["pinned_inputs"].pop("k888"); mutations.append(m)
    m = copy.deepcopy(base); m["classification"] = "CONVENTIONAL_ROUTE"; mutations.append(m)
    m = copy.deepcopy(base); m["target_claim"] = "SC-ACT-05"; mutations.append(m)
    m = copy.deepcopy(base); m["controls"]["controls_passed"] = 37; mutations.append(m)
    m = copy.deepcopy(base); m["controls"]["hostile_mutations_rejected"] = 19; mutations.append(m)
    rejected = 0
    for m in mutations:
        try: validate(m)
        except AssertionError: rejected += 1
    assert len(mutations) == 20 and rejected == 20
    print("K891 hostile probe: rejected 20/20 mutations")
if __name__ == "__main__": main()
