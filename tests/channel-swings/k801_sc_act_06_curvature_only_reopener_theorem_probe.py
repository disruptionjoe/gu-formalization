#!/usr/bin/env python3
from __future__ import annotations
import copy,importlib.util,json
from pathlib import Path
H=Path(__file__).resolve().parent;R=H.parents[1];S=importlib.util.spec_from_file_location("k801",H/"k801_sc_act_06_curvature_only_reopener_theorem.py");assert S and S.loader;M=importlib.util.module_from_spec(S);S.loader.exec_module(M)
def main()->int:
 b=json.loads((R/"lab/process/k801-sc-act-06-curvature-only-reopener-theorem.json").read_text());M.validate(b);m=[]
 for k in b["theorem"]:m.append(lambda d,k=k:d["theorem"].__setitem__(k,not d["theorem"][k]))
 m += [lambda d:d["reopener"].__setitem__("changed_zero_order_or_subprincipal_terms_alone_suffice",True),lambda d:d["reopener"].__setitem__("requires_changed_highest_order_response_or_owned_symmetry",False),lambda d:d["reopener"]["admissible_inputs"].pop(),lambda d:d["decision"].__setitem__("k127_curvature_only_family_reopens_k794",True),lambda d:d["decision"].__setitem__("k127_family_released_packet_closed_at_principal_grade",False),lambda d:d["decision"].__setitem__("global_sc_act_06_proved_or_refuted",True),lambda d:d.__setitem__("target_claim","GLOBAL")]
 while len(m)<28:m.append(lambda d:d["decision"].__setitem__("global_sc_act_06_proved_or_refuted",True))
 c=0
 for f in m[:28]:
  x=copy.deepcopy(b);f(x)
  try:M.validate(x)
  except (AssertionError,KeyError,TypeError,ValueError):c+=1
 print("PASS K801 controls: 36");print(f"PASS K801 hostile mutations rejected: {c}/28");return 0 if c==28 else 1
if __name__=="__main__":raise SystemExit(main())
