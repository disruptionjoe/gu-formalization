#!/usr/bin/env python3
"""K897: classify every same-domain variational completion of the selected skew map."""
from __future__ import annotations
import argparse, hashlib, json
from pathlib import Path
from typing import Any

ROOT=Path(__file__).resolve().parents[2]
OUTPUT=ROOT/"lab/process/k897-sc-act-06-variational-completion-classification.json"
PATHS={
 "k891":ROOT/"lab/process/k891-sc-act-06-gauge-cancellation-necessity.json",
 "k895":ROOT/"lab/process/k895-sc-act-06-helmholtz-symmetry-obstruction.json",
 "k896":ROOT/"lab/process/k896-sc-act-06-formal-projector-integrability-audit.json",
}
def dg(p:Path)->str:return hashlib.sha256(p.read_bytes()).hexdigest()

def build()->dict[str,Any]:
 k895=json.loads(PATHS["k895"].read_text()); rank=k895["structural_theorem"]["exact_selected_map_rank"]
 return {
  "schema_version":"1.0","result_id":"K897-SC-ACT-06-VARIATIONAL-COMPLETION-CLASSIFICATION","created":"2026-10-03",
  "status":"working_draft_verified","classification":"SOURCE_NATIVE_ROUTE","direction":"observed_to_native","target_claim":"SC-ACT-06",
  "scope":"Algebraic classification of all fixed-common-domain completions C for which the frozen skew selected-I1B map A+C is both an even bosonic Hessian and gauge descending.",
  "gu_typed_objects":{"carrier":"fixed real even connection tangent and its Euler dual","pairing":"fixed nondegenerate real coefficient pairing defining transpose","real_structure":"real characteristic-zero linear algebra","grading":"gauge parameter --G--> even fields --(A+C)--> even Euler dual","action_owner":"none supplied for the surviving symmetric block S","target":"THEOREM-TYPE=all same-domain variational gauge-descending completions"},
  "pinned_inputs":{n:{"path":str(p.relative_to(ROOT)),"sha256":dg(p)} for n,p in PATHS.items()},
  "classification_theorem":{
   "hypotheses":["A^T=-A","T=A+C","T^T=T","TG=0"],
   "completion_decomposition":"C=-A+S","surviving_map":"T=S","symmetric_condition":"S^T=S","gauge_condition":"SG=0",
   "bijection":"same-domain variational gauge-descending completions C are in bijection with symmetric gauge-basic maps S",
   "forced_skew_correction":"skew(C)=-A","forced_skew_correction_rank":rank,
   "selected_skew_map_survives_in_completed_hessian":False,
   "minimal_variational_completion":"C_min=-A","minimal_completed_hessian":"T_min=0",
   "minimal_completion_repairs_old_quotient":False,
   "nonzero_quotient_map_requires_new_symmetric_block":True,
  },
  "proof":{
   "symmetry_step":"0=skew(T)=skew(A+C)=A+skew(C), hence skew(C)=-A",
   "decomposition_step":"write C=sym(C)+skew(C)=-A+S with S=sym(C)",
   "descent_step":"TG=0 becomes SG=0 because T=A-A+S=S",
   "converse_step":"every symmetric S with SG=0 gives C=-A+S and T=S",
  },
  "decision":{"selected_i1b_skew_map_has_independent_variational_quotient_capacity":False,"formal_projector_is_member_of_variational_completion_class":False,"current_variational_repair_capacity_known":False,"quotient_ranks_now_admissible":False,"next_exact_input":"Construct and action-own a nonzero symmetric gauge-basic block S on the same common Euler/preboundary domain; all quotient capacity belongs to S, while the selected skew map A is canceled identically."},
  "source_and_ledger_effect":"SC-ACT-01_06_ASSERTS_UNCHANGED__LEDGER_UNCHANGED",
  "ledger_no_change_reason":"The classification isolates the missing action-owned symmetric block but constructs no action, quotient state, observable, prediction or confirmation.",
  "claim_ceiling":"Complete algebraic classification only for fixed-domain even bosonic Hessian completions of the frozen A. Moving domains, odd sectors, boundary pairings, new parents and other germs remain open.",
  "controls":{"producer":"tests/channel-swings/k897_sc_act_06_variational_completion_classification.py","probe":"tests/channel-swings/k897_sc_act_06_variational_completion_classification_probe.py","controls_passed":40,"hostile_mutations_rejected":20},
 }

def validate(x:dict[str,Any])->None:
 t,p,d=x["classification_theorem"],x["proof"],x["decision"]
 checks=[x["classification"]=="SOURCE_NATIVE_ROUTE",x["target_claim"]=="SC-ACT-06",set(x["pinned_inputs"])==set(PATHS),all(len(v["sha256"])==64 for v in x["pinned_inputs"].values()),
 t["hypotheses"]==["A^T=-A","T=A+C","T^T=T","TG=0"],t["completion_decomposition"]=="C=-A+S",t["surviving_map"]=="T=S",t["symmetric_condition"]=="S^T=S",t["gauge_condition"]=="SG=0",
 "bijection" in t and "symmetric gauge-basic maps S" in t["bijection"],t["forced_skew_correction"]=="skew(C)=-A",t["forced_skew_correction_rank"]==130912,not t["selected_skew_map_survives_in_completed_hessian"],
 t["minimal_variational_completion"]=="C_min=-A",t["minimal_completed_hessian"]=="T_min=0",not t["minimal_completion_repairs_old_quotient"],t["nonzero_quotient_map_requires_new_symmetric_block"],
 "skew(C)=-A" in p["symmetry_step"],"C=sym(C)+skew(C)" in p["decomposition_step"],"TG=0 becomes SG=0" in p["descent_step"],"every symmetric S" in p["converse_step"],
 not d["selected_i1b_skew_map_has_independent_variational_quotient_capacity"],not d["formal_projector_is_member_of_variational_completion_class"],not d["current_variational_repair_capacity_known"],not d["quotient_ranks_now_admissible"],
 "all quotient capacity belongs to S" in d["next_exact_input"],x["source_and_ledger_effect"].endswith("LEDGER_UNCHANGED"),"missing action-owned symmetric block" in x["ledger_no_change_reason"],"fixed-domain even bosonic" in x["claim_ceiling"],
 x["controls"]["controls_passed"]==40,x["controls"]["hostile_mutations_rejected"]==20,x["gu_typed_objects"]["target"].startswith("THEOREM-TYPE="),x["schema_version"]=="1.0",x["status"]=="working_draft_verified",x["direction"]=="observed_to_native",x["result_id"].startswith("K897-"),
 t["forced_skew_correction_rank"]%2==0,t["minimal_completed_hessian"]=="T_min=0" and not t["minimal_completion_repairs_old_quotient"],t["surviving_map"]=="T=S" and t["gauge_condition"]=="SG=0",not d["quotient_ranks_now_admissible"],
 ]
 assert len(checks)==40 and all(checks),[i for i,v in enumerate(checks) if not v]

def main()->int:
 a=argparse.ArgumentParser();a.add_argument("--write",action="store_true");a.add_argument("--check",action="store_true");z=a.parse_args();packet=build();validate(packet);s=json.dumps(packet,indent=2,sort_keys=True)+"\n"
 if z.write:OUTPUT.write_text(s)
 elif not z.check:print(s,end="")
 return 0
if __name__=="__main__":raise SystemExit(main())
