#!/usr/bin/env python3
"""Integrated controls for K1275."""
import hashlib,json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
DATA=json.loads((ROOT/"lab/process/k1275-odd-response-admission-boundary.json").read_text())
passed=0
def check(name,condition):
 global passed
 assert condition,name
 passed+=1; print(f"PASS {passed:02d}: {name}")
rows=DATA["certificate"]["rows"]
counts={s:sum(r["state"]==s for r in rows) for s in ("satisfied","excluded","conditional","missing")}
check("result id",DATA["result_id"]=="K1275-ODD-RESPONSE-ADMISSION-BOUNDARY")
check("twenty rows",len(rows)==20)
check("seven satisfied",counts["satisfied"]==DATA["certificate"]["satisfied_count"]==7)
check("four excluded",counts["excluded"]==DATA["certificate"]["excluded_count"]==4)
check("three conditional",counts["conditional"]==DATA["certificate"]["conditional_count"]==3)
check("six missing",counts["missing"]==DATA["certificate"]["missing_count"]==6)
for key,entry in DATA["pinned_inputs"].items():
 path=ROOT/entry["path"]
 check(f"{key} digest",hashlib.sha256(path.read_bytes()).hexdigest()==entry["sha256"])
check("global sign row satisfied",{"row":"nonzero odd tilt selects a unique global sign","state":"satisfied"} in rows)
check("infinitesimal basin claim excluded",{"row":"infinitesimal odd tilt removes metastable basin","state":"excluded"} in rows)
check("source odd response missing",{"row":"source-derived odd-in-p coefficient or owned sign restriction","state":"missing"} in rows)
check("domain missing",{"row":"common closed functional domain","state":"missing"} in rows)
check("K1145 zero",DATA["certificate"]["k1145_pass_count"]==0)
check("K1150 zero",DATA["certificate"]["k1150_pass_count"]==0)
check("single critical threshold retained",DATA["decision"]["single_critical_point_requires_strict_threshold"] is True)
check("uniform scale covariance retained",DATA["decision"]["uniform_response_requires_scale_covariance"] is True)
check("source ownership withheld",DATA["decision"]["source_odd_response_owned"] is False)
check("charged boundary default retained",DATA["decision"]["charged_boundary_symmetry_remains_honest_default"] is True)
check("protected status unchanged",DATA["protected_status_effect"]=="none")
assert passed==21
print("RESULT: PASS 21/21")
