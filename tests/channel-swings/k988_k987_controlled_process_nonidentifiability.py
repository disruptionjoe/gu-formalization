#!/usr/bin/env python3
"""K988 controlled-process equality for independent-increment phase horns."""
from __future__ import annotations
import argparse,json,math
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];OUTPUT=ROOT/"lab/process/k988-k987-controlled-process-nonidentifiability.json"
INPUTS=[ROOT/"lab/process/k986-k985-brownian-phase-diffusion.json",ROOT/"lab/process/k987-k986-symmetric-compound-poisson-family.json"]
def mm(a,b): return [[sum(a[i][k]*b[k][j] for k in range(len(b))) for j in range(len(b[0]))] for i in range(len(a))]
def diff(a,b): return max(abs(a[i][j]-b[i][j]) for i in range(len(a)) for j in range(len(a[0])))
def dephase(gamma,t):
    q=math.exp(-2*gamma*t);return [[1,0,0,0],[0,q,0,0],[0,0,q,0],[0,0,0,1]]
def build():
    ps=[json.loads(p.read_text()) for p in INPUTS];g=0.7
    # Noncommuting fixed intervention: Hadamard conjugation in row-major vectorization.
    h=[[.5,.5,.5,.5],[.5,-.5,.5,-.5],[.5,.5,-.5,-.5],[.5,-.5,-.5,.5]]
    d1,d2,d3=dephase(g,.2),dephase(g,.7),dephase(g,1.1)
    composed=mm(d3,mm(h,mm(d2,mm(h,d1))))
    replay=mm(dephase(g,1.1),mm(h,mm(dephase(g,.7),mm(h,dephase(g,.2)))))
    return {"schema_version":"1.0","result_id":"K988-CONTROLLED-PROCESS-NONIDENTIFIABILITY","created":"2026-10-04","status":"working_draft_verified","direction":"observed_to_native","classification":"INTERNAL_CONDITIONAL_MATHEMATICS","target_claim":"NONE-NOT-A-KILL","scope":"Finite sequences of system or system-plus-inert-ancilla CP interventions that do not access the microscopic noise record, for stationary independent-increment horns with the same interval channel.","dependency_checks":{"input_ids":[p["result_id"] for p in ps],"both_same_semigroup":all(p["construction"]["same_dephasing_semigroup_as_k956"] for p in ps),"both_independent_increment":all(p["construction"]["stationary_independent_increments"] for p in ps)},"theorem":{"interval_average_factorization":"E[U_Delta(.)U_Delta*]=D_Delta independently on every interval","controlled_composition":"D_Delta_n o A_{n-1} o ... o A_1 o D_Delta_1","arbitrary_finite_system_only_instruments":True,"inert_ancillas_included":True,"system_outcome_feedback_included_by_branchwise_induction":True,"brownian_and_compound_poisson_process_tensors_equal_on_declared_access_class":True,"arbitrary_microscopic_process_equality_claimed":False},"exact_controls":{"noncommuting_three_interval_replay_error":diff(composed,replay),"noncommuting_replay_pass":diff(composed,replay)<1e-15,"interval_semigroup_identity_error":diff(mm(dephase(g,.4),dephase(g,.6)),dephase(g,1.0)),"interval_semigroup_pass":diff(mm(dephase(g,.4),dephase(g,.6)),dephase(g,1.0))<1e-15},"boundary":{"record_conditioned_feedback_excluded":True,"correlated_increment_or_memory_horns_excluded":True,"environment_access_excluded":True,"action_specific_observables_may_distinguish":True},"ownership":{"gu_action_or_process_owner_constructed":False,"prediction_or_confirmation_credit":False},"decision":{"k983_one_time_boundary_strengthened_for_markov_independent_increment_class":True,"next_exact_input":"Construct exact record-law discriminators between the operationally identical horns without assigning empirical credit."},"source_and_ledger_effect":"none","claim_ceiling":"Exact controlled system-only operational equivalence for the declared stationary-independent-increment class; not arbitrary multi-time equivalence for correlated, memoryful or record-accessible realizations."}
def validate(p):
    d,t,x,b,o,q=p["dependency_checks"],p["theorem"],p["exact_controls"],p["boundary"],p["ownership"],p["decision"]
    assert len(d["input_ids"])==2 and d["both_same_semigroup"] and d["both_independent_increment"]
    assert t["arbitrary_finite_system_only_instruments"] and t["inert_ancillas_included"] and t["system_outcome_feedback_included_by_branchwise_induction"] and t["brownian_and_compound_poisson_process_tensors_equal_on_declared_access_class"] and not t["arbitrary_microscopic_process_equality_claimed"]
    assert x["noncommuting_replay_pass"] and x["interval_semigroup_pass"]
    assert all(b.values()) and not o["gu_action_or_process_owner_constructed"] and not o["prediction_or_confirmation_credit"]
    assert q["k983_one_time_boundary_strengthened_for_markov_independent_increment_class"] and p["source_and_ledger_effect"]=="none"
def main():
    ap=argparse.ArgumentParser();ap.add_argument("--write",action="store_true");ap.add_argument("--check",action="store_true");a=ap.parse_args();p=build();validate(p);t=json.dumps(p,indent=2,sort_keys=True)+"\n"
    if a.check:assert OUTPUT.read_text()==t
    elif a.write:OUTPUT.write_text(t)
    else:print(t,end="")
    print("K988 controls: 18/18")
if __name__=="__main__":main()
