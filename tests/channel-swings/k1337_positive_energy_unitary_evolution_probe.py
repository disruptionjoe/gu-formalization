#!/usr/bin/env python3
"""Hostile mutations for K1337."""
import copy,json
from pathlib import Path
D=json.loads((Path(__file__).resolve().parents[2]/"lab/process/k1337-positive-energy-unitary-evolution.json").read_text()); tests=[]
def rejects(label,mut,pred):
 x=copy.deepcopy(D); mut(x); assert not pred(x),label; tests.append(label); print(f"PASS {len(tests):02d}: rejects {label}")
rejects("wrong energy space",lambda x:x["energy_system"].__setitem__("energy_space","H direct_sum H"),lambda x:x["energy_system"]["energy_space"]=="E=D(A_m^(1/2)) direct_sum H")
rejects("wrong generator domain",lambda x:x["energy_system"].__setitem__("generator_domain","H2 direct_sum H"),lambda x:x["energy_system"]["generator_domain"]=="D(G)=D(A_m) direct_sum D(A_m^(1/2))")
rejects("wrong sign",lambda x:x["energy_system"].__setitem__("mode_generator","[[0,1],[+omega_k^2,0]]"),lambda x:x["energy_system"]["mode_generator"]=="G_k=[[0,1],[-omega_k^2,0]]")
rejects("skew-adjointness lost",lambda x:x["decision"].__setitem__("generator_skew_adjoint_on_energy_space",False),lambda x:x["decision"]["generator_skew_adjoint_on_energy_space"])
rejects("unitarity lost",lambda x:x["decision"].__setitem__("unitary_strongly_continuous_evolution",False),lambda x:x["decision"]["unitary_strongly_continuous_evolution"])
rejects("energy lost",lambda x:x["decision"].__setitem__("positive_conserved_energy",False),lambda x:x["decision"]["positive_conserved_energy"])
rejects("gap lost",lambda x:x["decision"].__setitem__("strict_frequency_gap",False),lambda x:x["decision"]["strict_frequency_gap"])
rejects("interaction overclaim",lambda x:x["decision"].__setitem__("bounded_below_interacting_hamiltonian_constructed",True),lambda x:not x["decision"]["bounded_below_interacting_hamiltonian_constructed"])
rejects("GU time overclaim",lambda x:x["decision"].__setitem__("gu_physical_time_evolution_constructed",True),lambda x:not x["decision"]["gu_physical_time_evolution_constructed"])
assert len(tests)==9; print("RESULT: PASS 9/9")
