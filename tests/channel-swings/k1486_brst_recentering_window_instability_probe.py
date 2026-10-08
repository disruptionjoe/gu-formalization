#!/usr/bin/env python3
"""Hostile mutations for K1486."""
import copy,importlib.util
from pathlib import Path
P=Path(__file__).with_name("k1486_brst_recentering_window_instability.py");S=importlib.util.spec_from_file_location("k1486",P);M=importlib.util.module_from_spec(S);S.loader.exec_module(M)
mutations=[("claim_id","K0"),("brst_window_transfer.full_family","wrong"),("brst_window_transfer.harmonic_vacuum","wrong"),("brst_window_transfer.spectral_transfer","bounded"),("brst_window_transfer.weak_transfer","zero"),("brst_window_transfer.mosco_transfer","holds"),("decision.excluded_scalar_window_transfers_to_full_brst",False),("decision.excluded_scalar_window_transfers_to_harmonic_compression",False),("decision.brst_window_weak_liminf_holds",True),("decision.finite_cutoff_nilpotence_invalidated",True),("decision.continuum_interacting_brst_constructed",True),("decision.protected_status_change",True)]
for i,(path,value) in enumerate(mutations,1):
 d=copy.deepcopy(M.D);node=d;bits=path.split(".")
 for key in bits[:-1]:node=node[key]
 node[bits[-1]]=value;assert not all(M.validate(d)),path;print(f"PASS {i:02d}: rejected {path}")
print(f"RESULT: PASS {len(mutations)}/{len(mutations)}")
