#!/usr/bin/env python3
"""Fail-closed scope audit for the K77 trace-q zero-order/reality packet."""

from __future__ import annotations

import json
from pathlib import Path

from k77_wave2_augmented_torsion_defect_euler_receiver_scope_audit import historical_wave2_checkpoint


ROOT = Path(__file__).resolve().parents[1]
REGISTRY = ROOT / "lab/process/k77-wave2-trace-q-coefficient-zero-order-reality-selection.json"
REPORT = ROOT / "explorations/k77-wave2-trace-q-coefficient-zero-order-reality-selection-2026-08-04.md"
REVIEW = ROOT / "lab/process/hostile-reviews/2026-08-04-k77-wave2-trace-q-coefficient-zero-order-reality-review.md"
SOURCE = ROOT / "lab/sources/curt-iceberg-fermion-zero-order-reinspection-2026-08-04.md"
CAMPAIGN = ROOT / "lab/process/k77-post-b2-next-eight-wave-campaign.json"


def unique_object(pairs):
    result = {}
    for key, value in pairs:
        if key in result:
            raise ValueError(f"duplicate JSON key: {key}")
        result[key] = value
    return result


def load_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8"), object_pairs_hook=unique_object)


def normalized(path: Path) -> str:
    return " ".join(path.read_text(encoding="utf-8").lower().split())


def main() -> None:
    registry = load_json(REGISTRY)
    campaign = load_json(CAMPAIGN)
    report = normalized(REPORT)
    review = normalized(REVIEW)
    source = normalized(SOURCE)

    expected = (
        "PARTIAL__FULL16_TRACE_Q_FAMILY_ASSEMBLED__"
        "CURT_ZERO_ORDER_PORT_NARROWED__NATIVE_REALITY_SELECTS_NOTHING__"
        "MAJORANA_RIVAL_EMPTY__COMMON_TWO_LAYER_ACTION_EULER_SELECTION_OPEN"
    )
    assert registry["named_gate"] == "K77_D916_TRACE_Q_COEFFICIENT_ZERO_ORDER_REALITY_SELECTION"
    assert registry["result"] == expected
    assert registry["construction"] == {
        "d916_cells": 16,
        "q_repaired_shiab_cells": 4,
        "first_order_cells": 6,
        "southeast_zero_cells": 4,
        "uniform_projective_coefficient": True,
        "cellwise_retuning": False,
        "degree_reality_solutions": [[-1, 1, 1, -1], [1, -1, -1, 1]],
        "degree_one_cell_factor": -1,
    }

    collision = registry["source_collision"]
    assert collision["curt_zero_order_port"] == "SOURCE_CONFIRMS_AS_RECONSTRUCTION_TARGET"
    assert collision["single_layer_minimal_coupling"].startswith("SOURCE_CORRECTS")
    assert collision["physical_higgs_as_adjoint_scalar"].startswith("SOURCE_CORRECTS")
    assert collision["exact_varpi_rs_higgs_cell"] == "SOURCE_SILENT"
    assert collision["trace_q_coefficient"] == "SOURCE_SILENT"

    selection = registry["selection"]
    assert selection["native_c_reality_rank"] == 0
    assert selection["independent_bar_sensitivity_rank"] == 2
    assert selection["source_euler_selection_rank"] == 0
    assert selection["majorana_principal_self_rank"] == 2
    assert selection["majorana_principal_skew_rank"] == 2
    assert selection["majorana_zero_self_rank"] == 2
    assert selection["majorana_zero_skew_rank"] == 2
    assert selection["majorana_projective_survivors"] == 0
    assert selection["source_faithful_projective_free_parameters"] == 1
    assert selection["source_faithful_constraint_surplus"] == -1

    assert registry["surviving_branch"] == "SOURCE_FAITHFUL_COMPLEX_DIRAC_INDEPENDENT_BAR_COEFFICIENT_FAMILY"
    assert registry["next_required_build"] == "K77_COMMON_TWO_LAYER_DIRAC_YANG_MILLS_HIGGS_ACTION_EULER_COEFFICIENT_SELECTION"
    assert registry["wave3_open"] is False
    assert registry["curt_status"] == "FORMALLY_SEPARATE_GUIDANCE_INSIDE_ERIC_LANE"
    assert registry["tg_promotion"] == "TG_1_AND_TG_2_AND_TG_3_NOT_PROMOTED"
    assert registry["p1_p2_p3_used"] is False

    required_emissions = (
        "FULL16_UNIFORM_TRACE_Q_COEFFICIENT_FAMILY",
        "CURT_ZERO_ORDER_CONNECTION_PORT_WITH_WEINSTEIN_TWO_LAYER_CORRECTION",
        "NATIVE_REALITY_COEFFICIENT_SELECTION_RANK_ZERO",
        "OPTIONAL_MAJORANA_RIVAL_EMPTY_ON_CURRENT_FULL_INDEX_FAMILY",
        "SOURCE_FAITHFUL_COMPLEX_DIRAC_PROJECTIVE_SURPLUS_MINUS_1",
    )
    assert historical_wave2_checkpoint(campaign, required_emissions)

    for token in (
        "source-corrects",
        "complete form-index times spinor krein pairing",
        "only solution is `alpha=beta=0`",
        "constraint surplus: -1",
        "p1/p2/p3 are unchanged and unused",
        "wave 3 does not open",
    ):
        assert token in report, f"missing report token: {token}"

    for token in (
        "majorana selects commutator",
        "two-layer adapter obligation",
        "zero-order connection candidate",
        "restricted higgs orbit",
        "56/56",
        "wave 3 remains closed",
    ):
        assert token in review, f"missing review token: {token}"

    for token in (
        "01:46:11--01:48:57",
        "00:41:50--00:42:44",
        "source-corrects",
        "four distinct variables",
        "cannot by itself spend the remaining projective coefficient",
    ):
        assert token in source, f"missing source token: {token}"

    print("k77_wave2_trace_q_coefficient_zero_order_reality_scope_audit: PASS")
    print("  full16 q family assembled; Curt port narrowed; native reality rank 0; Majorana rival empty; common two-layer action remains open")


if __name__ == "__main__":
    main()
