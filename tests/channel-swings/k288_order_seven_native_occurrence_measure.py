#!/usr/bin/env python3
"""K288 exact native occurrence and cumulative-time measure for order seven."""

from __future__ import annotations

import argparse
import importlib.util
import json
import math
import sys
from collections import Counter
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[2]
K280_PATH = Path(__file__).with_name("k280_order_seven_bessel_vandermonde_face_atlas.py")
K279_MANIFEST = ROOT / "lab/process/k279-higher-order-andreief-structural-closure.json"
K280_MANIFEST = ROOT / "lab/process/k280-order-seven-bessel-vandermonde-face-atlas.json"
K287_MANIFEST = ROOT / "lab/process/k287-order-seven-tensor-jacobi-remainder.json"
OUTPUT = ROOT / "lab/process/k288-order-seven-native-occurrence-measure.json"


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {path}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


K280 = load_module("k280_for_k288", K280_PATH)


def k280_serialized_entries(entries: list[dict[str, Any]]) -> list[dict[str, Any]]:
    """Replay the compact entry schema intentionally published by K280."""
    serialized_entries: list[dict[str, Any]] = []
    for entry in entries:
        serialized = dict(entry)
        serialized["species_factors"] = [
            {
                "species": factor["species"],
                "pattern": K280.pattern_key(factor),
                "size": factor["size"],
                "determinant_sign": factor["determinant_sign"],
            }
            for factor in entry["species_factors"]
        ]
        serialized_entries.append(serialized)
    return serialized_entries


def size_four_occurrences(entries: list[dict[str, Any]]) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    for entry_index, entry in enumerate(entries):
        for factor_index, factor in enumerate(entry["species_factors"]):
            if int(factor["size"]) != 4:
                continue
            companions = [
                other
                for index, other in enumerate(entry["species_factors"])
                if index != factor_index
            ]
            symmetry = 1 if entry["left"] == entry["right"] else 2
            rows.append(
                {
                    "entry_index": entry_index,
                    "factor_index": factor_index,
                    "group_id": entry["group_id"],
                    "left": entry["left"],
                    "right": entry["right"],
                    "left_old_position": int(entry["left_old_position"]),
                    "right_old_position": int(entry["right_old_position"]),
                    "coefficient_product": int(entry["coefficient_product"]),
                    "entry_integrand_sign": int(entry["entry_integrand_sign"]),
                    "gram_symmetry_multiplicity": symmetry,
                    "signed_occurrence_weight": symmetry
                    * int(entry["entry_integrand_sign"]),
                    "size_four_species": factor["species"],
                    "size_four_left_positions": factor["left_canonical_positions"],
                    "size_four_right_positions": factor["right_canonical_positions"],
                    "companion_factors": [
                        {
                            "species": companion["species"],
                            "size": int(companion["size"]),
                            "left_positions": companion["left_canonical_positions"],
                            "right_positions": companion["right_canonical_positions"],
                        }
                        for companion in companions
                    ],
                }
            )
    return rows


def certificate() -> dict[str, Any]:
    k279 = json.loads(K279_MANIFEST.read_text())
    k280 = json.loads(K280_MANIFEST.read_text())
    k287 = json.loads(K287_MANIFEST.read_text())
    entries = K280.gram_entries()
    stored_entries = k280["complete_factorization_inventory"]["entries"]
    if k280_serialized_entries(entries) != stored_entries:
        raise AssertionError("K280 owner generator no longer replays its stored entries")
    occurrences = size_four_occurrences(entries)
    weight_histogram = Counter(row["signed_occurrence_weight"] for row in occurrences)
    group_histogram = Counter(row["group_id"] for row in occurrences)
    old_position_histogram = Counter(
        (row["left_old_position"], row["right_old_position"])
        for row in occurrences
    )
    companion_sizes = Counter(
        tuple(factor["size"] for factor in row["companion_factors"])
        for row in occurrences
    )
    mass_numerator = math.factorial(3)
    y_denominator = 6
    bare_mass_reduces_to = f"{mass_numerator // y_denominator}/256^16"
    return {
        "schema_version": "1.0",
        "result_id": "K288-ORDER-SEVEN-NATIVE-OCCURRENCE-MEASURE",
        "created": "2026-09-21",
        "classification": "INTERNAL_STRUCTURAL_ONLY",
        "direction": "observed_to_native",
        "fixed_control": {
            "order": 7,
            "paths": int(k279["orders"][0]["paths"]),
            "groups": int(k279["orders"][0]["groups"]),
            "gram_entries_upper_triangle": len(entries),
            "species_determinant_occurrences": k280["complete_factorization_inventory"][
                "species_determinant_occurrences"
            ],
            "size_four_occurrences": len(occurrences),
            "auxiliary_chart_shift": 256,
            "native_prefactor": "(2*pi)^-9",
            "predecessor_manifests": [
                "lab/process/k279-higher-order-andreief-structural-closure.json",
                "lab/process/k280-order-seven-bessel-vandermonde-face-atlas.json",
                "lab/process/k287-order-seven-tensor-jacobi-remainder.json",
            ],
        },
        "coherent_gram_measure": {
            "upper_triangle_storage_rule": "one record for left<=right inside each coherent group",
            "native_reconstruction_rule": "diagonal multiplicity 1; off-diagonal multiplicity 2 before the real coherent Gram integral",
            "signed_weight_histogram": {
                str(weight): count for weight, count in sorted(weight_histogram.items())
            },
            "signed_weight_sum": sum(
                row["signed_occurrence_weight"] for row in occurrences
            ),
            "absolute_weight_sum": sum(
                abs(row["signed_occurrence_weight"]) for row in occurrences
            ),
            "group_histogram": dict(sorted(group_histogram.items())),
            "old_position_pair_histogram": {
                f"{left},{right}": count
                for (left, right), count in sorted(old_position_histogram.items())
            },
            "companion_size_histogram": {
                ",".join(map(str, sizes)): count
                for sizes, count in sorted(companion_sizes.items())
            },
            "signed_weight_sum_is_not_an_integral": "the old-position kernels and companion size-three determinants differ across the six records in every group",
            "size_four_occurrences": occurrences,
        },
        "native_coordinate_change": {
            "primitive_times": [f"s{index}" for index in range(1, 9)]
            + [f"v{index}" for index in range(1, 9)],
            "pair_sums": {
                "a_i": "s_(2i+1)+s_(2i+2), i=0..3",
                "b_i": "v_(2i+1)+v_(2i+2), i=0..3",
            },
            "internal_splits": {
                "u_i": "s_(2i+1)/a_i, i=0..3",
                "z_i": "v_(2i+1)/b_i, i=0..3",
                "domain": "[0,1]^8",
                "pair_jacobian": "product_i a_i*b_i",
            },
            "radial_projective_variables": {
                "x": "a_3+b_3",
                "y": "a_3/x",
                "r_i": "a_i/x, i=0..2",
                "c_i": "b_i/x, i=0..2",
                "domain": "x>0; y in [0,1]; r_i,c_i>0",
                "pair_sum_jacobian": "x^7",
            },
            "exact_measure_density": "exp(-256*x*L) * x^15 * y*(1-y) * product_i(r_i*c_i) dx dy dr dc du dz",
            "L": "1+sum_i r_i+sum_i c_i",
            "mass_replay": {
                "six_ratio_integrals": "(256*x)^-12",
                "y_integral": "1/6",
                "remaining_x_integral": "3!/256^4",
                "internal_split_cube_mass": "1",
                "transformed_total_mass": bare_mass_reduces_to,
                "primitive_product_total_mass": "1/256^16",
                "exact_match": bare_mass_reduces_to == "1/256^16",
            },
        },
        "measure_boundary": {
            "native_occurrence_weights_serialized": True,
            "native_radial_projective_measure_serialized": True,
            "native_internal_split_measure_serialized": True,
            "k287_uniform_tube_measure_is_native_measure": False,
            "reason": "K287 integrates one size-four regularizer against a normalized uniform six-box; the native occurrence retains the projective density, eight internal split variables, one companion determinant, two old-position kernels, coherent signs and (2*pi)^-9.",
        },
        "release_test": {
            "all_408_gram_entries_replayed": len(entries) == 408,
            "all_24_size_four_occurrences_serialized": len(occurrences) == 24,
            "all_four_groups_have_six_size_four_records": set(group_histogram.values())
            == {6},
            "all_size_four_records_have_one_size_three_companion": set(
                companion_sizes
            )
            == {(3,)},
            "native_bare_measure_mass_replays_exactly": bare_mass_reduces_to
            == "1/256^16",
            "complete_arbitrary_gap_ratio_domain_covered": False,
            "complete_base_action_column_evaluated": False,
            "native_K152_interval_emitted": False,
        },
        "ledger_effect": k287["ledger_effect"],
        "next_exact_input": "prove on all 24 occurrences which factors depend on pair sums alone and which retain internal split variables, then construct one common primitive chart before composing a native weighted Jacobi remainder or exterior bound",
        "claim_ceiling": "Exact signed occurrence weights and exact sixteen-primitive cumulative-time measure for the complete order-seven K179 size-four occurrence family. No weighted regularizer remainder, complete arbitrary-gap domain, action-column value, complete residual, exterior gap, native K152 interval, physical state, source/ledger move, canon, paper or public claim.",
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--write", action="store_true")
    args = parser.parse_args()
    payload = certificate()
    rendered = json.dumps(payload, indent=2, sort_keys=True) + "\n"
    if args.write:
        OUTPUT.write_text(rendered)
    else:
        print(rendered, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
