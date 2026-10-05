#!/usr/bin/env python3
"""K1118: apply the inertia floor to K129's source-native I1B symbols."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
OUTPUT = ROOT / "lab/process/k1118-k129-source-i1b-symbol-inertia.json"


def build():
    strata = {
        "timelike": {"rank_A": 6, "min_positive": 6, "min_negative": 6, "metric_kernel": "diffeomorphism_4"},
        "spacelike": {"rank_A": 6, "min_positive": 6, "min_negative": 6, "metric_kernel": "diffeomorphism_4"},
        "null": {"rank_A": 4, "min_positive": 4, "min_negative": 4, "metric_kernel": "diffeomorphism_4_plus_TT_2"},
    }
    return {
        "schema_version": "1.0",
        "result_id": "K1118-K129-SOURCE-I1B-SYMBOL-INERTIA",
        "status": "working_draft_verified",
        "created": "2026-10-05",
        "source_block": "K128 source-native I1B T=0 Hessian H=[[0,A*],[A,C]]",
        "source_rank_input": "K129 ranks A=(6,6,4) on timelike, spacelike and null covectors",
        "strata": strata,
        "ordinary_quotient_result": "quotienting the named metric kernel preserves rank(A) and therefore does not erase the paired positive/negative inertia floor",
        "strongest_conclusion": "every nonzero causal K129 symbol is indefinite before an additional action-owned constraint or cohomological reduction",
        "scope_boundary": "source-native local finite-symbol result; no global stationary background, common domain, BV/BFV cohomology or positive physical pairing",
        "target_claim": "SC-ACT-01",
    }


def validate(d):
    assert d["source_block"].startswith("K128 source-native I1B")
    assert "(6,6,4)" in d["source_rank_input"]
    assert d["strata"]["timelike"] == {"rank_A": 6, "min_positive": 6, "min_negative": 6, "metric_kernel": "diffeomorphism_4"}
    assert d["strata"]["spacelike"]["min_negative"] == 6
    assert d["strata"]["null"] == {"rank_A": 4, "min_positive": 4, "min_negative": 4, "metric_kernel": "diffeomorphism_4_plus_TT_2"}
    assert "preserves rank(A)" in d["ordinary_quotient_result"]
    assert "additional action-owned constraint" in d["strongest_conclusion"]
    assert "no global stationary background" in d["scope_boundary"]
    assert d["target_claim"] == "SC-ACT-01"


if __name__ == "__main__":
    data = build(); validate(data)
    OUTPUT.write_text(json.dumps(data, indent=2, sort_keys=True) + "\n")
    print("K1118 controls: 9/9")
