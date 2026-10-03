#!/usr/bin/env python3
"""Independent hostile replay for K956."""
import copy, importlib.util
from pathlib import Path

HERE = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location("k956", HERE / "k956_quantum_anchor_local_dephasing_semigroup.py")
m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)

def ok(p):
    try: m.validate(p); return True
    except (AssertionError, KeyError): return False

def main():
    p=m.build(); assert ok(p)
    muts=[
      lambda x:x["semigroup"].__setitem__("completely_positive_trace_preserving",False),
      lambda x:x["semigroup"].__setitem__("unital",False),
      lambda x:x["exact_controls"].__setitem__("composition_lambda_half_two_thirds_equals_one_third",False),
      lambda x:x["exact_controls"].__setitem__("identity_at_lambda_one",False),
      lambda x:x["exact_controls"].__setitem__("complete_dephasing_at_lambda_zero",False),
      lambda x:x["exact_controls"].__setitem__("remote_marginal_all_samples",False),
      lambda x:x["exact_controls"].__setitem__("trace_all_samples",False),
      lambda x:x["locality"].__setitem__("bob_marginal_invariant_for_every_input",False),
      lambda x:x["ownership"].__setitem__("gu_action_or_physical_quotient_constructed",True),
      lambda x:x["ownership"].__setitem__("prediction_or_confirmation_credit",True)]
    caught=0
    for f in muts:
        q=copy.deepcopy(p); f(q); caught += not ok(q)
    print(f"K956 hostile: {caught}/{len(muts)}")
    return 0 if caught==len(muts) else 1
if __name__=="__main__": raise SystemExit(main())
