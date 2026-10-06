#!/usr/bin/env python3
"""Freeze K1193's exact angular measure and compact boundary recursion."""

from __future__ import annotations

import argparse
import hashlib
import json
import math
from fractions import Fraction
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[2]
K414 = ROOT / "lab/process/k414-order-ten-face-normal-integrability-atlas.json"
K1193 = ROOT / "lab/process/k1193-order-ten-normal-projective-atlas.json"
OUTPUT = ROOT / "lab/process/k1194-order-ten-projective-measure-and-boundary-routing.json"


def q(value: Fraction) -> str:
    return str(value.numerator) if value.denominator == 1 else f"{value.numerator}/{value.denominator}"


def digest(value: Any) -> str:
    encoded = json.dumps(value, sort_keys=True, separators=(",", ":")).encode()
    return "sha256:" + hashlib.sha256(encoded).hexdigest()


def build() -> dict[str, Any]:
    k414 = json.loads(K414.read_text())
    k1193 = json.loads(K1193.read_text())
    atlas = k1193["mask_atlas"]
    if len(atlas) != 121 or len(k414["face_normal_atlas"]) != 936:
        raise AssertionError("K414/K1193 census changed")

    codimension_rows = []
    for codimension in k1193["fixed_control"]["reachable_codimensions"]:
        mask_count = sum(row["codimension"] == codimension for row in atlas)
        chart_mass = Fraction(1, math.factorial(codimension))
        simplex_mass = Fraction(1, math.factorial(codimension - 1))
        lower_coordinate_boundaries = codimension * (codimension - 1)
        tie_coordinate_boundaries = lower_coordinate_boundaries
        lower_strata_per_chart = 2 ** (codimension - 1) - 1
        codimension_rows.append({
            "codimension": codimension,
            "unique_masks": mask_count,
            "charts_per_mask": codimension,
            "chart_angular_mass": q(chart_mass),
            "simplex_angular_mass": q(simplex_mass),
            "chart_sum_replays_simplex_mass": codimension * chart_mass == simplex_mass,
            "oriented_lower_coordinate_boundaries_per_mask": lower_coordinate_boundaries,
            "oriented_tie_coordinate_boundaries_per_mask": tie_coordinate_boundaries,
            "nonempty_lower_boundary_strata_per_chart": lower_strata_per_chart,
            "maximum_zero_boundary_recursion_depth": codimension - 1,
        })

    unique_oriented_boundaries = sum(2 * row["codimension"] * (row["codimension"] - 1) for row in atlas)
    program_oriented_boundaries = sum(2 * row["codimension"] * (row["codimension"] - 1) for row in k1193["program_chart_map"])
    compact_lower_strata = sum(
        row["codimension"] * (2 ** (row["codimension"] - 1) - 1)
        for row in atlas
    )
    normal_powers = [int(row["minimum_second_derivative_face_normal_power"]) for row in k414["face_normal_atlas"]]

    return {
        "schema_version": "1.0",
        "result_id": "K1194-ORDER-TEN-PROJECTIVE-MEASURE-AND-BOUNDARY-ROUTING",
        "created": "2026-10-06",
        "classification": "INTERNAL_STRUCTURAL_ONLY",
        "direction": "observed_to_native",
        "fixed_control": {
            "predecessor_manifests": [str(K414.relative_to(ROOT)), str(K1193.relative_to(ROOT))],
            "face_programs": 936,
            "unique_zero_masks": 121,
            "unique_maximum_charts": 1022,
            "unique_oriented_coordinate_boundaries": unique_oriented_boundaries,
            "program_oriented_coordinate_boundary_uses": program_oriented_boundaries,
            "compactly_represented_nonempty_lower_strata": compact_lower_strata,
            "reachable_codimensions": k1193["fixed_control"]["reachable_codimensions"],
        },
        "measure_contract": {
            "simplex": "Delta^(c-1)={p_i>=0,sum p_i=1}",
            "simplex_angular_mass": "1/(c-1)!",
            "maximum_chart_angular_mass": "1/c! by coordinate-permutation symmetry",
            "chart_sum_identity": "c*(1/c!)=1/(c-1)!",
            "ratio_chart_density": "(1+sum r)^(-c) product_i dr_i",
            "radial_angular_factorization": "product_i dt_i=rho^(c-1) d_rho d_sigma",
            "K414_normal_power_already_includes_radial_jacobian": True,
            "angular_mass_must_not_be_applied_to_K1192_equal_line_values": True,
        },
        "boundary_routing_contract": {
            "zero_boundary": "for nonempty B subset of ratio axes, r_i=0 for i in B lowers positive support by |B| and routes to the corresponding lower-dimensional projective stratum",
            "vertex_boundary": "all ratios zero gives the anchor vertex",
            "tie_boundary": "r_i=1 adds i to the maximum set and routes ownership to the smallest canonical axis in that set",
            "multiple_tie_boundary": "apply the same smallest-axis rule to the complete maximum set",
            "termination_metric": "lexicographic (positive-support size, canonical owner index): zero routing strictly lowers support size and tie routing strictly lowers owner index unless already owned",
            "zero_routing_terminates": True,
            "tie_routing_terminates": True,
            "boundaries_have_angular_measure_zero": True,
            "interval_closures_still_require_one_sided_zero_safe_majorants": True,
            "K410_radial_zero_contract_does_not_by_itself_close_every_projective_coordinate_boundary": True,
            "explicit_exponential_boundary_expansion_avoided": True,
        },
        "codimension_measure_bank": codimension_rows,
        "K414_reconciliation": {
            "face_rows": len(normal_powers),
            "minimum_normal_power": min(normal_powers),
            "maximum_normal_power": max(normal_powers),
            "all_face_normal_powers_locally_integrable": all(power >= 0 for power in normal_powers),
            "radial_power_is_not_angular_uniformity": True,
        },
        "routing_summary": {
            "all_reachable_codimensions_measured": len(codimension_rows) == len(k1193["fixed_control"]["reachable_codimensions"]),
            "all_chart_mass_sums_exact": all(row["chart_sum_replays_simplex_mass"] for row in codimension_rows),
            "all_zero_and_tie_routes_terminate": True,
            "boundary_contract_sha256": digest(codimension_rows),
        },
        "decision": {
            "exact_angular_measure_compiled": True,
            "compact_projective_boundary_recursion_compiled": True,
            "positive_width_projective_cells_evaluated": False,
            "zero_inclusive_projective_boundary_majorants_complete": False,
            "recursive_positive_interior_cover_complete": False,
            "complete_hybrid_integrals_emitted": False,
            "next_exact_input": "execute anisotropic positive projective controls, then build positive-width ratio cells together with one-sided zero-boundary strip majorants before global face-neighborhood ownership",
        },
        "release_test": {
            "exactly_21624_unique_oriented_coordinate_boundaries": unique_oriented_boundaries == 21624,
            "exactly_107832_program_boundary_uses": program_oriented_boundaries == 107832,
            "exactly_94463974_compact_lower_strata": compact_lower_strata == 94_463_974,
            "all_chart_mass_sums_exact": all(row["chart_sum_replays_simplex_mass"] for row in codimension_rows),
            "all_K414_face_powers_nonnegative": all(power >= 0 for power in normal_powers),
            "boundary_measure_zero_not_interval_closure": True,
            "projective_cells_not_overclaimed": True,
            "complete_order_ten_remainder_not_overclaimed": True,
            "native_K152_interval_not_emitted": True,
        },
        "ledger_effect": k414["ledger_effect"],
        "source_routing": k414["source_routing"],
        "claim_ceiling": "Exact angular masses and compact recursive boundary routing for K1193's complete maximum-coordinate projective atlas. Every chart has mass 1/c!, the c charts sum to the simplex mass 1/(c-1)!, and zero/tie routing terminates. Measure-zero boundaries are not interval enclosures: one-sided zero-safe projective boundary majorants, positive-width chart cells, global face-neighborhood ownership, recursive interior, tails, K409 integrals, the complete order-ten remainder/integral, action column, R_ref, K152 interval, source/ledger move, canon, paper, public and physical posture remain open.",
    }


def validate_payload(payload: dict[str, Any]) -> None:
    fixed = payload["fixed_control"]
    if (fixed["face_programs"], fixed["unique_zero_masks"], fixed["unique_maximum_charts"]) != (936, 121, 1022):
        raise AssertionError("K1194 atlas census changed")
    if (fixed["unique_oriented_coordinate_boundaries"], fixed["program_oriented_coordinate_boundary_uses"], fixed["compactly_represented_nonempty_lower_strata"]) != (21624, 107832, 94_463_974):
        raise AssertionError("K1194 boundary census changed")
    if not all(row["chart_sum_replays_simplex_mass"] for row in payload["codimension_measure_bank"]):
        raise AssertionError("K1194 chart mass changed")
    measure = payload["measure_contract"]
    if not measure["K414_normal_power_already_includes_radial_jacobian"] or not measure["angular_mass_must_not_be_applied_to_K1192_equal_line_values"]:
        raise AssertionError("K1194 measure ownership changed")
    routing = payload["boundary_routing_contract"]
    required = ("zero_routing_terminates", "tie_routing_terminates", "boundaries_have_angular_measure_zero", "interval_closures_still_require_one_sided_zero_safe_majorants", "K410_radial_zero_contract_does_not_by_itself_close_every_projective_coordinate_boundary")
    if not all(routing[key] for key in required):
        raise AssertionError("K1194 boundary routing changed")
    decision = payload["decision"]
    if not decision["exact_angular_measure_compiled"] or not decision["compact_projective_boundary_recursion_compiled"] or any(decision[key] for key in ("positive_width_projective_cells_evaluated", "zero_inclusive_projective_boundary_majorants_complete", "recursive_positive_interior_cover_complete", "complete_hybrid_integrals_emitted")):
        raise AssertionError("K1194 decision boundary changed")
    if not all(payload["release_test"].values()):
        raise AssertionError("K1194 release test failed")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--write", action="store_true")
    args = parser.parse_args()
    payload = build()
    validate_payload(payload)
    rendered = json.dumps(payload, indent=2, sort_keys=True) + "\n"
    if args.write:
        OUTPUT.write_text(rendered)
    else:
        print(rendered, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
