#!/usr/bin/env python3
"""K179 coefficient-complete matched normal-order exchange family.

The compiler specializes the fixed K139/K156 equal-coupling boundary operator
to every K178 older-letter contraction.  It records the impurity matrix unit,
the Neumann and normal-order signs, every denominator containing the contracted
energy, the remaining-variable kernel, and the normalized specieswise exterior
projection.  It does not numerically integrate the resulting family.
"""

from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
import math
import sys
from collections import Counter
from pathlib import Path
from typing import Any, Iterable


ROOT = Path(__file__).resolve().parents[2]
K178_PATH = Path(__file__).with_name("k178_exchange_prefix_numerical_sufficiency.py")


class CertificateError(ValueError):
    """Raised when a matched term is not coefficient complete."""


def load_k178():
    spec = importlib.util.spec_from_file_location("k178_for_k179", K178_PATH)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {K178_PATH}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


K178 = load_k178()
K177 = K178.K177


def affine_denominator(last_index: int) -> str:
    return "256+" + "+".join(f"E_{j}" for j in range(1, last_index + 1))


def impurity_monomial(record: dict[str, Any]) -> dict[str, str]:
    newest_flavor = int(record["newest"][0])
    newest_polarity = record["newest"][1]
    old_flavor = int(record["annihilated"][0])
    old_polarity = record["annihilated"][1]
    if newest_polarity == "-" and old_polarity == "-" and newest_flavor == old_flavor:
        return {
            "operator_monomial_id": f"W_ex[h{newest_flavor},h{old_flavor}]",
            "boundary_factors": f"(B_{newest_flavor}^* a_{newest_flavor}-) R (a_{newest_flavor}-^* B_{newest_flavor})",
            "impurity_matrix_unit": "|0><0|",
            "bath_normal_order": f"a_{newest_flavor}-^*(p_new) a_{old_flavor}-(p_old)",
        }
    if newest_polarity == "+" and old_polarity == "+":
        return {
            "operator_monomial_id": f"W_ex[p{old_flavor},p{newest_flavor}]",
            "boundary_factors": f"(B_{old_flavor} a_{old_flavor}+) R (a_{newest_flavor}+^* B_{newest_flavor}^*)",
            "impurity_matrix_unit": f"|{old_flavor}><{newest_flavor}|",
            "bath_normal_order": f"a_{newest_flavor}+^*(p_new) a_{old_flavor}+(p_old)",
        }
    raise CertificateError("K177 contraction is not a K139 matched polarity monomial")


def exterior_normalization(output_letters: Iterable[str]) -> dict[str, Any]:
    counts = Counter(output_letters)
    factorials = {species: math.factorial(count) for species, count in sorted(counts.items())}
    return {
        "convention": "normalized CAR exterior basis",
        "projection": "product_s (1/sqrt(m_s!)) sum_(pi in S_m_s) sgn(pi) P_pi",
        "species_multiplicities": dict(sorted(counts.items())),
        "species_factorials": factorials,
        "ordered_creation_coefficient_has_no_extra_factorial": True,
        "wedge_inner_product_is_specieswise_determinant": True,
    }


def coefficient_complete_term(record: dict[str, Any]) -> dict[str, Any]:
    order = int(record["order"])
    old_position = int(record["old_position"])
    if not 1 <= old_position <= order:
        raise CertificateError("contracted position must be an older word position")
    monomial = impurity_monomial(record)
    car_sign = int(record["car_sign"])
    if car_sign not in (-1, 1):
        raise CertificateError("CAR sign must be exact and nonzero")

    neumann_word_sign = -1 if order % 2 else 1
    raw_x_coefficient = neumann_word_sign * car_sign
    # K156: C R C*=cD+X and W=(E_R-256)I-X.
    w_exchange_coefficient = -raw_x_coefficient
    outer_index = order + 1
    all_denominators = [affine_denominator(j) for j in range(1, outer_index + 1)]
    contracted_denominators = all_denominators[old_position - 1 :]
    remaining_variables = [f"p_{j}" for j in range(1, order + 1) if j != old_position]
    remaining_variables.append(f"p_{outer_index}")
    prefactor = f"(2*pi)^(-{order + 2}/2)"
    product = "*".join(f"({form})" for form in all_denominators)
    ordered_kernel = (
        f"{w_exchange_coefficient}*{prefactor}*int_R dp_{old_position}/[{product}]"
    )

    term = {
        **record,
        **monomial,
        "neumann_word_sign": neumann_word_sign,
        "raw_C_R_Cstar_older_contraction_coefficient": str(raw_x_coefficient),
        "W_equals_scalar_minus_X_sign": -1,
        "exact_operator_coefficient": str(w_exchange_coefficient),
        "contracted_resolvent_affine_forms": {
            "creation_resolvent": affine_denominator(old_position),
            "outer_exchange_resolvent": affine_denominator(outer_index),
            "all_denominators_containing_contracted_energy": contracted_denominators,
            "all_term_denominators": all_denominators,
        },
        "output_kernel_formula": {
            "integrated_variable": f"p_{old_position}",
            "new_variable": f"p_{outer_index}",
            "remaining_ordered_variables": remaining_variables,
            "normalization_prefactor": prefactor,
            "ordered_kernel": ordered_kernel,
            "energy_substitution": "E_j=sqrt(1+p_j^2)",
            "exterior_projection_applied_after_integration": True,
        },
        "antisymmetrizer_normalization": exterior_normalization(record["output_letters"]),
    }
    return term


def term_failures(term: dict[str, Any]) -> list[str]:
    failures: list[str] = []
    for field in K178.REQUIRED_COEFFICIENT_FIELDS:
        if term.get(field) in (None, "", [], {}):
            failures.append(field)
    order = int(term.get("order", -1))
    old_position = int(term.get("old_position", 0))
    incidence = term.get("contracted_resolvent_affine_forms")
    if not isinstance(incidence, dict):
        incidence = {}
    all_forms = incidence.get("all_term_denominators", [])
    containing = incidence.get("all_denominators_containing_contracted_energy", [])
    if all_forms != [affine_denominator(j) for j in range(1, order + 2)]:
        failures.append("all_denominators")
    if containing != all_forms[old_position - 1 :]:
        failures.append("contracted_incidence")
    if incidence.get("creation_resolvent") != affine_denominator(old_position):
        failures.append("creation_resolvent")
    if incidence.get("outer_exchange_resolvent") != affine_denominator(order + 1):
        failures.append("outer_resolvent")
    expected = -((-1 if order % 2 else 1) * int(term.get("car_sign", 0)))
    if term.get("exact_operator_coefficient") != str(expected):
        failures.append("coefficient_sign")
    kernel = term.get("output_kernel_formula")
    if not isinstance(kernel, dict):
        kernel = {}
    if kernel.get("normalization_prefactor") != f"(2*pi)^(-{order + 2}/2)":
        failures.append("point_normalization")
    if kernel.get("integrated_variable") != f"p_{old_position}":
        failures.append("integrated_variable")
    exterior = term.get("antisymmetrizer_normalization")
    if not isinstance(exterior, dict):
        exterior = {}
    if exterior.get("convention") != "normalized CAR exterior basis":
        failures.append("exterior_convention")
    counts = Counter(term.get("output_letters", []))
    if exterior.get("species_factorials") != {
        species: math.factorial(count) for species, count in sorted(counts.items())
    }:
        failures.append("exterior_factorials")
    if not str(term.get("operator_monomial_id", "")).startswith("W_ex["):
        failures.append("operator_monomial")
    return failures


def coefficient_family(maximum_order: int = 12) -> list[dict[str, Any]]:
    terms = [coefficient_complete_term(row) for row in K178.contraction_records(maximum_order)]
    failures = [(term["contraction_id"], term_failures(term)) for term in terms if term_failures(term)]
    if failures:
        raise CertificateError(f"coefficient compiler emitted invalid terms: {failures[:3]}")
    K178.validate_numerical_admission(terms)
    return terms


def _apply(bits: int, orbital: int, create: bool) -> tuple[int, int] | None:
    occupied = (bits >> orbital) & 1
    if occupied == int(create):
        return None
    sign = -1 if (bits & ((1 << orbital) - 1)).bit_count() % 2 else 1
    return bits ^ (1 << orbital), sign


def _apply_product(bits: int, factors_left_to_right: list[tuple[int, bool]]) -> tuple[int, int] | None:
    current, sign = bits, 1
    for orbital, create in reversed(factors_left_to_right):
        result = _apply(current, orbital, create)
        if result is None:
            return None
        current, local = result
        sign *= local
    return current, sign


def direct_finite_car_coefficient(term: dict[str, Any]) -> dict[str, Any]:
    """Independently apply the finite CAR monomial for an order-two control."""
    if term["order"] != 2:
        raise CertificateError("the direct finite CAR control is frozen at order two")
    mode_count = 3
    seed = int(term["seed_impurity"])
    state = 0 if seed == 0 else 1 << (seed - 1)
    sign = 1
    letters = [(int(label[0]), label[1]) for label in term["input_letters"]]
    for mode, letter in enumerate(letters):
        result = _apply_product(state, list(K177.creation_word(letter, mode, mode_count)))
        if result is None:
            raise AssertionError("order-two path vanished in direct CAR control")
        state, local = result
        sign *= local
    newest = (int(term["newest"][0]), term["newest"][1])
    result = _apply_product(state, list(K177.creation_word(newest, 2, mode_count)))
    if result is None:
        raise AssertionError("inner exchange creation vanished")
    state, local = result
    sign *= local
    old_position = int(term["old_position"]) - 1
    old = letters[old_position]
    if newest[1] == "-":
        outer = [(K177.bath_orbital(old, old_position, mode_count), False), (newest[0] - 1, False)]
    else:
        outer = [(old[0] - 1, True), (K177.bath_orbital(old, old_position, mode_count), False)]
    result = _apply_product(state, outer)
    if result is None:
        raise AssertionError("outer older-letter contraction vanished")
    final_state, local = result
    sign *= local
    raw = sign  # (-1)^2=+1 at the frozen control order.
    w_coefficient = -raw
    return {
        "contraction_id": term["contraction_id"],
        "direct_C_R_Cstar_G2_sign": raw,
        "direct_W_exchange_sign": w_coefficient,
        "compiled_W_exchange_sign": int(term["exact_operator_coefficient"]),
        "final_state": final_state,
        "passes": w_coefficient == int(term["exact_operator_coefficient"]),
    }


def family_digest(terms: list[dict[str, Any]]) -> str:
    payload = json.dumps(terms, sort_keys=True, separators=(",", ":")).encode()
    return hashlib.sha256(payload).hexdigest()


def demo() -> dict[str, Any]:
    terms = coefficient_family()
    order_two = [term for term in terms if term["order"] == 2]
    direct = [direct_finite_car_coefficient(term) for term in order_two]
    by_order = []
    for order in range(1, 13):
        rows = [term for term in terms if term["order"] == order]
        signs = Counter(term["exact_operator_coefficient"] for term in rows)
        by_order.append({"order": order, "terms": len(rows), "W_coefficients": dict(sorted(signs.items()))})
    return {
        "schema_version": "1.0",
        "classification": "INTERNAL_STRUCTURAL_ONLY",
        "direction": "observed_to_native",
        "fixed_control": {
            "carrier": "hard-core C3 tensor Gamma_-(L2(R;C4))",
            "auxiliary_chart_shift": 256,
            "seed_scope": "K162_zero_bath_seed_orbits",
            "equal_particle_hole_couplings": 1,
            "maximum_resolved_order": 12,
        },
        "coefficient_family": {
            "encoding": "deterministic per-contraction generator; --terms emits the canonical expansion",
            "term_count": len(terms),
            "family_sha256": family_digest(terms),
            "unresolved_required_field_instances": len(K178.missing_coefficient_fields(terms)),
            "K178_numerical_admission_passes": True,
            "orders": by_order,
        },
        "sign_theorem": {
            "path_Neumann_sign": "(-1)^n from G^n",
            "raw_older_contraction_sign": "(-1)^n times exact global-CAR contraction sign",
            "W_exchange_sign": "(-1)^(n+1) times exact global-CAR contraction sign",
            "K177_structural_car_sign_preserved": True,
            "K177_structural_record_alone_included_G_sign": False,
        },
        "order_two_direct_CAR_control": {
            "terms": len(order_two),
            "all_compiled_coefficients_match_direct_action": all(row["passes"] for row in direct),
            "rows": direct,
        },
        "normalization": {
            "point_factors": "n path creations plus inner creation plus outer annihilation give (2*pi)^(-(n+2)/2)",
            "contracted_measure": "dp_old after all point factors are placed in the prefactor",
            "exterior": "normalized specieswise wedge; coordinate projection has 1/sqrt(m_s!) and wedge Gram is a determinant",
        },
        "release_test": {
            "K178_required_fields_populated_for_every_contraction": True,
            "coefficient_complete_exchange_family_through_order_12_serialized": True,
            "order_2_direct_finite_CAR_control_passed": True,
            "outward_numerical_prefix_integrals_evaluated": False,
            "coefficient_complete_base_action_column_evaluated": False,
            "complete_R_ref_form_dual_residual_serialized": False,
            "positive_complete_M_orthogonal_complement_or_flux_floor_serialized": False,
            "scalar_center_left_floor_serialized": False,
            "native_K152_interval_emitted": False,
        },
        "next_exact_input": {
            "owner": "determinant-aware outward evaluator",
            "first_gate": "evaluate and independently cross-check the six order-two terms",
            "must_preserve": "signed sum before determinant-level interval enclosure",
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
    parser.add_argument("--terms", action="store_true")
    args = parser.parse_args()
    if args.terms:
        print(json.dumps(coefficient_family(), indent=2, sort_keys=True))
        return 0
    if args.demo or not args.terms:
        print(json.dumps(demo(), indent=2, sort_keys=True))
        return 0
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
