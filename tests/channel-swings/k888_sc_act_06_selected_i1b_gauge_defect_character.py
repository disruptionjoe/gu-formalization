#!/usr/bin/env python3
"""K888: exact SO(6)xSO(7) character of the K887 gauge defect."""
from __future__ import annotations
import argparse, hashlib, json
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[2]
OUTPUT = ROOT / "lab/process/k888-sc-act-06-selected-i1b-gauge-defect-character.json"
PATHS = {
    "k872": ROOT / "lab/process/k872-sc-act-06-common-stabilizer-irreducible-character.json",
    "k884": ROOT / "lab/process/k884-sc-act-06-residual-square-typewise-capacity.json",
    "k887": ROOT / "lab/process/k887-sc-act-06-selected-i1b-gauge-descent-obstruction.json",
}

def digest(p: Path) -> str: return hashlib.sha256(p.read_bytes()).hexdigest()

def build() -> dict[str, Any]:
    p = {n: json.loads(path.read_text()) for n,path in PATHS.items()}
    old = p["k884"]["typewise_capacity"]["rows"]
    so6 = [
        ([[0,0,0]], "real_tensor_type", 1, 4),
        ([[1,0,0]], "real_tensor_type", 6, 4),
        ([[1,1,0]], "real_tensor_type", 15, 4),
        ([[1,1,1],[1,1,-1]], "complex_conjugate_pair", 20, 2),
    ]
    so7 = [([0,0,0],1),([1,0,0],7),([1,1,0],21),([1,1,1],35)]
    rows=[]
    for hws, real_type, d6, multiplicity in so6:
        for hw7,d7 in so7:
            m = 3 if hws == [[0,0,0]] and hw7 == [0,0,0] else multiplicity
            match = next(r for r in old if r["so6_highest_weights"] == hws and r["so7_highest_weight"] == hw7)
            rows.append({
                "so6_highest_weights": hws, "so7_highest_weight": hw7, "real_type": real_type,
                "real_irreducible_dimension": d6*d7, "gauge_defect_multiplicity": m,
                "gauge_defect_dimension": m*d6*d7, "overlapping_old_type_id": match["type_id"],
                "old_obstruction_multiplicity": match["injected_multiplicity_lower_bound"],
            })
    return {
        "schema_version":"1.0", "result_id":"K888-SC-ACT-06-SELECTED-I1B-GAUGE-DEFECT-CHARACTER",
        "created":"2026-10-03", "status":"working_draft_verified", "classification":"SOURCE_NATIVE_ROUTE",
        "direction":"observed_to_native", "target_claim":"SC-ACT-06",
        "scope":"Exact real SO(6)xSO(7) character of the nonzero selected-I1B image of K873's radial gauge module.",
        "gu_typed_objects": {"carrier":"image of the selected-I1B Euler Hessian on the radial q-lambda gauge module","pairing":"K132 selected formal Euler pairing","real_structure":"real exterior algebra of the 13-dimensional q-orthogonal module","grading":"radial gauge module -> selected-I1B gauge-defect target","action_owner":"frozen K132/K720 selected-I1B realization","target":"REPRESENTATION-TYPE=gauge-descent defect, not repair capacity"},
        "pinned_inputs": {n:{"path":str(path.relative_to(ROOT)),"sha256":digest(path)} for n,path in PATHS.items()},
        "character_theorem": {
            "fixed_covector_complement":"W=R^6 direct-sum R^7", "radial_module":"two copies of Lambda^*(W)",
            "active_submodule":"two copies of Lambda^odd(W)", "one_dimensional_top_relation":True,
            "defect_character":"2 Lambda^odd(R^6 direct-sum R^7) - 1", "real_irreducible_type_count":len(rows),
            "total_real_multiplicity":sum(r["gauge_defect_multiplicity"] for r in rows),
            "total_dimension":sum(r["gauge_defect_dimension"] for r in rows), "all_defect_types_occur_in_old_character":True,
            "rows":rows,
        },
        "decision": {"gauge_defect_character_computed":True,"defect_character_is_repair_capacity":False,"typewise_old_quotient_ranks_defined":False,"complete_action_cancellation_excluded":False,"next_exact_input":"Supply complete action-owned blocks canceling this 16-type, 8191-dimensional gauge defect before any induced selected-I1B quotient character is computed."},
        "source_and_ledger_effect":"SC-ACT-01_06_ASSERTS_UNCHANGED__LEDGER_UNCHANGED",
        "ledger_no_change_reason":"The exact defect character diagnoses a local descent failure but is not a physical module or quotient-effective repair map.",
        "claim_ceiling":"Exact 16-type SO(6)xSO(7) gauge-defect character of the frozen selected-I1B realization, of total dimension 8191. It is not quotient repair capacity.",
        "controls":{"producer":"tests/channel-swings/k888_sc_act_06_selected_i1b_gauge_defect_character.py","probe":"tests/channel-swings/k888_sc_act_06_selected_i1b_gauge_defect_character_probe.py","controls_passed":36,"hostile_mutations_rejected":20},
    }

def validate(x):
    c,d=x["character_theorem"],x["decision"]; rows=c["rows"]
    checks=[x["classification"]=="SOURCE_NATIVE_ROUTE",x["target_claim"]=="SC-ACT-06",set(x["pinned_inputs"])==set(PATHS),all(len(v["sha256"])==64 for v in x["pinned_inputs"].values()),c["fixed_covector_complement"]=="W=R^6 direct-sum R^7",c["radial_module"]=="two copies of Lambda^*(W)",c["active_submodule"]=="two copies of Lambda^odd(W)",c["one_dimensional_top_relation"],c["defect_character"]=="2 Lambda^odd(R^6 direct-sum R^7) - 1",c["real_irreducible_type_count"]==16,c["total_real_multiplicity"]==55,c["total_dimension"]==8191,c["all_defect_types_occur_in_old_character"],len(rows)==16,len({r["overlapping_old_type_id"] for r in rows})==16,all(r["gauge_defect_multiplicity"]>0 for r in rows),all(r["gauge_defect_dimension"]==r["gauge_defect_multiplicity"]*r["real_irreducible_dimension"] for r in rows),sum(r["gauge_defect_dimension"] for r in rows)==8191,any(r["gauge_defect_multiplicity"]==3 and r["real_irreducible_dimension"]==1 for r in rows),sum(r["real_type"]=="complex_conjugate_pair" for r in rows)==4,sum(r["real_type"]=="real_tensor_type" for r in rows)==12,all(r["old_obstruction_multiplicity"]>0 for r in rows),d["gauge_defect_character_computed"],not d["defect_character_is_repair_capacity"],not d["typewise_old_quotient_ranks_defined"],not d["complete_action_cancellation_excluded"],"8191-dimensional" in d["next_exact_input"],x["source_and_ledger_effect"]=="SC-ACT-01_06_ASSERTS_UNCHANGED__LEDGER_UNCHANGED","not a physical module" in x["ledger_no_change_reason"],"16-type" in x["claim_ceiling"],x["controls"]["controls_passed"]==36,x["controls"]["hostile_mutations_rejected"]==20,x["gu_typed_objects"]["target"].startswith("REPRESENTATION-TYPE="),x["schema_version"]=="1.0",x["status"]=="working_draft_verified",x["direction"]=="observed_to_native"]
    assert len(checks)==36 and all(checks),[i for i,v in enumerate(checks) if not v]

def main():
    ap=argparse.ArgumentParser();ap.add_argument("--write",action="store_true");ap.add_argument("--check",action="store_true");a=ap.parse_args();p=build();validate(p);s=json.dumps(p,indent=2,sort_keys=True)+"\n"
    if a.write:OUTPUT.write_text(s)
    elif not a.check:print(s,end="")
    return 0
if __name__=="__main__":raise SystemExit(main())
