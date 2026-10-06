#!/usr/bin/env python3
"""Hostile mutations for K1228."""
import copy
import k1228_block_interleaving_drift_controls as p
def main():
  edits=[(("control","planted_nonzero_drift_entries"),1),(("decision","within_block_relations_detect_preparation_conditioned_inconsistency"),False),
    (("decision","cross_block_comparison_detects_planted_drift"),False),(("decision","zero_residuals_prove_memoryless_hardware"),True),
    (("decision","postselected_counts_self_validate_locality"),True),(("release_test","fixed_within_residuals_zero"),False),
    (("release_test","drifted_within_residuals_zero"),False),(("release_test","planted_cross_block_drift_detected"),False),
    (("release_test","exact_two_drift_entries"),False),(("ownership","gu_native_effect"),"prediction")]
  n=0
  for path,val in edits:
    x=copy.deepcopy(p.build());d=x
    for k in path[:-1]:d=d[k]
    d[path[-1]]=val
    try:p.validate(x)
    except AssertionError:n+=1
  assert n==len(edits);print(f"K1228 hostile probes: {n}/{len(edits)}")
if __name__=="__main__":main()
