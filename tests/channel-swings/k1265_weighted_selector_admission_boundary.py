#!/usr/bin/env python3
"""Integrated controls for K1265."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
DATA = json.loads((ROOT / "lab/process/k1265-weighted-selector-admission-boundary.json").read_text())
passed = 0

def check(name, condition):
    global passed
    assert condition, name
    passed += 1
    print(f"PASS {passed:02d}: {name}")

rows = DATA["certificate"]["rows"]
counts = {s: sum(r["state"] == s for r in rows) for s in ("satisfied","excluded","conditional","missing")}
check("result id", DATA["result_id"] == "K1265-WEIGHTED-SELECTOR-ADMISSION-BOUNDARY")
check("fourteen rows", len(rows) == 14)
check("four satisfied", counts["satisfied"] == DATA["certificate"]["satisfied_count"] == 4)
check("two excluded", counts["excluded"] == DATA["certificate"]["excluded_count"] == 2)
check("one conditional", counts["conditional"] == DATA["certificate"]["conditional_count"] == 1)
check("seven missing", counts["missing"] == DATA["certificate"]["missing_count"] == 7)
check("six shapes satisfied", any(r == {"row":"six continuous weighted-polynomial shape responses","state":"satisfied"} for r in rows))
check("odd source response missing", any(r == {"row":"source-derived odd-in-I7 response or physical sign identification","state":"missing"} for r in rows))
check("orbit image missing", any(r == {"row":"realized split-real orbit-image coverage","state":"missing"} for r in rows))
check("domain missing", any(r == {"row":"common closed functional domain","state":"missing"} for r in rows))
check("K1145 zero", DATA["certificate"]["k1145_pass_count"] == 0)
check("K1150 zero", DATA["certificate"]["k1150_pass_count"] == 0)
check("rank conflation rejected", DATA["decision"]["scalar_parameter_rank_conflation_rejected"] is True)
check("continuous lock exists", DATA["decision"]["finite_continuous_lock_exists_mathematically"] is True)
check("source ownership withheld", DATA["decision"]["finite_continuous_lock_is_source_owned"] is False)
check("sign unselected", DATA["decision"]["discrete_I7_sign_selected"] is False)
check("protected status unchanged", DATA["protected_status_effect"] == "none")
assert passed == 17
print("RESULT: PASS 17/17")
