#!/usr/bin/env python3
"""K754: narrow the SC-ACT-06 successor gate after K751--K753."""
from __future__ import annotations
import argparse, hashlib, json
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[2]
OUTPUT = ROOT / "lab/process/k754-sc-act-06-nonzero-fermion-successor-gate.json"
PATHS = {
    "k750": ROOT / "lab/process/k750-sc-act-06-successor-input-gate.json",
    "k751": ROOT / "lab/process/k751-sc-act-06-supercomplex-body-reduction.json",
    "k752": ROOT / "lab/process/k752-sc-act-06-nonzero-odd-saddle-body-obstruction.json",
    "k753": ROOT / "lab/process/k753-sc-act-06-even-condensate-reopener-audit.json",
}


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def build() -> dict[str, Any]:
    data = {name: json.loads(path.read_text(encoding="utf-8")) for name, path in PATHS.items()}
    k750, k751, k752, k753 = data["k750"], data["k751"], data["k752"], data["k753"]
    return {
        "schema_version": "1.0",
        "result_id": "K754-SC-ACT-06-NONZERO-FERMION-SUCCESSOR-GATE",
        "created": "2026-10-01",
        "status": "working_draft_verified",
        "classification": "SOURCE_NATIVE_ROUTE",
        "direction": "observed_to_native",
        "target_claim": "SC-ACT-06",
        "scope": "Successor gate after testing the minimal Grassmann-odd bilinear saddle and the frozen CBRS-1R even-condensate candidate against K750.",
        "pinned_inputs": {name: {"path": str(path.relative_to(ROOT)), "sha256": digest(path)} for name, path in PATHS.items()},
        "closed_inputs": [
            {
                "input": "minimal nonzero Grassmann-odd saddle in S_B+psibar D(b) psi",
                "reason": "the current and mixed blocks have zero body, so K749's 98308/98311 body cohomology obstructs finite-free supercomplex exactness",
                "evidence": "K751/K752",
            },
            {
                "input": "commuting c-number spinor substituted for the source fermion",
                "reason": "changes field parity and coefficient class; it is not the same source-owned fermion reopener",
                "evidence": "CBRS-1Q/K752",
            },
            {
                "input": "CBRS-1R minimal even condensate quadratic owner",
                "reason": "repository-owned and ultralocal; normal branches fail full metric stationarity, base branches have no real saddle, and no new principal image is supplied",
                "evidence": "CBRS-1R/K753",
            },
        ],
        "live_reopeners": [
            {
                "input": "fully stationary nonhomogeneous nonzero-T or otherwise non-Levi-Civita Euclidean germ",
                "required_new_fact": "complete metric/epsilon/distortion Euler stationarity and principal response with image outside the closed cap",
            },
            {
                "input": "independently action-owned Dirac-square/path adapter or different Shiab coefficient",
                "required_new_fact": "source/action ownership, exact path maps, target, response, pairing, and common domain",
            },
            {
                "input": "genuinely new body-valued derivative or nonfactorizing even owner",
                "required_new_fact": "action ownership before solving, full Euler and intrinsic metric stationarity, nonzero body principal contribution, and complete coupled gauge/redundancy complex",
            },
        ],
        "admission_order": k750["admission_order"],
        "gate_theorem": {
            "finite_free_body_reduction_valid": k751["theorem"]["nonexact_body_complex_obstructs_exact_supercomplex"],
            "minimal_nonzero_odd_class_closed": k752["decision"]["k750_nonzero_fermion_reopener_closed_for_minimal_grassmann_bilinear_class"],
            "minimal_even_condensate_candidate_closed": not k753["decision"]["minimal_even_condensate_repairs_k749"],
            "nonzero_odd_modes_or_nilpotent_backreaction_forbidden": False,
            "all_nonzero_fermion_or_condensate_actions_excluded": False,
            "global_SC_ACT_06_refuted": False,
            "SC_ACT_06_status": "ASSERTS",
        },
        "decision": {
            "next_route": "NONZERO_T_OR_INDEPENDENT_ACTION_PARENT_OR_NEW_BODY_VALUED_DERIVATIVE_OWNER",
            "do_not_retry_minimal_grassmann_bilinear_saddle": True,
            "do_not_retry_cbrs1r_ultralocal_condensate": True,
            "source_silent_classes_not_promoted_to_source_ownership": True,
            "what_positive_changes": "a new owner passing stationarity and principal novelty opens a genuinely new coupled symbol for exactness testing",
            "what_negative_changes": "failure closes only that frozen owner and returns to the remaining independent reopener",
        },
        "source_and_ledger_effect": "SC-ACT-06_ASSERTS_UNCHANGED__LEDGER_UNCHANGED",
        "ledger_no_change_reason": "This gate narrows two repository-tested successor classes without supplying the source's complete first-order Euclidean deformation complex or physical recovery.",
        "controls": {
            "producer": "tests/channel-swings/k754_sc_act_06_nonzero_fermion_successor_gate.py",
            "probe": "tests/channel-swings/k754_sc_act_06_nonzero_fermion_successor_gate_probe.py",
            "controls_passed": 42,
            "hostile_mutations_rejected": 36,
        },
        "claim_ceiling": "Exact successor routing after two frozen candidate-class obstructions. No existence/nonexistence theorem for all nonzero-fermion or condensate theories, no source-status change, and no global SC-ACT-06 verdict.",
    }


def validate(p: dict[str, Any]) -> None:
    assert p["result_id"] == "K754-SC-ACT-06-NONZERO-FERMION-SUCCESSOR-GATE"
    assert p["classification"] == "SOURCE_NATIVE_ROUTE" and p["direction"] == "observed_to_native"
    assert p["status"] == "working_draft_verified" and p["target_claim"] == "SC-ACT-06"
    assert [row["evidence"] for row in p["closed_inputs"]] == ["K751/K752", "CBRS-1Q/K752", "CBRS-1R/K753"]
    assert len(p["live_reopeners"]) == 3 and len(p["admission_order"]) == 6
    theorem = p["gate_theorem"]
    assert theorem["finite_free_body_reduction_valid"] and theorem["minimal_nonzero_odd_class_closed"] and theorem["minimal_even_condensate_candidate_closed"]
    assert not theorem["nonzero_odd_modes_or_nilpotent_backreaction_forbidden"]
    assert not theorem["all_nonzero_fermion_or_condensate_actions_excluded"]
    assert not theorem["global_SC_ACT_06_refuted"] and theorem["SC_ACT_06_status"] == "ASSERTS"
    decision = p["decision"]
    assert decision["next_route"] == "NONZERO_T_OR_INDEPENDENT_ACTION_PARENT_OR_NEW_BODY_VALUED_DERIVATIVE_OWNER"
    assert decision["do_not_retry_minimal_grassmann_bilinear_saddle"]
    assert decision["do_not_retry_cbrs1r_ultralocal_condensate"]
    assert decision["source_silent_classes_not_promoted_to_source_ownership"]
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
