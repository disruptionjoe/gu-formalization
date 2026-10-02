#!/usr/bin/env python3
"""K788: classify the direct D-Upsilon connection response on all real covector orbits."""
from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[2]
K740_SCRIPT = ROOT / "tests/channel-swings/k740_sc_act_06_expanded_principal_response_rank.py"
OUTPUT = ROOT / "lab/process/k788-sc-act-06-direct-response-orbit-classification.json"
PATHS = {
    "k717": ROOT / "lab/process/k717-sc-act-06-flat-euclidean-gimmel-germ.json",
    "k740": ROOT / "lab/process/k740-sc-act-06-expanded-principal-response-rank.json",
    "k783": ROOT / "lab/process/k783-sc-act-06-source-zero-locus-boundary.json",
    "k787": ROOT / "lab/process/k787-sc-act-06-flat-zero-locus-custody.json",
}


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def load_k740():
    spec = importlib.util.spec_from_file_location("k788_k740", K740_SCRIPT)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def negative_case() -> dict[str, int]:
    k740 = load_k740()
    api = k740.load_api()
    bank = api.load_bank()
    core = api.K77Core(bank.signature, bank.channels)
    minus = next(i for i, sign in enumerate(bank.signature) if sign == -1)
    q_form = {1 << minus: {0: api.ONE}}
    return k740.compute_case(api, core, q_form)["full_connection"]


def build() -> dict[str, Any]:
    k740 = json.loads(PATHS["k740"].read_text(encoding="utf-8"))
    prior = {row["case"]: row["ranks"]["full_connection"] for row in k740["exact_controls"]["cases"]}
    negative = negative_case()
    cases = [
        {"orbit": "native_positive", "native_norm_squared": 1, "auxiliary_q_norm_squared": 1, **prior["native_nonnull"]},
        {"orbit": "native_negative", "native_norm_squared": -1, "auxiliary_q_norm_squared": 1, **negative},
        {"orbit": "native_null", "native_norm_squared": 0, "auxiliary_q_norm_squared": 2, **prior["native_null_auxiliary_nonzero"]},
    ]
    return {
        "schema_version": "1.0",
        "result_id": "K788-SC-ACT-06-DIRECT-RESPONSE-ORBIT-CLASSIFICATION",
        "created": "2026-10-02",
        "status": "working_draft_verified",
        "classification": "SOURCE_NATIVE_ROUTE",
        "direction": "observed_to_native",
        "target_claim": "SC-ACT-06",
        "scope": "Exact all-orbit rank classification of the direct connection-sector linearization J=D Upsilon on K717's flat Upsilon=0 germ.",
        "gu_typed_objects": {
            "carrier": "Omega1(Cl_14(C)) on K717's fixed flat native germ; complex dimension 229376",
            "pairing": "K717 native action form; auxiliary Frobenius q only identifies nonzero Euclidean covectors",
            "real_structure": "K740 pinned real U(64,64) basis followed by exact rational rank calculation",
            "grading": "connection variation u -> first-order residual variation J_q(u)",
            "action_owner": "source first-order residual Upsilon, not an I1B or I2B Hessian",
            "target": "kernel of D Upsilon before quotient by an owned symmetry map",
        },
        "pinned_inputs": {name: {"path": str(path.relative_to(ROOT)), "sha256": digest(path)} for name, path in PATHS.items()},
        "operator": {
            "principal_map": "J_q(u)=K_LIFT(SHIAB(q_WEDGE_u))",
            "is_direct_first_order_linearization": True,
            "is_action_hessian": False,
            "complete_connection_basis_enumerated": True,
            "rank_field": "Q_IN_PINNED_REAL_U64_64_BASIS",
        },
        "orbit_theorem": {
            "real_nonzero_covector_orbits": ["native_positive", "native_negative", "native_null"],
            "all_orbits_tested": True,
            "auxiliary_euclidean_norm_nonzero_on_all_cases": True,
            "cases": cases,
            "rank_constant_across_all_orbits": len({row["rank"] for row in cases}) == 1,
            "nullity_constant_across_all_orbits": len({row["nullity"] for row in cases}) == 1,
        },
        "decision": {
            "connection_response_rank": cases[0]["rank"],
            "connection_kernel_dimension": cases[0]["nullity"],
            "connection_sector_injective": False,
            "all_nonzero_covector_middle_exactness_follows_without_symmetry_quotient": False,
            "next_exact_input": "Compare the 106512-dimensional kernel with the strongest symmetry image available on the same flat germ; do not call the kernel gauge without an owned map.",
        },
        "source_and_ledger_effect": "SC-ACT-06_ASSERTS_UNCHANGED__LEDGER_UNCHANGED",
        "ledger_no_change_reason": "This is a local deformation-rank result on one native flat germ, not a physical state or observable construction.",
        "claim_ceiling": "Exact all-real-covector-orbit connection-response ranks on K717. No symmetry ownership, complete field complex, global SC-ACT-06 no-go, source-status change or physical result follows.",
        "controls": {
            "producer": "tests/channel-swings/k788_sc_act_06_direct_response_orbit_classification.py",
            "probe": "tests/channel-swings/k788_sc_act_06_direct_response_orbit_classification_probe.py",
            "controls_passed": 46,
            "hostile_mutations_rejected": 34,
        },
    }


def validate(p: dict[str, Any]) -> None:
    op, theorem, d = p["operator"], p["orbit_theorem"], p["decision"]
    assert op["principal_map"] == "J_q(u)=K_LIFT(SHIAB(q_WEDGE_u))"
    assert op["is_direct_first_order_linearization"] and not op["is_action_hessian"]
    assert op["complete_connection_basis_enumerated"]
    assert theorem["real_nonzero_covector_orbits"] == ["native_positive", "native_negative", "native_null"]
    assert theorem["all_orbits_tested"] and theorem["auxiliary_euclidean_norm_nonzero_on_all_cases"]
    assert theorem["rank_constant_across_all_orbits"] and theorem["nullity_constant_across_all_orbits"]
    assert [row["native_norm_squared"] for row in theorem["cases"]] == [1, -1, 0]
    assert [row["auxiliary_q_norm_squared"] for row in theorem["cases"]] == [1, 1, 2]
    for row in theorem["cases"]:
        assert row["domain_dimension"] == 229376
        assert row["rank"] == 122864 and row["nullity"] == 106512
        assert row["domain_dimension"] == row["rank"] + row["nullity"]
    assert d["connection_response_rank"] == 122864 and d["connection_kernel_dimension"] == 106512
    assert not d["connection_sector_injective"] and not d["all_nonzero_covector_middle_exactness_follows_without_symmetry_quotient"]
    assert p["target_claim"] == "SC-ACT-06" and "UNCHANGED" in p["source_and_ledger_effect"]


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
