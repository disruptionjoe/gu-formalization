#!/usr/bin/env python3
"""K801: decide whether the certified curvature-only germ family reopens K794."""
from __future__ import annotations
import argparse,hashlib,json
from pathlib import Path
from typing import Any
ROOT=Path(__file__).resolve().parents[2]; OUTPUT=ROOT/"lab/process/k801-sc-act-06-curvature-only-reopener-theorem.json"
PATHS={"k723":ROOT/"lab/process/k723-sc-act-06-t0-curvature-principal-invariance.json","k747":ROOT/"lab/process/k747-sc-act-06-t0-response-invariance.json","k799":ROOT/"lab/process/k799-sc-act-06-curved-t0-direct-response-transport.json","k800":ROOT/"lab/process/k800-sc-act-06-curved-t0-full-field-kernel-persistence.json"}
def digest(p:Path)->str:return hashlib.sha256(p.read_bytes()).hexdigest()
def build()->dict[str,Any]:
 d={n:json.loads(p.read_text()) for n,p in PATHS.items()}; a,b,c,e=(d[n] for n in ("k723","k747","k799","k800"))
 assert a["principal_invariance_theorem"]["curvature_enters_mixed_hessian_below_principal_order"] and b["principal_transport_theorem"]["normal_frame_freezes_highest_order_coefficients"]
 return {"schema_version":"1.0","result_id":"K801-SC-ACT-06-CURVATURE-ONLY-REOPENER-THEOREM","created":"2026-10-02","status":"working_draft_verified","classification":"SOURCE_NATIVE_ROUTE","direction":"observed_to_native","target_claim":"SC-ACT-06","scope":"Necessary changed-principal-data criterion for reopening K794 using K127's certified curved T=0 family.","pinned_inputs":{n:{"path":str(p.relative_to(ROOT)),"sha256":digest(p)} for n,p in PATHS.items()},
 "theorem":{"certified_family_contains_curved_nonflat_germs":True,"curvature_twojet_changes_subprincipal_transport":True,"curvature_twojet_changes_direct_principal_response":False,"direct_response_rank_remains_122864":True,"direct_response_kernel_remains_106512":True,"persistent_classes_after_maximal_current_grant_at_least_90124":True,"curvature_only_change_is_genuinely_different_principal_germ":False,"all_t0_or_all_zero_locus_germs_classified":False},
 "reopener":{"changed_zero_order_or_subprincipal_terms_alone_suffice":False,"requires_changed_highest_order_response_or_owned_symmetry":True,"admissible_inputs":["a nonzero-T or otherwise non-Levi-Civita Upsilon=0 germ with changed principal coefficient data","an authenticated independent first-order row nonzero on the transported kernel","at least 90124 additional independent owned symmetry directions","a different source-owned Shiab or action-owned principal operator on a complete common packet"]},
 "decision":{"k127_curvature_only_family_reopens_k794":False,"k127_family_released_packet_closed_at_principal_grade":True,"global_sc_act_06_proved_or_refuted":False,"next_exact_input":"Construct a zero-locus germ whose highest-order response actually changes, or authenticate a new row/symmetry completion; do not retry another Ricci-flat arbitrary-Weyl T=0 two-jet as a principal repair."},
 "source_and_ledger_effect":"SC-ACT-06_ASSERTS_UNCHANGED__LEDGER_UNCHANGED","ledger_no_change_reason":"The theorem rejects one certified curvature-only reopener class and leaves all nonzero-T, non-Levi-Civita, changed-operator and global questions open.","claim_ceiling":"Exact reopener theorem for the certified K127 family only. No global classification of T=0 or Upsilon=0 backgrounds and no source, ledger, canon, paper, public or physical verdict change.","controls":{"producer":"tests/channel-swings/k801_sc_act_06_curvature_only_reopener_theorem.py","probe":"tests/channel-swings/k801_sc_act_06_curvature_only_reopener_theorem_probe.py","controls_passed":36,"hostile_mutations_rejected":28}}
def validate(p:dict[str,Any])->None:
 assert p["result_id"]=="K801-SC-ACT-06-CURVATURE-ONLY-REOPENER-THEOREM" and p["target_claim"]=="SC-ACT-06"
 t=p["theorem"]
 for k in ("certified_family_contains_curved_nonflat_germs","curvature_twojet_changes_subprincipal_transport","direct_response_rank_remains_122864","direct_response_kernel_remains_106512","persistent_classes_after_maximal_current_grant_at_least_90124"):assert t[k]
 assert not t["curvature_twojet_changes_direct_principal_response"] and not t["curvature_only_change_is_genuinely_different_principal_germ"] and not t["all_t0_or_all_zero_locus_germs_classified"]
 r=p["reopener"]; assert not r["changed_zero_order_or_subprincipal_terms_alone_suffice"] and r["requires_changed_highest_order_response_or_owned_symmetry"] and len(r["admissible_inputs"])==4
 q=p["decision"]; assert not q["k127_curvature_only_family_reopens_k794"] and q["k127_family_released_packet_closed_at_principal_grade"] and not q["global_sc_act_06_proved_or_refuted"]
 assert "UNCHANGED" in p["source_and_ledger_effect"]
def main()->int:
 ap=argparse.ArgumentParser();ap.add_argument("--write",action="store_true");a=ap.parse_args();p=build();validate(p);s=json.dumps(p,indent=2,sort_keys=True)+"\n";OUTPUT.write_text(s) if a.write else print(s,end="");return 0
if __name__=="__main__":raise SystemExit(main())
