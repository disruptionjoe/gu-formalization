#!/usr/bin/env python3
"""Hostile mutations for K1757's stability theorem."""
import copy,importlib.util,json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];P=ROOT/"tests/channel-swings/k1757_ou_variational_stability.py"
s=importlib.util.spec_from_file_location("m",P);m=importlib.util.module_from_spec(s);s.loader.exec_module(m);base=json.loads(m.ARTIFACT.read_text())
mutations=[lambda d:d["setting"].__setitem__("wasserstein_bound","none"),lambda d:d["derivative_envelope"].__setitem__("rounded_stability_constant",1),
 lambda d:d.__setitem__("theorem","J>=J_R"),lambda d:d["decision"].__setitem__("explicit_stability_modulus_proved",False),
 lambda d:d["decision"].__setitem__("rare_atom_face_identified_with_pointwise_continuity",True),lambda d:d["decision"].__setitem__("global_optimizer_proved",True)]
caught=0
for i,mut in enumerate(mutations,1):
 d=copy.deepcopy(base);mut(d);ok=all(v for _,v in m.validate(d));assert not ok,f"mutation {i} escaped";caught+=1;print(f"PASS {i:02d}: rejected mutation")
print(f"RESULT: PASS {caught}/{len(mutations)}")
