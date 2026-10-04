#!/usr/bin/env python3
import copy,importlib.util
from pathlib import Path
H=Path(__file__).resolve().parent;s=importlib.util.spec_from_file_location("k982",H/"k982_k981_poisson_generator_resource_boundary.py");m=importlib.util.module_from_spec(s);s.loader.exec_module(m)
def ok(p):
    try:m.validate(p);return True
    except (AssertionError,KeyError,TypeError):return False
def main():
    p=m.build();muts=[lambda x:x["dependency"].__setitem__("exact_stochastic_horn",False),lambda x:x["dependency"].__setitem__("source_and_ledger_effect_none",False),lambda x:x["generator"].__setitem__("finite_event_rate",0),lambda x:x["generator"].__setitem__("grid_step_or_h",1),lambda x:x["generator"].__setitem__("h_inverse_half_coupling",True),lambda x:x["resource"].__setitem__("rows",[]),lambda x:x["resource"].__setitem__("mean_and_variance_equal_gamma_T",False),lambda x:x["resource"].__setitem__("unbounded_horizon_count_support",False),lambda x:x["resource"].__setitem__("instantaneous_point_jumps_idealized",False),lambda x:x["resource"].__setitem__("classical_random_clock_and_probability_law_imported",False),lambda x:x["resource"].__setitem__("deterministic_closed_hamiltonian_parent_supplied",True),lambda x:x["decision"].__setitem__("k978_grid_coupling_divergence_not_universal_across_horns",False),lambda x:x["decision"].__setitem__("finite_rate_does_not_remove_stochastic_owner_debt",False),lambda x:x["ownership"].__setitem__("gu_action_or_clock_owner_constructed",True),lambda x:x["ownership"].__setitem__("prediction_or_confirmation_credit",True),lambda x:x.__setitem__("source_and_ledger_effect","changed")];caught=0
    for f in muts:q=copy.deepcopy(p);f(q);caught+=not ok(q)
    print(f"K982 hostile: {caught}/{len(muts)}");return 0 if caught==len(muts) else 1
if __name__=="__main__":raise SystemExit(main())
