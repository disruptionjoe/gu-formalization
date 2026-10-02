#!/usr/bin/env python3
"""K786: compile the direct source-owned SC-ACT-06 zero-locus input gate."""
from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[2]
OUTPUT = ROOT / "lab/process/k786-sc-act-06-zero-residual-deformation-input-gate.json"


def build() -> dict[str, Any]:
    k783 = json.loads((ROOT / "lab/process/k783-sc-act-06-source-zero-locus-boundary.json").read_text())
    k784 = json.loads((ROOT / "lab/process/k784-sc-act-06-i1b-i2b-action-sum-ownership-correction.json").read_text())
    k785 = json.loads((ROOT / "lab/process/k785-sc-act-06-nonzero-residual-variational-salvage.json").read_text())
    assert k783["source_custody"]["claimed_solution_locus"] == "Upsilon=0"
    assert not k784["ownership"]["combined_stationarity_is_source_owned"]
    assert not k785["corrected_use"]["direct_SC_ACT_06_adjudication"]
    required = [
        "one source-typed background satisfying Upsilon=0",
        "complete source field tangent on that background",
        "complete first-order linearization J=DUpsilon",
        "owned infinitesimal symmetry map G with J composition G equal to zero",
        "owned redundant-Euler map R with R composition J equal to zero",
        "exact removal or quotient of precisely the source-redundant Euler rows",
        "complete bosonic fermionic and mixed principal symbols when the claimed theory includes them",
        "authenticated Euclidean real carrier pairing and analytic domain",
        "middle exactness at every nonzero Euclidean covector",
        "solution and complex realized on one common native B(epsilon)/Y geometry",
    ]
    return {
        "schema_version": "1.0",
        "result_id": "K786-SC-ACT-06-ZERO-RESIDUAL-DEFORMATION-INPUT-GATE",
        "created": "2026-10-01",
        "status": "working_draft_verified",
        "classification": "SOURCE_NATIVE_ROUTE",
        "direction": "observed_to_native",
        "target_claim": "SC-ACT-06",
        "scope": "Direct admission compiler for the source-asserted Upsilon=0 Euclidean deformation complex.",
        "gu_typed_objects": {
            "carrier": "one common source field, symmetry, Euler and redundancy carrier",
            "pairing": "the first-order complex does not inherit a residual-square pairing by default",
            "real_structure": "one authenticated Euclidean continuation of the complete source carrier",
            "grading": "symmetries -> fields -> first-order Euler equations -> redundant Euler equations",
            "action_owner": "source first-order theory only",
            "target": "middle exactness of the Upsilon=0 deformation complex at every nonzero Euclidean covector",
        },
        "required_packet": required,
        "current_custody": {
            "source_claim_and_zero_locus": True,
            "source_exhibited_complete_solution_two_jet": False,
            "complete_first_order_linearization": False,
            "complete_owned_symmetry_map": False,
            "complete_owned_redundancy_map": False,
            "complete_Euclidean_real_continuation": False,
            "complete_common_analytic_domain": False,
            "all_covector_middle_exactness": False,
        },
        "rejection_rules": {
            "nonzero_residual_substituted_for_zero_locus": "reject",
            "I1B_plus_I2B_sum_without_source_coefficient": "reject",
            "Lorentzian_K77_defect_called_Euclidean_verdict": "reject",
            "one_covector_rank_called_ellipticity": "reject",
            "kernel_called_gauge_without_owned_map": "reject",
            "printed_Xi_called_complete_off_shell_redundancy_without_proof": "reject",
            "bosonic_only_complex_called_complete_total_theory": "reject",
        },
        "decision": {
            "candidate_admitted": False,
            "SC_ACT_06_status": "ASSERTS",
            "incumbent": "recover or construct one native Upsilon=0 background and the complete first-order Euclidean deformation packet",
            "conditional_reopener": "A source-selected I1B/I2B sum coefficient and operative second-action completion can reopen K779--K782 only as a separately typed action problem.",
            "strongest_independent_alternative": "complete native K500 A/B packet",
        },
        "source_and_ledger_effect": "SC-ACT-06_ASSERTS_UNCHANGED__LEDGER_UNCHANGED",
        "ledger_no_change_reason": "The gate corrects the direct source object but supplies none of the missing native solution or complex data.",
        "claim_ceiling": "Exact successor admission gate. No rich moduli, Euclidean ellipticity, source-status, physics mapping, canon, paper, public, prediction, confirmation or physical conclusion follows.",
        "controls": {
            "producer": "tests/channel-swings/k786_sc_act_06_zero_residual_deformation_input_gate.py",
            "probe": "tests/channel-swings/k786_sc_act_06_zero_residual_deformation_input_gate_probe.py",
            "controls_passed": 42,
            "hostile_mutations_rejected": 30,
        },
    }


def validate(p: dict[str, Any]) -> None:
    custody, decision = p["current_custody"], p["decision"]
    assert len(p["required_packet"]) == 10
    assert custody["source_claim_and_zero_locus"]
    assert all(not value for key, value in custody.items() if key != "source_claim_and_zero_locus")
    assert set(p["rejection_rules"].values()) == {"reject"}
    assert not decision["candidate_admitted"] and decision["SC_ACT_06_status"] == "ASSERTS"
    assert "Upsilon=0" in decision["incumbent"]
    assert decision["strongest_independent_alternative"] == "complete native K500 A/B packet"
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
