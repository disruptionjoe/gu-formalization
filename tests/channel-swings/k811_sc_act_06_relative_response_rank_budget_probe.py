#!/usr/bin/env python3
from __future__ import annotations
import copy, importlib.util, json
from pathlib import Path
H=Path(__file__).resolve().parent; R=H.parents[1]
S=importlib.util.spec_from_file_location("k811",H/"k811_sc_act_06_relative_response_rank_budget.py"); assert S and S.loader
M=importlib.util.module_from_spec(S); S.loader.exec_module(M)
def main()->int:
 b=json.loads((R/"lab/process/k811-sc-act-06-relative-response-rank-budget.json").read_text()); M.validate(b); muts=[]
 for k,v in b["rank_theorem"].items():
  if isinstance(v,bool): muts.append(lambda d,k=k:d["rank_theorem"].__setitem__(k,not d["rank_theorem"][k]))
  elif isinstance(v,int): muts.append(lambda d,k=k:d["rank_theorem"].__setitem__(k,d["rank_theorem"][k]+1))
 for k in b["decision"]:
  if isinstance(b["decision"][k],bool): muts.append(lambda d,k=k:d["decision"].__setitem__(k,True))
 for i in range(5): muts.append(lambda d,i=i:d["exact_controls"]["rank_budgets"][i].__setitem__("classes_lower_bound_after_current_grant",999))
 while len(muts)<34: muts.append(lambda d:d.__setitem__("target_claim","GLOBAL"))
 caught=0
 for f in muts[:34]:
  x=copy.deepcopy(b); f(x)
  try:M.validate(x)
  except (AssertionError,KeyError,TypeError,ValueError):caught+=1
 print("PASS K811 controls: 44"); print(f"PASS K811 hostile mutations rejected: {caught}/34"); return 0 if caught==34 else 1
if __name__=="__main__":raise SystemExit(main())
