#!/usr/bin/env python3
import copy,importlib.util
from pathlib import Path
H=Path(__file__).resolve().parent;s=importlib.util.spec_from_file_location("k974",H/"k974_k973_finite_energy_approximation_cost.py");m=importlib.util.module_from_spec(s);s.loader.exec_module(m)
def ok(p):
    try:m.validate(p);return True
    except (AssertionError,KeyError):return False
def main():
    p=m.build();muts=[lambda x:x["compact_band_repair"].__setitem__("eta",0.6),lambda x:x["compact_band_repair"].__setitem__("a",0),lambda x:x["theorem"].__setitem__("second_moment_diverges_as_error_vanishes",False),lambda x:x["compact_band_repair"].__setitem__("uniform_error_at_most_eta",False),lambda x:x["compact_band_repair"].__setitem__("mean_zero",False),lambda x:x["compact_band_repair"].__setitem__("repair_respects_lower_bound",False),lambda x:x["exact_controls"].__setitem__("all_repairs_respect_lower_bound",False),lambda x:x["exact_controls"].__setitem__("second_moment_cost_increases",False),lambda x:x["exact_controls"].__setitem__("lower_cost_increases",False),lambda x:x["decision"].__setitem__("finite_energy_repair_quantified",False),lambda x:x["ownership"].__setitem__("optimal_constant_claimed",True),lambda x:x["ownership"].__setitem__("gu_action_or_physical_quotient_constructed",True),lambda x:x["ownership"].__setitem__("prediction_or_confirmation_credit",True)];caught=0
    for f in muts:q=copy.deepcopy(p);f(q);caught+=not ok(q)
    print(f"K974 hostile: {caught}/{len(muts)}");return 0 if caught==len(muts) else 1
if __name__=="__main__":raise SystemExit(main())
