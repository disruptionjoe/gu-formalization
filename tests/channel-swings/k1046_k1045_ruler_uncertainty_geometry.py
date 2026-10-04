#!/usr/bin/env python3
"""K1046: exact squared-ruler uncertainty geometry for the two mass horns."""
import json
from fractions import Fraction as F
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
OUTPUT = ROOT / "lab/process/k1046-k1045-ruler-uncertainty-geometry.json"


def q(mass2, ruler2):
    return (4 * ruler2 + mass2) / (ruler2 + mass2)


def build():
    delta = F(1, 10)
    lo, hi = F(1) - delta, F(1) + delta
    i1 = [q(F(1), lo), q(F(1), hi)]
    i4 = [q(F(4), lo), q(F(4), hi)]
    return {
        "schema_version": "1.0",
        "result_id": "K1046-K1045-RULER-UNCERTAINTY-GEOMETRY",
        "status": "working_draft_verified",
        "created": "2026-10-04",
        "model": "Q_m(r)=(4r+m)/(r+m), with r=s^2 in [1-delta,1+delta] and m in {1,4}",
        "monotonicity": "Q_m is strictly increasing in r and strictly decreasing in m for positive r,m",
        "intervals": {
            "mass1": ["(5-4*delta)/(2-delta)", "(5+4*delta)/(2+delta)"],
            "mass4": ["(8-4*delta)/(5-delta)", "(8+4*delta)/(5+delta)"],
        },
        "gap": "(9-15*delta)/((2-delta)*(5+delta))",
        "theorem": "the fixed-horn ratio ranges are disjoint exactly for 0<=delta<3/5; they touch at delta=3/5",
        "fixture": {
            "delta": "1/10",
            "mass1_interval": [str(x) for x in i1],
            "mass4_interval": [str(x) for x in i4],
            "gap": str(i1[0] - i4[1]),
        },
        "scope": "delta bounds the common squared-spatial-scale coordinate; it is not a physical ruler calibration",
        "target_claim": "NONE-NOT-A-KILL",
    }


def validate(d):
    assert d["model"].startswith("Q_m(r)=(4r+m)/(r+m)")
    assert "strictly increasing in r" in d["monotonicity"] and "decreasing in m" in d["monotonicity"]
    assert d["intervals"]["mass1"][0] == "(5-4*delta)/(2-delta)"
    assert d["intervals"]["mass4"][1] == "(8+4*delta)/(5+delta)"
    assert d["gap"] == "(9-15*delta)/((2-delta)*(5+delta))"
    assert "exactly for 0<=delta<3/5" in d["theorem"] and "touch at delta=3/5" in d["theorem"]
    assert d["fixture"]["delta"] == "1/10"
    assert [F(x) for x in d["fixture"]["mass1_interval"]] == [F(46, 19), F(18, 7)]
    assert [F(x) for x in d["fixture"]["mass4_interval"]] == [F(76, 49), F(28, 17)]
    assert F(d["fixture"]["gap"]) == F(250, 323)
    assert "not a physical ruler calibration" in d["scope"]
    assert d["target_claim"] == "NONE-NOT-A-KILL"


if __name__ == "__main__":
    data = build()
    validate(data)
    OUTPUT.write_text(json.dumps(data, indent=2, sort_keys=True) + "\n")
    print("K1046 controls: 12/12")
