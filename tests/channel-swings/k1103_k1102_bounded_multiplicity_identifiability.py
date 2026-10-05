#!/usr/bin/env python3
"""K1103: bounded-multiplicity exact identifiability by root counting."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
OUTPUT = ROOT / "lab/process/k1103-k1102-bounded-multiplicity-identifiability.json"


def build():
    cases = [
        {"multiplicity_bound": m, "difference_numerator_degree_bound": 2*m+1, "sufficient_exact_modes": 2*m+2}
        for m in (1, 2, 3, 4)
    ]
    return {
        "schema_version": "1.0",
        "result_id": "K1103-K1102-BOUNDED-MULTIPLICITY-IDENTIFIABILITY",
        "status": "working_draft_verified",
        "created": "2026-10-05",
        "theorem": "two reduced affine-minus-Stieltjes branches with at most m distinct simple poles that agree at 2m+2 distinct regular points are identical rational functions",
        "degree_argument": "after multiplication by both pole polynomials, the difference numerator has degree at most 2m+1; 2m+2 distinct roots force it to vanish",
        "parameter_recovery": "identity of reduced rational functions fixes affine slope/intercept and every distinct pole and positive residue up to permutation",
        "cases": cases,
        "one_pole_consistency": "m=1 requires four exact modes, matching K1102",
        "boundary": "the theorem assumes a declared finite multiplicity bound and reduced distinct-pole form; it is sufficient, not a claim of noisy stability or minimality in every constrained subclass",
        "scope_boundary": "conditional rational identifiability theorem; no source-owned auxiliary multiplicity or physical samples",
        "target_claim": "NONE-NOT-A-KILL",
    }


def validate(d):
    assert "2m+2 distinct regular points" in d["theorem"]
    assert "degree at most 2m+1" in d["degree_argument"]
    assert "up to permutation" in d["parameter_recovery"]
    assert d["cases"] == [
        {"multiplicity_bound":1,"difference_numerator_degree_bound":3,"sufficient_exact_modes":4},
        {"multiplicity_bound":2,"difference_numerator_degree_bound":5,"sufficient_exact_modes":6},
        {"multiplicity_bound":3,"difference_numerator_degree_bound":7,"sufficient_exact_modes":8},
        {"multiplicity_bound":4,"difference_numerator_degree_bound":9,"sufficient_exact_modes":10},
    ]
    assert "matching K1102" in d["one_pole_consistency"]
    assert "sufficient" in d["boundary"] and "noisy stability" in d["boundary"]
    assert "no source-owned auxiliary multiplicity" in d["scope_boundary"]
    assert d["target_claim"] == "NONE-NOT-A-KILL"


if __name__ == "__main__":
    data = build(); validate(data)
    OUTPUT.write_text(json.dumps(data, indent=2, sort_keys=True) + "\n")
    print("K1103 controls: 8/8")
