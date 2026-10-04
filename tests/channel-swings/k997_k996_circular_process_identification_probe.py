#!/usr/bin/env python3
import copy,importlib.util
from pathlib import Path
H=Path(__file__).resolve().parent;s=importlib.util.spec_from_file_location("k997",H/"k997_k996_circular_process_identification.py");m=importlib.util.module_from_spec(s);s.loader.exec_module(m)
def ok(p):
 try:m.validate(p);return True
 except (AssertionError,KeyError):return False
def main():
 p=m.build();muts=[lambda x:x["theorem"].__setitem__("all_time_integer_harmonics_determine_each_increment_law",False),lambda x:x["theorem"].__setitem__("independent_increment_process_finite_dimensional_law_determined",False),lambda x:x["theorem"].__setitem__("single_time_marginal_does_not_determine_generator",False),lambda x:x["theorem"].__setitem__("real_line_lift_identified",True),lambda x:x["exact_controls"].__setitem__("semigroup_identity_pass",False),lambda x:x["exact_controls"].__setitem__("brownian_circle_semigroup_error",1.0),lambda x:x["exact_controls"].__setitem__("terminal_alias_pass",False),lambda x:x["exact_controls"].__setitem__("terminal_integer_harmonic_error",1.0),lambda x:x["exact_controls"].__setitem__("intermediate_laws_differ",False),lambda x:x["ownership"].__setitem__("circular_process_imported",False),lambda x:x["ownership"].__setitem__("all_time_harmonic_access_imported",False),lambda x:x["ownership"].__setitem__("gu_action_generator_or_clock_constructed",True),lambda x:x["ownership"].__setitem__("prediction_or_confirmation_credit",True),lambda x:x["decision"].__setitem__("fixed_time_log_branch_warning_required",False),lambda x:x.__setitem__("source_and_ledger_effect","changed")]
 c=0
 for f in muts:q=copy.deepcopy(p);f(q);c+=not ok(q)
 print(f"K997 hostile: {c}/{len(muts)}");return 0 if c==len(muts) else 1
if __name__=="__main__":raise SystemExit(main())
