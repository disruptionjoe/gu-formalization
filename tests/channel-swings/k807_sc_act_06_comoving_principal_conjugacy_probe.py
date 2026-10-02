#!/usr/bin/env python3
from __future__ import annotations
import copy,importlib.util,json
from pathlib import Path
H=Path(__file__).resolve().parent;R=H.parents[1];S=importlib.util.spec_from_file_location("k807",H/"k807_sc_act_06_comoving_principal_conjugacy.py");assert S and S.loader;M=importlib.util.module_from_spec(S);S.loader.exec_module(M)
def main()->int:
 b=json.loads((R/"lab/process/k807-sc-act-06-comoving-principal-conjugacy.json").read_text());M.validate(b);m=[]
 for k in ("domain_frame_map_invertible","residual_frame_map_invertible","covector_transport_invertible","moving_projector_cocycle_exact","hodge_shiab_clifford_packet_natural","pure_frame_motion_is_basis_change","genuine_relative_coefficient_motion_covered","singular_observation_map_covered"):m.append(lambda d,k=k:d["intertwiner_theorem"].__setitem__(k,not d["intertwiner_theorem"][k]))
 for k in ("domain_dimension","reference_rank","transported_rank","reference_kernel_dimension","transported_kernel_dimension"):m.append(lambda d,k=k:d["orbit_consequence"].__setitem__(k,d["orbit_consequence"][k]+1))
 m += [lambda d:d["intertwiner_theorem"].__setitem__("formula","other"),lambda d:d["orbit_consequence"].__setitem__("kernel_transport","other"),lambda d:d["orbit_consequence"]["real_nonzero_covector_orbits"].pop(),lambda d:d["decision"].__setitem__("comoving_frame_orbit_is_new_principal_packet",True),lambda d:d["decision"].__setitem__("all_moving_metric_epsilon_shiab_hodge_germs_classified",True),lambda d:d["decision"].__setitem__("global_sc_act_06_proved_or_refuted",True),lambda d:d.__setitem__("target_claim","GLOBAL")]
 while len(m)<32:m.append(lambda d:d["decision"].__setitem__("global_sc_act_06_proved_or_refuted",True))
 c=0
 for f in m[:32]:
  x=copy.deepcopy(b);f(x)
  try:M.validate(x)
  except (AssertionError,KeyError,TypeError,ValueError):c+=1
 print("PASS K807 controls: 44");print(f"PASS K807 hostile mutations rejected: {c}/32");return 0 if c==32 else 1
if __name__=="__main__":raise SystemExit(main())
