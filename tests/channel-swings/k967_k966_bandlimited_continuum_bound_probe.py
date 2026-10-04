#!/usr/bin/env python3
import copy,importlib.util
from pathlib import Path
H=Path(__file__).resolve().parent;s=importlib.util.spec_from_file_location("k967",H/"k967_k966_bandlimited_continuum_bound.py");m=importlib.util.module_from_spec(s);s.loader.exec_module(m)
def ok(p):
    try:m.validate(p);return True
    except (AssertionError,KeyError):return False
def main():
    p=m.build();muts=[lambda x:x["exact_controls"].__setitem__("gamma",0),lambda x:x["exact_controls"].__setitem__("Omega",0),lambda x:x["exact_controls"].__setitem__("tail_inequality",False),lambda x:x["exact_controls"].__setitem__("normalization_penalty_included",False),lambda x:x["theorem"].__setitem__("uniform_all_real_times",False),lambda x:x["theorem"].__setitem__("normalized_characteristic_error","none"),lambda x:x["decision"].__setitem__("uniform_bandwidth_bound_proved",False),lambda x:x["ownership"].__setitem__("spectral_cutoff_and_normalization_imported",False),lambda x:x["ownership"].__setitem__("gu_action_or_physical_quotient_constructed",True),lambda x:x["ownership"].__setitem__("prediction_or_confirmation_credit",True)];caught=0
    for f in muts:q=copy.deepcopy(p);f(q);caught+=not ok(q)
    print(f"K967 hostile: {caught}/{len(muts)}");return 0 if caught==len(muts) else 1
if __name__=="__main__":raise SystemExit(main())
