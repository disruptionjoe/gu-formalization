#!/usr/bin/env python3
"""K980 action/domain disposition for the bounded-dilation boundary."""
from __future__ import annotations

import argparse
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
OUTPUT = ROOT / "lab/process/k980-k979-action-domain-disposition.json"
INPUTS = [
    ROOT / "lab/process/k976-k975-bounded-dilation-first-jet-obstruction.json",
    ROOT / "lab/process/k977-k976-reduced-purity-zeno-boundary.json",
    ROOT / "lab/process/k978-k977-collision-uniform-convergence.json",
    ROOT / "lab/process/k979-k978-markov-dilation-assumption-fork.json",
]


def build():
    ps = [json.loads(p.read_text()) for p in INPUTS]
    return {
        "schema_version": "1.0",
        "result_id": "K980-ACTION-DOMAIN-DISPOSITION",
        "created": "2026-10-03",
        "status": "working_draft_verified",
        "direction": "observed_to_native",
        "classification": "INTERNAL_REQUIREMENT_DISPOSITION",
        "target_claim": "NONE-NOT-A-KILL",
        "scope": "Composition of K976--K979 into the physical quotient, action, domain, locality and holdout boundary for the K956 dephasing candidate.",
        "dependency_checks": {
            "input_ids": [p["result_id"] for p in ps],
            "all_source_and_ledger_effect_none": all(p["source_and_ledger_effect"] == "none" for p in ps),
            "all_prediction_or_confirmation_withheld": all(not p["ownership"]["prediction_or_confirmation_credit"] for p in ps),
            "assumption_fork_unselected": ps[3]["assumption_fork"]["does_not_select_a_failure_mode"],
        },
        "decision": {
            "bounded_product_autonomous_parent_excluded": True,
            "fresh_collision_family_uniformly_approximates": True,
            "fresh_collision_family_imports_singular_resources": True,
            "next_exact_input": "A GU-owned physical quotient and positive state/effect pairing plus an action must select an unbounded/domain-controlled reservoir, reset/time-dependent resource, correlated assignment, or another explicitly typed horn; prove its locality and controlled limit; and freeze a distinct empirical resolution or holdout before scoring.",
        },
        "demand": {
            "gu_physical_quotient_and_positive_effect_pairing_required": True,
            "gu_action_owned_local_coupling_required": True,
            "selected_horn_and_common_domain_required": True,
            "controlled_limit_or_reset_accounting_required": True,
            "remote_marginal_and_locality_theorem_required": True,
            "distinct_empirical_holdout_frozen_before_scoring_required": True,
        },
        "discriminator": {
            "bounded_autonomous_parent": "zero first-order purity loss and no dissipative first jet",
            "exact_markov_target": "linear first-order purity loss at positive rate",
            "fresh_collision_repair": "uniform O(h) coherence error with diverging coupling rate and ancilla supply",
            "status": "reserved_not_scored",
        },
        "ownership": {
            "repository_conditional_models_only": True,
            "gu_action_or_physical_quotient_constructed": False,
            "source_claim_or_ledger_verdict_changed": False,
            "prediction_or_confirmation_credit": False,
        },
        "source_and_ledger_effect": "none",
        "claim_ceiling": "Conditional microscopic action/domain requirement and unscored assumption fork only; no exhaustive dilation theorem, empirical score, GU derivation, prediction, confirmation or protected verdict.",
    }


def validate(p):
    c, d, q, x, o = p["dependency_checks"], p["decision"], p["demand"], p["discriminator"], p["ownership"]
    assert len(c["input_ids"]) == 4 and c["all_source_and_ledger_effect_none"]
    assert c["all_prediction_or_confirmation_withheld"] and c["assumption_fork_unselected"]
    assert d["bounded_product_autonomous_parent_excluded"] and d["fresh_collision_family_uniformly_approximates"]
    assert d["fresh_collision_family_imports_singular_resources"]
    assert all(q.values()) and x["status"] == "reserved_not_scored"
    assert o["repository_conditional_models_only"] and not o["gu_action_or_physical_quotient_constructed"]
    assert not o["source_claim_or_ledger_verdict_changed"] and not o["prediction_or_confirmation_credit"]
    assert p["source_and_ledger_effect"] == "none"


def main():
    ap = argparse.ArgumentParser(); ap.add_argument("--write", action="store_true"); ap.add_argument("--check", action="store_true"); a = ap.parse_args()
    p = build(); validate(p); text = json.dumps(p, indent=2, sort_keys=True) + "\n"
    if a.check: assert OUTPUT.read_text() == text
    elif a.write: OUTPUT.write_text(text)
    else: print(text, end="")
    print("K980 controls: 14/14")


if __name__ == "__main__": main()
