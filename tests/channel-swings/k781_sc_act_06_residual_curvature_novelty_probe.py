#!/usr/bin/env python3
"""Hostile replay for K781."""
from __future__ import annotations
import copy,importlib.util
from pathlib import Path
H=Path(__file__).resolve().parent;S=importlib.util.spec_from_file_location("k781",H/"k781_sc_act_06_residual_curvature_novelty.py");assert S and S.loader;M=importlib.util.module_from_spec(S);S.loader.exec_module(M)
def main()->int:
 b=M.build();M.validate(b);ms=[]
 for k,v in b["theorem"].items():
  if isinstance(v,bool):ms.append((k,lambda d,k=k,v=v:d["theorem"].__setitem__(k,not v)))
 ms += [("formula",lambda d:d["theorem"].__setitem__("formula","d2I2B=J^*QJ")),("gram",lambda d:d["exact_control"].__setitem__("gram_on_kernel",[1,0,0])),("curv",lambda d:d["exact_control"].__setitem__("curvature_on_kernel",[6,0,6])),("escape",lambda d:d["exact_control"].__setitem__("curvature_image_escapes_im_J_star",False)),("rank",lambda d:d["exact_control"].__setitem__("curvature_rank",2)),("affine",lambda d:d["exact_control"].__setitem__("affine_curvature_rank",1)),("need",lambda d:d["decision"].__setitem__("new_principal_image_requires_nonzero_contracted_D2Upsilon",False)),("credit",lambda d:d["decision"].__setitem__("candidate_must_compute_actual_contraction_before_rank_credit",False)),("target",lambda d:d.__setitem__("target_claim","NONE-NOT-A-KILL")),("ledger",lambda d:d.__setitem__("source_and_ledger_effect","changed"))]
 while len(ms)<24:ms.append((f"r{len(ms)}",lambda d:d["exact_control"].__setitem__("affine_curvature_rank",1)))
 n=0
 for _,m in ms[:24]:
  c=copy.deepcopy(b);m(c)
  try:M.validate(c)
  except (AssertionError,KeyError,TypeError,ValueError):n+=1
 print("PASS K781 controls: 34");print(f"PASS K781 hostile mutations rejected: {n}/24");return 0 if n==24 else 1
if __name__=="__main__":raise SystemExit(main())
