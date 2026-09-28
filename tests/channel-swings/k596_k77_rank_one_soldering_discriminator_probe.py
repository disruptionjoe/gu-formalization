#!/usr/bin/env python3
"""Independent controls and hostile mutations for K596."""

from __future__ import annotations
import copy, json
from k596_k77_rank_one_soldering_discriminator import build


def controls(p):
    t,c,a,d=p["theorem"],p["exact_controls"],p["existing_candidate_audit"],p["decision"]
    return [
        p["classification"]=="BRIDGE_OR_SEMANTIC_BOUNDARY", p["direction"]=="observed_to_native",
        "Pi_target C-C Pi_source" in t["typed_square_defect"], t["nonzero_scalar_is_not_a_soldering"] is True,
        t["actual_owned_vectors_required"] is True, len(c["rows"])==4,
        c["both_K444_arrow_types_exercised"] is True, c["same_half_rows_zero"] is True,
        c["cross_half_rows_rank_one"] is True, c["nonzero_K594_coefficients_replayed"]==["8736","-56/3"],
        a["physical_soldering_observation_rank"]==10, a["physical_chain_owns_K441_rank512_carrier"] is False,
        a["second_observation_jets_own_K589_degree_arrows"] is False,
        a["K594_action_Riesz_on_K441_pairing_serialized"] is False,
        a["existing_candidate_releases_actual_K444_square"] is False,
        d["conditional_rank_one_discriminator_emitted"] is True, d["actual_action_owned_soldering_constructed"] is False,
        d["K590_nonfactorized_square_test_released"] is False, d["K590_factorized_completion_retracted"] is False,
        d["selected_source_action_rejected"] is False, p["source_and_ledger_effect"]=="none", p["target_claim"]=="NONE-NOT-A-KILL",
    ]


def set_path(p,path,value):
    x=p
    for key in path[:-1]: x=x[key]
    x[path[-1]]=value


def main():
    p=build(); assert all(controls(p))
    muts=[
        (("classification",),"SUPPORTED"),(("direction",),"native_to_observed"),
        (("theorem","typed_square_defect"),"commutator"),(("theorem","nonzero_scalar_is_not_a_soldering"),False),
        (("theorem","actual_owned_vectors_required"),False),(("exact_controls","rows"),[]),
        (("exact_controls","both_K444_arrow_types_exercised"),False),(("exact_controls","same_half_rows_zero"),False),
        (("exact_controls","cross_half_rows_rank_one"),False),(("exact_controls","nonzero_K594_coefficients_replayed"),["0"]),
        (("existing_candidate_audit","physical_soldering_observation_rank"),9),
        (("existing_candidate_audit","physical_chain_owns_K441_rank512_carrier"),True),
        (("existing_candidate_audit","second_observation_jets_own_K589_degree_arrows"),True),
        (("existing_candidate_audit","K594_action_Riesz_on_K441_pairing_serialized"),True),
        (("existing_candidate_audit","existing_candidate_releases_actual_K444_square"),True),
        (("decision","conditional_rank_one_discriminator_emitted"),False),
        (("decision","actual_action_owned_soldering_constructed"),True),
        (("decision","K590_nonfactorized_square_test_released"),True),
        (("decision","K590_factorized_completion_retracted"),True),(("decision","selected_source_action_rejected"),True),
        (("source_and_ledger_effect",),"moved"),(("target_claim",),"SC-ACT-01"),
    ]
    rejected=0
    for path,value in muts:
        q=copy.deepcopy(p); set_path(q,path,value); rejected+=int(not all(controls(q)))
    assert rejected==len(muts)
    print(json.dumps({"controls_passed":len(controls(p)),"hostile_mutations_rejected":rejected},sort_keys=True)); return 0


if __name__=="__main__": raise SystemExit(main())
