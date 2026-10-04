#!/usr/bin/env python3
from copy import deepcopy
import importlib.util
from pathlib import Path
P=Path(__file__).with_name("k1002_k1001_fixed_versus_adaptive_bell_witness.py");S=importlib.util.spec_from_file_location("k1002",P);M=importlib.util.module_from_spec(S);S.loader.exec_module(M)
def main():
    b=M.build(); paths=[
      (["separator","visibility"],"1/2"),(["separator","S_fixed_squared"],"116/25"),(["separator","fixed_violates"],True),
      (["separator","S_max_squared"],"98/25"),(["separator","adaptive_violates"],False),(["separator","fixed_settings"],"Z"),
      (["separator","adaptive_settings"],"Z"),(["theorem","fixed_violation_iff"],"lambda>0"),(["theorem","adaptive_violation_iff"],"lambda>sqrt(2)-1"),
      (["theorem","fixed_witness_death_is_not_state_locality_death"],False),(["controls","same_remote_marginal"],"not fixed"),
      (["ownership","gu_effect"],"prediction")]
    caught=0
    for path,val in paths:
      x=deepcopy(b); cur=x
      for k in path[:-1]: cur=cur[k]
      cur[path[-1]]=val
      try:M.validate(x)
      except (AssertionError,KeyError,TypeError):caught+=1
    print(f"K1002 hostile: {caught}/{len(paths)}");return 0 if caught==len(paths) else 1
if __name__=="__main__":raise SystemExit(main())
