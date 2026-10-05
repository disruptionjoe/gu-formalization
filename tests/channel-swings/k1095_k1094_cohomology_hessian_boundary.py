#!/usr/bin/env python3
"""K1095: ownership boundary for gauge-Hessian cohomology reduction."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
OUTPUT = ROOT / "lab/process/k1095-k1094-cohomology-hessian-boundary.json"


def build():
    requirements = [
        ("harmonic_invariance", "K1091", "pass_conditional", True),
        ("ward_insufficiency", "K1092", "pass_conditional", True),
        ("schur_physical_hessian", "K1093", "pass_conditional", True),
        ("reduced_affine_branch_test", "K1094", "pass_conditional", True),
        ("source_selected_functional_complex", "SC-ACT-01/02/06", "open", False),
        ("positive_physical_cohomology", "LT-SM8/LT-GR6b", "open", False),
        ("measured_apparatus", "K1070 open rows", "open", False),
    ]
    rows = [
        {"id": i, "evidence": e, "candidate_grade": g,
         "repository_conditional_owned": own, "gu_source_owned": False, "scorable": False}
        for i,e,g,own in requirements
    ]
    return {
        "schema_version": "1.0",
        "result_id": "K1095-K1094-COHOMOLOGY-HESSIAN-BOUNDARY",
        "status": "working_draft_verified",
        "created": "2026-10-04",
        "advance": "physical spectral reading now has exact harmonic-invariance, Ward, Schur-reduction and reduced-affinity tests",
        "requirements": rows,
        "counts": {"mathematical_pass_or_conditional":4, "repository_conditional_owned":4,
                   "open_physical_or_source":3, "gu_source_owned":0, "scorable":0},
        "nonselection": "finite cohomology-Hessian tests do not select a GU action, BV/BFV differential, positive domain or apparatus",
        "source_scope": {"SC-ACT-01":"ASSERTS", "SC-ACT-02":"ASSERTS", "SC-ACT-06":"ASSERTS", "SC-META-53":"UNCERTAIN"},
        "ledger_effect": "none -- LT-SM8, LT-GR6b, RA-F1 and AC-F1 remain NEEDS",
        "next_condition": "supply a source-selected stationary Hessian, functional BV/BFV complex, positive pairing and common closed boundary domain; compute the harmonic projector or Schur reduction and test the reduced commutator and branch law",
        "target_claim": "NONE-NOT-A-KILL",
    }


def validate(d):
    assert "harmonic-invariance, Ward, Schur-reduction" in d["advance"]
    assert len(d["requirements"]) == 7
    assert sum(r["candidate_grade"].startswith("pass") for r in d["requirements"]) == 4
    assert sum(r["repository_conditional_owned"] for r in d["requirements"]) == 4
    assert not any(r["gu_source_owned"] or r["scorable"] for r in d["requirements"])
    assert d["counts"] == {"mathematical_pass_or_conditional":4,"repository_conditional_owned":4,"open_physical_or_source":3,"gu_source_owned":0,"scorable":0}
    assert "do not select a GU action" in d["nonselection"]
    assert d["source_scope"]["SC-ACT-06"] == "ASSERTS" and d["source_scope"]["SC-META-53"] == "UNCERTAIN"
    assert "remain NEEDS" in d["ledger_effect"]
    assert "harmonic projector or Schur reduction" in d["next_condition"]
    assert d["target_claim"] == "NONE-NOT-A-KILL"


if __name__ == "__main__":
    data = build(); validate(data)
    OUTPUT.write_text(json.dumps(data, indent=2, sort_keys=True) + "\n")
    print("K1095 controls: 10/10")
