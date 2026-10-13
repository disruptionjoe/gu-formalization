#!/usr/bin/env python3
"""Hostile mutations for K1759's rare-atom composition."""
import copy,importlib.util,json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];P=ROOT/"tests/channel-swings/k1759_rare_atom_quantitative_collar.py"
s=importlib.util.spec_from_file_location("m",P);m=importlib.util.module_from_spec(s);s.loader.exec_module(m);base=json.loads(m.ARTIFACT.read_text())
mutations=[lambda d:d["composition"].__setitem__("arb_input","uncertified"),lambda d:d["composition"].__setitem__("ou_monotonicity","decreasing"),
 lambda d:d["composition"].__setitem__("collar_choice","0<z<=1"),lambda d:d["decision"].__setitem__("quantitative_rare_atom_collar_excluded",False),
 lambda d:d["decision"].__setitem__("joint_corner_excluded",False),lambda d:d["decision"].__setitem__("collar_is_practically_wide",True),
 lambda d:d["decision"].__setitem__("global_optimizer_proved",True)]
caught=0
for i,mut in enumerate(mutations,1):
 d=copy.deepcopy(base);mut(d);ok=all(v for _,v in m.validate(d));assert not ok,f"mutation {i} escaped";caught+=1;print(f"PASS {i:02d}: rejected mutation")
print(f"RESULT: PASS {caught}/{len(mutations)}")
