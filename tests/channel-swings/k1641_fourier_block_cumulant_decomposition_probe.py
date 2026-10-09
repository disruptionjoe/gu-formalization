#!/usr/bin/env python3
"""Hostile mutations for K1641's block-cumulant identity."""
import json
from copy import deepcopy
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


def accept(d):
    q, z = d["block_decomposition"], d["decision"]
    return ("independent" in q["field"] and "centrally symmetric" in q["field"]
            and "mu3(x)=0" in q["third_moment"]
            and "sum_B kappa4" in q["pointwise_identity"]
            and "explicit class premise" in q["scope_guard"]
            and z["block_cumulant_identity_exact"]
            and z["third_moment_vanishes_under_central_symmetry"]
            and not z["defect_sign_fixed"]
            and not z["arbitrary_stationary_laws_covered"]
            and not z["protected_status_change"])


def main():
    d = json.loads((ROOT / "lab/process/k1641-fourier-block-cumulant-decomposition.json").read_text())
    checks = [("baseline", accept(d))]
    for label, key, value in [
        ("identity loss", "block_cumulant_identity_exact", False),
        ("symmetry loss", "third_moment_vanishes_under_central_symmetry", False),
        ("sign overclaim", "defect_sign_fixed", True),
        ("scope overclaim", "arbitrary_stationary_laws_covered", True),
        ("protected mutation", "protected_status_change", True),
    ]:
        m = deepcopy(d); m["decision"][key] = value
        checks.append((label, not accept(m)))
    m = deepcopy(d); m["block_decomposition"]["field"] = "dependent asymmetric coordinates"
    checks.append(("premise deletion", not accept(m)))
    m = deepcopy(d); m["block_decomposition"]["scope_guard"] = "all stationary laws"
    checks.append(("stationarity fence deletion", not accept(m)))
    for i, (label, ok) in enumerate(checks, 1):
        assert ok, label
        print(f"PASS {i:02d}: {label}")
    print(f"RESULT: PASS {len(checks)}/{len(checks)}")


if __name__ == "__main__":
    main()
