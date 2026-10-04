#!/usr/bin/env python3
import copy,importlib.util
from pathlib import Path
H=Path(__file__).resolve().parent;s=importlib.util.spec_from_file_location("k968",H/"k968_k967_finite_window_atomic_approximation.py");m=importlib.util.module_from_spec(s);s.loader.exec_module(m)
def ok(p):
    try:m.validate(p);return True
    except (AssertionError,KeyError):return False
def main():
    p=m.build();muts=[lambda x:x["construction"].__setitem__("gamma",0),lambda x:x["construction"].__setitem__("T",0),lambda x:x["construction"].__setitem__("epsilon",2),lambda x:x["construction"].__setitem__("atom_count",0),lambda x:x["construction"].__setitem__("weights_positive",False),lambda x:x["construction"].__setitem__("weights_sum",0),lambda x:x["construction"].__setitem__("finite_autonomous_reservoir",False),lambda x:x["theorem"].__setitem__("bound_below_epsilon",False),lambda x:x["exact_controls"].__setitem__("sample_errors_below_bound",False),lambda x:x["exact_controls"].__setitem__("imaginary_parts_cancel",False),lambda x:x["decision"].__setitem__("finite_window_indistinguishability_constructed",False),lambda x:x["ownership"].__setitem__("gu_action_or_physical_quotient_constructed",True),lambda x:x["ownership"].__setitem__("prediction_or_confirmation_credit",True)];caught=0
    for f in muts:q=copy.deepcopy(p);f(q);caught+=not ok(q)
    print(f"K968 hostile: {caught}/{len(muts)}");return 0 if caught==len(muts) else 1
if __name__=="__main__":raise SystemExit(main())
