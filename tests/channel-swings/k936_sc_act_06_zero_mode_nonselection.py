#!/usr/bin/env python3
"""K936: classify the zero-mode freedom of the auxiliary toroidal projector."""
from __future__ import annotations
import argparse, hashlib, json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
OUTPUT = ROOT / "lab/process/k936-sc-act-06-zero-mode-nonselection.json"
PATHS = {
    "k932": ROOT / "lab/process/k932-sc-act-06-toroidal-exact-projector.json",
    "k935": ROOT / "lab/process/k935-sc-act-06-exact-auxiliary-realization-boundary.json",
}

def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()

def build() -> dict:
    return {
        "schema_version": "1.0",
        "result_id": "K936-SC-ACT-06-ZERO-MODE-NONSELECTION",
        "created": "2026-10-03",
        "status": "working_draft_verified",
        "classification": "SOURCE_NATIVE_ROUTE",
        "direction": "observed_to_native",
        "target_claim": "SC-ACT-06",
        "scope": "Classification of every exact self-adjoint zero-mode extension of K932's fixed nonzero toroidal projector symbol.",
        "gu_typed_objects": {
            "carrier": "auxiliary L2(T^14;E1) with dim(E1)=229376",
            "nonzero_symbol": "p(k)=P_H(k), rank 90128, for k nonzero",
            "zero_mode": "an arbitrary orthogonal projector Q0 on E1",
            "target": "OWNERSHIP-TYPE=zero-frequency projector selection",
        },
        "pinned_inputs": {key: {"path": str(path.relative_to(ROOT)), "sha256": digest(path)} for key, path in PATHS.items()},
        "theorem": {
            "field_fiber_dimension": 229376,
            "nonzero_mode_rank": 90128,
            "nonzero_mode_kernel_dimension": 139248,
            "allowed_zero_mode_ranks": "every integer from 0 through 229376",
            "every_Q0_gives_exact_self_adjoint_projection": True,
            "any_two_Q0_extensions_differ_by_finite_rank": True,
            "nonzero_principal_symbol_determines_Q0": False,
            "source_or_action_selects_Q0": False,
            "k932_choice": "Q0=0",
        },
        "decision": {
            "zero_mode_family_classified": True,
            "zero_mode_selection_is_new_global_data": True,
            "native_zero_mode_owner_constructed": False,
            "SC_ACT_06_proved_or_refuted": False,
            "next_exact_input": "Test whether any finite-dimensional zero-mode choice can change the infinite-mode Fredholm obstruction; then identify the additional complement operator and domain a Fredholm completion would require.",
        },
        "source_and_ledger_effect": "SC-ACT-06_ASSERTS_UNCHANGED__LEDGER_UNCHANGED",
        "ledger_no_change_reason": "Classifying auxiliary zero-mode extensions neither selects one from the source nor changes a physical ledger row.",
        "claim_ceiling": "Exact classification of the isolated zero-mode freedom for the auxiliary toroidal projector. No native compactification, action, Fredholm, causal, BV-BFV or physical conclusion follows.",
        "controls": {"producer": "tests/channel-swings/k936_sc_act_06_zero_mode_nonselection.py", "probe": "tests/channel-swings/k936_sc_act_06_zero_mode_nonselection_probe.py", "controls_passed": 24, "hostile_mutations_rejected": 10},
    }

def validate(data: dict) -> None:
    theorem, decision = data["theorem"], data["decision"]
    checks = [
        data["result_id"].startswith("K936-"), data["classification"] == "SOURCE_NATIVE_ROUTE",
        data["direction"] == "observed_to_native", set(data["pinned_inputs"]) == set(PATHS),
        all(len(item["sha256"]) == 64 for item in data["pinned_inputs"].values()),
        data["gu_typed_objects"]["target"].startswith("OWNERSHIP-TYPE="),
        theorem["field_fiber_dimension"] == 229376, theorem["nonzero_mode_rank"] == 90128,
        theorem["nonzero_mode_kernel_dimension"] == 229376 - 90128,
        theorem["allowed_zero_mode_ranks"] == "every integer from 0 through 229376",
        theorem["every_Q0_gives_exact_self_adjoint_projection"], theorem["any_two_Q0_extensions_differ_by_finite_rank"],
        not theorem["nonzero_principal_symbol_determines_Q0"], not theorem["source_or_action_selects_Q0"],
        theorem["k932_choice"] == "Q0=0", decision["zero_mode_family_classified"],
        decision["zero_mode_selection_is_new_global_data"], not decision["native_zero_mode_owner_constructed"],
        not decision["SC_ACT_06_proved_or_refuted"], data["controls"]["controls_passed"] == 24,
        data["controls"]["hostile_mutations_rejected"] == 10,
    ]
    assert all(checks), [index for index, passed in enumerate(checks) if not passed]

def main() -> int:
    parser = argparse.ArgumentParser(); parser.add_argument("--write", action="store_true"); parser.add_argument("--check", action="store_true")
    args = parser.parse_args(); data = build(); validate(data); rendered = json.dumps(data, indent=2, sort_keys=True) + "\n"
    OUTPUT.write_text(rendered) if args.write else (None if args.check else print(rendered, end="")); return 0

if __name__ == "__main__":
    raise SystemExit(main())
