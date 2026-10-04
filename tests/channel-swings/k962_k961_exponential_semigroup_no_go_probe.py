#!/usr/bin/env python3
import copy, importlib.util
from pathlib import Path
H=Path(__file__).resolve().parent; s=importlib.util.spec_from_file_location("k962",H/"k962_k961_exponential_semigroup_no_go.py"); m=importlib.util.module_from_spec(s); s.loader.exec_module(m)
def ok(p):
    try:m.validate(p);return True
    except (AssertionError,KeyError):return False
def main():
    p=m.build(); muts=[lambda x:x["theorem"].__setitem__("recurrence_from_k961",False),lambda x:x["theorem"].__setitem__("exponential_limit_zero",False),lambda x:x["theorem"].__setitem__("finite_closed_exact_realization_exists",True),lambda x:x["exact_controls"].__setitem__("gamma",0),lambda x:x["exact_controls"].__setitem__("strictly_decreasing",False),lambda x:x["exact_controls"].__setitem__("late_value_below_one_fiftieth",False),lambda x:x["boundary"].__setitem__("not_excluded",[]),lambda x:x["decision"].__setitem__("finite_closed_exact_markov_parent_killed",False),lambda x:x["ownership"].__setitem__("gu_action_or_physical_quotient_constructed",True),lambda x:x["ownership"].__setitem__("prediction_or_confirmation_credit",True)]; caught=0
    for f in muts:q=copy.deepcopy(p);f(q);caught+=not ok(q)
    print(f"K962 hostile: {caught}/{len(muts)}");return 0 if caught==len(muts) else 1
if __name__=="__main__":raise SystemExit(main())
