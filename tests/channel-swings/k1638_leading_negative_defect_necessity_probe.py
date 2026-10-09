#!/usr/bin/env python3
"""Hostile mutations for K1638's necessity-only result."""
import json
from copy import deepcopy
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


def accept(d):
    q, z = d["necessity"], d["decision"]
    return ("necessary rather than sufficient" in q["scope_guard"]
            and "Fix g>0 independently" in q["fixed_coupling"]
            and z["nonstationarity_independent_escape_closed"]
            and z["phase_independent_escape_closed"]
            and z["leading_negative_defect_necessary"]
            and not z["leading_negative_defect_sufficient"]
            and not z["realizing_family_constructed"]
            and not z["unrestricted_coefficient_proved"]
            and not z["protected_status_change"])


def main():
    d = json.loads((ROOT / "lab/process/k1638-leading-negative-defect-necessity.json").read_text())
    checks = [("baseline", accept(d))]
    for label, key, value in [
        ("stationarity loss", "nonstationarity_independent_escape_closed", False),
        ("phase loss", "phase_independent_escape_closed", False),
        ("necessity loss", "leading_negative_defect_necessary", False),
        ("sufficiency overclaim", "leading_negative_defect_sufficient", True),
        ("family overclaim", "realizing_family_constructed", True),
        ("coefficient overclaim", "unrestricted_coefficient_proved", True),
        ("protected mutation", "protected_status_change", True),
    ]:
        m = deepcopy(d); m["decision"][key] = value
        checks.append((label, not accept(m)))
    m = deepcopy(d); m["necessity"]["scope_guard"] = "sufficient construction"
    checks.append(("scope deletion", not accept(m)))
    m = deepcopy(d); m["necessity"]["fixed_coupling"] = "arbitrary coupling"
    checks.append(("coupling-premise deletion", not accept(m)))
    for i, (label, ok) in enumerate(checks, 1):
        assert ok, label
        print(f"PASS {i:02d}: {label}")
    print(f"RESULT: PASS {len(checks)}/{len(checks)}")


if __name__ == "__main__":
    main()
