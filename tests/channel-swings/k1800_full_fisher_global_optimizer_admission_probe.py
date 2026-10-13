#!/usr/bin/env python3
"""Hostile mutations for K1800's protected admission ceiling."""
import copy,importlib.util,json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];SOURCE=ROOT/"tests/channel-swings/k1800_full_fisher_global_optimizer_admission.py";spec=importlib.util.spec_from_file_location("k1800_probe_target",SOURCE);module=importlib.util.module_from_spec(spec);spec.loader.exec_module(module);base=json.loads(module.ARTIFACT.read_text())
mutations=[(("bridge_census","total"),501),(("protected_state","canon_changed"),True),(("entry_state","degree_eleven_exact_partition_replayed"),False),(("entry_state","complete_complement_cover_available"),True),(("decision","slab_one_globally_excluded"),False),(("decision","slab_two_globally_excluded"),True),(("decision","unique_stationary_point_on_complete_slab_three"),True),(("decision","all_residual_faces_and_corners_closed"),True),(("decision","global_optimizer_proved"),True),(("decision","source_owned_physical_theory"),True)]
def setp(data,path,value):
    for key in path[:-1]:data=data[key]
    data[path[-1]]=value
for index,(path,value) in enumerate(mutations,1):
    mutant=copy.deepcopy(base);setp(mutant,path,value);assert not all(ok for _,ok in module.validate(mutant)),path;print(f"REJECT {index:02d}: {path}")
print(f"RESULT: PASS {len(mutations)}/{len(mutations)}")
