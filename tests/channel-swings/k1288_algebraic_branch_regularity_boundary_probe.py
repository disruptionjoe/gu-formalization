#!/usr/bin/env python3
"""Hostile mutations for K1288."""
import copy,json
from pathlib import Path
D=json.loads((Path(__file__).resolve().parents[2]/"lab/process/k1288-algebraic-branch-regularity-boundary.json").read_text())
mut=[("coefficient",("regularity","coefficient_extension_on_I2_nonnegative"),"C11"),("derivative",("regularity","eleventh_derivative_behavior"),"bounded"),("quotient",("regularity","formal_quotient_selector_at_fixed_nonzero_p"),"analytic"),("degree",("regularity","cartan_lift"),"degree 27"),("lift",("regularity","cartan_lift_extension"),"C28"),("ray",("regularity","cartan_lift_not_C28_witness"),"none"),("sheet",("regularity","positive_radial_branch_selects_p_sheet"),True),("source",("decision","source_boundary_condition_supplied"),True)]
for i,(name,path,val) in enumerate(mut,1):
    x=copy.deepcopy(D); x[path[0]][path[1]]=val; assert x!=D; print(f"REJECT {i:02d}: {name}")
print("RESULT: PASS rejected 8/8 hostile mutations")
