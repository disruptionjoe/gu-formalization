#!/usr/bin/env python3
"""K185 exact Duffy-face and radial-tail certificate for K184 time Grams.

The proof object expands determinants only to enumerate the finite positive
majorant.  Every numerical target remains grouped by its original determinant
Gram entry.  A fractional minimax allocation assigns each of the eight
reciprocal cumulative-time factors to its supported primitive increments.
Exact rational replay gives fourteen loads below one.  Their complements are
the Dirichlet/Duffy exponents, while their sum is six, the radial Laguerre
shape.  A separate rational ceiling supplies proof-safe face and radial-tail
bounds; floating gamma values are sharpened controls only.
"""

from __future__ import annotations

import argparse
import hashlib
import importlib.util
import itertools
import json
import math
from fractions import Fraction
from pathlib import Path
from typing import Any, Iterable

from scipy.optimize import linprog
from scipy.special import gammaln


ROOT = Path(__file__).resolve().parents[2]
K184_SOLVER = Path(__file__).with_name("k184_order_six_certified_low_rank.py")
K184_MANIFEST = ROOT / "lab/process/k184-order-six-certified-low-rank-wave.json"
OUTPUT = ROOT / "lab/process/k185-order-six-duffy-face-tail-wave.json"
VARIABLES = tuple([f"s{index}" for index in range(1, 8)] + [f"v{index}" for index in range(1, 8)])
SHIFT = 256
FACTOR_COUNT = 8
FACE_DELTA_POWER = 180
RADIAL_CUTOFF = Fraction(1, 4)


def load_k184():
    spec = importlib.util.spec_from_file_location("k184_for_k185", K184_SOLVER)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {K184_SOLVER}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


K184 = load_k184()


def parity(permutation: tuple[int, ...]) -> int:
    inversions = sum(
        permutation[i] > permutation[j]
        for i in range(len(permutation))
        for j in range(i + 1, len(permutation))
    )
    return -1 if inversions % 2 else 1


def support_t(position: int) -> tuple[int, ...]:
    return tuple(range(position - 1, 7))


def support_u(position: int) -> tuple[int, ...]:
    return tuple(range(7 + position - 1, 14))


def support_cross(left_position: int, right_position: int) -> tuple[int, ...]:
    return support_t(left_position) + support_u(right_position)


def expanded_terms(entry: dict[str, Any]) -> Iterable[dict[str, Any]]:
    species_choices = []
    for row in entry["species_kernels"]:
        left = tuple(int(value) for value in row["left_time_positions"])
        right = tuple(int(value) for value in row["right_time_positions"])
        species_choices.append(
            [
                {
                    "species": row["species"],
                    "right_permutation": permutation,
                    "sign": parity(tuple(right.index(value) for value in permutation)),
                    "supports": tuple(
                        support_cross(left_position, right_position)
                        for left_position, right_position in zip(left, permutation)
                    ),
                }
                for permutation in itertools.permutations(right)
            ]
        )
    for choice in itertools.product(*species_choices):
        factors = [support_t(int(entry["left_old_position"])), support_u(int(entry["right_old_position"]))]
        for species in choice:
            factors.extend(species["supports"])
        if len(factors) != FACTOR_COUNT:
            raise AssertionError("order-six time Gram must have eight Bessel factors")
        yield {
            "leibniz_sign": math.prod(row["sign"] for row in choice),
            "species_permutations": [
                {"species": row["species"], "right_positions": list(row["right_permutation"])}
                for row in choice
            ],
            "supports": tuple(factors),
        }


def hall_lower_bound(factors: tuple[tuple[int, ...], ...]) -> Fraction:
    """Exact bottleneck lower bound for the fractional factor-to-variable flow."""
    optimum = Fraction(0)
    for mask in range(1, 1 << len(factors)):
        chosen = [factors[index] for index in range(len(factors)) if mask & (1 << index)]
        neighborhood = set().union(*map(set, chosen))
        optimum = max(optimum, Fraction(len(chosen), len(neighborhood)))
    return optimum


def rational_allocation(factors: tuple[tuple[int, ...], ...]) -> dict[str, Any]:
    edges = [(factor, variable) for factor, support in enumerate(factors) for variable in support]
    variable_count = len(edges)
    result = linprog(
        [0.0] * variable_count + [1.0],
        A_ub=[
            [1.0 if edge_variable == variable else 0.0 for _factor, edge_variable in edges] + [-1.0]
            for variable in range(len(VARIABLES))
        ],
        b_ub=[0.0] * len(VARIABLES),
        A_eq=[
            [1.0 if edge_factor == factor else 0.0 for edge_factor, _variable in edges] + [0.0]
            for factor in range(len(factors))
        ],
        b_eq=[1.0] * len(factors),
        bounds=[(0.0, None)] * variable_count + [(0.0, None)],
        method="highs",
    )
    if not result.success:
        raise AssertionError(result.message)
    weights = [Fraction(float(value)).limit_denominator(84) for value in result.x[:-1]]
    if any(
        sum(weight for weight, (edge_factor, _variable) in zip(weights, edges) if edge_factor == factor) != 1
        for factor in range(len(factors))
    ):
        raise AssertionError("rationalized denominator weights do not sum to one")
    loads = tuple(
        sum(weight for weight, (_factor, edge_variable) in zip(weights, edges) if edge_variable == variable)
        for variable in range(len(VARIABLES))
    )
    maximum = max(loads)
    lower_bound = hall_lower_bound(factors)
    if maximum != lower_bound or maximum >= 1:
        raise AssertionError("allocation must attain the exact Hall optimum below one")
    factor_rows = []
    for factor, support in enumerate(factors):
        factor_rows.append({
            "support": [VARIABLES[index] for index in support],
            "weights": {
                VARIABLES[variable]: f"{weight.numerator}/{weight.denominator}"
                for weight, (edge_factor, variable) in zip(weights, edges)
                if edge_factor == factor and weight
            },
        })
    return {
        "factors": factor_rows,
        "loads": {VARIABLES[index]: f"{load.numerator}/{load.denominator}" for index, load in enumerate(loads)},
        "dirichlet_parameters": {
            VARIABLES[index]: f"{(1-load).numerator}/{(1-load).denominator}"
            for index, load in enumerate(loads)
        },
        "maximum_load": f"{maximum.numerator}/{maximum.denominator}",
        "minimum_dirichlet_parameter": f"{(1-maximum).numerator}/{(1-maximum).denominator}",
        "hall_optimum": f"{lower_bound.numerator}/{lower_bound.denominator}",
    }


def fraction_row(value: Fraction) -> dict[str, Any]:
    return {"numerator": value.numerator, "denominator": value.denominator, "decimal": float(value)}


def compact_allocation(allocation: dict[str, Any]) -> dict[str, Any]:
    return {
        "support_masks_hex": ",".join(
            format(sum(1 << VARIABLES.index(name) for name in factor["support"]), "x")
            for factor in allocation["factors"]
        ),
        "weights": ";".join(
            ",".join(f"{VARIABLES.index(name)}:{encoded}" for name, encoded in factor["weights"].items())
            for factor in allocation["factors"]
        ),
        "loads": ",".join(allocation["loads"].values()),
        "maximum_load": allocation["maximum_load"],
    }


def proof_safe_bounds(weighted_term_count: int) -> dict[str, Any]:
    # K_1(x) <= 1/x follows from (x K_1(x))' = -x K_0(x) and its unit limit.
    # For beta in [1/3,1], Gamma(beta) < 3 + exp(-1) < 27/8.
    # Also pi > 3 and every w^w <= 1.
    per_term = Fraction(27, 8) ** len(VARIABLES) / Fraction(3**8 * SHIFT**6)
    whole = weighted_term_count * per_term
    # Under the monomial majorant the radial shape is 14-8=6.  At rho=1/4,
    # Q(6,64)=exp(-64) sum_{k=0}^5 64^k/k!, and exp(-64)<(3/8)^64.
    radial_fraction = Fraction(3, 8) ** 64 * sum(Fraction(64**k, math.factorial(k)) for k in range(6))
    # Each Dirichlet marginal has beta>=1/3 and total shape six.  A direct
    # beta-integral bound gives P(z_i<delta)<=192 delta^(1/3).  Union over 14
    # faces and delta=2^-180 gives 2688*2^-60.
    face_fraction = Fraction(2688, 2**60)
    return {
        "per_leibniz_term_global_ceiling": fraction_row(per_term),
        "whole_group_global_ceiling": fraction_row(whole),
        "rho_greater_than_one_quarter_fraction_ceiling": fraction_row(radial_fraction),
        "rho_greater_than_one_quarter_group_ceiling": fraction_row(whole * radial_fraction),
        "any_simplex_coordinate_below_2^-180_fraction_ceiling": fraction_row(face_fraction),
        "any_simplex_coordinate_below_2^-180_group_ceiling": fraction_row(whole * face_fraction),
    }


def gamma_formula_control(allocation: dict[str, Any]) -> float:
    coefficient_log = 0.0
    for factor in allocation["factors"]:
        for encoded in factor["weights"].values():
            weight = float(Fraction(encoded))
            coefficient_log += weight * math.log(weight)
    loads = [float(Fraction(value)) for value in allocation["loads"].values()]
    return math.exp(
        -8.0 * math.log(math.pi)
        -6.0 * math.log(SHIFT)
        + coefficient_log
        + sum(float(gammaln(1.0 - load)) for load in loads)
    )


def pointwise_amgm_control(term: dict[str, Any], sample_index: int) -> bool:
    values = [Fraction((sample_index + 3) * (index + 5) % 37 + 1, 11) for index in range(14)]
    allocation = term["allocation"]
    direct = Fraction(1)
    majorant = 1.0
    for factor in allocation["factors"]:
        direct /= sum(values[VARIABLES.index(name)] for name in factor["support"])
        for name, encoded in factor["weights"].items():
            weight = float(Fraction(encoded))
            majorant *= (weight / float(values[VARIABLES.index(name)])) ** weight
    return float(direct) <= majorant * (1.0 + 1e-12)


def build() -> dict[str, Any]:
    source = json.loads(K184_MANIFEST.read_text())
    source_entries = source["andreief_time_gram_certificate"]["gram_entries"]
    entries = []
    optimum_histogram: dict[str, int] = {}
    all_gamma_bounds = []
    all_terms = []
    allocation_catalog: dict[str, dict[str, Any]] = {}
    for entry_index, entry in enumerate(source_entries):
        terms = []
        for local_index, expanded in enumerate(expanded_terms(entry)):
            allocation = rational_allocation(expanded["supports"])
            key = allocation["maximum_load"]
            optimum_histogram[key] = optimum_histogram.get(key, 0) + 1
            compact = compact_allocation(allocation)
            allocation_bytes = json.dumps(compact, separators=(",", ":"), sort_keys=True).encode()
            allocation_id = hashlib.sha256(allocation_bytes).hexdigest()[:20]
            allocation_catalog.setdefault(allocation_id, compact)
            row = {
                "term_id": f"entry-{entry_index:03d}-term-{local_index:02d}",
                "leibniz_sign": expanded["leibniz_sign"],
                "species_permutations": "|".join(
                    f"{item['species']}:{','.join(map(str, item['right_positions']))}"
                    for item in expanded["species_permutations"]
                ),
                "allocation_id": allocation_id,
            }
            gamma_bound = gamma_formula_control(allocation)
            row["gamma_formula_majorant_control"] = gamma_bound
            terms.append(row)
            all_terms.append({"allocation": allocation, "row": row})
            all_gamma_bounds.append(gamma_bound)
        entries.append({
            "group_id": entry["group_id"],
            "left": entry["left"],
            "right": entry["right"],
            "coefficient_product": entry["coefficient_product"],
            "leibniz_term_count": len(terms),
            "gamma_formula_absolute_entry_control": sum(row["gamma_formula_majorant_control"] for row in terms),
            "terms": terms,
        })
    groups: dict[str, dict[str, Any]] = {}
    old_projection = source["finite_rank_projection_certificate"]["groups"]
    for entry in entries:
        group = groups.setdefault(entry["group_id"], {"weighted_leibniz_term_count": 0, "gamma_formula_group_control": 0.0})
        multiplicity = 1 if entry["left"] == entry["right"] else 2
        group["weighted_leibniz_term_count"] += multiplicity * entry["leibniz_term_count"]
        group["gamma_formula_group_control"] += multiplicity * entry["gamma_formula_absolute_entry_control"]
    for group_id, group in groups.items():
        group["proof_safe_bounds"] = proof_safe_bounds(group["weighted_leibniz_term_count"])
        prior_upper = float(old_projection[group_id]["coherent_norm_squared_triangle_interval"][1])
        group["k184_pathwise_group_upper"] = prior_upper
        group["gamma_formula_improvement_factor_control"] = prior_upper / group["gamma_formula_group_control"]
        group["proof_safe_improvement_factor"] = prior_upper / group["proof_safe_bounds"]["whole_group_global_ceiling"]["decimal"]
    pointwise_checks = [
        pointwise_amgm_control(all_terms[index % len(all_terms)], index)
        for index in range(256)
    ]
    minimum_parameter = min(
        Fraction(term["allocation"]["minimum_dirichlet_parameter"])
        for term in all_terms
    )
    return {
        "schema_version": "1.0",
        "classification": "INTERNAL_STRUCTURAL_ONLY",
        "direction": "observed_to_native",
        "fixed_control": {
            "source_manifest": "lab/process/k184-order-six-certified-low-rank-wave.json",
            "source_entries": len(source_entries),
            "bessel_factors_per_term": FACTOR_COUNT,
            "primitive_time_variables": len(VARIABLES),
            "chart_shift": SHIFT,
        },
        "complete_face_hypergraph": {
            "gram_entries": len(entries),
            "leibniz_terms": len(all_terms),
            "entries": entries,
        },
        "exact_allocation_certificate": {
            "all_denominator_weights_sum_to_one": True,
            "all_variable_loads_strictly_below_one": True,
            "all_allocations_attain_exact_hall_lower_bound": True,
            "maximum_load_histogram": dict(sorted(optimum_histogram.items(), key=lambda row: Fraction(row[0]))),
            "worst_maximum_load": str(max(Fraction(key) for key in optimum_histogram)),
            "minimum_dirichlet_parameter": str(minimum_parameter),
            "allocation_catalog": dict(sorted(allocation_catalog.items())),
            "allocation_catalog_sha256": hashlib.sha256(
                json.dumps(allocation_catalog, separators=(",", ":"), sort_keys=True).encode()
            ).hexdigest(),
        },
        "radial_duffy_certificate": {
            "identity": "x_i=rho*z_i maps each AM--GM monomial to rho^5 exp(-256 rho) times a Dirichlet density with beta_i=1-load_i",
            "radial_shape": len(VARIABLES) - FACTOR_COUNT,
            "radial_weight": "rho^5 exp(-256 rho)",
            "angular_weight": "product_i z_i^(beta_i-1) on Delta_13; recursively Duffy-factorizable into beta-weighted Jacobi coordinates",
            "all_beta_at_least_one_third": minimum_parameter >= Fraction(1, 3),
            "determinants_remain_unexpanded_in_numerical_core": True,
            "face_delta": "2^-180",
            "large_radius_cutoff": "1/4",
        },
        "groups": dict(sorted(groups.items())),
        "independent_controls": {
            "pointwise_amgm_samples_passed": sum(pointwise_checks),
            "pointwise_amgm_samples_total": len(pointwise_checks),
            "gamma_formula_term_min": min(all_gamma_bounds),
            "gamma_formula_term_max": max(all_gamma_bounds),
            "role": "floating gamma evaluations and sampled inequalities sharpen and check the exact rational certificate; proof-safe rational ceilings carry outward claims",
        },
        "release_test": {
            "all_234_time_gram_entries_covered": len(entries) == 234,
            "all_1864_leibniz_terms_covered": len(all_terms) == 1864,
            "all_faces_have_exact_integrable_duffy_weights": minimum_parameter >= Fraction(1, 3),
            "large_radius_tail_has_explicit_bound": True,
            "face_strip_has_explicit_bound": True,
            "determinant_preserving_compact_core_quadrature_error_serialized": False,
            "accurate_order_six_prefix_released": False,
            "coefficient_complete_base_action_column_evaluated": False,
            "complete_R_ref_form_dual_residual_serialized": False,
            "positive_complete_M_orthogonal_complement_or_flux_floor_serialized": False,
            "scalar_center_left_floor_serialized": False,
            "native_K152_interval_emitted": False,
        },
        "next_exact_input": {
            "owner": "determinant-preserving weighted compact-core cubature",
            "first_gate": "factor each size-two/three Bessel determinant into ordered-time Vandermonde factors or certified divided differences, then interval the bounded Duffy/Jacobi quotient on the rho<=1/4 and z_i>=2^-180 core",
            "must_preserve": "all 234 coherent Gram entries, K179 signs, old-position factors, complete species determinants and shared time nodes",
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
    parser.add_argument("--write", action="store_true")
    parser.add_argument("--summary", action="store_true")
    args = parser.parse_args()
    payload = build()
    if args.write:
        OUTPUT.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
    if args.summary or not args.write:
        summary = {key: payload[key] for key in (
            "fixed_control", "radial_duffy_certificate", "independent_controls",
            "release_test", "next_exact_input",
        )}
        summary["exact_allocation_certificate"] = {
            key: value for key, value in payload["exact_allocation_certificate"].items()
            if key != "allocation_catalog"
        }
        summary["group_bound_range"] = {
            "gamma_formula_control": [
                min(row["gamma_formula_group_control"] for row in payload["groups"].values()),
                max(row["gamma_formula_group_control"] for row in payload["groups"].values()),
            ],
            "proof_safe": [
                min(row["proof_safe_bounds"]["whole_group_global_ceiling"]["decimal"] for row in payload["groups"].values()),
                max(row["proof_safe_bounds"]["whole_group_global_ceiling"]["decimal"] for row in payload["groups"].values()),
            ],
        }
        print(json.dumps(summary, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
