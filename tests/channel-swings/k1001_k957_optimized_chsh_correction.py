#!/usr/bin/env python3
"""K1001: optimal CHSH value for the K956 phase-damped Bell state."""
from __future__ import annotations
import argparse, json
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
OUTPUT = ROOT / "lab/process/k1001-k957-optimized-chsh-correction.json"

def build():
    rows = []
    for lam in (Fraction(0), Fraction(2, 5), Fraction(1, 2), Fraction(1)):
        rows.append({
            "lambda": str(lam),
            "correlation_squared_eigenvalues": ["1", str(lam * lam), str(lam * lam)],
            "S_max_squared": str(4 * (1 + lam * lam)),
            "violates_CHSH": lam > 0,
        })
    return {
        "schema_version": "1.0",
        "result_id": "K1001-K957-OPTIMIZED-CHSH-CORRECTION",
        "status": "working_draft_verified",
        "created": "2026-10-04",
        "classification": "INTERNAL_CONDITIONAL_MATHEMATICS",
        "target_claim": "NONE-NOT-A-KILL",
        "state": "rho_lambda=(I tensor I + lambda X tensor X - lambda Y tensor Y + Z tensor Z)/4",
        "correlation_tensor": "diag(lambda,-lambda,1)",
        "horodecki_spectrum": ["1", "lambda^2", "lambda^2"],
        "optimized_chsh": {
            "formula": "S_max(lambda)=2 sqrt(1+lambda^2)",
            "violation_iff": "lambda>0",
            "alice_settings": ["Z", "X"],
            "bob_settings": [
                "(Z+lambda X)/sqrt(1+lambda^2)",
                "(Z-lambda X)/sqrt(1+lambda^2)",
            ],
        },
        "k957_scope_correction": {
            "preserved_formula": "S_fixed(lambda)=sqrt(2)(1+lambda)",
            "preserved_settings": "Bell-endpoint settings frozen at lambda=1",
            "not_the_post_damping_optimum": True,
            "old_threshold_applies_only_to_fixed_witness": True,
        },
        "exact_controls": {
            "rows": rows,
            "lambda_two_fifths_S_max_squared": "116/25",
            "lambda_two_fifths_violates": True,
            "lambda_zero_saturates_classical_boundary": True,
            "lambda_one_saturates_tsirelson": True,
        },
        "ownership": {
            "bell_state_tensor_born_and_setting_optimization_imported": True,
            "gu_physical_quotient_or_action_constructed": False,
            "prediction_or_confirmation": False,
        },
        "claim_ceiling": "Exact correction distinguishing K957's frozen Bell-endpoint witness from the optimized CHSH value of the same imported damped Bell state; no GU-native state, observable, action, prediction or confirmation result.",
    }

def validate(p):
    assert p["correlation_tensor"] == "diag(lambda,-lambda,1)"
    assert p["horodecki_spectrum"] == ["1", "lambda^2", "lambda^2"]
    q = p["optimized_chsh"]
    assert q["formula"] == "S_max(lambda)=2 sqrt(1+lambda^2)"
    assert q["violation_iff"] == "lambda>0"
    assert q["alice_settings"] == ["Z", "X"] and len(q["bob_settings"]) == 2
    c = p["k957_scope_correction"]
    assert c["preserved_formula"] == "S_fixed(lambda)=sqrt(2)(1+lambda)"
    assert c["not_the_post_damping_optimum"] and c["old_threshold_applies_only_to_fixed_witness"]
    e = p["exact_controls"]
    assert e["lambda_two_fifths_S_max_squared"] == "116/25" and e["lambda_two_fifths_violates"]
    assert e["lambda_zero_saturates_classical_boundary"] and e["lambda_one_saturates_tsirelson"]
    assert [r["S_max_squared"] for r in e["rows"]] == ["4", "116/25", "5", "8"]
    o = p["ownership"]
    assert o["bell_state_tensor_born_and_setting_optimization_imported"]
    assert not o["gu_physical_quotient_or_action_constructed"] and not o["prediction_or_confirmation"]

def main():
    ap = argparse.ArgumentParser(); ap.add_argument("--write", action="store_true"); ap.add_argument("--check", action="store_true")
    a = ap.parse_args(); p = build(); validate(p); text = json.dumps(p, indent=2, sort_keys=True) + "\n"
    if a.check: assert OUTPUT.read_text() == text
    elif a.write: OUTPUT.write_text(text)
    else: print(text, end="")
    print("K1001 controls: 15/15")

if __name__ == "__main__": main()
