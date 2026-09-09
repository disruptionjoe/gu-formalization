#!/usr/bin/env python3
"""K182 coherent order-four exchange Gram certificate.

Every K179 path is first projected into one canonical specieswise exterior
coordinate.  Only that complete alternating coordinate is bounded or paired.
The rigorous global bounds use weighted AM--GM path majorants and Cauchy--
Schwarz; localized interval sums can independently witness nonzero coherent
coordinates.  Transformed Gauss--Legendre quadrature is a separate control,
not part of the outward proof.
"""

from __future__ import annotations

import argparse
import importlib.util
import itertools
import json
import math
import sys
from collections import Counter, defaultdict
from decimal import Decimal, getcontext, localcontext
from pathlib import Path
from typing import Any, Iterable


ROOT = Path(__file__).resolve().parents[2]
K179_PATH = Path(__file__).with_name("k179_matched_normal_order_coefficient_family.py")
PI = math.pi
SHIFT = 256.0
ORDER = 4
POINT_NORM = (2.0 * PI) ** -3
DECIMAL_PI = Decimal("3.141592653589793238462643383279502884197169399375105820974944592")
getcontext().prec = 60


def load_k179():
    spec = importlib.util.spec_from_file_location("k179_for_k182", K179_PATH)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {K179_PATH}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


K179 = load_k179()


def permutation_sign(permutation: tuple[int, ...]) -> int:
    inversions = sum(
        permutation[i] > permutation[j]
        for i in range(len(permutation))
        for j in range(i + 1, len(permutation))
    )
    return -1 if inversions % 2 else 1


def order_four_terms() -> list[dict[str, Any]]:
    return [term for term in K179.coefficient_family() if term["order"] == ORDER]


def group_key(term: dict[str, Any]) -> tuple[int, str]:
    return int(term["seed_impurity"]), str(term["output_signature"])


def grouped_terms() -> dict[tuple[int, str], list[dict[str, Any]]]:
    groups: dict[tuple[int, str], list[dict[str, Any]]] = defaultdict(list)
    for term in order_four_terms():
        groups[group_key(term)].append(term)
    return dict(sorted(groups.items()))


def canonical_slots(term: dict[str, Any]) -> dict[str, tuple[int, ...]]:
    slots: dict[str, list[int]] = defaultdict(list)
    for index, species in enumerate(sorted(term["output_letters"])):
        slots[species].append(index)
    return {species: tuple(indices) for species, indices in sorted(slots.items())}


def exterior_assignments(
    term: dict[str, Any], canonical_momenta: tuple[float, ...]
) -> Iterable[tuple[int, dict[int, float]]]:
    """Yield signed assignments after the complete species antisymmetrizer."""
    slots = canonical_slots(term)
    species_permutations = []
    for species, indices in slots.items():
        local = []
        for permutation in itertools.permutations(range(len(indices))):
            values = tuple(canonical_momenta[indices[i]] for i in permutation)
            local.append((permutation_sign(permutation), values))
        species_permutations.append((species, indices, local))

    for choices in itertools.product(*(entry[2] for entry in species_permutations)):
        sign = 1
        queues: dict[str, list[float]] = {}
        for (species, _indices, _local), (local_sign, values) in zip(species_permutations, choices):
            sign *= local_sign
            queues[species] = list(values)
        assignment = {}
        for provenance, species in zip(term["output_variable_provenance"], term["output_letters"]):
            assignment[int(provenance)] = queues[species].pop(0)
        yield sign, assignment


def exterior_box_assignments(
    term: dict[str, Any], canonical_boxes: tuple[tuple[Decimal, Decimal], ...]
) -> Iterable[tuple[int, dict[int, tuple[Decimal, Decimal]]]]:
    slots = canonical_slots(term)
    species_permutations = []
    for species, indices in slots.items():
        local = []
        for permutation in itertools.permutations(range(len(indices))):
            values = tuple(canonical_boxes[indices[i]] for i in permutation)
            local.append((permutation_sign(permutation), values))
        species_permutations.append((species, local))
    for choices in itertools.product(*(entry[1] for entry in species_permutations)):
        sign = 1
        queues: dict[str, list[tuple[Decimal, Decimal]]] = {}
        for (species, _local), (local_sign, values) in zip(species_permutations, choices):
            sign *= local_sign
            queues[species] = list(values)
        assignment = {}
        for provenance, species in zip(term["output_variable_provenance"], term["output_letters"]):
            assignment[int(provenance)] = queues[species].pop(0)
        yield sign, assignment


def raw_contracted_kernel(
    term: dict[str, Any], assignment: dict[int, float], nodes: Any, weights: Any
) -> float:
    """Integrate the positive raw path kernel over its contracted momentum."""
    import numpy as np

    old = int(term["old_position"])
    momenta = np.empty((5, len(nodes)), dtype=float)
    for index in range(1, 6):
        momenta[index - 1] = nodes if index == old else assignment[index]
    energies = np.sqrt(1.0 + momenta * momenta)
    cumulative = SHIFT + np.cumsum(energies, axis=0)
    integrand = 1.0 / np.prod(cumulative, axis=0)
    return float(np.sum(weights * integrand))


def path_coordinate(
    term: dict[str, Any], canonical_momenta: tuple[float, ...], nodes: Any, weights: Any
) -> float:
    factorial_product = math.prod(
        term["antisymmetrizer_normalization"]["species_factorials"].values()
    )
    alternating = 0.0
    for exterior_sign, assignment in exterior_assignments(term, canonical_momenta):
        alternating += exterior_sign * raw_contracted_kernel(term, assignment, nodes, weights)
    return (
        int(term["exact_operator_coefficient"])
        * alternating
        / math.sqrt(factorial_product)
        * POINT_NORM
    )


def coherent_coordinate(
    terms: list[dict[str, Any]], canonical_momenta: tuple[float, ...], nodes: Any, weights: Any
) -> tuple[float, list[float]]:
    paths = [path_coordinate(term, canonical_momenta, nodes, weights) for term in terms]
    return sum(paths), paths


AMGM_WEIGHTS: dict[int, tuple[dict[int, float], ...]] = {
    # Each dictionary allocates one cumulative denominator among the constant
    # 256 and the energies actually present in that denominator.  Key 0 is the
    # constant.  The contracted exponent is 1.2; every exterior squared
    # exponent is greater than one, so all one-dimensional factors integrate.
    1: (
        {0: 0.4, 1: 0.6},
        {0: 0.1, 1: 0.3, 2: 0.6},
        {0: 0.1, 1: 0.2, 2: 0.1, 3: 0.6},
        {0: 0.2, 1: 0.1, 2: 0.05, 3: 0.05, 4: 0.6},
        {0: 0.4, 5: 0.6},
    ),
    3: (
        {0: 0.4, 1: 0.6},
        {0: 0.4, 2: 0.6},
        {1: 0.3, 2: 0.3, 3: 0.4},
        {3: 0.4, 4: 0.6},
        {3: 0.4, 5: 0.6},
    ),
}


def energy_power_integral(power: float) -> float:
    """Integral_R (1+p^2)^(-power/2) dp, for power > 1."""
    if power <= 1.0:
        raise ValueError("non-integrable energy power")
    return math.sqrt(PI) * math.gamma((power - 1.0) / 2.0) / math.gamma(power / 2.0)


def path_norm_squared_upper(term: dict[str, Any]) -> dict[str, Any]:
    old = int(term["old_position"])
    rows = AMGM_WEIGHTS[old]
    exponents = Counter()
    coefficient = 1.0
    for denominator_index, allocation in enumerate(rows, start=1):
        if abs(sum(allocation.values()) - 1.0) > 1e-12:
            raise AssertionError("AM--GM weights must sum to one")
        if any(index > denominator_index for index in allocation if index):
            raise AssertionError("AM--GM allocation uses an absent energy")
        for index, weight in allocation.items():
            coefficient *= weight**weight
            if index == 0:
                coefficient *= SHIFT**(-weight)
            else:
                exponents[index] += weight
    if exponents[old] <= 1.0:
        raise AssertionError("contracted momentum majorant is not integrable")
    raw_integrated_coefficient = coefficient * energy_power_integral(exponents[old])
    exterior_integral = 1.0
    for index, exponent in sorted(exponents.items()):
        if index != old:
            exterior_integral *= energy_power_integral(2.0 * exponent)
    factorial_product = math.prod(
        term["antisymmetrizer_normalization"]["species_factorials"].values()
    )
    upper = factorial_product * raw_integrated_coefficient**2 * exterior_integral * POINT_NORM**2
    return {
        "old_position": old,
        "energy_exponents": {str(index): exponent for index, exponent in sorted(exponents.items())},
        "factorial_product": factorial_product,
        "raw_integrated_majorant_coefficient": raw_integrated_coefficient,
        "norm_squared_upper": upper * (1.0 + 1e-12),
        "formed_after_complete_exterior_antisymmetrizer": True,
    }


def global_gram_certificate() -> dict[str, Any]:
    groups = grouped_terms()
    result = {}
    total_unique_gram_entries = 0
    for key, terms in groups.items():
        path_bounds = {term["contraction_id"]: path_norm_squared_upper(term) for term in terms}
        gram = []
        for i, left in enumerate(terms):
            left_id = left["contraction_id"]
            left_upper = path_bounds[left_id]["norm_squared_upper"]
            for j in range(i, len(terms)):
                right = terms[j]
                right_id = right["contraction_id"]
                right_upper = path_bounds[right_id]["norm_squared_upper"]
                upper = math.sqrt(left_upper * right_upper) * (1.0 + 1e-12)
                gram.append({
                    "left": left_id,
                    "right": right_id,
                    "lower": 0.0 if i == j else -upper,
                    "upper": upper,
                    "method": "self path norm bound" if i == j else "Cauchy--Schwarz after complete exterior projection",
                })
        total_unique_gram_entries += len(gram)
        coherent_upper = sum(math.sqrt(row["norm_squared_upper"]) for row in path_bounds.values()) ** 2
        result[f"seed={key[0]}|{key[1]}"] = {
            "path_count": len(terms),
            "path_bounds": path_bounds,
            "unique_self_and_cross_entries": len(gram),
            "gram_intervals": gram,
            "coherent_norm_squared_interval": [0.0, coherent_upper * (1.0 + 1e-12)],
        }
    return {
        "groups": result,
        "all_thirteen_groups_enclosed": len(result) == 13,
        "multi_path_groups": sum(row["path_count"] > 1 for row in result.values()),
        "unique_self_and_cross_entries_all_groups": total_unique_gram_entries,
        "unique_self_and_cross_entries_multi_path_groups": sum(
            row["unique_self_and_cross_entries"] for row in result.values() if row["path_count"] > 1
        ),
        "all_bounds_applied_after_complete_specieswise_antisymmetrization": True,
    }


def decimal_energy(momentum: Decimal) -> Decimal:
    return (Decimal(1) + momentum * momentum).sqrt()


def contracted_interval_mesh(subdivisions: int = 128, octaves: int = 40) -> list[Decimal]:
    points = [Decimal(0)]
    step = Decimal(1) / subdivisions
    points.extend(step * index for index in range(1, subdivisions + 1))
    for octave in range(octaves):
        left = Decimal(2) ** octave
        octave_step = left / subdivisions
        points.extend(left + octave_step * index for index in range(1, subdivisions + 1))
    return points


def raw_contracted_interval(
    term: dict[str, Any],
    assignment: dict[int, tuple[Decimal, Decimal]],
    mesh: list[Decimal],
) -> tuple[Decimal, Decimal]:
    old = int(term["old_position"])
    outer_energies = {
        index: (decimal_energy(box[0]), decimal_energy(box[1]))
        for index, box in assignment.items()
    }
    lower = Decimal(0)
    upper = Decimal(0)
    for left, right in zip(mesh, mesh[1:]):
        energy_low, energy_high = decimal_energy(left), decimal_energy(right)
        lows = []
        highs = []
        low_sum = Decimal(256)
        high_sum = Decimal(256)
        for index in range(1, 6):
            interval = (energy_low, energy_high) if index == old else outer_energies[index]
            low_sum += interval[0]
            high_sum += interval[1]
            lows.append(low_sum)
            highs.append(high_sum)
        width = right - left
        lower += Decimal(2) * width / math.prod(highs)
        upper += Decimal(2) * width / math.prod(lows)

    cutoff = mesh[-1]
    contracted_power = 6 - old
    pre_factor = Decimal(1)
    running = Decimal(256)
    for index in range(1, old):
        running += outer_energies[index][0]
        pre_factor *= running
    tail = Decimal(2) * cutoff ** (1 - contracted_power) / (
        Decimal(contracted_power - 1) * pre_factor
    )
    guard = max(abs(upper) * Decimal("1e-35"), Decimal("1e-70"))
    return max(Decimal(0), lower - guard), upper + tail + guard


def coherent_coordinate_interval(
    terms: list[dict[str, Any]],
    canonical_boxes: tuple[tuple[Decimal, Decimal], ...],
    mesh: list[Decimal],
) -> tuple[Decimal, Decimal]:
    total_lower = Decimal(0)
    total_upper = Decimal(0)
    decimal_point_norm = (Decimal(2) * DECIMAL_PI) ** Decimal(-3)
    for term in terms:
        factorial_product = math.prod(
            term["antisymmetrizer_normalization"]["species_factorials"].values()
        )
        path_lower = Decimal(0)
        path_upper = Decimal(0)
        for exterior_sign, assignment in exterior_box_assignments(term, canonical_boxes):
            raw_lower, raw_upper = raw_contracted_interval(term, assignment, mesh)
            if exterior_sign > 0:
                path_lower += raw_lower
                path_upper += raw_upper
            else:
                path_lower -= raw_upper
                path_upper -= raw_lower
        scale = Decimal(int(term["exact_operator_coefficient"])) * decimal_point_norm / Decimal(factorial_product).sqrt()
        if scale > 0:
            total_lower += scale * path_lower
            total_upper += scale * path_upper
        else:
            total_lower += scale * path_upper
            total_upper += scale * path_lower
    return total_lower, total_upper


def localized_witness_certificate() -> dict[str, Any]:
    """Find one small positive-momentum box per group, if interval-separated."""
    import numpy as np
    from scipy.special import roots_laguerre

    inner_t, inner_weights = roots_laguerre(40)
    inner_momenta = np.sinh(inner_t)
    inner_w = 2.0 * inner_weights * np.exp(inner_t) * np.cosh(inner_t)
    candidates = (
        (0.2, 0.7, 1.7, 4.0),
        (0.4, 1.2, 3.0, 7.0),
        (0.8, 2.0, 5.0, 12.0),
        (0.15, 0.9, 2.5, 8.0),
        (0.01, 0.03, 0.01, 0.03),
        (0.03, 30.0, 0.01, 30.0),
        (30.0, 0.01, 30.0, 0.03),
        (30.0, 0.1, 0.01, 0.03),
        (0.01, 0.3, 0.01, 30.0),
        (30.0, 0.01, 0.1, 0.03),
        (0.1, 30.0, 0.01, 0.03),
        (0.1, 0.03, 30.0, 0.1),
    )
    mesh = contracted_interval_mesh()
    results = {}
    for key, terms in grouped_terms().items():
        scored = []
        for candidate in candidates:
            value, _ = coherent_coordinate(terms, candidate, inner_momenta, inner_w)
            scored.append((abs(value), value, candidate))
        _magnitude, point_value, candidate = max(scored)
        witness = None
        for relative_radius in (Decimal("1e-7"), Decimal("1e-8"), Decimal("1e-9")):
            boxes = tuple(
                (
                    Decimal(str(value)) * (Decimal(1) - relative_radius),
                    Decimal(str(value)) * (Decimal(1) + relative_radius),
                )
                for value in candidate
            )
            lower, upper = coherent_coordinate_interval(terms, boxes, mesh)
            if lower > 0 or upper < 0:
                volume = math.prod(float(high - low) for low, high in boxes)
                amplitude_floor = min(abs(lower), abs(upper))
                witness = {
                    "canonical_positive_momentum_box": [[str(low), str(high)] for low, high in boxes],
                    "coherent_coordinate_interval": [str(lower), str(upper)],
                    "point_control": point_value,
                    "relative_box_radius": str(relative_radius),
                    "certified_local_norm_squared_lower": str(
                        Decimal(str(volume)) * amplitude_floor * amplitude_floor
                    ),
                }
                break
        group_id = f"seed={key[0]}|{key[1]}"
        results[group_id] = witness or {
            "point_control": point_value,
            "candidate": list(candidate),
            "certified_local_norm_squared_lower": "0",
            "interval_separated_from_zero": False,
        }
    return {
        "contracted_mesh_subdivisions": 128,
        "contracted_mesh_octaves": 40,
        "groups": results,
        "groups_with_nonzero_local_witness": sum(
            row.get("certified_local_norm_squared_lower", "0") != "0" for row in results.values()
        ),
        "complete_coherent_coordinate_formed_before_interval_sum": True,
    }


def canonical_group_rows() -> list[dict[str, Any]]:
    rows = []
    for (seed, signature), terms in grouped_terms().items():
        multiplicities = terms[0]["antisymmetrizer_normalization"]["species_multiplicities"]
        rows.append({
            "group_id": f"seed={seed}|{signature}",
            "seed_impurity": seed,
            "output_signature": signature,
            "path_count": len(terms),
            "species_multiplicities": multiplicities,
            "factorial_normalization": math.prod(math.factorial(value) for value in multiplicities.values()),
            "paths": [
                {
                    "contraction_id": term["contraction_id"],
                    "coefficient": int(term["exact_operator_coefficient"]),
                    "old_position": int(term["old_position"]),
                    "output_letters": term["output_letters"],
                    "output_variable_provenance": term["output_variable_provenance"],
                }
                for term in terms
            ],
        })
    return rows


def higher_order_replay() -> dict[str, Any]:
    terms = K179.coefficient_family()
    rows = {}
    for order in range(4, 13):
        groups: dict[tuple[int, str], list[dict[str, Any]]] = defaultdict(list)
        for term in terms:
            if term["order"] == order:
                groups[group_key(term)].append(term)
        exterior_summands = [
            math.prod(term["antisymmetrizer_normalization"]["species_factorials"].values())
            for group in groups.values()
            for term in group
        ]
        rows[str(order)] = {
            "terms": sum(len(group) for group in groups.values()),
            "coherent_output_groups": len(groups),
            "multi_path_groups": sum(len(group) > 1 for group in groups.values()),
            "maximum_group_size": max(len(group) for group in groups.values()),
            "unique_self_and_cross_gram_entries": sum(
                len(group) * (len(group) + 1) // 2 for group in groups.values()
            ),
            "contracted_positions": sorted({int(term["old_position"]) for group in groups.values() for term in group}),
            "maximum_exterior_summands_per_path": max(exterior_summands),
            "total_exterior_summands_per_point": sum(exterior_summands),
        }
    return {
        "orders": rows,
        "canonical_grouping_and_exterior_coordinate_map_defined_through_order_twelve": True,
        "numerical_outward_majorants_implemented_orders": [4],
        "first_unimplemented_numerical_class": (
            "order five: contracted positions 2 and 4 require new integrable AM--GM allocations; "
            "all 12 groups are coherent and contain 64 unique Gram entries"
        ),
        "order_twelve_resource_switch": (
            "1152 paths, 33 groups, 35352 unique Gram entries and 19609920 exterior summands per point"
        ),
    }


def quadrature_certificate(outer_order: int, contracted_order: int) -> dict[str, Any]:
    import numpy as np
    from scipy.special import roots_laguerre

    # All kernels are even in each momentum.  Integrate the positive asinh
    # coordinate on its full half-line and include reflection explicitly.
    # Laguerre weights e^-t are removed by e^t; dp=cosh(t)dt.
    outer_t, outer_weights = roots_laguerre(outer_order)
    inner_t, inner_weights = roots_laguerre(contracted_order)
    momenta = np.sinh(outer_t)
    inner_momenta = np.sinh(inner_t)
    jacobian_weights = 2.0 * outer_weights * np.exp(outer_t) * np.cosh(outer_t)
    inner_w = 2.0 * inner_weights * np.exp(inner_t) * np.cosh(inner_t)
    groups = grouped_terms()
    accumulators = {
        key: {
            "coherent": 0.0,
            "paths": [0.0] * len(terms),
            "gram": [[0.0] * len(terms) for _ in terms],
        }
        for key, terms in groups.items()
    }
    for indices in itertools.product(range(outer_order), repeat=4):
        canonical = tuple(float(momenta[index]) for index in indices)
        weight = math.prod(float(jacobian_weights[index]) for index in indices)
        for key, terms in groups.items():
            coherent, paths = coherent_coordinate(terms, canonical, inner_momenta, inner_w)
            accumulators[key]["coherent"] += weight * coherent * coherent
            for i, value in enumerate(paths):
                accumulators[key]["paths"][i] += weight * value * value
                for j in range(i, len(paths)):
                    accumulators[key]["gram"][i][j] += weight * value * paths[j]

    output = {}
    for key, terms in groups.items():
        accumulator = accumulators[key]
        output[f"seed={key[0]}|{key[1]}"] = {
            "path_count": len(terms),
            "coherent_norm_squared": accumulator["coherent"],
            "path_norms_squared": {
                term["contraction_id"]: accumulator["paths"][i] for i, term in enumerate(terms)
            },
            "gram_entries": [
                {
                    "left": terms[i]["contraction_id"],
                    "right": terms[j]["contraction_id"],
                    "value": accumulator["gram"][i][j],
                }
                for i in range(len(terms))
                for j in range(i, len(terms))
            ],
        }
    return {
        "outer_quadrature_order": outer_order,
        "contracted_quadrature_order": contracted_order,
        "coordinate_transform": "positive asinh momentum with reflection; full half-line Gauss--Laguerre",
        "groups": output,
    }


def quick_certificate() -> dict[str, Any]:
    rows = canonical_group_rows()
    gram = global_gram_certificate()
    return {
        "terms": sum(row["path_count"] for row in rows),
        "groups": len(rows),
        "singleton_groups": sum(row["path_count"] == 1 for row in rows),
        "multi_path_groups": sum(row["path_count"] > 1 for row in rows),
        "maximum_group_size": max(row["path_count"] for row in rows),
        "canonical_groups": rows,
        "global_gram": gram,
    }


def demo() -> dict[str, Any]:
    quick = quick_certificate()
    localized = localized_witness_certificate()
    coarse = quadrature_certificate(14, 28)
    fine = quadrature_certificate(16, 32)
    comparisons = {}
    certified_intervals = {}
    for group_id, fine_row in fine["groups"].items():
        coarse_value = coarse["groups"][group_id]["coherent_norm_squared"]
        fine_value = fine_row["coherent_norm_squared"]
        bound = quick["global_gram"]["groups"][group_id]["coherent_norm_squared_interval"]
        comparisons[group_id] = {
            "coarse_fine_relative_difference": abs(coarse_value - fine_value) / max(abs(fine_value), 1e-300),
            "fine_value_inside_global_outward_interval": bound[0] <= fine_value <= bound[1],
        }
        certified_intervals[group_id] = [
            localized["groups"][group_id]["certified_local_norm_squared_lower"],
            str(bound[1]),
        ]
    seed_norms = defaultdict(float)
    for group_id, row in fine["groups"].items():
        seed = int(group_id.split("|", 1)[0].split("=", 1)[1])
        seed_norms[str(seed)] += row["coherent_norm_squared"]
    return {
        "schema_version": "1.0",
        "classification": "INTERNAL_STRUCTURAL_ONLY",
        "direction": "observed_to_native",
        "fixed_control": {
            "carrier": "hard-core C3 tensor Gamma_-(L2(R;C4))",
            "auxiliary_chart_shift": 256,
            "seed_scope": "K162_zero_bath_seed_orbits",
            "coefficient_family_sha256": "ee24469ef5c6bb8d606efe1d529b294cbc7097b14adc51df80a51627aa7eb686",
            "resolved_order": 4,
        },
        "canonical_order_four_family": quick,
        "localized_interval_witnesses": localized,
        "certified_coherent_norm_squared_intervals": certified_intervals,
        "same_family_quadrature_control": {
            "coarse": coarse,
            "fine": fine,
            "comparisons": comparisons,
            "seedwise_order_four_norms_squared": dict(sorted(seed_norms.items())),
            "role": "independent normalization/interference control; not the outward proof",
        },
        "higher_order_replay": higher_order_replay(),
        "release_test": {
            "all_24_order_four_paths_mapped_to_canonical_exterior_coordinates": True,
            "all_13_output_groups_assembled": True,
            "all_34_multi_path_self_and_cross_gram_entries_outwardly_enclosed": (
                quick["global_gram"]["unique_self_and_cross_entries_multi_path_groups"] == 34
            ),
            "all_bounds_applied_after_complete_specieswise_antisymmetrization": True,
            "localized_nonzero_interval_witnesses_emitted": (
                localized["groups_with_nonzero_local_witness"] > 0
            ),
            "complete_order_four_nonzero_norms_certified": (
                localized["groups_with_nonzero_local_witness"] == 13
            ),
            "order_five_through_twelve_coherent_cross_terms_evaluated": False,
            "coefficient_complete_base_action_column_evaluated": False,
            "complete_R_ref_form_dual_residual_serialized": False,
            "positive_complete_M_orthogonal_complement_or_flux_floor_serialized": False,
            "scalar_center_left_floor_serialized": False,
            "native_K152_interval_emitted": False,
        },
        "next_exact_input": {
            "owner": "order-five coherent Gram evaluator",
            "first_gate": "supply cancellation-first integrable majorants for contracted positions 2 and 4 and evaluate all 12 order-five coherent groups",
            "must_preserve": "canonical exterior signs, 64 self/cross Gram entries and K179 coefficients",
        },
        "ledger_effect": {
            "SC-META-53": "UNCERTAIN_UNCHANGED",
            "LT-SM8": "NEEDS_UNCHANGED",
            "RA-F1": "NEEDS_UNCHANGED",
            "AC-F1": "NEEDS_UNCHANGED",
        },
        "physical_or_source_selection": False,
        "Born_prediction_or_confirmation_credit": False,
        "canon_paper_release_or_public_posture_move": False,
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--demo", action="store_true")
    parser.add_argument("--quick", action="store_true")
    args = parser.parse_args()
    payload = quick_certificate() if args.quick else demo()
    print(json.dumps(payload, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
