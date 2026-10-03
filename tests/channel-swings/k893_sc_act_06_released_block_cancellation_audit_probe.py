#!/usr/bin/env python3
"""Hostile mutations for K893."""
import copy
from k893_sc_act_06_released_block_cancellation_audit import build,validate
def main():
 b=build();ms=[]
 for k,v in [("required_rank",8190),("equation","CG=HG")]:m=copy.deepcopy(b);m["cancellation_target"][k]=v;ms.append(m)
 for k,v in [("released_action_owned_candidate_count",2),("released_action_owned_passing_count",1),("unbuilt_source_silent_candidate_count",0),("unowned_formal_control_passing_count",0),("current_owned_cancellation_rank",8191),("current_owned_rank_deficit",0)]:m=copy.deepcopy(b);m["inventory_result"][k]=v;ms.append(m)
 m=copy.deepcopy(b);m["inventory_result"]["all_future_action_blocks_exhausted"]=True;ms.append(m)
 for k in ["current_released_owned_packet_restores_descent","formal_control_counts_as_action_completion","quotient_ranks_now_admissible"]:m=copy.deepcopy(b);m["decision"][k]=True;ms.append(m)
 m=copy.deepcopy(b);m["decision"]["formal_control_restores_descent"]=False;ms.append(m)
 m=copy.deepcopy(b);m["decision"]["new_owned_block_or_new_germ_still_open"]=False;ms.append(m)
 for idx,val in [(0,1),(1,1),(2,1),(4,8190)]:m=copy.deepcopy(b);m["candidate_rows"][idx]["cancellation_rank"]=val;ms.append(m)
 m=copy.deepcopy(b);m["candidate_rows"][4]["custody"]="action_owned";ms.append(m)
 m=copy.deepcopy(b);m["source_and_ledger_effect"]="SC-ACT-06_REFUTED";ms.append(m)
 assert len(ms)==20
 n=0
 for m in ms:
  try:validate(m)
  except AssertionError:n+=1
 assert n==20
 print("K893 hostile probe: rejected 20/20 mutations")
if __name__=="__main__":main()
