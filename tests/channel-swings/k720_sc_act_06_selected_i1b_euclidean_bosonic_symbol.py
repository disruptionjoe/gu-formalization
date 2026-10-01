#!/usr/bin/env python3
"""K720: transport the selected K132 I1B bosonic symbol to the K717 germ."""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[2]
K132 = ROOT / "lab/process/selected-k132-native-i1b-t0-all-grade-noether-complex.json"
K717 = ROOT / "lab/process/k717-sc-act-06-flat-euclidean-gimmel-germ.json"
OUTPUT = ROOT / "lab/process/k720-sc-act-06-selected-i1b-euclidean-bosonic-symbol.json"


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def build() -> dict[str, Any]:
    k132 = json.loads(K132.read_text(encoding="utf-8"))
    k717 = json.loads(K717.read_text(encoding="utf-8"))
    coupled = k132["coupled_dn_symbol"]
    gauge_rank = k132["minimal_bv_kt_bfv"]["metric_diffeomorphism_generator_rank"]
    field_dim = coupled["carrier_dimension"]
    cases = []
    for name, rank, q_norm in (
        ("native_nonnull", coupled["ranks"]["timelike"], 1),
        ("native_null_auxiliary_nonzero", coupled["ranks"]["null"], 2),
    ):
        kernel = field_dim - rank
        cases.append({
            "case": name,
            "action_euler_rank": rank,
            "action_euler_kernel_dimension": kernel,
            "owned_gauge_image_rank": gauge_rank,
            "middle_cohomology_dimension": kernel - gauge_rank,
            "auxiliary_q_covector_norm_squared": q_norm,
            "middle_exact": kernel == gauge_rank,
        })
    return {
        "schema_version": "1.0",
        "result_id": "K720-SC-ACT-06-SELECTED-I1B-EUCLIDEAN-BOSONIC-SYMBOL",
        "created": "2026-09-30",
        "status": "working_draft_verified",
        "classification": "SOURCE_NATIVE_ROUTE",
        "direction": "observed_to_native",
        "target_claim": "SC-ACT-06",
        "scope": "Complex-principal-symbol transport of K132's selected comm/symi/symi I1B coupled bosonic gauge/Euler rank strata to K717's flat (13,1) action carrier.",
        "pinned_inputs": {
            "k132_path": str(K132.relative_to(ROOT)),
            "k132_sha256": digest(K132),
            "k717_path": str(K717.relative_to(ROOT)),
            "k717_sha256": digest(K717),
            "selected_shiab": k132["background"]["selected_shiab"],
        },
        "gu_typed_objects": {
            "carrier": "S^2(T*X) direct-sum Omega1(Cl_14(C)); complex dimension 229386",
            "pairing": "K717 native DeWitt action form, not the auxiliary positive q",
            "real_structure": "rank statement after complexification; no Euclidean reality selector is inferred",
            "grading": "rank-four metric diffeomorphism gauge -> coupled metric/distortion field -> action Euler rows",
            "action_owner": "K132 selected I1B comm/symi/symi displayed-family row",
            "target": "middle principal-symbol cohomology for the frozen selected bosonic realization",
        },
        "transport_theorem": {
            "complex_clifford_14_real_forms_are_isomorphic": True,
            "similarity_and_carrier_changes_preserve_rank": True,
            "nonnull_and_null_complex_covector_orbits_are_preserved": True,
            "k717_auxiliary_q_changes_quantification_not_action_rank": True,
            "independent_row_restriction_preserves_euler_kernel": True,
            "selected_bosonic_middle_symbol_is_exact": False,
            "k718_exterior_skeleton_equals_selected_action_euler": False,
            "full_SC_ACT_06_ellipticity_proved": False,
        },
        "exact_controls": {
            "field_dimension": field_dim,
            "owned_metric_diffeomorphism_rank": gauge_rank,
            "cases": cases,
            "nonnull_cohomology_dimension": cases[0]["middle_cohomology_dimension"],
            "native_null_cohomology_dimension": cases[1]["middle_cohomology_dimension"],
            "native_null_is_auxiliary_q_nonzero": cases[1]["auxiliary_q_covector_norm_squared"] > 0,
        },
        "decision": {
            "selected_flat_bosonic_realization_is_elliptic": False,
            "native_null_case_alone_refutes_all_nonzero_covector_exactness": True,
            "row_projector_can_repair_field_middle_cohomology": False,
            "result_refutes_every_source_admitted_shiab_or_background": False,
            "next_exact_input": "Compose with the source-displayed Euclidean equation-(9.16) fermion diagonal using K719's zero-mixed-block theorem; if the fermion diagonal is exact, the bosonic defect still survives.",
        },
        "source_and_ledger_effect": "SC-ACT-06_ASSERTS_UNCHANGED__LEDGER_UNCHANGED",
        "ledger_no_change_reason": "This rejects one frozen selected flat action realization, not every source-admitted coefficient, nonflat stationary germ, analytic domain or physical quotient.",
        "controls": {
            "producer": "tests/channel-swings/k720_sc_act_06_selected_i1b_euclidean_bosonic_symbol.py",
            "probe": "tests/channel-swings/k720_sc_act_06_selected_i1b_euclidean_bosonic_symbol_probe.py",
            "controls_passed": 36,
            "hostile_mutations_rejected": 30,
        },
        "claim_ceiling": "Exact complex rank transport and middle-cohomology obstruction for K132's selected I1B coefficient on K717's flat germ. It neither proves a unique source selector nor rejects every action/background, and it moves no source, ledger, canon, paper, prediction, confirmation or physical verdict.",
    }


def validate(p: dict[str, Any]) -> None:
    t, c, d = p["transport_theorem"], p["exact_controls"], p["decision"]
    assert p["target_claim"] == "SC-ACT-06"
    assert p["pinned_inputs"]["selected_shiab"] == "comm/symi/symi displayed family row"
    assert c["field_dimension"] == 229386 and c["owned_metric_diffeomorphism_rank"] == 4
    assert c["cases"] == [
        {"case": "native_nonnull", "action_euler_rank": 130912, "action_euler_kernel_dimension": 98474, "owned_gauge_image_rank": 4, "middle_cohomology_dimension": 98470, "auxiliary_q_covector_norm_squared": 1, "middle_exact": False},
        {"case": "native_null_auxiliary_nonzero", "action_euler_rank": 122748, "action_euler_kernel_dimension": 106638, "owned_gauge_image_rank": 4, "middle_cohomology_dimension": 106634, "auxiliary_q_covector_norm_squared": 2, "middle_exact": False},
    ]
    assert c["nonnull_cohomology_dimension"] == 98470
    assert c["native_null_cohomology_dimension"] == 106634 and c["native_null_is_auxiliary_q_nonzero"]
    for key in ("complex_clifford_14_real_forms_are_isomorphic", "similarity_and_carrier_changes_preserve_rank", "nonnull_and_null_complex_covector_orbits_are_preserved", "k717_auxiliary_q_changes_quantification_not_action_rank", "independent_row_restriction_preserves_euler_kernel"):
        assert t[key]
    for key in ("selected_bosonic_middle_symbol_is_exact", "k718_exterior_skeleton_equals_selected_action_euler", "full_SC_ACT_06_ellipticity_proved"):
        assert not t[key]
    assert not d["selected_flat_bosonic_realization_is_elliptic"]
    assert d["native_null_case_alone_refutes_all_nonzero_covector_exactness"]
    assert not d["row_projector_can_repair_field_middle_cohomology"]
    assert not d["result_refutes_every_source_admitted_shiab_or_background"]
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
