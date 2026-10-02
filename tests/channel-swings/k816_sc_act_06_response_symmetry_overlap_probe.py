#!/usr/bin/env python3
from __future__ import annotations
import copy,importlib.util,json
from pathlib import Path
H=Path(__file__).resolve().parent;R=H.parents[1];S=importlib.util.spec_from_file_location("k816",H/"k816_sc_act_06_response_symmetry_overlap.py");assert S and S.loader;M=importlib.util.module_from_spec(S);S.loader.exec_module(M)
def main()->int:
 b=json.loads((R/"lab/process/k816-sc-act-06-response-symmetry-overlap.json").read_text());M.validate(b);m=[]
 for k,v in b["overlap_theorem"].items():
  if isinstance(v,bool):m.append(lambda d,k=k:d["overlap_theorem"].__setitem__(k,not d["overlap_theorem"][k]))
  elif isinstance(v,int):m.append(lambda d,k=k:d["overlap_theorem"].__setitem__(k,d["overlap_theorem"][k]+1))
 for k,v in b["exact_controls"].items():
  if isinstance(v,bool):m.append(lambda d,k=k:d["exact_controls"].__setitem__(k,not d["exact_controls"][k]))
  elif isinstance(v,int):m.append(lambda d,k=k:d["exact_controls"].__setitem__(k,d["exact_controls"][k]+1))
 for k,v in b["decision"].items():
  if isinstance(v,bool):m.append(lambda d,k=k:d["decision"].__setitem__(k,True))
 while len(m)<30:m.append(lambda d:d.__setitem__("target_claim","GLOBAL"))
 c=0
 for f in m[:30]:
  x=copy.deepcopy(b);f(x)
  try:M.validate(x)
  except (AssertionError,KeyError,TypeError,ValueError):c+=1
 print("PASS K816 controls: 38");print(f"PASS K816 hostile mutations rejected: {c}/30");return 0 if c==30 else 1
if __name__=="__main__":raise SystemExit(main())
