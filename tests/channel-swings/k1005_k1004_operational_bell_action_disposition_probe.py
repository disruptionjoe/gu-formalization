#!/usr/bin/env python3
from copy import deepcopy
import importlib.util
from pathlib import Path
P=Path(__file__).with_name("k1005_k1004_operational_bell_action_disposition.py");S=importlib.util.spec_from_file_location("k1005",P);M=importlib.util.module_from_spec(S);S.loader.exec_module(M)
def main():
 b=M.build();spec=[(["preserved","fixed_witness_formula"],False),(["preserved","remote_marginal_theorem"],False),(["corrected","fixed_threshold_is_not_optimized_bell_death"],False),(["corrected","optimized_formula"],"sqrt(2)(1+V)"),(["corrected","finite_optimized_death_time"],True),(["corrected","asymptotic_resolution_cost"],False),(["native_requirements"],b["native_requirements"][:-1]),(["holdout","visibility"],"1/2"),(["holdout","fixed_witness"],"violation"),(["holdout","status"],"scored"),(["effects","prediction"],"positive")];caught=0
 for path,val in spec:
  x=deepcopy(b);cur=x
  for k in path[:-1]:cur=cur[k]
  cur[path[-1]]=val
  try:M.validate(x)
  except (AssertionError,KeyError,TypeError):caught+=1
 print(f"K1005 hostile: {caught}/{len(spec)}");return 0 if caught==len(spec) else 1
if __name__=="__main__":raise SystemExit(main())
