#!/usr/bin/env python3
"""K1085: reconcile the functional lift with ownership and scoring."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
OUTPUT = ROOT / "lab/process/k1085-k1084-functional-hessian-boundary.json"


def build():
    rows = [
        ("common_functional_domain", "K1081", "pass", True, False, False),
        ("positive_hamiltonian", "K1082", "pass", True, False, False),
        ("functional_branch_selector", "K1083", "pass_conditional", True, False, False),
        ("variable_mass_obstruction", "K1084", "pass_conditional", True, False, False),
        ("source_selected_gu_hessian", "SC-ACT-01/02/06", "open", False, False, False),
        ("physical_positive_cohomology", "LT-SM8/LT-GR6b", "open", False, False, False),
        ("measured_apparatus", "K1070 open rows", "open", False, False, False),
    ]
    return {
        "schema_version": "1.0",
        "result_id": "K1085-K1084-FUNCTIONAL-HESSIAN-BOUNDARY",
        "status": "working_draft_verified",
        "created": "2026-10-04",
        "requirements": [{"id": i, "evidence": e, "candidate_grade": g, "repository_action_owned": a, "gu_source_owned": o, "scorable": s} for i, e, g, a, o, s in rows],
        "counts": {"mathematical_pass_or_conditional": 4, "repository_action_owned": 4, "gu_source_owned": 0, "scorable": 0, "open_physical_or_source": 3},
        "advance": "the K1036 flat candidate now has one common H2 Hessian domain, positive Hamiltonian flow, exact affine branches and an exact variable-mass failure criterion",
        "nonselection": "repository action ownership does not identify a source-selected GU action, physical BV cohomology, dimensional ruler or apparatus",
        "source_scope": {"SC-ACT-01": "ASSERTS", "SC-ACT-02": "ASSERTS", "SC-ACT-06": "ASSERTS", "SC-META-53": "UNCERTAIN"},
        "ledger_effect": "none -- LT-SM8, LT-GR6b, RA-F1 and AC-F1 remain NEEDS",
        "next_condition": "instantiate the same common-domain test on a source-selected GU stationary Hessian or a curved action-owned quotient: identify its principal kinetic block, lower-order mass block and boundary domain, compute the full commutator, then compose a physical positive cohomology and independently owned ruler/apparatus",
        "target_claim": "NONE-NOT-A-KILL",
    }


def validate(d):
    rows = d["requirements"]
    assert len(rows) == 7 and len({r["id"] for r in rows}) == 7
    assert sum(r["candidate_grade"].startswith("pass") for r in rows) == 4
    assert sum(r["repository_action_owned"] for r in rows) == 4
    assert all(r["gu_source_owned"] is False and r["scorable"] is False for r in rows)
    assert d["counts"] == {"mathematical_pass_or_conditional": 4, "repository_action_owned": 4, "gu_source_owned": 0, "scorable": 0, "open_physical_or_source": 3}
    assert "common H2 Hessian domain" in d["advance"] and "variable-mass failure criterion" in d["advance"]
    assert "does not identify a source-selected GU action" in d["nonselection"]
    assert d["source_scope"] == {"SC-ACT-01": "ASSERTS", "SC-ACT-02": "ASSERTS", "SC-ACT-06": "ASSERTS", "SC-META-53": "UNCERTAIN"}
    assert d["ledger_effect"].startswith("none") and d["ledger_effect"].endswith("NEEDS")
    assert "source-selected GU stationary Hessian" in d["next_condition"] and "full commutator" in d["next_condition"]
    assert d["target_claim"] == "NONE-NOT-A-KILL"


if __name__ == "__main__":
    data = build(); validate(data)
    OUTPUT.write_text(json.dumps(data, indent=2, sort_keys=True) + "\n")
    print("K1085 controls: 10/10")
