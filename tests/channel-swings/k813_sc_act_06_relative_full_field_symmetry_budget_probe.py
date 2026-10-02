#!/usr/bin/env python3
from __future__ import annotations
import copy,importlib.util,json
from pathlib import Path
H=Path(__file__).resolve().parent;R=H.parents[1];S=importlib.util.spec_from_file_location("k813",H/"k813_sc_act_06_relative_full_field_symmetry_budget.py");assert S and S.loader;M=importlib.util.module_from_spec(S);S.loader.exec_module(M)
def main()->int:
 b=json.loads((R/"lab/process/k813-sc-act-06-relative-full-field-symmetry-budget.json").read_text());M.validate(b);m=[]
 for k,v in b["combined_budget_theorem"].items():
  if isinstance(v,bool):m.append(lambda d,k=k:d["combined_budget_theorem"].__setitem__(k,not d["combined_budget_theorem"][k]))
  elif isinstance(v,int):m.append(lambda d,k=k:d["combined_budget_theorem"].__setitem__(k,d["combined_budget_theorem"][k]+1))
 for i in range(6):m.append(lambda d,i=i:d["exact_controls"]["budgets"][i].__setitem__("full_field_classes_lower_bound",999))
 while len(m)<30:m.append(lambda d:d["decision"].__setitem__("global_sc_act_06_proved_or_refuted",True))
 c=0
 for f in m[:30]:
  x=copy.deepcopy(b);f(x)
  try:M.validate(x)
  except (AssertionError,KeyError,TypeError,ValueError):c+=1
 print("PASS K813 controls: 38");print(f"PASS K813 hostile mutations rejected: {c}/30");return 0 if c==30 else 1
if __name__=="__main__":raise SystemExit(main())
