#!/usr/bin/env python3
import copy,importlib.util
from pathlib import Path
H=Path(__file__).resolve().parent;s=importlib.util.spec_from_file_location("k971",H/"k971_k970_cauchy_energy_domain_boundary.py");m=importlib.util.module_from_spec(s);s.loader.exec_module(m)
def ok(p):
    try:m.validate(p);return True
    except (AssertionError,KeyError):return False
def main():
    p=m.build();muts=[lambda x:x["construction"].__setitem__("scale",0),lambda x:x["theorem"].__setitem__("absolute_first_moment_diverges",False),lambda x:x["theorem"].__setitem__("second_moment_diverges",False),lambda x:x["theorem"].__setitem__("initial_vector_in_generator_domain",True),lambda x:x["theorem"].__setitem__("initial_vector_in_absolute_form_domain",True),lambda x:x["theorem"].__setitem__("unitary_orbit_still_defined",False),lambda x:x["exact_controls"].__setitem__("absolute_first_strictly_increases",False),lambda x:x["exact_controls"].__setitem__("second_strictly_increases",False),lambda x:x["decision"].__setitem__("k966_finite_energy_seam_closed_negatively",False),lambda x:x["ownership"].__setitem__("finite_energy_physical_state_constructed",True),lambda x:x["ownership"].__setitem__("gu_action_or_physical_quotient_constructed",True),lambda x:x["ownership"].__setitem__("prediction_or_confirmation_credit",True)];caught=0
    for f in muts:q=copy.deepcopy(p);f(q);caught+=not ok(q)
    print(f"K971 hostile: {caught}/{len(muts)}");return 0 if caught==len(muts) else 1
if __name__=="__main__":raise SystemExit(main())
