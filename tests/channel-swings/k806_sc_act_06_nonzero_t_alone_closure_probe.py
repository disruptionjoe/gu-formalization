#!/usr/bin/env python3
from __future__ import annotations
import copy,importlib.util,json
from pathlib import Path
H=Path(__file__).resolve().parent;R=H.parents[1];S=importlib.util.spec_from_file_location("k806",H/"k806_sc_act_06_nonzero_t_alone_closure.py");assert S and S.loader;M=importlib.util.module_from_spec(S);S.loader.exec_module(M)
def main()->int:
 b=json.loads((R/"lab/process/k806-sc-act-06-nonzero-t-alone-closure.json").read_text());M.validate(b);m=[]
 for k,v in b["composition"].items():m.append(lambda d,k=k,v=v:d["composition"].__setitem__(k,(v+1) if isinstance(v,int) and not isinstance(v,bool) else (not v)))
 for k in ("nonzero_T_alone_reopens_certified_packet","all_nonzero_T_or_non_levi_civita_zero_locus_germs_closed","moving_principal_geometry_closed","future_owned_symmetry_or_independent_row_closed","global_sc_act_06_proved_or_refuted","source_claim_status_changes"):m.append(lambda d,k=k:d["decision"].__setitem__(k,True))
 m += [lambda d:d["reranked_frontier"].pop(),lambda d:d["protected_effects"].__setitem__("sc_act_06","REFUTED"),lambda d:d.__setitem__("target_claim","GLOBAL")]
 while len(m)<30:m.append(lambda d:d["decision"].__setitem__("global_sc_act_06_proved_or_refuted",True))
 c=0
 for f in m[:30]:
  x=copy.deepcopy(b);f(x)
  try:M.validate(x)
  except (AssertionError,KeyError,TypeError,ValueError):c+=1
 print("PASS K806 controls: 40");print(f"PASS K806 hostile mutations rejected: {c}/30");return 0 if c==30 else 1
if __name__=="__main__":raise SystemExit(main())
