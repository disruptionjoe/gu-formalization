#!/usr/bin/env python3
"""Hostile mutations for K1631's all-term identity scope."""
import json
from copy import deepcopy
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


def reject(d):
    q, z = d["all_term_identity"], d["decision"]
    return (
        "stationary diagonal Gaussian" in q["scope_guard"]
        and z["full_free_plus_wick_balance_computed"]
        and not z["missing_fisher_alone_used_as_energy_verdict"]
        and z["stationary_diagonal_scope_only"]
        and not z["unrestricted_coefficient_proved"]
        and not z["protected_status_change"]
    )


def main():
    d = json.loads((ROOT / "lab/process/k1631-critical-shell-all-term-identity.json").read_text())
    checks = [("baseline", reject(d))]
    for label, key, value in [
        ("drop all-term", "full_free_plus_wick_balance_computed", False),
        ("Fisher-only verdict", "missing_fisher_alone_used_as_energy_verdict", True),
        ("drop scope", "stationary_diagonal_scope_only", False),
        ("unrestricted overclaim", "unrestricted_coefficient_proved", True),
        ("protected mutation", "protected_status_change", True),
    ]:
        m = deepcopy(d)
        m["decision"][key] = value
        checks.append((label, not reject(m)))
    m = deepcopy(d)
    m["all_term_identity"]["scope_guard"] = "unrestricted theorem"
    checks.append(("scope deletion", not reject(m)))
    for i, (label, ok) in enumerate(checks, 1):
        assert ok, label
        print(f"PASS {i:02d}: {label}")
    print(f"RESULT: PASS {len(checks)}/{len(checks)}")


if __name__ == "__main__":
    main()
