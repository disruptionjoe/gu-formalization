#!/usr/bin/env python3
"""Fail-closed scope audit for RESOLVER-WAVE-C-REBASED.

This gate verifies disposition and Layer-0 fences.  It does not reproduce the
representation or topology calculations and moves no scientific status.
"""
from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
REGISTRY = ROOT / "explorations/cycle-gates-and-audits/resolver-wave-c-rebased-disposition-2026-08-03.json"
REPORT = ROOT / "explorations/resolver-wave-c-rebased-q5-q6-mh7-2026-08-03.md"


def main() -> None:
    data = json.loads(REGISTRY.read_text(encoding="utf-8"))
    report = REPORT.read_text(encoding="utf-8")

    assert data["named_gate"] == "RESOLVER-WAVE-C-REBASED"
    assert data["gate_after"] == "REBASE_REQUIRED"
    assert data["route_disposition"] == "REBASE"

    q5 = data["subwaves"]["Q5"]
    assert q5["bare_same_label_contains_126"] is False
    assert q5["dualized_hom_contains_126"] is True
    assert q5["hom_condition"] == "complex_linear_internal_operator_factor_only"
    assert q5["physical_krein_C_real_pairing_built"] is False
    assert q5["multiplicity"] == 1
    assert q5["existing_B5_symbol_channel"] == "10"
    assert q5["new_channel_selected"] is False

    q6 = data["subwaves"]["Q6"]
    assert q6["internal_degree_zero_dimension"] == 252
    assert q6["complex_hodge_halves"] == ["126+", "126-"]
    assert q6["real_internal_carrier_dimension"] == 252
    assert q6["raw_real_lambda5_adjoint_class"] == "K_SELF_ADJOINT"
    assert q6["Sp_connection_generator_required_adjoint_class"] == "K_ANTI_SELF_ADJOINT"
    assert q6["raw_lambda5_subset_adP_allowed"] is False
    assert q6["native_connection_placement_built"] is False
    assert q6["vev_built"] is False and q6["mass_built"] is False

    mh7 = data["subwaves"]["M-H7"]
    assert mh7["Omega13fr"] == "Z/3"
    assert mh7["Omega13Spin"] == "0"
    assert mh7["global_link_built"] is False
    assert mh7["stable_framing_built"] is False
    assert mh7["nonzero_PT_class_built"] is False
    assert mh7["external_product_stable_framing_class"] == "0_if_X4_closed_stably_framed"
    assert mh7["nonproduct_framing_controlled"] is False
    assert mh7["supersedes_degree3_spine_J_route"] is False

    assert data["assertion_counts"]["total"] == 126
    assert data["assertion_counts"]["planted"] == 7
    assert data["source_collision"]["weinstein_exact_lambda5_126_carrier"] == "SOURCE-SILENT"
    assert all(value == "unchanged_unused" for key, value in data["external_datum"].items()
               if key in {"P1", "P2", "P3"})
    assert data["external_datum"]["order_three_torsion_is_integer_P3"] is False
    assert data["next_gate"]["id"] == "RESOLVER-WAVE-D-NATIVE-126-CONNECTION-PLACEMENT"

    for token in (
        "Hom(F+,T+)",
        "not two independent real fields",
        "external-product stable framing",
        "raw `Lambda^5 subset ad(P)` is obstructed",
        "P1/P2/P3 remain unchanged and unused",
        "Omega^1(Y, ad P)  --->  Lambda^5 V10",
    ):
        assert token in report, "report missing scope token {!r}".format(token)

    for forbidden in (
        "the 126 is the existing B5 mediator",
        "the product model realizes the generator",
        "order-three torsion proves three generations",
    ):
        assert forbidden not in report.lower()

    print("resolver_wave_c_scope_audit: PASS")
    print("  conditional Hom, adjoint obstruction, dim-13 realization, and P3 fences retained")


if __name__ == "__main__":
    main()
