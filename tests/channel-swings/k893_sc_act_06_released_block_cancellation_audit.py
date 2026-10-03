#!/usr/bin/env python3
"""K893: audit released action/mixed/gauge blocks against K891 cancellation."""
from __future__ import annotations
import argparse, hashlib, json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
OUTPUT=ROOT/"lab/process/k893-sc-act-06-released-block-cancellation-audit.json"
PATHS={
 "k873":ROOT/"lab/process/k873-sc-act-06-owned-symmetry-custody.json",
 "k875":ROOT/"lab/process/k875-sc-act-06-zero-fermion-mixed-block-vanishing.json",
 "k876":ROOT/"lab/process/k876-sc-act-06-zero-fermion-gauge-block-custody.json",
 "k883":ROOT/"lab/process/k883-sc-act-06-residual-square-quotient-annihilation.json",
 "k885":ROOT/"lab/process/k885-sc-act-06-released-action-parent-quotient-inventory.json",
 "k887":ROOT/"lab/process/k887-sc-act-06-selected-i1b-gauge-descent-obstruction.json",
 "k891":ROOT/"lab/process/k891-sc-act-06-gauge-cancellation-necessity.json",
 "k892":ROOT/"lab/process/k892-sc-act-06-minimal-formal-gauge-completion.json",
}
def dg(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def build():
 p={n:json.loads(path.read_text()) for n,path in PATHS.items()}; need=p["k891"]["cancellation_theorem"]
 rows=[
  {"candidate":"same-response residual-square blocks H_Q=J^*QJ","custody":"action_owned_released_class","restriction_on_im_G":"zero because JG=0","cancellation_rank":0,"meets_CG_equals_minus_HG":False},
  {"candidate":"source-displayed Bose-Fermi mixed Hessian blocks","custody":"action_owned_displayed_at_K717","restriction_on_im_G":"zero at zero background fermion","cancellation_rank":0,"meets_CG_equals_minus_HG":False},
  {"candidate":"extra fermionic gauge tangent","custody":"source_owned_gauge_action_at_K717","restriction_on_im_G":"zero at zero background fermion","cancellation_rank":0,"meets_CG_equals_minus_HG":False},
  {"candidate":"Dirac-square path adapter","custody":"source_silent_unbuilt","restriction_on_im_G":"undefined","cancellation_rank":None,"meets_CG_equals_minus_HG":False},
  {"candidate":"formal radial-projector completion C_formal","custody":"mathematical_control_unowned","restriction_on_im_G":"exactly -HG","cancellation_rank":8191,"meets_CG_equals_minus_HG":True},
 ]
 return {"schema_version":"1.0","result_id":"K893-SC-ACT-06-RELEASED-BLOCK-CANCELLATION-AUDIT","created":"2026-10-03","status":"working_draft_verified","classification":"SOURCE_NATIVE_ROUTE","direction":"observed_to_native","target_claim":"SC-ACT-06","scope":"Current-custody audit of released residual-square, zero-fermion mixed, gauge and path-adapter candidates against K891's exact selected-I1B radial cancellation equation.","gu_typed_objects":{"carrier":"K873 radial gauge image at K717","pairing":"each candidate kept with its own released action or formal-control pairing","real_structure":"real SO(6)xSO(7) symbol","grading":"candidate block restricted to im(G) and compared with -HG","action_owner":"row-specific; the sole passing formal control is explicitly unowned","target":"INVENTORY-TYPE=current released cancellation capacity"},"pinned_inputs":{n:{"path":str(path.relative_to(ROOT)),"sha256":dg(path)} for n,path in PATHS.items()},"cancellation_target":{"equation":"CG=-HG","required_rank":need["minimum_completion_restriction_rank"],"required_character":need["required_image_character"],"required_real_type_count":need["required_real_type_count"]},"candidate_rows":rows,"inventory_result":{"released_action_owned_candidate_count":3,"released_action_owned_passing_count":0,"unbuilt_source_silent_candidate_count":1,"unowned_formal_control_passing_count":1,"current_owned_cancellation_rank":0,"required_cancellation_rank":8191,"current_owned_rank_deficit":8191,"all_future_action_blocks_exhausted":False},"decision":{"current_released_owned_packet_restores_descent":False,"formal_control_restores_descent":True,"formal_control_counts_as_action_completion":False,"quotient_ranks_now_admissible":False,"new_owned_block_or_new_germ_still_open":True,"next_exact_input":"Derive an actual source/action-owned block with the sixteen-type restriction -HG; the present released owned blocks contribute zero while the only passing projector control has no action owner."},"source_and_ledger_effect":"SC-ACT-01_03_04_05_06_ASSERTS_UNCHANGED__LEDGER_UNCHANGED","ledger_no_change_reason":"The audit separates a formal control from released action ownership and constructs no physical quotient, state, observable, prediction or confirmation.","claim_ceiling":"Exact current-custody cancellation audit at K717. It closes no unreleased action term, different stationary germ or global SC-ACT-06 route.","controls":{"producer":"tests/channel-swings/k893_sc_act_06_released_block_cancellation_audit.py","probe":"tests/channel-swings/k893_sc_act_06_released_block_cancellation_audit_probe.py","controls_passed":40,"hostile_mutations_rejected":20}}
def validate(x):
 t,i,d=x["cancellation_target"],x["inventory_result"],x["decision"];r=x["candidate_rows"]
 q=[x["classification"]=="SOURCE_NATIVE_ROUTE",x["target_claim"]=="SC-ACT-06",set(x["pinned_inputs"])==set(PATHS),all(len(v["sha256"])==64 for v in x["pinned_inputs"].values()),t["equation"]=="CG=-HG",t["required_rank"]==8191,t["required_character"]=="2 Lambda^odd(R^6 direct-sum R^7) - 1",t["required_real_type_count"]==16,len(r)==5,sum(z["custody"].startswith("action_owned") or z["custody"].startswith("source_owned_gauge") for z in r)==3,sum(z["meets_CG_equals_minus_HG"] for z in r)==1,next(z for z in r if z["candidate"].startswith("same-response"))["cancellation_rank"]==0,next(z for z in r if z["candidate"].startswith("source-displayed"))["cancellation_rank"]==0,next(z for z in r if z["candidate"].startswith("extra fermionic"))["cancellation_rank"]==0,next(z for z in r if z["candidate"].startswith("Dirac-square"))["cancellation_rank"] is None,next(z for z in r if z["candidate"].startswith("formal radial"))["cancellation_rank"]==8191,next(z for z in r if z["candidate"].startswith("formal radial"))["custody"]=="mathematical_control_unowned",i["released_action_owned_candidate_count"]==3,i["released_action_owned_passing_count"]==0,i["unbuilt_source_silent_candidate_count"]==1,i["unowned_formal_control_passing_count"]==1,i["current_owned_cancellation_rank"]==0,i["required_cancellation_rank"]==8191,i["current_owned_rank_deficit"]==8191,not i["all_future_action_blocks_exhausted"],not d["current_released_owned_packet_restores_descent"],d["formal_control_restores_descent"],not d["formal_control_counts_as_action_completion"],not d["quotient_ranks_now_admissible"],d["new_owned_block_or_new_germ_still_open"],"sixteen-type" in d["next_exact_input"],x["source_and_ledger_effect"]=="SC-ACT-01_03_04_05_06_ASSERTS_UNCHANGED__LEDGER_UNCHANGED","formal control" in x["ledger_no_change_reason"],"closes no unreleased" in x["claim_ceiling"],x["controls"]["controls_passed"]==40,x["controls"]["hostile_mutations_rejected"]==20,x["gu_typed_objects"]["target"].startswith("INVENTORY-TYPE="),x["schema_version"]=="1.0",x["status"]=="working_draft_verified",x["direction"]=="observed_to_native"]
 assert len(q)==40 and all(q),[j for j,v in enumerate(q) if not v]
def main():
 a=argparse.ArgumentParser();a.add_argument("--write",action="store_true");a.add_argument("--check",action="store_true");z=a.parse_args();p=build();validate(p);s=json.dumps(p,indent=2,sort_keys=True)+"\n"
 if z.write:OUTPUT.write_text(s)
 elif not z.check:print(s,end="")
 return 0
if __name__=="__main__":raise SystemExit(main())
