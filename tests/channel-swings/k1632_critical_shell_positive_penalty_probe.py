#!/usr/bin/env python3
"""Hostile mutations for K1632's positive-penalty conclusion."""
import json
from copy import deepcopy
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


def reject(d):
    q, z = d["positive_penalty"], d["decision"]
    return (
        "Jordan-measurable" in q["shell"]
        and "boundary measure zero" in q["shell"]
        and "Boundary-null Jordan measurability" in q["full_energy"]
        and
        "does not classify arbitrary" in q["scope_guard"]
        and z["critical_information_retained"]
        and z["leading_missing_fisher_retained"]
        and z["strict_positive_full_energy_penalty"]
        and not z["critical_channel_lowers_profiled_coefficient"]
        and not z["unrestricted_coefficient_proved"]
        and not z["protected_status_change"]
    )


def main():
    d = json.loads((ROOT / "lab/process/k1632-critical-shell-positive-penalty.json").read_text())
    checks = [("baseline", reject(d))]
    for label, key, value in [
        ("lose information", "critical_information_retained", False),
        ("lose Fisher", "leading_missing_fisher_retained", False),
        ("lose penalty", "strict_positive_full_energy_penalty", False),
        ("lowering overclaim", "critical_channel_lowers_profiled_coefficient", True),
        ("unrestricted overclaim", "unrestricted_coefficient_proved", True),
        ("protected mutation", "protected_status_change", True),
    ]:
        m = deepcopy(d)
        m["decision"][key] = value
        checks.append((label, not reject(m)))
    m = deepcopy(d)
    m["positive_penalty"]["scope_guard"] = "all channels"
    checks.append(("scope deletion", not reject(m)))
    m = deepcopy(d)
    m["positive_penalty"]["shell"] = "Choose an arbitrary measurable shell."
    checks.append(("Riemann premise deletion", not reject(m)))
    for i, (label, ok) in enumerate(checks, 1):
        assert ok, label
        print(f"PASS {i:02d}: {label}")
    print(f"RESULT: PASS {len(checks)}/{len(checks)}")


if __name__ == "__main__":
    main()
