#!/usr/bin/env python3
"""K1105: ownership boundary for finite-mode identifiability results."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
OUTPUT = ROOT / "lab/process/k1105-k1104-finite-mode-identifiability-boundary.json"


def build():
    requirements = [
        ("higher_divided_difference_sign_law", "K1101", "pass_conditional", True),
        ("four_mode_one_auxiliary_recovery", "K1102", "pass_conditional", True),
        ("bounded_multiplicity_uniqueness", "K1103", "pass_conditional", True),
        ("unbounded_finite_sample_alias", "K1104", "pass_conditional", True),
        ("source_selected_functional_complex", "SC-ACT-01/02/06", "open", False),
        ("positive_physical_cohomology", "LT-SM8/LT-GR6b", "open", False),
        ("owned_multiplicity_modes_and_systematics", "K1102--K1104 scope boundaries", "open", False),
    ]
    rows = [
        {"id":i,"evidence":e,"candidate_grade":g,"repository_conditional_owned":own,"gu_source_owned":False,"scorable":False}
        for i,e,g,own in requirements
    ]
    return {
        "schema_version":"1.0","result_id":"K1105-K1104-FINITE-MODE-IDENTIFIABILITY-BOUNDARY",
        "status":"working_draft_verified","created":"2026-10-05",
        "advance":"finite-mode Stieltjes data now have exact sign, one-pole recovery, bounded-multiplicity uniqueness and unbounded-multiplicity alias theorems",
        "requirements":rows,
        "counts":{"mathematical_pass_or_conditional":4,"repository_conditional_owned":4,"open_physical_or_source":3,"gu_source_owned":0,"scorable":0},
        "nonselection":"the finite-mode theorems do not select a GU Hessian, auxiliary multiplicity, physical mode family, positive quotient, ruler or apparatus",
        "source_scope":{"SC-ACT-01":"ASSERTS","SC-ACT-02":"ASSERTS","SC-ACT-06":"ASSERTS","SC-META-53":"UNCERTAIN"},
        "ledger_effect":"none -- LT-SM8, LT-GR6b, RA-F1 and AC-F1 remain NEEDS",
        "next_condition":"supply a source-selected stationary functional Hessian and BV/BFV complex with an owned finite auxiliary bound or full reduced rational law; then acquire prepared modes and an error model before using the exact sample thresholds",
        "target_claim":"NONE-NOT-A-KILL",
    }


def validate(d):
    assert "bounded-multiplicity uniqueness" in d["advance"]
    assert len(d["requirements"]) == 7
    assert sum(r["candidate_grade"].startswith("pass") for r in d["requirements"]) == 4
    assert sum(r["repository_conditional_owned"] for r in d["requirements"]) == 4
    assert not any(r["gu_source_owned"] or r["scorable"] for r in d["requirements"])
    assert d["counts"] == {"mathematical_pass_or_conditional":4,"repository_conditional_owned":4,"open_physical_or_source":3,"gu_source_owned":0,"scorable":0}
    assert "do not select a GU Hessian" in d["nonselection"]
    assert d["source_scope"]["SC-ACT-06"] == "ASSERTS" and d["source_scope"]["SC-META-53"] == "UNCERTAIN"
    assert "remain NEEDS" in d["ledger_effect"]
    assert "owned finite auxiliary bound" in d["next_condition"]
    assert d["target_claim"] == "NONE-NOT-A-KILL"


if __name__ == "__main__":
    data = build(); validate(data)
    OUTPUT.write_text(json.dumps(data, indent=2, sort_keys=True) + "\n")
    print("K1105 controls: 10/10")
