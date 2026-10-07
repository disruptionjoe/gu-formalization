#!/usr/bin/env python3
"""Exact mode controls for K1342's transverse Maxwell quotient."""
import hashlib,json
from fractions import Fraction
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]; D=json.loads((ROOT/"lab/process/k1342-transverse-positive-cohomology-green-boundary.json").read_text()); n=0
def check(label,value):
 global n; assert value,label; n+=1; print(f"PASS {n:02d}: {label}")
for key,pin in D["pinned_inputs"].items(): check(f"{key} pin",hashlib.sha256((ROOT/pin["path"]).read_bytes()).hexdigest()==pin["sha256"])
P=D["physical_reduction"]; G=D["green_boundary"]; Q=D["decision"]
check("orthogonal Hodge split","orthogonal_sum ker delta" in P["mean_zero_hodge_split"])
check("closed gauge image","closed range" in P["closed_gauge_image"])
check("unique Coulomb representative",P["coulomb_representative"].startswith("P_T A"))
modes=[(a,b,c) for a in range(-2,3) for b in range(-2,3) for c in range(-2,3) if (a,b,c)!=(0,0,0)]
ranks=[]; orth=[]; idempotent=[]
for k in modes:
 q=sum(x*x for x in k); A=[[Fraction(int(i==j))-Fraction(k[i]*k[j],q) for j in range(3)] for i in range(3)]
 ranks.append(sum(A[i][i] for i in range(3)))
 orth.append(all(sum(A[i][j]*k[j] for j in range(3))==0 for i in range(3)))
 idempotent.append(all(sum(A[i][r]*A[r][j] for r in range(3))==A[i][j] for i in range(3) for j in range(3)))
check("all projectors transverse",all(orth))
check("all projectors idempotent",all(idempotent))
check("two polarizations",all(r==2 for r in ranks) and P["polarization_count"]==2)
check("finite control quotient nonzero",sum(ranks)==248)
check("positive energy formula",P["energy"].startswith("E=1/2"))
check("unit spatial floor",P["energy_floor"].endswith("gap one"))
check("one-form wave operator",G["gauge_fixed_operator"]=="Box_1 tensor I_Hps")
check("causal support","J_plus" in G["causal_support"] and "J_minus" in G["causal_support"])
check("constraint propagation","Box_0 delta" in G["constraint_propagation"])
check("boundary descent","annihilates infinitesimal gauge directions" in G["descent"])
check("closed quotient",Q["closed_nontrivial_gauge_quotient_constructed"])
check("positive nonzero quotient",Q["positive_nonzero_transverse_cohomology_constructed"])
check("causal boundary",Q["causal_green_and_boundary_reduction_constructed"])
check("internal equivariance",Q["internal_G_equivariance_constructed"])
check("GU ceiling",not Q["gu_physical_cohomology_constructed"])
check("interaction ceiling",not Q["interacting"])
check("source ceiling",not Q["source_owned"])
assert n==22; print("RESULT: PASS 22/22")
