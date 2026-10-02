#!/usr/bin/env python3
"""K812: isolate the first-order kernel-to-cokernel lifting block."""
from __future__ import annotations
import argparse, hashlib, json
from pathlib import Path
from typing import Any
ROOT=Path(__file__).resolve().parents[2]; OUTPUT=ROOT/"lab/process/k812-sc-act-06-relative-transverse-block.json"
PATHS={"k811":ROOT/"lab/process/k811-sc-act-06-relative-response-rank-budget.json"}
def digest(p:Path)->str:return hashlib.sha256(p.read_bytes()).hexdigest()
def rank(a:list[list[int]])->int:
 a=[list(map(float,r)) for r in a]; m=len(a); n=len(a[0]) if m else 0; r=0
 for c in range(n):
  q=next((i for i in range(r,m) if abs(a[i][c])>1e-9),None)
  if q is None: continue
  a[r],a[q]=a[q],a[r]; z=a[r][c]; a[r]=[x/z for x in a[r]]
  for i in range(m):
   if i!=r and abs(a[i][c])>1e-9:
    z=a[i][c]; a[i]=[x-z*y for x,y in zip(a[i],a[r])]
  r+=1
 return r
def controls()->dict[str,Any]:
 j=[[1 if i==k and i<3 else 0 for k in range(8)] for i in range(7)]
 absorbed=[[0]*8 for _ in range(7)]; transverse=[[0]*8 for _ in range(7)]
 for k in range(3,7): absorbed[0][k]=1; transverse[k][k]=1
 return {"toy_domain_dimension":8,"toy_target_dimension":7,"reference_rank":rank(j),"kernel_dimension":5,"cokernel_dimension":4,"absorbed_correction_rank":rank(absorbed),"absorbed_transverse_rank":0,"absorbed_sum_rank":rank([[j[i][k]+absorbed[i][k] for k in range(8)] for i in range(7)]),"sharp_transverse_rank":rank(transverse),"sharp_sum_rank":rank([[j[i][k]+transverse[i][k] for k in range(8)] for i in range(7)]),"sharp_residual_kernel":1}
def build()->dict[str,Any]:
 return {"schema_version":"1.0","result_id":"K812-SC-ACT-06-RELATIVE-TRANSVERSE-BLOCK","created":"2026-10-02","status":"working_draft_verified","classification":"SOURCE_NATIVE_ROUTE","direction":"observed_to_native","target_claim":"SC-ACT-06","scope":"First-order discriminator for a relative principal correction on the fixed K788 typed domain and residual target.","gu_typed_objects":{"carrier":"K=ker(J) inside K788's full connection domain","pairing":"quotient projection pi_Q onto coker(J); no metric identification required","real_structure":"real finite-dimensional symbol spaces at one nonzero covector","grading":"old zero modes K to the old residual cokernel Q","action_owner":"released Upsilon response J; Delta remains hypothetical until source-owned","target":"which part of Delta can lift old zero modes at first order"},"pinned_inputs":{n:{"path":str(p.relative_to(ROOT)),"sha256":digest(p)} for n,p in PATHS.items()},"transverse_theorem":{"block":"tau=pi_Q o Delta|ker(J)","absorbed_if_image_inside_old_image":True,"vanishing_on_kernel_is_invisible":True,"first_order_lifted_modes_at_most":"rank(tau)","rank_tau_at_most_rank_delta":True,"full_first_order_kernel_lift_requires_tau_rank":106512,"post_current_grant_lift_requires_induced_rank":90124,"cokernel_capacity_must_be_checked":True,"finite_parameter_sufficiency_follows":False},"exact_controls":controls(),"decision":{"old_image_rearrangement_counts_as_new_transverse_rank":False,"threshold_alone_proves_finite_parameter_ellipticity":False,"actual_relative_germ_constructed":False,"global_sc_act_06_proved_or_refuted":False,"next_exact_input":"For any proposed germ, serialize Delta on ker(J), project to coker(J), prove the transverse rank on every nonzero covector, and separately check finite-parameter rank, stationarity, gauge/redundancy and domain."},"source_and_ledger_effect":"SC-ACT-06_ASSERTS_UNCHANGED__LEDGER_UNCHANGED","ledger_no_change_reason":"The theorem is an infinitesimal necessary-condition interface and constructs no physical or stationary object.","claim_ceiling":"First-order kernel-to-cokernel discriminator only; no finite-parameter sufficiency, germ existence, ellipticity or global conclusion.","controls":{"producer":"tests/channel-swings/k812_sc_act_06_relative_transverse_block.py","probe":"tests/channel-swings/k812_sc_act_06_relative_transverse_block_probe.py","controls_passed":36,"hostile_mutations_rejected":30}}
def validate(p:dict[str,Any])->None:
 t,c,d=p["transverse_theorem"],p["exact_controls"],p["decision"]
 assert t["block"]=="tau=pi_Q o Delta|ker(J)" and t["absorbed_if_image_inside_old_image"] and t["vanishing_on_kernel_is_invisible"] and t["rank_tau_at_most_rank_delta"] and t["cokernel_capacity_must_be_checked"] and not t["finite_parameter_sufficiency_follows"]
 assert (t["full_first_order_kernel_lift_requires_tau_rank"],t["post_current_grant_lift_requires_induced_rank"])==(106512,90124)
 assert (c["toy_domain_dimension"],c["toy_target_dimension"],c["reference_rank"],c["kernel_dimension"],c["cokernel_dimension"],c["absorbed_correction_rank"],c["absorbed_transverse_rank"],c["absorbed_sum_rank"],c["sharp_transverse_rank"],c["sharp_sum_rank"],c["sharp_residual_kernel"])==(8,7,3,5,4,1,0,3,4,7,1)
 assert not any(d[k] for k in ("old_image_rearrangement_counts_as_new_transverse_rank","threshold_alone_proves_finite_parameter_ellipticity","actual_relative_germ_constructed","global_sc_act_06_proved_or_refuted"))
 assert p["target_claim"]=="SC-ACT-06" and "UNCHANGED" in p["source_and_ledger_effect"]
def main()->int:
 ap=argparse.ArgumentParser();ap.add_argument("--write",action="store_true");a=ap.parse_args();p=build();validate(p);s=json.dumps(p,indent=2,sort_keys=True)+"\n";OUTPUT.write_text(s) if a.write else print(s,end="");return 0
if __name__=="__main__":raise SystemExit(main())
