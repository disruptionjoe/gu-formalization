#!/usr/bin/env python3
"""Hostile mutations for K894."""
import copy
from k894_sc_act_06_action_owned_completion_boundary import build,validate
def main():
 b=build();ms=[]
 for k,v in [("required_radial_identity","CG=HG"),("required_restriction_rank",8190),("required_real_type_count",15),("quotient_rank_gate","now")]:m=copy.deepcopy(b);m["admission_boundary"][k]=v;ms.append(m)
 for k,v in [("formal_linear_completion_exists",False),("formal_completion_action_owned",True),("current_released_owned_cancellation_rank",8191),("required_cancellation_rank",8190),("forty_quotient_ranks_defined",True),("credited_quotient_repair_rows",1),("old_obstruction_real_type_count",39),("corrected_completion_gate_satisfied_rows",6),("corrected_completion_gate_total_rows",10),("SC_ACT_06_proved_or_refuted",True)]:m=copy.deepcopy(b);m["current_disposition"][k]=v;ms.append(m)
 for k,v in [("current_selected_i1b_complete_action_class_closed",True),("current_released_owned_packet_closed_as_completion",False),("abstract_descent_impossibility_claimed",True),("global_no_go_claimed",True)]:m=copy.deepcopy(b);m["decision"][k]=v;ms.append(m)
 m=copy.deepcopy(b);m["source_and_ledger_effect"]="SC-ACT-06_REFUTED";ms.append(m)
 m=copy.deepcopy(b);m["claim_ceiling"]="all completions excluded";ms.append(m)
 assert len(ms)==20
 n=0
 for m in ms:
  try:validate(m)
  except AssertionError:n+=1
 assert n==20
 print("K894 hostile probe: rejected 20/20 mutations")
if __name__=="__main__":main()
