#!/usr/bin/env python3
"""Hostile mutations for K1491."""
import copy,importlib.util
from pathlib import Path
P=Path(__file__).with_name("k1491_krylov_recentering_brst_instability.py")
S=importlib.util.spec_from_file_location("k1491",P);M=importlib.util.module_from_spec(S);S.loader.exec_module(M)
mutations=[("claim_id","K0000"),("recentering_and_brst.constant","zero"),
 ("recentering_and_brst.necessary_recentering","old"),("recentering_and_brst.explicit_window","bounded"),
 ("recentering_and_brst.weak_limit","zero"),("recentering_and_brst.mosco_failure","holds"),
 ("recentering_and_brst.brst_transfer","repair"),("decision.necessary_scalar_correction_coefficient_lower","1"),
 ("decision.old_coefficient_one_window_is_final",True),("decision.enlarged_fixed_fraction_window_spectral_bottom_diverges",False),
 ("decision.enlarged_window_mosco_weak_liminf_holds",True),("decision.harmonic_brst_factor_repairs_window",True),
 ("decision.true_ground_energy_recentering_excluded",True),("decision.changed_representation_excluded",True),
 ("decision.protected_status_change",True)]
for i,(path,value) in enumerate(mutations,1):
 d=copy.deepcopy(M.D);node=d;bits=path.split(".")
 for key in bits[:-1]:node=node[key]
 node[bits[-1]]=value
 assert not all(M.validate(d)),path;print(f"PASS {i:02d}: rejected {path}")
print(f"RESULT: PASS {len(mutations)}/{len(mutations)}")
