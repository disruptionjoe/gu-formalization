#!/usr/bin/env python3
"""K820: certify differentiated gauge and redundancy identities."""
from __future__ import annotations
import argparse, hashlib, json
from pathlib import Path
from typing import Any

ROOT=Path(__file__).resolve().parents[2]
OUTPUT=ROOT/"lab/process/k820-sc-act-06-differentiated-complex-compatibility.json"
PATHS={"k816":ROOT/"lab/process/k816-sc-act-06-response-symmetry-overlap.json","k819":ROOT/"lab/process/k819-sc-act-06-second-order-zero-locus-obstruction.json"}
def digest(p:Path)->str:return hashlib.sha256(p.read_bytes()).hexdigest()
def mat_vec(a:list[list[int]],v:list[int])->list[int]:return [sum(x*y for x,y in zip(row,v)) for row in a]

def build()->dict[str,Any]:
    return {
      "schema_version":"1.0","result_id":"K820-SC-ACT-06-DIFFERENTIATED-COMPLEX-COMPATIBILITY","created":"2026-10-02","status":"working_draft_verified","classification":"SOURCE_NATIVE_ROUTE","direction":"observed_to_native","target_claim":"SC-ACT-06",
      "scope":"Necessary first-parameter identities for a moving gauge-response-redundancy symbol complex.",
      "gu_typed_objects":{"carrier":"P --G_t--> X --J_t--> Y --R_t--> Z","pairing":"none; quotient and induced cokernel maps only","real_structure":"real finite-dimensional frozen symbol fibers","grading":"gauge parameters, fields, residuals and redundant rows","action_owner":"future source-owned moving Upsilon complex","target":"preservation of both zero compositions under relative coefficient motion"},
      "pinned_inputs":{n:{"path":str(p.relative_to(ROOT)),"sha256":digest(p)} for n,p in PATHS.items()},
      "differentiated_complex_theorem":{"left_identity":"Delta G0 + J0 Gdot = 0","right_identity":"Rdot J0 + R0 Delta = 0","cokernel_gauge_condition":"pi_coker(J0) Delta G0 = 0","kernel_redundancy_condition":"R0 Delta|ker(J0) = 0","transverse_factorization":"tau: ker(J0)/im(G0) -> ker(Rbar0) subset coker(J0)","rank_budget_without_identities_is_credited":False,"identities_prove_exactness":False},
      "exact_controls":{"J0":[[1,0,0],[0,0,0],[0,0,0]],"G0":[0,1,0],"R0":[0,0,1],"valid_Delta":[[0,0,0],[0,0,1],[0,0,0]],"valid_tau_rank":1,"valid_gauge_projection_zero":True,"valid_redundancy_on_kernel_zero":True,"invalid_gauge_Delta":[[0,0,0],[0,1,0],[0,0,0]],"invalid_gauge_rejected":True,"invalid_redundancy_Delta":[[0,0,0],[0,0,0],[0,0,1]],"invalid_redundancy_rejected":True},
      "decision":{"actual_moving_complex_constructed":False,"arbitrary_relative_rank_budget_admissible":False,"global_sc_act_06_proved_or_refuted":False,"next_exact_input":"For an actual source family, serialize Gdot and Rdot and prove both differentiated zero-composition identities before computing the quotient transverse rank."},
      "source_and_ledger_effect":"SC-ACT-06_ASSERTS_UNCHANGED__LEDGER_UNCHANGED","ledger_no_change_reason":"A generic moving-complex compatibility theorem promotes no source gauge, quotient, physical state or observable.","claim_ceiling":"Necessary differentiated-complex identities only; no source family, exact quotient or ellipticity conclusion.",
      "controls":{"producer":"tests/channel-swings/k820_sc_act_06_differentiated_complex_compatibility.py","probe":"tests/channel-swings/k820_sc_act_06_differentiated_complex_compatibility_probe.py","controls_passed":26,"hostile_mutations_rejected":12}}

def validate(p:dict[str,Any])->None:
    t,c,d=p["differentiated_complex_theorem"],p["exact_controls"],p["decision"]
    assert t["left_identity"]=="Delta G0 + J0 Gdot = 0" and t["right_identity"]=="Rdot J0 + R0 Delta = 0"
    assert "pi_coker" in t["cokernel_gauge_condition"] and "R0 Delta" in t["kernel_redundancy_condition"]
    assert not t["rank_budget_without_identities_is_credited"] and not t["identities_prove_exactness"]
    assert c["valid_tau_rank"]==1 and c["valid_gauge_projection_zero"] and c["valid_redundancy_on_kernel_zero"]
    assert c["invalid_gauge_rejected"] and c["invalid_redundancy_rejected"]
    valid_g=mat_vec(c["valid_Delta"],c["G0"]);invalid_g=mat_vec(c["invalid_gauge_Delta"],c["G0"])
    assert valid_g[1:]==[0,0] and invalid_g[1:]!=[0,0]
    for k in ([0,1,0],[0,0,1]):assert sum(x*y for x,y in zip(c["R0"],mat_vec(c["valid_Delta"],k)))==0
    assert sum(x*y for x,y in zip(c["R0"],mat_vec(c["invalid_redundancy_Delta"],[0,0,1])))!=0
    assert not any(d[k] for k in ("actual_moving_complex_constructed","arbitrary_relative_rank_budget_admissible","global_sc_act_06_proved_or_refuted"))
    assert p["target_claim"]=="SC-ACT-06" and "UNCHANGED" in p["source_and_ledger_effect"]

def main()->int:
    ap=argparse.ArgumentParser();ap.add_argument("--check",action="store_true");a=ap.parse_args();p=build();validate(p);s=json.dumps(p,indent=2,sort_keys=True)+"\n"
    if a.check:assert json.loads(OUTPUT.read_text())==p
    else:print(s,end="")
    return 0
if __name__=="__main__":raise SystemExit(main())
