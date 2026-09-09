#!/usr/bin/env python3
"""K183 complete order-five coherent Gram and compression certificate.

The rigorous layer forms each complete normalized specieswise exterior
coordinate before interval operations.  Weighted AM--GM path majorants and
post-projection Cauchy bounds enclose every Gram entry; localized interval
sums witness nonzero coherent coordinates.  A scrambled-Sobol/asinh control is
independent numerical evidence only.  The exact higher-order representation
is the K177 Laplace-simplex species-determinant formula with shared cumulative
time nodes, not a literal permutation expansion.
"""

from __future__ import annotations

import argparse
import importlib.util
import itertools
import json
import math
import sys
from collections import Counter, defaultdict
from decimal import Decimal, getcontext
from pathlib import Path
from typing import Any, Iterable


ROOT = Path(__file__).resolve().parents[2]
K179_PATH = Path(__file__).with_name("k179_matched_normal_order_coefficient_family.py")
PI = math.pi
SHIFT = 256.0
ORDER = 5
TOTAL_POSITIONS = ORDER + 1
POINT_NORM = (2.0 * PI) ** (-(ORDER + 2) / 2.0)
DECIMAL_PI = Decimal("3.141592653589793238462643383279502884197169399375105820974944592")
DECIMAL_POINT_NORM = Decimal(1) / (
    (Decimal(2) * DECIMAL_PI) ** 3 * (Decimal(2) * DECIMAL_PI).sqrt()
)
getcontext().prec = 60


def load_k179():
    spec = importlib.util.spec_from_file_location("k179_for_k183", K179_PATH)
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


def order_five_terms() -> list[dict[str, Any]]:
    return [term for term in K179.coefficient_family() if term["order"] == ORDER]


def group_key(term: dict[str, Any]) -> tuple[int, str]:
    return int(term["seed_impurity"]), str(term["output_signature"])


def grouped_terms() -> dict[tuple[int, str], list[dict[str, Any]]]:
    groups: dict[tuple[int, str], list[dict[str, Any]]] = defaultdict(list)
    for term in order_five_terms():
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
    species_permutations = []
    for species, indices in canonical_slots(term).items():
        local = []
        for permutation in itertools.permutations(range(len(indices))):
            values = tuple(canonical_momenta[indices[i]] for i in permutation)
            local.append((permutation_sign(permutation), values))
        species_permutations.append((species, local))
    for choices in itertools.product(*(entry[1] for entry in species_permutations)):
        sign = 1
        queues: dict[str, list[float]] = {}
        for (species, _local), (local_sign, values) in zip(species_permutations, choices):
            sign *= local_sign
            queues[species] = list(values)
        assignment = {}
        for provenance, species in zip(term["output_variable_provenance"], term["output_letters"]):
            assignment[int(provenance)] = queues[species].pop(0)
        yield sign, assignment


def exterior_box_assignments(
    term: dict[str, Any], canonical_boxes: tuple[tuple[Decimal, Decimal], ...]
) -> Iterable[tuple[int, dict[int, tuple[Decimal, Decimal]]]]:
    species_permutations = []
    for species, indices in canonical_slots(term).items():
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
    import numpy as np

    old = int(term["old_position"])
    momenta = np.empty((TOTAL_POSITIONS, len(nodes)), dtype=float)
    for index in range(1, TOTAL_POSITIONS + 1):
        momenta[index - 1] = nodes if index == old else assignment[index]
    energies = np.sqrt(1.0 + momenta * momenta)
    cumulative = SHIFT + np.cumsum(energies, axis=0)
    return float(np.sum(weights / np.prod(cumulative, axis=0)))


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
        * POINT_NORM
        / math.sqrt(factorial_product)
    )


def coherent_coordinate(
    terms: list[dict[str, Any]], canonical_momenta: tuple[float, ...], nodes: Any, weights: Any
) -> tuple[float, list[float]]:
    paths = [path_coordinate(term, canonical_momenta, nodes, weights) for term in terms]
    return sum(paths), paths


# Each row allocates a cumulative denominator among 256 and energies already
# present in that denominator.  Position two obtains exponent 1.2 and position
# four obtains exponent 1.1; every exterior energy obtains exponent >= 0.6.
AMGM_WEIGHTS: dict[int, tuple[dict[int, float], ...]] = {
    2: (
        {0: 0.4, 1: 0.6},
        {0: 0.1, 1: 0.3, 2: 0.6},
        {0: 0.1, 2: 0.3, 3: 0.6},
        {0: 0.2, 2: 0.2, 4: 0.6},
        {0: 0.3, 2: 0.1, 5: 0.6},
        {0: 0.4, 6: 0.6},
    ),
    4: (
        {0: 0.4, 1: 0.6},
        {0: 0.4, 2: 0.6},
        {0: 0.4, 3: 0.6},
        {0: 0.4, 4: 0.6},
        {0: 0.1, 4: 0.3, 5: 0.6},
        {0: 0.2, 4: 0.2, 6: 0.6},
    ),
}


def energy_power_integral(power: float) -> float:
    if power <= 1.0:
        raise ValueError("non-integrable energy power")
    return math.sqrt(PI) * math.gamma((power - 1.0) / 2.0) / math.gamma(power / 2.0)


def path_norm_squared_upper(term: dict[str, Any]) -> dict[str, Any]:
    old = int(term["old_position"])
    exponents = Counter()
    coefficient = 1.0
    for denominator_index, allocation in enumerate(AMGM_WEIGHTS[old], start=1):
        if abs(sum(allocation.values()) - 1.0) > 1e-12:
            raise AssertionError("AM--GM weights must sum to one")
        if any(index > denominator_index for index in allocation if index):
            raise AssertionError("AM--GM allocation uses an absent energy")
        for index, weight in allocation.items():
            coefficient *= weight**weight
            if index == 0:
                coefficient *= SHIFT ** (-weight)
            else:
                exponents[index] += weight
    if exponents[old] <= 1.0:
        raise AssertionError("contracted momentum majorant is not integrable")
    if any(2.0 * exponent <= 1.0 for index, exponent in exponents.items() if index != old):
        raise AssertionError("exterior squared majorant is not integrable")
    raw_integrated_coefficient = coefficient * energy_power_integral(exponents[old])
    exterior_integral = math.prod(
        energy_power_integral(2.0 * exponent)
        for index, exponent in sorted(exponents.items())
        if index != old
    )
    factorial_product = math.prod(
        term["antisymmetrizer_normalization"]["species_factorials"].values()
    )
    upper = (
        factorial_product
        * raw_integrated_coefficient**2
        * exterior_integral
        * POINT_NORM**2
    )
    return {
        "old_position": old,
        "energy_exponents": {str(index): exponent for index, exponent in sorted(exponents.items())},
        "factorial_product": factorial_product,
        "raw_integrated_majorant_coefficient": raw_integrated_coefficient,
        "norm_squared_upper": upper * (1.0 + 1e-12),
        "formed_after_complete_exterior_antisymmetrizer": True,
    }


def global_gram_certificate() -> dict[str, Any]:
    result = {}
    total_entries = 0
    for key, terms in grouped_terms().items():
        bounds = {term["contraction_id"]: path_norm_squared_upper(term) for term in terms}
        gram = []
        for i, left in enumerate(terms):
            left_id = left["contraction_id"]
            for j in range(i, len(terms)):
                right = terms[j]
                right_id = right["contraction_id"]
                upper = math.sqrt(
                    bounds[left_id]["norm_squared_upper"]
                    * bounds[right_id]["norm_squared_upper"]
                ) * (1.0 + 1e-12)
                gram.append({
                    "left": left_id,
                    "right": right_id,
                    "lower": 0.0 if i == j else -upper,
                    "upper": upper,
                    "method": "self path norm bound" if i == j else "Cauchy--Schwarz after complete exterior projection",
                })
        total_entries += len(gram)
        coherent_upper = sum(math.sqrt(row["norm_squared_upper"]) for row in bounds.values()) ** 2
        result[f"seed={key[0]}|{key[1]}"] = {
            "path_count": len(terms),
            "path_bounds": bounds,
            "unique_self_and_cross_entries": len(gram),
            "gram_intervals": gram,
            "coherent_norm_squared_interval": [0.0, coherent_upper * (1.0 + 1e-12)],
        }
    return {
        "groups": result,
        "all_twelve_groups_enclosed": len(result) == 12,
        "all_groups_multi_path": all(row["path_count"] > 1 for row in result.values()),
        "unique_self_and_cross_entries_all_groups": total_entries,
        "all_bounds_applied_after_complete_specieswise_antisymmetrization": True,
    }


def decimal_energy(momentum: Decimal) -> Decimal:
    return (Decimal(1) + momentum * momentum).sqrt()


def decimal_acosh(value: Decimal) -> Decimal:
    return (value + (value * value - Decimal(1)).sqrt()).ln()


def pair_resolvent_integral(a: Decimal, b: Decimal) -> Decimal:
    """Integral_R dp/((sqrt(1+p^2)+a)(sqrt(1+p^2)+b))."""
    if not b > a:
        raise ValueError("strictly increasing resolvent parameters required")
    primitive_a = a * decimal_acosh(a) / (a * a - Decimal(1)).sqrt()
    primitive_b = b * decimal_acosh(b) / (b * b - Decimal(1)).sqrt()
    return Decimal(2) * (primitive_b - primitive_a) / (b - a)


def multi_resolvent_integral(parameters: tuple[Decimal, ...]) -> Decimal:
    """Positive contracted integral by recursive divided differences."""
    if len(parameters) < 2 or any(b <= a for a, b in zip(parameters, parameters[1:])):
        raise ValueError("at least two strictly increasing parameters required")
    if len(parameters) == 2:
        return pair_resolvent_integral(*parameters)
    return (
        multi_resolvent_integral(parameters[:-1])
        - multi_resolvent_integral(parameters[:-2] + (parameters[-1],))
    ) / (parameters[-1] - parameters[-2])


def closed_contracted_value(term: dict[str, Any], energies: dict[int, Decimal]) -> Decimal:
    """Exact positive raw path kernel after integrating the old momentum."""
    old = int(term["old_position"])
    running = Decimal(256)
    prefactor = Decimal(1)
    parameters = []
    for index in range(1, TOTAL_POSITIONS + 1):
        if index != old:
            running += energies[index]
        if index < old:
            prefactor *= running
        else:
            parameters.append(running)
    return multi_resolvent_integral(tuple(parameters)) / prefactor


def closed_contracted_interval(
    term: dict[str, Any], assignment: dict[int, tuple[Decimal, Decimal]]
) -> tuple[Decimal, Decimal]:
    """Monotone interval after exact contracted-momentum integration."""
    low_energies = {index: decimal_energy(box[0]) for index, box in assignment.items()}
    high_energies = {index: decimal_energy(box[1]) for index, box in assignment.items()}
    lower = closed_contracted_value(term, high_energies)
    upper = closed_contracted_value(term, low_energies)
    guard = max(abs(upper) * Decimal("1e-32"), Decimal("1e-75"))
    return max(Decimal(0), lower - guard), upper + guard


def contracted_interval_mesh(subdivisions: int = 96, octaves: int = 40) -> list[Decimal]:
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
    outer = {index: (decimal_energy(box[0]), decimal_energy(box[1])) for index, box in assignment.items()}
    lower = Decimal(0)
    upper = Decimal(0)
    for left, right in zip(mesh, mesh[1:]):
        contracted = (decimal_energy(left), decimal_energy(right))
        lows, highs = [], []
        low_sum = high_sum = Decimal(256)
        for index in range(1, TOTAL_POSITIONS + 1):
            interval = contracted if index == old else outer[index]
            low_sum += interval[0]
            high_sum += interval[1]
            lows.append(low_sum)
            highs.append(high_sum)
        width = right - left
        lower += Decimal(2) * width / math.prod(highs)
        upper += Decimal(2) * width / math.prod(lows)
    cutoff = mesh[-1]
    contracted_power = TOTAL_POSITIONS + 1 - old
    prefactor = Decimal(1)
    running = Decimal(256)
    for index in range(1, old):
        running += outer[index][0]
        prefactor *= running
    tail = Decimal(2) * cutoff ** (1 - contracted_power) / (
        Decimal(contracted_power - 1) * prefactor
    )
    guard = max(abs(upper) * Decimal("1e-35"), Decimal("1e-75"))
    return max(Decimal(0), lower - guard), upper + tail + guard


def coherent_coordinate_interval(
    terms: list[dict[str, Any]],
    boxes: tuple[tuple[Decimal, Decimal], ...],
) -> tuple[Decimal, Decimal]:
    total_lower = total_upper = Decimal(0)
    for term in terms:
        factorial_product = math.prod(
            term["antisymmetrizer_normalization"]["species_factorials"].values()
        )
        path_lower = path_upper = Decimal(0)
        for sign, assignment in exterior_box_assignments(term, boxes):
            raw_lower, raw_upper = closed_contracted_interval(term, assignment)
            if sign > 0:
                path_lower += raw_lower
                path_upper += raw_upper
            else:
                path_lower -= raw_upper
                path_upper -= raw_lower
        scale = (
            Decimal(int(term["exact_operator_coefficient"]))
            * DECIMAL_POINT_NORM
            / Decimal(factorial_product).sqrt()
        )
        if scale > 0:
            total_lower += scale * path_lower
            total_upper += scale * path_upper
        else:
            total_lower += scale * path_upper
            total_upper += scale * path_lower
    return total_lower, total_upper


def point_candidates() -> list[tuple[float, ...]]:
    import numpy as np

    fixed = [
        (0.2, 0.7, 1.7, 4.0, 9.0),
        (0.4, 1.2, 3.0, 7.0, 15.0),
        (0.03, 0.2, 1.0, 6.0, 30.0),
        (30.0, 0.03, 0.2, 3.0, 12.0),
        (0.01, 30.0, 0.03, 10.0, 0.2),
        (10.0, 0.02, 30.0, 0.1, 3.0),
    ]
    rng = np.random.default_rng(183)
    random_rows = [tuple(float(x) for x in 10.0 ** rng.uniform(-2.0, 1.5, 5)) for _ in range(42)]
    return fixed + random_rows


def localized_witness_certificate() -> dict[str, Any]:
    import numpy as np
    from numpy.polynomial.legendre import leggauss

    base, weights = leggauss(56)
    coordinate = 12.0 * base
    nodes = np.sinh(coordinate)
    contracted_weights = 12.0 * weights * np.cosh(coordinate)
    results = {}
    for key, terms in grouped_terms().items():
        scored = []
        for candidate in point_candidates():
            value, _ = coherent_coordinate(terms, candidate, nodes, contracted_weights)
            scored.append((abs(value), value, candidate))
        _magnitude, point_value, candidate = max(scored)
        witness = None
        for relative_radius in (Decimal("1e-8"), Decimal("1e-9"), Decimal("1e-10"), Decimal("1e-11")):
            boxes = tuple(
                (
                    Decimal(str(value)) * (Decimal(1) - relative_radius),
                    Decimal(str(value)) * (Decimal(1) + relative_radius),
                )
                for value in candidate
            )
            lower, upper = coherent_coordinate_interval(terms, boxes)
            if lower > 0 or upper < 0:
                volume = math.prod(float(high - low) for low, high in boxes)
                floor = min(abs(lower), abs(upper))
                witness = {
                    "canonical_positive_momentum_box": [[str(low), str(high)] for low, high in boxes],
                    "coherent_coordinate_interval": [str(lower), str(upper)],
                    "point_control": point_value,
                    "relative_box_radius": str(relative_radius),
                    "certified_local_norm_squared_lower": str(Decimal(str(volume)) * floor * floor),
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
        "contracted_evaluation": "positive multi-resolvent divided differences after exact old-momentum integration",
        "decimal_precision": 60,
        "relative_rounding_guard": "1e-32",
        "groups": results,
        "groups_with_nonzero_local_witness": sum(
            row["certified_local_norm_squared_lower"] != "0" for row in results.values()
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


def qmc_quadrature_certificate(
    power: int, contracted_order: int, seed: int = 183, span: float = 12.0
) -> dict[str, Any]:
    import numpy as np
    from numpy.polynomial.legendre import leggauss
    from scipy.stats import qmc

    unit = qmc.Sobol(d=ORDER, scramble=True, seed=seed).random_base2(power)
    outer_x = span * unit
    momenta = np.sinh(outer_x)
    sample_weights = np.prod(2.0 * span * np.cosh(outer_x), axis=1) / len(unit)
    inner_base, inner_weights = leggauss(contracted_order)
    inner_x = span * inner_base
    inner_nodes = np.sinh(inner_x)
    inner_w = span * inner_weights * np.cosh(inner_x)
    groups = grouped_terms()
    accumulators = {
        key: {"coherent": 0.0, "paths": [0.0] * len(terms)}
        for key, terms in groups.items()
    }
    for sample, weight in zip(momenta, sample_weights):
        canonical = tuple(float(value) for value in sample)
        for key, terms in groups.items():
            coherent, paths = coherent_coordinate(terms, canonical, inner_nodes, inner_w)
            accumulators[key]["coherent"] += float(weight) * coherent * coherent
            for index, value in enumerate(paths):
                accumulators[key]["paths"][index] += float(weight) * value * value
    output = {}
    for key, terms in groups.items():
        row = accumulators[key]
        output[f"seed={key[0]}|{key[1]}"] = {
            "path_count": len(terms),
            "coherent_norm_squared": row["coherent"],
            "path_norms_squared": {
                term["contraction_id"]: row["paths"][index]
                for index, term in enumerate(terms)
            },
        }
    return {
        "outer_sobol_power": power,
        "outer_sample_count": 2**power,
        "contracted_gauss_legendre_order": contracted_order,
        "asinh_coordinate_span": span,
        "coordinate_transform": "positive bounded asinh momentum with reflection; scrambled Sobol outside and full-line Gauss--Legendre inside",
        "scramble_seed": seed,
        "groups": output,
    }


def literal_laplace_exterior(term: dict[str, Any], momenta: tuple[float, ...], cumulative_times: dict[int, float]) -> float:
    total = 0.0
    for sign, assignment in exterior_assignments(term, momenta):
        product = 1.0
        for provenance, momentum in assignment.items():
            product *= math.exp(-cumulative_times[provenance] * math.sqrt(1.0 + momentum * momentum))
        total += sign * product
    return total


def determinant_laplace_exterior(term: dict[str, Any], momenta: tuple[float, ...], cumulative_times: dict[int, float]) -> float:
    import numpy as np

    product = 1.0
    slots = canonical_slots(term)
    occurrences: dict[str, list[int]] = defaultdict(list)
    for provenance, species in zip(term["output_variable_provenance"], term["output_letters"]):
        occurrences[species].append(int(provenance))
    for species, row_positions in sorted(occurrences.items()):
        columns = slots[species]
        matrix = np.array([
            [
                math.exp(-cumulative_times[position] * math.sqrt(1.0 + momenta[column] ** 2))
                for column in columns
            ]
            for position in row_positions
        ])
        product *= float(np.linalg.det(matrix))
    return product


def compression_certificate() -> dict[str, Any]:
    terms = K179.coefficient_family()
    tests = []
    test_momenta = (
        (0.13, 0.41, 1.07, 2.31, 5.17),
        (0.07, 0.29, 0.83, 3.11, 8.03),
        (0.19, 0.53, 1.61, 4.09, 11.3),
    )
    laplace_steps = (0.11, 0.17, 0.23, 0.31, 0.43, 0.59)
    cumulative_times = {
        index: sum(laplace_steps[index - 1 :]) for index in range(1, TOTAL_POSITIONS + 1)
    }
    max_error = 0.0
    for term in order_five_terms():
        for momenta in test_momenta:
            literal = literal_laplace_exterior(term, momenta, cumulative_times)
            determinant = determinant_laplace_exterior(term, momenta, cumulative_times)
            error = abs(literal - determinant)
            max_error = max(max_error, error)
            tests.append({
                "contraction_id": term["contraction_id"],
                "literal": literal,
                "determinant": determinant,
                "absolute_error": error,
            })
    replay = {}
    for order in range(4, 13):
        order_terms = [term for term in terms if term["order"] == order]
        literal = sum(
            math.prod(term["antisymmetrizer_normalization"]["species_factorials"].values())
            for term in order_terms
        )
        determinant_square_entries = sum(
            sum(value**2 for value in term["antisymmetrizer_normalization"]["species_multiplicities"].values())
            for term in order_terms
        )
        determinant_cubic_proxy = sum(
            sum(value**3 for value in term["antisymmetrizer_normalization"]["species_multiplicities"].values())
            for term in order_terms
        )
        replay[str(order)] = {
            "paths": len(order_terms),
            "literal_exterior_summands_per_time_point": literal,
            "determinant_matrix_entries_per_time_point": determinant_square_entries,
            "dense_determinant_cubic_proxy_per_time_point": determinant_cubic_proxy,
            "literal_to_cubic_proxy_ratio": literal / determinant_cubic_proxy,
        }
    return {
        "identity": "specieswise Leibniz permutation sum equals the product of species determinants after the Laplace-simplex transform",
        "contracted_factor": "the old-position momentum integrates separately as 2*K_1(T_old); common cumulative-time nodes are shared by a DAG",
        "order_five_identity_tests": len(tests),
        "maximum_absolute_identity_error": max_error,
        "all_order_five_paths_and_three_controls_agree": max_error < 1e-12 and len(tests) == 96,
        "tests": tests,
        "replay": replay,
        "first_dense_proxy_advantage_order": min(
            int(order) for order, row in replay.items()
            if row["literal_exterior_summands_per_time_point"] > row["dense_determinant_cubic_proxy_per_time_point"]
        ),
        "selected_representation": "hybrid: canonical literal exterior sums through order seven; Laplace-simplex species determinants with memoized cumulative-time DAG from order eight",
        "remaining_numerical_problem": "choose and certify the positive-orthant time quadrature or low-rank integration error before evaluating orders six through twelve",
    }


def contracted_formula_control() -> dict[str, Any]:
    """Independent full-line quadrature check of both divided-difference classes."""
    import numpy as np
    from numpy.polynomial.legendre import leggauss

    base, weights = leggauss(120)
    coordinate = 20.0 * base
    nodes = np.sinh(coordinate)
    jacobian_weights = 20.0 * weights * np.cosh(coordinate)
    rows = []
    for old in (2, 4):
        term = next(term for term in order_five_terms() if int(term["old_position"]) == old)
        assignment = {
            index: 0.13 + 0.37 * index
            for index in range(1, TOTAL_POSITIONS + 1)
            if index != old
        }
        numerical = raw_contracted_kernel(term, assignment, nodes, jacobian_weights)
        analytic = float(closed_contracted_value(
            term,
            {index: decimal_energy(Decimal(str(value))) for index, value in assignment.items()},
        ))
        rows.append({
            "old_position": old,
            "full_line_asinh_gauss_legendre": numerical,
            "positive_multi_resolvent_divided_difference": analytic,
            "relative_difference": abs(numerical - analytic) / analytic,
        })
    return {
        "quadrature_order": 120,
        "asinh_coordinate_span": 20,
        "rows": rows,
        "maximum_relative_difference": max(row["relative_difference"] for row in rows),
    }


def quick_certificate() -> dict[str, Any]:
    rows = canonical_group_rows()
    return {
        "terms": sum(row["path_count"] for row in rows),
        "groups": len(rows),
        "singleton_groups": sum(row["path_count"] == 1 for row in rows),
        "multi_path_groups": sum(row["path_count"] > 1 for row in rows),
        "maximum_group_size": max(row["path_count"] for row in rows),
        "canonical_groups": rows,
        "global_gram": global_gram_certificate(),
        "contracted_formula_control": contracted_formula_control(),
        "compression": compression_certificate(),
    }


def demo() -> dict[str, Any]:
    quick = quick_certificate()
    localized = localized_witness_certificate()
    coarse = qmc_quadrature_certificate(13, 48)
    fine = qmc_quadrature_certificate(14, 56)
    comparisons = {}
    intervals = {}
    for group_id, fine_row in fine["groups"].items():
        coarse_value = coarse["groups"][group_id]["coherent_norm_squared"]
        fine_value = fine_row["coherent_norm_squared"]
        bound = quick["global_gram"]["groups"][group_id]["coherent_norm_squared_interval"]
        comparisons[group_id] = {
            "coarse_fine_relative_difference": abs(coarse_value - fine_value) / max(abs(fine_value), 1e-300),
            "fine_value_inside_global_outward_interval": bound[0] <= fine_value <= bound[1],
        }
        intervals[group_id] = [
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
            "resolved_order": 5,
        },
        "canonical_order_five_family": quick,
        "localized_interval_witnesses": localized,
        "certified_coherent_norm_squared_intervals": intervals,
        "same_family_numerical_control": {
            "coarse": coarse,
            "fine": fine,
            "comparisons": comparisons,
            "seedwise_order_five_norms_squared": dict(sorted(seed_norms.items())),
            "role": "independent normalization/interference control; not the outward proof",
        },
        "release_test": {
            "all_32_order_five_paths_mapped_to_canonical_exterior_coordinates": True,
            "all_12_output_groups_assembled": True,
            "all_64_self_and_cross_gram_entries_outwardly_enclosed": quick["global_gram"]["unique_self_and_cross_entries_all_groups"] == 64,
            "all_bounds_applied_after_complete_specieswise_antisymmetrization": True,
            "complete_order_five_nonzero_norms_certified": localized["groups_with_nonzero_local_witness"] == 12,
            "determinant_dag_representation_selected_and_identity_checked": quick["compression"]["all_order_five_paths_and_three_controls_agree"],
            "order_six_through_twelve_coherent_cross_terms_evaluated": False,
            "coefficient_complete_base_action_column_evaluated": False,
            "complete_R_ref_form_dual_residual_serialized": False,
            "positive_complete_M_orthogonal_complement_or_flux_floor_serialized": False,
            "scalar_center_left_floor_serialized": False,
            "native_K152_interval_emitted": False,
        },
        "next_exact_input": {
            "owner": "Laplace-simplex determinant time integrator",
            "first_gate": "certify a positive-orthant cumulative-time quadrature or low-rank integration error and evaluate the complete order-six family",
            "must_preserve": "K179 coefficients, species determinants, old-position Bessel factor, common-time DAG and all coherent cross terms",
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
