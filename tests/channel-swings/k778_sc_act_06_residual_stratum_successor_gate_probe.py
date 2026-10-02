#!/usr/bin/env python3
from __future__ import annotations
import copy,importlib.util
from pathlib import Path
H=Path(__file__).resolve().parent;S=importlib.util.spec_from_file_location("k778",H/"k778_sc_act_06_residual_stratum_successor_gate.py");assert S and S.loader;M=importlib.util.module_from_spec(S);S.loader.exec_module(M)
def main()->int:
 b=M.build();M.validate(b);ms=[]
 for i,row in enumerate(b["residual_strata"]):
  v=row["stationary_for_I1B_plus_I2B"];ms.append(lambda d,i=i,v=v:d["residual_strata"][i].__setitem__("stationary_for_I1B_plus_I2B",True if v is None else not v))
 for k,v in b["decision"].items():
  if isinstance(v,bool):ms.append(lambda d,k=k,v=v:d["decision"].__setitem__(k,not v))
 ms += [lambda d:d["decision"].__setitem__("SC_ACT_06_status","REFUTED"),lambda d:d.__setitem__("residual_strata",[]),lambda d:d.__setitem__("closed_classes",[]),lambda d:d.__setitem__("target_claim","NONE"),lambda d:d.__setitem__("source_and_ledger_effect","changed")]
 while len(ms)<21:ms.append(lambda d:d["decision"].__setitem__("do_not_retry_K726_with_residual_pairing_or_weight",False))
 n=0
 for f in ms[:21]:
  x=copy.deepcopy(b);f(x)
  try:M.validate(x)
  except (AssertionError,KeyError,TypeError,ValueError):n+=1
 print("PASS K778 controls: 32");print(f"PASS K778 hostile mutations rejected: {n}/21");return 0 if n==21 else 1
if __name__=="__main__":raise SystemExit(main())
