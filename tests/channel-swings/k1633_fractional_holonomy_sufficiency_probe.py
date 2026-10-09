#!/usr/bin/env python3
"""Hostile mutations for K1633's fractional threshold and scope."""
import json
from copy import deepcopy
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


def reject(d):
    q, z = d["fractional_sufficiency"], d["decision"]
    return (
        "does not assert endpoint" in q["scope_guard"]
        and z["fractional_Hs_sufficient_for_holonomy_L1"]
        and z["threshold_requires_s_strictly_greater_than_half"]
        and not z["h1_necessary"]
        and not z["endpoint_half_proved"]
        and not z["source_owned_flow"]
        and not z["protected_status_change"]
    )


def main():
    d = json.loads((ROOT / "lab/process/k1633-fractional-holonomy-sufficiency.json").read_text())
    checks = [("baseline", reject(d))]
    for label, key, value in [
        ("lose sufficiency", "fractional_Hs_sufficient_for_holonomy_L1", False),
        ("lose threshold", "threshold_requires_s_strictly_greater_than_half", False),
        ("H1 necessity overclaim", "h1_necessary", True),
        ("endpoint overclaim", "endpoint_half_proved", True),
        ("source overclaim", "source_owned_flow", True),
        ("protected mutation", "protected_status_change", True),
    ]:
        m = deepcopy(d)
        m["decision"][key] = value
        checks.append((label, not reject(m)))
    m = deepcopy(d)
    m["fractional_sufficiency"]["scope_guard"] = "endpoint and flow proved"
    checks.append(("scope deletion", not reject(m)))
    for i, (label, ok) in enumerate(checks, 1):
        assert ok, label
        print(f"PASS {i:02d}: {label}")
    print(f"RESULT: PASS {len(checks)}/{len(checks)}")


if __name__ == "__main__":
    main()
