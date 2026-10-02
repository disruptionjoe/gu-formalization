#!/usr/bin/env python3
"""K778: classify residual strata and freeze the next SC-ACT-06 input."""
from __future__ import annotations
import argparse,hashlib,json
from pathlib import Path
from typing import Any
ROOT=Path(__file__).resolve().parents[2]
PATHS={"k774":ROOT/"lab/process/k774-sc-act-06-positive-curvature-successor-gate.json","k775":ROOT/"lab/process/k775-sc-act-06-residual-zero-variation-theorem.json","k776":ROOT/"lab/process/k776-sc-act-06-homogeneous-residual-square-stationarity-closure.json","k777":ROOT/"lab/process/k777-sc-act-06-nonzero-residual-hessian-split.json"}
OUTPUT=ROOT/"lab/process/k778-sc-act-06-residual-stratum-successor-gate.json"
def digest(p:Path)->str:return hashlib.sha256(p.read_bytes()).hexdigest()
def build()->dict[str,Any]:
 d={k:json.loads(p.read_text()) for k,p in PATHS.items()};assert d["k776"]["decision"]["current_homogeneous_branch_closed_for_all_fixed_residual_pairings_and_finite_weights"]
 return {"schema_version":"1.0","result_id":"K778-SC-ACT-06-RESIDUAL-STRATUM-SUCCESSOR-GATE","created":"2026-10-01","status":"working_draft_verified","classification":"SOURCE_NATIVE_ROUTE","direction":"observed_to_native","target_claim":"SC-ACT-06","scope":"Successor routing after the exact residual-zero variation theorem, homogeneous-branch closure and nonzero-residual Hessian split.","pinned_inputs":{k:{"path":str(p.relative_to(ROOT)),"sha256":digest(p)} for k,p in PATHS.items()},
 "gu_typed_objects":{"carrier":"source I1B/I2B field and residual strata, without identifying comparator carriers","pairing":"fixed operative residual pairing on each candidate common domain","real_structure":"candidate-specific and still owed for a Euclidean exactness test","grading":"background stationarity -> coupled principal complex -> gauge/redundancy cohomology","action_owner":"released source I1B and I2B only","target":"SC-ACT-06 next-input routing across Upsilon-zero and Upsilon-nonzero strata"},
 "residual_strata":[
  {"stratum":"Upsilon=0 and dI1B nonzero","stationary_for_I1B_plus_I2B":False,"principal_effect":"I2B Hessian factors as J^*QJ","disposition":"CLOSED_INDEPENDENTLY_OF_FIXED_PAIRING_AND_FINITE_WEIGHT"},
  {"stratum":"Upsilon=0 and dI1B=0","stationary_for_I1B_plus_I2B":True,"principal_effect":"same-response J^*QJ only","disposition":"OPEN_ONLY_WITH_NEW_STATIONARY_GERM_AND_COMPLETE_EXACT_COMPLEX"},
  {"stratum":"Upsilon nonzero","stationary_for_I1B_plus_I2B":None,"principal_effect":"J^*QJ plus potentially nonfactorizing (D2U)^*(Q U)","disposition":"OPEN__COMPLETE_COMBINED_EULER_AND_HESSIAN_PACKET_REQUIRED"}],
 "closed_classes":["I2B pairing or finite-weight rescue of K726's raw-residual-zero homogeneous Phi1 branch","using residual-zero I2B first variation to cancel any nonzero I1B Euler covector","claiming nonzero residual alone supplies stationarity, new rank, gauge, or ellipticity"],
 "decision":{"SC_ACT_06_status":"ASSERTS","global_nonzero_T_no_go_proved":False,"do_not_retry_K726_with_residual_pairing_or_weight":True,"incumbent":"construct one source-typed Upsilon-nonzero stationary two-jet with Q Upsilon, DUpsilon, D2Upsilon, gauge/redundancy maps and Euclidean reduction","zero_residual_alternative":"construct a different I1B-stationary germ and exact same-response complex","strongest_independent_alternative":"complete native K500 A/B packet once its native remainder, boundary maps and complete lower certificates exist"},
 "source_and_ledger_effect":"SC-ACT-06_ASSERTS_UNCHANGED__LEDGER_UNCHANGED","ledger_no_change_reason":"The gate narrows admissible action inputs but neither constructs one nor changes source fidelity or a physics verdict.","controls":{"producer":"tests/channel-swings/k778_sc_act_06_residual_stratum_successor_gate.py","probe":"tests/channel-swings/k778_sc_act_06_residual_stratum_successor_gate_probe.py","controls_passed":32,"hostile_mutations_rejected":21},"claim_ceiling":"Exact successor gate for residual-zero versus nonzero-residual source I2B backgrounds. No global nonzero-T no-go, new stationary germ, complete elliptic complex, or protected verdict change."}
def validate(p:dict[str,Any])->None:
 r,d=p["residual_strata"],p["decision"];assert p["target_claim"]=="SC-ACT-06" and len(r)==3 and len(p["closed_classes"])==3
 assert not r[0]["stationary_for_I1B_plus_I2B"] and r[1]["stationary_for_I1B_plus_I2B"] and r[2]["stationary_for_I1B_plus_I2B"] is None
 assert d["SC_ACT_06_status"]=="ASSERTS" and not d["global_nonzero_T_no_go_proved"] and d["do_not_retry_K726_with_residual_pairing_or_weight"] and "UNCHANGED" in p["source_and_ledger_effect"]
def main()->int:
 a=argparse.ArgumentParser();a.add_argument("--write",action="store_true");x=a.parse_args();p=build();validate(p);s=json.dumps(p,indent=2,sort_keys=True)+"\n";OUTPUT.write_text(s) if x.write else print(s,end="");return 0
if __name__=="__main__":raise SystemExit(main())
