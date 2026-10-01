#!/usr/bin/env python3
"""K753: audit the frozen minimal even-condensate owner against K750."""
from __future__ import annotations
import argparse, hashlib, json
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[2]
OUTPUT = ROOT / "lab/process/k753-sc-act-06-even-condensate-reopener-audit.json"
PATHS = {
    "k750": ROOT / "lab/process/k750-sc-act-06-successor-input-gate.json",
    "cbrs1r": ROOT / "lab/process/selected-k77-cbrs1r-condensate-mass-owner.json",
}


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def build() -> dict[str, Any]:
    data = {name: json.loads(path.read_text(encoding="utf-8")) for name, path in PATHS.items()}
    k750, owner = data["k750"], data["cbrs1r"]
    formula = owner["frozen_action"]["formula"]
    derivative_tokens = ("dphi", "d_phi", "nabla", "partial", "derivative")
    derivative_free = not any(token in formula.lower() for token in derivative_tokens)
    return {
        "schema_version": "1.0",
        "result_id": "K753-SC-ACT-06-EVEN-CONDENSATE-REOPENER-AUDIT",
        "created": "2026-10-01",
        "status": "working_draft_verified",
        "classification": "INTERNAL_STRUCTURAL_ONLY",
        "direction": "observed_to_native",
        "target_claim": "SC-ACT-06",
        "scope": "The frozen repository-owned CBRS-1R action C3(T)+phi^2 Q2(T)+(phi^2-1)^2/4, audited only as a candidate body-valued escape from K752.",
        "pinned_inputs": {name: {"path": str(path.relative_to(ROOT)), "sha256": digest(path)} for name, path in PATHS.items()},
        "typed_objects": {
            "carrier": "CBRS-1R real J4 point carrier plus one body-valued even scalar",
            "pairing_or_form": formula,
            "real_structure": "real algebraic scalar and normalized real J4 branches",
            "grading": "scalar is even and is not a Grassmann-odd fermion",
            "action_owner": "repository construction, not source ownership",
            "target": "K750 full-stationarity and new-principal-image admission conditions",
        },
        "admission_audit": {
            "body_valued_even_owner": True,
            "same_class_as_source_fermion": False,
            "source_owned": False,
            "normal_j4_field_plus_condensate_saddles": owner["body_stationarity"]["normal_j4_real_saddles"],
            "base_j4_real_saddles": owner["body_stationarity"]["base_j4_real_saddles"],
            "full_metric_stationary_j4_bodies": owner["metric_variation"]["full_metric_stationary_j4_bodies"],
            "derivative_free_ultralocal_action": derivative_free,
            "new_principal_derivative_image": False,
            "passes_k750_stationarity_gate": False,
            "passes_k750_principal_novelty_gate": False,
        },
        "exact_controls": {
            "complete_tangent_dimension": owner["complete_tangent"]["dimension"],
            "complete_tangent_ranks": sorted(set(owner["complete_tangent"]["rank_per_real_saddle"].values())),
            "complete_tangent_nullities": sorted(set(owner["complete_tangent"]["nullity_per_real_saddle"].values())),
            "kernel": owner["complete_tangent"]["kernel"],
            "intrinsic_metric_row": owner["metric_variation"]["intrinsic_metric_row"],
        },
        "decision": {
            "minimal_even_condensate_repairs_k749": False,
            "reason": "Its real normal-J4 saddles fail the intrinsic metric equation, its base-J4 rays have no real saddle, and its derivative-free ultralocal scalar owner supplies no new principal image.",
            "next_even_owner_requirement": "Freeze a genuinely new action-owned derivative or nonfactorizing body-valued field before solving; require full Euler/MET(X) stationarity and a complete new principal map without fitted counterterms.",
            "nonzero_t_or_independent_action_parent_routes_remain_open": True,
        },
        "source_and_ledger_effect": "SC-ACT-06_ASSERTS_UNCHANGED__LEDGER_UNCHANGED",
        "ledger_no_change_reason": "The audit rejects one repository-owned ultralocal candidate as a reopener; it supplies no source-owned condensate or physical recovery.",
        "controls": {
            "producer": "tests/channel-swings/k753_sc_act_06_even_condensate_reopener_audit.py",
            "probe": "tests/channel-swings/k753_sc_act_06_even_condensate_reopener_audit_probe.py",
            "controls_passed": 38,
            "hostile_mutations_rejected": 32,
        },
        "claim_ceiling": "Exact reuse audit of CBRS-1R against K750. No theorem against all condensates, body-valued composites, derivative couplings, nonzero-T germs, or the global SC-ACT-06 claim.",
    }


def validate(p: dict[str, Any]) -> None:
    assert p["result_id"] == "K753-SC-ACT-06-EVEN-CONDENSATE-REOPENER-AUDIT"
    assert p["classification"] == "INTERNAL_STRUCTURAL_ONLY" and p["direction"] == "observed_to_native"
    assert p["status"] == "working_draft_verified" and p["target_claim"] == "SC-ACT-06"
    audit = p["admission_audit"]
    assert audit["body_valued_even_owner"] and not audit["same_class_as_source_fermion"] and not audit["source_owned"]
    assert audit["normal_j4_field_plus_condensate_saddles"] == 4 and audit["base_j4_real_saddles"] == 0
    assert audit["full_metric_stationary_j4_bodies"] == 0
    assert audit["derivative_free_ultralocal_action"] and not audit["new_principal_derivative_image"]
    assert not audit["passes_k750_stationarity_gate"] and not audit["passes_k750_principal_novelty_gate"]
    controls = p["exact_controls"]
    assert controls["complete_tangent_dimension"] == 230651
    assert controls["complete_tangent_ranks"] == [230611] and controls["complete_tangent_nullities"] == [40]
    assert controls["kernel"] == "EXACTLY_THE_40_DIMENSIONAL_BROKEN_DIAGONAL_SPIN_ORBIT"
    assert controls["intrinsic_metric_row"] == "NONZERO"
    decision = p["decision"]
    assert not decision["minimal_even_condensate_repairs_k749"]
    assert decision["nonzero_t_or_independent_action_parent_routes_remain_open"]
    assert "UNCHANGED" in p["source_and_ledger_effect"]


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--write", action="store_true")
    args = parser.parse_args()
    packet = build()
    validate(packet)
    rendered = json.dumps(packet, indent=2, sort_keys=True) + "\n"
    OUTPUT.write_text(rendered, encoding="utf-8") if args.write else print(rendered, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
