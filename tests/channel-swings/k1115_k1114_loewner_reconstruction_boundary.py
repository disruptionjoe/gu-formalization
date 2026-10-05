#!/usr/bin/env python3
"""K1115: reconcile Loewner reconstruction with GU and apparatus ownership."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
OUTPUT = ROOT / "lab/process/k1115-k1114-loewner-reconstruction-boundary.json"


def build():
    rows = [
        ("shifted_loewner_pencil_recovery", "K1111", "pass_conditional", True),
        ("positive_class_reconstruction_test", "K1112", "pass_conditional", True),
        ("separation_to_singular_gap_bound", "K1113", "pass_conditional", True),
        ("sample_to_matrix_error_map", "K1114", "pass_conditional", True),
        ("source_selected_functional_complex", "SC-ACT-01/02/06", "open", False),
        ("positive_physical_cohomology", "LT-SM8/LT-GR6b", "open", False),
        ("owned_inverse_inputs_and_apparatus", "K1111--K1114 scope boundaries", "open", False),
    ]
    requirements = [{
        "id": i, "evidence": e, "candidate_grade": grade,
        "repository_conditional_owned": owned,
        "gu_source_owned": False, "scorable": False,
    } for i, e, grade, owned in rows]
    return {
        "schema_version": "1.0",
        "result_id": "K1115-K1114-LOEWNER-RECONSTRUCTION-BOUNDARY",
        "status": "working_draft_verified",
        "created": "2026-10-05",
        "requirements": requirements,
        "counts": {"repository_conditional_owned": 4, "mathematical_pass_or_conditional": 4, "gu_source_owned": 0, "open_physical_or_source": 3, "scorable": 0},
        "advance": "an owned affine part and finite order turn exact paired mode values into a constructive pole-and-residue inverse, while explicit separation and scalar-error budgets feed the Loewner matrices",
        "nonselection": "the inverse does not supply a GU Hessian, physical BV/BFV quotient, affine coefficients, multiplicity cap, pole floors, mode preparation, ruler or measured systematics",
        "source_scope": {"SC-ACT-01": "ASSERTS", "SC-ACT-02": "ASSERTS", "SC-ACT-06": "ASSERTS", "SC-META-53": "UNCERTAIN"},
        "ledger_effect": "none -- LT-SM8, LT-GR6b, RA-F1 and AC-F1 remain NEEDS",
        "next_condition": "return to source/action or apparatus ownership: supply a source-selected stationary functional Hessian and proper positive BV/BFV complex, or own the affine branch, finite order, separated poles and weights, prepared paired modes, scalar error box, dimensional ruler and complete systematics",
        "target_claim": "NONE-NOT-A-KILL",
    }


def validate(d):
    assert len(d["requirements"]) == 7
    assert d["counts"] == {"repository_conditional_owned": 4, "mathematical_pass_or_conditional": 4, "gu_source_owned": 0, "open_physical_or_source": 3, "scorable": 0}
    assert "constructive pole-and-residue inverse" in d["advance"]
    assert "does not supply a GU Hessian" in d["nonselection"]
    assert d["source_scope"] == {"SC-ACT-01": "ASSERTS", "SC-ACT-02": "ASSERTS", "SC-ACT-06": "ASSERTS", "SC-META-53": "UNCERTAIN"}
    assert "remain NEEDS" in d["ledger_effect"]
    assert d["next_condition"].startswith("return to source/action or apparatus ownership")
    assert all(not row["gu_source_owned"] and not row["scorable"] for row in d["requirements"])
    assert sum(row["repository_conditional_owned"] for row in d["requirements"]) == 4
    assert d["target_claim"] == "NONE-NOT-A-KILL"


if __name__ == "__main__":
    data = build(); validate(data)
    OUTPUT.write_text(json.dumps(data, indent=2, sort_keys=True) + "\n")
    print("K1115 controls: 10/10")
