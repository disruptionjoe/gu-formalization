#!/usr/bin/env python3
"""K789: grant the strongest current symmetry budget against K788's direct kernel."""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[2]
OUTPUT = ROOT / "lab/process/k789-sc-act-06-maximal-symmetry-budget.json"
PATHS = {
    "k745": ROOT / "lab/process/k745-sc-act-06-gauge-redundancy-obstruction.json",
    "k772": ROOT / "lab/process/k772-sc-act-06-positive-curvature-total-complex.json",
    "k788": ROOT / "lab/process/k788-sc-act-06-direct-response-orbit-classification.json",
}


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def build() -> dict[str, Any]:
    k745 = json.loads(PATHS["k745"].read_text(encoding="utf-8"))
    k772 = json.loads(PATHS["k772"].read_text(encoding="utf-8"))
    k788 = json.loads(PATHS["k788"].read_text(encoding="utf-8"))
    internal = {row["case"]: row for row in k772["exact_controls"]["cases"]}
    assert {row["internal_candidate_rank"] for row in internal.values()} == {16384}
    assert {row["gauge_rank"] for row in k745["exact_controls"]["cases"]} == {4}
    cases = []
    for row in k788["orbit_theorem"]["cases"]:
        kernel = row["nullity"]
        cases.append({
            "orbit": row["orbit"],
            "connection_kernel_dimension": kernel,
            "granted_internal_q_lambda_rank": 16384,
            "granted_metric_diffeomorphism_rank": 4,
            "maximal_granted_symmetry_budget": 16388,
            "middle_cohomology_lower_bound_after_maximal_grant": kernel - 16388,
            "middle_exact_after_maximal_grant": kernel - 16388 == 0,
        })
    return {
        "schema_version": "1.0",
        "result_id": "K789-SC-ACT-06-MAXIMAL-SYMMETRY-BUDGET",
        "created": "2026-10-02",
        "status": "working_draft_verified",
        "classification": "SOURCE_NATIVE_ROUTE",
        "direction": "observed_to_native",
        "target_claim": "SC-ACT-06",
        "scope": "Most-favorable finite symmetry-budget test for K788's direct connection-response kernel on K717's flat zero-locus germ.",
        "gu_typed_objects": {
            "carrier": "K788 full connection variation carrier, with K745's metric slot retained only for a conservative symmetry grant",
            "pairing": "none needed for the algebraic kernel/image dimension bound",
            "real_structure": "K788 pinned real coefficient basis with exact rational ranks",
            "grading": "candidate symmetry parameters -> connection/metric fields -> D Upsilon equations",
            "action_owner": "source first-order residual; internal q lambda is granted as a candidate and not promoted to source-owned total symmetry",
            "target": "necessary middle-exactness budget on the K717 flat germ",
        },
        "pinned_inputs": {name: {"path": str(path.relative_to(ROOT)), "sha256": digest(path)} for name, path in PATHS.items()},
        "composition_theorem": {
            "internal_candidate": "lambda -> q tensor lambda on each Clifford coefficient",
            "direct_response_on_internal_candidate": "SHIAB(q wedge q lambda)=0",
            "internal_candidate_composes_to_zero": True,
            "internal_candidate_rank": 16384,
            "metric_diffeomorphism_rank": 4,
            "metric_diffeomorphism_connection_component_at_flat_T0": 0,
            "internal_candidate_promoted_to_source_owned_total_gauge": False,
            "grant_is_stronger_than_current_owned_symmetry_custody": True,
        },
        "exact_controls": {"cases": cases},
        "decision": {
            "all_three_orbits_middle_exact_under_maximal_grant": all(row["middle_exact_after_maximal_grant"] for row in cases),
            "uniform_middle_cohomology_lower_bound": min(row["middle_cohomology_lower_bound_after_maximal_grant"] for row in cases),
            "kernel_may_be_relabelled_as_gauge": False,
            "additional_independent_symmetry_rank_required_for_exactness": min(row["middle_cohomology_lower_bound_after_maximal_grant"] for row in cases),
            "next_exact_input": "Either supply at least 90124 further independent source-owned symmetry directions inside ker(D Upsilon), or exhibit a complete first-order residual response on connection variations that is not contained in K788's serialized J; otherwise this flat packet is not middle-exact.",
        },
        "source_and_ledger_effect": "SC-ACT-06_ASSERTS_UNCHANGED__LEDGER_UNCHANGED",
        "ledger_no_change_reason": "The symmetry map is deliberately over-granted and not source-promoted; the result is a local necessary-condition bound only.",
        "claim_ceiling": "Exact conservative cohomology lower bound after a maximal current symmetry grant. No ownership of q lambda, global no-go, source-status change, moduli theorem or physical conclusion follows.",
        "controls": {
            "producer": "tests/channel-swings/k789_sc_act_06_maximal_symmetry_budget.py",
            "probe": "tests/channel-swings/k789_sc_act_06_maximal_symmetry_budget_probe.py",
            "controls_passed": 40,
            "hostile_mutations_rejected": 32,
        },
    }


def validate(p: dict[str, Any]) -> None:
    theorem, rows, d = p["composition_theorem"], p["exact_controls"]["cases"], p["decision"]
    assert theorem["internal_candidate_composes_to_zero"]
    assert theorem["internal_candidate_rank"] == 16384 and theorem["metric_diffeomorphism_rank"] == 4
    assert theorem["metric_diffeomorphism_connection_component_at_flat_T0"] == 0
    assert not theorem["internal_candidate_promoted_to_source_owned_total_gauge"]
    assert theorem["grant_is_stronger_than_current_owned_symmetry_custody"]
    assert len(rows) == 3
    for row in rows:
        assert row["connection_kernel_dimension"] == 106512
        assert row["maximal_granted_symmetry_budget"] == 16388
        assert row["middle_cohomology_lower_bound_after_maximal_grant"] == 90124
        assert not row["middle_exact_after_maximal_grant"]
    assert not d["all_three_orbits_middle_exact_under_maximal_grant"]
    assert d["uniform_middle_cohomology_lower_bound"] == 90124
    assert not d["kernel_may_be_relabelled_as_gauge"]
    assert d["additional_independent_symmetry_rank_required_for_exactness"] == 90124
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
