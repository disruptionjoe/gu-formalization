#!/usr/bin/env python3
"""Hostile certificate and scope mutations for K1753."""
import copy,importlib.util,json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];P=ROOT/"tests/channel-swings/k1753_arb_rational_interior_improvement.py"
s=importlib.util.spec_from_file_location("producer",P);m=importlib.util.module_from_spec(s);s.loader.exec_module(m)
base=json.loads(m.ARTIFACT.read_text()); mutations=[
 (("backend",),"binary-float quadrature"),
 (("certificate","comparison"),"J_candidate-J_selected"),
 (("decision","rational_candidate_strictly_better"),False),
 (("decision","k1749_selected_linear_finite_strength_optimality"),True),
 (("decision","whole_chart_global_optimizer_proved"),True),
 (("scope_guard",),"This proves all-seed physical optimality.")]
def setp(d,path,val):
 for k in path[:-1]:d=d[k]
 d[path[-1]]=val
for i,(path,val) in enumerate(mutations,1):
 d=copy.deepcopy(base);setp(d,path,val);assert not all(ok for _,ok in m.validate(d)),path;print(f"PASS {i:02d}: rejected {'.'.join(path)}")
print(f"RESULT: PASS {len(mutations)}/{len(mutations)}")
