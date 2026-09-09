#!/usr/bin/env python3
"""K178 numerical-sufficiency audit for the K177 exchange prefix.

K177 proves an exact representation class and exposes the automaton needed to
enumerate its structural coordinates.  This module compiles that complete
structural skeleton and checks the stronger question needed by outward
quadrature: whether every signed coefficient-level integral is actually
determined.  It never guesses missing normal-order coefficients.
"""

from __future__ import annotations

import argparse
import importlib.util
import json
import sys
from collections import Counter, defaultdict
from fractions import Fraction
from pathlib import Path
from typing import Any, Iterable


ROOT = Path(__file__).resolve().parents[2]
K177_PATH = Path(__file__).with_name("k177_laplace_simplex_exchange_prefix.py")
REQUIRED_COEFFICIENT_FIELDS = (
    "operator_monomial_id",
    "exact_operator_coefficient",
    "contracted_resolvent_affine_forms",
    "output_kernel_formula",
    "antisymmetrizer_normalization",
)


class CertificateError(ValueError):
    """Raised when a coefficient-level integral family is incomplete."""


def load_k177():
    spec = importlib.util.spec_from_file_location("k177_for_k178", K177_PATH)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {K177_PATH}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


K177 = load_k177()


def species_label(letter: tuple[int, str]) -> str:
    return f"{letter[0]}{letter[1]}"


def occupation_signature(impurity: int, letters: Iterable[tuple[int, str]]) -> str:
    counts = Counter(species_label(letter) for letter in letters)
    body = ",".join(f"{key}^{counts[key]}" for key in sorted(counts))
    return f"d={impurity}|{body}"


def denominator_prefixes(order: int) -> list[str]:
    return ["256+" + "+".join(f"E_{r}" for r in range(1, j + 1)) for j in range(1, order + 1)]


def path_records(maximum_order: int = 12) -> list[dict[str, Any]]:
    records: list[dict[str, Any]] = []
    for seed in (0, 1, 2):
        for order in range(maximum_order + 1):
            for path_index, word in enumerate(K177.words(seed, order), start=1):
                mode_count = order + 1
                _, car_sign = K177.build_state(word, mode_count)
                records.append(
                    {
                        "path_id": f"seed-{seed}-order-{order}-path-{path_index}",
                        "seed_impurity": seed,
                        "order": order,
                        "path_index": path_index,
                        "letters": [species_label(letter) for letter in word.letters],
                        "output_impurity": word.impurity,
                        "occupation_signature": occupation_signature(word.impurity, word.letters),
                        "global_car_sign": car_sign,
                        "ordered_energy_variables": [f"E_{j}" for j in range(1, order + 1)],
                        "cumulative_denominator_factors": denominator_prefixes(order),
                    }
                )
    return records


def contraction_records(maximum_order: int = 12) -> list[dict[str, Any]]:
    records: list[dict[str, Any]] = []
    for seed in (0, 1, 2):
        for order in range(1, maximum_order + 1):
            for path_index, word in enumerate(K177.words(seed, order), start=1):
                path_id = f"seed-{seed}-order-{order}-path-{path_index}"
                for contraction_index, contraction in enumerate(
                    K177.contraction_candidates(word), start=1
                ):
                    old_position = contraction["old_position"]
                    newest = (int(contraction["newest"][0]), contraction["newest"][1])
                    output_letters = list(word.letters)
                    output_letters.pop(old_position - 1)
                    output_letters.append(newest)
                    record = {
                        "contraction_id": f"{path_id}-contraction-{contraction_index}",
                        "path_id": path_id,
                        "seed_impurity": seed,
                        "order": order,
                        "input_letters": [species_label(letter) for letter in word.letters],
                        "newest": contraction["newest"],
                        "old_position": old_position,
                        "annihilated": contraction["annihilated"],
                        "output_impurity": contraction["output_impurity"],
                        "output_letters": [species_label(letter) for letter in output_letters],
                        "output_signature": occupation_signature(
                            contraction["output_impurity"], output_letters
                        ),
                        "car_sign": contraction["car_sign"],
                        "output_variable_provenance": [
                            j for j in range(1, order + 1) if j != old_position
                        ]
                        + [order + 1],
                        "base_cumulative_denominator_factors": denominator_prefixes(order),
                    }
                    for field in REQUIRED_COEFFICIENT_FIELDS:
                        record[field] = None
                    records.append(record)
    return records


def missing_coefficient_fields(records: Iterable[dict[str, Any]]) -> list[tuple[str, str]]:
    missing: list[tuple[str, str]] = []
    for record in records:
        identity = str(record.get("contraction_id", "unknown"))
        for field in REQUIRED_COEFFICIENT_FIELDS:
            value = record.get(field)
            if value is None or value == "" or value == []:
                missing.append((identity, field))
    return missing


def validate_numerical_admission(records: Iterable[dict[str, Any]]) -> None:
    missing = missing_coefficient_fields(records)
    if missing:
        raise CertificateError(
            f"coefficient-level family incomplete: {len(missing)} unresolved field instances"
        )


def positive_control_term() -> dict[str, Any]:
    return {
        "contraction_id": "control-order-2",
        "operator_monomial_id": "X_ex[1-,1+]",
        "exact_operator_coefficient": "-1",
        "contracted_resolvent_affine_forms": ["256+E_1", "256+E_1+E_3"],
        "output_kernel_formula": "Alt[(2*pi)^(-3/2)/(D_1*D_2*D_3)]",
        "antisymmetrizer_normalization": "specieswise exterior convention fixed",
    }


def quadratic_value(coefficients: Iterable[Fraction], gram: list[list[Fraction]]) -> Fraction:
    vector = list(coefficients)
    if len(gram) != len(vector) or any(len(row) != len(vector) for row in gram):
        raise CertificateError("coefficient vector and Gram dimensions disagree")
    return sum(vector[i] * gram[i][j] * vector[j] for i in range(len(vector)) for j in range(len(vector)))


def nonidentifiability_control() -> dict[str, Any]:
    gram = [[Fraction(1)]]
    first = quadratic_value([Fraction(1)], gram)
    second = quadratic_value([Fraction(2)], gram)
    return {
        "shared_structural_skeleton": True,
        "shared_generic_heat_kernel_gram": True,
        "coefficient_assignments": ["1", "2"],
        "quadratic_values": [str(first), str(second)],
        "values_differ": first != second,
        "native_coefficient_selected": False,
    }


def census() -> dict[str, Any]:
    paths = path_records()
    contractions = contraction_records()
    path_groups: dict[tuple[int, int, str], list[dict[str, Any]]] = defaultdict(list)
    contraction_groups: dict[tuple[int, int, str], list[dict[str, Any]]] = defaultdict(list)
    for row in paths:
        path_groups[(row["seed_impurity"], row["order"], row["occupation_signature"])].append(row)
    for row in contractions:
        contraction_groups[(row["seed_impurity"], row["order"], row["output_signature"])].append(row)
    ambiguous = [
        rows
        for rows in contraction_groups.values()
        if len(rows) > 1
        and len({(row["path_id"], row["old_position"], tuple(row["output_variable_provenance"])) for row in rows}) > 1
    ]
    by_order = []
    for order in range(13):
        order_paths = [row for row in paths if row["order"] == order]
        order_contractions = [row for row in contractions if row["order"] == order]
        by_order.append(
            {
                "order": order,
                "path_records": len(order_paths),
                "path_signature_blocks": len(
                    {(row["seed_impurity"], row["occupation_signature"]) for row in order_paths}
                ),
                "contraction_records": len(order_contractions),
                "contraction_signature_blocks": len(
                    {(row["seed_impurity"], row["output_signature"]) for row in order_contractions}
                ),
            }
        )
    return {
        "path_records": len(paths),
        "path_signature_blocks": len(path_groups),
        "contraction_records": len(contractions),
        "contraction_signature_blocks": len(contraction_groups),
        "ambiguous_multi_record_contraction_signature_blocks": len(ambiguous),
        "unresolved_coefficient_field_instances": len(missing_coefficient_fields(contractions)),
        "by_order": by_order,
    }


def demo() -> dict[str, Any]:
    current = contraction_records()
    rejected = False
    try:
        validate_numerical_admission(current)
    except CertificateError:
        rejected = True
    validate_numerical_admission([positive_control_term()])
    counts = census()
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
        "structural_compiler": counts,
        "numerical_admission_contract": {
            "required_coefficient_fields": list(REQUIRED_COEFFICIENT_FIELDS),
            "current_k177_family_rejected": rejected,
            "positive_complete_control_accepted": True,
            "census_or_generic_formula_is_sufficient": False,
            "occupation_signature_alone_is_a_cancellation_group": False,
        },
        "nonidentifiability_control": nonidentifiability_control(),
        "release_test": {
            "k177_representation_class_preserved": True,
            "complete_structural_skeleton_compiled": True,
            "coefficient_complete_integral_family_serialized": False,
            "outward_numerical_prefix_integrals_evaluated": False,
            "coefficient_complete_base_action_column_evaluated": False,
            "complete_R_ref_form_dual_residual_serialized": False,
            "positive_complete_M_orthogonal_complement_or_flux_floor_serialized": False,
            "scalar_center_left_floor_serialized": False,
            "native_K152_interval_emitted": False,
        },
        "next_exact_input": {
            "owner": "K156 matched finite-cutoff normal ordering",
            "deliverable": "one coefficient-complete term record per surviving exchange contribution",
            "must_precede": "determinant-aware outward quadrature",
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
