#!/usr/bin/env python3
"""Hostile mutations for K1219."""
import copy
import k1219_three_aligned_axes_nonidentifiability as p
def main():
    edits=[(("shared_aligned_transfers",),["0","0","1"]),(("low_channel","S_squared_over_4"),"1"),
      (("high_channel","S_squared_over_4"),"1"),(("high_channel","cp"),False),
      (("decision","three_aligned_axis_reads_identify_score"),True),
      (("decision","off_diagonal_frame_transport_is_load_bearing"),False),
      (("decision","pauli_three_axis_result_transfers_to_general_unital_class"),True),
      (("release_test","cyclic_matrix_orthogonal_det_plus_one"),False),(("ownership","gu_prediction"),True)]
    n=0
    for path,val in edits:
        x=copy.deepcopy(p.build());d=x
        for k in path[:-1]:d=d[k]
        d[path[-1]]=val
        try:p.validate(x)
        except AssertionError:n+=1
    assert n==len(edits);print(f"K1219 hostile probes: {n}/{len(edits)}")
if __name__=="__main__":main()
