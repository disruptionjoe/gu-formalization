#!/usr/bin/env python3
"""Fail-closed scope audit for K77 Wave-2 action/current/Riesz/Ward."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
REGISTRY = ROOT / "lab/process/k77-wave2-action-current-riesz-superig-ward-rendezvous.json"
REPORT = ROOT / "explorations/k77-wave2-action-current-riesz-superig-ward-rendezvous-2026-08-04.md"
REVIEW = ROOT / "lab/process/hostile-reviews/2026-08-04-k77-wave2-action-ward-review.md"
CAMPAIGN = ROOT / "lab/process/k77-post-b2-next-eight-wave-campaign.json"
SUCCESSOR = ROOT / "lab/process/k77-wave2-dirac-derham-superig-rebase.json"
CURRENT = ROOT / "lab/process/k77-wave2-global-draft916-krein-preboundary.json"


def unique_object(pairs):
    result = {}
    for key, value in pairs:
        if key in result:
            raise ValueError(f"duplicate JSON key: {key}")
        result[key] = value
    return result


def load_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8"), object_pairs_hook=unique_object)


def main() -> None:
    registry = load_json(REGISTRY)
    campaign = load_json(CAMPAIGN)
    successor = load_json(SUCCESSOR)
    current = load_json(CURRENT)
    report = " ".join(REPORT.read_text(encoding="utf-8").lower().split())
    review = " ".join(REVIEW.read_text(encoding="utf-8").lower().split())

    assert registry["named_gate"] == "RENDEZVOUS-ACTION-CURRENT-RIESZ-SUPERIG-WARD"
    assert registry["gate_status"] == "PARTIAL_FROZEN_LOCAL_ACTION_EVEN_WARD__ODD_SUPERIG_ACTION_OPEN"
    architecture = registry["selected_architecture"]
    assert architecture["bosonic_euler"] == "ACTUAL_SYMMETRIZED_DERIVATIVE_OF_WRITTEN_ACTION"
    assert architecture["current"] == "JD_PLUS_JF_EMITTED_ONCE_BY_S20"
    assert architecture["bridge"] == "NONE_IN_PRIMARY_ACTION"
    assert "PSEUDO_MUSICAL" in architecture["current_carrier_map"]
    assert architecture["selection_grade"] == "SOURCE_FAITHFUL_PRIMARY_NOT_MATHEMATICALLY_UNIQUE"

    exact = registry["exact_fixture"]
    assert exact["actual_translation_derivative"] == "-211/21"
    assert exact["advertised_translation_pairing"] == "-68/7"
    assert exact["defect"] == "-1/3"
    assert exact["moving_shiab_response"] == "-58/3"
    assert exact["even_ward_contraction"] == "0"
    assert exact["checks"] == {"exact": 25, "source": 6, "type": 14, "planted": 7, "total": 52}

    assert registry["current_comparison"]["ward_selects_bridge_policy"] is False
    assert registry["superig"]["TG1"].startswith("PARTIAL_REAL_POINTWISE")
    assert registry["superig"]["TG2"].startswith("OPEN")
    assert registry["superig"]["TG3"].startswith("OPEN")
    assert registry["superig"]["conjunction"] == "NOT_PROMOTED"
    assert registry["external_datum"] == {"P1": "UNUSED", "P2": "UNUSED", "P3": "UNUSED"}
    assert all(value is False for value in registry["status_boundary"].values())

    # The original action/current result remains immutable evidence.  The
    # campaign itself has source-triggered successors which rebase the odd
    # action demand, build the Dirac--de Rham symbol, and then expose the
    # still-open actual D916 assembly. Historical registries remain immutable.
    wave2 = campaign["waves"][1]
    assert wave2["status"] == current["campaign_disposition"]["successor_status"]
    assert wave2["result_ref"].endswith("k77-wave2-actual-draft916-k77-blockwise-adjoint-descent-2026-08-04.md")
    assert "ACTION_FIRST_NO_SEPARATE_BRIDGE" in wave2["emitted"]
    assert "SOURCE_AMBIENT_SIGN_DUALITY_SHIAB_PARITY_RECONCILIATION" in wave2["carried_debt"]
    assert "ACTUAL_ZERO_ORDER_W_RS_COEFFICIENTS_AND_MULTIINDEX_ADJOINT" in wave2["carried_debt"]
    assert campaign["frontier"]["next_wave"] == 2
    assert campaign["frontier"]["next_named_gate"] == "RENDEZVOUS-ACTION-CURRENT-RIESZ-SUPERIG-WARD"
    assert campaign["frontier"]["next_required_build"] == "K77_D916_SOURCE_SIGN_DUALITY_SHIAB_PARITY_RECONCILIATION"
    assert successor["gate_status"] == "PARTIAL_DIRAC_DERHAM_SYMBOL_BUILT__SOURCE_SELECTED_ACTION_AND_DOMAIN_OPEN"
    assert current["campaign_disposition"]["wave2"] == "PARTIAL"
    assert successor["superig_rebase"]["not_source_required"] == [
        "FULL_ODD_ACTION_SYMMETRY",
        "ODD_NOETHER_WARD_BV_IDENTITY",
        "ODD_MAP_TO_NONLINEAR_IG_SECTOR",
    ]

    for token in (
        "source-faithful, nonduplicating primary construction",
        "actual symmetrized euler derivative",
        "moving epsilon/shiab response",
        "indefinite pointwise pseudo-musical",
        "tg-2 = open",
        "tg-3 = open",
        "campaign stays on the same named wave-2 gate",
        "p1/p2/p3 use remain held out",
    ):
        assert token in report, f"missing report token: {token}"
    for token in (
        "pass_with_material_scope_repairs__gate_partial",
        "ward validates transformation ownership, not bridge policy",
        "source-group projection",
        "artifact defends a superseded object",
        "does not earn a complete odd action",
    ):
        assert token in review, f"missing review token: {token}"

    print("k77_wave2_action_ward_scope_audit: PASS")
    print("  original action/current evidence retained; successor Dirac--de Rham rebase recognized without rewriting provenance")


if __name__ == "__main__":
    main()
