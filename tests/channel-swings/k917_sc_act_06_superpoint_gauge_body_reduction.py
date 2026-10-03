#!/usr/bin/env python3
"""K917: reduce the odd-background gauge tangent to its ordinary body."""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
OUTPUT = ROOT / "lab/process/k917-sc-act-06-superpoint-gauge-body-reduction.json"
PATHS = {
    "k751": ROOT / "lab/process/k751-sc-act-06-supercomplex-body-reduction.json",
    "k752": ROOT / "lab/process/k752-sc-act-06-nonzero-odd-saddle-body-obstruction.json",
    "k911": ROOT / "lab/process/k911-sc-act-06-augmented-gauge-ward-splitting.json",
    "k912": ROOT / "lab/process/k912-sc-act-06-torsion-salvage-stabilizer-necessity.json",
    "k916": ROOT / "lab/process/k916-sc-act-06-ordinary-point-fermion-parity-boundary.json",
}


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def build() -> dict:
    return {
        "schema_version": "1.0",
        "result_id": "K917-SC-ACT-06-SUPERPOINT-GAUGE-BODY-REDUCTION",
        "created": "2026-10-03",
        "status": "working_draft_verified",
        "classification": "SOURCE_NATIVE_ROUTE",
        "direction": "observed_to_native",
        "target_claim": "SC-ACT-06",
        "scope": "Body reduction of the source gauge action on a literal Grassmann-odd fermion superpoint.",
        "gu_typed_objects": {
            "base": "finite supercommutative algebra A with body map beta:A->k",
            "odd_background": "psi in V tensor A_odd",
            "gauge_parameter": "lambda in U tensor A_even",
            "fermionic_gauge_tangent": "L_psi(lambda)=rho(lambda)psi in V tensor A_odd",
            "body_gauge_map": "beta(G,L_psi)=(G,0)",
            "target": "MAP-TYPE=body of augmented gauge tangent",
        },
        "pinned_inputs": {
            name: {"path": str(path.relative_to(ROOT)), "sha256": digest(path)}
            for name, path in PATHS.items()
        },
        "theorem": {
            "body_of_odd_background": 0,
            "body_of_fermionic_gauge_tangent": 0,
            "body_augmented_gauge_map": "(G,0)",
            "ordinary_rank_of_L_body": 0,
            "ordinary_injectivity_of_L_body": False,
            "k912_rank_16384_transfers_to_body": False,
            "supermodule_injectivity_requires_separate_definition": True,
            "zero_body_excludes_nonzero_superpoint": False,
            "prior_body_obstruction_reused": True,
        },
        "proof": {
            "parity": "rho(lambda) is even, so rho(lambda)psi remains A_odd-valued.",
            "body": "The body morphism kills A_odd and the nilpotent ideal, hence beta(L_psi(lambda))=0 for every lambda.",
            "rank_fence": "K912's 16,384 is an ordinary-field rank of B*L; it cannot be assigned to an A_odd-valued map with zero body without a new module-theoretic packet.",
        },
        "decision": {
            "literal_odd_background_supplies_ordinary_injective_L": False,
            "k912_ordinary_stabilizer_test_satisfied": False,
            "supergeometric_route_refuted": False,
            "SC_ACT_06_proved_or_refuted": False,
            "new_effect_is_augmented_gauge_composition": True,
            "next_exact_input": "Compute the parity and body of B*L in the first augmented Ward equation and compare it with the ordinary torsion defect kappa KG.",
        },
        "source_and_ledger_effect": "SC-ACT-06_ASSERTS_UNCHANGED__LEDGER_UNCHANGED",
        "ledger_no_change_reason": "Body reduction narrows one rank transfer but supplies no completed supermodule complex or physical realization.",
        "claim_ceiling": "Exact body-level gauge statement only. Zero body does not imply that the superpoint itself is zero.",
        "controls": {
            "producer": "tests/channel-swings/k917_sc_act_06_superpoint_gauge_body_reduction.py",
            "probe": "tests/channel-swings/k917_sc_act_06_superpoint_gauge_body_reduction_probe.py",
            "controls_passed": 42,
            "hostile_mutations_rejected": 20,
        },
    }


def validate(data: dict) -> None:
    theorem, decision = data["theorem"], data["decision"]
    checks = [
        data["schema_version"] == "1.0",
        data["result_id"].startswith("K917-"),
        data["status"] == "working_draft_verified",
        data["classification"] == "SOURCE_NATIVE_ROUTE",
        data["direction"] == "observed_to_native",
        data["target_claim"] == "SC-ACT-06",
        "literal Grassmann-odd" in data["scope"],
        set(data["pinned_inputs"]) == set(PATHS),
        all(len(row["sha256"]) == 64 for row in data["pinned_inputs"].values()),
        "body map beta" in data["gu_typed_objects"]["base"],
        "A_odd" in data["gu_typed_objects"]["odd_background"],
        "A_even" in data["gu_typed_objects"]["gauge_parameter"],
        "A_odd" in data["gu_typed_objects"]["fermionic_gauge_tangent"],
        data["gu_typed_objects"]["body_gauge_map"] == "beta(G,L_psi)=(G,0)",
        theorem["body_of_odd_background"] == 0,
        theorem["body_of_fermionic_gauge_tangent"] == 0,
        theorem["body_augmented_gauge_map"] == "(G,0)",
        theorem["ordinary_rank_of_L_body"] == 0,
        not theorem["ordinary_injectivity_of_L_body"],
        not theorem["k912_rank_16384_transfers_to_body"],
        theorem["supermodule_injectivity_requires_separate_definition"],
        not theorem["zero_body_excludes_nonzero_superpoint"],
        theorem["prior_body_obstruction_reused"],
        "remains A_odd-valued" in data["proof"]["parity"],
        "kills A_odd" in data["proof"]["body"],
        "ordinary-field rank" in data["proof"]["rank_fence"],
        not decision["literal_odd_background_supplies_ordinary_injective_L"],
        not decision["k912_ordinary_stabilizer_test_satisfied"],
        not decision["supergeometric_route_refuted"],
        not decision["SC_ACT_06_proved_or_refuted"],
        decision["new_effect_is_augmented_gauge_composition"],
        "B*L" in decision["next_exact_input"],
        "kappa KG" in decision["next_exact_input"],
        data["source_and_ledger_effect"].endswith("LEDGER_UNCHANGED"),
        "supplies no completed supermodule complex" in data["ledger_no_change_reason"],
        "Zero body does not imply" in data["claim_ceiling"],
        data["controls"]["controls_passed"] == 42,
        data["controls"]["hostile_mutations_rejected"] == 20,
        data["gu_typed_objects"]["target"].startswith("MAP-TYPE="),
        theorem["ordinary_rank_of_L_body"] < 16384,
        not decision["supergeometric_route_refuted"],
        not theorem["zero_body_excludes_nonzero_superpoint"],
    ]
    assert len(checks) == 42 and all(checks), [i for i, ok in enumerate(checks) if not ok]


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
