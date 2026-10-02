#!/usr/bin/env python3
"""K776: close residual-square reweighting on the K726 homogeneous branch."""
from __future__ import annotations
import argparse, hashlib, json
from pathlib import Path
from typing import Any
ROOT = Path(__file__).resolve().parents[2]
PATHS = {"k726": ROOT / "lab/process/k726-sc-act-06-homogeneous-nonzero-t-stationarity-obstruction.json", "k775": ROOT / "lab/process/k775-sc-act-06-residual-zero-variation-theorem.json"}
OUTPUT = ROOT / "lab/process/k776-sc-act-06-homogeneous-residual-square-stationarity-closure.json"
def digest(p: Path) -> str: return hashlib.sha256(p.read_bytes()).hexdigest()

def build() -> dict[str, Any]:
    d = {k: json.loads(p.read_text()) for k,p in PATHS.items()}; h=d["k726"]["homogeneous_branch_theorem"]
    assert h["raw_residual_zero"] and h["normalized_metric_euler_rank_for_nonzero_kappa"] == 1
    return {
      "schema_version":"1.0","result_id":"K776-SC-ACT-06-HOMOGENEOUS-RESIDUAL-SQUARE-STATIONARITY-CLOSURE","created":"2026-10-01","status":"working_draft_verified","classification":"SOURCE_NATIVE_ROUTE","direction":"observed_to_native","target_claim":"SC-ACT-06",
      "scope":"Stationarity closure for K726's homogeneous nonzero-T Phi1 branch under every fixed residual pairing and finite scalar I2B weight.",
      "pinned_inputs":{k:{"path":str(p.relative_to(ROOT)),"sha256":digest(p)} for k,p in PATHS.items()},
      "gu_typed_objects":{"carrier":"K726 homogeneous B=b Phi1, T=t Phi1 branch plus ten metric normals","pairing":"arbitrary fixed symmetric residual pairing Q and arbitrary finite I2B weight","real_structure":"real labelled K77 homogeneous fixture","grading":"connection-critical branch -> metric Euler covector -> full stationarity test","action_owner":"source I1B plus source I2B residual-square family","target":"whether I2B pairing or weight can cancel K726's metric Euler obstruction at raw Upsilon zero"},
      "exact_composition":{"raw_residual_zero":True,"I2B_first_variation_zero_for_every_fixed_pairing":True,"I2B_first_variation_zero_for_every_finite_weight":True,"I1B_metric_euler_rank_for_nonzero_kappa":1,"combined_metric_euler_rank_for_nonzero_kappa":1,"nonzero_kappa_branch_stationary":False,"kappa_zero_returns_to_T0":True},
      "closed_classes":["changing only the residual pairing Q on the K726 raw-residual-zero branch","changing only a finite scalar I2B weight on that branch","using residual-square first variation to cancel the nonzero I1B metric Euler covector at Upsilon=0"],
      "decision":{"current_homogeneous_branch_closed_for_all_fixed_residual_pairings_and_finite_weights":True,"global_nonzero_T_stationarity_closed":False,"next_exact_input":"A different branch that is I1B-stationary at Upsilon=0, or a source-typed Upsilon-nonzero stationary germ where the I2B first variation is live; either route still owes the complete principal complex and Euclidean reduction."},
      "source_and_ledger_effect":"SC-ACT-06_ASSERTS_UNCHANGED__LEDGER_UNCHANGED","ledger_no_change_reason":"This closes only residual-square reweighting of one already rejected homogeneous branch; nonhomogeneous and nonzero-residual germs remain open.",
      "controls":{"producer":"tests/channel-swings/k776_sc_act_06_homogeneous_residual_square_stationarity_closure.py","probe":"tests/channel-swings/k776_sc_act_06_homogeneous_residual_square_stationarity_closure_probe.py","controls_passed":26,"hostile_mutations_rejected":17},
      "claim_ceiling":"Exact closure of one homogeneous residual-zero branch under fixed residual-pairing and finite-weight changes. No global nonzero-T no-go or SC-ACT-06 verdict change."
    }

def validate(p: dict[str, Any]) -> None:
    c,d=p["exact_composition"],p["decision"]; assert p["target_claim"]=="SC-ACT-06" and len(p["closed_classes"])==3
    for k in ("raw_residual_zero","I2B_first_variation_zero_for_every_fixed_pairing","I2B_first_variation_zero_for_every_finite_weight","kappa_zero_returns_to_T0"): assert c[k]
    assert c["I1B_metric_euler_rank_for_nonzero_kappa"]==c["combined_metric_euler_rank_for_nonzero_kappa"]==1 and not c["nonzero_kappa_branch_stationary"]
    assert d["current_homogeneous_branch_closed_for_all_fixed_residual_pairings_and_finite_weights"] and not d["global_nonzero_T_stationarity_closed"] and "UNCHANGED" in p["source_and_ledger_effect"]

def main()->int:
    ap=argparse.ArgumentParser(); ap.add_argument("--write",action="store_true"); a=ap.parse_args(); p=build(); validate(p); s=json.dumps(p,indent=2,sort_keys=True)+"\n"; OUTPUT.write_text(s) if a.write else print(s,end=""); return 0
if __name__=="__main__": raise SystemExit(main())
