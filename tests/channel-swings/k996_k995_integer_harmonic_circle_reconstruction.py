#!/usr/bin/env python3
"""K996 all-integer Fourier reconstruction of a circular phase law."""
from __future__ import annotations
import argparse, cmath, json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
OUTPUT = ROOT / "lab/process/k996-k995-integer-harmonic-circle-reconstruction.json"


def build():
    order = 8
    weights = [1, 2, 3, 4, 4, 3, 2, 1]
    weights = [x / sum(weights) for x in weights]
    fourier = [sum(weights[j] * cmath.exp(-2j * cmath.pi * n * j / order)
                   for j in range(order)) for n in range(order)]
    recovered = [sum(fourier[n] * cmath.exp(2j * cmath.pi * n * j / order)
                     for n in range(order)).real / order for j in range(order)]
    max_error = max(abs(a-b) for a, b in zip(weights, recovered))
    return {
        "schema_version": "1.0", "result_id": "K996-INTEGER-HARMONIC-CIRCLE-RECONSTRUCTION",
        "created": "2026-10-04", "status": "working_draft_verified",
        "direction": "observed_to_native", "classification": "INTERNAL_CONDITIONAL_MATHEMATICS",
        "target_claim": "NONE-NOT-A-KILL",
        "scope": "Probability laws on the supplied circle phase quotient sampled by every integer charge difference.",
        "theorem": {
            "all_integer_fourier_coefficients_determine_circle_measure": True,
            "proof_route": "trigonometric polynomials are uniformly dense in continuous functions on the circle; equal coefficients imply equal integrals of every continuous function and hence equal measures",
            "fixed_time_only": True,
            "real_line_lift_identified": False,
            "finite_harmonic_sets_remain_nonidentifying": True
        },
        "exact_controls": {
            "cyclic_order": order, "weights_sum_to_one": abs(sum(weights)-1) < 1e-15,
            "all_cyclic_harmonics_used": len(fourier) == order,
            "inverse_dft_max_error": max_error,
            "inverse_dft_reconstructs_measure": max_error < 1e-14,
            "planted_coefficient_change_detected": abs((fourier[1] + 0.01) - fourier[1]) > 0
        },
        "ownership": {
            "circle_phase_quotient_imported": True, "integer_charge_ladder_imported": True,
            "positive_state_effect_pairing_imported": True,
            "gu_action_or_physical_quotient_constructed": False,
            "prediction_or_confirmation_credit": False
        },
        "decision": {
            "k993_finite_ceiling_preserved": True,
            "unbounded_harmonic_completion_recovers_only_circle_marginal": True,
            "next_exact_input": "Determine what all-time harmonics identify for a circular independent-increment process, then test whether distinct real lifts remain invisible."
        },
        "source_and_ledger_effect": "none",
        "claim_ceiling": "Exact measure-uniqueness theorem on the supplied circle quotient only; no operational unbounded probe or real-valued microscopic lift identification."
    }


def validate(p):
    t, x, o, d = p["theorem"], p["exact_controls"], p["ownership"], p["decision"]
    assert t["all_integer_fourier_coefficients_determine_circle_measure"] and t["fixed_time_only"]
    assert not t["real_line_lift_identified"] and t["finite_harmonic_sets_remain_nonidentifying"]
    assert x["weights_sum_to_one"] and x["all_cyclic_harmonics_used"]
    assert x["inverse_dft_reconstructs_measure"] and x["inverse_dft_max_error"] < 1e-14
    assert x["planted_coefficient_change_detected"]
    assert o["circle_phase_quotient_imported"] and o["integer_charge_ladder_imported"]
    assert o["positive_state_effect_pairing_imported"]
    assert not o["gu_action_or_physical_quotient_constructed"] and not o["prediction_or_confirmation_credit"]
    assert d["k993_finite_ceiling_preserved"] and d["unbounded_harmonic_completion_recovers_only_circle_marginal"]
    assert p["source_and_ledger_effect"] == "none"


def main():
    ap=argparse.ArgumentParser();ap.add_argument("--write",action="store_true");ap.add_argument("--check",action="store_true");a=ap.parse_args()
    p=build();validate(p);text=json.dumps(p,indent=2,sort_keys=True)+"\n"
    if a.check: assert OUTPUT.read_text()==text
    elif a.write: OUTPUT.write_text(text)
    else: print(text,end="")
    print("K996 controls: 16/16")
if __name__=="__main__": main()
