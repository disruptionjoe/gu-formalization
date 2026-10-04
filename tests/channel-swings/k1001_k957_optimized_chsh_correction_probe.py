#!/usr/bin/env python3
"""Hostile mutations for K1001."""
from copy import deepcopy
import importlib.util
from pathlib import Path

P = Path(__file__).with_name("k1001_k957_optimized_chsh_correction.py")
S = importlib.util.spec_from_file_location("k1001", P); M = importlib.util.module_from_spec(S); S.loader.exec_module(M)

def main():
    base = M.build(); muts = []
    def add(path, value):
        x = deepcopy(base); cur = x
        for key in path[:-1]: cur = cur[key]
        cur[path[-1]] = value; muts.append(x)
    add(["correlation_tensor"], "diag(lambda,lambda,1)")
    add(["horodecki_spectrum"], ["1", "lambda", "lambda"])
    add(["optimized_chsh", "formula"], "2 sqrt(1+lambda)")
    add(["optimized_chsh", "violation_iff"], "lambda>sqrt(2)-1")
    add(["optimized_chsh", "alice_settings"], ["Z", "Z"])
    add(["optimized_chsh", "bob_settings"], ["Z"])
    add(["k957_scope_correction", "preserved_formula"], "S_max")
    add(["k957_scope_correction", "not_the_post_damping_optimum"], False)
    add(["k957_scope_correction", "old_threshold_applies_only_to_fixed_witness"], False)
    add(["exact_controls", "lambda_two_fifths_S_max_squared"], "98/25")
    add(["exact_controls", "lambda_zero_saturates_classical_boundary"], False)
    add(["exact_controls", "lambda_one_saturates_tsirelson"], False)
    add(["ownership", "gu_physical_quotient_or_action_constructed"], True)
    caught = 0
    for x in muts:
        try: M.validate(x)
        except (AssertionError, KeyError, TypeError): caught += 1
    print(f"K1001 hostile: {caught}/{len(muts)}")
    return 0 if caught == len(muts) else 1

if __name__ == "__main__": raise SystemExit(main())
