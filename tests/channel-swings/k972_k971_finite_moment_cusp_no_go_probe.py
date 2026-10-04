#!/usr/bin/env python3
import copy,importlib.util
from pathlib import Path
H=Path(__file__).resolve().parent;s=importlib.util.spec_from_file_location("k972",H/"k972_k971_finite_moment_cusp_no_go.py");m=importlib.util.module_from_spec(s);s.loader.exec_module(m)
def ok(p):
    try:m.validate(p);return True
    except (AssertionError,KeyError):return False
def main():
    p=m.build();muts=[lambda x:x["exact_controls"].__setitem__("a",0),lambda x:x["theorem"].__setitem__("characteristic_differentiable_at_zero",False),lambda x:x["theorem"].__setitem__("target_right_derivative",x["theorem"]["target_left_derivative"]),lambda x:x["theorem"].__setitem__("exact_positive_rate_target_impossible",False),lambda x:x["exact_controls"].__setitem__("difference_quotients_converge_to_i_mean",False),lambda x:x["exact_controls"].__setitem__("target_one_sided_derivatives_disagree",False),lambda x:x["decision"].__setitem__("finite_first_moment_excludes_exact_cusp",False),lambda x:x["ownership"].__setitem__("positive_spectral_model_only",False),lambda x:x["ownership"].__setitem__("general_open_system_no_go",True),lambda x:x["ownership"].__setitem__("gu_action_or_physical_quotient_constructed",True),lambda x:x["ownership"].__setitem__("prediction_or_confirmation_credit",True)];caught=0
    for f in muts:q=copy.deepcopy(p);f(q);caught+=not ok(q)
    print(f"K972 hostile: {caught}/{len(muts)}");return 0 if caught==len(muts) else 1
if __name__=="__main__":raise SystemExit(main())
