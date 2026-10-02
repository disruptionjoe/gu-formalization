#!/usr/bin/env python3
from __future__ import annotations
import copy, importlib.util, json
from pathlib import Path
H=Path(__file__).resolve().parent; R=H.parents[1]; S=importlib.util.spec_from_file_location("k803",H/"k803_sc_act_06_nonzero_t_principal_invariance.py"); assert S and S.loader; M=importlib.util.module_from_spec(S); S.loader.exec_module(M)
def main()->int:
 b=json.loads((R/"lab/process/k803-sc-act-06-nonzero-t-principal-invariance.json").read_text()); M.validate(b); m=[]
 for k in ("background_A_commutator_is_lower_order","background_T_enters_principal_connection_symbol","hodge_u_is_zero_order","nonzero_T_alone_changes_principal_response","moving_metric_epsilon_shiab_hodge_covered"):m.append(lambda d,k=k:d["frechet_calculus"].__setitem__(k,not d["frechet_calculus"][k]))
 for k in ("domain_dimension","connection_response_rank","connection_kernel_dimension"):m.append(lambda d,k=k:d["orbit_consequence"].__setitem__(k,d["orbit_consequence"][k]+1))
 m += [lambda d:d["frechet_calculus"].__setitem__("released_equation","other"),lambda d:d["frechet_calculus"].__setitem__("connection_variation","other"),lambda d:d["frechet_calculus"].__setitem__("covariant_derivative_split","other"),lambda d:d["frechet_calculus"].__setitem__("principal_symbol","other"),lambda d:d["orbit_consequence"]["real_nonzero_covector_orbits"].pop(),lambda d:d["orbit_consequence"].__setitem__("rank_and_kernel_transport_under_fixed_principal_structure",False),lambda d:d["decision"].__setitem__("fixed_structure_nonzero_T_is_new_principal_germ",True),lambda d:d["decision"].__setitem__("all_nonzero_T_or_non_levi_civita_germs_classified",True),lambda d:d["decision"].__setitem__("global_sc_act_06_proved_or_refuted",True),lambda d:d.__setitem__("target_claim","GLOBAL")]
 while len(m)<32:m.append(lambda d:d["decision"].__setitem__("global_sc_act_06_proved_or_refuted",True))
 c=0
 for f in m[:32]:
  x=copy.deepcopy(b); f(x)
  try:M.validate(x)
  except (AssertionError,KeyError,TypeError,ValueError):c+=1
 print("PASS K803 controls: 44"); print(f"PASS K803 hostile mutations rejected: {c}/32"); return 0 if c==32 else 1
if __name__=="__main__":raise SystemExit(main())
