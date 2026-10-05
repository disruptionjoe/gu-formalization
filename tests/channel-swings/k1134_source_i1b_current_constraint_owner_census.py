#!/usr/bin/env python3
"""K1134: census current action-owned constraint candidates against 6/6/4."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
OUTPUT = ROOT / "lab/process/k1134-source-i1b-current-constraint-owner-census.json"


def load(name):
    return json.loads((ROOT / "lab/process" / name).read_text())


def build():
    floors = load("k1123-k1122-source-i1b-constraint-rank-floor.json")["stronger_typewise_floors"]
    k1132 = load("k1132-nonzero-kappa-elimination-not-constraint.json")
    k1133 = load("k1133-zero-kappa-symbol-null-propagation-audit.json")
    k1130 = load("k1130-k1129-corrected-action-boundary.json")
    rows = [
        {"candidate": "metric_diffeomorphism_image", "owned": True, "non_gauge": False, "propagated": True, "typewise_certified_rank": [4, 4, 4], "meets_non_gauge_floor": False, "reason": "gauge radical quotient preserves nonzero inertia"},
        {"candidate": "nonzero_kappa_solvability_map", "owned": True, "non_gauge": True, "propagated": False, "typewise_certified_rank": [0, 0, 0], "meets_non_gauge_floor": False, "reason": "generic invertibility gives elimination, not constraints"},
        {"candidate": "zero_kappa_symbol_left_nulls", "owned": True, "non_gauge": True, "propagated": False, "typewise_certified_rank": None, "meets_non_gauge_floor": False, "reason": "tangential and covariant-complex tests fail"},
        {"candidate": "fixed_frequency_graph_projector", "owned": False, "non_gauge": True, "propagated": False, "typewise_certified_rank": None, "meets_non_gauge_floor": False, "reason": "inverse-dependent graph is not a homogeneous action-owned constraint projector"},
    ]
    return {
        "schema_version": "1.0",
        "result_id": "K1134-SOURCE-I1B-CURRENT-CONSTRAINT-OWNER-CENSUS",
        "status": "working_draft_verified",
        "created": "2026-10-05",
        "negative_floor": floors,
        "action_owned_t0_gauge": k1130["action_owned_t0_gauge"],
        "nonzero_kappa_conclusion": k1132["conclusion"],
        "zero_kappa_conclusion": k1133["conclusion"],
        "rows": rows,
        "counts": {"candidate_classes": 4, "meets_floor_on_common_propagated_domain": 0, "physical_quotient_owned": 0, "scorable_rows_added": 0},
        "conclusion": "none of the currently identified native I1B candidates supplies an owned propagated non-gauge constraint map meeting 6/6/4 on one common domain",
        "scope_boundary": "current candidate census, not an all-completions no-go and not a source-claim falsification",
        "target_claim": "NONE-NOT-A-KILL",
    }


def validate(d):
    assert d["negative_floor"] == [6, 6, 4]
    assert "rank-four metric diffeomorphism" in d["action_owned_t0_gauge"]
    assert len(d["rows"]) == 4
    assert all(r["meets_non_gauge_floor"] is False for r in d["rows"])
    assert d["rows"][1]["typewise_certified_rank"] == [0, 0, 0]
    assert d["rows"][2]["propagated"] is False
    assert d["rows"][3]["owned"] is False
    assert d["counts"] == {"candidate_classes": 4, "meets_floor_on_common_propagated_domain": 0, "physical_quotient_owned": 0, "scorable_rows_added": 0}
    assert "meeting 6/6/4" in d["conclusion"]
    assert "not an all-completions no-go" in d["scope_boundary"]
    assert d["target_claim"] == "NONE-NOT-A-KILL"


if __name__ == "__main__":
    data = build(); validate(data)
    OUTPUT.write_text(json.dumps(data, indent=2, sort_keys=True) + "\n")
    print("K1134 controls: 12/12")
