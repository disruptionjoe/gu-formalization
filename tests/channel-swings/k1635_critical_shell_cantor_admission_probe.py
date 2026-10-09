#!/usr/bin/env python3
"""Hostile mutations for K1635 protected integration."""
import json
from copy import deepcopy
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


def reject(d):
    c, p = d["census"], d["protected_boundaries"]
    return (
        c["rows"] == 350
        and c["satisfied"] + c["conditional"] + c["excluded"] + c["missing"] == 350
        and all(not value for value in p.values())
        and len(d["next_wakes"]) == 3
    )


def main():
    d = json.loads((ROOT / "lab/process/k1635-critical-shell-cantor-admission.json").read_text())
    checks = [("baseline", reject(d))]
    for key in d["protected_boundaries"]:
        m = deepcopy(d)
        m["protected_boundaries"][key] = True
        checks.append((f"reject {key}", not reject(m)))
    for label, key, delta in [
        ("row drift", "rows", 1),
        ("satisfied drift", "satisfied", 1),
        ("conditional drift", "conditional", 1),
        ("excluded drift", "excluded", 1),
        ("missing drift", "missing", 1),
    ]:
        m = deepcopy(d)
        m["census"][key] += delta
        checks.append((label, not reject(m)))
    m = deepcopy(d)
    m["next_wakes"] = m["next_wakes"][:2]
    checks.append(("wake loss", not reject(m)))
    for i, (label, ok) in enumerate(checks, 1):
        assert ok, label
        print(f"PASS {i:02d}: {label}")
    print(f"RESULT: PASS {len(checks)}/{len(checks)}")


if __name__ == "__main__":
    main()
