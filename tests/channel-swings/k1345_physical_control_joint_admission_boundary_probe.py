#!/usr/bin/env python3
"""Hostile mutations for K1345."""
import copy,json
from pathlib import Path
D=json.loads((Path(__file__).resolve().parents[2]/"lab/process/k1345-physical-control-joint-admission-boundary.json").read_text()); tests=[]
def rejects(label,mut,pred):
 x=copy.deepcopy(D); mut(x); assert not pred(x),label; tests.append(label); print(f"PASS {len(tests):02d}: rejects {label}")
rejects("bad census",lambda x:x["joint_control_census"].__setitem__("satisfied_count",16),lambda x:x["joint_control_census"]["satisfied_count"]+x["joint_control_census"]["conditional_count"]+x["joint_control_census"]["missing_count"]==21)
rejects("conditional promoted",lambda x:x["joint_control_census"].__setitem__("conditional_count",0),lambda x:x["joint_control_census"]["conditional_count"]==2)
rejects("missing erased",lambda x:x["joint_control_census"].__setitem__("missing_count",0),lambda x:x["joint_control_census"]["missing_count"]==4)
rejects("gauge conclusion lost",lambda x:x["decision"].__setitem__("carrier_obstruction_to_nontrivial_free_gauge_reduction_excluded_for_this_control",False),lambda x:x["decision"]["carrier_obstruction_to_nontrivial_free_gauge_reduction_excluded_for_this_control"])
rejects("joint action invented",lambda x:x["decision"].__setitem__("separate_controls_compose_to_one_action",True),lambda x:not x["decision"]["separate_controls_compose_to_one_action"])
rejects("GU complex overclaim",lambda x:x["decision"].__setitem__("source_owned_interacting_gu_constraint_complex_constructed",True),lambda x:not x["decision"]["source_owned_interacting_gu_constraint_complex_constructed"])
rejects("GU cohomology overclaim",lambda x:x["decision"].__setitem__("gu_physical_cohomology_constructed",True),lambda x:not x["decision"]["gu_physical_cohomology_constructed"])
rejects("GU export overclaim",lambda x:x["decision"].__setitem__("gu_observed_state_map_constructed",True),lambda x:not x["decision"]["gu_observed_state_map_constructed"])
rejects("protected movement",lambda x:x["decision"].__setitem__("protected_status_change",True),lambda x:not x["decision"]["protected_status_change"])
rejects("ledger movement",lambda x:x.__setitem__("source_and_ledger_effect","LEDGER_MOVED"),lambda x:"LEDGER_UNCHANGED" in x["source_and_ledger_effect"])
assert len(tests)==10; print("RESULT: PASS 10/10")
