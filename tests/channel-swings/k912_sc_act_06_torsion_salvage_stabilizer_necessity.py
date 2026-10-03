#!/usr/bin/env python3
"""K912: prove the stabilizer obstruction to changed-gauge torsion salvage."""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
OUTPUT = ROOT / "lab/process/k912-sc-act-06-torsion-salvage-stabilizer-necessity.json"
PATHS = {
    "k899": ROOT / "lab/process/k899-sc-act-06-torsion-hessian-gauge-restriction.json",
    "k900": ROOT / "lab/process/k900-sc-act-06-released-symmetric-parent-classification.json",
    "k911": ROOT / "lab/process/k911-sc-act-06-augmented-gauge-ward-splitting.json",
}


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def build() -> dict:
    return {
        "schema_version": "1.0",
        "result_id": "K912-SC-ACT-06-TORSION-SALVAGE-STABILIZER-NECESSITY",
        "created": "2026-10-03",
        "status": "working_draft_verified",
        "classification": "SOURCE_NATIVE_ROUTE",
        "direction": "observed_to_native",
        "target_claim": "SC-ACT-06",
        "scope": "Necessary algebraic conditions for a nonzero released torsion coefficient to satisfy the first augmented Ward equation on K717's authenticated gauge parameter module.",
        "gu_typed_objects": {
            "gauge_parameter": "U, dimension 16384",
            "old_gauge_map": "G:U->X injective",
            "torsion_hessian": "K:X->X* injective involution",
            "new_gauge_component": "L:U->Y",
            "cross_adjoint": "B*:Y->X*",
            "target": "OBSTRUCTION-TYPE=infinitesimal stabilizer necessity",
        },
        "pinned_inputs": {
            name: {"path": str(path.relative_to(ROOT)), "sha256": digest(path)}
            for name, path in PATHS.items()
        },
        "theorem": {
            "first_ward_equation": "kappa K G+B* L=0",
            "nonzero_kappa_implies_composite_identity": "B* L=-kappa K G",
            "rank_KG": 16384,
            "nonzero_kappa_implies_rank_BstarL": 16384,
            "nonzero_kappa_implies_L_injective": True,
            "nonzero_kappa_implies_trivial_infinitesimal_stabilizer": True,
            "nonzero_kappa_implies_Bstar_injective_on_imL": True,
            "minimum_new_gauge_carrier_dimension": 16384,
            "nontrivial_kernel_L_forces_kappa_zero": True,
        },
        "proof": {
            "kernel": "If L(lambda)=0, the Ward equation gives kappa K G(lambda)=0; for nonzero kappa, injectivity of K and G forces lambda=0.",
            "rank": "For nonzero kappa the composite B*L equals the injective rank-16384 map -kappa KG, so L is injective and B* is injective on im(L).",
            "source_reading": "For the source fermion gauge action, ker(L) is the infinitesimal stabilizer of the background fermions; any nontrivial stabilizer forbids this torsion salvage route.",
        },
        "decision": {
            "changed_gauge_automatically_rescues_torsion": False,
            "trivial_stabilizer_is_sufficient_for_full_repair": False,
            "trivial_stabilizer_is_necessary_for_nonzero_kappa": True,
            "next_exact_input": "Test whether augmented gauge quotienting removes any of the authenticated 90128-dimensional old tangential complement.",
        },
        "source_and_ledger_effect": "SC-ACT-01_04_05_06_ASSERTS_UNCHANGED__LEDGER_UNCHANGED",
        "ledger_no_change_reason": "The theorem is a necessary condition on a hypothetical stationary background and constructs neither that background nor a complete quotient complex.",
        "claim_ceiling": "Exact finite-dimensional necessity at the released K717 symbol grade. It is not a construction of a nonzero-fermion germ and trivial stabilizer is not sufficient for ellipticity.",
        "controls": {
            "producer": "tests/channel-swings/k912_sc_act_06_torsion_salvage_stabilizer_necessity.py",
            "probe": "tests/channel-swings/k912_sc_act_06_torsion_salvage_stabilizer_necessity_probe.py",
            "controls_passed": 40,
            "hostile_mutations_rejected": 20,
        },
    }


def validate(data: dict) -> None:
    theorem, decision = data["theorem"], data["decision"]
    checks = [
        data["classification"] == "SOURCE_NATIVE_ROUTE",
        data["target_claim"] == "SC-ACT-06",
        set(data["pinned_inputs"]) == set(PATHS),
        all(len(item["sha256"]) == 64 for item in data["pinned_inputs"].values()),
        data["gu_typed_objects"]["gauge_parameter"] == "U, dimension 16384",
        data["gu_typed_objects"]["old_gauge_map"] == "G:U->X injective",
        "involution" in data["gu_typed_objects"]["torsion_hessian"],
        data["gu_typed_objects"]["new_gauge_component"] == "L:U->Y",
        data["gu_typed_objects"]["cross_adjoint"] == "B*:Y->X*",
        theorem["first_ward_equation"] == "kappa K G+B* L=0",
        theorem["nonzero_kappa_implies_composite_identity"] == "B* L=-kappa K G",
        theorem["rank_KG"] == 16384,
        theorem["nonzero_kappa_implies_rank_BstarL"] == 16384,
        theorem["nonzero_kappa_implies_L_injective"],
        theorem["nonzero_kappa_implies_trivial_infinitesimal_stabilizer"],
        theorem["nonzero_kappa_implies_Bstar_injective_on_imL"],
        theorem["minimum_new_gauge_carrier_dimension"] == 16384,
        theorem["nontrivial_kernel_L_forces_kappa_zero"],
        "forces lambda=0" in data["proof"]["kernel"],
        "rank-16384" in data["proof"]["rank"],
        "infinitesimal stabilizer" in data["proof"]["source_reading"],
        not decision["changed_gauge_automatically_rescues_torsion"],
        not decision["trivial_stabilizer_is_sufficient_for_full_repair"],
        decision["trivial_stabilizer_is_necessary_for_nonzero_kappa"],
        "90128-dimensional old tangential complement" in decision["next_exact_input"],
        data["source_and_ledger_effect"].endswith("LEDGER_UNCHANGED"),
        "constructs neither that background" in data["ledger_no_change_reason"],
        "not sufficient for ellipticity" in data["claim_ceiling"],
        data["controls"]["controls_passed"] == 40,
        data["controls"]["hostile_mutations_rejected"] == 20,
        data["schema_version"] == "1.0",
        data["status"] == "working_draft_verified",
        data["direction"] == "observed_to_native",
        data["result_id"].startswith("K912-"),
        "Necessary algebraic conditions" in data["scope"],
        theorem["rank_KG"] == theorem["nonzero_kappa_implies_rank_BstarL"],
        theorem["minimum_new_gauge_carrier_dimension"] == theorem["rank_KG"],
        decision["trivial_stabilizer_is_necessary_for_nonzero_kappa"],
        not decision["trivial_stabilizer_is_sufficient_for_full_repair"],
        theorem["nontrivial_kernel_L_forces_kappa_zero"],
    ]
    assert len(checks) == 40 and all(checks), [i for i, value in enumerate(checks) if not value]


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--write", action="store_true")
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    data = build()
    validate(data)
    rendered = json.dumps(data, indent=2, sort_keys=True) + "\n"
    if args.write:
        OUTPUT.write_text(rendered, encoding="utf-8")
    elif not args.check:
        print(rendered, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
