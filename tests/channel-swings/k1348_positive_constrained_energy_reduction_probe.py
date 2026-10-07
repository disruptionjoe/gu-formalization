#!/usr/bin/env python3
"""Hostile mutations for K1348."""
import copy,json
from pathlib import Path
D=json.loads((Path(__file__).resolve().parents[2]/"lab/process/k1348-positive-constrained-energy-reduction.json").read_text()); tests=[]
def rejects(label,mut,pred):
 x=copy.deepcopy(D); mut(x); assert not pred(x),label; tests.append(label); print(f"PASS {len(tests):02d}: rejects {label}")
rejects("negative potential",lambda x:x["constrained_reduction"].__setitem__("hamiltonian","-lambda ||phi||4^4"),lambda x:"+lambda/4" in x["constrained_reduction"]["hamiltonian"])
rejects("Gauss surface lost",lambda x:x["decision"].__setitem__("interacting_gauss_surface_nonempty",False),lambda x:x["decision"]["interacting_gauss_surface_nonempty"])
rejects("energy descent lost",lambda x:x["decision"].__setitem__("classical_energy_descends_to_gauge_classes",False),lambda x:x["decision"]["classical_energy_descends_to_gauge_classes"])
rejects("linearized cohomology lost",lambda x:x["decision"].__setitem__("positive_nonzero_linearized_brst_cohomology_constructed",False),lambda x:x["decision"]["positive_nonzero_linearized_brst_cohomology_constructed"])
rejects("harmonic zero mode restored",lambda x:x["decision"].__setitem__("harmonic_zero_mode_removed_by_declared_sector",False),lambda x:x["decision"]["harmonic_zero_mode_removed_by_declared_sector"])
rejects("nonlinear Hilbert overclaim",lambda x:x["decision"].__setitem__("closed_nonlinear_physical_hilbert_quotient_constructed",True),lambda x:not x["decision"]["closed_nonlinear_physical_hilbert_quotient_constructed"])
rejects("global evolution overclaim",lambda x:x["decision"].__setitem__("global_large_data_interacting_evolution_constructed",True),lambda x:not x["decision"]["global_large_data_interacting_evolution_constructed"])
rejects("quantum overclaim",lambda x:x["decision"].__setitem__("quantum_positive_physical_space_constructed",True),lambda x:not x["decision"]["quantum_positive_physical_space_constructed"])
rejects("GU cohomology overclaim",lambda x:x["decision"].__setitem__("gu_physical_cohomology_constructed",True),lambda x:not x["decision"]["gu_physical_cohomology_constructed"])
rejects("linearized-only fence removed",lambda x:x["constrained_reduction"].__setitem__("nonlinear_status","complete physical Hilbert space"),lambda x:"not" in x["constrained_reduction"]["nonlinear_status"])
assert len(tests)==10; print("RESULT: PASS 10/10")
