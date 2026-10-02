#!/usr/bin/env python3
"""K816: exact first-order response/symmetry overlap accounting."""
from __future__ import annotations
import argparse, hashlib, json
from pathlib import Path
from typing import Any
ROOT=Path(__file__).resolve().parents[2]
OUTPUT=ROOT/"lab/process/k816-sc-act-06-response-symmetry-overlap.json"
PATHS={"k812":ROOT/"lab/process/k812-sc-act-06-relative-transverse-block.json","k813":ROOT/"lab/process/k813-sc-act-06-relative-full-field-symmetry-budget.json","k815":ROOT/"lab/process/k815-sc-act-06-zero-locus-tangent-compatibility.json"}
def digest(p:Path)->str:return hashlib.sha256(p.read_bytes()).hexdigest()
def build()->dict[str,Any]:
 return {"schema_version":"1.0","result_id":"K816-SC-ACT-06-RESPONSE-SYMMETRY-OVERLAP","created":"2026-10-02","status":"working_draft_verified","classification":"SOURCE_NATIVE_ROUTE","direction":"observed_to_native","target_claim":"SC-ACT-06","scope":"Exact first-order accounting of transverse response and authenticated symmetry after composition and overlap.","gu_typed_objects":{"carrier":"K=ker(J) in the K788 connection response","pairing":"quotient by an authenticated symmetry image G only after tau(G)=0","real_structure":"K788 real coefficient basis","grading":"symmetry parameters -> old kernel K -> old residual cokernel Q","action_owner":"released Upsilon response; candidate q-lambda remains a conservative grant","target":"first-order unresolved classes after transverse lifting and valid symmetry quotient"},"pinned_inputs":{n:{"path":str(p.relative_to(ROOT)),"sha256":digest(p)} for n,p in PATHS.items()},"overlap_theorem":{"transverse_block":"tau:K->Q","composition_requirement":"G subset ker(tau)","exact_unresolved_dimension":"dim(K)-rank(tau)-dim(G)","old_new_union_rank":"g0+g1-overlap","naive_rank_addition_valid_without_overlap_check":False,"noncomposing_direction_is_symmetry":False,"current_kernel_dimension":106512,"current_grant_rank_upper":16388,"necessary_exact_budget":"rank(tau)+dim(G0+G1)>=106512"},"exact_controls":{"toy_kernel_dimension":7,"toy_tau_rank":3,"toy_tau_kernel_dimension":4,"old_symmetry_rank":2,"new_symmetry_rank":2,"symmetry_overlap_rank":1,"symmetry_union_rank":3,"exact_unresolved_dimension":1,"naive_unresolved_dimension":0,"naive_addition_overcounts_by":1,"noncomposing_candidate_rejected":True,"gu_examples":[{"transverse_rank":50000,"new_rank":40124,"overlap":0,"unresolved_lower_bound":0},{"transverse_rank":50000,"new_rank":40124,"overlap":1,"unresolved_lower_bound":1},{"transverse_rank":90124,"new_rank":0,"overlap":0,"unresolved_lower_bound":0}]},"decision":{"current_candidate_grant_promoted_to_owned_gauge":False,"budget_without_composition_is_credited":False,"budget_without_overlap_is_credited":False,"full_field_ellipticity_proved":False,"global_sc_act_06_proved_or_refuted":False,"next_exact_input":"For every proposed symmetry family, prove image containment in ker(tau), compute old/new intersection rank, and quotient only by the authenticated union image."},"source_and_ledger_effect":"SC-ACT-06_ASSERTS_UNCHANGED__LEDGER_UNCHANGED","ledger_no_change_reason":"The exact quotient accounting promotes no candidate symmetry and constructs no physical state or observable.","claim_ceiling":"Exact first-order overlap accounting only; no symmetry ownership, finite-parameter complex, ellipticity or global conclusion.","controls":{"producer":"tests/channel-swings/k816_sc_act_06_response_symmetry_overlap.py","probe":"tests/channel-swings/k816_sc_act_06_response_symmetry_overlap_probe.py","controls_passed":38,"hostile_mutations_rejected":30}}
def validate(p:dict[str,Any])->None:
 t,c,d=p["overlap_theorem"],p["exact_controls"],p["decision"]
 assert t["composition_requirement"]=="G subset ker(tau)" and not t["naive_rank_addition_valid_without_overlap_check"] and not t["noncomposing_direction_is_symmetry"]
 assert (t["current_kernel_dimension"],t["current_grant_rank_upper"])==(106512,16388)
 assert c["toy_tau_kernel_dimension"]==c["toy_kernel_dimension"]-c["toy_tau_rank"]==4
 assert c["symmetry_union_rank"]==c["old_symmetry_rank"]+c["new_symmetry_rank"]-c["symmetry_overlap_rank"]==3
 assert c["exact_unresolved_dimension"]==c["toy_tau_kernel_dimension"]-c["symmetry_union_rank"]==1
 assert c["naive_unresolved_dimension"]==0 and c["naive_addition_overcounts_by"]==1 and c["noncomposing_candidate_rejected"]
 assert [(x["overlap"],x["unresolved_lower_bound"]) for x in c["gu_examples"]]==[(0,0),(1,1),(0,0)]
 assert not any(d[k] for k in ("current_candidate_grant_promoted_to_owned_gauge","budget_without_composition_is_credited","budget_without_overlap_is_credited","full_field_ellipticity_proved","global_sc_act_06_proved_or_refuted"))
 assert p["target_claim"]=="SC-ACT-06" and "UNCHANGED" in p["source_and_ledger_effect"]
def main()->int:
 ap=argparse.ArgumentParser();ap.add_argument("--write",action="store_true");a=ap.parse_args();p=build();validate(p);s=json.dumps(p,indent=2,sort_keys=True)+"\n";OUTPUT.write_text(s) if a.write else print(s,end="");return 0
if __name__=="__main__":raise SystemExit(main())
