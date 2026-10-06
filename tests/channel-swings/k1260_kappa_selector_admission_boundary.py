#!/usr/bin/env python3
"""Integrated controls for K1260."""
import json
from pathlib import Path
ROOT = Path(__file__).resolve().parents[2]
DATA = json.loads((ROOT / "lab/process/k1260-kappa-selector-admission-boundary.json").read_text())
passed=0
def check(name, condition):
    global passed
    assert condition, name
    passed += 1
    print(f"PASS {passed:02d}: {name}")

rows=DATA["certificate"]["rows"]
counts={s:sum(r["state"]==s for r in rows) for s in ("satisfied","excluded","conditional","missing")}
check("result id", DATA["result_id"] == "K1260-KAPPA-SELECTOR-ADMISSION-BOUNDARY")
check("twelve rows", len(rows)==12)
check("two satisfied", counts["satisfied"]==DATA["certificate"]["satisfied_count"]==2)
check("two excluded", counts["excluded"]==DATA["certificate"]["excluded_count"]==2)
check("one conditional", counts["conditional"]==DATA["certificate"]["conditional_count"]==1)
check("seven missing", counts["missing"]==DATA["certificate"]["missing_count"]==7)
check("six shape channels missing", any(r=={"row":"six independent shape channels","state":"missing"} for r in rows))
check("finite proper selector satisfied", any(r=={"row":"globally proper formal-base finite selector","state":"satisfied"} for r in rows))
check("source coupling missing", any(r=={"row":"source-owned charge-Casimir coupling","state":"missing"} for r in rows))
check("real orbit scope missing", any(r=={"row":"realized split-real orbit-image coverage","state":"missing"} for r in rows))
check("K1145 zero", DATA["certificate"]["k1145_pass_count"]==0)
check("K1150 zero", DATA["certificate"]["k1150_pass_count"]==0)
check("Casimir-only lock rejected", DATA["decision"]["kappa_casimir_only_regular_lock_exists"] is False)
check("finite selector exists", DATA["decision"]["finite_global_selector_exists_mathematically"] is True)
check("charged boundary symmetry retained", DATA["decision"]["charged_boundary_symmetry_remains_honest_default"] is True)
check("protected status unchanged", DATA["protected_status_effect"]=="none")
assert passed==16
print("RESULT: PASS 16/16")
