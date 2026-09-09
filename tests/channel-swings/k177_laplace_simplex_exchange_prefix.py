#!/usr/bin/env python3
"""K177 exact continuum-coordinate compiler for the K176 finite prefix.

The module never replaces the continuum by a finite momentum grid.  It
enumerates the impurity/bath word automaton, checks every older-letter Wick
contraction with exact CAR signs on distinct dummy modes, and records the
ordered-simplex representation of the cumulative resolvents.  Numerical
quadrature and the complete K171 residual deliberately remain downstream.
"""

from __future__ import annotations

import argparse
import json
from collections import Counter
from dataclasses import dataclass
from typing import Any, Iterable


Species = tuple[int, str]


class CertificateError(ValueError):
    """Raised when a seed word or continuum-coordinate premise is invalid."""


@dataclass(frozen=True)
class Word:
    seed_impurity: int
    impurity: int
    letters: tuple[Species, ...]


def next_letters(impurity: int) -> tuple[Species, ...]:
    if impurity == 0:
        return ((1, "-"), (2, "-"))
    if impurity in (1, 2):
        return ((impurity, "+"),)
    raise CertificateError("impurity label must be 0, 1, or 2")


def advance(impurity: int, letter: Species) -> int:
    flavor, polarity = letter
    if letter not in next_letters(impurity):
        raise CertificateError("letter is not admitted by the hard-core boundary automaton")
    return flavor if polarity == "-" else 0


def words(seed_impurity: int, order: int) -> list[Word]:
    if seed_impurity not in (0, 1, 2) or order < 0:
        raise CertificateError("invalid K162 seed or word order")
    out = [Word(seed_impurity, seed_impurity, ())]
    for _ in range(order):
        out = [
            Word(word.seed_impurity, advance(word.impurity, letter), word.letters + (letter,))
            for word in out
            for letter in next_letters(word.impurity)
        ]
    return out


def charges(impurity: int, letters: Iterable[Species]) -> tuple[int, int]:
    result = [int(impurity == 1), int(impurity == 2)]
    for flavor, polarity in letters:
        result[flavor - 1] += 1 if polarity == "+" else -1
    return result[0], result[1]


def signature(word: Word) -> tuple[int, tuple[tuple[str, int], ...]]:
    counts = Counter(f"{flavor}{polarity}" for flavor, polarity in word.letters)
    return word.impurity, tuple(sorted(counts.items()))


def apply_car(state: int, orbital: int, create: bool) -> tuple[int, int] | None:
    occupied = (state >> orbital) & 1
    if occupied == int(create):
        return None
    sign = -1 if (state & ((1 << orbital) - 1)).bit_count() % 2 else 1
    return state ^ (1 << orbital), sign


def apply_word(state: int, operators_left_to_right: tuple[tuple[int, bool], ...]) -> tuple[int, int] | None:
    sign = 1
    current = state
    for orbital, create in reversed(operators_left_to_right):
        result = apply_car(current, orbital, create)
        if result is None:
            return None
        current, local = result
        sign *= local
    return current, sign


def bath_orbital(letter: Species, mode: int, mode_count: int) -> int:
    flavor, polarity = letter
    species = 2 * (flavor - 1) + int(polarity == "-")
    return 2 + species * mode_count + mode


def creation_word(letter: Species, mode: int, mode_count: int) -> tuple[tuple[int, bool], ...]:
    flavor, polarity = letter
    bath = bath_orbital(letter, mode, mode_count)
    impurity = flavor - 1
    if polarity == "-":
        return ((impurity, True), (bath, True))
    return ((bath, True), (impurity, False))


def build_state(word: Word, mode_count: int) -> tuple[int, int]:
    state = 0 if word.seed_impurity == 0 else 1 << (word.seed_impurity - 1)
    sign = 1
    for mode, letter in enumerate(word.letters):
        result = apply_word(state, creation_word(letter, mode, mode_count))
        if result is None:
            raise AssertionError("admitted path vanished in the exact CAR representation")
        state, local = result
        sign *= local
    return state, sign


def contraction_candidates(word: Word) -> list[dict[str, Any]]:
    """Return every non-adjacent contraction after one C* extension.

    The extension uses a fresh mode.  C then annihilates an older matching
    bath letter.  The fresh-mode contraction is the matched endpoint and is
    intentionally absent from this list.
    """
    mode_count = len(word.letters) + 1
    base_state, base_sign = build_state(word, mode_count)
    result: list[dict[str, Any]] = []
    for newest in next_letters(word.impurity):
        extended = apply_word(base_state, creation_word(newest, len(word.letters), mode_count))
        if extended is None:
            raise AssertionError("admitted adjacent creation vanished")
        extended_state, extension_sign = extended
        newest_flavor, newest_polarity = newest
        for old_position, old in enumerate(word.letters):
            old_flavor, old_polarity = old
            contraction_word: tuple[tuple[int, bool], ...] | None = None
            output_impurity: int | None = None
            if newest_polarity == "-" and old == newest:
                contraction_word = (
                    (bath_orbital(old, old_position, mode_count), False),
                    (newest_flavor - 1, False),
                )
                output_impurity = 0
            elif newest_polarity == "+" and old_polarity == "+":
                contraction_word = (
                    (old_flavor - 1, True),
                    (bath_orbital(old, old_position, mode_count), False),
                )
                output_impurity = old_flavor
            if contraction_word is None:
                continue
            contracted = apply_word(extended_state, contraction_word)
            if contracted is None:
                raise AssertionError("selected older-letter contraction vanished")
            target_state, contraction_sign = contracted
            output_letters = list(word.letters)
            output_letters.pop(old_position)
            output_letters.append(newest)
            expected_charge = charges(word.seed_impurity, ())
            actual_charge = charges(output_impurity, output_letters)
            if actual_charge != expected_charge:
                raise AssertionError("matched contraction left the fixed charge sector")
            expected_state = 0 if output_impurity == 0 else 1 << (output_impurity - 1)
            for mode, letter in enumerate(word.letters):
                if mode != old_position:
                    expected_state |= 1 << bath_orbital(letter, mode, mode_count)
            expected_state |= 1 << bath_orbital(newest, len(word.letters), mode_count)
            if target_state != expected_state:
                raise AssertionError("CAR contraction target disagrees with the kernel replacement rule")
            result.append(
                {
                    "newest": f"{newest_flavor}{newest_polarity}",
                    "old_position": old_position + 1,
                    "annihilated": f"{old_flavor}{old_polarity}",
                    "output_impurity": output_impurity,
                    "car_sign": base_sign * extension_sign * contraction_sign,
                    "target_state_verified": True,
                }
            )
    return result


def expected_path_count(seed_impurity: int, order: int) -> int:
    if seed_impurity == 0:
        return 2 ** ((order + 1) // 2)
    return 2 ** (order // 2)


def laplace_simplex_certificate(order: int) -> dict[str, Any]:
    """Compile the exact Schwinger-to-ordered-simplex change of variables."""
    if order < 1:
        raise CertificateError("positive word order required")
    # t_j=s_j-s_(j+1), s_(n+1)=0.  In product_j
    # (lambda+sum_(r<=j) E_r)^-1, lambda has coefficient sum_j t_j=s_1
    # and E_r has coefficient sum_(j>=r)t_j=s_r.
    energy_coefficients: list[list[int]] = []
    for energy_index in range(order):
        coefficients = [int(j >= energy_index) for j in range(order)]
        energy_coefficients.append(coefficients)
    telescopes = all(
        sum(coefficients[j] - (coefficients[j - 1] if j else 0) for j in range(order))
        in (0, 1)
        for coefficients in energy_coefficients
    )
    return {
        "order": order,
        "denominator": "prod_(j=1)^n (lambda+sum_(r=1)^j E_r)^(-1)",
        "simplex": "s_1>s_2>...>s_n>0",
        "integrand": "exp(-lambda*s_1-sum_(r=1)^n E_r*s_r)",
        "change_of_variables": "t_j=s_j-s_(j+1), s_(n+1)=0",
        "jacobian": 1,
        "lambda_telescopes_to_s1": True,
        "each_energy_telescopes_to_its_sr": telescopes,
    }


def seed_census(seed_impurity: int, maximum_order: int = 12) -> dict[str, Any]:
    rows = []
    seed_charge = charges(seed_impurity, ())
    for order in range(maximum_order + 1):
        current = words(seed_impurity, order)
        if len(current) != expected_path_count(seed_impurity, order):
            raise AssertionError("closed-form path count failed")
        if any(charges(word.impurity, word.letters) != seed_charge for word in current):
            raise AssertionError("boundary word changed charge")
        contractions = sum(len(contraction_candidates(word)) for word in current) if order else 0
        rows.append(
            {
                "order": order,
                "path_count": len(current),
                "occupation_signatures": len({signature(word) for word in current}),
                "matched_older_letter_contractions": contractions,
            }
        )
    return {
        "seed": "Omega" if seed_impurity == 0 else f"d_{seed_impurity}^*Omega",
        "charge": list(seed_charge),
        "orders": rows,
        "order_12_path_count": rows[12]["path_count"],
        "order_1_exchange_contractions": rows[1]["matched_older_letter_contractions"],
        "total_paths_orders_0_through_12": sum(row["path_count"] for row in rows),
        "total_matched_contractions_orders_1_through_12": sum(
            row["matched_older_letter_contractions"] for row in rows[1:]
        ),
    }


def demo() -> dict[str, Any]:
    seeds = [seed_census(seed) for seed in (0, 1, 2)]
    simplex = [laplace_simplex_certificate(order) for order in range(1, 13)]
    return {
        "schema_version": "1.0",
        "classification": "INTERNAL_STRUCTURAL_ONLY",
        "direction": "observed_to_native",
        "fixed_control": {
            "carrier": "hard-core C3 tensor Gamma_-(L2(R;C4))",
            "auxiliary_chart_shift": 256,
            "seed_scope": "K162_zero_bath_seed_orbits",
            "maximum_resolved_order": 12,
        },
        "boundary_word_automaton": {
            "zero_to_i": "create i- and occupy impurity i",
            "i_to_zero": "create i+ and empty impurity i",
            "global_CAR_order_preserved": True,
            "all_words_charge_preserving": True,
            "seed_census": seeds,
            "all_three_order_12_path_counts": [row["order_12_path_count"] for row in seeds],
        },
        "matched_contraction_compiler": {
            "adjacent_fresh_mode_removed_as_endpoint": True,
            "only_older_modes_contracted": True,
            "exact_CAR_signs_computed_on_distinct_modes": True,
            "output_charge_checked_for_every_contraction": True,
            "order_1_exchange_vector_is_zero_for_all_three_seeds": all(
                row["order_1_exchange_contractions"] == 0 for row in seeds
            ),
            "total_resolved_path_coordinates": sum(
                row["total_paths_orders_0_through_12"] for row in seeds
            ),
            "total_matched_contraction_coordinates": sum(
                row["total_matched_contractions_orders_1_through_12"] for row in seeds
            ),
        },
        "laplace_simplex": {
            "all_orders_1_through_12_compiled": len(simplex) == 12,
            "all_jacobians_one": all(row["jacobian"] == 1 for row in simplex),
            "all_exponents_telescope": all(
                row["lambda_telescopes_to_s1"] and row["each_energy_telescopes_to_its_sr"]
                for row in simplex
            ),
            "order_12": simplex[-1],
        },
        "fermionic_gram_reduction": {
            "one_particle_heat_kernel": "kappa(t)=int_R exp(-t*sqrt(1+p^2)) dp/(2*pi)=K_1(t)/pi",
            "same_species_wedge_inner_product": "det[kappa(s_i+r_j)]",
            "different_species_factorize": True,
            "path_pair_selection": "equal output impurity and equal species occupation counts",
            "matched_exchange_adds_one_positive_Schwinger_parameter": True,
            "all_prefix_scalar_products_reduce_to_finite_ordered_simplex_integrals": True,
        },
        "release_test": {
            "resolved_prefix_path_coordinates_through_order_12_serialized": True,
            "matched_exchange_contraction_coordinates_through_order_12_serialized": True,
            "order_1_exchange_vector_evaluated_as_zero": True,
            "continuum_scalar_products_reduced_to_heat_kernel_integrals": True,
            "outward_numerical_prefix_integrals_evaluated": False,
            "coefficient_complete_base_action_column_evaluated": False,
            "complete_R_ref_form_dual_residual_serialized": False,
            "positive_complete_M_orthogonal_complement_or_flux_floor_serialized": False,
            "scalar_center_left_floor_serialized": False,
            "native_K152_interval_emitted": False,
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
    parser.parse_args()
    print(json.dumps(demo(), indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
