#!/usr/bin/env python3
"""K1125: reconcile the exact reduction necessities with open owners."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
OUTPUT = ROOT / "lab/process/k1125-k1124-physical-reduction-ownership-boundary.json"


def build():
    requirements = [
        {"requirement": "radical_quotient_inertia", "state": "exact_general", "evidence": "K1121"},
        {"requirement": "nonnegative_constraint_codimension", "state": "exact_general", "evidence": "K1122"},
        {"requirement": "source_causal_constraint_floors", "state": "exact_finite_symbol", "evidence": "K1123"},
        {"requirement": "acyclic_positivity_control", "state": "exact_distinct_carrier_control", "evidence": "K1124/K590"},
        {"requirement": "action_owned_constraint_maps_and_propagation", "state": "open", "evidence": None},
        {"requirement": "common_closed_functional_domain", "state": "open", "evidence": None},
        {"requirement": "positive_pairing_on_nontrivial_physical_cohomology", "state": "open", "evidence": None},
    ]
    return {
        "schema_version": "1.0", "result_id": "K1125-K1124-PHYSICAL-REDUCTION-OWNERSHIP-BOUNDARY",
        "status": "working_draft_verified", "created": "2026-10-05",
        "requirements": requirements,
        "counts": {"exact_necessities": 4, "open_physical_owners": 3, "new_global_physical_owned": 0, "scorable": 0},
        "protected_disposition": "SC-ACT-01/02/06 remain ASSERTS; SC-META-53 remains UNCERTAIN; LT-SM8, LT-GR6b, RA-F1 and AC-F1 remain NEEDS",
        "next_condition": "construct the source-action constraint/KT/BFV maps on one common closed domain, prove constraint propagation and a nonnegative restriction of codimension at least 6/6/4, then exhibit a positive pairing on nonzero physical cohomology",
        "alternate_source_advances": ["actual source boundary coupling", "stationary global background"],
        "scope_boundary": "necessary source-local reduction budget only; no physical positivity, prediction, confirmation or empirical score follows",
        "target_claim": "NONE-NOT-A-KILL",
    }


def validate(d):
    assert len(d["requirements"]) == 7
    assert d["counts"] == {"exact_necessities": 4, "open_physical_owners": 3, "new_global_physical_owned": 0, "scorable": 0}
    assert "remain ASSERTS" in d["protected_disposition"]
    assert "remains UNCERTAIN" in d["protected_disposition"]
    assert "remain NEEDS" in d["protected_disposition"]
    assert "codimension at least 6/6/4" in d["next_condition"]
    assert d["alternate_source_advances"] == ["actual source boundary coupling", "stationary global background"]
    assert "no physical positivity" in d["scope_boundary"]
    assert d["target_claim"] == "NONE-NOT-A-KILL"


if __name__ == "__main__":
    data = build(); validate(data)
    OUTPUT.write_text(json.dumps(data, indent=2, sort_keys=True) + "\n")
    print("K1125 controls: 9/9")
