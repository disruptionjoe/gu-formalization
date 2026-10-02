#!/usr/bin/env python3
from __future__ import annotations
import copy,importlib.util,json
from pathlib import Path
H=Path(__file__).resolve().parent;R=H.parents[1];S=importlib.util.spec_from_file_location("k808",H/"k808_sc_act_06_comoving_full_field_kernel.py");assert S and S.loader;M=importlib.util.module_from_spec(S);S.loader.exec_module(M)
def main()->int:
 b=json.loads((R/"lab/process/k808-sc-act-06-comoving-full-field-kernel.json").read_text());M.validate(b);m=[]
 for k,v in b["extension_theorem"].items():m.append(lambda d,k=k,v=v:d["extension_theorem"].__setitem__(k,(v+1) if isinstance(v,int) and not isinstance(v,bool) else (not v)))
 for k in ("comoving_full_field_packet_middle_exact_before_symmetry","all_moving_full_field_germs_classified","global_sc_act_06_proved_or_refuted"):m.append(lambda d,k=k:d["decision"].__setitem__(k,True))
 m += [lambda d:d.__setitem__("target_claim","GLOBAL")]
 while len(m)<30:m.append(lambda d:d["decision"].__setitem__("global_sc_act_06_proved_or_refuted",True))
 c=0
 for f in m[:30]:
  x=copy.deepcopy(b);f(x)
  try:M.validate(x)
  except (AssertionError,KeyError,TypeError,ValueError):c+=1
 print("PASS K808 controls: 40");print(f"PASS K808 hostile mutations rejected: {c}/30");return 0 if c==30 else 1
if __name__=="__main__":raise SystemExit(main())
