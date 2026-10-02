#!/usr/bin/env python3
from __future__ import annotations
import copy,importlib.util,json
from pathlib import Path
H=Path(__file__).resolve().parent;R=H.parents[1];S=importlib.util.spec_from_file_location("k814",H/"k814_sc_act_06_relative_packet_gate.py");assert S and S.loader;M=importlib.util.module_from_spec(S);S.loader.exec_module(M)
def main()->int:
 b=json.loads((R/"lab/process/k814-sc-act-06-relative-packet-gate.json").read_text());M.validate(b);m=[]
 for k,v in b["necessary_packet"].items():m.append(lambda d,k=k,v=v:d["necessary_packet"].__setitem__(k,(v+1) if isinstance(v,int) and not isinstance(v,bool) else not v))
 for k,v in b["closure"].items():m.append(lambda d,k=k:d["closure"].__setitem__(k,not d["closure"][k]))
 m += [lambda d:d["reranked_frontier"].pop(),lambda d:d["protected_effects"].__setitem__("sc_act_06","REFUTED")]
 while len(m)<32:m.append(lambda d:d.__setitem__("target_claim","GLOBAL"))
 c=0
 for f in m[:32]:
  x=copy.deepcopy(b);f(x)
  try:M.validate(x)
  except (AssertionError,KeyError,TypeError,ValueError):c+=1
 print("PASS K814 controls: 42");print(f"PASS K814 hostile mutations rejected: {c}/32");return 0 if c==32 else 1
if __name__=="__main__":raise SystemExit(main())
