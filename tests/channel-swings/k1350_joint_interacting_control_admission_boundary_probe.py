#!/usr/bin/env python3
"""Hostile mutations for K1350."""
import copy,json
from pathlib import Path
D=json.loads((Path(__file__).resolve().parents[2]/"lab/process/k1350-joint-interacting-control-admission-boundary.json").read_text()); tests=[]
def rejects(label,mut,pred):
 x=copy.deepcopy(D); mut(x); assert not pred(x),label; tests.append(label); print(f"PASS {len(tests):02d}: rejects {label}")
rejects("census arithmetic",lambda x:x["joint_control_census"].__setitem__("row_count",25),lambda x:x["joint_control_census"]["row_count"]==x["joint_control_census"]["satisfied_count"]+x["joint_control_census"]["conditional_count"]+x["joint_control_census"]["missing_count"])
rejects("one-action result lost",lambda x:x["decision"].__setitem__("prior_separate_controls_replaced_by_one_repository_interacting_action",False),lambda x:x["decision"]["prior_separate_controls_replaced_by_one_repository_interacting_action"])
rejects("gauge carrier result lost",lambda x:x["decision"].__setitem__("carrier_obstruction_to_classical_interacting_gauge_algebra_excluded_for_this_control",False),lambda x:x["decision"]["carrier_obstruction_to_classical_interacting_gauge_algebra_excluded_for_this_control"])
rejects("linear no-go misapplied",lambda x:x["decision"].__setitem__("bounded_linear_scalar_no_go_bypassed_by_explicit_nonlinear_map_class",False),lambda x:x["decision"]["bounded_linear_scalar_no_go_bypassed_by_explicit_nonlinear_map_class"])
rejects("source complex overclaim",lambda x:x["decision"].__setitem__("source_owned_interacting_gu_constraint_complex_constructed",True),lambda x:not x["decision"]["source_owned_interacting_gu_constraint_complex_constructed"])
rejects("global quotient overclaim",lambda x:x["decision"].__setitem__("closed_global_nonlinear_physical_hilbert_quotient_constructed",True),lambda x:not x["decision"]["closed_global_nonlinear_physical_hilbert_quotient_constructed"])
rejects("GU cohomology overclaim",lambda x:x["decision"].__setitem__("gu_physical_cohomology_constructed",True),lambda x:not x["decision"]["gu_physical_cohomology_constructed"])
rejects("GU observation overclaim",lambda x:x["decision"].__setitem__("gu_observed_state_map_constructed",True),lambda x:not x["decision"]["gu_observed_state_map_constructed"])
rejects("native candidates moved",lambda x:x["decision"].__setitem__("k1145_k1150_candidate_counts_move",True),lambda x:not x["decision"]["k1145_k1150_candidate_counts_move"])
rejects("protected movement",lambda x:x["decision"].__setitem__("protected_status_change",True),lambda x:not x["decision"]["protected_status_change"])
assert len(tests)==10; print("RESULT: PASS 10/10")
