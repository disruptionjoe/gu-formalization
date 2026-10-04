#!/usr/bin/env python3
from copy import deepcopy
import importlib.util
from pathlib import Path
P=Path(__file__).with_name("k1004_k959_visibility_maximal_chsh_law.py");S=importlib.util.spec_from_file_location("k1004",P);M=importlib.util.module_from_spec(S);S.loader.exec_module(M)
def main():
 b=M.build();spec=[(["shared_imported_law","visibility"],"V=lambda^2"),(["shared_imported_law","fixed_relation"],"S_max"),(["shared_imported_law","optimized_relation"],"S_max/2-1=V"),(["shared_imported_law","optimized_formula"],"sqrt(2)(1+V)"),(["finite_resolution","visibility_requirement"],"V>=delta"),(["finite_resolution","strict_violation_only"],"V>sqrt(2)-1"),(["finite_resolution","delta_one_tenth_squared_requirement"],"1/10"),(["holdout","S_fixed_squared"],"116/25"),(["holdout","S_max_squared"],"98/25"),(["holdout","fixed_fails_while_optimized_passes"],False),(["controls","nonlinear_not_linear_optimum"],False),(["ownership","gu_effect"],"prediction")];caught=0
 for path,val in spec:
  x=deepcopy(b);cur=x
  for k in path[:-1]:cur=cur[k]
  cur[path[-1]]=val
  try:M.validate(x)
  except (AssertionError,KeyError,TypeError):caught+=1
 print(f"K1004 hostile: {caught}/{len(spec)}");return 0 if caught==len(spec) else 1
if __name__=="__main__":raise SystemExit(main())
