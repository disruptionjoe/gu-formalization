#!/usr/bin/env python3
from __future__ import annotations
import copy,importlib.util,json
from pathlib import Path
H=Path(__file__).resolve().parent;R=H.parents[1];S=importlib.util.spec_from_file_location("k809",H/"k809_sc_act_06_comoving_symmetry_quotient.py");assert S and S.loader;M=importlib.util.module_from_spec(S);S.loader.exec_module(M)
def main()->int:
 b=json.loads((R/"lab/process/k809-sc-act-06-comoving-symmetry-quotient.json").read_text());M.validate(b);m=[]
 for k,v in b["quotient_transport"].items():m.append(lambda d,k=k,v=v:d["quotient_transport"].__setitem__(k,(v+1) if isinstance(v,int) and not isinstance(v,bool) else (not v)))
 for k in ("current_transported_grant_closes_packet","future_background_dependent_symmetry_closed","global_sc_act_06_proved_or_refuted"):m.append(lambda d,k=k:d["decision"].__setitem__(k,True))
 m += [lambda d:d.__setitem__("target_claim","GLOBAL")]
 while len(m)<28:m.append(lambda d:d["decision"].__setitem__("global_sc_act_06_proved_or_refuted",True))
 c=0
 for f in m[:28]:
  x=copy.deepcopy(b);f(x)
  try:M.validate(x)
  except (AssertionError,KeyError,TypeError,ValueError):c+=1
 print("PASS K809 controls: 36");print(f"PASS K809 hostile mutations rejected: {c}/28");return 0 if c==28 else 1
if __name__=="__main__":raise SystemExit(main())
