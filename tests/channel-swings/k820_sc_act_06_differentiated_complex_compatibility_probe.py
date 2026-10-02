#!/usr/bin/env python3
from __future__ import annotations
import copy,importlib.util
from pathlib import Path
P=Path(__file__).with_name("k820_sc_act_06_differentiated_complex_compatibility.py");S=importlib.util.spec_from_file_location("k820",P);M=importlib.util.module_from_spec(S);S.loader.exec_module(M)
def main()->int:
    muts=[lambda x:x["differentiated_complex_theorem"].__setitem__("left_identity","none"),lambda x:x["differentiated_complex_theorem"].__setitem__("right_identity","none"),lambda x:x["differentiated_complex_theorem"].__setitem__("rank_budget_without_identities_is_credited",True),lambda x:x["differentiated_complex_theorem"].__setitem__("identities_prove_exactness",True),lambda x:x["exact_controls"].__setitem__("valid_tau_rank",2),lambda x:x["exact_controls"].__setitem__("valid_gauge_projection_zero",False),lambda x:x["exact_controls"].__setitem__("valid_redundancy_on_kernel_zero",False),lambda x:x["exact_controls"].__setitem__("invalid_gauge_rejected",False),lambda x:x["exact_controls"].__setitem__("invalid_redundancy_rejected",False),lambda x:x["decision"].__setitem__("actual_moving_complex_constructed",True),lambda x:x["decision"].__setitem__("global_sc_act_06_proved_or_refuted",True),lambda x:x.__setitem__("target_claim","NONE")]
    for i,mut in enumerate(muts):
        q=copy.deepcopy(M.build());mut(q)
        try:M.validate(q)
        except AssertionError:continue
        raise AssertionError(i)
    print("K820 hostile mutations rejected: 12/12");return 0
if __name__=="__main__":raise SystemExit(main())
