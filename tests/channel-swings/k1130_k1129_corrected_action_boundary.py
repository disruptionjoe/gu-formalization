#!/usr/bin/env python3
"""K1130: freeze the corrected source-action boundary after K1126--K1129."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
OUTPUT = ROOT / "lab/process/k1130-k1129-corrected-action-boundary.json"


def build():
    inputs = {}
    for n, name in [(1126, "k1126-k895-first-order-formal-adjoint-correction.json"),
                    (1127, "k1127-k887-t0-gauge-carrier-correction.json"),
                    (1128, "k1128-k896-projector-commutator-audit.json"),
                    (1129, "k1129-k887-k940-consumer-survival-audit.json")]:
        inputs[f"K{n}"] = json.loads((ROOT / "lab/process" / name).read_text())["result_id"]
    return {
        "schema_version": "1.0",
        "result_id": "K1130-K1129-CORRECTED-ACTION-BOUNDARY",
        "status": "working_draft_verified",
        "created": "2026-10-05",
        "inputs": inputs,
        "exact_corrections": 2,
        "first_order_principal_coefficient_status": "skew coefficient has the correct formal self-adjoint parity; complete Hessian and domain remain open",
        "formal_projector_status": "restores the auxiliary radial-slice descent equation but fails first-order principal integrability at commutator rank 16382 and has no action owner",
        "action_owned_t0_gauge": "rank-four metric diffeomorphism image only; no independent distortion d-chi column",
        "negative_sector_floor": [6, 6, 4],
        "action_owned_non_gauge_constraint_map_present": False,
        "physical_quotient_present": False,
        "scorable_rows_added": 0,
        "retired_frontier": "the K887-K925 radial old-quotient completion gate is not a current source-action gate",
        "next_condition": "derive source-action constraint/KT/BFV maps on the native (g,T) carrier with propagation on one common closed domain and a positive pairing on nonzero cohomology; alternate source advances remain the actual boundary coupling or a stationary global background",
        "protected_disposition": "SC-ACT-01/02/06 remain ASSERTS; SC-META-53 remains UNCERTAIN; LT-SM8, LT-GR6b, RA-F1 and AC-F1 remain NEEDS",
        "scope_boundary": "correction and ownership boundary only; no source validation, physical positivity, prediction, confirmation, canon or public move",
    }


def validate(d):
    assert list(d["inputs"]) == ["K1126", "K1127", "K1128", "K1129"]
    assert d["exact_corrections"] == 2
    assert "correct formal self-adjoint parity" in d["first_order_principal_coefficient_status"]
    assert "commutator rank 16382" in d["formal_projector_status"]
    assert "rank-four metric diffeomorphism" in d["action_owned_t0_gauge"]
    assert d["negative_sector_floor"] == [6, 6, 4]
    assert d["action_owned_non_gauge_constraint_map_present"] is False
    assert d["physical_quotient_present"] is False
    assert d["scorable_rows_added"] == 0
    assert "not a current source-action gate" in d["retired_frontier"]
    assert "native (g,T) carrier" in d["next_condition"]
    assert "remain ASSERTS" in d["protected_disposition"]
    assert "remains UNCERTAIN" in d["protected_disposition"]
    assert "remain NEEDS" in d["protected_disposition"]
    assert "no source validation" in d["scope_boundary"]


if __name__ == "__main__":
    data = build(); validate(data)
    OUTPUT.write_text(json.dumps(data, indent=2, sort_keys=True) + "\n")
    print("K1130 controls: 15/15")
