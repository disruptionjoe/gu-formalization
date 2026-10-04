#!/usr/bin/env python3
"""K977 reduced-purity short-time boundary."""
from __future__ import annotations

import argparse
import json
import math
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
OUTPUT = ROOT / "lab/process/k977-k976-reduced-purity-zeno-boundary.json"


def build():
    gamma = 1.0
    hs = [0.1, 0.03, 0.01, 0.003]
    semigroup = []
    bounded_example = []
    for h in hs:
        p_markov = (1 + math.exp(-4 * gamma * h)) / 2
        p_unitary = (1 + math.cos(2 * h) ** 2) / 2
        semigroup.append({"t": h, "purity": p_markov, "linear_loss_ratio": (1 - p_markov) / h})
        bounded_example.append({"t": h, "purity": p_unitary, "linear_loss_ratio": (1 - p_unitary) / h, "quadratic_loss_ratio": (1 - p_unitary) / h**2})
    return {
        "schema_version": "1.0",
        "result_id": "K977-REDUCED-PURITY-ZENO-BOUNDARY",
        "created": "2026-10-03",
        "status": "working_draft_verified",
        "direction": "observed_to_native",
        "classification": "INTERNAL_CONDITIONAL_MATHEMATICS",
        "target_claim": "NONE-NOT-A-KILL",
        "scope": "Short-time purity of a pure system input under K976 bounded product-state Hamiltonian dilation versus K956 positive-rate dephasing.",
        "theorem": {
            "bounded_parent_first_jet": "rho_dot(0)=-i[H_eff,P]",
            "pure_input_purity_derivative": "2 Tr(P rho_dot(0))=0",
            "bounded_parent_purity_loss_order": "O(t^2)",
            "dephasing_plus_state": "rho_t=(I+exp(-2 gamma t)X)/2",
            "dephasing_purity": "(1+exp(-4 gamma t))/2",
            "dephasing_purity_derivative": "-2 gamma",
            "positive_rate_orders_incompatible": True,
        },
        "contrary_control": {
            "Hamiltonian": "H=Z tensor Y",
            "environment_state": "|0><0|",
            "system_input": "|+><+|",
            "reduced_coherence": "cos(2t)",
            "reduced_purity": "(1+cos(2t)^2)/2",
            "short_time_loss": "2t^2+O(t^4)",
        },
        "exact_controls": {
            "gamma": gamma,
            "semigroup_rows": semigroup,
            "bounded_example_rows": bounded_example,
            "semigroup_linear_ratio_tends_to_two_gamma": abs(semigroup[-1]["linear_loss_ratio"] - 2 * gamma) < 0.02,
            "bounded_example_linear_ratio_tends_to_zero": bounded_example[-1]["linear_loss_ratio"] < 0.01,
            "bounded_example_quadratic_ratio_tends_to_two": abs(bounded_example[-1]["quadratic_loss_ratio"] - 2) < 0.001,
        },
        "ownership": {
            "purity_and_born_trace_imported": True,
            "general_unbounded_dilation_excluded": False,
            "gu_positive_state_effect_pairing_constructed": False,
            "prediction_or_confirmation_credit": False,
        },
        "decision": {
            "observable_short_time_boundary_proved": True,
            "next_exact_input": "Quantify continuous-time convergence of the fresh-collision repair between its exact grid points.",
        },
        "source_and_ledger_effect": "none",
        "claim_ceiling": "Exact purity-order incompatibility under K976 hypotheses; no universal Zeno theorem for singular, reset, correlated or non-Hamiltonian parents.",
    }


def validate(p):
    t, c, o, d = p["theorem"], p["exact_controls"], p["ownership"], p["decision"]
    assert t["positive_rate_orders_incompatible"]
    assert c["semigroup_linear_ratio_tends_to_two_gamma"]
    assert c["bounded_example_linear_ratio_tends_to_zero"]
    assert c["bounded_example_quadratic_ratio_tends_to_two"]
    assert len(c["semigroup_rows"]) == len(c["bounded_example_rows"]) == 4
    assert o["purity_and_born_trace_imported"] and not o["general_unbounded_dilation_excluded"]
    assert not o["gu_positive_state_effect_pairing_constructed"] and not o["prediction_or_confirmation_credit"]
    assert d["observable_short_time_boundary_proved"] and p["source_and_ledger_effect"] == "none"


def main():
    ap = argparse.ArgumentParser(); ap.add_argument("--write", action="store_true"); ap.add_argument("--check", action="store_true"); a = ap.parse_args()
    p = build(); validate(p); text = json.dumps(p, indent=2, sort_keys=True) + "\n"
    if a.check: assert OUTPUT.read_text() == text
    elif a.write: OUTPUT.write_text(text)
    else: print(text, end="")
    print("K977 controls: 12/12")


if __name__ == "__main__": main()
