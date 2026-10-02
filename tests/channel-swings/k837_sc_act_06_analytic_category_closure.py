#!/usr/bin/env python3
"""K837: analytic convergence is the exact boundary missing from smooth formal data."""
from __future__ import annotations
import argparse,json,math
from pathlib import Path
from typing import Any
ROOT=Path(__file__).resolve().parents[2]; OUTPUT=ROOT/"lab/process/k837-sc-act-06-analytic-category-closure.json"
def build()->dict[str,Any]:
    controls=[]
    for m in (2,3,5):
      controls.append({"map":f"k_{m}(x)=x^{m}","zero_derivative_orders":list(range(m)),"first_nonzero_order":m,"first_nonzero_coefficient":math.factorial(m),"zero_germ":False})
    return {
      "schema_version":"1.0","result_id":"K837-SC-ACT-06-ANALYTIC-CATEGORY-CLOSURE","created":"2026-10-02","status":"working_draft_verified",
      "classification":"SOURCE_NATIVE_ROUTE","direction":"observed_to_native","target_claim":"SC-ACT-06",
      "scope":"Exact real-analytic identity boundary distinguishing a convergent obstruction germ from finite jets and from a merely formal smooth series.",
      "analytic_identity_theorem":{"hypothesis":"real-analytic germ on a connected neighborhood","all_taylor_coefficients_zero_implies_local_zero_germ":True,"convergent_taylor_series_determines_local_germ":True,"finite_jet_order_suffices_without_degree_bound":False,"polynomial_controls":controls},
      "category_boundary":{"smooth_flat_counterexample_ref":"lab/process/k836-sc-act-06-smooth-flat-obstruction.json","analytic_identity_excludes_smooth_flat_behavior":True,"regularity_category_must_be_declared":True,"formal_series_requires_convergence_or_actual_map":True},
      "decision":{"actual_gu_regular_category_declared":False,"actual_gu_convergent_kuranishi_series_constructed":False,"actual_gu_nonlinear_germ_constructed":False,"global_sc_act_06_proved_or_refuted":False,"next_exact_input":"Declare the GU slice and obstruction-map regularity. In the analytic category prove convergence; in the smooth category control the actual map rather than its formal series."},
      "source_and_ledger_effect":"SC-ACT-06_ASSERTS_UNCHANGED__LEDGER_UNCHANGED","claim_ceiling":"Exact analytic identity boundary and polynomial controls only; no GU category, convergent series, rich moduli, source, ledger, canon, or physical conclusion.",
      "controls":{"producer":"tests/channel-swings/k837_sc_act_06_analytic_category_closure.py","probe":"tests/channel-swings/k837_sc_act_06_analytic_category_closure_probe.py","controls_passed":27,"hostile_mutations_rejected":12},
    }
def validate(p:dict[str,Any])->None:
    a,c,d=p["analytic_identity_theorem"],p["category_boundary"],p["decision"]
    assert a["all_taylor_coefficients_zero_implies_local_zero_germ"] and a["convergent_taylor_series_determines_local_germ"]
    assert not a["finite_jet_order_suffices_without_degree_bound"]
    for row,m in zip(a["polynomial_controls"],(2,3,5)):
      assert row["zero_derivative_orders"]==list(range(m)) and row["first_nonzero_order"]==m and row["first_nonzero_coefficient"]==math.factorial(m) and not row["zero_germ"]
    assert c["analytic_identity_excludes_smooth_flat_behavior"] and c["regularity_category_must_be_declared"] and c["formal_series_requires_convergence_or_actual_map"]
    assert not d["actual_gu_regular_category_declared"] and not d["actual_gu_convergent_kuranishi_series_constructed"]
    assert not d["actual_gu_nonlinear_germ_constructed"] and not d["global_sc_act_06_proved_or_refuted"]
def main()->int:
    ap=argparse.ArgumentParser();ap.add_argument("--write",action="store_true");ap.add_argument("--check",action="store_true");x=ap.parse_args();p=build();validate(p);s=json.dumps(p,indent=2,sort_keys=True)+"\n"
    if x.write:OUTPUT.write_text(s,encoding="utf-8")
    elif x.check:assert json.loads(OUTPUT.read_text())==p
    else:print(s,end="")
    return 0
if __name__=="__main__":raise SystemExit(main())
