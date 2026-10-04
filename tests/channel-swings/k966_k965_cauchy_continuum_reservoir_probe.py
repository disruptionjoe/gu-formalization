#!/usr/bin/env python3
import copy,importlib.util
from pathlib import Path
H=Path(__file__).resolve().parent;s=importlib.util.spec_from_file_location("k966",H/"k966_k965_cauchy_continuum_reservoir.py");m=importlib.util.module_from_spec(s);s.loader.exec_module(m)
def ok(p):
    try:m.validate(p);return True
    except (AssertionError,KeyError):return False
def main():
    p=m.build();muts=[lambda x:x["exact_controls"].__setitem__("gamma",0),lambda x:x["exact_controls"].__setitem__("normalization",False),lambda x:x["exact_controls"].__setitem__("sample_equalities",False),lambda x:x["construction"].__setitem__("positive_pairing",False),lambda x:x["construction"].__setitem__("unitary_group",False),lambda x:x["construction"].__setitem__("remote_marginal_invariant",False),lambda x:x["construction"].__setitem__("coherence","unknown"),lambda x:x["decision"].__setitem__("exact_continuum_escape_constructed",False),lambda x:x["ownership"].__setitem__("continuum_measure_rate_split_and_trace_imported",False),lambda x:x["ownership"].__setitem__("gu_action_or_physical_quotient_constructed",True),lambda x:x["ownership"].__setitem__("prediction_or_confirmation_credit",True)];caught=0
    for f in muts:q=copy.deepcopy(p);f(q);caught+=not ok(q)
    print(f"K966 hostile: {caught}/{len(muts)}");return 0 if caught==len(muts) else 1
if __name__=="__main__":raise SystemExit(main())
