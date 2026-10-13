#!/usr/bin/env python3
"""Hostile mutations for K1760's protected admission."""
import copy,importlib.util,json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];P=ROOT/"tests/channel-swings/k1760_two_radius_collar_admission.py"
s=importlib.util.spec_from_file_location("m",P);m=importlib.util.module_from_spec(s);s.loader.exec_module(m);base=json.loads(m.ARTIFACT.read_text())
mutations=[lambda d:d.__setitem__("inputs",[]),lambda d:d["residual_domain"].__setitem__("rectangle","open/unbounded"),
 lambda d:d["bridge_census"].__setitem__("total",1),lambda d:d["decision"].__setitem__("joint_rare_zero_corner_completed",False),
 lambda d:d["decision"].__setitem__("compact_core_branch_and_bound_completed",True),lambda d:d["decision"].__setitem__("stationarity_or_uniqueness_proved",True),
 lambda d:d["decision"].__setitem__("global_optimizer_proved",True),lambda d:d["decision"].__setitem__("source_ledger_canon_paper_prediction_confirmation_or_public_status_changed",True)]
caught=0
for i,mut in enumerate(mutations,1):
 d=copy.deepcopy(base);mut(d);ok=all(v for _,v in m.validate(d));assert not ok,f"mutation {i} escaped";caught+=1;print(f"PASS {i:02d}: rejected mutation")
print(f"RESULT: PASS {caught}/{len(mutations)}")
