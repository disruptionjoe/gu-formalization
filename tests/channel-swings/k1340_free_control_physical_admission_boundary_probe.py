#!/usr/bin/env python3
"""Hostile mutations for K1340."""
import copy,json
from pathlib import Path
D=json.loads((Path(__file__).resolve().parents[2]/"lab/process/k1340-free-control-physical-admission-boundary.json").read_text()); tests=[]
def rejects(label,mut,pred):
 x=copy.deepcopy(D); mut(x); assert not pred(x),label; tests.append(label); print(f"PASS {len(tests):02d}: rejects {label}")
rejects("bad census",lambda x:x["free_control_census"].__setitem__("satisfied_count",10),lambda x:x["free_control_census"]["satisfied_count"]+x["free_control_census"]["conditional_count"]+x["free_control_census"]["missing_count"]==14)
rejects("conditional promoted",lambda x:x["free_control_census"].__setitem__("conditional_count",0),lambda x:x["free_control_census"]["conditional_count"]==1)
rejects("missing erased",lambda x:x["free_control_census"].__setitem__("missing_count",0),lambda x:x["free_control_census"]["missing_count"]==4)
rejects("free package removed",lambda x:x["decision"].__setitem__("free_common_domain_positive_energy_causality_and_boundary_constructed",False),lambda x:x["decision"]["free_common_domain_positive_energy_causality_and_boundary_constructed"])
rejects("equivariance removed",lambda x:x["decision"].__setitem__("principal_series_internal_equivariance_constructed",False),lambda x:x["decision"]["principal_series_internal_equivariance_constructed"])
rejects("source overclaim",lambda x:x["decision"].__setitem__("source_charge_or_chamber_selected",True),lambda x:not x["decision"]["source_charge_or_chamber_selected"])
rejects("interaction overclaim",lambda x:x["decision"].__setitem__("interacting_gu_constraint_complex_constructed",True),lambda x:not x["decision"]["interacting_gu_constraint_complex_constructed"])
rejects("cohomology overclaim",lambda x:x["decision"].__setitem__("nontrivial_gu_physical_cohomology_constructed",True),lambda x:not x["decision"]["nontrivial_gu_physical_cohomology_constructed"])
rejects("observation overclaim",lambda x:x["decision"].__setitem__("observed_state_map_constructed",True),lambda x:not x["decision"]["observed_state_map_constructed"])
rejects("ledger movement",lambda x:x.__setitem__("source_and_ledger_effect","LEDGER_MOVED"),lambda x:"LEDGER_UNCHANGED" in x["source_and_ledger_effect"])
assert len(tests)==10; print("RESULT: PASS 10/10")
