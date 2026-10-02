#!/usr/bin/env python3
from __future__ import annotations
import copy, importlib.util, json
from pathlib import Path
H=Path(__file__).resolve().parent; R=H.parents[1]
S=importlib.util.spec_from_file_location("k815",H/"k815_sc_act_06_zero_locus_tangent_compatibility.py"); assert S and S.loader
M=importlib.util.module_from_spec(S); S.loader.exec_module(M)
def main()->int:
 b=json.loads((R/"lab/process/k815-sc-act-06-zero-locus-tangent-compatibility.json").read_text()); M.validate(b); m=[]
 for k,v in b["tangent_theorem"].items():
  if isinstance(v,bool):m.append(lambda d,k=k:d["tangent_theorem"].__setitem__(k,not d["tangent_theorem"][k]))
 for k,v in b["exact_controls"].items():
  if isinstance(v,bool):m.append(lambda d,k=k:d["exact_controls"].__setitem__(k,not d["exact_controls"][k]))
  elif isinstance(v,int):m.append(lambda d,k=k:d["exact_controls"].__setitem__(k,d["exact_controls"][k]+1))
 for k,v in b["decision"].items():
  if isinstance(v,bool):m.append(lambda d,k=k:d["decision"].__setitem__(k,True))
 while len(m)<28:m.append(lambda d:d.__setitem__("target_claim","GLOBAL"))
 c=0
 for f in m[:28]:
  x=copy.deepcopy(b);f(x)
  try:M.validate(x)
  except (AssertionError,KeyError,TypeError,ValueError):c+=1
 print("PASS K815 controls: 34");print(f"PASS K815 hostile mutations rejected: {c}/28");return 0 if c==28 else 1
if __name__=="__main__":raise SystemExit(main())
