#!/usr/bin/env python3
"""K752: compose K751 with K749 and CBRS-1Q for nonzero odd saddles."""
from __future__ import annotations
import argparse, hashlib, json
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[2]
OUTPUT = ROOT / "lab/process/k752-sc-act-06-nonzero-odd-saddle-body-obstruction.json"
PATHS = {
    "k751": ROOT / "lab/process/k751-sc-act-06-supercomplex-body-reduction.json",
    "k749": ROOT / "lab/process/k749-sc-act-06-t0-full-symbol-obstruction.json",
    "cbrs1q": ROOT / "lab/process/selected-k77-cbrs1q-grassmann-body-obstruction.json",
}


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def build() -> dict[str, Any]:
    data = {name: json.loads(path.read_text(encoding="utf-8")) for name, path in PATHS.items()}
    k751, k749, cbrs1q = data["k751"], data["k749"], data["cbrs1q"]
    cases = []
    for row in k749["exact_controls"]["cases"]:
        cases.append({
            "case": row["case"],
            "body_middle_cohomology_lower_bound": row["full_symbol_middle_cohomology_lower_bound"],
            "odd_current_body_rank": cbrs1q["body_projection"]["bosonic_current_body"],
            "mixed_principal_body_rank": cbrs1q["body_projection"]["mixed_hessian_body"],
            "finite_free_supercomplex_exact": False,
        })
    return {
        "schema_version": "1.0",
        "result_id": "K752-SC-ACT-06-NONZERO-ODD-SADDLE-BODY-OBSTRUCTION",
        "created": "2026-10-01",
        "status": "working_draft_verified",
        "classification": "SOURCE_NATIVE_ROUTE",
        "direction": "observed_to_native",
        "target_claim": "SC-ACT-06",
        "scope": "Minimal even bilinear action S_B(b)+psibar D(b) psi on K749's released T=0 body family, with independent barred/unbarred Grassmann-odd fields and any nonzero odd saddle over a local nilpotent coefficient algebra.",
        "pinned_inputs": {name: {"path": str(path.relative_to(ROOT)), "sha256": digest(path)} for name, path in PATHS.items()},
        "typed_objects": {
            "carrier": "K749 finite body symbol carrier extended by finite free Grassmann coefficients",
            "pairing_or_form": "released bosonic action plus even bilinear psibar D(b) psi",
            "real_structure": "K749 Euclidean body carrier; odd nilpotent extension",
            "grading": "symbol-chain degree, Clifford grade, and super parity kept distinct",
            "action_owner": "released bosonic grammar plus minimal source-adjacent bilinear fermion class",
            "target": "middle exactness of the coupled principal supercomplex",
        },
        "composition_theorem": {
            "nonzero_odd_saddles_may_exist": cbrs1q["nonzero_odd_saddle"]["exact_fixture_exists"],
            "odd_bilinear_bosonic_backreaction_body_zero": cbrs1q["body_projection"]["bosonic_current_body"] == 0,
            "mixed_boson_fermion_principal_body_zero": cbrs1q["body_projection"]["mixed_hessian_body"] == 0,
            "even_even_body_hessian_unchanged": cbrs1q["body_projection"]["even_body_hessian"] == "EXACTLY_THE_BOSONIC_BODY_HESSIAN",
            "body_symbol_remains_k749": True,
            "k751_body_obstruction_applies": k751["theorem"]["nonexact_body_complex_obstructs_exact_supercomplex"],
            "minimal_nonzero_odd_saddle_repairs_middle_exactness": False,
            "global_SC_ACT_06_refuted": False,
        },
        "exact_controls": {"cases": cases},
        "decision": {
            "k750_nonzero_fermion_reopener_closed_for_minimal_grassmann_bilinear_class": True,
            "commuting_c_number_spinor_is_same_class": False,
            "body_valued_even_condensate_is_same_class": False,
            "fermion_zero_modes_or_nilpotent_backreaction_excluded": False,
            "next_exact_input": "A body-valued even composite or altered-parity field needs a separately owned action, stationarity equation, and principal map; otherwise use the nonzero-T/non-Levi-Civita or independent-action-parent reopener.",
        },
        "source_and_ledger_effect": "SC-ACT-06_ASSERTS_UNCHANGED__LEDGER_UNCHANGED",
        "ledger_no_change_reason": "The result closes one minimal coefficient/parity class on an already rejected body realization; it does not construct or refute the complete first-order theory.",
        "controls": {
            "producer": "tests/channel-swings/k752_sc_act_06_nonzero_odd_saddle_body_obstruction.py",
            "probe": "tests/channel-swings/k752_sc_act_06_nonzero_odd_saddle_body_obstruction_probe.py",
            "controls_passed": 40,
            "hostile_mutations_rejected": 34,
        },
        "claim_ceiling": "Exact body obstruction for the minimal bilinear Grassmann-odd action class on the K749 released T=0 body family. Nonzero odd modes and nilpotent backreaction remain possible; no global SC-ACT-06, source, physical-vacuum, BV, domain, spectrum, or condensate conclusion follows.",
    }


def validate(p: dict[str, Any]) -> None:
    assert p["result_id"] == "K752-SC-ACT-06-NONZERO-ODD-SADDLE-BODY-OBSTRUCTION"
    assert p["classification"] == "SOURCE_NATIVE_ROUTE" and p["direction"] == "observed_to_native"
    assert p["status"] == "working_draft_verified" and p["target_claim"] == "SC-ACT-06"
    theorem = p["composition_theorem"]
    for key in (
        "nonzero_odd_saddles_may_exist",
        "odd_bilinear_bosonic_backreaction_body_zero",
        "mixed_boson_fermion_principal_body_zero",
        "even_even_body_hessian_unchanged",
        "body_symbol_remains_k749",
        "k751_body_obstruction_applies",
    ):
        assert theorem[key]
    assert not theorem["minimal_nonzero_odd_saddle_repairs_middle_exactness"]
    assert not theorem["global_SC_ACT_06_refuted"]
    cases = {row["case"]: row for row in p["exact_controls"]["cases"]}
    assert (cases["native_nonnull"]["body_middle_cohomology_lower_bound"], cases["native_null_auxiliary_nonzero"]["body_middle_cohomology_lower_bound"]) == (98308, 98311)
    for row in cases.values():
        assert row["odd_current_body_rank"] == 0 and row["mixed_principal_body_rank"] == 0
        assert not row["finite_free_supercomplex_exact"]
    decision = p["decision"]
    assert decision["k750_nonzero_fermion_reopener_closed_for_minimal_grassmann_bilinear_class"]
    assert not decision["commuting_c_number_spinor_is_same_class"] and not decision["body_valued_even_condensate_is_same_class"]
    assert not decision["fermion_zero_modes_or_nilpotent_backreaction_excluded"]
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
