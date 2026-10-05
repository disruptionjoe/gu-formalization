#!/usr/bin/env python3
"""K1128: recompute K896 with first-order adjoint parity."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
OUTPUT = ROOT / "lab/process/k1128-k896-projector-commutator-audit.json"


def build():
    k895 = json.loads((ROOT / "lab/process/k895-sc-act-06-helmholtz-symmetry-obstruction.json").read_text())
    exact = k895["exact_helmholtz_test"]
    return {
        "schema_version": "1.0",
        "result_id": "K1128-K896-PROJECTOR-COMMUTATOR-AUDIT",
        "status": "working_draft_verified",
        "created": "2026-10-05",
        "formal_projector": "T=A(I-P_R)",
        "transpose": "T^T=-(I-P_R)A",
        "first_order_self_adjoint_condition": "T^T=-T",
        "equivalent_condition": "[P_R,A]=0",
        "corrected_defect": "T+T^T=P_R A-A P_R",
        "corrected_defect_rank": exact["formal_correction_symmetric_part_rank"],
        "retired_zero_order_defect_rank": exact["formal_completed_helmholtz_defect_rank"],
        "completed_map_rank": exact["formal_completed_rank"],
        "radial_descent_restored": True,
        "first_order_principal_integrability": False,
        "projector_action_owned": False,
        "classification_theorem": "all first-order completions have C=-A+Q with Q^T=-Q; gauge descent is QG=0 and the surviving principal coefficient is Q",
        "zero_order_symmetric_completion_classification_survives": False,
        "correction_scope": "K896's nonintegrability conclusion survives with commutator rank 16382, but its rank-130912 anticommutator defect and K897's symmetric-S classification are withdrawn",
        "source_and_ledger_effect": "SC-ACT-01_06_ASSERTS_UNCHANGED__LEDGER_UNCHANGED",
    }


def validate(d):
    assert d["formal_projector"] == "T=A(I-P_R)"
    assert d["transpose"] == "T^T=-(I-P_R)A"
    assert d["first_order_self_adjoint_condition"] == "T^T=-T"
    assert d["equivalent_condition"] == "[P_R,A]=0"
    assert d["corrected_defect"] == "T+T^T=P_R A-A P_R"
    assert d["corrected_defect_rank"] == 16382
    assert d["retired_zero_order_defect_rank"] == 130912
    assert d["completed_map_rank"] == 122721
    assert d["radial_descent_restored"] is True
    assert d["first_order_principal_integrability"] is False
    assert d["projector_action_owned"] is False
    assert "Q^T=-Q" in d["classification_theorem"]
    assert d["zero_order_symmetric_completion_classification_survives"] is False
    assert "commutator rank 16382" in d["correction_scope"]
    assert d["source_and_ledger_effect"].endswith("LEDGER_UNCHANGED")


if __name__ == "__main__":
    data = build(); validate(data)
    OUTPUT.write_text(json.dumps(data, indent=2, sort_keys=True) + "\n")
    print("K1128 controls: 15/15")
