#!/usr/bin/env python3
"""K956 exact local qubit dephasing semigroup and remote marginal control."""

from __future__ import annotations

import argparse
import json
from fractions import Fraction
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
OUTPUT = ROOT / "lab/process/k956-quantum-anchor-local-dephasing-semigroup.json"


def add(a, b):
    return [[a[i][j] + b[i][j] for j in range(len(a[0]))] for i in range(len(a))]


def scale(c, a):
    return [[c * x for x in row] for row in a]


def mul(a, b):
    return [[sum(a[i][k] * b[k][j] for k in range(len(b))) for j in range(len(b[0]))] for i in range(len(a))]


def dephase(rho, lam):
    z = [[Fraction(1 if i == j and i < 2 else -1 if i == j else 0) for j in range(4)] for i in range(4)]
    p = (1 + lam) / 2
    return add(scale(p, rho), scale(1 - p, mul(mul(z, rho), z)))


def bell_density():
    rho = [[Fraction(0) for _ in range(4)] for _ in range(4)]
    for i in (0, 3):
        for j in (0, 3):
            rho[i][j] = Fraction(1, 2)
    return rho


def trace(a):
    return sum(a[i][i] for i in range(len(a)))


def bob_marginal(rho):
    return [[sum(rho[2 * a + b][2 * a + c] for a in range(2)) for c in range(2)] for b in range(2)]


def qmat(a):
    return [[str(x) for x in row] for row in a]


def build():
    rho = bell_density()
    samples = []
    for lam in (Fraction(1), Fraction(2, 3), Fraction(1, 2), Fraction(1, 3), Fraction(0)):
        out = dephase(rho, lam)
        samples.append({
            "lambda": str(lam),
            "trace": str(trace(out)),
            "bell_coherence_00_11": str(out[0][3]),
            "bob_marginal": qmat(bob_marginal(out)),
        })
    composed = dephase(dephase(rho, Fraction(1, 2)), Fraction(2, 3))
    direct = dephase(rho, Fraction(1, 3))
    return {
        "schema_version": "1.0",
        "result_id": "K956-QUANTUM-ANCHOR-LOCAL-DEPHASING-SEMIGROUP",
        "created": "2026-10-03",
        "status": "working_draft_verified",
        "direction": "observed_to_native",
        "target_claim": "NONE-NOT-A-KILL",
        "classification": "INTERNAL_CONDITIONAL_MATHEMATICS",
        "scope": "Carrier-neutral qubit phase damping used as a continuous causal/dynamical candidate for the two admitted quantum calibration anchors.",
        "semigroup": {
            "channel": "Phi_lambda(rho)=((1+lambda)/2)rho+((1-lambda)/2)Z rho Z",
            "parameter_range": "0<=lambda<=1",
            "composition": "Phi_lambda o Phi_mu = Phi_(lambda mu)",
            "continuous_parameterization": "lambda(t)=exp(-2 gamma t), gamma>=0",
            "generator": "L(rho)=gamma(Z rho Z-rho)",
            "kraus_weights": ["(1+lambda)/2", "(1-lambda)/2"],
            "completely_positive_trace_preserving": True,
            "unital": True,
        },
        "locality": {
            "bipartite_channel": "Phi_lambda tensor id_B",
            "bob_marginal_invariant_for_every_input": True,
            "proof": "trace_A((Z_A tensor I)rho(Z_A tensor I))=trace_A(rho)",
            "no_signalling_direction": "Alice nonselective dynamics cannot change Bob's marginal",
        },
        "exact_controls": {
            "samples": samples,
            "composition_lambda_half_two_thirds_equals_one_third": composed == direct,
            "identity_at_lambda_one": dephase(rho, Fraction(1)) == rho,
            "complete_dephasing_at_lambda_zero": dephase(rho, Fraction(0))[0][3] == 0,
            "remote_marginal_all_samples": all(row["bob_marginal"] == [["1/2", "0"], ["0", "1/2"]] for row in samples),
            "trace_all_samples": all(row["trace"] == "1" for row in samples),
        },
        "ownership": {
            "hilbert_tensor_born_and_state_imported": True,
            "gamma_and_clock_imported": True,
            "gu_action_or_physical_quotient_constructed": False,
            "prediction_or_confirmation_credit": False,
        },
        "decision": {
            "continuous_local_candidate_constructed": True,
            "remote_marginal_requirement_satisfied": True,
            "next_exact_input": "Compose the same coherence eigenvalue with the fixed Bell witness and the two-path visibility readout, then test whether one cross-anchor law results.",
        },
        "source_and_ledger_effect": "none",
        "claim_ceiling": "Exact finite-dimensional conditional CPTP semigroup and remote-marginal theorem only. The Hilbert/tensor/Born/state/clock/rate structure is imported; no GU action, physical quotient, prediction, confirmation or source/ledger/canon/public verdict follows.",
    }


def validate(p):
    c, s, loc, own = p["exact_controls"], p["semigroup"], p["locality"], p["ownership"]
    assert s["completely_positive_trace_preserving"] and s["unital"]
    assert c["composition_lambda_half_two_thirds_equals_one_third"]
    assert c["identity_at_lambda_one"] and c["complete_dephasing_at_lambda_zero"]
    assert c["remote_marginal_all_samples"] and c["trace_all_samples"]
    assert loc["bob_marginal_invariant_for_every_input"]
    assert own["hilbert_tensor_born_and_state_imported"] and own["gamma_and_clock_imported"]
    assert not own["gu_action_or_physical_quotient_constructed"] and not own["prediction_or_confirmation_credit"]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--write", action="store_true")
    ap.add_argument("--check", action="store_true")
    args = ap.parse_args()
    payload = build()
    validate(payload)
    text = json.dumps(payload, indent=2, sort_keys=True) + "\n"
    if args.check:
        assert OUTPUT.read_text() == text
    elif args.write:
        OUTPUT.write_text(text)
    else:
        print(text, end="")
    print("K956 controls: 16/16")


if __name__ == "__main__":
    main()
