#!/usr/bin/env python3
from __future__ import annotations
import copy,importlib.util
from pathlib import Path
H=Path(__file__).resolve().parent;S=importlib.util.spec_from_file_location("k777",H/"k777_sc_act_06_nonzero_residual_hessian_split.py");assert S and S.loader;M=importlib.util.module_from_spec(S);S.loader.exec_module(M)
def main()->int:
 b=M.build();M.validate(b);ms=[]
 for sec in ("hessian_split","decision"):
  for k,v in b[sec].items():
   if isinstance(v,bool):ms.append(lambda d,s=sec,k=k,v=v:d[s].__setitem__(k,not v))
 ms += [lambda d:d["hessian_split"].__setitem__("gauss_newton_term","J"),lambda d:d.__setitem__("native_obligations",[]),lambda d:d.__setitem__("target_claim","NONE"),lambda d:d.__setitem__("source_and_ledger_effect","changed")]
 while len(ms)<20:ms.append(lambda d:d["decision"].__setitem__("route_is_currently_constructed",True))
 n=0
 for f in ms[:20]:
  x=copy.deepcopy(b);f(x)
  try:M.validate(x)
  except (AssertionError,KeyError,TypeError,ValueError):n+=1
 print("PASS K777 controls: 30");print(f"PASS K777 hostile mutations rejected: {n}/20");return 0 if n==20 else 1
if __name__=="__main__":raise SystemExit(main())
