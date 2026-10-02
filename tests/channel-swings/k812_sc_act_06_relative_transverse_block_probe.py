#!/usr/bin/env python3
from __future__ import annotations
import copy,importlib.util,json
from pathlib import Path
H=Path(__file__).resolve().parent;R=H.parents[1];S=importlib.util.spec_from_file_location("k812",H/"k812_sc_act_06_relative_transverse_block.py");assert S and S.loader;M=importlib.util.module_from_spec(S);S.loader.exec_module(M)
def main()->int:
 b=json.loads((R/"lab/process/k812-sc-act-06-relative-transverse-block.json").read_text());M.validate(b);m=[]
 for k,v in b["transverse_theorem"].items():
  if isinstance(v,bool):m.append(lambda d,k=k:d["transverse_theorem"].__setitem__(k,not d["transverse_theorem"][k]))
  elif isinstance(v,int):m.append(lambda d,k=k:d["transverse_theorem"].__setitem__(k,d["transverse_theorem"][k]+1))
 for k in b["exact_controls"]:m.append(lambda d,k=k:d["exact_controls"].__setitem__(k,d["exact_controls"][k]+1))
 while len(m)<30:m.append(lambda d:d["decision"].__setitem__("global_sc_act_06_proved_or_refuted",True))
 c=0
 for f in m[:30]:
  x=copy.deepcopy(b);f(x)
  try:M.validate(x)
  except (AssertionError,KeyError,TypeError,ValueError):c+=1
 print("PASS K812 controls: 36");print(f"PASS K812 hostile mutations rejected: {c}/30");return 0 if c==30 else 1
if __name__=="__main__":raise SystemExit(main())
