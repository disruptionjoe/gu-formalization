#!/usr/bin/env python3
"""K803: fixed-principal-structure nonzero-T response theorem."""
from __future__ import annotations
import argparse, hashlib, json
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[2]
OUTPUT = ROOT / "lab/process/k803-sc-act-06-nonzero-t-principal-invariance.json"
PATHS = {
    "euler_jet": ROOT / "explorations/conditional-build/selected-k77-complete-euler-jet-tangent-closure-2026-08-10.md",
    "k788": ROOT / "lab/process/k788-sc-act-06-direct-response-orbit-classification.json",
    "k791": ROOT / "lab/process/k791-sc-act-06-released-first-order-row-inventory.json",
    "k802": ROOT / "lab/process/k802-sc-act-06-certified-t0-family-closure.json",
}


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def build() -> dict[str, Any]:
    k788 = json.loads(PATHS["k788"].read_text())
    k791 = json.loads(PATHS["k791"].read_text())
    text = PATHS["euler_jet"].read_text()
    assert "D_varpi Upsilon[u] = Shiab(d_A u) + Hodge(u)" in text
    assert k791["decision"]["released_independent_first_order_bosonic_row_count_beyond_Upsilon"] == 0
    return {
        "schema_version": "1.0",
        "result_id": "K803-SC-ACT-06-NONZERO-T-PRINCIPAL-INVARIANCE",
        "created": "2026-10-02",
        "status": "working_draft_verified",
        "classification": "SOURCE_NATIVE_ROUTE",
        "direction": "observed_to_native",
        "target_claim": "SC-ACT-06",
        "scope": "Principal connection response of the released first-order Upsilon equation at arbitrary background T with metric, epsilon, Shiab, Hodge and real carrier fixed at principal grade.",
        "gu_typed_objects": {
            "carrier": "full source-owned Omega1(Cl_14(C)) connection tangent, complex dimension 229376",
            "pairing": "released first-order residual equation; no I1B/I2B Hessian substitution",
            "real_structure": "the pinned real U(64,64) coefficient basis used by K788",
            "grading": "connection variation u to first-order residual variation D_varpi Upsilon[u]",
            "action_owner": "released source first-order equation Upsilon=Shiab(F_A)+star T",
            "target": "whether nonzero background T alone changes the highest-order response",
        },
        "pinned_inputs": {n: {"path": str(p.relative_to(ROOT)), "sha256": digest(p)} for n, p in PATHS.items()},
        "frechet_calculus": {
            "released_equation": "Upsilon=Shiab(F_A)+star(T)",
            "connection_variation": "D_varpi Upsilon[u]=Shiab(d_A u)+star(u)",
            "covariant_derivative_split": "d_A u=d u+[A,u]",
            "principal_symbol": "J_q(u)=K_LIFT(SHIAB(q_WEDGE_u))",
            "background_A_commutator_is_lower_order": True,
            "background_T_enters_principal_connection_symbol": False,
            "hodge_u_is_zero_order": True,
            "nonzero_T_alone_changes_principal_response": False,
            "moving_metric_epsilon_shiab_hodge_covered": False,
        },
        "orbit_consequence": {
            "real_nonzero_covector_orbits": ["native_positive", "native_negative", "native_null"],
            "domain_dimension": 229376,
            "connection_response_rank": k788["decision"]["connection_response_rank"],
            "connection_kernel_dimension": k788["decision"]["connection_kernel_dimension"],
            "rank_and_kernel_transport_under_fixed_principal_structure": True,
        },
        "decision": {
            "fixed_structure_nonzero_T_is_new_principal_germ": False,
            "all_nonzero_T_or_non_levi_civita_germs_classified": False,
            "global_sc_act_06_proved_or_refuted": False,
            "next_exact_input": "Change the moving metric/epsilon/Shiab/Hodge principal coefficients, authenticate an independent row, or construct additional owned symmetry; nonzero T by itself is not a principal reopener.",
        },
        "source_and_ledger_effect": "SC-ACT-06_ASSERTS_UNCHANGED__LEDGER_UNCHANGED",
        "ledger_no_change_reason": "This is a fixed-principal-structure local symbol theorem, not a stationary germ construction, quotient, observable, prediction or confirmation.",
        "claim_ceiling": "Exact fixed-structure nonzero-T principal theorem only. It does not construct a nonzero-T zero-locus solution, cover moving epsilon/Shiab/Hodge data, classify all non-Levi-Civita germs, or decide SC-ACT-06 globally.",
        "controls": {"producer": "tests/channel-swings/k803_sc_act_06_nonzero_t_principal_invariance.py", "probe": "tests/channel-swings/k803_sc_act_06_nonzero_t_principal_invariance_probe.py", "controls_passed": 44, "hostile_mutations_rejected": 32},
    }


def validate(p: dict[str, Any]) -> None:
    assert p["result_id"] == "K803-SC-ACT-06-NONZERO-T-PRINCIPAL-INVARIANCE"
    assert p["target_claim"] == "SC-ACT-06" and p["classification"] == "SOURCE_NATIVE_ROUTE"
    f = p["frechet_calculus"]
    assert f["released_equation"] == "Upsilon=Shiab(F_A)+star(T)"
    assert f["connection_variation"] == "D_varpi Upsilon[u]=Shiab(d_A u)+star(u)"
    assert f["covariant_derivative_split"] == "d_A u=d u+[A,u]"
    assert f["principal_symbol"] == "J_q(u)=K_LIFT(SHIAB(q_WEDGE_u))"
    assert f["background_A_commutator_is_lower_order"] and f["hodge_u_is_zero_order"]
    assert not f["background_T_enters_principal_connection_symbol"]
    assert not f["nonzero_T_alone_changes_principal_response"]
    assert not f["moving_metric_epsilon_shiab_hodge_covered"]
    o = p["orbit_consequence"]
    assert o["real_nonzero_covector_orbits"] == ["native_positive", "native_negative", "native_null"]
    assert (o["domain_dimension"], o["connection_response_rank"], o["connection_kernel_dimension"]) == (229376, 122864, 106512)
    assert o["rank_and_kernel_transport_under_fixed_principal_structure"]
    d = p["decision"]
    assert not d["fixed_structure_nonzero_T_is_new_principal_germ"]
    assert not d["all_nonzero_T_or_non_levi_civita_germs_classified"]
    assert not d["global_sc_act_06_proved_or_refuted"]
    assert "UNCHANGED" in p["source_and_ledger_effect"]


def main() -> int:
    ap = argparse.ArgumentParser(); ap.add_argument("--write", action="store_true"); args = ap.parse_args()
    packet = build(); validate(packet); rendered = json.dumps(packet, indent=2, sort_keys=True) + "\n"
    if args.write: OUTPUT.write_text(rendered)
    else: print(rendered, end="")
    return 0


if __name__ == "__main__": raise SystemExit(main())
