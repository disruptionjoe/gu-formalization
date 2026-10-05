#!/usr/bin/env python3
"""K1135: freeze the constructive constraint frontier after the current census."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
OUTPUT = ROOT / "lab/process/k1135-k1134-constraint-frontier-boundary.json"


def build():
    census = json.loads((ROOT / "lab/process/k1134-source-i1b-current-constraint-owner-census.json").read_text())
    requirements = [
        {"requirement": "action_derived_non_gauge_constraint_map", "state": "open", "acceptance": "typewise symbol ranks at least 6/6/4"},
        {"requirement": "constraint_propagation", "state": "open", "acceptance": "intertwining or closed evolution on the same native carrier"},
        {"requirement": "common_closed_domain", "state": "open", "acceptance": "one domain for H, constraints, adjoints and boundary traces"},
        {"requirement": "nonnegative_restriction", "state": "open", "acceptance": "exact inertia after restriction and residual-radical quotient"},
        {"requirement": "nonzero_physical_cohomology_positive_pairing", "state": "open", "acceptance": "positive pairing on at least one nonzero class"},
    ]
    return {
        "schema_version": "1.0",
        "result_id": "K1135-K1134-CONSTRAINT-FRONTIER-BOUNDARY",
        "status": "working_draft_verified",
        "created": "2026-10-05",
        "census_input": census["result_id"],
        "current_candidates_meeting_complete_gate": census["counts"]["meets_floor_on_common_propagated_domain"],
        "requirements": requirements,
        "reopeners": ["new source-action constraint/KT map", "actual source boundary coupling", "stationary global background", "different source-owned differential or completed coefficient"],
        "protected_disposition": "SC-ACT-01/02/06 remain ASSERTS; SC-META-53 remains UNCERTAIN; LT-SM8, LT-GR6b, RA-F1 and AC-F1 remain NEEDS",
        "scorable_rows_added": 0,
        "next_condition": "construct one action-derived non-gauge map with typewise ranks at least 6/6/4, prove propagation and a common closed domain, then compute restricted inertia and positive pairing on nonzero cohomology",
        "scope_boundary": "constructive ownership boundary only; no GU falsification, physical quotient, prediction, confirmation, canon or public move",
        "target_claim": "NONE-NOT-A-KILL",
    }


def validate(d):
    assert d["current_candidates_meeting_complete_gate"] == 0
    assert len(d["requirements"]) == 5 and all(r["state"] == "open" for r in d["requirements"])
    assert "6/6/4" in d["requirements"][0]["acceptance"]
    assert len(d["reopeners"]) == 4
    assert "remain ASSERTS" in d["protected_disposition"]
    assert "remains UNCERTAIN" in d["protected_disposition"]
    assert "remain NEEDS" in d["protected_disposition"]
    assert d["scorable_rows_added"] == 0
    assert "nonzero cohomology" in d["next_condition"]
    assert "no GU falsification" in d["scope_boundary"]
    assert d["target_claim"] == "NONE-NOT-A-KILL"


if __name__ == "__main__":
    data = build(); validate(data)
    OUTPUT.write_text(json.dumps(data, indent=2, sort_keys=True) + "\n")
    print("K1135 controls: 12/12")
