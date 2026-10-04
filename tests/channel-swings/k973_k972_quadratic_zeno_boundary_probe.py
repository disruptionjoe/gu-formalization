#!/usr/bin/env python3
import copy,importlib.util
from pathlib import Path
H=Path(__file__).resolve().parent;s=importlib.util.spec_from_file_location("k973",H/"k973_k972_quadratic_zeno_boundary.py");m=importlib.util.module_from_spec(s);s.loader.exec_module(m)
def ok(p):
    try:m.validate(p);return True
    except (AssertionError,KeyError):return False
def main():
    p=m.build();muts=[lambda x:x["exact_controls"].__setitem__("a",0),lambda x:x["exact_controls"].__setitem__("symmetric_two_atom_variance",0),lambda x:x["theorem"].__setitem__("finite_variance_exact_exponential_impossible",False),lambda x:x["exact_controls"].__setitem__("quadratic_ratio_tends_to_variance",False),lambda x:x["exact_controls"].__setitem__("linear_ratio_tends_to_2a",False),lambda x:x["decision"].__setitem__("quadratic_vs_linear_boundary_proved",False),lambda x:x["ownership"].__setitem__("general_nonunitary_dynamics_excluded",True),lambda x:x["ownership"].__setitem__("gu_action_or_physical_quotient_constructed",True),lambda x:x["ownership"].__setitem__("prediction_or_confirmation_credit",True)];caught=0
    for f in muts:q=copy.deepcopy(p);f(q);caught+=not ok(q)
    print(f"K973 hostile: {caught}/{len(muts)}");return 0 if caught==len(muts) else 1
if __name__=="__main__":raise SystemExit(main())
