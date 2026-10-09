#!/usr/bin/env python3
"""Certificate for K1627's critical information-method boundary."""
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]

def sha(path): return hashlib.sha256(path.read_bytes()).hexdigest()

def main():
    d = json.loads((ROOT / "lab/process/k1627-critical-information-method-boundary.json").read_text())
    q, z = d["method_boundary"], d["decision"]
    pin = d["pinned_inputs"]["k1626"]
    checks = [
        ("claim", d["claim_id"] == "K1627"),
        ("pin", sha(ROOT / pin["path"]) == pin["sha256"]),
        ("critical remainder", "o(N^4)" in q["negative_result"]),
        ("new structure", "component coercivity" in q["required_new_structure"]),
        ("Gaussian output", "itself Gaussian" in q["variational_guard"]),
        ("profile preserved", "profiled stationary-diagonal" in q["variational_guard"]),
        ("classification", q["classification"] == "method-sharp but variationally undecided"),
        ("ground guard", "true ground energy" in q["scope_guard"]),
        ("scale sharp", z["subcritical_information_hypothesis_scale_sharp"]),
        ("no critical rigidity", not z["critical_rigidity_from_information_alone"]),
        ("no coefficient change", not z["actual_coefficient_change_proved"]),
        ("all-term analysis", z["direct_all_term_analysis_still_required"]),
        ("protected", not z["protected_status_change"]),
    ]
    for i,(label,ok) in enumerate(checks,1):
        assert ok,label; print(f"PASS {i:02d}: {label}")
    print(f"RESULT: PASS {len(checks)}/{len(checks)}")

if __name__ == "__main__": main()
