#!/usr/bin/env python3
"""Exact controls for K1274's connected/outer symmetry fork."""
import itertools,json,math
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
DATA=json.loads((ROOT/"lab/process/k1274-connected-outer-symmetry-fork.json").read_text())
passed=0
def check(name,condition):
 global passed
 assert condition,name
 passed+=1; print(f"PASS {passed:02d}: {name}")

x=(1,2,3,4,5,6,7); px=math.prod(x)
even_signs=[s for s in itertools.product((-1,1),repeat=7) if math.prod(s)==1]
odd_signs=[s for s in itertools.product((-1,1),repeat=7) if math.prod(s)==-1]
check("result id",DATA["result_id"]=="K1274-CONNECTED-OUTER-SYMMETRY-FORK")
check("verified status",DATA["status"]=="working_draft_verified")
check("64 even sign patterns",len(even_signs)==64)
check("64 odd sign patterns",len(odd_signs)==64)
check("connected signs preserve p",all(math.prod(si*xi for si,xi in zip(s,x))==px for s in even_signs))
check("outer signs reverse p",all(math.prod(si*xi for si,xi in zip(s,x))==-px for s in odd_signs))
check("odd term connected invariant",DATA["symmetry_fork"]["connected_group"].startswith("W(D7) preserves p"))
check("outer involution reverses p",DATA["symmetry_fork"]["outer_involution"]=="sigma(p)=-p")
check("fixed odd term forbidden when outer gauged","forbidden" in DATA["symmetry_fork"]["outer_gauged_consequence"])
check("spurion must transform", "sigma(epsilon)=-epsilon" in DATA["symmetry_fork"]["spurion_option"])
check("connected D7 does not forbid",DATA["decision"]["connected_D7_forbids_odd_p_term"] is False)
check("outer gauging does not allow fixed scalar",DATA["decision"]["gauged_outer_parity_allows_fixed_scalar_odd_p_term"] is False)
check("spurion not owner free",DATA["decision"]["nonzero_spurion_is_owner_free"] is False)
check("source horn unchosen",DATA["decision"]["source_chooses_symmetry_horn"] is False)
check("claim status unchanged",DATA["decision"]["SC_ACT_06_proved_or_refuted"] is False)
assert passed==15
print("RESULT: PASS 15/15")
