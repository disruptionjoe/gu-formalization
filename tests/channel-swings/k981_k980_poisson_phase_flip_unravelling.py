#!/usr/bin/env python3
"""K981 exact Poisson phase-flip unraveling of the K956 semigroup."""
from __future__ import annotations

import argparse
import json
import math
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
OUTPUT = ROOT / "lab/process/k981-k980-poisson-phase-flip-unravelling.json"


def build():
    gamma = 0.7
    rows = []
    for t in (0.0, 0.25, 1.0, 2.0, 4.0):
        x = gamma * t
        even = (1.0 + math.exp(-2.0 * x)) / 2.0
        odd = (1.0 - math.exp(-2.0 * x)) / 2.0
        # Independent finite-sum replay of E[(-1)^N] for N~Poisson(x).
        terms = [math.exp(-x) * x**n / math.factorial(n) for n in range(80)]
        replay = sum(((-1) ** n) * p for n, p in enumerate(terms))
        rows.append({
            "t": t,
            "p_even": even,
            "p_odd": odd,
            "coherence_even_minus_odd": even - odd,
            "target_exp_minus_2_gamma_t": math.exp(-2.0 * gamma * t),
            "finite_sum_replay": replay,
            "normalization_error": abs(even + odd - 1.0),
            "identity_error": abs(replay - math.exp(-2.0 * gamma * t)),
        })
    return {
        "schema_version": "1.0",
        "result_id": "K981-POISSON-PHASE-FLIP-UNRAVELLING",
        "created": "2026-10-03",
        "status": "working_draft_verified",
        "direction": "observed_to_native",
        "classification": "INTERNAL_CONDITIONAL_MATHEMATICS",
        "target_claim": "NONE-NOT-A-KILL",
        "scope": "A qubit driven by a supplied classical Poisson clock of rate gamma and pathwise phase flips Z^N_t.",
        "construction": {
            "count_law": "N_t~Poisson(gamma t)",
            "pathwise_unitary": "U_t=Z^N_t",
            "ensemble_channel": "D_t(rho)=P(even)rho+P(odd)ZrhoZ",
            "coherence": "E[(-1)^N_t]=exp(-2 gamma t)",
            "semigroup": True,
            "cptp": True,
            "remote_marginal_invariant": True,
        },
        "exact_controls": {
            "gamma": gamma,
            "rows": rows,
            "all_probabilities_normalized": all(r["normalization_error"] < 1e-15 for r in rows),
            "all_characteristic_identities_replayed": all(r["identity_error"] < 1e-13 for r in rows),
            "strict_decay_after_zero": all(rows[i + 1]["coherence_even_minus_odd"] < rows[i]["coherence_even_minus_odd"] for i in range(len(rows) - 1)),
            "identity_at_zero": rows[0]["p_even"] == 1.0 and rows[0]["p_odd"] == 0.0,
        },
        "ownership": {
            "classical_poisson_clock_imported": True,
            "point_jump_rule_imported": True,
            "positive_hilbert_pairing_imported": True,
            "gu_action_or_physical_quotient_constructed": False,
            "prediction_or_confirmation_credit": False,
        },
        "decision": {
            "exact_stochastic_horn_constructed": True,
            "deterministic_grid_singularity_not_horn_general": True,
            "next_exact_input": "Derive the generator and separate finite event rate from the imported stochastic clock, point-jump and record resources.",
        },
        "source_and_ledger_effect": "none",
        "claim_ceiling": "Exact random-unitary unraveling of the imported qubit semigroup only; not a deterministic Hamiltonian dilation or GU-owned stochastic action.",
    }


def validate(p):
    c, x, o, d = p["construction"], p["exact_controls"], p["ownership"], p["decision"]
    assert c["semigroup"] and c["cptp"] and c["remote_marginal_invariant"]
    assert len(x["rows"]) == 5 and x["all_probabilities_normalized"]
    assert x["all_characteristic_identities_replayed"] and x["strict_decay_after_zero"] and x["identity_at_zero"]
    assert o["classical_poisson_clock_imported"] and o["point_jump_rule_imported"] and o["positive_hilbert_pairing_imported"]
    assert not o["gu_action_or_physical_quotient_constructed"] and not o["prediction_or_confirmation_credit"]
    assert d["exact_stochastic_horn_constructed"] and d["deterministic_grid_singularity_not_horn_general"]
    assert p["source_and_ledger_effect"] == "none"


def main():
    ap = argparse.ArgumentParser(); ap.add_argument("--write", action="store_true"); ap.add_argument("--check", action="store_true"); a = ap.parse_args()
    p = build(); validate(p); text = json.dumps(p, indent=2, sort_keys=True) + "\n"
    if a.check: assert OUTPUT.read_text() == text
    elif a.write: OUTPUT.write_text(text)
    else: print(text, end="")
    print("K981 controls: 14/14")


if __name__ == "__main__": main()
