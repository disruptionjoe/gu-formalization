#!/usr/bin/env python3
"""Hostile mutations for K838."""
from __future__ import annotations
import copy,importlib.util
from pathlib import Path
P=Path(__file__).with_name("k838_sc_act_06_nonlinear_germ_admission_compiler.py");S=importlib.util.spec_from_file_location("k838",P);M=importlib.util.module_from_spec(S);assert S.loader;S.loader.exec_module(M)
def main()->int:
  muts=[
   ("base count",lambda x:x["compiler"].__setitem__("k834_row_count",24)),("new count",lambda x:x["compiler"].__setitem__("new_row_count",1)),("total",lambda x:x["compiler"].__setitem__("total_row_count",26)),
   ("finite admissible",lambda x:x["compiler"].__setitem__("finite_jet_or_formal_data_alone_admissible",True)),("no convergence",lambda x:x["compiler"].__setitem__("smooth_actual_map_or_analytic_convergence_required",False)),
   ("full rejected",lambda x:x["exact_controls"].__setitem__("category_complete_admitted",False)),("finite passes",lambda x:x["exact_controls"].__setitem__("finite_jet_only_admitted",True)),("missing",lambda x:x["exact_controls"].__setitem__("current_gu_missing_row_count",25)),
   ("GU passes",lambda x:x["exact_controls"].__setitem__("current_gu_admitted",True)),("category supplied",lambda x:x["decision"].__setitem__("actual_gu_regularity_category_declared",True)),
   ("germ supplied",lambda x:x["decision"].__setitem__("actual_gu_nonlinear_germ_or_convergent_series_constructed",True)),("global",lambda x:x["decision"].__setitem__("global_sc_act_06_proved_or_refuted",True)),
  ]
  for n,m in muts:
   p=copy.deepcopy(M.build());m(p)
   try:M.validate(p)
   except AssertionError:continue
   raise AssertionError(n)
  print("K838 hostile mutations rejected: 12/12");return 0
if __name__=="__main__":raise SystemExit(main())
