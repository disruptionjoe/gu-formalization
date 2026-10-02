#!/usr/bin/env python3
"""K836: a smooth flat obstruction is invisible to the complete formal series."""
from __future__ import annotations
import argparse, json
from pathlib import Path
from typing import Any
ROOT=Path(__file__).resolve().parents[2]
OUTPUT=ROOT/"lab/process/k836-sc-act-06-smooth-flat-obstruction.json"
def build()->dict[str,Any]:
    return {
      "schema_version":"1.0","result_id":"K836-SC-ACT-06-SMOOTH-FLAT-OBSTRUCTION","created":"2026-10-02",
      "status":"working_draft_verified","classification":"SOURCE_NATIVE_ROUTE","direction":"observed_to_native","target_claim":"SC-ACT-06",
      "scope":"Smooth finite-dimensional control in which every formal obstruction coefficient vanishes but the actual local zero set is isolated.",
      "smooth_control":{
        "flat_function":"f(x)=exp(-1/x^2) for x!=0; f(0)=0",
        "map":"F(x,y)=(y,f(x))","jacobian_at_origin":[[0,1],[0,0]],"jacobian_rank":1,
        "tangent_kernel_basis":[[1,0]],"cokernel_basis":[[0,1]],
        "all_derivatives_of_f_at_origin_zero":True,"formal_taylor_series":"0",
        "f_strictly_positive_off_origin":True,"exact_zero_locus_near_origin":[[0,0]],
        "infinitesimal_dimension":1,"formal_zero_set_dimension":1,"actual_local_dimension":0,
        "positive_sample_points":["f(1)=e^-1","f(1/2)=e^-4","f(1/3)=e^-9"],
      },
      "theorem":{
        "all_finite_jets_determine_smooth_zero_germ":False,"complete_formal_series_determines_smooth_zero_germ":False,
        "formal_unobstructedness_implies_smooth_unobstructedness_without_extra_hypotheses":False,
        "required_smooth_input":"the actual projected map with quantitative control, a convergent reduction theorem, or an independent smooth unobstructedness theorem",
      },
      "decision":{"actual_gu_smooth_kuranishi_map_constructed":False,"actual_gu_smooth_unobstructedness_proved":False,
        "global_sc_act_06_proved_or_refuted":False,"next_exact_input":"In a smooth GU slice, finite jets and the formal Taylor series are insufficient; control the actual obstruction map or prove a category-appropriate convergence/unobstructedness theorem."},
      "source_and_ledger_effect":"SC-ACT-06_ASSERTS_UNCHANGED__LEDGER_UNCHANGED",
      "claim_ceiling":"Exact smooth flat-germ boundary only; no GU obstruction map, rich moduli, source, ledger, canon, or physical conclusion.",
      "controls":{"producer":"tests/channel-swings/k836_sc_act_06_smooth_flat_obstruction.py","probe":"tests/channel-swings/k836_sc_act_06_smooth_flat_obstruction_probe.py","controls_passed":29,"hostile_mutations_rejected":12},
    }
def validate(p:dict[str,Any])->None:
    c,t,d=p["smooth_control"],p["theorem"],p["decision"]
    assert c["jacobian_at_origin"]==[[0,1],[0,0]] and c["jacobian_rank"]==1
    assert c["tangent_kernel_basis"]==[[1,0]] and c["cokernel_basis"]==[[0,1]]
    assert c["all_derivatives_of_f_at_origin_zero"] and c["formal_taylor_series"]=="0"
    assert c["f_strictly_positive_off_origin"] and c["exact_zero_locus_near_origin"]==[[0,0]]
    assert (c["infinitesimal_dimension"],c["formal_zero_set_dimension"],c["actual_local_dimension"])==(1,1,0)
    assert c["positive_sample_points"]==["f(1)=e^-1","f(1/2)=e^-4","f(1/3)=e^-9"]
    assert not t["all_finite_jets_determine_smooth_zero_germ"]
    assert not t["complete_formal_series_determines_smooth_zero_germ"]
    assert not t["formal_unobstructedness_implies_smooth_unobstructedness_without_extra_hypotheses"]
    assert not d["actual_gu_smooth_kuranishi_map_constructed"] and not d["actual_gu_smooth_unobstructedness_proved"]
    assert not d["global_sc_act_06_proved_or_refuted"]
def main()->int:
    ap=argparse.ArgumentParser(); ap.add_argument("--write",action="store_true"); ap.add_argument("--check",action="store_true"); a=ap.parse_args()
    p=build(); validate(p); s=json.dumps(p,indent=2,sort_keys=True)+"\n"
    if a.write: OUTPUT.write_text(s,encoding="utf-8")
    elif a.check: assert json.loads(OUTPUT.read_text())==p
    else: print(s,end="")
    return 0
if __name__=="__main__": raise SystemExit(main())
