#!/usr/bin/env python3
import copy,importlib.util
from pathlib import Path
H=Path(__file__).resolve().parent;s=importlib.util.spec_from_file_location("k983",H/"k983_k982_system_only_nonidentifiability.py");m=importlib.util.module_from_spec(s);s.loader.exec_module(m)
def ok(p):
    try:m.validate(p);return True
    except (AssertionError,KeyError):return False
def main():
    p=m.build();muts=[lambda x:x["dependency"].__setitem__("input_ids",[]),lambda x:x["dependency"].__setitem__("same_reduced_semigroup",False),lambda x:x["dependency"].__setitem__("source_and_ledger_effect_none",False),lambda x:x["theorem"].__setitem__("diamond_distance_between_reduced_channels",1),lambda x:x["theorem"].__setitem__("endpoint_system_only_selector_exists",True),lambda x:x["theorem"].__setitem__("environment_or_record_sensitive_observable_required",False),lambda x:x["theorem"].__setitem__("multi_time_process_claimed",True),lambda x:x["exact_controls"].__setitem__("rows",[]),lambda x:x["exact_controls"].__setitem__("all_endpoint_differences_zero",False),lambda x:x["exact_controls"].__setitem__("three_witness_classes_replayed",False),lambda x:x["exact_controls"].__setitem__("ancilla_assisted_scope_included",False),lambda x:x["decision"].__setitem__("system_only_endpoint_holdout_cannot_select_horn",False),lambda x:x["decision"].__setitem__("k980_holdout_must_cross_reduced_channel_equivalence_class",False),lambda x:x["ownership"].__setitem__("environment_record_constructed",True),lambda x:x["ownership"].__setitem__("gu_observable_or_action_constructed",True),lambda x:x["ownership"].__setitem__("prediction_or_confirmation_credit",True),lambda x:x.__setitem__("source_and_ledger_effect","changed")];caught=0
    for f in muts:q=copy.deepcopy(p);f(q);caught+=not ok(q)
    print(f"K983 hostile: {caught}/{len(muts)}");return 0 if caught==len(muts) else 1
if __name__=="__main__":raise SystemExit(main())
