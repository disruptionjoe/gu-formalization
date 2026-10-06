#!/usr/bin/env python3
"""Hostile mutations for K1227."""
import copy
import k1227_spam_gauge_nonidentifiability as p
def main():
    edits=[(("control","probability_equalities"),17),(("control","distinct_channel_coordinates"),False),
      (("decision","twelve_nominal_statistics_self_authenticate"),True),(("decision","independent_spam_or_self_consistent_gate_set_required"),False),
      (("decision","optimized_chsh_basis_invariant_under_this_rotation"),False),(("release_test","all_probability_equalities"),False),
      (("release_test","coordinates_change"),False),(("release_test","physical_rotation"),False),
      (("ownership","gu_native_effect"),"confirmation")]
    n=0
    for path,val in edits:
      x=copy.deepcopy(p.build());d=x
      for k in path[:-1]:d=d[k]
      d[path[-1]]=val
      try:p.validate(x)
      except AssertionError:n+=1
    assert n==len(edits);print(f"K1227 hostile probes: {n}/{len(edits)}")
if __name__=="__main__":main()
