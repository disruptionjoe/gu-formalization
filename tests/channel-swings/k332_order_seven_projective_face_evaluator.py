#!/usr/bin/env python3
"""Finite normalized complete-determinant bounds on both projective faces.

K331 supplies the legal projective preconditioners.  This module applies them
to shared entry jets before the complete bordered determinant Taylor
polynomial is assembled.  The lower face scales the final row of both D4 and
B5 by ``s``.  The upper face scales the singular border-column jet of order k
by ``(1-s)^(3+k)``; coefficient order j may discard the remaining factor
``(1-s)^(j-k)<=1``.  K328 supplies every zero-safe derivative bound.
"""

from __future__ import annotations

import argparse
import importlib.util
import json
import math
from fractions import Fraction
from pathlib import Path
from typing import Any

from flint import arb, ctx


ROOT = Path(__file__).resolve().parents[2]
HERE = Path(__file__).resolve().parent
K312_MODULE = HERE / "k312_order_seven_positive_cell_measure_backend.py"
K314_MODULE = HERE / "k314_order_seven_projective_face_oracle.py"
K326_MODULE = HERE / "k326_order_seven_signed_entry_jet_chart_bank.py"
K328_MODULE = HERE / "k328_order_seven_scaled_derivative_envelope_bank.py"
K331 = ROOT / "lab/process/k331-order-seven-projective-face-homogeneity.json"
OUTPUT = ROOT / "lab/process/k332-order-seven-projective-face-evaluator.json"

ctx.dps = 180
ctx.threads = 1

RADIUS = Fraction(1, 16)
GAPS = [(Fraction(1, 8), Fraction(5, 24)) for _ in range(6)]
ROW_ORDERS = [0, 1, 2, 0]
COLUMN_ORDERS = [0, 1, 2, 0]
ARGUMENT_MAX = Fraction(3, 2)


def load_module(path: Path, name: str):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {path}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def q(value: Fraction) -> str:
    return str(value.numerator) if value.denominator == 1 else f"{value.numerator}/{value.denominator}"


def symmetric(value: arb) -> arb:
    return arb(0, abs(value).upper())


def upper_text(value: arb) -> str:
    return repr(math.nextafter(float(abs(value).upper()), math.inf))


def scaled_dd_upper(k328, radius: Fraction, lower: Fraction, row: int, column: int, y_order: int = 0) -> arb:
    if lower <= 0:
        raise AssertionError("positive normalized argument lower required")
    order = row + column + y_order
    phi = k328.scaled_derivative_upper(order, radius * ARGUMENT_MAX)
    value = phi / (lower ** (order + 1) * math.factorial(row) * math.factorial(column))
    return arb(q(value))


def nodes(face: str) -> tuple[dict[str, list[Fraction]], Fraction, Fraction]:
    p0 = min(interval[0] for interval in GAPS)
    if face == "s0":
        s0, s1 = Fraction(0), Fraction(1, 4)
        b0, b1 = Fraction(3, 4), Fraction(1)
    elif face == "s1":
        s0, s1 = Fraction(3, 4), Fraction(1)
        b0, b1 = Fraction(0), Fraction(1, 4)
    else:
        raise AssertionError("unknown face")
    lower = {
        "odd_left": [b0 * p0 * count for count in (3, 2, 1, 0)],
        "odd_right": [s0 / 2 + b0 * p0 * count for count in (3, 2, 1, 0)],
        "even_left": [b0 * p0 * value for value in (Fraction(9, 4), Fraction(5, 4), Fraction(1, 4), Fraction(0))],
        "even_right": [s0 / 2 + b0 * p0 * value for value in (Fraction(9, 4), Fraction(5, 4), Fraction(1, 4), Fraction(0))],
    }
    return lower, s1, b1


def d4_bound(k328, radius: Fraction, face: str) -> tuple[arb, dict[str, Any]]:
    bank, s_max, _ = nodes(face)
    matrix: list[list[arb]] = []
    special = 0
    for row in range(4):
        entries = []
        for column in range(4):
            lower = bank["odd_left"][row] + bank["odd_right"][column]
            if face == "s0" and (row, column) == (3, 3):
                # H=s/2, hence s*r*f(r*H)=2*Phi_0(r*H).
                value = arb(q(2 * k328.scaled_derivative_upper(0, radius * ARGUMENT_MAX)))
                special += 1
            else:
                value = scaled_dd_upper(k328, radius, lower, row, column)
                if face == "s0" and row == 3:
                    value *= arb(q(s_max))
            entries.append(value)
        matrix.append(entries)
    bound = arb(1)
    for row in matrix:
        bound *= sum((value * value for value in row), arb(0)).sqrt()
    return bound, {
        "preconditioned_row": 3 if face == "s0" else None,
        "zero_safe_special_slots": special,
        "minimum_positive_argument": q(min(
            bank["odd_left"][row] + bank["odd_right"][column]
            for row in range(4) for column in range(4)
            if not (face == "s0" and (row, column) == (3, 3))
        )),
    }


def upper_face_border_jets(k328, radius: Fraction, row: int) -> list[arb]:
    """Return t^(3+k) times border-column jet k, k=0,1,2."""
    p0 = min(interval[0] for interval in GAPS)
    h = p0 * (Fraction(9, 4), Fraction(5, 4), Fraction(1, 4))[row]
    a = ROW_ORDERS[row]
    tmax = Fraction(1, 4)
    xmax = Fraction(1)
    yhalf = Fraction(1, 2)

    def derivative(order: int) -> arb:
        phi = k328.scaled_derivative_upper(order, radius * ARGUMENT_MAX)
        return arb(q(phi / (h ** (order + 1) * math.factorial(a))))

    f0, f1, f2 = derivative(a), derivative(a + 1), derivative(a + 2)
    value = arb(q(tmax ** (2 - a) * yhalf)) * f0
    first = arb(q(tmax ** (3 - a))) * f0 + arb(q(tmax ** (2 - a) * yhalf * xmax * (a + 1))) * f1
    second = (
        arb(q(tmax ** (3 - a) * 2 * xmax * (a + 1))) * f1
        + arb(q(tmax ** (2 - a) * yhalf * xmax * xmax * (a + 1) * (a + 2))) * f2
    )
    return [symmetric(value), symmetric(first), symmetric(second)]


def b5_jets(k326, k328, radius: Fraction, face: str) -> tuple[list[arb], dict[str, Any]]:
    bank, s_max, _ = nodes(face)
    jets = [[[arb(0), arb(0), arb(0)] for _ in range(5)] for _ in range(5)]
    terminal = [arb(q(radius)) * value for value in k326.terminal_jet_uppers((Fraction(0), radius * s_max))]
    minimum_positive: list[Fraction] = []

    for row in range(4):
        for column in range(4):
            if (row, column) == (3, 3):
                values = [symmetric(value) for value in terminal]
            else:
                lower = bank["even_left"][row] + bank["even_right"][column]
                minimum_positive.append(lower)
                a, c = ROW_ORDERS[row], COLUMN_ORDERS[column]
                delta = Fraction(0) if row < 3 and column < 3 else s_max
                values = [
                    symmetric(scaled_dd_upper(k328, radius, lower, a, c)),
                    symmetric(arb(q(delta)) * scaled_dd_upper(k328, radius, lower, a, c, 1)) if delta else arb(0),
                    symmetric(arb(q(delta * delta)) * scaled_dd_upper(k328, radius, lower, a, c, 2)) if delta else arb(0),
                ]
            if face == "s0" and row == 3:
                values = [arb(q(s_max)) * value for value in values]
            jets[row][column] = values

    yhalf = Fraction(1, 2)
    for row in range(3):
        a = ROW_ORDERS[row]
        if face == "s1":
            jets[row][4] = upper_face_border_jets(k328, radius, row)
        else:
            lower = bank["even_left"][row]
            minimum_positive.append(lower)
            f0 = scaled_dd_upper(k328, radius, lower, a, 0)
            f1 = scaled_dd_upper(k328, radius, lower, a + 1, 0)
            f2 = scaled_dd_upper(k328, radius, lower, a + 2, 0)
            jets[row][4] = [
                symmetric(arb(q(yhalf)) * f0),
                symmetric(f0 + arb(q(yhalf * s_max * (a + 1))) * f1),
                symmetric(arb(q(2 * s_max * (a + 1))) * f1 + arb(q(yhalf * s_max * s_max * (a + 1) * (a + 2))) * f2),
            ]

    for column in range(3):
        c = COLUMN_ORDERS[column]
        lower = bank["even_right"][column]
        minimum_positive.append(lower)
        f0 = scaled_dd_upper(k328, radius, lower, 0, c)
        f1 = scaled_dd_upper(k328, radius, lower, 0, c + 1)
        f2 = scaled_dd_upper(k328, radius, lower, 0, c + 2)
        jets[4][column] = [
            symmetric(f0),
            symmetric(f0 + arb(q(s_max * (c + 1))) * f1),
            symmetric(arb(q(2 * s_max * (c + 1))) * f1 + arb(q(s_max * s_max * (c + 1) * (c + 2))) * f2),
        ]

    determinant = k326.determinant_taylor(jets)
    return determinant, {
        "minimum_positive_nonterminal_argument": q(min(minimum_positive)),
        "literal_zero_slots": [[3, 4], [4, 3], [4, 4]],
        "terminal_zero_safe": True,
        "preconditioner": "s times final row" if face == "s0" else "t^(3+k) on border-column jet order k",
        "shared_entry_substitution_precedes_complete_determinant_enclosure": True,
    }


def face_bank(radius: Fraction = RADIUS) -> dict[str, Any]:
    k312 = load_module(K312_MODULE, "k332_k312_backend")
    k314 = load_module(K314_MODULE, "k332_k314_backend")
    k326 = load_module(K326_MODULE, "k332_k326_backend")
    k328 = load_module(K328_MODULE, "k332_k328_backend")
    projective = k314.projective_polynomial_upper(
        {name: interval for name, interval in zip(k314.GAPS, GAPS, strict=True)}
    )
    gap_volume = math.prod((right - left for left, right in GAPS), start=Fraction(1))
    radial_mass = k312.radial_finite_upper(Fraction(0), radius, 6)
    faces = []
    for face, interval, reduced_powers in (
        ("s0", (Fraction(0), Fraction(1, 4)), [1, 1, 1]),
        ("s1", (Fraction(3, 4), Fraction(1)), [26, 25, 24]),
    ):
        d4, d4_audit = d4_bound(k328, radius, face)
        b5, b5_audit = b5_jets(k326, k328, radius, face)
        s_max = interval[1]
        scalar = Fraction(4, 120) * radius * radius * s_max * s_max * Fraction(1, 16) * projective
        normalized = [arb(16) * d4 * value * arb(q(scalar)) for value in b5]
        projective_masses = [
            k312.polynomial_cell_moment(interval[0], interval[1], power, 29 if face == "s0" else 0)
            if face == "s0"
            else k312.polynomial_cell_moment(interval[0], interval[1], 3, power)
            for power in reduced_powers
        ]
        integrated = [
            value * arb(q(radial_mass * projective_masses[order] * gap_volume))
            for order, value in enumerate(normalized)
        ]
        if any(not math.isfinite(float(value.upper())) or value.upper() <= 0 for value in integrated):
            raise AssertionError(f"{face} integrated bank is not finite positive")
        faces.append({
            "face": face,
            "projective_interval": [q(value) for value in interval],
            "preconditioned_D4_abs_upper": upper_text(d4),
            "preconditioned_bordered_B5_value_first_second_intervals": [str(value) for value in b5],
            "sixteen_chart_preconditioned_value_first_second_abs_uppers": [upper_text(value) for value in normalized],
            "reduced_projective_powers": reduced_powers,
            "reduced_projective_masses": [q(value) for value in projective_masses],
            "origin_integrated_value_first_second_abs_uppers": [upper_text(value) for value in integrated],
            "D4_audit": d4_audit,
            "B5_audit": b5_audit,
        })
    return {
        "radius_upper": q(radius),
        "radial_mass_upper": q(radial_mass),
        "native_projective_polynomial_upper": q(projective),
        "six_gap_exact_volume": q(gap_volume),
        "faces": faces,
    }


def build() -> dict[str, Any]:
    k331 = json.loads(K331.read_text())
    if not k331["decision"]["normalized_confluent_face_evaluator_released"]:
        raise AssertionError("K331 did not release the face evaluator")
    bank = face_bank()
    return {
        "schema_version": "1.0",
        "result_id": "K332-ORDER-SEVEN-PROJECTIVE-FACE-EVALUATOR",
        "created": "2026-09-22",
        "classification": "INTERNAL_STRUCTURAL_ONLY",
        "direction": "observed_to_native",
        "fixed_control": {
            "predecessor_manifests": [
                "lab/process/k328-order-seven-scaled-derivative-envelope-bank.json",
                "lab/process/k331-order-seven-projective-face-homogeneity.json",
            ],
            "arb_decimal_digits": 180,
            "threads": 1,
            "radial_cell": ["0", q(RADIUS)],
            "endpoint_chart_count": 16,
            "coefficient_orders": [0, 1, 2],
        },
        "projective_face_bank": bank,
        "composition_contract": {
            "projective_preconditioners_applied_before_interval_substitution": True,
            "shared_entry_substitution_precedes_complete_determinant_enclosure": True,
            "familywise_absolute_summation_used": False,
            "permutationwise_absolute_summation_used_for_B5": False,
            "raw_Bessel_evaluation_at_zero_used": False,
            "projective_cutoff_used": False,
        },
        "decision": {
            "both_projective_origin_face_cells_bounded": True,
            "radius_one_face_reference_released": True,
            "face_annulus_and_tail_complete": False,
            "recursive_tolerance_complete": False,
            "complete_y_master_constant_emitted": False,
            "next_exact_input": "evaluate the same preconditioned face bank at radius one, combine a finite [1/16,1] annulus with K330's degree ledger and exact incomplete-gamma tails, then test recursive global subdivision",
        },
        "release_test": {
            "both_faces_present": [row["face"] for row in bank["faces"]] == ["s0", "s1"],
            "all_six_integrated_coefficients_finite_positive": all(
                math.isfinite(float(value)) and float(value) > 0
                for row in bank["faces"] for value in row["origin_integrated_value_first_second_abs_uppers"]
            ),
            "literal_border_zeros_retained": all(row["B5_audit"]["literal_zero_slots"] == [[3, 4], [4, 3], [4, 4]] for row in bank["faces"]),
            "complete_numerical_norm_overclaim": False,
            "native_K152_interval_emitted": False,
        },
        "ledger_effect": k331["ledger_effect"],
        "source_routing": k331["source_routing"],
        "claim_ceiling": "Finite post-assembly complete-determinant value/first/second bounds on the radial-origin cells over both projective faces. K331's s-row and (1-s)-border preconditioners are applied to shared entry jets before one bordered determinant Taylor enclosure; K328 supplies zero-safe derivative bounds and the reduced native projective powers are integrated exactly. This covers r in [0,1/16] on s in [0,1/4] and [3/4,1], all six positive gap cells and all sixteen endpoint charts. The face annulus, face tail, recursive tolerance, complete y constant, gap transfer, K294 join, action-column value, residual, K152 interval, source/ledger, canon, paper, public and physical claims remain open.",
    }


def validate_payload(payload: dict[str, Any]) -> None:
    fixed = payload["fixed_control"]
    if fixed["radial_cell"] != ["0", "1/16"] or fixed["endpoint_chart_count"] != 16:
        raise AssertionError("face origin domain changed")
    faces = payload["projective_face_bank"]["faces"]
    if [row["face"] for row in faces] != ["s0", "s1"]:
        raise AssertionError("face coverage changed")
    if faces[0]["reduced_projective_powers"] != [1, 1, 1] or faces[1]["reduced_projective_powers"] != [26, 25, 24]:
        raise AssertionError("K331 face powers changed")
    contract = payload["composition_contract"]
    if contract["raw_Bessel_evaluation_at_zero_used"] or contract["projective_cutoff_used"]:
        raise AssertionError("forbidden boundary workaround used")
    if contract["familywise_absolute_summation_used"] or contract["permutationwise_absolute_summation_used_for_B5"]:
        raise AssertionError("early complete-determinant absolute summation used")
    if not payload["decision"]["both_projective_origin_face_cells_bounded"]:
        raise AssertionError("face bank not released")
    if payload["decision"]["complete_y_master_constant_emitted"]:
        raise AssertionError("complete numerical release overclaimed")


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
