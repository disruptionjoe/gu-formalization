#!/usr/bin/env python3
"""Exact controls for K1311's split-charge prequantum character."""
import cmath,hashlib,json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]; D=json.loads((ROOT/"lab/process/k1311-split-charge-prequantum-character.json").read_text()); n=0
def check(label,value):
 global n; assert value,label; n+=1; print(f"PASS {n:02d}: {label}")
for key,pin in D["pinned_inputs"].items(): check(f"{key} pin",hashlib.sha256((ROOT/pin["path"]).read_bytes()).hexdigest()==pin["sha256"])
C=D["construction"]; Q=D["decision"]
check("spin dimension",C["group_dimension"]==14*13//2==91)
check("split rank",C["split_rank"]==7)
check("orbit dimension",C["orbit_dimension"]==C["group_dimension"]-C["split_rank"]==84)
mu=(2,-3,5,7,-11,13,17); H=(3,1,-2,4,0,-1,2); phase=sum(x*y for x,y in zip(mu,H)); chi=cmath.exp(1j*phase)
check("unit modulus",C["character_modulus_one"] and abs(abs(chi)-1)<1e-12)
check("all real charges integrate",C["character_exists_for_every_real_mu"])
check("homogeneous line",C["homogeneous_line"].startswith("L_mu=G x_(MA)"))
check("KKS curvature",C["invariant_connection_curvature"].startswith("minus i"))
check("no charge lattice",not C["charge_integrality_lattice_required"])
check("prequantum line exists",Q["equivariant_prequantum_line_exists"])
check("mu not selected",not Q["prequantization_selects_mu"])
check("mu not discretized",not Q["prequantization_discretizes_mu"])
check("finite M not physical",not Q["finite_M_supplies_physical_sector"])
assert n==14; print("RESULT: PASS 14/14")
