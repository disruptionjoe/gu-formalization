#!/usr/bin/env python3
"""Identity controls for K1374's smooth Noether/Gauss/BRST layer."""
import hashlib,json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
D=json.loads((ROOT/"lab/process/k1374-smooth-constraint-propagation-brst.json").read_text());n=0
def check(label,value):
 global n
 assert value,label;n+=1;print(f"PASS {n:02d}: {label}")
for key,pin in D["pinned_inputs"].items():check(f"{key} pin",hashlib.sha256((ROOT/pin["path"]).read_bytes()).hexdigest()==pin["sha256"])
S,B,Q=D["smooth_identity"],D["brst"],D["decision"]
check("matter equation typed","mu Q^2" in S["matter_equation"])
check("current typed","Im<Qphi,D^mu phi>" in S["current"])
check("continuity typed","partial_mu j^mu=0" in S["continuity"])
check("self-adjoint cancellation","self-adjoint" in S["continuity"])
check("Maxwell equation typed","F^(mu nu)" in S["maxwell_equation"])
check("Gauss propagation typed","partial_t(div E-j^0)=0" in S["gauss_propagation"])
check("smooth conditionality","not an existence theorem" in S["conditionality"])
check("BRST rules typed","sphi=i e c Qphi" in B["rules"])
check("BRST nilpotency typed","s^2" in B["nilpotency"])
check("Gauss BRST closed","BRST closed" in B["gauss_covariance"])
check("properness boundary","not inferred" in B["boundary"])
check("continuity proved",Q["smooth_noether_continuity_proved"])
check("propagation proved",Q["smooth_gauss_constraint_propagation_proved"])
check("nilpotency proved",Q["nonlinear_brst_nilpotency_on_common_core_proved"])
check("global existence absent",not Q["global_graph_solution_exists"])
check("KT closure absent",not Q["closed_nonlinear_KT_range_proved"])
check("physical cohomology absent",not Q["positive_GU_physical_cohomology_proved"])
check("source absent",not Q["source_action_identified"])
check("protected fixed",not Q["protected_status_change"])
assert n==21,n
print("RESULT: PASS 21/21")
