#!/usr/bin/env python3
import copy,importlib.util
from pathlib import Path
H=Path(__file__).resolve().parent;s=importlib.util.spec_from_file_location("k988",H/"k988_k987_controlled_process_nonidentifiability.py");m=importlib.util.module_from_spec(s);s.loader.exec_module(m)
def ok(p):
    try:m.validate(p);return True
    except (AssertionError,KeyError):return False
def main():
    p=m.build();muts=[lambda x:x["dependency_checks"].__setitem__("input_ids",[]),lambda x:x["dependency_checks"].__setitem__("both_same_semigroup",False),lambda x:x["dependency_checks"].__setitem__("both_independent_increment",False),lambda x:x["theorem"].__setitem__("arbitrary_finite_system_only_instruments",False),lambda x:x["theorem"].__setitem__("inert_ancillas_included",False),lambda x:x["theorem"].__setitem__("system_outcome_feedback_included_by_branchwise_induction",False),lambda x:x["theorem"].__setitem__("brownian_and_compound_poisson_process_tensors_equal_on_declared_access_class",False),lambda x:x["theorem"].__setitem__("arbitrary_microscopic_process_equality_claimed",True),lambda x:x["exact_controls"].__setitem__("noncommuting_replay_pass",False),lambda x:x["exact_controls"].__setitem__("interval_semigroup_pass",False),lambda x:x["boundary"].__setitem__("record_conditioned_feedback_excluded",False),lambda x:x["boundary"].__setitem__("correlated_increment_or_memory_horns_excluded",False),lambda x:x["boundary"].__setitem__("environment_access_excluded",False),lambda x:x["boundary"].__setitem__("action_specific_observables_may_distinguish",False),lambda x:x["ownership"].__setitem__("gu_action_or_process_owner_constructed",True),lambda x:x["ownership"].__setitem__("prediction_or_confirmation_credit",True),lambda x:x["decision"].__setitem__("k983_one_time_boundary_strengthened_for_markov_independent_increment_class",False),lambda x:x.__setitem__("source_and_ledger_effect","changed")];caught=0
    for f in muts:q=copy.deepcopy(p);f(q);caught+=not ok(q)
    print(f"K988 hostile: {caught}/{len(muts)}");return 0 if caught==len(muts) else 1
if __name__=="__main__":raise SystemExit(main())
