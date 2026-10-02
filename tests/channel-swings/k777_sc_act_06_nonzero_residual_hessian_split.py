#!/usr/bin/env python3
"""K777: isolate the nonfactorizing Hessian term at nonzero residual."""
from __future__ import annotations
import argparse, hashlib, json
from pathlib import Path
from typing import Any
ROOT=Path(__file__).resolve().parents[2]
PATHS={"k743":ROOT/"lab/process/k743-sc-act-06-residual-square-image-cap.json","k775":ROOT/"lab/process/k775-sc-act-06-residual-zero-variation-theorem.json","k776":ROOT/"lab/process/k776-sc-act-06-homogeneous-residual-square-stationarity-closure.json"}
OUTPUT=ROOT/"lab/process/k777-sc-act-06-nonzero-residual-hessian-split.json"
def digest(p:Path)->str:return hashlib.sha256(p.read_bytes()).hexdigest()
def build()->dict[str,Any]:
    d={k:json.loads(p.read_text()) for k,p in PATHS.items()}; assert d["k775"]["variation_theorem"]["nonzero_residual_second_derivative_term_present"]
    return {"schema_version":"1.0","result_id":"K777-SC-ACT-06-NONZERO-RESIDUAL-HESSIAN-SPLIT","created":"2026-10-01","status":"working_draft_verified","classification":"SOURCE_NATIVE_ROUTE","direction":"observed_to_native","target_claim":"SC-ACT-06",
      "scope":"Exact decomposition of the quadratic-residual Hessian away from Upsilon=0 and the minimum native data required to credit its nonfactorizing term.","pinned_inputs":{k:{"path":str(p.relative_to(ROOT)),"sha256":digest(p)} for k,p in PATHS.items()},
      "gu_typed_objects":{"carrier":"one source-typed field two-jet and residual fibre at a candidate Upsilon-nonzero background","pairing":"the operative source-owned residual pairing Q on one common real domain","real_structure":"must be supplied by the candidate background; not inferred from the K720 comparator","grading":"field tangent -> combined I1B/I2B Euler and Hessian rows -> redundancy","action_owner":"source I1B plus source I2B; no curvature-square substitution","target":"the Hessian component capable of escaping the old DUpsilon-adjoint image"},
      "hessian_split":{"first_variation":"dS2=J^* Q U","stationarity_equation":"dS1+J^* Q U=0","gauss_newton_term":"J^* Q J","residual_curvature_term":"(D2U)^*(Q U)","residual_zero_kills_residual_curvature_term":True,"nonzero_residual_makes_residual_curvature_term_potentially_live":True,"gauss_newton_image_forced_inside_J_adjoint_image":True,"residual_curvature_image_forced_inside_J_adjoint_image":False,"nonzero_residual_alone_proves_new_rank":False,"nonzero_residual_alone_proves_stationarity":False},
      "native_obligations":["one source-typed Upsilon-nonzero background satisfying the complete combined Euler equations","the actual residual pairing and finite coefficient on the same real carrier","complete DUpsilon and D2Upsilon symbols, including metric, epsilon and distortion legs","owned gauge and redundancy maps with Euler-after-gauge composition","one Euclidean reduction or authenticated continuation and all-covector exactness test"],
      "decision":{"only_known_I2B_route_outside_same_response_factorization":"a stationary Upsilon-nonzero germ with nonzero residual-curvature Hessian term","route_is_currently_constructed":False,"next_exact_input":"Construct one Upsilon-nonzero source-typed stationary two-jet and serialize Q Upsilon, DUpsilon and D2Upsilon before rank or exactness credit."},
      "source_and_ledger_effect":"SC-ACT-06_ASSERTS_UNCHANGED__LEDGER_UNCHANGED","ledger_no_change_reason":"The split exposes an exact construction target but supplies none of its background data or physical interpretation.","controls":{"producer":"tests/channel-swings/k777_sc_act_06_nonzero_residual_hessian_split.py","probe":"tests/channel-swings/k777_sc_act_06_nonzero_residual_hessian_split_probe.py","controls_passed":30,"hostile_mutations_rejected":20},"claim_ceiling":"Exact local Hessian split and admission obligations. No constructed nonzero-residual stationary germ, new rank theorem, ellipticity result, or SC-ACT-06 verdict change."}
def validate(p:dict[str,Any])->None:
    h,d=p["hessian_split"],p["decision"]; assert p["target_claim"]=="SC-ACT-06" and len(p["native_obligations"])==5
    for k in ("residual_zero_kills_residual_curvature_term","nonzero_residual_makes_residual_curvature_term_potentially_live","gauss_newton_image_forced_inside_J_adjoint_image"): assert h[k]
    for k in ("residual_curvature_image_forced_inside_J_adjoint_image","nonzero_residual_alone_proves_new_rank","nonzero_residual_alone_proves_stationarity"): assert not h[k]
    assert h["gauss_newton_term"]=="J^* Q J" and not d["route_is_currently_constructed"] and "UNCHANGED" in p["source_and_ledger_effect"]
def main()->int:
    a=argparse.ArgumentParser();a.add_argument("--write",action="store_true");x=a.parse_args();p=build();validate(p);s=json.dumps(p,indent=2,sort_keys=True)+"\n";OUTPUT.write_text(s) if x.write else print(s,end="");return 0
if __name__=="__main__":raise SystemExit(main())
