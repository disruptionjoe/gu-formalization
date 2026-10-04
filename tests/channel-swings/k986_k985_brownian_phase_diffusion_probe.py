#!/usr/bin/env python3
import copy,importlib.util
from pathlib import Path
H=Path(__file__).resolve().parent;s=importlib.util.spec_from_file_location("k986",H/"k986_k985_brownian_phase_diffusion.py");m=importlib.util.module_from_spec(s);s.loader.exec_module(m)
def ok(p):
    try:m.validate(p);return True
    except (AssertionError,KeyError):return False
def main():
    p=m.build();muts=[lambda x:x["construction"].__setitem__("continuous_paths_almost_surely",False),lambda x:x["construction"].__setitem__("stationary_independent_increments",False),lambda x:x["construction"].__setitem__("same_dephasing_semigroup_as_k956",False),lambda x:x["construction"].__setitem__("remote_marginal_invariant",False),lambda x:x["exact_controls"].__setitem__("rows",[]),lambda x:x["exact_controls"].__setitem__("all_characteristic_identities_replayed",False),lambda x:x["exact_controls"].__setitem__("identity_at_zero",False),lambda x:x["exact_controls"].__setitem__("strict_decay_after_zero",False),lambda x:x["ownership"].__setitem__("brownian_clock_and_probability_imported",False),lambda x:x["ownership"].__setitem__("white_noise_limit_or_stochastic_action_imported",False),lambda x:x["ownership"].__setitem__("positive_hilbert_pairing_imported",False),lambda x:x["ownership"].__setitem__("gu_action_or_physical_quotient_constructed",True),lambda x:x["ownership"].__setitem__("prediction_or_confirmation_credit",True),lambda x:x["decision"].__setitem__("exact_nonjump_horn_constructed",False),lambda x:x.__setitem__("source_and_ledger_effect","changed")];caught=0
    for f in muts:q=copy.deepcopy(p);f(q);caught+=not ok(q)
    print(f"K986 hostile: {caught}/{len(muts)}");return 0 if caught==len(muts) else 1
if __name__=="__main__":raise SystemExit(main())
