#!/usr/bin/env python3
import copy,importlib.util
from pathlib import Path
H=Path(__file__).resolve().parent;s=importlib.util.spec_from_file_location("k965",H/"k965_k964_action_reservoir_demand_disposition.py");m=importlib.util.module_from_spec(s);s.loader.exec_module(m)
def ok(p):
    try:m.validate(p);return True
    except (AssertionError,KeyError):return False
def main():
    p=m.build();muts=[lambda x:x["demand"].__setitem__("physical_quotient_and_positive_pairing_required",False),lambda x:x["demand"].__setitem__("action_owned_local_coupling_required",False),lambda x:x["demand"].__setitem__("continuum_reservoir_or_explicit_reset_law_required",False),lambda x:x["demand"].__setitem__("controlled_thermodynamic_or_white_noise_limit_required",False),lambda x:x["demand"].__setitem__("remote_marginal_and_locality_theorem_required",False),lambda x:x["demand"].__setitem__("distinct_holdout_frozen_before_scoring",False),lambda x:x["discriminator"].__setitem__("status","scored"),lambda x:x["ownership"].__setitem__("all_quantum_state_trace_clock_and_environment_semantics_imported",False),lambda x:x["ownership"].__setitem__("gu_action_or_physical_quotient_constructed",True),lambda x:x["ownership"].__setitem__("prediction_or_confirmation_credit",True),lambda x:x["ownership"].__setitem__("source_claim_or_ledger_verdict_changed",True),lambda x:x["decision"].__setitem__("candidate_action_requirement_sharpened",False)];caught=0
    for f in muts:q=copy.deepcopy(p);f(q);caught+=not ok(q)
    print(f"K965 hostile: {caught}/{len(muts)}");return 0 if caught==len(muts) else 1
if __name__=="__main__":raise SystemExit(main())
