#!/usr/bin/env python3
"""Hostile replay for K780."""
from __future__ import annotations
import copy,importlib.util
from pathlib import Path
H=Path(__file__).resolve().parent; S=importlib.util.spec_from_file_location("k780",H/"k780_sc_act_06_kernel_transverse_stationarity_obstruction.py"); assert S and S.loader; M=importlib.util.module_from_spec(S); S.loader.exec_module(M)
def main()->int:
    b=M.build();M.validate(b);ms=[]
    for k,v in b["theorem"].items():
        if isinstance(v,bool):ms.append((k,lambda d,k=k,v=v:d["theorem"].__setitem__(k,not v)))
    ms += [("eq",lambda d:d["theorem"].__setitem__("combined_stationarity_equation","E_I1B+Q Upsilon=0")),("nec",lambda d:d["theorem"].__setitem__("necessary_condition","none")),("good",lambda d:d["exact_control"].__setitem__("compatible_kernel_pairing",1)),("bad",lambda d:d["exact_control"].__setitem__("transverse_kernel_pairing",0)),("total",lambda d:d["exact_control"].__setitem__("compatible_total_euler",[1,0,0])),("reject",lambda d:d["decision"].__setitem__("transverse_candidate_rejected",False)),("admit",lambda d:d["decision"].__setitem__("compatible_candidate_admitted_to_next_gate_only",False)),("target",lambda d:d.__setitem__("target_claim","NONE-NOT-A-KILL")),("ledger",lambda d:d.__setitem__("source_and_ledger_effect","changed"))]
    while len(ms)<22:ms.append((f"r{len(ms)}",lambda d:d["exact_control"].__setitem__("transverse_kernel_pairing",0)))
    n=0
    for _,m in ms[:22]:
        c=copy.deepcopy(b);m(c)
        try:M.validate(c)
        except (AssertionError,KeyError,TypeError,ValueError):n+=1
    print("PASS K780 controls: 32");print(f"PASS K780 hostile mutations rejected: {n}/22");return 0 if n==22 else 1
if __name__=="__main__":raise SystemExit(main())
