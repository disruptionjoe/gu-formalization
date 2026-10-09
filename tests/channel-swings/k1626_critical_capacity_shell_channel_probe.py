#!/usr/bin/env python3
"""Hostile mutations for K1626's method-sharpness scope."""
import json
from copy import deepcopy
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]

def reject(d):
    q, z = d["shell_channel"], d["decision"]
    return (
        "method-sharpness witness" in q["scope_guard"]
        and z["critical_information_realized"]
        and z["leading_missing_fisher_realized"]
        and z["information_method_scale_sharp"]
        and not z["actual_coefficient_change_proved"]
        and not z["unrestricted_state_theorem"]
        and not z["protected_status_change"]
    )

def main():
    d = json.loads((ROOT / "lab/process/k1626-critical-capacity-shell-channel.json").read_text())
    checks = [("baseline", reject(d))]
    for label, key, value in [
        ("coefficient overclaim", "actual_coefficient_change_proved", True),
        ("unrestricted overclaim", "unrestricted_state_theorem", True),
        ("method loss", "information_method_scale_sharp", False),
        ("critical loss", "critical_information_realized", False),
        ("Fisher loss", "leading_missing_fisher_realized", False),
        ("protected mutation", "protected_status_change", True),
    ]:
        m = deepcopy(d); m["decision"][key] = value
        checks.append((label, not reject(m)))
    m = deepcopy(d); m["shell_channel"]["scope_guard"] = "coefficient changes"
    checks.append(("scope deletion", not reject(m)))
    for i, (label, ok) in enumerate(checks, 1):
        assert ok, label; print(f"PASS {i:02d}: {label}")
    print(f"RESULT: PASS {len(checks)}/{len(checks)}")

if __name__ == "__main__": main()
