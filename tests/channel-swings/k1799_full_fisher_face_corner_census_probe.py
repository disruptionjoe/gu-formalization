#!/usr/bin/env python3
"""Hostile mutations for K1799's residual boundary census."""
import copy,importlib.util,json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];SOURCE=ROOT/"tests/channel-swings/k1799_full_fisher_face_corner_census.py";spec=importlib.util.spec_from_file_location("k1799_probe_target",SOURCE);module=importlib.util.module_from_spec(spec);spec.loader.exec_module(module);base=json.loads(module.ARTIFACT.read_text())
mutations=[(("census","retained_terminal_leaves"),84),(("census","box_local_face_incidences"),339),(("census","box_local_corner_incidences"),339),(("census","face_incidences_remaining"),0),(("census","corner_incidences_remaining"),0),(("census","incidence_count_is_unique_geometric_boundary_count"),True),(("decision","all_residual_faces_closed"),True),(("decision","global_optimizer_proved"),True)]
def setp(data,path,value):
    for key in path[:-1]:data=data[key]
    data[path[-1]]=value
for index,(path,value) in enumerate(mutations,1):
    mutant=copy.deepcopy(base);setp(mutant,path,value);assert not all(ok for _,ok in module.validate(mutant)),path;print(f"REJECT {index:02d}: {path}")
print(f"RESULT: PASS {len(mutations)}/{len(mutations)}")
