#!/usr/bin/env python3
"""Hostile mutations for K1339."""
import copy,json
from pathlib import Path
D=json.loads((Path(__file__).resolve().parents[2]/"lab/process/k1339-principal-series-internal-equivariance.json").read_text()); tests=[]
def rejects(label,mut,pred):
 x=copy.deepcopy(D); mut(x); assert not pred(x),label; tests.append(label); print(f"PASS {len(tests):02d}: rejects {label}")
rejects("wrong tensor operator",lambda x:x["tensor_symmetry"].__setitem__("field_operator","P_spacetime tensor A_internal"),lambda x:x["tensor_symmetry"]["field_operator"]=="P=P_spacetime tensor I_Hps")
rejects("commutator removed",lambda x:x["tensor_symmetry"].__setitem__("commutator","open"),lambda x:x["tensor_symmetry"]["commutator"]=="[P,U(g)]=0")
rejects("Weyl transport removed",lambda x:x["tensor_symmetry"].__setitem__("weyl_transport","none"),lambda x:x["tensor_symmetry"]["weyl_transport"].startswith("I_spacetime tensor R_w"))
rejects("internal equivariance lost",lambda x:x["decision"].__setitem__("internal_G_equivariance_constructed",False),lambda x:x["decision"]["internal_G_equivariance_constructed"])
rejects("evolution equivariance lost",lambda x:x["decision"].__setitem__("evolution_equivariance_constructed",False),lambda x:x["decision"]["evolution_equivariance_constructed"])
rejects("Green equivariance lost",lambda x:x["decision"].__setitem__("green_equivariance_constructed",False),lambda x:x["decision"]["green_equivariance_constructed"])
rejects("chamber blindness lost",lambda x:x["decision"].__setitem__("chamber_blind_free_dynamics_constructed",False),lambda x:x["decision"]["chamber_blind_free_dynamics_constructed"])
rejects("charge overclaim",lambda x:x["decision"].__setitem__("charge_selected",True),lambda x:not x["decision"]["charge_selected"])
rejects("observation overclaim",lambda x:x["decision"].__setitem__("physical_observation_map_constructed",True),lambda x:not x["decision"]["physical_observation_map_constructed"])
assert len(tests)==9; print("RESULT: PASS 9/9")
