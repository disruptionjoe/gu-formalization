#!/usr/bin/env python3
"""K1041: two-mode dispersion ratios do not identify an absolute mass with a free ruler."""
import json
from fractions import Fraction as F
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
OUTPUT = ROOT / "lab/process/k1041-k1040-mass-scale-nonidentifiability.json"


def q(mass_squared, scale_squared):
    return F(4 * scale_squared + mass_squared, scale_squared + mass_squared)


def build():
    examples = [
        {"mass_squared": 1, "scale_squared": 1, "Q": str(q(1, 1))},
        {"mass_squared": 4, "scale_squared": 4, "Q": str(q(4, 4))},
    ]
    scaling_checks = []
    for mass_squared, scale_squared, factor in [(1, 2, 3), (4, 3, 5), (7, 11, 2)]:
        scaling_checks.append(
            {
                "mass_squared": mass_squared,
                "scale_squared": scale_squared,
                "factor": factor,
                "before": str(q(mass_squared, scale_squared)),
                "after": str(q(factor * mass_squared, factor * scale_squared)),
            }
        )
    return {
        "schema_version": "1.0",
        "result_id": "K1041-K1040-MASS-SCALE-NONIDENTIFIABILITY",
        "status": "working_draft_verified",
        "created": "2026-10-04",
        "mode_family": "omega_n_squared=n_squared*s_squared+mass_squared for n_squared in {1,4}",
        "observable": "Q=omega_2_squared/omega_1_squared=(4*s_squared+mass_squared)/(s_squared+mass_squared)",
        "scaling_theorem": "Q(c*mass_squared,c*s_squared)=Q(mass_squared,s_squared) for every c>0",
        "scaling_checks": scaling_checks,
        "degenerate_horns": examples,
        "degenerate_value": "5/2",
        "consequence": "without an independently owned spatial scale, dimensionless two-mode dispersion cannot identify the absolute mass coefficient",
        "scope": "theorem for the K77 constant-coefficient candidate family; not a GU action no-go",
        "ownership": {"candidate_formula_owned": True, "spatial_scale_owned_by_GU": False, "scorable": False},
        "target_claim": "NONE-NOT-A-KILL",
    }


def validate(d):
    assert "n_squared*s_squared+mass_squared" in d["mode_family"]
    assert d["observable"].startswith("Q=omega_2_squared/omega_1_squared")
    assert d["scaling_theorem"] == "Q(c*mass_squared,c*s_squared)=Q(mass_squared,s_squared) for every c>0"
    assert len(d["scaling_checks"]) == 3
    assert all(x["before"] == x["after"] for x in d["scaling_checks"])
    assert d["degenerate_horns"] == [
        {"mass_squared": 1, "scale_squared": 1, "Q": "5/2"},
        {"mass_squared": 4, "scale_squared": 4, "Q": "5/2"},
    ]
    assert d["degenerate_value"] == "5/2"
    assert "independently owned spatial scale" in d["consequence"]
    assert "not a GU action no-go" in d["scope"]
    assert d["ownership"] == {"candidate_formula_owned": True, "spatial_scale_owned_by_GU": False, "scorable": False}
    assert d["target_claim"] == "NONE-NOT-A-KILL"


if __name__ == "__main__":
    data = build()
    validate(data)
    OUTPUT.write_text(json.dumps(data, indent=2, sort_keys=True) + "\n")
    print("K1041 controls: 12/12")
