#!/usr/bin/env python3
"""Hostile mutations for K1651."""
import copy
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


def valid(d):
    q, z = d.get("individual_moment", {}), d.get("decision", {})
    return all([
        d.get("claim_id") == "K1651",
        "16d_n" in q.get("difference_identity", ""),
        "disjoint Fourier supports" in q.get("orthogonality", ""),
        "4/3-(1/3)(-1/2)^n" in q.get("closed_form", ""),
        "(-1/8)^r" in q.get("cubic_defect", ""),
        z.get("individual_fourth_moments_equal") is True,
        z.get("cubic_defect_coefficient_exact") is True,
        z.get("energy_descent_proved") is False,
        z.get("protected_status_change") is False,
    ])


def main():
    source = json.loads((ROOT / "lab/process/k1651-rudin-shapiro-individual-fourth-moment.json").read_text())
    assert valid(source)
    muts = []
    for path, value in [
        (("claim_id",), "K1646"),
        (("individual_moment", "difference_identity"), "wrong factor"),
        (("individual_moment", "orthogonality"), "overlapping"),
        (("individual_moment", "closed_form"), "3/2"),
        (("individual_moment", "cubic_defect"), "unknown"),
        (("decision", "individual_fourth_moments_equal"), False),
        (("decision", "cubic_defect_coefficient_exact"), False),
        (("decision", "energy_descent_proved"), True),
        (("decision", "protected_status_change"), True),
    ]:
        m = copy.deepcopy(source)
        cur = m
        for key in path[:-1]:
            cur = cur[key]
        cur[path[-1]] = value
        muts.append(m)
    for i, m in enumerate(muts, 1):
        assert not valid(m), i
        print(f"REJECT {i:02d}: hostile mutation")
    print(f"RESULT: REJECTED {len(muts)}/{len(muts)}")


if __name__ == "__main__":
    main()
