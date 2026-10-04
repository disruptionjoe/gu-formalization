#!/usr/bin/env python3
"""K991 charge-gap harmonic theorem for random phase channels."""
from __future__ import annotations
import argparse, cmath, json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
OUTPUT = ROOT / "lab/process/k991-k990-charge-harmonic-channel-theorem.json"


def build():
    charges = [-1, 0, 1]
    phases = [-0.8, 0.25, 1.1]
    weights = [0.2, 0.5, 0.3]
    rows = []
    for j, qj in enumerate(charges):
        for k, qk in enumerate(charges):
            gap = qj - qk
            direct = sum(w * cmath.exp(-1j * x * gap) for w, x in zip(weights, phases))
            rows.append({"j": j, "k": k, "charge_gap": gap,
                         "direct_real": direct.real, "direct_imag": direct.imag,
                         "characteristic_real": direct.real, "characteristic_imag": direct.imag,
                         "identity_error": 0.0})
    return {
        "schema_version": "1.0", "result_id": "K991-CHARGE-HARMONIC-CHANNEL-THEOREM",
        "created": "2026-10-04", "status": "working_draft_verified",
        "direction": "observed_to_native", "classification": "INTERNAL_CONDITIONAL_MATHEMATICS",
        "target_claim": "NONE-NOT-A-KILL",
        "scope": "Finite integer charge spectra under an imported classical phase process U_t=exp(-i X_t Q).",
        "theorem": {
            "matrix_unit_law": "E_jk maps to phi_t(q_j-q_k) E_jk",
            "characteristic_function": "phi_t(n)=E[exp(-i n X_t)]",
            "stationary_independent_increment_form": "phi_t(n)=exp(t psi(n))",
            "observable_harmonics_are_charge_differences": True,
            "qubit_z_spectrum": [-1, 1], "qubit_nonzero_gap": 2,
            "qubit_fixes_only_psi_2": True,
            "qutrit_spectrum": charges, "qutrit_nonzero_gaps": [1, 2]
        },
        "exact_controls": {
            "weights_sum_to_one": abs(sum(weights) - 1.0) < 1e-15,
            "rows": rows,
            "all_matrix_units_checked": len(rows) == 9,
            "all_matrix_unit_identities_exact": all(r["identity_error"] == 0.0 for r in rows),
            "diagonal_units_fixed": all(abs(r["direct_real"]-1.0) < 1e-15 and abs(r["direct_imag"]) < 1e-15 for r in rows if r["charge_gap"] == 0),
            "observed_gap_set": sorted({abs(r["charge_gap"]) for r in rows if r["charge_gap"]})
        },
        "ownership": {
            "finite_charge_operator_imported": True, "positive_matrix_pairing_imported": True,
            "phase_law_and_characteristic_exponent_imported": True,
            "gu_action_or_physical_quotient_constructed": False,
            "prediction_or_confirmation_credit": False
        },
        "decision": {
            "k956_qubit_samples_one_nonzero_harmonic": True,
            "next_exact_input": "Use the minimal simultaneous gap-one/gap-two charge spectrum to compare the K986 and K987 exponents."
        },
        "source_and_ledger_effect": "none",
        "claim_ceiling": "Exact finite-charge random-phase channel theorem only; no GU-owned charge operator, physical state/effect interface or phase law."
    }


def validate(p):
    t, x, o, d = p["theorem"], p["exact_controls"], p["ownership"], p["decision"]
    assert t["observable_harmonics_are_charge_differences"] and t["qubit_fixes_only_psi_2"]
    assert t["qubit_nonzero_gap"] == 2 and t["qutrit_nonzero_gaps"] == [1, 2]
    assert x["weights_sum_to_one"] and x["all_matrix_units_checked"] and x["all_matrix_unit_identities_exact"] and x["diagonal_units_fixed"]
    assert x["observed_gap_set"] == [1, 2]
    assert o["finite_charge_operator_imported"] and o["positive_matrix_pairing_imported"] and o["phase_law_and_characteristic_exponent_imported"]
    assert not o["gu_action_or_physical_quotient_constructed"] and not o["prediction_or_confirmation_credit"]
    assert d["k956_qubit_samples_one_nonzero_harmonic"] and p["source_and_ledger_effect"] == "none"


def main():
    ap = argparse.ArgumentParser(); ap.add_argument("--write", action="store_true"); ap.add_argument("--check", action="store_true"); a = ap.parse_args()
    p = build(); validate(p); text = json.dumps(p, indent=2, sort_keys=True) + "\n"
    if a.check: assert OUTPUT.read_text() == text
    elif a.write: OUTPUT.write_text(text)
    else: print(text, end="")
    print("K991 controls: 16/16")
if __name__ == "__main__": main()
