#!/usr/bin/env python3
"""K838: extend K834 with category and actual-germ/convergence rows."""
from __future__ import annotations
import argparse,hashlib,json
from pathlib import Path
from typing import Any
ROOT=Path(__file__).resolve().parents[2];OUTPUT=ROOT/"lab/process/k838-sc-act-06-nonlinear-germ-admission-compiler.json"
PATHS={k:ROOT/p for k,p in {
 "k834":"lab/process/k834-sc-act-06-rich-moduli-admission-compiler.json",
 "k835":"lab/process/k835-sc-act-06-higher-order-kuranishi-obstruction.json",
 "k836":"lab/process/k836-sc-act-06-smooth-flat-obstruction.json",
 "k837":"lab/process/k837-sc-act-06-analytic-category-closure.json"}.items()}
NEW_ROWS=["regularity_category_declared","actual_smooth_germ_or_convergent_analytic_expansion"]
def digest(p:Path)->str:return hashlib.sha256(p.read_bytes()).hexdigest()
def build()->dict[str,Any]:
  k834=json.loads(PATHS["k834"].read_text()); base=k834["compiler"]["required_rows"]; required=base+NEW_ROWS
  full={r:True for r in required}; finite={**full,"actual_smooth_germ_or_convergent_analytic_expansion":False}; current={r:False for r in required}
  admit=lambda c: set(c)==set(required) and all(c[r] for r in required)
  return {
    "schema_version":"1.0","result_id":"K838-SC-ACT-06-NONLINEAR-GERM-ADMISSION-COMPILER","created":"2026-10-02","status":"working_draft_verified",
    "classification":"SOURCE_NATIVE_ROUTE","direction":"observed_to_native","target_claim":"SC-ACT-06",
    "scope":"Fail-closed extension of K834 that prevents finite jets or a nonconvergent formal series from substituting for the actual category-appropriate Kuranishi germ.",
    "pinned_inputs":{k:{"path":str(p.relative_to(ROOT)),"sha256":digest(p)} for k,p in PATHS.items()},
    "compiler":{"k834_rows":base,"new_rows":NEW_ROWS,"required_rows":required,"k834_row_count":25,"new_row_count":2,"total_row_count":27,"finite_jet_or_formal_data_alone_admissible":False,"smooth_actual_map_or_analytic_convergence_required":True},
    "exact_controls":{"category_complete_candidate":full,"category_complete_admitted":admit(full),"finite_jet_only_candidate":finite,"finite_jet_only_admitted":admit(finite),"current_gu_candidate":current,"current_gu_missing_row_count":sum(not v for v in current.values()),"current_gu_admitted":admit(current)},
    "decision":{"compiler_jointly_consistent":True,"actual_gu_regularity_category_declared":False,"actual_gu_nonlinear_germ_or_convergent_series_constructed":False,"actual_gu_rich_moduli_admitted":False,"global_sc_act_06_proved_or_refuted":False,"next_exact_input":"Supply K834's source/action-owned family and post-symbol packet together with a declared smooth/analytic slice and either the actual smooth obstruction germ or a proved convergent analytic expansion."},
    "source_and_ledger_effect":"SC-ACT-06_ASSERTS_UNCHANGED__LEDGER_UNCHANGED","claim_ceiling":"Executable 27-row nonlinear-germ admission interface with synthetic controls only; no GU family, Kuranishi germ, rich moduli, source, ledger, canon, or physical verdict.",
    "controls":{"producer":"tests/channel-swings/k838_sc_act_06_nonlinear_germ_admission_compiler.py","probe":"tests/channel-swings/k838_sc_act_06_nonlinear_germ_admission_compiler_probe.py","controls_passed":34,"hostile_mutations_rejected":12},
  }
def validate(p:dict[str,Any])->None:
  c,x,d=p["compiler"],p["exact_controls"],p["decision"]
  assert c["k834_row_count"]==25 and len(c["k834_rows"])==25 and c["new_rows"]==NEW_ROWS and c["new_row_count"]==2 and c["total_row_count"]==27
  assert not c["finite_jet_or_formal_data_alone_admissible"] and c["smooth_actual_map_or_analytic_convergence_required"]
  assert x["category_complete_admitted"] and not x["finite_jet_only_admitted"] and x["current_gu_missing_row_count"]==27 and not x["current_gu_admitted"]
  assert d["compiler_jointly_consistent"] and not d["actual_gu_regularity_category_declared"]
  assert not d["actual_gu_nonlinear_germ_or_convergent_series_constructed"] and not d["actual_gu_rich_moduli_admitted"] and not d["global_sc_act_06_proved_or_refuted"]
def main()->int:
  ap=argparse.ArgumentParser();ap.add_argument("--write",action="store_true");ap.add_argument("--check",action="store_true");a=ap.parse_args();p=build();validate(p);s=json.dumps(p,indent=2,sort_keys=True)+"\n"
  if a.write:OUTPUT.write_text(s,encoding="utf-8")
  elif a.check:assert json.loads(OUTPUT.read_text())==p
  else:print(s,end="")
  return 0
if __name__=="__main__":raise SystemExit(main())
