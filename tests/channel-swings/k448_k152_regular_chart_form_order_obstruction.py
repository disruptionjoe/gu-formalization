#!/usr/bin/env python3
"""K448 form-order consequences of the complete K447 defect census."""

from __future__ import annotations

import argparse
import json

from k447_k152_charge_sector_galerkin_defect_census import demo as k447_demo


def demo() -> dict:
    census = k447_demo()
    rows = census["sectors"]
    raw_inertia = [row["raw_defect"]["inertia_positive_negative_zero"] for row in rows]
    regular_inertia = [row["regular_defect"]["inertia_positive_negative_zero"] for row in rows]
    return {
        "schema_version": "1.0",
        "result_id": "K448-K152-REGULAR-CHART-FORM-ORDER-OBSTRUCTION",
        "classification": "INTERNAL_STRUCTURAL_ONLY",
        "direction": "observed_to_native",
        "input": "K447 exact q00/q10/q01 defect census",
        "raw_cutoff_forms": {
            "defect_inertias": raw_inertia,
            "fine_compression_strictly_above_independent_coarse_form": True,
            "all_three_sectors_positive_definite": raw_inertia == [[8, 0, 0], [7, 0, 0], [7, 0, 0]],
        },
        "regular_chart_forms": {
            "defect_inertias": regular_inertia,
            "all_three_sectors_indefinite": regular_inertia == [[5, 3, 0], [5, 2, 0], [5, 2, 0]],
            "fine_compression_ge_independent_coarse": False,
            "fine_compression_le_independent_coarse": False,
            "one_sided_minmax_transfer_available": False,
            "nonlinear_regular_pullback_preserves_raw_form_order": False,
        },
        "decision": {
            "K163_first_entry_was_isolated_accident": False,
            "obstruction_is_full_rank_and_sector_wide": True,
            "independent_rediscretization_can_supply_native_K152_gap": False,
            "requires_exact_compression_or_two_sided_defect_bound": True,
            "coercivity_or_exterior_gap_proved": False,
            "native_K152_interval_emitted": False,
        },
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--demo", action="store_true")
    args = parser.parse_args()
    if not args.demo:
        parser.error("use --demo")
    print(json.dumps(demo(), indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
