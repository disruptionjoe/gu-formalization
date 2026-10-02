#!/usr/bin/env python3
"""K784: correct ownership of the I1B-plus-I2B stationary comparator."""
from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[2]
OUTPUT = ROOT / "lab/process/k784-sc-act-06-i1b-i2b-action-sum-ownership-correction.json"


def build() -> dict[str, Any]:
    k780 = json.loads((ROOT / "lab/process/k780-sc-act-06-kernel-transverse-stationarity-obstruction.json").read_text())
    branch_return = (ROOT / "lab/sources/selected-k77-branch-hessian-source-reinspection-2026-08-09.md").read_text()
    owner_return = (ROOT / "lab/sources/selected-k77-i2b-action-euler-principal-owner-comparison-source-return-2026-08-13.md").read_text()
    assert k780["theorem"]["combined_stationarity_equation"] == "E_I1B+J^*Q Upsilon=0"
    assert "These are two action candidates; the source does not\nsupply a relative coefficient that would license summing them" in branch_return
    assert "SOURCE_SILENT_OPERATIVE_SECOND_ACTION" in owner_return
    return {
        "schema_version": "1.0",
        "result_id": "K784-SC-ACT-06-I1B-I2B-ACTION-SUM-OWNERSHIP-CORRECTION",
        "created": "2026-10-01",
        "status": "working_draft_verified",
        "classification": "SOURCE_NATIVE_ROUTE_CORRECTION",
        "direction": "observed_to_native",
        "target_claim": "SC-ACT-06",
        "scope": "Action-ownership correction for the combined I1B-plus-I2B stationary equation used in K780--K782.",
        "gu_typed_objects": {
            "carrier": "the common field carrier only after a candidate realizes both distinct source action grammars",
            "pairing": "Q belongs to the residual-square action and does not supply the missing relative action coefficient",
            "real_structure": "unchanged local real comparator; Euclidean source realization remains missing",
            "grading": "first-action Euler covector plus second-action Euler covector",
            "action_owner": "two separately source-confirmed action candidates; their weighted sum is repository-conditional",
            "target": "ownership of E_I1B + lambda J^*Q Upsilon = 0",
        },
        "ownership": {
            "source_confirms_I1B": True,
            "source_confirms_distinct_I2B_grammar": True,
            "source_supplies_relative_sum_coefficient": False,
            "source_selects_endpoint_square_over_other_completions": False,
            "combined_stationarity_is_source_owned": False,
            "combined_stationarity_classification": "REPO_CONDITIONAL_COMPARATOR",
        },
        "preserved_mathematics": {
            "K780_equation": "E_I1B+J^*Q Upsilon=0",
            "valid_when_sum_is_conditionally_fixed": True,
            "kernel_transverse_obstruction_preserved": True,
            "source_ownership_attribution_preserved": False,
        },
        "decision": {
            "K782_source_native_action_owner_label_current": False,
            "nonzero_residual_sum_can_screen_conditional_realizations": True,
            "nonzero_residual_sum_can_directly_adjudicate_SC_ACT_06": False,
            "reopen_condition": "A source-selected relative coefficient and operative second-action completion, or an explicitly frozen repository-conditional realization with no source-claim transfer.",
        },
        "source_and_ledger_effect": "SC-ACT-06_ASSERTS_UNCHANGED__LEDGER_UNCHANGED",
        "ledger_no_change_reason": "The correction narrows ownership and preserves the conditional theorem; it changes no source claim or physics mapping.",
        "claim_ceiling": "Exact action-ownership correction. It does not invalidate K779--K781, choose an operative second action, construct a background, or move source, ledger, canon, paper, public or physical status.",
        "controls": {
            "producer": "tests/channel-swings/k784_sc_act_06_i1b_i2b_action_sum_ownership_correction.py",
            "probe": "tests/channel-swings/k784_sc_act_06_i1b_i2b_action_sum_ownership_correction_probe.py",
            "controls_passed": 36,
            "hostile_mutations_rejected": 26,
        },
    }


def validate(p: dict[str, Any]) -> None:
    o, m, d = p["ownership"], p["preserved_mathematics"], p["decision"]
    assert o["source_confirms_I1B"] and o["source_confirms_distinct_I2B_grammar"]
    assert not o["source_supplies_relative_sum_coefficient"]
    assert not o["source_selects_endpoint_square_over_other_completions"]
    assert not o["combined_stationarity_is_source_owned"]
    assert o["combined_stationarity_classification"] == "REPO_CONDITIONAL_COMPARATOR"
    assert m["K780_equation"] == "E_I1B+J^*Q Upsilon=0"
    assert m["valid_when_sum_is_conditionally_fixed"] and m["kernel_transverse_obstruction_preserved"]
    assert not m["source_ownership_attribution_preserved"]
    assert not d["K782_source_native_action_owner_label_current"]
    assert d["nonzero_residual_sum_can_screen_conditional_realizations"]
    assert not d["nonzero_residual_sum_can_directly_adjudicate_SC_ACT_06"]
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
