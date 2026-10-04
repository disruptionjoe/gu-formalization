#!/usr/bin/env python3
import copy,importlib.util
from pathlib import Path
H=Path(__file__).resolve().parent;s=importlib.util.spec_from_file_location("k989",H/"k989_k988_record_law_discriminator.py");m=importlib.util.module_from_spec(s);s.loader.exec_module(m)
def ok(p):
    try:m.validate(p);return True
    except (AssertionError,KeyError):return False
def main():
    p=m.build();muts=[lambda x:x["dependency_checks"].__setitem__("system_only_controlled_processes_equal",False),lambda x:x["record_laws"].__setitem__("brownian_paths_continuous_probability",0.0),lambda x:x["record_laws"].__setitem__("compound_paths_continuous_probability",0.0),lambda x:x["record_laws"].__setitem__("record_laws_equal",True),lambda x:x["preregistration"].__setitem__("status","scored"),lambda x:x["preregistration"].__setitem__("no_holdout_refit",False),lambda x:x["preregistration"].__setitem__("requires_action_owned_record_observable",False),lambda x:x["preregistration"].__setitem__("empirical_score_assigned",True),lambda x:x["exact_controls"].__setitem__("rate_equals_two_gamma",False),lambda x:x["exact_controls"].__setitem__("p_no_jump_in_unit_interval",False),lambda x:x["exact_controls"].__setitem__("terminal_law_type_differs",False),lambda x:x["ownership"].__setitem__("record_access_and_resolution_imported",False),lambda x:x["ownership"].__setitem__("gu_record_observable_constructed",True),lambda x:x["ownership"].__setitem__("prediction_or_confirmation_credit",True),lambda x:x["decision"].__setitem__("reduced_controlled_process_not_enough_to_select_levy_horn",False),lambda x:x["decision"].__setitem__("record_crosses_operational_equivalence_class",False),lambda x:x.__setitem__("source_and_ledger_effect","changed")];caught=0
    for f in muts:q=copy.deepcopy(p);f(q);caught+=not ok(q)
    print(f"K989 hostile: {caught}/{len(muts)}");return 0 if caught==len(muts) else 1
if __name__=="__main__":raise SystemExit(main())
