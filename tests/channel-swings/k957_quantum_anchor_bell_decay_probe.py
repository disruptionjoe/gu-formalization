#!/usr/bin/env python3
import copy, importlib.util
from pathlib import Path
H=Path(__file__).resolve().parent; s=importlib.util.spec_from_file_location("k957",H/"k957_quantum_anchor_bell_decay.py"); m=importlib.util.module_from_spec(s); s.loader.exec_module(m)
def good(p):
  try:m.validate(p);return True
  except (AssertionError,KeyError):return False
def main():
 p=m.build(); muts=[
 lambda x:x["bell_decay"].__setitem__("chsh_formula","S=2"),lambda x:x["bell_decay"].__setitem__("remote_marginal","changed"),
 lambda x:x["exact_controls"].__setitem__("bell_endpoint_S_squared","4"),lambda x:x["exact_controls"].__setitem__("dephased_endpoint_S_squared","4"),
 lambda x:x["exact_controls"].__setitem__("two_fifths_does_not_violate",False),lambda x:x["exact_controls"].__setitem__("five_twelfths_violates",False),
 lambda x:x["decision"].__setitem__("bell_decay_exact",False),lambda x:x["decision"].__setitem__("no_signalling_preserved",False),
 lambda x:x["ownership"].__setitem__("spacelike_local_net_constructed",True),lambda x:x["ownership"].__setitem__("gu_prediction",True)]
 caught=0
 for f in muts:q=copy.deepcopy(p);f(q);caught+=not good(q)
 print(f"K957 hostile: {caught}/{len(muts)}");return 0 if caught==len(muts) else 1
if __name__=="__main__":raise SystemExit(main())
