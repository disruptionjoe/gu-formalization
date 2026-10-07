#!/usr/bin/env python3
"""Data-mutation probe for K1368."""
import copy,json
from pathlib import Path
D=json.loads((Path(__file__).resolve().parents[2]/"lab/process/k1368-regularizer-symmetry-normalization-boundary.json").read_text())
def validate(x):
 s,n,q=x["symmetry_classification"],x["normalization_classification"],x["decision"]; e=[]
 if "U*Q^2U=Q^2" not in s["invariance_group"]:e.append("invariance group")
 if "Schur" not in s["full_G_test"]:e.append("Schur test")
 if "mu/c^2" not in n["rescaling_degeneracy"]:e.append("rescaling")
 if "Q and -Q" not in n["sign_degeneracy"]:e.append("sign")
 if not q["exact_Q_squared_invariance_group_classified"]:e.append("classification")
 if q["full_split_G_invariance"]:e.append("full G overclaim")
 if q["charge_sign_selected"]:e.append("sign overclaim")
 if q["charge_normalization_selected"]:e.append("normalization overclaim")
 if q["primitive_compact_generator_source_selected"]:e.append("source overclaim")
 if q["regularizer_reduces_canonicity_distance"]:e.append("distance overclaim")
 return e
assert not validate(D),validate(D)
mutations=[
 ("invariance group",lambda x:x["symmetry_classification"].__setitem__("invariance_group","all unitaries")),
 ("Schur test",lambda x:x["symmetry_classification"].__setitem__("full_G_test","unknown")),
 ("rescaling",lambda x:x["normalization_classification"].__setitem__("rescaling_degeneracy","none")),
 ("sign",lambda x:x["normalization_classification"].__setitem__("sign_degeneracy","none")),
 ("classification",lambda x:x["decision"].__setitem__("exact_Q_squared_invariance_group_classified",False)),
 ("full G overclaim",lambda x:x["decision"].__setitem__("full_split_G_invariance",True)),
 ("sign overclaim",lambda x:x["decision"].__setitem__("charge_sign_selected",True)),
 ("normalization overclaim",lambda x:x["decision"].__setitem__("charge_normalization_selected",True)),
 ("source overclaim",lambda x:x["decision"].__setitem__("primitive_compact_generator_source_selected",True)),
 ("distance overclaim",lambda x:x["decision"].__setitem__("regularizer_reduces_canonicity_distance",True)),
]
for i,(label,mutate) in enumerate(mutations,1):
 x=copy.deepcopy(D);mutate(x);errors=validate(x);assert errors,label;print(f"PASS {i:02d}: rejects {label} via [FAIL] {errors[0]}")
print("RESULT: PASS 10/10")
