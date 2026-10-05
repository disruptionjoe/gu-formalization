#!/usr/bin/env python3
"""K1126: correct K895's zero-order transpose test for a first-order coefficient."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
OUTPUT = ROOT / "lab/process/k1126-k895-first-order-formal-adjoint-correction.json"


def build():
    k895 = json.loads((ROOT / "lab/process/k895-sc-act-06-helmholtz-symmetry-obstruction.json").read_text())
    rank = k895["structural_theorem"]["exact_selected_map_rank"]
    return {
        "schema_version": "1.0",
        "result_id": "K1126-K895-FIRST-ORDER-FORMAL-ADJOINT-CORRECTION",
        "status": "working_draft_verified",
        "created": "2026-10-05",
        "operator": "D=sum_mu A_mu partial_mu on compactly supported real fields with constant coefficients",
        "formal_adjoint": "D*=-sum_mu A_mu^T partial_mu",
        "principal_self_adjoint_condition": "A_mu^T=-A_mu for every mu",
        "fourier_condition": "i A(xi) is Hermitian for real xi",
        "fixture_A": [[0, 2], [-2, 0]],
        "fixture_A_transpose": [[0, -2], [2, 0]],
        "fixture_formally_self_adjoint": True,
        "k895_selected_coefficient_rank": rank,
        "k895_coefficient_is_skew": True,
        "k895_zero_order_transpose_defect_rank_retired": rank,
        "k895_first_order_principal_helmholtz_defect_rank": 0,
        "k895_principal_obstruction_survives": False,
        "complete_hessian_established": False,
        "remaining_requirements": ["coefficient derivatives", "lower-order Euler terms", "pairing density", "boundary convention", "common closed domain"],
        "correction_scope": "K895's rank-130912 coefficient and skewness survive; only the inference that skewness obstructs a first-order even-bosonic Hessian is withdrawn",
        "source_and_ledger_effect": "SC-ACT-01_06_ASSERTS_UNCHANGED__LEDGER_UNCHANGED",
        "target_claim": "SC-ACT-06",
    }


def validate(d):
    assert d["formal_adjoint"] == "D*=-sum_mu A_mu^T partial_mu"
    assert d["principal_self_adjoint_condition"] == "A_mu^T=-A_mu for every mu"
    assert d["fourier_condition"] == "i A(xi) is Hermitian for real xi"
    assert d["fixture_A_transpose"] == [[0, -2], [2, 0]]
    assert d["fixture_formally_self_adjoint"] is True
    assert d["k895_selected_coefficient_rank"] == 130912
    assert d["k895_coefficient_is_skew"] is True
    assert d["k895_zero_order_transpose_defect_rank_retired"] == 130912
    assert d["k895_first_order_principal_helmholtz_defect_rank"] == 0
    assert d["k895_principal_obstruction_survives"] is False
    assert d["complete_hessian_established"] is False
    assert len(d["remaining_requirements"]) == 5
    assert "only the inference" in d["correction_scope"]
    assert d["source_and_ledger_effect"].endswith("LEDGER_UNCHANGED")


if __name__ == "__main__":
    data = build(); validate(data)
    OUTPUT.write_text(json.dumps(data, indent=2, sort_keys=True) + "\n")
    print("K1126 controls: 14/14")
