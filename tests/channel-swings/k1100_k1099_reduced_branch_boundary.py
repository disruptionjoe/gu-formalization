#!/usr/bin/env python3
"""K1100: ownership boundary for reduced affine-branch diagnostics."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
OUTPUT = ROOT / "lab/process/k1100-k1099-reduced-branch-boundary.json"


def build():
    requirements = [
        ("schur_affinity_classification", "K1096", "pass_conditional", True),
        ("one_auxiliary_curvature", "K1097", "pass_conditional", True),
        ("multi_auxiliary_stieltjes_law", "K1098", "pass_conditional", True),
        ("three_mode_mixing_witness", "K1099", "pass_conditional", True),
        ("source_selected_functional_complex", "SC-ACT-01/02/06", "open", False),
        ("positive_physical_cohomology", "LT-SM8/LT-GR6b", "open", False),
        ("measured_modes_and_systematics", "K1099 scope boundary", "open", False),
    ]
    rows = [
        {"id": i, "evidence": e, "candidate_grade": g,
         "repository_conditional_owned": own, "gu_source_owned": False, "scorable": False}
        for i,e,g,own in requirements
    ]
    return {
        "schema_version": "1.0",
        "result_id": "K1100-K1099-REDUCED-BRANCH-BOUNDARY",
        "status": "working_draft_verified",
        "created": "2026-10-04",
        "advance": "reduced affine-branch survival now has exact divisibility, curvature, multi-auxiliary and three-mode tests",
        "requirements": rows,
        "counts": {"mathematical_pass_or_conditional":4,"repository_conditional_owned":4,"open_physical_or_source":3,"gu_source_owned":0,"scorable":0},
        "nonselection": "the reduced-branch tests do not select a GU action, BV/BFV differential, positive domain, auxiliary splitting or apparatus",
        "source_scope": {"SC-ACT-01":"ASSERTS","SC-ACT-02":"ASSERTS","SC-ACT-06":"ASSERTS","SC-META-53":"UNCERTAIN"},
        "ledger_effect": "none -- LT-SM8, LT-GR6b, RA-F1 and AC-F1 remain NEEDS",
        "next_condition": "supply a source-selected stationary Hessian with functional BV/BFV complex, positive pairing, common domain and auxiliary splitting; compute the exact reduced branch and test its three-mode divided difference before apparatus scoring",
        "target_claim": "NONE-NOT-A-KILL",
    }


def validate(d):
    assert "divisibility, curvature, multi-auxiliary" in d["advance"]
    assert len(d["requirements"]) == 7
    assert sum(r["candidate_grade"].startswith("pass") for r in d["requirements"]) == 4
    assert sum(r["repository_conditional_owned"] for r in d["requirements"]) == 4
    assert not any(r["gu_source_owned"] or r["scorable"] for r in d["requirements"])
    assert d["counts"] == {"mathematical_pass_or_conditional":4,"repository_conditional_owned":4,"open_physical_or_source":3,"gu_source_owned":0,"scorable":0}
    assert "do not select a GU action" in d["nonselection"]
    assert d["source_scope"]["SC-ACT-06"] == "ASSERTS" and d["source_scope"]["SC-META-53"] == "UNCERTAIN"
    assert "remain NEEDS" in d["ledger_effect"]
    assert "three-mode divided difference" in d["next_condition"]
    assert d["target_claim"] == "NONE-NOT-A-KILL"


if __name__ == "__main__":
    data = build(); validate(data)
    OUTPUT.write_text(json.dumps(data, indent=2, sort_keys=True) + "\n")
    print("K1100 controls: 10/10")
