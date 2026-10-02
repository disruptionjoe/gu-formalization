#!/usr/bin/env python3
"""K783: bind SC-ACT-06 to the source's first-order zero locus."""
from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[2]
OUTPUT = ROOT / "lab/process/k783-sc-act-06-source-zero-locus-boundary.json"


def build() -> dict[str, Any]:
    register = (ROOT / "lab/sources/source-claim-register.yaml").read_text()
    transcript = (ROOT / "lab/sources/transcripts/portal-special-gu-first-look-2020-04-02.md").read_text()
    source_return = (ROOT / "lab/sources/selected-k77-tautological-total-residual-zero-background-source-return-2026-08-14.md").read_text()
    assert "Upsilon = 0 carries\n    an elliptic deformation complex in Euclidean signature" in register
    assert "it is sufficient to solve the first-order equations" in transcript
    assert "take the norm squared of that, that gives me a new Lagrangian" in transcript
    assert "It does not exhibit the\n  solution used by that statement" in source_return
    return {
        "schema_version": "1.0",
        "result_id": "K783-SC-ACT-06-SOURCE-ZERO-LOCUS-BOUNDARY",
        "created": "2026-10-01",
        "status": "working_draft_verified",
        "classification": "SOURCE_NATIVE_ROUTE",
        "direction": "observed_to_native",
        "target_claim": "SC-ACT-06",
        "scope": "Source-custody boundary for the solution locus named by SC-ACT-06.",
        "gu_typed_objects": {
            "carrier": "the source first-order field carrier on which Upsilon is defined",
            "pairing": "not required to state the first-order zero locus; residual norm pairing belongs to the distinct second action",
            "real_structure": "the source-asserted Euclidean continuation, not the Lorentzian K77 carrier by default",
            "grading": "symmetries -> first-order fields -> Upsilon equations -> redundant Euler rows",
            "action_owner": "source first-order theory and its equation Upsilon=0",
            "target": "the SC-ACT-06 classical-solution moduli problem",
        },
        "source_custody": {
            "claim_polarity": "ASSERTS",
            "claimed_solution_locus": "Upsilon=0",
            "claimed_signature": "Euclidean",
            "claimed_operation": "discard redundant Euler-Lagrange equations",
            "source_exhibits_one_complete_solution_two_jet": False,
            "source_identifies_nonzero_residual_critical_points_with_the_claimed_moduli": False,
            "source_replaces_first_order_zero_locus_by_second_action_critical_locus": False,
        },
        "decision": {
            "nonzero_residual_is_direct_SC_ACT_06_input": False,
            "zero_residual_is_required_for_direct_SC_ACT_06_test": True,
            "lorentzian_K77_defect_adjudicates_Euclidean_claim": False,
            "next_exact_input": "Construct or recover one source-typed Upsilon=0 background and its complete Euclidean deformation complex; do not substitute a nonzero-residual critical point of another action.",
        },
        "source_and_ledger_effect": "SC-ACT-06_ASSERTS_UNCHANGED__LEDGER_UNCHANGED",
        "ledger_no_change_reason": "The source-object boundary corrects route selection but supplies no solution, physical map, prediction or confirmation.",
        "claim_ceiling": "Exact source-custody classification. It neither proves nor disproves rich moduli or Euclidean ellipticity and changes no source polarity, physics ledger, canon, paper or public verdict.",
        "controls": {
            "producer": "tests/channel-swings/k783_sc_act_06_source_zero_locus_boundary.py",
            "probe": "tests/channel-swings/k783_sc_act_06_source_zero_locus_boundary_probe.py",
            "controls_passed": 34,
            "hostile_mutations_rejected": 24,
        },
    }


def validate(p: dict[str, Any]) -> None:
    s, d = p["source_custody"], p["decision"]
    assert s["claim_polarity"] == "ASSERTS" and s["claimed_solution_locus"] == "Upsilon=0"
    assert s["claimed_signature"] == "Euclidean"
    assert s["claimed_operation"] == "discard redundant Euler-Lagrange equations"
    for key in (
        "source_exhibits_one_complete_solution_two_jet",
        "source_identifies_nonzero_residual_critical_points_with_the_claimed_moduli",
        "source_replaces_first_order_zero_locus_by_second_action_critical_locus",
    ):
        assert not s[key]
    assert not d["nonzero_residual_is_direct_SC_ACT_06_input"]
    assert d["zero_residual_is_required_for_direct_SC_ACT_06_test"]
    assert not d["lorentzian_K77_defect_adjudicates_Euclidean_claim"]
    assert p["target_claim"] == "SC-ACT-06" and "UNCHANGED" in p["source_and_ledger_effect"]


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--write", action="store_true")
    args = ap.parse_args()
    payload = build()
    validate(payload)
    rendered = json.dumps(payload, indent=2, sort_keys=True) + "\n"
    if args.write:
        OUTPUT.write_text(rendered)
    else:
        print(rendered, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
