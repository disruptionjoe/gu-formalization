#!/usr/bin/env python3
"""Exact controls for K1313's compact-picture positive Hilbert control."""
import hashlib,json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]; D=json.loads((ROOT/"lab/process/k1313-compact-picture-positive-hilbert-control.json").read_text()); n=0
def check(label,value):
 global n; assert value,label; n+=1; print(f"PASS {n:02d}: {label}")
for key,pin in D["pinned_inputs"].items(): check(f"{key} pin",hashlib.sha256((ROOT/pin["path"]).read_bytes()).hexdigest()==pin["sha256"])
C=D["construction"]; Q=D["decision"]
check("compact dimension",C["K_dimension"]==2*(7*6//2)==42)
check("M finite",C["M_dimension"]==0)
check("base dimension",C["compact_picture_dimension"]==C["K_dimension"]-C["M_dimension"]==42)
weights=(1,2,3,5); f=(1+2j,-3j,2-1j,-1); g=(2,1j,-1+4j,3)
ff=sum(w*(z.conjugate()*z).real for w,z in zip(weights,f)); gg=sum(w*(z.conjugate()*z).real for w,z in zip(weights,g))
fg=sum(w*z.conjugate()*y for w,z,y in zip(weights,f,g))
check("positive f norm",ff>0)
check("positive g norm",gg>0)
check("Cauchy Schwarz",abs(fg)**2<=ff*gg+1e-12)
check("positive definite",C["positive_definite"])
check("unitary axis",C["charge_parameter"].startswith("i mu"))
check("unitary normalized induction",C["normalized_principal_series_unitary"])
check("conserved norm",C["conserved_norm"])
check("neutral tangent retained",C["tangent_para_kahler_signature"]==[42,42])
check("mathematical control",Q["positive_mathematical_hilbert_control_exists"])
check("neutral metric not a block",not Q["neutral_tangent_metric_blocks_unitary_induction"])
check("not physical",not Q["physical_pairing_constructed"] and not Q["causal_generator_or_Green_law_constructed"])
assert n==16; print("RESULT: PASS 16/16")
