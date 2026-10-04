#!/usr/bin/env python3
from copy import deepcopy
import importlib.util
from pathlib import Path
P=Path(__file__).with_name("k1003_k1002_exponential_bell_persistence.py");S=importlib.util.spec_from_file_location("k1003",P);M=importlib.util.module_from_spec(S);S.loader.exec_module(M)
def main():
 b=M.build();spec=[(["law","lambda(t)"],"exp(-gamma t)"),(["law","S_max(t)"],"sqrt(2)(1+exp(-2 gamma t))"),(["law","finite_time_violation"],False),(["law","limit_at_infinity"],"0"),(["fixed_witness","S_fixed(t)"],"S_max"),(["fixed_witness","violation_interval"],"all t"),(["fixed_witness","finite_threshold_is_witness_specific"],False),(["distinction","optimized_bell_death_time"],"finite"),(["distinction","requires_gamma_positive"],False),(["controls","t_zero_S_max_squared"],"4"),(["controls","finite_t_S_max_strictly_above_two"],False),(["ownership","gu_effect"],"confirmation")];caught=0
 for path,val in spec:
  x=deepcopy(b);cur=x
  for k in path[:-1]:cur=cur[k]
  cur[path[-1]]=val
  try:M.validate(x)
  except (AssertionError,KeyError,TypeError):caught+=1
 print(f"K1003 hostile: {caught}/{len(spec)}");return 0 if caught==len(spec) else 1
if __name__=="__main__":raise SystemExit(main())
