#!/usr/bin/env python3
import copy,importlib.util
from pathlib import Path
H=Path(__file__).resolve().parent;s=importlib.util.spec_from_file_location("k984",H/"k984_k983_record_sensitive_holdout.py");m=importlib.util.module_from_spec(s);s.loader.exec_module(m)
def ok(p):
    try:m.validate(p);return True
    except (AssertionError,KeyError):return False
def main():
    p=m.build();muts=[lambda x:x["dependency"].__setitem__("input_ids",[]),lambda x:x["dependency"].__setitem__("system_endpoint_nonidentifiability_proved",False),lambda x:x["dependency"].__setitem__("source_and_ledger_effect_none",False),lambda x:x["preregistration"].__setitem__("holdout_time_T",3),lambda x:x["preregistration"].__setitem__("fit_on_holdout",True),lambda x:x["preregistration"].__setitem__("primary_checks",[]),lambda x:x["preregistration"].__setitem__("status","scored"),lambda x:x["exact_controls"].__setitem__("probabilities_n_0_through_11",[]),lambda x:x["exact_controls"].__setitem__("probabilities_normalize",False),lambda x:x["exact_controls"].__setitem__("parity_matches_system_coherence",False),lambda x:x["exact_controls"].__setitem__("counts_beyond_parity_have_positive_probability",False),lambda x:x["information_boundary"].__setitem__("system_endpoint_reads_only_parity",False),lambda x:x["information_boundary"].__setitem__("count_record_strictly_refines_parity",False),lambda x:x["information_boundary"].__setitem__("same_endpoint_unitary_for_n_and_n_plus_2",False),lambda x:x["information_boundary"].__setitem__("record_not_supplied_by_reduced_channel",False),lambda x:x["ownership"].__setitem__("gu_record_observable_constructed",True),lambda x:x["ownership"].__setitem__("gu_action_or_clock_constructed",True),lambda x:x["ownership"].__setitem__("empirical_data_collected",True),lambda x:x["ownership"].__setitem__("prediction_or_confirmation_credit",True),lambda x:x["decision"].__setitem__("distinct_holdout_frozen_before_scoring",False),lambda x:x["decision"].__setitem__("holdout_execution_requires_new_native_owner",False),lambda x:x.__setitem__("source_and_ledger_effect","changed")];caught=0
    for f in muts:q=copy.deepcopy(p);f(q);caught+=not ok(q)
    print(f"K984 hostile: {caught}/{len(muts)}");return 0 if caught==len(muts) else 1
if __name__=="__main__":raise SystemExit(main())
