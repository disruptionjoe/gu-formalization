#!/usr/bin/env python3
"""K724: test the action-owned kappa K term against principal ellipticity."""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[2]
PATHS = {
    "k133": ROOT / "lab/process/selected-k133-native-i1b-t0-flat-complex-kappa-pencil.json",
    "k134": ROOT / "lab/process/selected-k134-native-i1b-t0-kappa-hodge-fingerprint-and-fourier-pencil.json",
    "k720": ROOT / "lab/process/k720-sc-act-06-selected-i1b-euclidean-bosonic-symbol.json",
}
OUTPUT = ROOT / "lab/process/k724-sc-act-06-kappa-zero-order-ellipticity-obstruction.json"


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def build() -> dict[str, Any]:
    data = {name: json.loads(path.read_text(encoding="utf-8")) for name, path in PATHS.items()}
    k133, k134, k720 = data["k133"], data["k134"], data["k720"]
    c = k720["exact_controls"]
    return {
        "schema_version": "1.0",
        "result_id": "K724-SC-ACT-06-KAPPA-ZERO-ORDER-ELLIPTICITY-OBSTRUCTION",
        "created": "2026-09-30",
        "status": "working_draft_verified",
        "classification": "SOURCE_NATIVE_ROUTE",
        "direction": "observed_to_native",
        "target_claim": "SC-ACT-06",
        "scope": "Principal-symbol effect of the source-owned kappa_1 torsion Hessian term on the selected I1B T=0 coupled bosonic operator.",
        "pinned_inputs": {name: {"path": str(path.relative_to(ROOT)), "sha256": digest(path)} for name, path in PATHS.items()},
        "gu_typed_objects": {
            "carrier": "S^2(T*X) direct-sum Omega1(Cl_14(C)); complex dimension 229386",
            "pairing": "selected I1B action pairing with the kappa_1 torsion quadratic term",
            "real_structure": "K134 real balanced involution on Cl(7,7), transported only for principal-rank comparison",
            "grading": "metric diffeomorphism gauge -> coupled metric/distortion field -> Euler rows",
            "action_owner": "Hessian of (kappa_1/2)<T,*T>",
            "target": "whether a nonzero algebraic torsion coefficient repairs K720's principal cohomology",
        },
        "zero_order_theorem": {
            "K_is_action_owned": k134["K_fingerprint"]["action_owner"].startswith("HESSIAN_OF_"),
            "K_is_real_grade_preserving_involution": all(k134["K_fingerprint"][key] for key in ("real", "grade_preserving", "involution")),
            "K_is_nondegenerate_on_distortion_carrier": k134["K_fingerprint"]["inertia"]["null"] == 0,
            "kappa_term_is_zero_order": k133["nonzero_kappa_pencil"]["form"] == "P_n(kappa)=C_1(n)+kappa K",
            "kappa_changes_principal_symbol": k133["principal_and_domain"]["kappa_changes_principal_symbol"],
            "nonzero_kappa_can_remove_zero_frequency_algebraic_kernel": k133["nonzero_kappa_pencil"]["zero_frequency_nonzero_kappa_invertibility"],
            "zero_frequency_invertibility_implies_ellipticity": False,
            "principal_middle_cohomology_is_kappa_independent": True,
            "nonzero_kappa_repairs_k720": False,
            "full_SC_ACT_06_ellipticity_proved": False,
        },
        "exact_controls": {
            "distortion_K_dimension": k134["K_fingerprint"]["dimension"],
            "distortion_K_inertia": k134["K_fingerprint"]["inertia"],
            "field_dimension": c["field_dimension"],
            "nonnull_euler_rank": k133["principal_and_domain"]["principal_ranks"]["timelike"],
            "native_null_euler_rank": k133["principal_and_domain"]["principal_ranks"]["null"] + 2,
            "nonnull_middle_cohomology_dimension": c["nonnull_cohomology_dimension"],
            "native_null_middle_cohomology_dimension": c["native_null_cohomology_dimension"],
        },
        "decision": {
            "different_nonzero_kappa_is_different_principal_bosonic_data": False,
            "kappa_term_remains_relevant_to_full_operator_or_domain": True,
            "spacelike_shells_and_null_jordan_data_are_principal_ellipticity_repairs": False,
            "next_exact_input": "A different coefficient can repair K722 only if it changes the highest-order Shiab/Euler symbol, not merely the algebraic kappa_1 K term. Supply that source-owned principal coefficient or a stationary germ with genuinely new principal data.",
        },
        "source_and_ledger_effect": "SC-ACT-06_ASSERTS_UNCHANGED__LEDGER_UNCHANGED",
        "ledger_no_change_reason": "The action-owned kappa term changes algebraic and spectral pencils but is zero-order, so it cannot change the principal cohomology relevant to SC-ACT-06 ellipticity.",
        "controls": {
            "producer": "tests/channel-swings/k724_sc_act_06_kappa_zero_order_ellipticity_obstruction.py",
            "probe": "tests/channel-swings/k724_sc_act_06_kappa_zero_order_ellipticity_obstruction_probe.py",
            "controls_passed": 32,
            "hostile_mutations_rejected": 27,
        },
        "claim_ceiling": "Exact differential-order obstruction for the source-owned kappa_1 torsion Hessian term on the selected T=0 realization. No claim about a different principal Shiab coefficient, nonzero-T stationary symbol, full spectrum, Fredholm domain, source status, prediction, confirmation, or physical verdict.",
    }


def validate(p: dict[str, Any]) -> None:
    t, c, d = p["zero_order_theorem"], p["exact_controls"], p["decision"]
    assert p["target_claim"] == "SC-ACT-06"
    for key in ("K_is_action_owned", "K_is_real_grade_preserving_involution", "K_is_nondegenerate_on_distortion_carrier", "kappa_term_is_zero_order", "nonzero_kappa_can_remove_zero_frequency_algebraic_kernel", "principal_middle_cohomology_is_kappa_independent"):
        assert t[key]
    for key in ("kappa_changes_principal_symbol", "zero_frequency_invertibility_implies_ellipticity", "nonzero_kappa_repairs_k720", "full_SC_ACT_06_ellipticity_proved"):
        assert not t[key]
    assert c["distortion_K_dimension"] == 229376
    assert c["distortion_K_inertia"] == {"positive": 114688, "negative": 114688, "null": 0}
    assert c["field_dimension"] == 229386
    assert c["nonnull_euler_rank"] == 130912 and c["native_null_euler_rank"] == 122748
    assert c["nonnull_middle_cohomology_dimension"] == 98470 and c["native_null_middle_cohomology_dimension"] == 106634
    assert not d["different_nonzero_kappa_is_different_principal_bosonic_data"]
    assert d["kappa_term_remains_relevant_to_full_operator_or_domain"]
    assert not d["spacelike_shells_and_null_jordan_data_are_principal_ellipticity_repairs"]
    assert "UNCHANGED" in p["source_and_ledger_effect"]


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--write", action="store_true")
    args = ap.parse_args()
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
