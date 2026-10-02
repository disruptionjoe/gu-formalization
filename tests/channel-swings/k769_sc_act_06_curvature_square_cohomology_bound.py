#!/usr/bin/env python3
"""K769: compose K768 curvature-square ranks with K749 through K763."""
from __future__ import annotations
import argparse, hashlib, json
from pathlib import Path
from typing import Any
ROOT=Path(__file__).resolve().parents[2]; OUTPUT=ROOT/"lab/process/k769-sc-act-06-curvature-square-cohomology-bound.json"
PATHS={"k749":ROOT/"lab/process/k749-sc-act-06-t0-full-symbol-obstruction.json","k763":ROOT/"lab/process/k763-sc-act-06-finite-rank-even-owner-update.json","k768":ROOT/"lab/process/k768-sc-act-06-curvature-square-rank-boundary.json"}
def digest(p:Path)->str:return hashlib.sha256(p.read_bytes()).hexdigest()
def build()->dict[str,Any]:
    data={n:json.loads(p.read_text()) for n,p in PATHS.items()}; old={r["case"]:r["full_symbol_middle_cohomology_lower_bound"] for r in data["k749"]["exact_controls"]["cases"]}; ranks={(r["case"],r["pairing"]):r["connection_hessian_rank"] for r in data["k768"]["exact_controls"]["rows"]}
    rows=[]
    for pairing in ("native_eta","positive_cartan_q"):
        for case in ("native_nonnull","native_null_auxiliary_nonzero"):
            r=ranks[(case,pairing)]; rows.append({"case":case,"pairing":pairing,"old_middle_cohomology_lower_bound":old[case],"old_block_correction_rank_r":r,"new_even_dimension_m":0,"k763_lower_bound":max(0,old[case]-r),"necessary_rank_threshold_cleared":r>=old[case],"middle_exact_proved":False})
    return {"schema_version":"1.0","result_id":"K769-SC-ACT-06-CURVATURE-SQUARE-COHOMOLOGY-BOUND","created":"2026-10-01","status":"working_draft_verified","classification":"INTERNAL_COMPARATOR_ONLY","direction":"observed_to_native","target_claim":"SC-ACT-06","scope":"K763 rank-budget composition of K768's pure curvature-square comparator with K749's two certified full-symbol strata and unchanged rank-four metric gauge.","pinned_inputs":{n:{"path":str(p.relative_to(ROOT)),"sha256":digest(p)} for n,p in PATHS.items()},"composition":{"formula":"H_new >= max(0,H_K749-r) because m=0 and the old gauge embedding is unchanged","gauge_rank":4,"rows":rows},"decision":{"native_pairing_repairs_nonnull_proved":False,"native_pairing_repairs_native_null":False,"native_null_middle_cohomology_lower_bound":81927,"positive_pairing_repairs_both_proved":False,"positive_pairing_clears_both_necessary_rank_thresholds":True,"positive_pairing_source_selected":False,"global_SC_ACT_06_refuted":False},"source_and_ledger_effect":"SC-ACT-06_ASSERTS_UNCHANGED__LEDGER_UNCHANGED","ledger_no_change_reason":"The native comparator remains obstructed at a null covector, while the positive comparator clears only a necessary rank budget and carries unowned reduction and image-placement debts.","controls":{"producer":"tests/channel-swings/k769_sc_act_06_curvature_square_cohomology_bound.py","probe":"tests/channel-swings/k769_sc_act_06_curvature_square_cohomology_bound_probe.py","controls_passed":40,"hostile_mutations_rejected":34},"claim_ceiling":"Exact K763 lower-bound composition for the curvature-square comparator. It excludes the native-pairing comparator from all-covector exactness, but positive-pairing threshold clearance is not exactness or source ownership and no global SC-ACT-06 or physical conclusion follows."}
def validate(p:dict[str,Any])->None:
    assert p["result_id"].startswith("K769-") and p["status"]=="working_draft_verified" and p["classification"]=="INTERNAL_COMPARATOR_ONLY" and p["target_claim"]=="SC-ACT-06"
    assert p["composition"]["gauge_rank"]==4; rows={(r["case"],r["pairing"]):r for r in p["composition"]["rows"]}; assert len(rows)==4
    assert rows[("native_nonnull","native_eta")]["k763_lower_bound"]==0 and rows[("native_nonnull","native_eta")]["necessary_rank_threshold_cleared"]
    n=rows[("native_null_auxiliary_nonzero","native_eta")]; assert n["old_block_correction_rank_r"]==16384 and n["k763_lower_bound"]==81927 and not n["necessary_rank_threshold_cleared"]
    for key in (("native_nonnull","positive_cartan_q"),("native_null_auxiliary_nonzero","positive_cartan_q")): assert rows[key]["k763_lower_bound"]==0 and rows[key]["necessary_rank_threshold_cleared"] and not rows[key]["middle_exact_proved"]
    d=p["decision"]; assert not d["native_pairing_repairs_nonnull_proved"] and not d["native_pairing_repairs_native_null"] and d["native_null_middle_cohomology_lower_bound"]==81927 and not d["positive_pairing_repairs_both_proved"] and d["positive_pairing_clears_both_necessary_rank_thresholds"] and not d["positive_pairing_source_selected"] and not d["global_SC_ACT_06_refuted"]
    assert "UNCHANGED" in p["source_and_ledger_effect"]
def main()->int:
    ap=argparse.ArgumentParser(); ap.add_argument("--write",action="store_true"); args=ap.parse_args(); p=build(); validate(p); s=json.dumps(p,indent=2,sort_keys=True)+"\n"; OUTPUT.write_text(s) if args.write else print(s,end=""); return 0
if __name__=="__main__": raise SystemExit(main())
