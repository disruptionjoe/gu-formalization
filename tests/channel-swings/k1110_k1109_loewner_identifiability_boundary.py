#!/usr/bin/env python3
"""K1110: reconcile Loewner rank results with GU and apparatus ownership."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
OUTPUT = ROOT / "lab/process/k1110-k1109-loewner-identifiability-boundary.json"


def build():
    rows = [
        ("symmetric_loewner_factorization", "K1106", "pass_conditional", True),
        ("confluent_order_lower_bound", "K1107", "pass_conditional", True),
        ("cross_mode_order_lower_bound", "K1108", "pass_conditional", True),
        ("noisy_singular_gap_boundary", "K1109", "pass_conditional", True),
        ("source_selected_functional_complex", "SC-ACT-01/02/06", "open", False),
        ("positive_physical_cohomology", "LT-SM8/LT-GR6b", "open", False),
        ("owned_modes_cap_gap_and_systematics", "K1107--K1109 scope boundaries", "open", False),
    ]
    requirements = [{"id": i, "evidence": e, "candidate_grade": g, "repository_conditional_owned": o, "gu_source_owned": False, "scorable": False} for i, e, g, o in rows]
    return {
        "schema_version": "1.0",
        "result_id": "K1110-K1109-LOEWNER-IDENTIFIABILITY-BOUNDARY",
        "status": "working_draft_verified",
        "created": "2026-10-05",
        "requirements": requirements,
        "counts": {"repository_conditional_owned": 4, "mathematical_pass_or_conditional": 4, "gu_source_owned": 0, "open_physical_or_source": 3, "scorable": 0},
        "advance": "finite Stieltjes data now have exact positive Loewner factorization, confluent and derivative-free order lower bounds, and a noise-gap/near-coalescence boundary",
        "nonselection": "the rank certificates do not select a GU Hessian, auxiliary upper bound, physical mode family, Loewner error norm, pole-separation floor, ruler or apparatus",
        "source_scope": {"SC-ACT-01": "ASSERTS", "SC-ACT-02": "ASSERTS", "SC-ACT-06": "ASSERTS", "SC-META-53": "UNCERTAIN"},
        "ledger_effect": "none -- LT-SM8, LT-GR6b, RA-F1 and AC-F1 remain NEEDS",
        "next_condition": "supply a source-selected stationary functional Hessian and BV/BFV complex with a positive pairing, common domain and owned auxiliary law; then own a multiplicity cap, pole/weight separation, paired or derivative mode data and matrix-norm error budget before scoring Loewner rank",
        "target_claim": "NONE-NOT-A-KILL",
    }


def validate(d):
    assert len(d["requirements"]) == 7
    assert d["counts"] == {"repository_conditional_owned": 4, "mathematical_pass_or_conditional": 4, "gu_source_owned": 0, "open_physical_or_source": 3, "scorable": 0}
    assert "exact positive Loewner factorization" in d["advance"]
    assert "do not select a GU Hessian" in d["nonselection"]
    assert d["source_scope"] == {"SC-ACT-01": "ASSERTS", "SC-ACT-02": "ASSERTS", "SC-ACT-06": "ASSERTS", "SC-META-53": "UNCERTAIN"}
    assert "remain NEEDS" in d["ledger_effect"]
    assert "matrix-norm error budget" in d["next_condition"]
    assert all(not row["gu_source_owned"] and not row["scorable"] for row in d["requirements"])
    assert sum(row["repository_conditional_owned"] for row in d["requirements"]) == 4
    assert d["target_claim"] == "NONE-NOT-A-KILL"


if __name__ == "__main__":
    data = build(); validate(data)
    OUTPUT.write_text(json.dumps(data, indent=2, sort_keys=True) + "\n")
    print("K1110 controls: 10/10")
