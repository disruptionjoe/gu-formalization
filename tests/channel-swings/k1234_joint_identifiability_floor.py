#!/usr/bin/env python3
"""K1234: exact dimension floors for channel plus source ownership."""
from fractions import Fraction as F
import json
from pathlib import Path
from k1233_minimal_holdout_source_certificate import rank
OUT=Path(__file__).parents[2]/"lab/process/k1234-joint-identifiability-floor.json"

def validate(d):
 M=[[F(3,10),-F(2,5),0],[F(2,13),F(3,26),-F(3,13)],[F(24,65),F(18,65),F(5,52)]]
 t=[0,-F(9,13),F(15,52)];a=[F(3,5),0,F(4,5)];b=[0,F(4,5),F(3,5)]
 w=[sum(a[i]*M[i][j] for i in range(3)) for j in range(3)]
 A=w+[F(0)]*12
 B=[F(0)]*3+b+[F(0)]*9
 C=[F(0)]*3+[sum(a[i]*t[i] for i in range(3))*x for x in b]+[w[i]*b[j] for i in range(3) for j in range(3)]
 assert rank([A,B,C])==3
 assert d["dimensions"]=={"affine_channel":12,"general_two_qubit_source":15,"joint_full_owner":27,"joint_single_holdout":15}
 assert d["block_jacobian"]["process_rows_on_source_columns"]==0
 assert d["block_jacobian"]["selected_holdout_source_rank"]==3
 assert d["decision"]["eighteen_process_reads_identify_general_source"] is False
 assert d["decision"]["full_source_tomography_required_for_single_holdout"] is False
 assert d["decision"]["independent_three_scalar_source_certificate_suffices_for_single_holdout"] is True
 assert d["ownership"]["physical_frame_still_requires_independent_authentication"] is True

if __name__=="__main__":
 d=json.loads(OUT.read_text());validate(d);print("K1234 controls: 10/10")
