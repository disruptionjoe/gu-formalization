#!/usr/bin/env python3
"""Hostile mutations for K1642's dependence threshold."""
import json
from copy import deepcopy
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


def accept(d):
    q, z = d["dependence_bound"], d["decision"]
    return ("<=K||u||_2^4" in q["directional_cumulant"]
            and "b_N sum_j lambda_j^2" in q["finite_bound"]
            and "O_(m,S)(N)" in q["profile_bound"]
            and "b_N=o(N^3)" in q["leading_threshold"]
            and "necessary rather than sufficient" in q["scope_guard"]
            and z["finite_block_bound_proved"]
            and z["three_dimensional_sum_order_N"]
            and z["submacroscopic_leading_defect_excluded"]
            and not z["macroscopic_dependence_sufficient"]
            and not z["unrestricted_defect_bound"]
            and not z["protected_status_change"])


def main():
    d = json.loads((ROOT / "lab/process/k1642-submacroscopic-dependence-bound.json").read_text())
    checks = [("baseline", accept(d))]
    for label, key, value in [
        ("finite bound loss", "finite_block_bound_proved", False),
        ("dimension count loss", "three_dimensional_sum_order_N", False),
        ("exclusion loss", "submacroscopic_leading_defect_excluded", False),
        ("sufficiency overclaim", "macroscopic_dependence_sufficient", True),
        ("unrestricted overclaim", "unrestricted_defect_bound", True),
        ("protected mutation", "protected_status_change", True),
    ]:
        m = deepcopy(d); m["decision"][key] = value
        checks.append((label, not accept(m)))
    for label, key, value in [
        ("cumulant premise deletion", "directional_cumulant", "unbounded cumulants"),
        ("profile premise deletion", "profile_bound", "arbitrary covariance"),
        ("scope deletion", "scope_guard", "macroscopic blocks construct descent"),
    ]:
        m = deepcopy(d); m["dependence_bound"][key] = value
        checks.append((label, not accept(m)))
    for i, (label, ok) in enumerate(checks, 1):
        assert ok, label
        print(f"PASS {i:02d}: {label}")
    print(f"RESULT: PASS {len(checks)}/{len(checks)}")


if __name__ == "__main__":
    main()
