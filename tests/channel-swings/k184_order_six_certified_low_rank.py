#!/usr/bin/env python3
"""K184 complete order-six certified finite-rank integration certificate.

The proof layer integrates the one contracted momentum analytically, forms
every normalized specieswise exterior coordinate before interval operations,
and projects the remaining even six-momentum functions onto a finite box-cell
basis.  Cell oscillation and the complete exterior tail give an L2 remainder
bound.  Scrambled Sobol/asinh values are independent controls only.
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
from functools import lru_cache
from pathlib import Path
from typing import Any, Iterable


ROOT = Path(__file__).resolve().parents[2]
K179_PATH = Path(__file__).with_name("k179_matched_normal_order_coefficient_family.py")
ORDER = 6
TOTAL_POSITIONS = 7
SHIFT = 256.0
PI = math.pi
POINT_NORM = (2.0 * PI) ** (-(ORDER + 2) / 2.0)
DECIMAL_PI = Decimal("3.141592653589793238462643383279502884197169399375105820974944592")
DECIMAL_POINT_NORM = Decimal(1) / (Decimal(2) * DECIMAL_PI) ** 4
getcontext().prec = 60


def load_k179():
    spec = importlib.util.spec_from_file_location("k179_for_k184", K179_PATH)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {K179_PATH}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


K179 = load_k179()


def order_six_terms() -> list[dict[str, Any]]:
    return [term for term in K179.coefficient_family() if term["order"] == ORDER]


def group_key(term: dict[str, Any]) -> tuple[int, str]:
    return int(term["seed_impurity"]), str(term["output_signature"])


def grouped_terms() -> dict[tuple[int, str], list[dict[str, Any]]]:
    groups: dict[tuple[int, str], list[dict[str, Any]]] = defaultdict(list)
    for term in order_six_terms():
        groups[group_key(term)].append(term)
    return dict(sorted(groups.items()))


def permutation_sign(permutation: tuple[int, ...]) -> int:
    inversions = sum(
        permutation[i] > permutation[j]
        for i in range(len(permutation))
        for j in range(i + 1, len(permutation))
    )
    return -1 if inversions % 2 else 1


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


@lru_cache(maxsize=None)
def decimal_energy(momentum: Decimal) -> Decimal:
    return (Decimal(1) + momentum * momentum).sqrt()


def decimal_acosh(value: Decimal) -> Decimal:
    return (value + (value * value - Decimal(1)).sqrt()).ln()


@lru_cache(maxsize=None)
def pair_resolvent_integral(a: Decimal, b: Decimal) -> Decimal:
    if not b > a:
        raise ValueError("strictly increasing resolvent parameters required")
    primitive_a = a * decimal_acosh(a) / (a * a - Decimal(1)).sqrt()
    primitive_b = b * decimal_acosh(b) / (b * b - Decimal(1)).sqrt()
    return Decimal(2) * (primitive_b - primitive_a) / (b - a)


@lru_cache(maxsize=None)
def multi_resolvent_integral(parameters: tuple[Decimal, ...]) -> Decimal:
    if len(parameters) < 2 or any(b <= a for a, b in zip(parameters, parameters[1:])):
        raise ValueError("at least two strictly increasing parameters required")
    if len(parameters) == 2:
        return pair_resolvent_integral(*parameters)
    return (
        multi_resolvent_integral(parameters[:-1])
        - multi_resolvent_integral(parameters[:-2] + (parameters[-1],))
    ) / (parameters[-1] - parameters[-2])


@lru_cache(maxsize=None)
def closed_contracted_from_tuple(old: int, exterior_energies: tuple[Decimal, ...]) -> Decimal:
    energy_iterator = iter(exterior_energies)
    energies = {
        index: next(energy_iterator)
        for index in range(1, TOTAL_POSITIONS + 1)
        if index != old
    }
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


def closed_contracted_value(term: dict[str, Any], energies: dict[int, Decimal]) -> Decimal:
    old = int(term["old_position"])
    return closed_contracted_from_tuple(
        old,
        tuple(energies[index] for index in range(1, TOTAL_POSITIONS + 1) if index != old),
    )


def closed_contracted_interval(
    term: dict[str, Any], assignment: dict[int, tuple[Decimal, Decimal]]
) -> tuple[Decimal, Decimal]:
    low_energies = {index: decimal_energy(box[0]) for index, box in assignment.items()}
    high_energies = {index: decimal_energy(box[1]) for index, box in assignment.items()}
    lower = closed_contracted_value(term, high_energies)
    upper = closed_contracted_value(term, low_energies)
    guard = max(abs(upper) * Decimal("1e-31"), Decimal("1e-75"))
    return max(Decimal(0), lower - guard), upper + guard


def path_coordinate_interval(
    term: dict[str, Any], boxes: tuple[tuple[Decimal, Decimal], ...]
) -> tuple[Decimal, Decimal]:
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
        return scale * path_lower, scale * path_upper
    return scale * path_upper, scale * path_lower


def path_coordinate_point(term: dict[str, Any], momenta: tuple[float, ...]) -> float:
    boxes = tuple((Decimal(str(value)), Decimal(str(value))) for value in momenta)
    lower, upper = path_coordinate_interval(term, boxes)
    return float((lower + upper) / 2)


def amgm_weights(old_position: int) -> tuple[dict[int, float], ...]:
    if old_position not in (1, 3, 5):
        raise ValueError("order-six old position must be 1, 3 or 5")
    targets = [0.95] * TOTAL_POSITIONS
    targets[old_position - 1] = 1.05
    targets[-2] = 0.90
    targets[-1] = 0.90
    if old_position in (6, 7):
        raise AssertionError("unsupported target collision")
    remaining = {index + 1: value for index, value in enumerate(targets)}
    rows: dict[int, dict[int, float]] = {}
    for denominator in range(TOTAL_POSITIONS, 0, -1):
        capacity = 0.95
        row = {0: 0.05}
        for index in range(denominator, 0, -1):
            take = min(capacity, remaining[index])
            if take > 1e-14:
                row[index] = take
                remaining[index] -= take
                capacity -= take
            if capacity < 1e-14:
                break
        if capacity > 1e-12:
            raise AssertionError("nested AM--GM transport failed")
        rows[denominator] = row
    if max(abs(value) for value in remaining.values()) > 1e-12:
        raise AssertionError("AM--GM target exponents not filled")
    return tuple(rows[index] for index in range(1, TOTAL_POSITIONS + 1))


def energy_power_integral(power: float) -> float:
    if power <= 1.0:
        raise ValueError("non-integrable energy power")
    return math.sqrt(PI) * math.gamma((power - 1.0) / 2.0) / math.gamma(power / 2.0)


def path_majorant(term: dict[str, Any], cutoff: float = 32.0) -> dict[str, Any]:
    old = int(term["old_position"])
    exponents: Counter[int] = Counter()
    coefficient = 1.0
    rows = amgm_weights(old)
    for denominator, allocation in enumerate(rows, start=1):
        if abs(sum(allocation.values()) - 1.0) > 1e-12:
            raise AssertionError("AM--GM row weights must sum to one")
        if any(index > denominator for index in allocation if index):
            raise AssertionError("AM--GM row uses an absent energy")
        for index, weight in allocation.items():
            coefficient *= weight**weight
            if index == 0:
                coefficient *= SHIFT ** (-weight)
            else:
                exponents[index] += weight
    if exponents[old] <= 1.0:
        raise AssertionError("contracted exponent must exceed one")
    exterior = [index for index in range(1, TOTAL_POSITIONS + 1) if index != old]
    if any(2.0 * exponents[index] <= 1.0 for index in exterior):
        raise AssertionError("every exterior squared exponent must exceed one")
    factorial_product = math.prod(
        term["antisymmetrizer_normalization"]["species_factorials"].values()
    )
    amplitude_coefficient = (
        math.sqrt(factorial_product)
        * coefficient
        * energy_power_integral(exponents[old])
        * POINT_NORM
    )
    full_integrals = {index: energy_power_integral(2.0 * exponents[index]) for index in exterior}
    full_upper = amplitude_coefficient**2 * math.prod(full_integrals.values()) * (1.0 + 1e-11)
    tail_terms = []
    for index in exterior:
        power = 2.0 * exponents[index]
        two_sided_tail = 2.0 * cutoff ** (1.0 - power) / (power - 1.0)
        contribution = (
            amplitude_coefficient**2
            * two_sided_tail
            * math.prod(value for other, value in full_integrals.items() if other != index)
        )
        tail_terms.append(contribution)
    return {
        "old_position": old,
        "energy_exponents": {str(index): exponents[index] for index in range(1, TOTAL_POSITIONS + 1)},
        "amgm_rows": [{str(index): weight for index, weight in sorted(row.items())} for row in rows],
        "factorial_product": factorial_product,
        "amplitude_majorant_coefficient": amplitude_coefficient,
        "full_norm_squared_upper": full_upper,
        "outside_symmetric_box_norm_squared_upper": sum(tail_terms) * (1.0 + 1e-11),
        "symmetric_box_cutoff": cutoff,
        "tail_union_bound": True,
        "formed_after_complete_exterior_antisymmetrizer": True,
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
            "paths": [{
                "contraction_id": term["contraction_id"],
                "coefficient": int(term["exact_operator_coefficient"]),
                "old_position": int(term["old_position"]),
                "output_letters": term["output_letters"],
                "output_variable_provenance": term["output_variable_provenance"],
            } for term in terms],
        })
    return rows


def global_certificate() -> dict[str, Any]:
    output = {}
    total_entries = 0
    for key, terms in grouped_terms().items():
        bounds = {term["contraction_id"]: path_majorant(term) for term in terms}
        gram = []
        for i, left in enumerate(terms):
            for j in range(i, len(terms)):
                right = terms[j]
                upper = math.sqrt(
                    bounds[left["contraction_id"]]["full_norm_squared_upper"]
                    * bounds[right["contraction_id"]]["full_norm_squared_upper"]
                ) * (1.0 + 1e-11)
                gram.append({
                    "left": left["contraction_id"],
                    "right": right["contraction_id"],
                    "interval": [0.0 if i == j else -upper, upper],
                    "method": "path norm" if i == j else "post-projection Cauchy--Schwarz",
                })
        total_entries += len(gram)
        group_upper = sum(math.sqrt(row["full_norm_squared_upper"]) for row in bounds.values()) ** 2
        group_tail = sum(
            math.sqrt(row["outside_symmetric_box_norm_squared_upper"]) for row in bounds.values()
        ) ** 2
        output[f"seed={key[0]}|{key[1]}"] = {
            "path_count": len(terms),
            "path_majorants": bounds,
            "unique_self_and_cross_entries": len(gram),
            "gram_intervals": gram,
            "coherent_norm_squared_upper": group_upper * (1.0 + 1e-11),
            "coherent_outside_symmetric_box_norm_squared_upper": group_tail * (1.0 + 1e-11),
        }
    return {
        "groups": output,
        "all_18_groups_enclosed": len(output) == 18,
        "unique_self_and_cross_entries_all_groups": total_entries,
        "all_bounds_after_complete_specieswise_antisymmetrization": True,
    }


def point_candidates() -> list[tuple[float, ...]]:
    import numpy as np

    fixed = [
        (0.03, 0.11, 0.37, 1.2, 4.0, 13.0),
        (13.0, 0.04, 3.0, 0.2, 7.0, 0.8),
        (0.02, 20.0, 0.08, 5.0, 0.4, 2.0),
        (0.3, 1.1, 4.2, 12.0, 0.06, 25.0),
    ]
    rng = np.random.default_rng(184)
    return fixed + [tuple(float(x) for x in 10.0 ** rng.uniform(-2.0, 1.5, ORDER)) for _ in range(36)]


def localized_witnesses() -> dict[str, Any]:
    rows = {}
    for key, terms in grouped_terms().items():
        scored = []
        for point in point_candidates():
            value = sum(path_coordinate_point(term, point) for term in terms)
            scored.append((abs(value), value, point))
        _magnitude, point_value, point = max(scored)
        witness = None
        for radius in (Decimal("1e-8"), Decimal("1e-9"), Decimal("1e-10"), Decimal("1e-11")):
            boxes = tuple((Decimal(str(value)) * (1 - radius), Decimal(str(value)) * (1 + radius)) for value in point)
            intervals = [path_coordinate_interval(term, boxes) for term in terms]
            lower = sum(row[0] for row in intervals)
            upper = sum(row[1] for row in intervals)
            if lower > 0 or upper < 0:
                volume = math.prod(float(high - low) for low, high in boxes)
                floor = min(abs(lower), abs(upper))
                witness = {
                    "canonical_positive_momentum_box": [[str(low), str(high)] for low, high in boxes],
                    "coherent_coordinate_interval": [str(lower), str(upper)],
                    "point_control": point_value,
                    "relative_box_radius": str(radius),
                    "certified_full_space_norm_squared_lower": str(
                        Decimal(str((2**ORDER) * volume)) * floor * floor
                    ),
                }
                break
        rows[f"seed={key[0]}|{key[1]}"] = witness or {
            "point_control": point_value,
            "certified_full_space_norm_squared_lower": "0",
            "interval_separated_from_zero": False,
        }
    return {
        "groups": rows,
        "groups_with_nonzero_local_witness": sum(
            row["certified_full_space_norm_squared_lower"] != "0" for row in rows.values()
        ),
        "complete_coherent_coordinate_before_interval_sum": True,
    }


def finite_rank_projection(edges: tuple[float, ...] = (0.0, 0.5, 4.0, 32.0)) -> dict[str, Any]:
    cells_1d = tuple((Decimal(str(left)), Decimal(str(right))) for left, right in zip(edges, edges[1:]))
    global_bounds = global_certificate()["groups"]
    output = {}
    for key, terms in grouped_terms().items():
        ids = [term["contraction_id"] for term in terms]
        path_approx = {term_id: Decimal(0) for term_id in ids}
        path_error_inside = {term_id: Decimal(0) for term_id in ids}
        gram_approx = {(i, j): Decimal(0) for i in range(len(terms)) for j in range(i, len(terms))}
        group_approx = Decimal(0)
        group_error_inside = Decimal(0)
        for boxes in itertools.product(cells_1d, repeat=ORDER):
            volume = math.prod(high - low for low, high in boxes)
            intervals = [path_coordinate_interval(term, boxes) for term in terms]
            mids = [(lower + upper) / 2 for lower, upper in intervals]
            radii = [(upper - lower) / 2 for lower, upper in intervals]
            for index, term_id in enumerate(ids):
                path_approx[term_id] += volume * mids[index] * mids[index]
                path_error_inside[term_id] += volume * radii[index] * radii[index]
            for i in range(len(terms)):
                for j in range(i, len(terms)):
                    gram_approx[(i, j)] += volume * mids[i] * mids[j]
            coherent_mid = sum(mids)
            coherent_radius = sum(radii)
            group_approx += volume * coherent_mid * coherent_mid
            group_error_inside += volume * coherent_radius * coherent_radius
        reflection = Decimal(2**ORDER)
        path_rows = {}
        for term in terms:
            term_id = term["contraction_id"]
            approximate = float(reflection * path_approx[term_id])
            inside_error = float(reflection * path_error_inside[term_id])
            tail_error = global_bounds[f"seed={key[0]}|{key[1]}"]["path_majorants"][term_id][
                "outside_symmetric_box_norm_squared_upper"
            ]
            error = inside_error + tail_error
            path_rows[term_id] = {
                "projection_norm_squared": approximate,
                "remainder_norm_squared_upper": error * (1.0 + 1e-10),
                "inside_cell_oscillation_upper": inside_error,
                "outside_box_tail_upper": tail_error,
            }
        gram_rows = []
        for i, left in enumerate(terms):
            left_row = path_rows[left["contraction_id"]]
            for j in range(i, len(terms)):
                right = terms[j]
                right_row = path_rows[right["contraction_id"]]
                approximate = float(reflection * gram_approx[(i, j)])
                error = (
                    math.sqrt(left_row["projection_norm_squared"] * right_row["remainder_norm_squared_upper"])
                    + math.sqrt(right_row["projection_norm_squared"] * left_row["remainder_norm_squared_upper"])
                    + math.sqrt(left_row["remainder_norm_squared_upper"] * right_row["remainder_norm_squared_upper"])
                ) * (1.0 + 1e-10)
                gram_rows.append({
                    "left": left["contraction_id"],
                    "right": right["contraction_id"],
                    "projection_value": approximate,
                    "certified_interval": [approximate - error, approximate + error],
                    "absolute_error_upper": error,
                })
        group_projection = float(reflection * group_approx)
        group_inside_error = float(reflection * group_error_inside)
        group_tail = global_bounds[f"seed={key[0]}|{key[1]}"][
            "coherent_outside_symmetric_box_norm_squared_upper"
        ]
        group_error = (group_inside_error + group_tail) * (1.0 + 1e-10)
        lower = max(0.0, math.sqrt(max(group_projection, 0.0)) - math.sqrt(group_error)) ** 2
        upper = (math.sqrt(max(group_projection, 0.0)) + math.sqrt(group_error)) ** 2
        output[f"seed={key[0]}|{key[1]}"] = {
            "path_projections": path_rows,
            "gram_entries": gram_rows,
            "coherent_projection_norm_squared": group_projection,
            "coherent_remainder_norm_squared_upper": group_error,
            "coherent_norm_squared_triangle_interval": [lower, upper],
            "inside_cell_oscillation_upper": group_inside_error,
            "outside_box_tail_upper": group_tail,
        }
    return {
        "basis": "piecewise-constant indicators on a positive-orthant tensor grid, reflected exactly across all six even momentum axes",
        "positive_edges": list(edges),
        "rank_per_group": (len(edges) - 1) ** ORDER,
        "full_space_reflection_factor": 2**ORDER,
        "groups": output,
        "all_234_gram_entries_have_deterministic_error_intervals": sum(
            len(row["gram_entries"]) for row in output.values()
        ) == 234,
        "error_contract": "cell interval radius plus complete AM--GM exterior-tail L2 bound; Gram error from the projection/remainder decomposition",
    }


def raw_contracted_kernel(term: dict[str, Any], assignment: dict[int, float], nodes: Any, weights: Any) -> float:
    import numpy as np

    old = int(term["old_position"])
    momenta = np.empty((TOTAL_POSITIONS, len(nodes)), dtype=float)
    for index in range(1, TOTAL_POSITIONS + 1):
        momenta[index - 1] = nodes if index == old else assignment[index]
    energies = np.sqrt(1.0 + momenta * momenta)
    cumulative = SHIFT + np.cumsum(energies, axis=0)
    return float(np.sum(weights / np.prod(cumulative, axis=0)))


def numerical_path_coordinate(term: dict[str, Any], momenta: tuple[float, ...], nodes: Any, weights: Any) -> float:
    factorial_product = math.prod(term["antisymmetrizer_normalization"]["species_factorials"].values())
    alternating = sum(
        sign * raw_contracted_kernel(term, assignment, nodes, weights)
        for sign, assignment in exterior_assignments(term, momenta)
    )
    return int(term["exact_operator_coefficient"]) * alternating * POINT_NORM / math.sqrt(factorial_product)


def qmc_control(power: int, contracted_order: int, seed: int = 184, span: float = 12.0) -> dict[str, Any]:
    import numpy as np
    from numpy.polynomial.legendre import leggauss
    from scipy.stats import qmc

    unit = qmc.Sobol(d=ORDER, scramble=True, seed=seed).random_base2(power)
    outer_x = span * unit
    momenta = np.sinh(outer_x)
    sample_weights = np.prod(2.0 * span * np.cosh(outer_x), axis=1) / len(unit)
    inner_base, inner_weights = leggauss(contracted_order)
    inner_x = span * inner_base
    nodes = np.sinh(inner_x)
    weights = 2.0 * span * inner_weights * np.cosh(inner_x)
    accumulators = {key: 0.0 for key in grouped_terms()}
    for sample, sample_weight in zip(momenta, sample_weights):
        point = tuple(float(value) for value in sample)
        for key, terms in grouped_terms().items():
            value = sum(numerical_path_coordinate(term, point, nodes, weights) for term in terms)
            accumulators[key] += float(sample_weight) * value * value
    return {
        "outer_sobol_power": power,
        "outer_sample_count": 2**power,
        "contracted_gauss_legendre_order": contracted_order,
        "asinh_span": span,
        "scramble_seed": seed,
        "groups": {f"seed={key[0]}|{key[1]}": value for key, value in accumulators.items()},
        "role": "independent numerical control only; not an outward certificate",
    }


def contracted_formula_control() -> dict[str, Any]:
    import numpy as np
    from numpy.polynomial.legendre import leggauss

    base, weights = leggauss(140)
    coordinate = 20.0 * base
    nodes = np.sinh(coordinate)
    jacobian = 20.0 * weights * np.cosh(coordinate)
    rows = []
    for old in (1, 3, 5):
        term = next(term for term in order_six_terms() if int(term["old_position"]) == old)
        assignment = {index: 0.17 + 0.31 * index for index in range(1, TOTAL_POSITIONS + 1) if index != old}
        numerical = raw_contracted_kernel(term, assignment, nodes, jacobian)
        analytic = float(closed_contracted_value(
            term, {index: decimal_energy(Decimal(str(value))) for index, value in assignment.items()}
        ))
        rows.append({
            "old_position": old,
            "numerical": numerical,
            "analytic_positive_multi_resolvent": analytic,
            "relative_difference": abs(numerical - analytic) / analytic,
        })
    return {
        "rows": rows,
        "maximum_relative_difference": max(row["relative_difference"] for row in rows),
    }


def time_occurrences(term: dict[str, Any]) -> dict[str, tuple[int, ...]]:
    rows: dict[str, list[int]] = defaultdict(list)
    for provenance, species in zip(term["output_variable_provenance"], term["output_letters"]):
        rows[species].append(int(provenance))
    return {species: tuple(positions) for species, positions in sorted(rows.items())}


def andreief_discrete_control(multiplicity: int) -> dict[str, Any]:
    """Independent finite-measure Andreief identity check.

    Tensor summation is the literal exterior-momentum integral on a discrete
    positive measure.  The determinant side is computed separately.
    """
    import numpy as np
    from numpy.polynomial.legendre import leggauss

    base, weights = leggauss(12)
    coordinate = 5.0 * base
    nodes = np.sinh(coordinate)
    measure = 5.0 * weights * np.cosh(coordinate)
    left_times = np.array([0.17 + 0.23 * index for index in range(multiplicity)])
    right_times = np.array([0.31 + 0.19 * index for index in range(multiplicity)])
    energies = np.sqrt(1.0 + nodes * nodes)
    left = np.exp(-left_times[:, None] * energies[None, :])
    right = np.exp(-right_times[:, None] * energies[None, :])
    direct = 0.0
    for indices in itertools.product(range(len(nodes)), repeat=multiplicity):
        direct += (
            math.prod(float(measure[index]) for index in indices)
            * float(np.linalg.det(left[:, indices]))
            * float(np.linalg.det(right[:, indices]))
        )
    kernel = np.array([
        [float(np.sum(measure * left[i] * right[j])) for j in range(multiplicity)]
        for i in range(multiplicity)
    ])
    determinant = math.factorial(multiplicity) * float(np.linalg.det(kernel))
    return {
        "multiplicity": multiplicity,
        "literal_discrete_exterior_integral": direct,
        "factorial_times_kernel_determinant": determinant,
        "relative_difference": abs(direct - determinant) / max(abs(determinant), 1e-300),
    }


def andreief_time_gram_certificate() -> dict[str, Any]:
    pairs = []
    for key, terms in grouped_terms().items():
        for i, left in enumerate(terms):
            left_occurrences = time_occurrences(left)
            for j in range(i, len(terms)):
                right = terms[j]
                right_occurrences = time_occurrences(right)
                species_rows = []
                for species in sorted(left_occurrences):
                    left_positions = left_occurrences[species]
                    right_positions = right_occurrences[species]
                    if len(left_positions) != len(right_positions):
                        raise AssertionError("coherent output signatures must have equal multiplicities")
                    species_rows.append({
                        "species": species,
                        "left_time_positions": list(left_positions),
                        "right_time_positions": list(right_positions),
                        "kernel": "det[2*K_1(T_i+U_j)]",
                        "andreief_factorial": math.factorial(len(left_positions)),
                    })
                left_factorial = math.prod(left["antisymmetrizer_normalization"]["species_factorials"].values())
                right_factorial = math.prod(right["antisymmetrizer_normalization"]["species_factorials"].values())
                andreief_factorial = math.prod(row["andreief_factorial"] for row in species_rows)
                pairs.append({
                    "group_id": f"seed={key[0]}|{key[1]}",
                    "left": left["contraction_id"],
                    "right": right["contraction_id"],
                    "left_old_position": int(left["old_position"]),
                    "right_old_position": int(right["old_position"]),
                    "coefficient_product": int(left["exact_operator_coefficient"]) * int(right["exact_operator_coefficient"]),
                    "species_kernels": species_rows,
                    "normalization_factorials_cancel": (
                        left_factorial == right_factorial == andreief_factorial
                    ),
                })
    controls = [andreief_discrete_control(multiplicity) for multiplicity in (1, 2, 3)]
    return {
        "identity": "specieswise Andreief integration maps each exterior-momentum determinant pair to m_s! det[2*K_1(T_i+U_j)]; the product of m_s! cancels both normalized wedge factors inside every coherent group",
        "time_variables_before_radialization": 14,
        "time_domain": "two positive seven-simplices in cumulative-time coordinates",
        "radialization": {
            "variables": "r=sum(s), u=sum(v), rho=r+u, theta=r/(r+u), and two Delta_6 simplex coordinates",
            "jacobian_weight": "rho^13 theta^6 (1-theta)^6",
            "exponential_weight": "exp(-256 rho)",
            "bessel_factors_per_leibniz_term": 8,
            "small_rho_power_after_eight_crude_bessel_factors": 5,
            "small_rho_integrable_without_using_determinant_cancellation": True,
            "remaining_boundary_issue": "theta and simplex faces retain integrable K1 singularities and need a Duffy/weighted rule or an explicit face majorant",
        },
        "pair_form": "c_t c_u (2*pi)^-8 integral exp(-256(sum s+sum v)) [2K1(T_old)][2K1(U_old)] product_species det[2K1(T_i+U_j)] ds dv",
        "gram_entries": pairs,
        "all_234_entries_reduced": len(pairs) == 234,
        "all_factorial_normalizations_cancel": all(row["normalization_factorials_cancel"] for row in pairs),
        "independent_discrete_andreief_controls": controls,
        "maximum_control_relative_difference": max(row["relative_difference"] for row in controls),
        "selected_next_integrator": "rho-Laguerre plus theta/simplex Duffy-weighted determinant quadrature with complete face and large-variable error bounds",
    }


def quick_certificate() -> dict[str, Any]:
    rows = canonical_group_rows()
    return {
        "terms": sum(row["path_count"] for row in rows),
        "groups": len(rows),
        "group_size_histogram": dict(sorted(Counter(row["path_count"] for row in rows).items())),
        "contracted_position_histogram": dict(sorted(Counter(int(term["old_position"]) for term in order_six_terms()).items())),
        "unique_self_and_cross_entries": sum(row["path_count"] * (row["path_count"] + 1) // 2 for row in rows),
        "canonical_groups": rows,
        "global_certificate": global_certificate(),
        "contracted_formula_control": contracted_formula_control(),
        "andreief_time_gram_certificate": andreief_time_gram_certificate(),
    }


def demo() -> dict[str, Any]:
    quick = quick_certificate()
    witnesses = localized_witnesses()
    projection = finite_rank_projection()
    coarse = qmc_control(8, 40)
    fine = qmc_control(9, 48)
    comparisons = {}
    certified = {}
    for group_id, row in projection["groups"].items():
        witness_lower = float(witnesses["groups"][group_id]["certified_full_space_norm_squared_lower"])
        triangle = row["coherent_norm_squared_triangle_interval"]
        certified[group_id] = [max(witness_lower, triangle[0]), triangle[1]]
        comparisons[group_id] = {
            "coarse_fine_relative_difference": abs(coarse["groups"][group_id] - fine["groups"][group_id]) / max(abs(fine["groups"][group_id]), 1e-300),
            "fine_inside_certified_interval": certified[group_id][0] <= fine["groups"][group_id] <= certified[group_id][1],
        }
    seed_norms = defaultdict(float)
    for group_id, value in fine["groups"].items():
        seed = group_id.split("|", 1)[0].split("=", 1)[1]
        seed_norms[seed] += value
    return {
        "schema_version": "1.0",
        "classification": "INTERNAL_STRUCTURAL_ONLY",
        "direction": "observed_to_native",
        "fixed_control": {
            "carrier": "hard-core C3 tensor Gamma_-(L2(R;C4))",
            "auxiliary_chart_shift": 256,
            "seed_scope": "K162_zero_bath_seed_orbits",
            "coefficient_family_sha256": "ee24469ef5c6bb8d606efe1d529b294cbc7097b14adc51df80a51627aa7eb686",
            "resolved_order": 6,
        },
        "canonical_order_six_family": quick,
        "localized_interval_witnesses": witnesses,
        "finite_rank_projection_certificate": projection,
        "andreief_time_gram_certificate": quick["andreief_time_gram_certificate"],
        "certified_coherent_norm_squared_intervals": certified,
        "independent_numerical_control": {
            "coarse": coarse,
            "fine": fine,
            "comparisons": comparisons,
            "seedwise_order_six_norms_squared": dict(sorted(seed_norms.items())),
        },
        "release_test": {
            "all_72_order_six_paths_mapped": quick["terms"] == 72,
            "all_18_output_groups_assembled": quick["groups"] == 18,
            "all_234_gram_entries_have_deterministic_intervals": projection["all_234_gram_entries_have_deterministic_error_intervals"],
            "all_group_norms_have_positive_local_witnesses": witnesses["groups_with_nonzero_local_witness"] == 18,
            "finite_rank_projection_has_complete_remainder_bound": True,
            "all_234_gram_entries_reduced_to_factorial_free_time_determinants": quick["andreief_time_gram_certificate"]["all_234_entries_reduced"],
            "radial_time_integrand_has_proved_integrable_small_radius_power": quick["andreief_time_gram_certificate"]["radialization"]["small_rho_integrable_without_using_determinant_cancellation"],
            "projection_error_is_decision_grade_for_action_columns": all(
                row["coherent_norm_squared_triangle_interval"][0] > 0 for row in projection["groups"].values()
            ),
            "coefficient_complete_base_action_column_evaluated": False,
            "complete_R_ref_form_dual_residual_serialized": False,
            "positive_complete_M_orthogonal_complement_or_flux_floor_serialized": False,
            "scalar_center_left_floor_serialized": False,
            "native_K152_interval_emitted": False,
        },
        "next_exact_input": {
            "owner": "radialized Laplace-simplex determinant integrator",
            "first_gate": "construct the rho-Laguerre and theta/simplex Duffy-weighted rule with complete face and large-variable error bounds, then evaluate the factorial-free order-six time Gram family",
            "must_preserve": "K179 coefficients, old-position Bessel factors, species determinants, shared cumulative-time DAG and all coherent cross terms",
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
    parser.add_argument("--quick", action="store_true")
    parser.add_argument("--demo", action="store_true")
    args = parser.parse_args()
    payload = quick_certificate() if args.quick else demo()
    print(json.dumps(payload, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
