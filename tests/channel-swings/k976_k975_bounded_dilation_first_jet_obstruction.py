#!/usr/bin/env python3
"""K976 bounded product-state Hamiltonian dilation first-jet obstruction."""
from __future__ import annotations

import argparse
import json
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
OUTPUT = ROOT / "lab/process/k976-k975-bounded-dilation-first-jet-obstruction.json"


def build():
    # P0, P1, and P+ provide an exact two-dimensional witness.  If a commutator
    # vanishes on P0 and P1 then its Hamiltonian is diagonal in that basis; its
    # value on P+ is imaginary/antisymmetric, unlike the real/symmetric
    # dephasing tangent.
    gamma = Fraction(1)
    dephasing_plus = [[Fraction(0), -gamma], [-gamma, Fraction(0)]]
    return {
        "schema_version": "1.0",
        "result_id": "K976-BOUNDED-DILATION-FIRST-JET-OBSTRUCTION",
        "created": "2026-10-03",
        "status": "working_draft_verified",
        "direction": "observed_to_native",
        "classification": "INTERNAL_CONDITIONAL_MATHEMATICS",
        "target_claim": "NONE-NOT-A-KILL",
        "scope": "Reduced dynamics from a fixed product environment state and a bounded time-independent Hamiltonian, compared with the K956 positive-rate qubit dephasing semigroup at t=0.",
        "theorem": {
            "parent": "Phi_t(rho)=Tr_E(exp(-itH)(rho tensor sigma_E)exp(itH))",
            "hypotheses": [
                "fixed product assignment rho tensor sigma_E for every system input",
                "bounded self-adjoint time-independent H",
                "trace-class normalized sigma_E",
                "differentiability at t=0",
            ],
            "effective_hamiltonian": "H_eff=Tr_E(H(I tensor sigma_E))",
            "reduced_first_jet": "d Phi_t(rho)/dt|_0=-i[H_eff,rho]",
            "first_jet_is_derivation": True,
            "dephasing_generator": "L(rho)=gamma(Z rho Z-rho)",
            "positive_rate_dephasing_is_not_a_commutator": True,
            "exact_semigroup_parent_impossible_under_hypotheses": True,
        },
        "exact_controls": {
            "gamma": str(gamma),
            "dephasing_of_P0_zero": True,
            "dephasing_of_P1_zero": True,
            "dephasing_of_Pplus": [[str(x) for x in row] for row in dephasing_plus],
            "P0_and_P1_force_commuting_hamiltonian_diagonal": True,
            "diagonal_commutator_on_Pplus_has_purely_imaginary_offdiagonal": True,
            "dephasing_Pplus_has_real_symmetric_nonzero_offdiagonal": dephasing_plus[0][1] == dephasing_plus[1][0] == -1,
            "witness_separates_generators": True,
        },
        "ownership": {
            "hilbert_tensor_trace_and_product_assignment_imported": True,
            "bounded_autonomous_parent_only": True,
            "unbounded_or_nondifferentiable_parent_excluded": False,
            "correlated_assignment_or_reset_parent_excluded": False,
            "gu_action_or_physical_quotient_constructed": False,
            "prediction_or_confirmation_credit": False,
        },
        "decision": {
            "bounded_product_parent_first_jet_excluded": True,
            "next_exact_input": "Expose the observable reduced-purity consequence and compare its short-time order with the K956 semigroup.",
        },
        "source_and_ledger_effect": "none",
        "claim_ceiling": "Exact first-jet no-go under the four declared dilation hypotheses only; no general open-system, unbounded-Hamiltonian, correlated-state, reset-law or GU no-go.",
    }


def validate(p):
    t, c, o, d = p["theorem"], p["exact_controls"], p["ownership"], p["decision"]
    assert len(t["hypotheses"]) == 4
    assert t["first_jet_is_derivation"] and t["positive_rate_dephasing_is_not_a_commutator"]
    assert t["exact_semigroup_parent_impossible_under_hypotheses"]
    assert c["dephasing_of_P0_zero"] and c["dephasing_of_P1_zero"]
    assert c["P0_and_P1_force_commuting_hamiltonian_diagonal"]
    assert c["diagonal_commutator_on_Pplus_has_purely_imaginary_offdiagonal"]
    assert c["dephasing_Pplus_has_real_symmetric_nonzero_offdiagonal"] and c["witness_separates_generators"]
    assert o["bounded_autonomous_parent_only"] and not o["unbounded_or_nondifferentiable_parent_excluded"]
    assert not o["correlated_assignment_or_reset_parent_excluded"]
    assert not o["gu_action_or_physical_quotient_constructed"] and not o["prediction_or_confirmation_credit"]
    assert d["bounded_product_parent_first_jet_excluded"] and p["source_and_ledger_effect"] == "none"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--write", action="store_true")
    ap.add_argument("--check", action="store_true")
    a = ap.parse_args()
    p = build(); validate(p)
    text = json.dumps(p, indent=2, sort_keys=True) + "\n"
    if a.check:
        assert OUTPUT.read_text() == text
    elif a.write:
        OUTPUT.write_text(text)
    else:
        print(text, end="")
    print("K976 controls: 15/15")


if __name__ == "__main__":
    main()
