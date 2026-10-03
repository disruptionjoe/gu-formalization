#!/usr/bin/env python3
"""Hostile mutations for K892."""
import copy
from k892_sc_act_06_minimal_formal_gauge_completion import build, validate
def main():
    b=build(); ms=[]
    for k,v in [("completion_restriction_rank",8190),("real_type_count",15),("definition","C_formal=H P_R"),("projector_on_gauge","P_R G=0"),("completed_restriction","(H+C_formal)G=HG")]: m=copy.deepcopy(b);m["formal_completion"][k]=v;ms.append(m)
    for k in ["rank_minimal_among_all_completions","formal_solution_exists","unique_on_radial_gauge_image"]: m=copy.deepcopy(b);m["formal_completion"][k]=False;ms.append(m)
    m=copy.deepcopy(b);m["formal_completion"]["unique_off_radial_gauge_image"]=True;ms.append(m)
    for k in b["ownership_fence"]: m=copy.deepcopy(b);m["ownership_fence"][k]=True;ms.append(m)
    for k in ["action_owned_completion_constructed","formal_control_may_be_credited_to_SC_ACT_06","quotient_ranks_now_admissible"]: m=copy.deepcopy(b);m["decision"][k]=True;ms.append(m)
    m=copy.deepcopy(b);m["source_and_ledger_effect"]="SC-ACT-06_CONFIRMED";ms.append(m)
    m=copy.deepcopy(b);m["pinned_inputs"].pop("k891");ms.append(m)
    assert len(ms)==20
    rejected=0
    for m in ms:
        try: validate(m)
        except AssertionError: rejected+=1
    assert rejected==20
    print("K892 hostile probe: rejected 20/20 mutations")
if __name__=="__main__": main()
