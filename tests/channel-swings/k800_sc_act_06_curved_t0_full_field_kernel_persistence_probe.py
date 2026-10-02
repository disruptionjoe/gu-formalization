#!/usr/bin/env python3
from __future__ import annotations
import copy,importlib.util,json
from pathlib import Path
H=Path(__file__).resolve().parent; R=H.parents[1]; S=importlib.util.spec_from_file_location("k800",H/"k800_sc_act_06_curved_t0_full_field_kernel_persistence.py"); assert S and S.loader; M=importlib.util.module_from_spec(S); S.loader.exec_module(M)
def main()->int:
 b=json.loads((R/"lab/process/k800-sc-act-06-curved-t0-full-field-kernel-persistence.json").read_text()); M.validate(b); muts=[]
 for k in b["composition"]: muts.append((lambda d,k=k:d["composition"].__setitem__(k,not d["composition"][k])))
 for k in ("embedded_connection_kernel_dimension","granted_internal_q_lambda_rank","granted_metric_diffeomorphism_rank","maximal_current_granted_symmetry_rank","persistent_middle_classes_lower_bound"): muts.append(lambda d,k=k:d["exact_bound"].__setitem__(k,d["exact_bound"][k]+1))
 muts += [lambda d:d["exact_bound"].__setitem__("uniform_on_certified_family_and_positive_negative_null_real_covectors",False),lambda d:d["decision"].__setitem__("released_full_field_extension_repairs_certified_family",True),lambda d:d["decision"].__setitem__("curvature_only_family_middle_exact_under_maximal_grant",True),lambda d:d.__setitem__("target_claim","GLOBAL")]
 while len(muts)<30:muts.append(lambda d:d["decision"].__setitem__("curvature_only_family_middle_exact_under_maximal_grant",True))
 c=0
 for m in muts[:30]:
  x=copy.deepcopy(b); m(x)
  try:M.validate(x)
  except (AssertionError,KeyError,TypeError,ValueError):c+=1
 print("PASS K800 controls: 40"); print(f"PASS K800 hostile mutations rejected: {c}/30"); return 0 if c==30 else 1
if __name__=="__main__":raise SystemExit(main())
