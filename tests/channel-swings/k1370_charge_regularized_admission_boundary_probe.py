#!/usr/bin/env python3
"""Data-mutation probe for K1370."""
import copy,json
from pathlib import Path
D=json.loads((Path(__file__).resolve().parents[2]/"lab/process/k1370-charge-regularized-admission-boundary.json").read_text())
def validate(x):
 b,q=x["bridge_census"],x["decision"]; e=[]
 if b["row_count"]!=b["satisfied_count"]+b["conditional_count"]+b["excluded_count"]+b["missing_count"]:e.append("census sum")
 if b["row_count"]!=45:e.append("row count")
 if len(b["new_satisfied_rows"])!=3:e.append("new satisfied")
 if len(b["new_excluded_rows"])!=1:e.append("new excluded")
 if len(b["missing_rows"])!=4:e.append("missing rows")
 if not q["charge_coercive_repository_regularized_action_constructed"]:e.append("regularizer")
 if not q["positive_completed_vacuum_linearized_BRST_cohomology_constructed"]:e.append("linear cohomology")
 if q["regularizer_selects_Q_sign_or_normalization"]:e.append("selection overclaim")
 if q["fully_coupled_global_nonlinear_BV_BFV_domain_constructed"]:e.append("nonlinear overclaim")
 if q["positive_GU_physical_Hilbert_cohomology_constructed"]:e.append("physical overclaim")
 return e
assert not validate(D),validate(D)
mutations=[
 ("census sum",lambda x:x["bridge_census"].__setitem__("satisfied_count",31)),
 ("row count",lambda x:x["bridge_census"].__setitem__("row_count",44)),
 ("new satisfied",lambda x:x["bridge_census"].__setitem__("new_satisfied_rows",[])),
 ("new excluded",lambda x:x["bridge_census"].__setitem__("new_excluded_rows",[])),
 ("missing rows",lambda x:x["bridge_census"].__setitem__("missing_rows",[])),
 ("regularizer",lambda x:x["decision"].__setitem__("charge_coercive_repository_regularized_action_constructed",False)),
 ("linear cohomology",lambda x:x["decision"].__setitem__("positive_completed_vacuum_linearized_BRST_cohomology_constructed",False)),
 ("selection overclaim",lambda x:x["decision"].__setitem__("regularizer_selects_Q_sign_or_normalization",True)),
 ("nonlinear overclaim",lambda x:x["decision"].__setitem__("fully_coupled_global_nonlinear_BV_BFV_domain_constructed",True)),
 ("physical overclaim",lambda x:x["decision"].__setitem__("positive_GU_physical_Hilbert_cohomology_constructed",True)),
]
for i,(label,mutate) in enumerate(mutations,1):
 x=copy.deepcopy(D);mutate(x);errors=validate(x);assert errors,label;print(f"PASS {i:02d}: rejects {label} via [FAIL] {errors[0]}")
print("RESULT: PASS 10/10")
