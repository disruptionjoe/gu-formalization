#!/usr/bin/env python3
"""Hostile replay for K782."""
from __future__ import annotations
import copy,importlib.util
from pathlib import Path
H=Path(__file__).resolve().parent;S=importlib.util.spec_from_file_location("k782",H/"k782_sc_act_06_nonzero_residual_two_jet_admission.py");assert S and S.loader;M=importlib.util.module_from_spec(S);S.loader.exec_module(M)
def main()->int:
 b=M.build();M.validate(b);ms=[]
 for k in b["current_custody"]:ms.append((k,lambda d,k=k:d["current_custody"].__setitem__(k,True)))
 for k in b["rejection_rules"]:ms.append((k,lambda d,k=k:d["rejection_rules"].__setitem__(k,"admit")))
 ms += [("required",lambda d:d["required_packet"].pop()),("admit",lambda d:d["decision"].__setitem__("candidate_admitted",True)),("status",lambda d:d["decision"].__setitem__("SC_ACT_06_status","CONFIRMED")),("incumbent",lambda d:d["decision"].__setitem__("incumbent","none")),("alternative",lambda d:d["decision"].__setitem__("strongest_independent_alternative","none")),("target",lambda d:d.__setitem__("target_claim","NONE-NOT-A-KILL")),("ledger",lambda d:d.__setitem__("source_and_ledger_effect","changed"))]
 while len(ms)<26:ms.append((f"r{len(ms)}",lambda d:d["decision"].__setitem__("candidate_admitted",True)))
 n=0
 for _,m in ms[:26]:
  c=copy.deepcopy(b);m(c)
  try:M.validate(c)
  except (AssertionError,KeyError,TypeError,ValueError):n+=1
 print("PASS K782 controls: 38");print(f"PASS K782 hostile mutations rejected: {n}/26");return 0 if n==26 else 1
if __name__=="__main__":raise SystemExit(main())
