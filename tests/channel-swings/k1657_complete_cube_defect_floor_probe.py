#!/usr/bin/env python3
"""Hostile mutations for K1657."""
import copy
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


def valid(d):
    q, z = d.get("defect_floor", {}), d.get("decision", {})
    return all([
        d.get("claim_id") == "K1657",
        "unit-modulus coefficients" in q.get("pattern", ""),
        "(3/2)A_N^4I_(4,N)" in q.get("moments", ""),
        ">=-3A_N^4d_N^2" in q.get("floor", ""),
        "unequal magnitudes" in q.get("scope_guard", ""),
        z.get("universal_defect_floor_proved") is True,
        z.get("rudin_shapiro_sharpness_claimed") is False,
        z.get("unrestricted_defect_floor_proved") is False,
        z.get("protected_status_change") is False,
    ])


def main():
    source = json.loads((ROOT / "lab/process/k1657-complete-cube-defect-floor.json").read_text())
    assert valid(source)
    changes = [
        (("claim_id",), "K1647"),
        (("defect_floor", "pattern"), "arbitrary magnitudes"),
        (("defect_floor", "moments"), "wrong phase factor"),
        (("defect_floor", "floor"), "unbounded"),
        (("defect_floor", "scope_guard"), "all laws"),
        (("decision", "universal_defect_floor_proved"), False),
        (("decision", "rudin_shapiro_sharpness_claimed"), True),
        (("decision", "unrestricted_defect_floor_proved"), True),
        (("decision", "protected_status_change"), True),
    ]
    for i, (path, value) in enumerate(changes, 1):
        m = copy.deepcopy(source)
        cur = m
        for key in path[:-1]:
            cur = cur[key]
        cur[path[-1]] = value
        assert not valid(m), i
        print(f"REJECT {i:02d}: hostile mutation")
    print(f"RESULT: REJECTED {len(changes)}/{len(changes)}")


if __name__ == "__main__":
    main()
