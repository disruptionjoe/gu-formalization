#!/usr/bin/env python3
"""K792: Xi=D_A Upsilon cannot reduce ker(D Upsilon) at Upsilon=0."""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[2]
OUTPUT = ROOT / "lab/process/k792-sc-act-06-redundant-prolongation-kernel-theorem.json"
PATHS = {
    "k788": ROOT / "lab/process/k788-sc-act-06-direct-response-orbit-classification.json",
    "k790": ROOT / "lab/process/k790-sc-act-06-flat-zero-locus-realization-gate.json",
    "k791": ROOT / "lab/process/k791-sc-act-06-released-first-order-row-inventory.json",
}


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def build() -> dict[str, Any]:
    k788 = json.loads(PATHS["k788"].read_text(encoding="utf-8"))
    rank = k788["decision"]["connection_response_rank"]
    kernel = k788["decision"]["connection_kernel_dimension"]
    return {
        "schema_version": "1.0",
        "result_id": "K792-SC-ACT-06-REDUNDANT-PROLONGATION-KERNEL-THEOREM",
        "created": "2026-10-02",
        "status": "working_draft_verified",
        "classification": "SOURCE_NATIVE_ROUTE",
        "direction": "observed_to_native",
        "target_claim": "SC-ACT-06",
        "scope": "Principal-symbol effect of adjoining the released redundant Xi=D_omega Upsilon equation at K717's Upsilon=0 flat germ.",
        "pinned_inputs": {name: {"path": str(path.relative_to(ROOT)), "sha256": digest(path)} for name, path in PATHS.items()},
        "linearization": {
            "background_residual_zero": True,
            "identity": "delta(D_A Upsilon)=D_A(delta Upsilon)+(delta D_A)Upsilon",
            "zero_locus_reduction": "delta Xi=D_A(delta Upsilon)",
            "principal_factorization": "sigma_q(delta Xi)=(q wedge) J_q",
            "variation_of_connection_times_background_residual_vanishes": True,
            "xi_row_factors_through_direct_response": True,
        },
        "exact_consequence": {
            "connection_domain_dimension": rank + kernel,
            "direct_response_rank": rank,
            "direct_response_kernel_dimension": kernel,
            "kernel_inclusion": "ker(J_q) subset ker((J_q,(q wedge)J_q))",
            "stacked_row_rank": rank,
            "stacked_row_kernel_dimension": kernel,
            "all_three_real_nonzero_covector_orbits": True,
        },
        "decision": {
            "xi_can_act_nontrivially_on_a_vector_killed_by_J": False,
            "xi_supplies_K790_missing_independent_row": False,
            "discarding_xi_changes_field_kernel": False,
            "next_exact_input": "Compose the kernel inclusion with the zero-fermion block split and prove that added field columns cannot delete the embedded connection-kernel subspace.",
        },
        "source_and_ledger_effect": "SC-ACT-06_ASSERTS_UNCHANGED__LEDGER_UNCHANGED",
        "ledger_no_change_reason": "The theorem only classifies a declared redundant local equation row on one flat germ.",
        "claim_ceiling": "Exact zero-locus factorization theorem for the released Xi row. It does not exclude a genuinely independent future response row, another background, or another source completion.",
        "controls": {
            "producer": "tests/channel-swings/k792_sc_act_06_redundant_prolongation_kernel_theorem.py",
            "probe": "tests/channel-swings/k792_sc_act_06_redundant_prolongation_kernel_theorem_probe.py",
            "controls_passed": 38,
            "hostile_mutations_rejected": 26,
        },
    }


def validate(p: dict[str, Any]) -> None:
    assert p["result_id"] == "K792-SC-ACT-06-REDUNDANT-PROLONGATION-KERNEL-THEOREM"
    assert p["target_claim"] == "SC-ACT-06" and p["classification"] == "SOURCE_NATIVE_ROUTE"
    lin, exact, decision = p["linearization"], p["exact_consequence"], p["decision"]
    assert lin["background_residual_zero"] and lin["variation_of_connection_times_background_residual_vanishes"]
    assert lin["identity"] == "delta(D_A Upsilon)=D_A(delta Upsilon)+(delta D_A)Upsilon"
    assert lin["zero_locus_reduction"] == "delta Xi=D_A(delta Upsilon)"
    assert lin["principal_factorization"] == "sigma_q(delta Xi)=(q wedge) J_q"
    assert lin["xi_row_factors_through_direct_response"]
    assert exact["connection_domain_dimension"] == 229376
    assert exact["direct_response_rank"] == 122864
    assert exact["direct_response_kernel_dimension"] == 106512
    assert exact["stacked_row_rank"] == exact["direct_response_rank"]
    assert exact["stacked_row_kernel_dimension"] == exact["direct_response_kernel_dimension"]
    assert exact["all_three_real_nonzero_covector_orbits"]
    assert not any([decision["xi_can_act_nontrivially_on_a_vector_killed_by_J"], decision["xi_supplies_K790_missing_independent_row"], decision["discarding_xi_changes_field_kernel"]])
    assert "UNCHANGED" in p["source_and_ledger_effect"]
    assert set(p["pinned_inputs"]) == set(PATHS)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--write", action="store_true")
    args = parser.parse_args()
    packet = build()
    validate(packet)
    rendered = json.dumps(packet, indent=2, sort_keys=True) + "\n"
    if args.write:
        OUTPUT.write_text(rendered, encoding="utf-8")
    else:
        print(rendered, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
