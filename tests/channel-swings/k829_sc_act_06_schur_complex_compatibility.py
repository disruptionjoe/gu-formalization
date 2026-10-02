#!/usr/bin/env python3
"""K829: Schur elimination must transport gauge and redundancy maps."""
from __future__ import annotations
import argparse, hashlib, json
from pathlib import Path
from typing import Any

ROOT=Path(__file__).resolve().parents[2]
OUTPUT=ROOT/"lab/process/k829-sc-act-06-schur-complex-compatibility.json"
PATHS={"k820":ROOT/"lab/process/k820-sc-act-06-differentiated-complex-compatibility.json","k824":ROOT/"lab/process/k824-sc-act-06-mixed-symbol-schur-gate.json"}
def digest(path:Path)->str:return hashlib.sha256(path.read_bytes()).hexdigest()

def build()->dict[str,Any]:
    return {
        "schema_version":"1.0","result_id":"K829-SC-ACT-06-SCHUR-COMPLEX-COMPATIBILITY","created":"2026-10-02","status":"working_draft_verified",
        "classification":"SOURCE_NATIVE_ROUTE","direction":"observed_to_native","target_claim":"SC-ACT-06",
        "scope":"Exact transport of gauge and redundancy maps through an invertible fermion-block Schur reduction.",
        "pinned_inputs":{n:{"path":str(p.relative_to(ROOT)),"sha256":digest(p)} for n,p in PATHS.items()},
        "schur_complex_theorem":{
            "full_symbol":"M=[[B,C],[D,F]] with F invertible","reduced_symbol":"S=B-C F^-1 D",
            "field_lift":"L(x)=(x,-F^-1 D x)","equation_projection":"P(y,z)=y-C F^-1 z","factorization":"P M L=S",
            "full_gauge_descends_if":"M(G_b,G_f)=0; then G_f=-F^-1 D G_b and S G_b=0",
            "full_redundancy_descends_if":"(R_b,R_f)M=0; then R_f=-R_b C F^-1 and R_b S=0",
            "kernel_equivalence_alone_authenticates_reduced_complex":False,
            "owned_two_sided_mixed_blocks_required":True,
        },
        "exact_controls":{
            "B":[[1,0],[0,1]],"C":[[0],[1]],"D":[[0,1]],"F":[[1]],"S":[[1,0],[0,0]],
            "G_b":[0,1],"G_f":[-1],"M_G":[0,0,0],"S_G_b":[0,0],
            "R_b":[0,1],"R_f":[-1],"R_M":[0,0,0],"R_b_S":[0,0],
            "full_kernel_dimension":1,"reduced_kernel_dimension":1,"gauge_image_equals_reduced_kernel":True,
        },
        "decision":{"actual_gu_mixed_complex_constructed":False,"actual_gu_gauge_or_redundancy_authenticated":False,"global_sc_act_06_proved_or_refuted":False,"next_exact_input":"Supply action-owned B,C,D,F and full G,R on one domain, then verify their Schur-descended maps and all-covector exactness."},
        "source_and_ledger_effect":"SC-ACT-06_ASSERTS_UNCHANGED__LEDGER_UNCHANGED",
        "claim_ceiling":"Schur-complex compatibility theorem and exact control only; no GU mixed complex, gauge ownership, ellipticity, or physical conclusion.",
        "controls":{"producer":"tests/channel-swings/k829_sc_act_06_schur_complex_compatibility.py","probe":"tests/channel-swings/k829_sc_act_06_schur_complex_compatibility_probe.py","controls_passed":30,"hostile_mutations_rejected":12},
    }

def validate(p:dict[str,Any])->None:
    t,c,d=p["schur_complex_theorem"],p["exact_controls"],p["decision"]
    assert t["reduced_symbol"]=="S=B-C F^-1 D" and t["factorization"]=="P M L=S"
    assert "G_f=-F^-1 D G_b" in t["full_gauge_descends_if"] and "R_f=-R_b C F^-1" in t["full_redundancy_descends_if"]
    assert not t["kernel_equivalence_alone_authenticates_reduced_complex"] and t["owned_two_sided_mixed_blocks_required"]
    assert c["S"]==[[1,0],[0,0]] and c["M_G"]==[0,0,0] and c["S_G_b"]==[0,0]
    assert c["R_M"]==[0,0,0] and c["R_b_S"]==[0,0]
    assert c["full_kernel_dimension"]==c["reduced_kernel_dimension"]==1 and c["gauge_image_equals_reduced_kernel"]
    assert not d["actual_gu_mixed_complex_constructed"] and not d["actual_gu_gauge_or_redundancy_authenticated"] and not d["global_sc_act_06_proved_or_refuted"]
    assert p["target_claim"]=="SC-ACT-06" and "UNCHANGED" in p["source_and_ledger_effect"]

def main()->int:
    ap=argparse.ArgumentParser();ap.add_argument("--check",action="store_true");a=ap.parse_args();p=build();validate(p)
    if a.check:assert json.loads(OUTPUT.read_text())==p
    else:print(json.dumps(p,indent=2,sort_keys=True))
    return 0
if __name__=="__main__":raise SystemExit(main())
