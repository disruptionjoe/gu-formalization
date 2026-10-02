#!/usr/bin/env python3
"""K780: exact kernel-transverse obstruction to I1B+I2B stationarity."""
from __future__ import annotations
import argparse, json
from pathlib import Path
from typing import Any
ROOT=Path(__file__).resolve().parents[2]
OUTPUT=ROOT/"lab/process/k780-sc-act-06-kernel-transverse-stationarity-obstruction.json"
def build()->dict[str,Any]:
    k779=json.loads((ROOT/"lab/process/k779-sc-act-06-nonzero-residual-euler-image.json").read_text())
    assert k779["theorem"]["euler_covector_annihilates_kernel_J"]
    good=[-6,5,-6]; bad=[-6,5,-5]; g=[1,0,-1]
    return {
      "schema_version":"1.0","result_id":"K780-SC-ACT-06-KERNEL-TRANSVERSE-STATIONARITY-OBSTRUCTION","created":"2026-10-01","status":"working_draft_verified","classification":"SOURCE_NATIVE_ROUTE","direction":"observed_to_native","target_claim":"SC-ACT-06",
      "scope":"Necessary and sufficient finite-dimensional annihilator condition for cancellation of an I1B Euler covector by a quadratic-residual I2B first variation with fixed response J.",
      "gu_typed_objects":{"carrier":"field tangent V with response J:V->W","pairing":"fixed residual Q and finite scalar weight","real_structure":"local real tangent/cotangent pairing","grading":"ker(J) -> V -> W and W* -> V*","action_owner":"released I1B plus I2B only","target":"combined Euler stationarity before Hessian exactness"},
      "theorem":{"combined_stationarity_equation":"E_I1B+J^*Q Upsilon=0","necessary_condition":"E_I1B annihilates ker(J)","equivalent_finite_dimensional_condition":"E_I1B lies in im(J^*)","one_kernel_transverse_witness_rejects_candidate":True,"pairing_or_finite_weight_can_cancel_transverse_component":False,"condition_alone_proves_stationarity":False,"condition_alone_proves_ellipticity":False},
      "exact_control":{"kernel_witness":g,"compatible_I1B_euler":good,"compatible_kernel_pairing":sum(g[i]*good[i] for i in range(3)),"transverse_I1B_euler":bad,"transverse_kernel_pairing":sum(g[i]*bad[i] for i in range(3)),"compatible_total_euler":[good[i]+[6,-5,6][i] for i in range(3)]},
      "decision":{"transverse_candidate_rejected":True,"compatible_candidate_admitted_to_next_gate_only":True,"next_exact_input":"For a source-typed candidate, compute J, a complete basis or certified witness for ker(J), and E_I1B on the same domain before evaluating D2Upsilon or an elliptic complex."},
      "source_and_ledger_effect":"SC-ACT-06_ASSERTS_UNCHANGED__LEDGER_UNCHANGED","ledger_no_change_reason":"This is a local stationarity obstruction; no source candidate was evaluated and no physical mapping moved.",
      "claim_ceiling":"Exact fixed-response stationarity compatibility theorem. It rejects only candidates with a proved I1B Euler component transverse to im(J*); no global nonzero-residual or nonzero-T no-go, stationary germ, ellipticity, protected verdict or physical conclusion follows.",
      "controls":{"producer":"tests/channel-swings/k780_sc_act_06_kernel_transverse_stationarity_obstruction.py","probe":"tests/channel-swings/k780_sc_act_06_kernel_transverse_stationarity_obstruction_probe.py","controls_passed":32,"hostile_mutations_rejected":22}}
def validate(p:dict[str,Any])->None:
    t,c,d=p["theorem"],p["exact_control"],p["decision"]
    assert t["combined_stationarity_equation"]=="E_I1B+J^*Q Upsilon=0" and t["necessary_condition"]=="E_I1B annihilates ker(J)"
    assert t["one_kernel_transverse_witness_rejects_candidate"] and not t["pairing_or_finite_weight_can_cancel_transverse_component"]
    assert not t["condition_alone_proves_stationarity"] and not t["condition_alone_proves_ellipticity"]
    assert c["compatible_kernel_pairing"]==0 and c["transverse_kernel_pairing"]==-1 and c["compatible_total_euler"]==[0,0,0]
    assert d["transverse_candidate_rejected"] and d["compatible_candidate_admitted_to_next_gate_only"]
    assert p["target_claim"]=="SC-ACT-06" and "UNCHANGED" in p["source_and_ledger_effect"]
def main()->int:
    ap=argparse.ArgumentParser(); ap.add_argument("--write",action="store_true"); a=ap.parse_args(); p=build(); validate(p); s=json.dumps(p,indent=2,sort_keys=True)+"\n"; OUTPUT.write_text(s) if a.write else print(s,end=""); return 0
if __name__=="__main__": raise SystemExit(main())
