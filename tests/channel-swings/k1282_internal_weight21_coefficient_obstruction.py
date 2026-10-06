#!/usr/bin/env python3
"""Exact controls for K1282."""
import json
from pathlib import Path
D=json.loads((Path(__file__).resolve().parents[2]/"lab/process/k1282-internal-weight21-coefficient-obstruction.json").read_text()); n=0
def c(label,x):
    global n; assert x,label; n+=1; print(f"PASS {n:02d}: {label}")
def count_even(rem, weights=(2,4,6,8,10,12)):
    if not weights: return int(rem==0)
    return sum(count_even(rem-a*weights[0],weights[1:]) for a in range(rem//weights[0]+1))
classes=[]
for j in range(4):
    rem=21-7*j
    if rem>=0: classes.extend([j]*count_even(rem))
c("id",D["result_id"]=="K1282-INTERNAL-WEIGHT21-COEFFICIENT-OBSTRUCTION")
c("fifteen classes",len(classes)==15==D["coefficient_census"]["monomial_exponent_classes"])
c("p exponents",sorted(set(classes))==[1,3])
c("all odd",all(j%2 for j in classes))
for p in (-5,-2,1,4):
    epsilon=p**3+3*p
    c(f"coefficient odd p={p}",(-p)**3+3*(-p)==-epsilon)
    c(f"product even p={p}",epsilon*p==(((-p)**3+3*(-p))*(-p)))
c("fixed tilt excluded",D["decision"]["internally_generated_homogeneous_weight21_coefficient_supplies_fixed_odd_tilt"] is False)
c("external data",D["decision"]["fixed_scalar_or_independently_transforming_spurion_is_extra_data"] is True)
assert n==14; print("RESULT: PASS 14/14")
