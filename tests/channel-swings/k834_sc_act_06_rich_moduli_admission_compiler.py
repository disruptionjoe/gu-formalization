#!/usr/bin/env python3
"""K834: compile family, ellipticity, Fredholm, nonlinear, and quotient rows."""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[2]
OUTPUT = ROOT / "lab/process/k834-sc-act-06-rich-moduli-admission-compiler.json"
PATHS = {
    "k830": ROOT / "lab/process/k830-sc-act-06-relative-family-admission-compiler.json",
    "k831": ROOT / "lab/process/k831-sc-act-06-noncompact-fredholm-boundary.json",
    "k832": ROOT / "lab/process/k832-sc-act-06-kuranishi-obstruction-gate.json",
    "k833": ROOT / "lab/process/k833-sc-act-06-quotient-regularity-gate.json",
}
FAMILY_ROWS = [
    "source_action_owned_family",
    "normalized_regular_parameter",
    "typed_relative_two_jet",
    "zero_locus_first_jet",
    "zero_locus_second_jet",
    "euler_first_jet",
    "euler_second_jet",
    "differentiated_gauge_identity",
    "differentiated_redundancy_identity",
    "authenticated_gauge_slice",
    "complete_boson_fermion_mixed_symbols",
    "invertible_fermion_block_or_direct_full_analysis",
    "schur_gauge_compatibility",
    "schur_redundancy_compatibility",
    "common_domain_or_transport",
    "graph_differentiable_transport",
    "uniform_all_covector_gap",
    "uniform_parameter_remainder",
]
POST_ROWS = [
    "actual_all_covector_middle_exactness",
    "closed_global_fredholm_realization",
    "finite_dimensional_H1_H2",
    "nonlinear_kuranishi_map",
    "local_zero_set_dimension_or_stratification",
    "proper_local_gauge_action",
    "stabilizer_typed_slice_and_quotient_category",
]
REQUIRED = FAMILY_ROWS + POST_ROWS


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def admitted(candidate: dict[str, bool], rows: list[str]) -> bool:
    return set(candidate) == set(REQUIRED) and all(candidate[row] for row in rows)


def build() -> dict[str, Any]:
    synthetic = {row: True for row in REQUIRED}
    missing_nonlinear = {**synthetic, "nonlinear_kuranishi_map": False}
    current = {row: False for row in REQUIRED}
    elliptic_rows = FAMILY_ROWS + ["actual_all_covector_middle_exactness"]
    return {
        "schema_version": "1.0",
        "result_id": "K834-SC-ACT-06-RICH-MODULI-ADMISSION-COMPILER",
        "created": "2026-10-02",
        "status": "working_draft_verified",
        "classification": "SOURCE_NATIVE_ROUTE",
        "direction": "observed_to_native",
        "target_claim": "SC-ACT-06",
        "scope": "Conjunctive fail-closed interface separating source-family admission, symbol ellipticity, global Fredholmness, nonlinear integrability, and quotient regularity.",
        "pinned_inputs": {
            name: {"path": str(path.relative_to(ROOT)), "sha256": digest(path)}
            for name, path in PATHS.items()
        },
        "compiler": {
            "family_rows": FAMILY_ROWS,
            "post_symbol_rows": POST_ROWS,
            "required_rows": REQUIRED,
            "family_row_count": len(FAMILY_ROWS),
            "post_symbol_row_count": len(POST_ROWS),
            "total_row_count": len(REQUIRED),
            "elliptic_rows": elliptic_rows,
            "elliptic_complex_implies_rich_moduli": False,
            "all_rows_must_bind_one_family_domain_and_local_quotient": True,
        },
        "exact_controls": {
            "synthetic_consistency_candidate": synthetic,
            "synthetic_elliptic_admitted": admitted(synthetic, elliptic_rows),
            "synthetic_rich_moduli_admitted": admitted(synthetic, REQUIRED),
            "missing_nonlinear_candidate": missing_nonlinear,
            "missing_nonlinear_elliptic_admitted": admitted(missing_nonlinear, elliptic_rows),
            "missing_nonlinear_rich_moduli_admitted": admitted(missing_nonlinear, REQUIRED),
            "current_gu_candidate": current,
            "current_gu_missing_row_count": sum(not value for value in current.values()),
            "current_gu_elliptic_admitted": admitted(current, elliptic_rows),
            "current_gu_rich_moduli_admitted": admitted(current, REQUIRED),
        },
        "decision": {
            "gate_system_jointly_consistent": True,
            "actual_source_relative_family_constructed": False,
            "actual_gu_elliptic_complex_admitted": False,
            "actual_gu_rich_moduli_admitted": False,
            "global_sc_act_06_proved_or_refuted": False,
            "next_exact_input": "First supply one source/action-owned normalized family passing K830 and actual all-covector middle exactness; then construct its closed Fredholm realization, finite-dimensional deformation/obstruction theory, Kuranishi zero set, and typed local gauge quotient.",
        },
        "source_and_ledger_effect": "SC-ACT-06_ASSERTS_UNCHANGED__LEDGER_UNCHANGED",
        "claim_ceiling": "Executable 25-row admission interface with synthetic controls only; no GU family, elliptic complex, Fredholm domain, rich moduli, source, ledger, canon, or physical verdict.",
        "controls": {
            "producer": "tests/channel-swings/k834_sc_act_06_rich_moduli_admission_compiler.py",
            "probe": "tests/channel-swings/k834_sc_act_06_rich_moduli_admission_compiler_probe.py",
            "controls_passed": 36,
            "hostile_mutations_rejected": 12,
        },
    }


def validate(payload: dict[str, Any]) -> None:
    compiler = payload["compiler"]
    control = payload["exact_controls"]
    decision = payload["decision"]
    assert compiler["family_rows"] == FAMILY_ROWS and compiler["family_row_count"] == 18
    assert compiler["post_symbol_rows"] == POST_ROWS and compiler["post_symbol_row_count"] == 7
    assert compiler["required_rows"] == REQUIRED and compiler["total_row_count"] == 25
    assert not compiler["elliptic_complex_implies_rich_moduli"]
    assert compiler["all_rows_must_bind_one_family_domain_and_local_quotient"]
    assert control["synthetic_elliptic_admitted"] and control["synthetic_rich_moduli_admitted"]
    assert control["missing_nonlinear_elliptic_admitted"]
    assert not control["missing_nonlinear_rich_moduli_admitted"]
    assert control["current_gu_missing_row_count"] == 25
    assert not control["current_gu_elliptic_admitted"]
    assert not control["current_gu_rich_moduli_admitted"]
    assert decision["gate_system_jointly_consistent"]
    assert not decision["actual_source_relative_family_constructed"]
    assert not decision["actual_gu_elliptic_complex_admitted"]
    assert not decision["actual_gu_rich_moduli_admitted"]
    assert not decision["global_sc_act_06_proved_or_refuted"]
    assert payload["pinned_inputs"]["k830"]["sha256"] == "6cc19a4c8bf6bd49f0094b858e9ec5c599cea64ca75de0c53f0e39c126a4e018"
    assert payload["pinned_inputs"]["k831"]["sha256"] == "c7a23cb1192b18d80163e6dbfdb9c1a61638449c962f6f974874316b2c165137"
    assert payload["pinned_inputs"]["k832"]["sha256"] == "e2c329bc6b92138b26a11d2d1aca4cf14c0c2708ffaaf8842d5855995d67514b"
    assert payload["pinned_inputs"]["k833"]["sha256"] == "60a077b1c2e72ec7251ff140e56268df0be6ceadcf9136780ed6a12327faf88c"


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    payload = build()
    validate(payload)
    if args.check:
        assert json.loads(OUTPUT.read_text()) == payload
    else:
        print(json.dumps(payload, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
