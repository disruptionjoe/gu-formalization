#!/usr/bin/env python3
import copy,importlib.util
from pathlib import Path
H=Path(__file__).resolve().parent;s=importlib.util.spec_from_file_location("k987",H/"k987_k986_symmetric_compound_poisson_family.py");m=importlib.util.module_from_spec(s);s.loader.exec_module(m)
def ok(p):
    try:m.validate(p);return True
    except (AssertionError,KeyError):return False
def main():
    p=m.build();muts=[lambda x:x["construction"].__setitem__("same_dephasing_semigroup_as_k956",False),lambda x:x["construction"].__setitem__("stationary_independent_increments",False),lambda x:x["construction"].__setitem__("continuum_of_exact_horns",False),lambda x:x["construction"].__setitem__("k981_recovered_at_theta_pi_over_2_up_to_global_phase",False),lambda x:x["exact_controls"].__setitem__("rows",[]),lambda x:x["exact_controls"].__setitem__("all_rate_angle_identities_replayed",False),lambda x:x["exact_controls"].__setitem__("all_rates_finite_positive",False),lambda x:x["exact_controls"].__setitem__("theta_pi_over_2_rate_equals_gamma",False),lambda x:x["ownership"].__setitem__("jump_clock_angles_and_signs_imported",False),lambda x:x["ownership"].__setitem__("gu_action_or_record_owner_constructed",True),lambda x:x["ownership"].__setitem__("prediction_or_confirmation_credit",True),lambda x:x["decision"].__setitem__("k981_not_an_isolated_exact_horn",False),lambda x:x.__setitem__("source_and_ledger_effect","changed")];caught=0
    for f in muts:q=copy.deepcopy(p);f(q);caught+=not ok(q)
    print(f"K987 hostile: {caught}/{len(muts)}");return 0 if caught==len(muts) else 1
if __name__=="__main__":raise SystemExit(main())
