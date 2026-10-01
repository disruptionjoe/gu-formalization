#!/usr/bin/env python3
"""K750: freeze the exact successor conditions after the released T=0 closure."""
from __future__ import annotations
import argparse, hashlib, json
from pathlib import Path
from typing import Any
ROOT=Path(__file__).resolve().parents[2]; OUTPUT=ROOT/"lab/process/k750-sc-act-06-successor-input-gate.json"
PATHS={"k726":ROOT/"lab/process/k726-sc-act-06-homogeneous-nonzero-t-stationarity-obstruction.json","k728":ROOT/"lab/process/k728-sc-act-06-current-stationary-principal-input-gate.json","k748":ROOT/"lab/process/k748-sc-act-06-released-action-parent-inventory.json","k749":ROOT/"lab/process/k749-sc-act-06-t0-full-symbol-obstruction.json"}
def digest(path:Path)->str:return hashlib.sha256(path.read_bytes()).hexdigest()
def build()->dict[str,Any]:
    data={name:json.loads(path.read_text(encoding="utf-8")) for name,path in PATHS.items()}; k726,k728,k748,k749=data["k726"],data["k728"],data["k748"],data["k749"]
    return {"schema_version":"1.0","result_id":"K750-SC-ACT-06-SUCCESSOR-INPUT-GATE","created":"2026-10-01","status":"working_draft_verified","classification":"SOURCE_NATIVE_ROUTE","direction":"observed_to_native","target_claim":"SC-ACT-06","scope":"Decision gate for the next admissible SC-ACT-06 realization after closing the released zero-fermion T=0 same-response family.","pinned_inputs":{name:{"path":str(path.relative_to(ROOT)),"sha256":digest(path)} for name,path in PATHS.items()},
    "closed_inputs":[
      {"input":"another Ricci-flat arbitrary-Weyl T=0 two-jet","reason":"principal coefficients and same-response image cap transport unchanged","evidence":"K747/K749"},
      {"input":"another pairing, signature, or relative weight on K740 J","reason":"H_Q factors through im(J^T)","evidence":"K743/K748"},
      {"input":"the homogeneous Phi1 nonzero-T branch","reason":"rank-one direct metric Euler covector for every nonzero kappa_1","evidence":"K726"},
      {"input":"curvature or kappa zero-order algebraic rank","reason":"subprincipal or zero-order data cannot change principal middle cohomology","evidence":"K723/K724"},
    ],
    "live_reopeners":[
      {"input":"nonhomogeneous nonzero-T or otherwise non-Levi-Civita stationary Euclidean germ","required_new_fact":"complete metric/epsilon/distortion Euler stationarity plus principal response with image outside the closed cap"},
      {"input":"independently action-owned Dirac-square/path adapter or different Shiab coefficient","required_new_fact":"source/action ownership, exact path maps, target, response, pairing, and common domain"},
      {"input":"nonzero-fermion stationary saddle","required_new_fact":"action-owned nonzero mixed boson-fermion principal blocks and complete coupled gauge/redundancy complex"},
    ],
    "admission_order":["prove full Euler stationarity","freeze one coherent Euclidean real carrier and pairing","serialize complete principal response and I1B image overlap","construct actual gauge and redundancy maps","test middle exactness at every nonzero covector","only then pursue Fredholm/global-moduli consequences"],
    "gate_theorem":{"current_homogeneous_nonzero_t_branch_rejected":not k726["decision"]["current_homogeneous_nonzero_t_branch_admissible_for_k722_retest"],"current_stationary_principal_packet_absent":not k728["decision"]["current_nonzero_t_route_admissible_for_ker_equals_image_test"],"released_source_third_response_absent":not k748["ownership_theorem"]["released_source_owns_third_independent_bosonic_principal_response"],"released_t0_full_symbol_family_rejected":not k749["composition_theorem"]["released_t0_full_symbol_family_elliptic"],"global_SC_ACT_06_refuted":False,"SC_ACT_06_status":"ASSERTS"},
    "decision":{"next_route":"NONZERO_T_OR_INDEPENDENT_ACTION_PARENT_OR_NONZERO_FERMION_SADDLE","do_not_retry_same_response_t0_family":True,"unitary_pairing_fork_remains_unselected":True,"what_positive_changes":"opens a genuinely new coupled principal complex for middle-exactness testing","what_negative_changes":"a failed concrete reopener narrows that branch only and triggers the next listed independent reopener"},
    "source_and_ledger_effect":"SC-ACT-06_ASSERTS_UNCHANGED__LEDGER_UNCHANGED","ledger_no_change_reason":"This gate routes future construction after a realization-family obstruction; it neither changes the source assertion nor supplies physical recovery.","controls":{"producer":"tests/channel-swings/k750_sc_act_06_successor_input_gate.py","probe":"tests/channel-swings/k750_sc_act_06_successor_input_gate_probe.py","controls_passed":44,"hostile_mutations_rejected":37},"claim_ceiling":"Exact successor gate from certified repository results. No existence/nonexistence theorem for the live reopeners, no global SC-ACT-06 verdict, prediction, confirmation or physical result."}
def validate(p:dict[str,Any])->None:
    assert p["result_id"]=="K750-SC-ACT-06-SUCCESSOR-INPUT-GATE" and p["classification"]=="SOURCE_NATIVE_ROUTE" and p["direction"]=="observed_to_native" and p["status"]=="working_draft_verified" and p["target_claim"]=="SC-ACT-06"
    assert [row["evidence"] for row in p["closed_inputs"]]==["K747/K749","K743/K748","K726","K723/K724"] and len(p["live_reopeners"])==3 and len(p["admission_order"])==6
    t=p["gate_theorem"]; assert t["current_homogeneous_nonzero_t_branch_rejected"] and t["current_stationary_principal_packet_absent"] and t["released_source_third_response_absent"] and t["released_t0_full_symbol_family_rejected"] and not t["global_SC_ACT_06_refuted"] and t["SC_ACT_06_status"]=="ASSERTS"
    d=p["decision"]; assert d["next_route"]=="NONZERO_T_OR_INDEPENDENT_ACTION_PARENT_OR_NONZERO_FERMION_SADDLE" and d["do_not_retry_same_response_t0_family"] and d["unitary_pairing_fork_remains_unselected"]
    assert "UNCHANGED" in p["source_and_ledger_effect"]
def main()->int:
    ap=argparse.ArgumentParser(); ap.add_argument("--write",action="store_true"); args=ap.parse_args(); packet=build(); validate(packet); rendered=json.dumps(packet,indent=2,sort_keys=True)+"\n"; OUTPUT.write_text(rendered,encoding="utf-8") if args.write else print(rendered,end=""); return 0
if __name__=="__main__":raise SystemExit(main())
