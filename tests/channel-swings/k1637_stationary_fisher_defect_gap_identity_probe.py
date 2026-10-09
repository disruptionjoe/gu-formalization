#!/usr/bin/env python3
"""Hostile mutations for K1637's exact identity."""
import json
from copy import deepcopy
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


def accept(d):
    q, z = d["gap_identity"], d["decision"]
    return ("not by itself" in q["scope_guard"]
            and "Finite Fisher alone does not imply" in q["scope_guard"]
            and "The factor 1/4 multiplies only" in q["normalization"]
            and z["stationary_matching_gaussian"]
            and z["weighted_score_pythagoras_exact"]
            and z["full_gap_identity_exact"]
            and not z["wick_defect_nonnegative"]
            and not z["global_coercivity_proved"]
            and not z["unrestricted_coefficient_proved"]
            and not z["protected_status_change"])


def main():
    d = json.loads((ROOT / "lab/process/k1637-stationary-fisher-defect-gap-identity.json").read_text())
    checks = [("baseline", accept(d))]
    for label, key, value in [
        ("stationarity loss", "stationary_matching_gaussian", False),
        ("Pythagoras loss", "weighted_score_pythagoras_exact", False),
        ("identity loss", "full_gap_identity_exact", False),
        ("defect sign overclaim", "wick_defect_nonnegative", True),
        ("coercivity overclaim", "global_coercivity_proved", True),
        ("coefficient overclaim", "unrestricted_coefficient_proved", True),
        ("protected mutation", "protected_status_change", True),
    ]:
        m = deepcopy(d); m["decision"][key] = value
        checks.append((label, not accept(m)))
    m = deepcopy(d); m["gap_identity"]["normalization"] = "all terms have factor 1/4"
    checks.append(("normalization mutation", not accept(m)))
    m = deepcopy(d); m["gap_identity"]["scope_guard"] = "finite Fisher is enough; not by itself coercive"
    checks.append(("moment-domain deletion", not accept(m)))
    for i, (label, ok) in enumerate(checks, 1):
        assert ok, label
        print(f"PASS {i:02d}: {label}")
    print(f"RESULT: PASS {len(checks)}/{len(checks)}")


if __name__ == "__main__":
    main()
