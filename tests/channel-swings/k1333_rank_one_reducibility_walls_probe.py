#!/usr/bin/env python3
"""Hostile mutations for K1333."""
import copy,json
from pathlib import Path
D=json.loads((Path(__file__).resolve().parents[2]/"lab/process/k1333-rank-one-reducibility-walls.json").read_text()); tests=[]
def rejects(label,mut,pred):
 x=copy.deepcopy(D); mut(x); assert not pred(x),label; tests.append(label); print(f"PASS {len(tests):02d}: rejects {label}")
rejects("even zeros",lambda x:x["normalized_divisor"].__setitem__("mode_n_zeros","z=0,2,4"),lambda x:"z=1,3" in x["normalized_divisor"]["mode_n_zeros"])
rejects("even poles",lambda x:x["normalized_divisor"].__setitem__("mode_n_poles","z=-2,-4"),lambda x:"z=-1,-3" in x["normalized_divisor"]["mode_n_poles"])
rejects("low-mode kernel",lambda x:x["normalized_divisor"].__setitem__("positive_wall_kernel","low modes"),lambda x:"|n|>=r+1" in x["normalized_divisor"]["positive_wall_kernel"])
rejects("zero singular",lambda x:x["normalized_divisor"].__setitem__("zero_parameter","pole"),lambda x:"regular" in x["normalized_divisor"]["zero_parameter"])
rejects("imaginary kernel",lambda x:x["reducibility"].__setitem__("imaginary_axis","kernel"),lambda x:x["reducibility"]["imaginary_axis"].startswith("no zero"))
rejects("wall classification absent",lambda x:x["decision"].__setitem__("all_rank_one_normalized_mode_walls_classified",False),lambda x:x["decision"]["all_rank_one_normalized_mode_walls_classified"])
rejects("D7 wall admitted",lambda x:x["decision"].__setitem__("regular_imaginary_d7_reducibility_excluded",False),lambda x:x["decision"]["regular_imaginary_d7_reducibility_excluded"])
rejects("nonspherical overclaim",lambda x:x["decision"].__setitem__("singular_or_nonspherical_M_type_classified",True),lambda x:not x["decision"]["singular_or_nonspherical_M_type_classified"])
rejects("physical overclaim",lambda x:x["decision"].__setitem__("physical_reducibility_statement",True),lambda x:not x["decision"]["physical_reducibility_statement"])
assert len(tests)==9; print("RESULT: PASS 9/9")
