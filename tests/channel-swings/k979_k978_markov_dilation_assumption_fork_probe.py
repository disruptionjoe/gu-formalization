#!/usr/bin/env python3
import copy, importlib.util
from pathlib import Path
H=Path(__file__).resolve().parent;s=importlib.util.spec_from_file_location("k979",H/"k979_k978_markov_dilation_assumption_fork.py");m=importlib.util.module_from_spec(s);s.loader.exec_module(m)
def ok(p):
    try:m.validate(p);return True
    except (AssertionError,KeyError):return False
def main():
    p=m.build();muts=[lambda x:x["dependency_checks"].__setitem__("input_ids",[]),lambda x:x["dependency_checks"].__setitem__("all_source_and_ledger_effect_none",False),lambda x:x["dependency_checks"].__setitem__("all_prediction_or_confirmation_withheld",False),lambda x:x["dependency_checks"].__setitem__("bounded_parent_obstruction_present",False),lambda x:x["dependency_checks"].__setitem__("purity_boundary_present",False),lambda x:x["dependency_checks"].__setitem__("collision_repair_present",False),lambda x:x["assumption_fork"].__setitem__("jointly_incompatible_parent_assumptions",[]),lambda x:x["assumption_fork"].__setitem__("candidate_failure_modes_not_exhaustive",[]),lambda x:x["assumption_fork"].__setitem__("does_not_select_a_failure_mode",False),lambda x:x["ownership"].__setitem__("logical_fork_only",False),lambda x:x["ownership"].__setitem__("gu_action_selects_no_horn",False),lambda x:x["ownership"].__setitem__("gu_physical_quotient_constructed",True),lambda x:x["ownership"].__setitem__("held_out_scored",True),lambda x:x["ownership"].__setitem__("prediction_or_confirmation_credit",True),lambda x:x["decision"].__setitem__("bounded_autonomous_horn_closed",False),lambda x:x["decision"].__setitem__("fresh_resource_horn_conditionally_open",False),lambda x:x.__setitem__("source_and_ledger_effect","changed")];caught=0
    for f in muts:q=copy.deepcopy(p);f(q);caught+=not ok(q)
    print(f"K979 hostile: {caught}/{len(muts)}");return 0 if caught==len(muts) else 1
if __name__=="__main__":raise SystemExit(main())
