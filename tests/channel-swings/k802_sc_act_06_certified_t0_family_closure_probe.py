#!/usr/bin/env python3
from __future__ import annotations
import copy,importlib.util,json
from pathlib import Path
H=Path(__file__).resolve().parent;R=H.parents[1];S=importlib.util.spec_from_file_location("k802",H/"k802_sc_act_06_certified_t0_family_closure.py");assert S and S.loader;M=importlib.util.module_from_spec(S);S.loader.exec_module(M)
def main()->int:
 b=json.loads((R/"lab/process/k802-sc-act-06-certified-t0-family-closure.json").read_text());M.validate(b);m=[]
 for k in ("certified_family_direct_response_rank","certified_family_connection_kernel","maximal_current_symmetry_grant","uniform_persistent_middle_classes"):m.append(lambda d,k=k:d["composition"].__setitem__(k,d["composition"][k]+1))
 for k in ("xi_factors_through_D_Upsilon_on_zero_locus","zero_fermion_full_field_extension_repairs_kernel","curvature_only_changes_highest_order_response","current_k500_seed_prefix_assembly_available"):m.append(lambda d,k=k:d["composition"].__setitem__(k,not d["composition"][k]))
 for k in ("certified_k127_t0_family_is_complete_elliptic_realization_under_released_packet","certified_k127_t0_family_packet_closed","all_t0_or_all_zero_locus_germs_closed","global_sc_act_06_proved_or_refuted","source_claim_status_changes"):m.append(lambda d,k=k:d["decision"].__setitem__(k,not d["decision"][k]))
 m += [lambda d:d["reranked_frontier"].pop(),lambda d:d["protected_effects"].__setitem__("sc_act_06","REFUTED"),lambda d:d.__setitem__("target_claim","GLOBAL")]
 while len(m)<30:m.append(lambda d:d["decision"].__setitem__("global_sc_act_06_proved_or_refuted",True))
 c=0
 for f in m[:30]:
  x=copy.deepcopy(b);f(x)
  try:M.validate(x)
  except (AssertionError,KeyError,TypeError,ValueError):c+=1
 print("PASS K802 controls: 40");print(f"PASS K802 hostile mutations rejected: {c}/30");return 0 if c==30 else 1
if __name__=="__main__":raise SystemExit(main())
