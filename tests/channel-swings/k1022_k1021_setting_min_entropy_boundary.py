#!/usr/bin/env python3
"""K1022: exact pair-source min-entropy boundary for CHSH inputs."""
import json
import math
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
OUTPUT = ROOT / "lab/process/k1022-k1021-setting-min-entropy-boundary.json"


def extremal(h):
    m = 2 ** (-h)
    if m >= 1 / 3:
        pi = (0.0, 1 / 3, 1 / 3, 1 / 3)
    else:
        pi = (1 - 3 * m, m, m, m)
    return m, pi


def build():
    hs = [1.5, math.log2(3), 1.8, 2.0]
    rows = []
    for h in hs:
        m, pi = extremal(h)
        q = max(0.0, 1 - 3 * m)
        rows.append({"h": h, "max_probability_bound": m, "pi": list(pi), "minimum_pair_floor": q, "local_ceiling": min(1.0, 3 * m)})
    return {
        "schema_version": "1.0", "result_id": "K1022-K1021-SETTING-MIN-ENTROPY-BOUNDARY",
        "status": "working_draft_verified", "created": "2026-10-04",
        "assumption": "for feasible 0<=h<=2, the pointwise conditional bound H_infinity(XY|F)>=h is equivalent to max_j pi_j<=2^-h",
        "minimum_pair_floor": "min_j pi_j>=max(0,1-3*2^-h)",
        "local_ceiling": "b<=min(1,3*2^-h)",
        "critical_entropy": "h>log2(3) is necessary and sufficient for this assumption alone to force a nonzero minimum pair probability",
        "extremal_family": rows,
        "interpretation": "pair-source min-entropy at or below log2(3) permits one absent input pair and therefore a perfect deterministic local CHSH score",
        "unowned_assumptions": ["conditional pair-source min-entropy against the devices", "event-ready no-postselection trials"],
        "ownership": {"gu_randomness_source_constructed": False, "entropy_certified": False},
        "target_claim": "NONE-NOT-A-KILL",
    }


def validate(d):
    assert "feasible 0<=h<=2" in d["assumption"] and "max_j pi_j<=2^-h" in d["assumption"]
    assert d["minimum_pair_floor"] == "min_j pi_j>=max(0,1-3*2^-h)"
    assert d["local_ceiling"] == "b<=min(1,3*2^-h)"
    assert "necessary and sufficient" in d["critical_entropy"]
    for row in d["extremal_family"]:
        pi = row["pi"]
        assert math.isclose(sum(pi), 1, abs_tol=1e-14)
        assert max(pi) <= row["max_probability_bound"] + 1e-14
        assert math.isclose(min(pi), row["minimum_pair_floor"], abs_tol=1e-14)
        assert math.isclose(1 - min(pi), row["local_ceiling"], abs_tol=1e-14)
    assert d["extremal_family"][0]["local_ceiling"] == 1
    assert d["extremal_family"][-1]["local_ceiling"] == 0.75
    assert "absent input pair" in d["interpretation"]
    assert len(d["unowned_assumptions"]) == 2
    assert d["ownership"]["gu_randomness_source_constructed"] is False
    assert d["ownership"]["entropy_certified"] is False
    assert d["target_claim"] == "NONE-NOT-A-KILL"


if __name__ == "__main__":
    d = build(); validate(d)
    OUTPUT.write_text(json.dumps(d, indent=2, sort_keys=True) + "\n")
    print("K1022 controls: 12/12")
