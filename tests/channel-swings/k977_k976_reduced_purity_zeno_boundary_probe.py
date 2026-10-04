#!/usr/bin/env python3
import copy, importlib.util
from pathlib import Path
H=Path(__file__).resolve().parent;s=importlib.util.spec_from_file_location("k977",H/"k977_k976_reduced_purity_zeno_boundary.py");m=importlib.util.module_from_spec(s);s.loader.exec_module(m)
def ok(p):
    try:m.validate(p);return True
    except (AssertionError,KeyError):return False
def main():
    p=m.build();muts=[lambda x:x["theorem"].__setitem__("positive_rate_orders_incompatible",False),lambda x:x["exact_controls"].__setitem__("semigroup_linear_ratio_tends_to_two_gamma",False),lambda x:x["exact_controls"].__setitem__("bounded_example_linear_ratio_tends_to_zero",False),lambda x:x["exact_controls"].__setitem__("bounded_example_quadratic_ratio_tends_to_two",False),lambda x:x["exact_controls"].__setitem__("semigroup_rows",[]),lambda x:x["ownership"].__setitem__("purity_and_born_trace_imported",False),lambda x:x["ownership"].__setitem__("general_unbounded_dilation_excluded",True),lambda x:x["ownership"].__setitem__("gu_positive_state_effect_pairing_constructed",True),lambda x:x["ownership"].__setitem__("prediction_or_confirmation_credit",True),lambda x:x["decision"].__setitem__("observable_short_time_boundary_proved",False),lambda x:x.__setitem__("source_and_ledger_effect","changed")];caught=0
    for f in muts:q=copy.deepcopy(p);f(q);caught+=not ok(q)
    print(f"K977 hostile: {caught}/{len(muts)}");return 0 if caught==len(muts) else 1
if __name__=="__main__":raise SystemExit(main())
