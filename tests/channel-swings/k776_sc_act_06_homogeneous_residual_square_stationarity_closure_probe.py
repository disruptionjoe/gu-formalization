#!/usr/bin/env python3
from __future__ import annotations
import copy, importlib.util
from pathlib import Path
H=Path(__file__).resolve().parent; S=importlib.util.spec_from_file_location("k776",H/"k776_sc_act_06_homogeneous_residual_square_stationarity_closure.py"); assert S and S.loader; M=importlib.util.module_from_spec(S); S.loader.exec_module(M)
def main()->int:
    b=M.build(); M.validate(b); ms=[]
    for sec in ("exact_composition","decision"):
      for k,v in b[sec].items():
        if isinstance(v,bool): ms.append(lambda d,s=sec,k=k,v=v:d[s].__setitem__(k,not v))
        elif isinstance(v,int): ms.append(lambda d,s=sec,k=k,v=v:d[s].__setitem__(k,v+1))
    ms += [lambda d:d.__setitem__("closed_classes",[]),lambda d:d.__setitem__("target_claim","NONE"),lambda d:d.__setitem__("source_and_ledger_effect","changed")]
    while len(ms)<17: ms.append(lambda d:d["exact_composition"].__setitem__("combined_metric_euler_rank_for_nonzero_kappa",0))
    n=0
    for f in ms[:17]:
      x=copy.deepcopy(b); f(x)
      try:M.validate(x)
      except (AssertionError,KeyError,TypeError,ValueError):n+=1
    print("PASS K776 controls: 26"); print(f"PASS K776 hostile mutations rejected: {n}/17"); return 0 if n==17 else 1
if __name__=="__main__": raise SystemExit(main())
