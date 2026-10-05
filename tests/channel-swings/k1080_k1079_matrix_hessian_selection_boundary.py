#!/usr/bin/env python3
"""K1080: reconcile matrix-Hessian mathematics with ownership and scoring."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
OUTPUT = ROOT / "lab/process/k1080-k1079-matrix-hessian-selection-boundary.json"


def build():
    rows = [
        ("matrix_action_hamiltonian", "K1076", "pass", False, False),
        ("simultaneous_normal_mode_criterion", "K1077", "pass", False, False),
        ("branch_selector", "K1078", "pass_conditional", False, False),
        ("two_mode_commutator_witness", "K1079", "pass_conditional", False, False),
        ("source_action_functional_hessian", "SC-ACT-01/02/06 and LT-SM8/LT-GR6b", "open", False, False),
        ("measured_apparatus", "K1070 open rows", "open", False, False),
    ]
    return {
        "schema_version": "1.0",
        "result_id": "K1080-K1079-MATRIX-HESSIAN-SELECTION-BOUNDARY",
        "status": "working_draft_verified",
        "created": "2026-10-04",
        "requirements": [{"id": i, "evidence": e, "candidate_grade": g, "gu_source_owned": o, "scorable": s} for i, e, g, o, s in rows],
        "counts": {"mathematical_pass_or_conditional": 4, "gu_source_owned": 0, "scorable": 0, "open_physical_or_source": 2},
        "selection_result": "a supplied positive matrix Hessian has affine branches in one fixed basis exactly on the commuting normalized horn; the noncommuting horn is detected by two spatial modes",
        "nonselection_result": "K1076-K1079 supply tests for an independently owned Hessian but do not supply the Hessian, domain, quotient or physical ruler",
        "source_scope": {"SC-ACT-01": "ASSERTS", "SC-ACT-02": "ASSERTS", "SC-ACT-06": "ASSERTS", "SC-META-53": "UNCERTAIN"},
        "ledger_effect": "none -- LT-SM8, LT-GR6b, RA-F1 and AC-F1 remain NEEDS",
        "next_condition": "obtain a source/action-owned positive functional Hessian on one native stationary quotient; extract its kinetic, gradient and mass blocks, test the two-mode commutator on a common domain, and only on the commuting horn read branch intercept-to-slope ratios before apparatus scoring",
        "target_claim": "NONE-NOT-A-KILL",
    }


def validate(d):
    rows = d["requirements"]
    assert len(rows) == 6 and len({r["id"] for r in rows}) == 6
    assert sum(r["candidate_grade"].startswith("pass") for r in rows) == 4
    assert all(r["gu_source_owned"] is False and r["scorable"] is False for r in rows)
    assert d["counts"] == {"mathematical_pass_or_conditional": 4, "gu_source_owned": 0, "scorable": 0, "open_physical_or_source": 2}
    assert "commuting normalized horn" in d["selection_result"] and "two spatial modes" in d["selection_result"]
    assert "do not supply the Hessian" in d["nonselection_result"]
    assert d["source_scope"] == {"SC-ACT-01": "ASSERTS", "SC-ACT-02": "ASSERTS", "SC-ACT-06": "ASSERTS", "SC-META-53": "UNCERTAIN"}
    assert d["ledger_effect"].startswith("none") and d["ledger_effect"].endswith("NEEDS")
    assert "source/action-owned positive functional Hessian" in d["next_condition"] and "common domain" in d["next_condition"]
    assert d["target_claim"] == "NONE-NOT-A-KILL"


if __name__ == "__main__":
    data = build(); validate(data)
    OUTPUT.write_text(json.dumps(data, indent=2, sort_keys=True) + "\n")
    print("K1080 controls: 9/9")
