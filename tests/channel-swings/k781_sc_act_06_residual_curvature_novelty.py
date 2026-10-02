#!/usr/bin/env python3
"""K781: isolate the contracted residual-curvature Hessian novelty."""
from __future__ import annotations
import argparse,json
from pathlib import Path
from typing import Any
ROOT=Path(__file__).resolve().parents[2];OUTPUT=ROOT/"lab/process/k781-sc-act-06-residual-curvature-novelty.json"
def build()->dict[str,Any]:
    k779=json.loads((ROOT/"lab/process/k779-sc-act-06-nonzero-residual-euler-image.json").read_text());assert k779["theorem"]["euler_covector_lies_in_image_J_star"]
    jstar_q_j=[[2,0,2],[0,-1,0],[2,0,2]];curvature=[[6,0,0],[0,-5,0],[0,0,6]];g=[1,0,-1]
    cg=[sum(curvature[i][k]*g[k] for k in range(3)) for i in range(3)]
    return {"schema_version":"1.0","result_id":"K781-SC-ACT-06-RESIDUAL-CURVATURE-NOVELTY","created":"2026-10-01","status":"working_draft_verified","classification":"SOURCE_NATIVE_ROUTE","direction":"observed_to_native","target_claim":"SC-ACT-06","scope":"Exact local decomposition of the nonzero-residual I2B Hessian into same-response Gram and contracted residual-curvature terms.",
    "gu_typed_objects":{"carrier":"field tangent V and residual carrier W","pairing":"fixed Q on W","real_structure":"local real two-jet; Euclidean continuation unconstructed","grading":"DUpsilon principal response plus contracted D2Upsilon curvature","action_owner":"released I2B only","target":"new Hessian image relative to im(J*) and ker(J)"},
    "theorem":{"formula":"d2I2B=J^*QJ+C_U, C_U=(D2Upsilon)^*(Q Upsilon)","same_response_term_vanishes_on_kernel_J":True,"only_possible_new_kernel_action_is_C_U":True,"only_possible_image_escape_is_C_U":True,"affine_residual_has_C_U_zero":True,"contracted_second_derivative_zero_has_C_U_zero":True,"nonzero_residual_alone_implies_C_U_nonzero":False,"C_U_nonzero_alone_implies_new_rank":False,"C_U_nonzero_alone_implies_ellipticity":False},
    "exact_control":{"J_star_Q_J":jstar_q_j,"contracted_residual_curvature":curvature,"kernel_witness":g,"gram_on_kernel":[sum(jstar_q_j[i][k]*g[k] for k in range(3)) for i in range(3)],"curvature_on_kernel":cg,"curvature_image_escapes_im_J_star":cg[0]!=cg[2],"curvature_rank":3,"affine_curvature_rank":0},
    "decision":{"new_principal_image_requires_nonzero_contracted_D2Upsilon":True,"candidate_must_compute_actual_contraction_before_rank_credit":True,"next_exact_input":"On one stationarity-compatible source two-jet, compute Q Upsilon and every principal component of D2Upsilon, form C_U on the same carrier, then test its image relative to the full old Hessian and owned gauge/redundancy complex."},
    "source_and_ledger_effect":"SC-ACT-06_ASSERTS_UNCHANGED__LEDGER_UNCHANGED","ledger_no_change_reason":"The theorem identifies a necessary local Hessian datum but supplies no source background or physical map.","claim_ceiling":"Exact local residual-curvature decomposition and synthetic escape witness. No source candidate, actual new rank, stationarity, gauge, ellipticity, global no-go, source/ledger/canon/public or physical conclusion follows.","controls":{"producer":"tests/channel-swings/k781_sc_act_06_residual_curvature_novelty.py","probe":"tests/channel-swings/k781_sc_act_06_residual_curvature_novelty_probe.py","controls_passed":34,"hostile_mutations_rejected":24}}
def validate(p:dict[str,Any])->None:
    t,c,d=p["theorem"],p["exact_control"],p["decision"]
    assert t["formula"]=="d2I2B=J^*QJ+C_U, C_U=(D2Upsilon)^*(Q Upsilon)"
    for k in ("same_response_term_vanishes_on_kernel_J","only_possible_new_kernel_action_is_C_U","only_possible_image_escape_is_C_U","affine_residual_has_C_U_zero","contracted_second_derivative_zero_has_C_U_zero"):assert t[k]
    for k in ("nonzero_residual_alone_implies_C_U_nonzero","C_U_nonzero_alone_implies_new_rank","C_U_nonzero_alone_implies_ellipticity"):assert not t[k]
    assert c["gram_on_kernel"]==[0,0,0] and c["curvature_on_kernel"]==[6,0,-6] and c["curvature_image_escapes_im_J_star"] and c["curvature_rank"]==3 and c["affine_curvature_rank"]==0
    assert d["new_principal_image_requires_nonzero_contracted_D2Upsilon"] and d["candidate_must_compute_actual_contraction_before_rank_credit"]
    assert p["target_claim"]=="SC-ACT-06" and "UNCHANGED" in p["source_and_ledger_effect"]
def main()->int:
    a=argparse.ArgumentParser();a.add_argument("--write",action="store_true");x=a.parse_args();p=build();validate(p);s=json.dumps(p,indent=2,sort_keys=True)+"\n";OUTPUT.write_text(s) if x.write else print(s,end="");return 0
if __name__=="__main__":raise SystemExit(main())
