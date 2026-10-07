#!/usr/bin/env python3
"""Data-mutation probe for K1374."""
import copy,json
from pathlib import Path
D=json.loads((Path(__file__).resolve().parents[2]/"lab/process/k1374-smooth-constraint-propagation-brst.json").read_text())
def validate(x):
 s,b,q=x["smooth_identity"],x["brst"],x["decision"];e=[]
 if "mu Q^2" not in s["matter_equation"]:e.append("equation")
 if "partial_mu j^mu=0" not in s["continuity"]:e.append("continuity")
 if "partial_t(div E-j^0)=0" not in s["gauss_propagation"]:e.append("propagation")
 if "not an existence theorem" not in s["conditionality"]:e.append("conditionality")
 if "sphi=i e c Qphi" not in b["rules"]:e.append("BRST")
 if not q["smooth_noether_continuity_proved"]:e.append("continuity decision")
 if not q["smooth_gauss_constraint_propagation_proved"]:e.append("propagation decision")
 if q["global_graph_solution_exists"]:e.append("existence overclaim")
 if q["closed_nonlinear_KT_range_proved"]:e.append("KT overclaim")
 if q["positive_GU_physical_cohomology_proved"]:e.append("cohomology overclaim")
 return e
assert not validate(D),validate(D)
mutations=[
 ("equation",lambda x:x["smooth_identity"].__setitem__("matter_equation","free scalar")),
 ("continuity",lambda x:x["smooth_identity"].__setitem__("continuity","unknown")),
 ("propagation",lambda x:x["smooth_identity"].__setitem__("gauss_propagation","unknown")),
 ("conditionality",lambda x:x["smooth_identity"].__setitem__("conditionality","global theorem")),
 ("BRST",lambda x:x["brst"].__setitem__("rules","linearized only")),
 ("continuity decision",lambda x:x["decision"].__setitem__("smooth_noether_continuity_proved",False)),
 ("propagation decision",lambda x:x["decision"].__setitem__("smooth_gauss_constraint_propagation_proved",False)),
 ("existence overclaim",lambda x:x["decision"].__setitem__("global_graph_solution_exists",True)),
 ("KT overclaim",lambda x:x["decision"].__setitem__("closed_nonlinear_KT_range_proved",True)),
 ("cohomology overclaim",lambda x:x["decision"].__setitem__("positive_GU_physical_cohomology_proved",True))]
for i,(label,mutate) in enumerate(mutations,1):
 x=copy.deepcopy(D);mutate(x);errors=validate(x);assert errors,label;print(f"PASS {i:02d}: rejects {label} via [FAIL] {errors[0]}")
print("RESULT: PASS 10/10")
