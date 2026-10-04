#!/usr/bin/env python3
import copy,importlib.util
from pathlib import Path
H=Path(__file__).resolve().parent;s=importlib.util.spec_from_file_location("k963",H/"k963_k962_fresh_ancilla_dephasing_dilation.py");m=importlib.util.module_from_spec(s);s.loader.exec_module(m)
def ok(p):
    try:m.validate(p);return True
    except (AssertionError,KeyError):return False
def main():
    p=m.build();muts=[lambda x:x["construction"].__setitem__("cptp",False),lambda x:x["construction"].__setitem__("remote_marginal_invariant",False),lambda x:x["construction"].__setitem__("n_step_coherence","lambda"),lambda x:x["exact_controls"].__setitem__("semigroup_on_integer_steps",False),lambda x:x["exact_controls"].__setitem__("identity_at_n_zero",False),lambda x:x["exact_controls"].__setitem__("strict_decay",False),lambda x:x["resource"].__setitem__("reset_or_unbounded_tape_required_for_unbounded_time",False),lambda x:x["resource"].__setitem__("closed_finite_environment",True),lambda x:x["ownership"].__setitem__("ancilla_preparation_trace_and_clock_imported",False),lambda x:x["ownership"].__setitem__("gu_action_or_physical_quotient_constructed",True),lambda x:x["ownership"].__setitem__("prediction_or_confirmation_credit",True)];caught=0
    for f in muts:q=copy.deepcopy(p);f(q);caught+=not ok(q)
    print(f"K963 hostile: {caught}/{len(muts)}");return 0 if caught==len(muts) else 1
if __name__=="__main__":raise SystemExit(main())
