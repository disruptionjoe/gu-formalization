#!/usr/bin/env python3
"""Independent hostile mutations for K1327."""
import copy,json
from pathlib import Path
D=json.loads((Path(__file__).resolve().parents[2]/"lab/process/k1327-spherical-coefficient-meromorphic-divisor.json").read_text())
def valid(x):
 m=x["meromorphic_divisor"]; u=x["unitary_axis"]; r=x["d7_regular_charge"]; q=x["decision"]; return m["simple_poles"]=="z=0,-2,-4,..." and m["simple_zeros"]=="z=-1,-3,-5,..." and m["imaginary_axis"]=="finite_nonzero_except_z=0" and u["regularity_condition"]=="t!=0" and u["phase_modulus"]==1 and r["positive_root_count"]==42 and r["singular_wall_excluded"] and q["meromorphic_scalar_divisor_classified"] and not q["operator_pole_and_reducibility_classification_constructed"]
mut=[(("meromorphic_divisor","simple_poles"),"z=-1,-3,..."),(("meromorphic_divisor","simple_zeros"),"none"),(("meromorphic_divisor","imaginary_axis"),"entire"),(("unitary_axis","regularity_condition"),"all t"),(("unitary_axis","phase_modulus"),0),(("d7_regular_charge","positive_root_count"),41),(("d7_regular_charge","singular_wall_excluded"),False),(("decision","operator_pole_and_reducibility_classification_constructed"),True)]
for i,(path,value) in enumerate(mut,1):
 x=copy.deepcopy(D); x[path[0]][path[1]]=value; assert not valid(x),path; print(f"REJECT {i:02d}: {path[1]}")
assert valid(D); print("RESULT: PASS 8/8 hostile mutations rejected")
