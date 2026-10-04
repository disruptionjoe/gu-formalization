#!/usr/bin/env python3
import copy,importlib.util
from pathlib import Path
H=Path(__file__).resolve().parent;s=importlib.util.spec_from_file_location("k964",H/"k964_k963_white_noise_scaling_boundary.py");m=importlib.util.module_from_spec(s);s.loader.exec_module(m)
def ok(p):
    try:m.validate(p);return True
    except (AssertionError,KeyError):return False
def main():
    p=m.build();muts=[lambda x:x["exact_controls"].__setitem__("gamma",0),lambda x:x["exact_controls"].__setitem__("grid_exact",False),lambda x:x["exact_controls"].__setitem__("coupling_strictly_increases",False),lambda x:x["exact_controls"].__setitem__("scaled_coupling_converges_to_sqrt_gamma",False),lambda x:x["boundary"].__setitem__("finite_coupling_continuum_limit",True),lambda x:x["boundary"].__setitem__("finite_ancilla_supply_continuum_limit",True),lambda x:x["boundary"].__setitem__("white_noise_or_thermodynamic_resource_required",False),lambda x:x["decision"].__setitem__("singular_resource_boundary_proved",False),lambda x:x["ownership"].__setitem__("gamma_clock_scaling_and_freshness_imported",False),lambda x:x["ownership"].__setitem__("gu_action_or_physical_quotient_constructed",True),lambda x:x["ownership"].__setitem__("prediction_or_confirmation_credit",True)];caught=0
    for f in muts:q=copy.deepcopy(p);f(q);caught+=not ok(q)
    print(f"K964 hostile: {caught}/{len(muts)}");return 0 if caught==len(muts) else 1
if __name__=="__main__":raise SystemExit(main())
