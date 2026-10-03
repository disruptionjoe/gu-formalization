#!/usr/bin/env python3
import copy,importlib.util
from pathlib import Path
H=Path(__file__).resolve().parent;s=importlib.util.spec_from_file_location("k959",H/"k959_quantum_anchor_cross_benchmark_coherence_law.py");m=importlib.util.module_from_spec(s);s.loader.exec_module(m)
def good(p):
 try:m.validate(p);return True
 except (AssertionError,KeyError):return False
def main():
 p=m.build();muts=[lambda x:x["cross_anchor_law"].__setitem__("identity","S=V"),lambda x:x["cross_anchor_law"].__setitem__("shared_rate_is_not_empirically_asserted_across_distinct_environments",False),lambda x:x["exact_controls"].__setitem__("identity_all_rows",False),lambda x:x["exact_controls"].__setitem__("rational_threshold_width","1/2"),lambda x:x["discriminator"].__setitem__("candidate_with_one_shared_law_must_use_one_coherence_eigenvalue",False),lambda x:x["discriminator"].__setitem__("different_environments_may_have_different_gamma",False),lambda x:x["discriminator"].__setitem__("calibration_fit_is_not_held_out_prediction",False),lambda x:x["discriminator"].__setitem__("distinct_held_out_family_still_required",False),lambda x:x["decision"].__setitem__("cross_benchmark_information_gain",False),lambda x:x["decision"].__setitem__("one_parameter_relation_derived",False)]
 caught=0
 for f in muts:q=copy.deepcopy(p);f(q);caught+=not good(q)
 print(f"K959 hostile: {caught}/{len(muts)}");return 0 if caught==len(muts) else 1
if __name__=="__main__":raise SystemExit(main())
