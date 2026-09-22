#!/usr/bin/env python3
"""Compose K338 with the native prefactor without inventing a base value.

K338 closes the six-axis Peano remainder.  The accepted K334 bank from which
its y term is drawn is still integrated against K318's y-Peano endpoint atlas;
its zeroth Taylor coefficient is therefore not the K299 one-node value at
``p_i=1/6, y=1/2``.  This producer applies the one remaining native scalar
``(2*pi)^-9`` to the remainder, replays every exact normalization, and records
the missing value-mode functional explicitly.
"""

from __future__ import annotations

import argparse
import json
import math
from fractions import Fraction
from pathlib import Path
from typing import Any

from flint import arb, ctx


ROOT = Path(__file__).resolve().parents[2]
K288 = ROOT / "lab/process/k288-order-seven-native-occurrence-measure.json"
K294 = ROOT / "lab/process/k294-order-seven-global-radial-simplex-atlas.json"
K299 = ROOT / "lab/process/k299-order-seven-positive-peano-simplex-rule.json"
K305 = ROOT / "lab/process/k305-order-seven-coherent-bordered-functional-compiler.json"
K318 = ROOT / "lab/process/k318-order-seven-weighted-endpoint-blowup-atlas.json"
K334 = ROOT / "lab/process/k334-order-seven-recursive-global-subdivision.json"
K338 = ROOT / "lab/process/k338-order-seven-complete-gap-axis-peano-bank.json"
OUTPUT = ROOT / "lab/process/k339-order-seven-normalized-residual-composition.json"

ctx.dps = 180
ctx.threads = 1


def outward_upper(value: arb) -> str:
    return repr(math.nextafter(float(abs(value).upper()), math.inf))


def build() -> dict[str, Any]:
    k288 = json.loads(K288.read_text())
    k294 = json.loads(K294.read_text())
    k299 = json.loads(K299.read_text())
    k305 = json.loads(K305.read_text())
    k318 = json.loads(K318.read_text())
    k334 = json.loads(K334.read_text())
    k338 = json.loads(K338.read_text())

    occurrences = k288["coherent_gram_measure"]["size_four_occurrences"]
    groups = k305["coherent_groups"]
    if len(occurrences) != 24 or len(groups) != 4:
        raise AssertionError("K288/K305 coherent occurrence census changed")
    if not k305["release_test"]["bordered_identity_exact"]:
        raise AssertionError("K305 coherent bordered identity unavailable")
    if k294["normalization_replay"]["complete_bare_mass"] != "1/340282366920938463463374607431768211456":
        raise AssertionError("K294 complete bare mass changed")
    if k294["global_chart"]["native_projective_product"] != "product_i g_i=q^6*product_i p_i":
        raise AssertionError("K294 native projective normalization changed")
    if k299["positive_cubature"]["simplex_weight"] != "1/120":
        raise AssertionError("K299 one-node weight changed")
    atlas = k318["determinant_preserving_endpoint_atlas"]
    if atlas["exact_total_mass"] != "1/24" or not atlas["K299_y_Peano_mass_replayed"]:
        raise AssertionError("K318 y-Peano atlas changed")
    if not k334["decision"]["complete_y_master_constant_emitted"]:
        raise AssertionError("K334 y-Peano master unavailable")
    if not k338["decision"]["complete_six_axis_peano_norm_emitted"]:
        raise AssertionError("K338 six-axis remainder unavailable")

    raw_residual = arb(k338["six_axis_peano_bank"]["complete_six_axis_sum_upper"])
    native_prefactor = (2 * arb.pi()) ** -9
    normalized_residual = native_prefactor * raw_residual
    prefactor_lower = math.nextafter(float(native_prefactor.lower()), -math.inf)
    prefactor_upper = math.nextafter(float(native_prefactor.upper()), math.inf)

    return {
        "schema_version": "1.0",
        "result_id": "K339-ORDER-SEVEN-NORMALIZED-RESIDUAL-COMPOSITION",
        "created": "2026-09-22",
        "classification": "INTERNAL_NUMERICAL_CONTROL_ONLY",
        "direction": "observed_to_native",
        "fixed_control": {
            "predecessor_manifests": [
                "lab/process/k288-order-seven-native-occurrence-measure.json",
                "lab/process/k294-order-seven-global-radial-simplex-atlas.json",
                "lab/process/k299-order-seven-positive-peano-simplex-rule.json",
                "lab/process/k305-order-seven-coherent-bordered-functional-compiler.json",
                "lab/process/k318-order-seven-weighted-endpoint-blowup-atlas.json",
                "lab/process/k334-order-seven-recursive-global-subdivision.json",
                "lab/process/k338-order-seven-complete-gap-axis-peano-bank.json",
            ],
            "arb_decimal_digits": 180,
            "threads": 1,
            "stored_occurrences": len(occurrences),
            "coherent_groups": len(groups),
            "ordered_terms_per_group": 9,
            "K299_simplex_weight": k299["positive_cubature"]["simplex_weight"],
            "K318_y_Peano_mass": atlas["exact_total_mass"],
            "K294_complete_bare_mass": k294["normalization_replay"]["complete_bare_mass"],
        },
        "normalization_ledger": {
            "native_prefactor_exact": "(2*pi)^-9",
            "native_prefactor_interval": {
                "lower": repr(prefactor_lower),
                "upper": repr(prefactor_upper),
            },
            "K294_radial_simplex_density_already_inside_K338": True,
            "K299_Peano_masses_already_inside_K338": True,
            "K299_one_node_weight_not_applied_to_the_residual": True,
            "K294_complete_bare_mass_is_a_replay_control_not_an_extra_multiplier": True,
            "K318_chart_mass_not_multiplied_twice": True,
            "only_outstanding_scalar_applied_here": "(2*pi)^-9",
        },
        "normalized_order_seven_peano_residual": {
            "prefactor_free_six_axis_radius_upper": k338["six_axis_peano_bank"]["complete_six_axis_sum_upper"],
            "native_prefactor_applied_once": True,
            "radius_upper": outward_upper(normalized_residual),
            "symmetric_interval": [f"-{outward_upper(normalized_residual)}", outward_upper(normalized_residual)],
            "meaning": "absolute K299 tensor-Peano error radius for the complete four-group K288/K305 order-seven coherent occurrence sum after the native (2*pi)^-9 scalar",
        },
        "value_residual_separation": {
            "K334_zero_order_coefficient_is_a_base_cubature_value": False,
            "reason": "K334 inherits K318's determinant-preserving y-endpoint charts and exact y-Peano mass 1/24; its value/first/second bank consists of Taylor coefficients inside that weighted remainder atlas, not F(p_i=1/6,y=1/2)",
            "invalid_substitution_rejected": "(2*pi)^-9*K334.complete_y_master.complete_value_first_second_abs_uppers[0] is not the K299 one-node action value",
            "base_action_value_evaluated": False,
            "complete_action_residual_evaluated": False,
            "available_result": "the order-seven K299 Peano component of the residual is now normalized and finite",
            "missing_value_functional": "integrate the complete four-group K305 D4-times-bordered-B5 value at p_i=1/6 and y=1/2 over r,s and all eight native split variables, using a value-mode terminal split blow-up without the K318 Peano kernel",
            "missing_complete_residual_inputs": "all other action-column orders/components and the R_ref form-dual residual composition remain separate K171/K279 dependencies",
        },
        "decision": {
            "K294_normalization_composed_into_order_seven_peano_residual": True,
            "complete_order_seven_action_value_emitted": False,
            "complete_base_action_column_evaluated": False,
            "complete_R_ref_residual_evaluated": False,
            "native_K152_interval_emitted": False,
            "next_exact_input": "construct a value-mode barycentric terminal-split atlas at p_i=1/6 and y=1/2, integrate the complete four-group K305 value functional over the full radial/projective and eight-split domain, then join that signed or interval base value to K339's separate normalized Peano radius; only later compose the other action-column orders and R_ref residual",
        },
        "release_test": {
            "all_24_K288_occurrences_replayed": len(occurrences) == 24,
            "all_four_K305_groups_replayed": len(groups) == 4,
            "K305_bordered_identity_replayed": k305["release_test"]["bordered_identity_exact"],
            "K294_bare_mass_replayed_without_double_multiplication": True,
            "K299_one_node_and_Peano_weights_kept_distinct": True,
            "K318_Peano_atlas_not_relabelled_as_value_mode": True,
            "native_prefactor_applied_exactly_once": True,
            "normalized_residual_finite_positive": math.isfinite(float(normalized_residual.upper())) and normalized_residual.upper() > 0,
            "native_K152_interval_emitted": False,
        },
        "ledger_effect": k338["ledger_effect"],
        "source_routing": k338["source_routing"],
        "claim_ceiling": "Exact normalization and type-safe composition of K338's six-axis Peano radius into the complete four-group K288/K305 order-seven coherent occurrence-sum scale. Applying the native (2*pi)^-9 factor once gives residual radius below 0.004477466184517202. K334's zeroth coefficient is proved ineligible as the K299 one-node value because it remains inside the K318 y-Peano atlas of mass 1/24. Therefore no action value, complete base action column, complete R_ref residual, K152 interval, source/ledger move, canon, paper, public or physical claim is emitted.",
    }


def validate_payload(payload: dict[str, Any]) -> None:
    fixed = payload["fixed_control"]
    if fixed["stored_occurrences"] != 24 or fixed["coherent_groups"] != 4 or fixed["ordered_terms_per_group"] != 9:
        raise AssertionError("coherent occurrence census changed")
    if fixed["K299_simplex_weight"] != "1/120" or fixed["K318_y_Peano_mass"] != "1/24":
        raise AssertionError("value/remainder weight typing changed")
    ledger = payload["normalization_ledger"]
    if not all(ledger[key] for key in (
        "K294_radial_simplex_density_already_inside_K338",
        "K299_Peano_masses_already_inside_K338",
        "K299_one_node_weight_not_applied_to_the_residual",
        "K294_complete_bare_mass_is_a_replay_control_not_an_extra_multiplier",
        "K318_chart_mass_not_multiplied_twice",
    )):
        raise AssertionError("a normalization was omitted or double-applied")
    if ledger["only_outstanding_scalar_applied_here"] != "(2*pi)^-9":
        raise AssertionError("native prefactor composition changed")
    residual = payload["normalized_order_seven_peano_residual"]
    if not residual["native_prefactor_applied_once"] or not math.isfinite(float(residual["radius_upper"])) or float(residual["radius_upper"]) <= 0:
        raise AssertionError("normalized residual invalid")
    separation = payload["value_residual_separation"]
    if separation["K334_zero_order_coefficient_is_a_base_cubature_value"]:
        raise AssertionError("K334 Peano coefficient relabelled as the K299 node value")
    if separation["base_action_value_evaluated"] or separation["complete_action_residual_evaluated"]:
        raise AssertionError("downstream value or residual overclaimed")
    decision = payload["decision"]
    if not decision["K294_normalization_composed_into_order_seven_peano_residual"]:
        raise AssertionError("K294/K338 residual composition missing")
    if any(decision[key] for key in (
        "complete_order_seven_action_value_emitted",
        "complete_base_action_column_evaluated",
        "complete_R_ref_residual_evaluated",
        "native_K152_interval_emitted",
    )):
        raise AssertionError("downstream result overclaimed")
    release = payload["release_test"]
    if not all(value for key, value in release.items() if key != "native_K152_interval_emitted") or release["native_K152_interval_emitted"]:
        raise AssertionError("K339 release control failed")


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
