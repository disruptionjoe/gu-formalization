#!/usr/bin/env python3
import copy,importlib.util
from pathlib import Path
H=Path(__file__).resolve().parent;s=importlib.util.spec_from_file_location("k958",H/"k958_quantum_anchor_interference_visibility_decay.py");m=importlib.util.module_from_spec(s);s.loader.exec_module(m)
def good(p):
 try:m.validate(p);return True
 except (AssertionError,KeyError):return False
def main():
 p=m.build();muts=[lambda x:x["fringe_law"].__setitem__("visibility","V=1"),lambda x:x["fringe_law"].__setitem__("continuous_decay","unknown"),lambda x:x["exact_controls"].__setitem__("normalization_all_rows",False),lambda x:x["exact_controls"].__setitem__("visibility_equals_lambda_all_rows",False),lambda x:x["exact_controls"].__setitem__("unit_visibility_at_lambda_one",False),lambda x:x["exact_controls"].__setitem__("zero_visibility_at_lambda_zero",False),lambda x:x["decision"].__setitem__("visibility_decay_exact",False),lambda x:x["decision"].__setitem__("same_semigroup_parameter_as_k956",False),lambda x:x["ownership"].__setitem__("gu_interference_prediction",True)]
 caught=0
 for f in muts:q=copy.deepcopy(p);f(q);caught+=not good(q)
 print(f"K958 hostile: {caught}/{len(muts)}");return 0 if caught==len(muts) else 1
if __name__=="__main__":raise SystemExit(main())
