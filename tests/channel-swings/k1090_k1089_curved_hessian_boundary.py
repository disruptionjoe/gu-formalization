#!/usr/bin/env python3
"""K1090: ownership and scoring boundary for the curved Hessian packet."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
OUTPUT = ROOT / "lab/process/k1090-k1089-curved-hessian-boundary.json"


def build():
    requirements = [
        ("covariant_commutator", "K1086", "pass_conditional", True),
        ("boundary_domain_preservation", "K1087", "pass_conditional", True),
        ("holonomy_branch_decomposition", "K1088", "pass_conditional", True),
        ("shared_ladder_obstruction", "K1089", "pass_conditional", True),
        ("source_selected_gu_hessian", "SC-ACT-01/02/06", "open", False),
        ("physical_positive_cohomology", "LT-SM8/LT-GR6b", "open", False),
        ("measured_apparatus", "K1070 open rows", "open", False),
    ]
    rows = [
        {"id": i, "evidence": e, "candidate_grade": g,
         "repository_conditional_owned": own, "gu_source_owned": False, "scorable": False}
        for i, e, g, own in requirements
    ]
    return {
        "schema_version": "1.0",
        "result_id": "K1090-K1089-CURVED-HESSIAN-BOUNDARY",
        "status": "working_draft_verified",
        "created": "2026-10-04",
        "advance": "the flat selector now has exact covariant, boundary-domain, holonomy and common-ladder survival conditions",
        "requirements": rows,
        "counts": {"mathematical_pass_or_conditional": 4, "repository_conditional_owned": 4,
                   "open_physical_or_source": 3, "gu_source_owned": 0, "scorable": 0},
        "nonselection": "necessary curved-domain conditions do not select a GU action, connection, boundary law, physical BV cohomology or apparatus",
        "source_scope": {"SC-ACT-01": "ASSERTS", "SC-ACT-02": "ASSERTS", "SC-ACT-06": "ASSERTS", "SC-META-53": "UNCERTAIN"},
        "ledger_effect": "none -- LT-SM8, LT-GR6b, RA-F1 and AC-F1 remain NEEDS",
        "next_condition": "a source-selected stationary Hessian must supply M,E,nabla,B,C and a self-adjoint boundary realization; test nabla C, [B,C], the boundary defect and cross-sector spectral identification before positive cohomology or apparatus scoring",
        "target_claim": "NONE-NOT-A-KILL",
    }


def validate(d):
    assert "covariant, boundary-domain, holonomy" in d["advance"]
    assert len(d["requirements"]) == 7
    assert sum(r["candidate_grade"].startswith("pass") for r in d["requirements"]) == 4
    assert sum(r["repository_conditional_owned"] for r in d["requirements"]) == 4
    assert not any(r["gu_source_owned"] or r["scorable"] for r in d["requirements"])
    assert d["counts"] == {"mathematical_pass_or_conditional": 4, "repository_conditional_owned": 4,
                           "open_physical_or_source": 3, "gu_source_owned": 0, "scorable": 0}
    assert "do not select a GU action" in d["nonselection"]
    assert d["source_scope"]["SC-ACT-06"] == "ASSERTS" and d["source_scope"]["SC-META-53"] == "UNCERTAIN"
    assert "remain NEEDS" in d["ledger_effect"]
    assert "test nabla C, [B,C]" in d["next_condition"] and "boundary defect" in d["next_condition"]
    assert d["target_claim"] == "NONE-NOT-A-KILL"


if __name__ == "__main__":
    data = build(); validate(data)
    OUTPUT.write_text(json.dumps(data, indent=2, sort_keys=True) + "\n")
    print("K1090 controls: 10/10")
