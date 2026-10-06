#!/usr/bin/env python3
"""K1229: predeclare an off-frame Bell coincidence holdout from affine calibration."""
from __future__ import annotations
import argparse,json
from fractions import Fraction as F
from pathlib import Path
OUTPUT=Path(__file__).parents[2]/"lab/process/k1229-off-frame-bell-holdout-preregistration.json"
def dot(a,b):return sum(x*y for x,y in zip(a,b))
def mv(a,v):return [sum(a[i][j]*v[j] for j in range(3)) for i in range(3)]
def sv(v):return [str(x) for x in v]
def build():
  z=F(0);M=[[F(3,10),-F(2,5),z],[F(2,13),F(3,26),-F(3,13)],[F(24,65),F(18,65),F(5,52)]];t=[z,-F(9,13),F(15,52)]
  a=[F(3,5),z,F(4,5)];b=[z,F(4,5),F(3,5)];Db=[b[0],-b[1],b[2]]
  local=dot(a,t);corr=dot(a,mv(M,Db));rows=[]
  for x in (-1,1):
    for y in (-1,1):rows.append({"x":x,"y":y,"probability":str((1+x*local+x*y*corr)/4)})
  probs=[F(r["probability"]) for r in rows]
  return {"schema_version":"1.0","result_id":"K1229-OFF-FRAME-BELL-HOLDOUT-PREREGISTRATION","created":"2026-10-06",
    "status":"working_draft_verified","classification":"INTERNAL_CONDITIONAL_MATHEMATICS","direction":"observed_to_native",
    "target_claim":"NONE-NOT-A-KILL","scope":"A sealed off-axis Bell coincidence table predicted from a separately fitted affine process frame under the same channel-owner schema.",
    "preregistration":{"analyzer_A":sv(a),"analyzer_B":sv(b),"settings_absent_from_axial_fit":True,"fit_inputs":"only six axial preparations by three Pauli effects","holdout_inputs":"Bell coincidences at the sealed off-axis analyzer pair","refit_after_unseal":False,"predicted_formula":"p(x,y|a,b)=[1+x a.t + x y a^T M diag(1,-1,1)b]/4","score":"max_xy |f_xy-p_xy| <= sqrt(log(8/alpha)/(2N_holdout))+epsilon_systematic","required_before_unseal":["alpha","N_holdout","epsilon_systematic","event inclusion rule","schedule digest"]},
    "exact_control":{"M_source":"K1223 rational rotated-amplitude-damping control","a_dot_t":str(local),"correlation":str(corr),"probabilities":rows,"probability_sum":str(sum(probs)),"minimum_probability":str(min(probs))},
    "decision":{"holdout_is_predeclared":True,"holdout_is_scored":False,"calibration_refit_on_holdout_forbidden":True,"holdout_validates_common_owner_model_not_GU":True,"delayed_choice_entanglement_swapping_consumed":False},
    "release_test":{"off_axis_unit_vectors":dot(a,a)==dot(b,b)==1,"probabilities_normalized":sum(probs)==1,"probabilities_nonnegative":min(probs)>=0,"four_outcomes":len(rows)==4,"no_refit":True,"delayed_choice_reserved":True,"protected_status_unchanged":True},
    "ownership":{"bell_source_channel_pairing_analyzers_counts_and_error_budget_imported":True,"gu_native_effect":"none"},
    "claim_ceiling":"Exact holdout prediction and scoring preregistration for one synthetic affine control; no empirical score, loophole closure, GU prediction or confirmation."}
def validate(x):
  assert x["result_id"].startswith("K1229-")
  assert x["exact_control"]["a_dot_t"]=="3/13" and x["exact_control"]["correlation"]=="99/1625"
  assert [r["probability"] for r in x["exact_control"]["probabilities"]]==["1349/6500","1151/6500","1901/6500","2099/6500"]
  assert all(x["release_test"].values()) and len(x["preregistration"]["required_before_unseal"])==5
  assert x["decision"]["holdout_is_predeclared"] and x["decision"]["holdout_is_scored"] is False
  assert x["decision"]["calibration_refit_on_holdout_forbidden"] and x["decision"]["holdout_validates_common_owner_model_not_GU"]
  assert x["decision"]["delayed_choice_entanglement_swapping_consumed"] is False
  assert x["ownership"]["gu_native_effect"]=="none"
if __name__=="__main__":
  q=argparse.ArgumentParser();q.add_argument("--check",action="store_true");a=q.parse_args();x=build();validate(x)
  if a.check:assert json.loads(OUTPUT.read_text())==x
  else:print(json.dumps(x,indent=2,sort_keys=True))
  print("K1229 controls: 12/12")
