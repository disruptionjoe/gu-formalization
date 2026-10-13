#!/usr/bin/env python3
"""Hostile mutations for K1798's slab-three admission boundary."""
import copy,importlib.util,json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];SOURCE=ROOT/"tests/channel-swings/k1798_full_fisher_slab_three_global_stationarity.py";spec=importlib.util.spec_from_file_location("k1798_probe_target",SOURCE);module=importlib.util.module_from_spec(spec);spec.loader.exec_module(module);base=json.loads(module.ARTIFACT.read_text())
mutations=[(("certificate","retained_leaves"),0),(("certificate","retained_fraction_of_slab_input_area"),"0"),(("certificate","named_local_stationary_box_strictly_isolated"),False),(("decision","strict_outer_frontier_contraction"),False),(("decision","unique_stationary_point_on_complete_slab_three"),True),(("decision","every_slab_three_face_and_corner_closed"),True),(("decision","global_optimizer_proved"),True)]
def setp(data,path,value):
    for key in path[:-1]:data=data[key]
    data[path[-1]]=value
for index,(path,value) in enumerate(mutations,1):
    mutant=copy.deepcopy(base);setp(mutant,path,value);assert not all(ok for _,ok in module.validate(mutant)),path;print(f"REJECT {index:02d}: {path}")
print(f"RESULT: PASS {len(mutations)}/{len(mutations)}")
