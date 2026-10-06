#!/usr/bin/env python3
"""K1183: sharp overlap envelope for a prior rank-98 channel and native J."""
from __future__ import annotations
import argparse, hashlib, json
from pathlib import Path
from typing import Any
ROOT=Path(__file__).resolve().parents[2]
OUTPUT=ROOT/"lab/process/k1183-rank98-overlap-envelope.json"
PATHS={"k1173":ROOT/"lab/process/k1173-k132-causal-repair-polytope.json","k1182":ROOT/"lab/process/k1182-native-upsilon-k132-complement-ranks.json"}
def digest(p:Path)->str:return hashlib.sha256(p.read_bytes()).hexdigest()
def build()->dict[str,Any]:
    k1173=json.loads(PATHS["k1173"].read_text()); k1182=json.loads(PATHS["k1182"].read_text())
    j={x["case"]:x for x in k1182["exact_controls"]["cases"]}
    deficit_by_case={
        "native_nonnull": k1173["causal"]["timelike"]["best_case_repair_deficit"],
        "native_null_auxiliary_nonzero": k1173["causal"]["null"]["best_case_repair_deficit"],
    }
    rows=[]
    for name in ("native_nonnull","native_null_auxiliary_nonzero"):
        c=j[name]["rank_j_on_ker_h"]; prior=98; low=max(0,c-prior); high=c; d=deficit_by_case[name]
        rows.append({"case":name,"prior_channel_rank":prior,"j_complement_before_prior":c,"j_sequential_complement_min":low,"j_sequential_complement_max":high,"joint_rank_min":max(prior,c),"joint_rank_max":prior+c,"repair_residual_best_case":d-high,"repair_residual_worst_overlap":d-low})
    return {"schema_version":"1.0","result_id":"K1183-RANK98-OVERLAP-ENVELOPE","created":"2026-10-05","status":"working_draft_verified","pinned_inputs":{k:{"path":str(v.relative_to(ROOT)),"sha256":digest(v)} for k,v in PATHS.items()},"theorem":"for subspaces of ranks a,b, the second sequential complement lies in [max(0,b-a),b]","exact_controls":{"cases":rows},"prior_channel_ownership":"favorable unowned K132 transport grant","claim_ceiling":"sharp dimension-only overlap interval; no measured common coupling or source ownership for the rank-98 channel"}
def validate(p:dict[str,Any])->None:
    assert p["result_id"]=="K1183-RANK98-OVERLAP-ENVELOPE" and p["status"]=="working_draft_verified"
    r={x["case"]:x for x in p["exact_controls"]["cases"]}; a,b=r["native_nonnull"],r["native_null_auxiliary_nonzero"]
    assert (a["j_sequential_complement_min"],a["j_sequential_complement_max"])==(64,162)
    assert (b["j_sequential_complement_min"],b["j_sequential_complement_max"])==(8225,8323)
    assert (a["repair_residual_best_case"],a["repair_residual_worst_overlap"])==(98210,98308)
    assert (b["repair_residual_best_case"],b["repair_residual_worst_overlap"])==(98213,98311)
    for x in r.values(): assert x["joint_rank_min"]==max(x["prior_channel_rank"],x["j_complement_before_prior"]) and x["joint_rank_max"]==x["prior_channel_rank"]+x["j_complement_before_prior"]
    assert p["prior_channel_ownership"].startswith("favorable unowned")
def main()->int:
    q=argparse.ArgumentParser();q.add_argument("--write",action="store_true");a=q.parse_args();p=build();validate(p);s=json.dumps(p,indent=2,sort_keys=True)+"\n";OUTPUT.write_text(s) if a.write else print(s,end="");return 0
if __name__=="__main__":raise SystemExit(main())
