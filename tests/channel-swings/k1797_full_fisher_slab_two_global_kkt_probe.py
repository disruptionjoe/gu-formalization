#!/usr/bin/env python3
"""Hostile mutations for K1797's slab-two admission boundary."""
import copy,importlib.util,json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];SOURCE=ROOT/"tests/channel-swings/k1797_full_fisher_slab_two_global_kkt.py"
spec=importlib.util.spec_from_file_location("k1797_probe_target",SOURCE);module=importlib.util.module_from_spec(spec);spec.loader.exec_module(module);base=json.loads(module.ARTIFACT.read_text())
mutations=[(("certificate","retained_leaves"),0),(("certificate","retained_fraction_of_slab_input_area"),"0"),(("decision","local_boundary_kkt_isolated"),False),(("decision","strict_outer_frontier_contraction"),False),(("decision","complete_slab_two_sublevel_excluded"),True),(("decision","every_slab_two_face_and_corner_closed"),True),(("decision","global_optimizer_proved"),True)]
def setp(data,path,value):
    for key in path[:-1]:data=data[key]
    data[path[-1]]=value
for index,(path,value) in enumerate(mutations,1):
    mutant=copy.deepcopy(base);setp(mutant,path,value);assert not all(ok for _,ok in module.validate(mutant)),path;print(f"REJECT {index:02d}: {path}")
print(f"RESULT: PASS {len(mutations)}/{len(mutations)}")
