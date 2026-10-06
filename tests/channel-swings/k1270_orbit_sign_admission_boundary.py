#!/usr/bin/env python3
"""Integrated controls for K1270."""
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
DATA = json.loads((ROOT / "lab/process/k1270-orbit-sign-admission-boundary.json").read_text())
passed = 0

def check(name, condition):
    global passed
    assert condition, name
    passed += 1
    print(f"PASS {passed:02d}: {name}")

rows = DATA["certificate"]["rows"]
counts = {s: sum(r["state"] == s for r in rows) for s in ("satisfied","excluded","conditional","missing")}

check("result id", DATA["result_id"] == "K1270-ORBIT-SIGN-ADMISSION-BOUNDARY")
check("seventeen rows", len(rows) == 17)
check("six satisfied", counts["satisfied"] == DATA["certificate"]["satisfied_count"] == 6)
check("three excluded", counts["excluded"] == DATA["certificate"]["excluded_count"] == 3)
check("two conditional", counts["conditional"] == DATA["certificate"]["conditional_count"] == 2)
check("six missing", counts["missing"] == DATA["certificate"]["missing_count"] == 6)
check("realized pair satisfied", any(r == {"row":"opposite signs realized on regular split Cartan","state":"satisfied"} for r in rows))
check("connected identification excluded", any(r == {"row":"connected Spin77 identification of opposite signs","state":"excluded"} for r in rows))
check("disconnected parity conditional", any(r == {"row":"disconnected O77 parity exchange","state":"conditional"} for r in rows))
check("odd source response missing", any(r == {"row":"source-derived odd-in-I7 response or physical outer gauging","state":"missing"} for r in rows))
check("domain missing", any(r == {"row":"common closed functional domain","state":"missing"} for r in rows))
check("K1145 zero", DATA["certificate"]["k1145_pass_count"] == 0)
check("K1150 zero", DATA["certificate"]["k1150_pass_count"] == 0)
check("both signs realized", DATA["decision"]["both_signs_realized"] is True)
check("connected source identification rejected", DATA["decision"]["connected_source_gauge_identifies_pair"] is False)
check("disconnected mathematical identification retained", DATA["decision"]["disconnected_mathematical_extension_identifies_pair"] is True)
check("disconnected source ownership withheld", DATA["decision"]["disconnected_extension_is_source_owned"] is False)
check("odd action response withheld", DATA["decision"]["odd_action_response_owned"] is False)
check("source claim unchanged", DATA["decision"]["SC_ACT_06_proved_or_refuted"] is False)
check("protected status unchanged", DATA["protected_status_effect"] == "none")
assert passed == 20
print("RESULT: PASS 20/20")
