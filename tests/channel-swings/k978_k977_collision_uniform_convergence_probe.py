#!/usr/bin/env python3
import copy, importlib.util
from pathlib import Path
H=Path(__file__).resolve().parent;s=importlib.util.spec_from_file_location("k978",H/"k978_k977_collision_uniform_convergence.py");m=importlib.util.module_from_spec(s);s.loader.exec_module(m)
def ok(p):
    try:m.validate(p);return True
    except (AssertionError,KeyError):return False
def main():
    p=m.build();muts=[lambda x:x["theorem"].__setitem__("uniform_on_every_fixed_finite_horizon",False),lambda x:x["theorem"].__setitem__("grid_error_zero",False),lambda x:x["exact_controls"].__setitem__("rows",[]),lambda x:x["exact_controls"].__setitem__("all_bounds_hold",False),lambda x:x["exact_controls"].__setitem__("sampled_errors_decrease",False),lambda x:x["exact_controls"].__setitem__("coupling_rates_increase",False),lambda x:x["exact_controls"].__setitem__("white_noise_scales_tend_to_gamma",False),lambda x:x["ownership"].__setitem__("clock_reset_and_freshness_imported",False),lambda x:x["ownership"].__setitem__("continuous_time_action_constructed",True),lambda x:x["ownership"].__setitem__("gu_reservoir_or_domain_constructed",True),lambda x:x["ownership"].__setitem__("prediction_or_confirmation_credit",True),lambda x:x["decision"].__setitem__("off_grid_convergence_quantified",False),lambda x:x["decision"].__setitem__("grid_equality_not_microscopic_owner",False),lambda x:x.__setitem__("source_and_ledger_effect","changed")];caught=0
    for f in muts:q=copy.deepcopy(p);f(q);caught+=not ok(q)
    print(f"K978 hostile: {caught}/{len(muts)}");return 0 if caught==len(muts) else 1
if __name__=="__main__":raise SystemExit(main())
