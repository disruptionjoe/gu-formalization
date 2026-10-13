#!/usr/bin/env python3
"""Hostile mutations for the K1756 Arb ordering."""
import copy,importlib.util,json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];P=ROOT/"tests/channel-swings/k1756_rademacher_arb_gap.py"
s=importlib.util.spec_from_file_location("m",P);m=importlib.util.module_from_spec(s);s.loader.exec_module(m)
base=json.loads(m.ARTIFACT.read_text())
mutations=[lambda d:d.__setitem__("backend","float64"),lambda d:d["comparison"].__setitem__("compact_cell_count",1),
 lambda d:d["comparison"].__setitem__("whole_line_gap","[-1 +/- 0]"),lambda d:d["decision"].__setitem__("rademacher_strictly_above_candidate",False),
 lambda d:d["decision"].__setitem__("rare_atom_collar_follows_without_stability_bound",True),lambda d:d["decision"].__setitem__("global_optimizer_proved",True)]
caught=0
for i,mut in enumerate(mutations,1):
 d=copy.deepcopy(base);mut(d)
 try: ok=all(v for _,v in m.validate(d))
 except Exception: ok=False
 assert not ok,f"mutation {i} escaped";caught+=1;print(f"PASS {i:02d}: rejected mutation")
print(f"RESULT: PASS {caught}/{len(mutations)}")
