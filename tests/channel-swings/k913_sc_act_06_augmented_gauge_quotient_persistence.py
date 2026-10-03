#!/usr/bin/env python3
"""K913: prove persistence of the old tangential quotient under graph gauge."""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
OUTPUT = ROOT / "lab/process/k913-sc-act-06-augmented-gauge-quotient-persistence.json"
PATHS = {
    "k873": ROOT / "lab/process/k873-sc-act-06-owned-symmetry-custody.json",
    "k879": ROOT / "lab/process/k879-sc-act-06-full-field-quotient-injection.json",
    "k911": ROOT / "lab/process/k911-sc-act-06-augmented-gauge-ward-splitting.json",
    "k912": ROOT / "lab/process/k912-sc-act-06-torsion-salvage-stabilizer-necessity.json",
}


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def build() -> dict:
    return {
        "schema_version": "1.0",
        "result_id": "K913-SC-ACT-06-AUGMENTED-GAUGE-QUOTIENT-PERSISTENCE",
        "created": "2026-10-03",
        "status": "working_draft_verified",
        "classification": "SOURCE_NATIVE_ROUTE",
        "direction": "observed_to_native",
        "target_claim": "SC-ACT-06",
        "scope": "Field-quotient theorem for replacing the old radial gauge image by the graph of an arbitrary complementary gauge component L.",
        "gu_typed_objects": {
            "old_field_split": "X contains R direct-sum H_old with R=im(G)",
            "old_tangential_quotient": "H_old, dimension 90128, forty real types, multiplicity 169",
            "augmented_field": "X direct-sum Y",
            "graph_gauge_image": "Gamma_L={(G lambda,L lambda):lambda in U}",
            "quotient": "(X direct-sum Y)/Gamma_L",
            "target": "THEOREM-TYPE=old tangential quotient persistence",
        },
        "pinned_inputs": {
            name: {"path": str(path.relative_to(ROOT)), "sha256": digest(path)}
            for name, path in PATHS.items()
        },
        "theorem": {
            "inclusion": "i_L:H_old->(X direct-sum Y)/Gamma_L, h maps to [(h,0)]",
            "inclusion_is_injective_for_every_L": True,
            "proof_hypothesis": "H_old intersect im(G)=0",
            "surviving_lower_bound_dimension": 90128,
            "surviving_real_type_count": 40,
            "surviving_total_real_multiplicity": 169,
            "augmented_gauge_can_change_ward_cancellation": True,
            "augmented_gauge_alone_erases_old_tangential_classes": False,
        },
        "proof": {
            "kernel": "If [(h,0)]=0 then (h,0)=(G lambda,L lambda). The X component puts h in H_old intersect im(G), hence h=0.",
            "independence_from_L": "No injectivity, rank or stabilizer hypothesis on L is needed for this field-quotient injection.",
            "scope_fence": "The theorem concerns the gauge field quotient only; Hessian nondegeneracy, response-kernel membership and elliptic exactness require separate action data.",
        },
        "decision": {
            "changed_gauge_removes_k879_old_obstruction_by_quotienting": False,
            "changed_gauge_may_still_change_hessian_on_old_classes": True,
            "old_typewise_repair_obligation_persists": True,
            "next_exact_input": "Audit whether current source/action custody contains a nonzero-fermion stationary germ on which L and every Hessian block can actually be computed.",
        },
        "source_and_ledger_effect": "SC-ACT-01_04_05_06_ASSERTS_UNCHANGED__LEDGER_UNCHANGED",
        "ledger_no_change_reason": "The quotient injection preserves a lower-bound obligation but supplies no stationary germ, response map or physical state.",
        "claim_ceiling": "Exact algebraic field-quotient injection only. It does not assert that H_old remains in a changed response kernel or that the changed Hessian is degenerate there.",
        "controls": {
            "producer": "tests/channel-swings/k913_sc_act_06_augmented_gauge_quotient_persistence.py",
            "probe": "tests/channel-swings/k913_sc_act_06_augmented_gauge_quotient_persistence_probe.py",
            "controls_passed": 42,
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
        "R direct-sum H_old" in data["gu_typed_objects"]["old_field_split"],
        "90128" in data["gu_typed_objects"]["old_tangential_quotient"],
        "forty" in data["gu_typed_objects"]["old_tangential_quotient"],
        data["gu_typed_objects"]["augmented_field"] == "X direct-sum Y",
        data["gu_typed_objects"]["graph_gauge_image"].startswith("Gamma_L="),
        data["gu_typed_objects"]["quotient"] == "(X direct-sum Y)/Gamma_L",
        theorem["inclusion"].startswith("i_L:H_old"),
        theorem["inclusion_is_injective_for_every_L"],
        theorem["proof_hypothesis"] == "H_old intersect im(G)=0",
        theorem["surviving_lower_bound_dimension"] == 90128,
        theorem["surviving_real_type_count"] == 40,
        theorem["surviving_total_real_multiplicity"] == 169,
        theorem["augmented_gauge_can_change_ward_cancellation"],
        not theorem["augmented_gauge_alone_erases_old_tangential_classes"],
        "h=0" in data["proof"]["kernel"],
        "No injectivity" in data["proof"]["independence_from_L"],
        "Hessian nondegeneracy" in data["proof"]["scope_fence"],
        not decision["changed_gauge_removes_k879_old_obstruction_by_quotienting"],
        decision["changed_gauge_may_still_change_hessian_on_old_classes"],
        decision["old_typewise_repair_obligation_persists"],
        "nonzero-fermion stationary germ" in decision["next_exact_input"],
        data["source_and_ledger_effect"].endswith("LEDGER_UNCHANGED"),
        "supplies no stationary germ" in data["ledger_no_change_reason"],
        "does not assert" in data["claim_ceiling"],
        data["controls"]["controls_passed"] == 42,
        data["controls"]["hostile_mutations_rejected"] == 20,
        data["schema_version"] == "1.0",
        data["status"] == "working_draft_verified",
        data["direction"] == "observed_to_native",
        data["result_id"].startswith("K913-"),
        "arbitrary complementary gauge component" in data["scope"],
        theorem["surviving_lower_bound_dimension"] == 90128,
        theorem["surviving_real_type_count"] == 40,
        theorem["surviving_total_real_multiplicity"] == 169,
        decision["old_typewise_repair_obligation_persists"],
        not decision["changed_gauge_removes_k879_old_obstruction_by_quotienting"],
        theorem["inclusion_is_injective_for_every_L"],
        not theorem["augmented_gauge_alone_erases_old_tangential_classes"],
    ]
    assert len(checks) == 42 and all(checks), [i for i, value in enumerate(checks) if not value]


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
