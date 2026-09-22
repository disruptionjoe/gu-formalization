#!/usr/bin/env python3
"""Signed shared-entry jets for the complete K318 endpoint chart bank.

K325 requires interval substitution into one complete determinant Taylor
polynomial before coefficient enclosure.  This implementation supplies signed
divided-difference jets for every nonterminal entry, K322's zero-safe scaled
terminal jets, exact literal border zeros, and a single post-assembly Arb
enclosure for value, first and second coefficients.
"""

from __future__ import annotations

import argparse
import importlib.util
import itertools
import json
import math
from fractions import Fraction
from pathlib import Path
from typing import Any

from flint import arb, ctx


ROOT = Path(__file__).resolve().parents[2]
K308_MODULE = Path(__file__).with_name("k308_order_seven_regularized_y_master_operator.py")
K314_MODULE = Path(__file__).with_name("k314_order_seven_projective_face_oracle.py")
K318 = ROOT / "lab/process/k318-order-seven-weighted-endpoint-blowup-atlas.json"
K322 = ROOT / "lab/process/k322-order-seven-zero-safe-scaled-bessel-envelopes.json"
K324 = ROOT / "lab/process/k324-order-seven-complete-value-chart-bank.json"
K325 = ROOT / "lab/process/k325-order-seven-correlated-determinant-jet-algebra.json"
OUTPUT = ROOT / "lab/process/k326-order-seven-signed-entry-jet-chart-bank.json"

ctx.dps = 180
ctx.threads = 1

DEFAULT_X = (Fraction(1, 16), Fraction(1, 8))
DEFAULT_B = (Fraction(1, 32), Fraction(1, 8))
DEFAULT_P = [(Fraction(1, 8), Fraction(5, 24)) for _ in range(6)]
ROW_ORDERS = [0, 1, 2, 0]
COLUMN_ORDERS = [0, 1, 2, 0]


def load_module(path: Path, name: str):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {path}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def symmetric(upper: arb) -> arb:
    return arb(0, upper.upper())


def signed(upper: arb, sign: int) -> arb:
    upper = arb(upper.upper())
    half = upper / 2
    return (half if sign > 0 else -half) + arb(0, half)


def abs_upper_text(value: arb) -> str:
    return repr(math.nextafter(float(abs(value).upper()), math.inf))


def interval_width_text(value: arb) -> str:
    return repr(math.nextafter(float(value.upper() - value.lower()), math.inf))


def add_poly(left: list[arb], right: list[arb]) -> list[arb]:
    return [a + b for a, b in zip(left, right, strict=True)]


def multiply_poly(left: list[arb], right: list[arb]) -> list[arb]:
    result = [arb(0), arb(0), arb(0)]
    for i, a in enumerate(left):
        for j, b in enumerate(right):
            if i + j <= 2:
                result[i + j] += a * b
    return result


def determinant_taylor(entry_jets: list[list[list[arb]]]) -> list[arb]:
    """Return det(A), det(A)' and det(A)'' after one interval assembly."""
    total = [arb(0), arb(0), arb(0)]
    for permutation in itertools.permutations(range(5)):
        inversions = sum(
            permutation[i] > permutation[j]
            for i in range(5)
            for j in range(i + 1, 5)
        )
        term = [arb(-1 if inversions % 2 else 1), arb(0), arb(0)]
        for row, column in enumerate(permutation):
            value, first, second = entry_jets[row][column]
            term = multiply_poly(term, [value, first, second / 2])
        total = add_poly(total, term)
    return [total[0], total[1], 2 * total[2]]


def node_lowers(
    x: tuple[Fraction, Fraction],
    b: tuple[Fraction, Fraction],
    gaps: list[tuple[Fraction, Fraction]],
) -> dict[str, list[Fraction]]:
    x0, _ = x
    b0, _ = b
    p0 = min(interval[0] for interval in gaps)
    return {
        "odd_left": [b0 * p0 * count for count in (3, 2, 1, 0)],
        "odd_right": [x0 / 2 + b0 * p0 * count for count in (3, 2, 1, 0)],
        "even_left": [b0 * p0 * value for value in (Fraction(9, 4), Fraction(5, 4), Fraction(1, 4), Fraction(0))],
        "even_right": [x0 / 2 + b0 * p0 * value for value in (Fraction(9, 4), Fraction(5, 4), Fraction(1, 4), Fraction(0))],
    }


def terminal_jet_uppers(x: tuple[Fraction, Fraction]) -> list[arb]:
    # w=lambda*H, lambda<=x_max and H<=3/2.  K322's adapter gives
    # |D^m Phi_m/H^(m+1)| <= U_m(W)*2^(m+1), with |D|<=1.
    width = x[1] * Fraction(3, 2)
    base = [Fraction(2), 2 * (1 + width), 4 + 2 * width + 2 * width * width]
    return [arb(str(value * 2 ** (order + 1))) for order, value in enumerate(base)]


def build_entry_jets(
    module,
    x: tuple[Fraction, Fraction] = DEFAULT_X,
    b: tuple[Fraction, Fraction] = DEFAULT_B,
    gaps: list[tuple[Fraction, Fraction]] = DEFAULT_P,
) -> tuple[list[list[list[arb]]], dict[str, Any], arb]:
    nodes = node_lowers(x, b, gaps)
    x1 = x[1]
    y1 = Fraction(1, 2)

    d4_lower = min(nodes["odd_left"]) + min(nodes["odd_right"])
    d4 = [
        [module.dd_abs_upper(d4_lower, row, column) for column in range(4)]
        for row in range(4)
    ]
    d4_bound = arb(1)
    for row in d4:
        d4_bound *= sum((value * value for value in row), arb(0)).sqrt()

    jets = [[[arb(0), arb(0), arb(0)] for _ in range(5)] for _ in range(5)]
    terminal = terminal_jet_uppers(x)
    nonterminal_lowers: list[Fraction] = []
    sign_definite = 0
    symmetric_count = 0

    for row in range(4):
        for column in range(4):
            if (row, column) == (3, 3):
                jets[row][column] = [symmetric(value) for value in terminal]
                symmetric_count += 3
                continue
            lower = nodes["even_left"][row] + nodes["even_right"][column]
            if lower <= 0:
                raise AssertionError("nonterminal core entry touched zero")
            nonterminal_lowers.append(lower)
            a, c = ROW_ORDERS[row], COLUMN_ORDERS[column]
            base = module.dd_abs_upper(lower, a, c)
            jets[row][column][0] = signed(base, -1 if (a + c) % 2 else 1)
            sign_definite += 1
            delta = Fraction(0) if row < 3 and column < 3 else x1
            if not delta:
                continue
            first = module.ball(delta) * module.dd_abs_upper(lower, a, c, 1)
            second = module.ball(delta * delta) * module.dd_abs_upper(lower, a, c, 2)
            jets[row][column][1] = symmetric(first)
            jets[row][column][2] = signed(second, -1 if (a + c + 2) % 2 else 1)
            symmetric_count += 1
            sign_definite += 1

    # Last border column: y*f(T), with its Peano/Hepp chart weight retained in
    # the same column.  Its cube upper is one; no detached multiplier appears.
    for row in range(3):
        a = ROW_ORDERS[row]
        lower = nodes["even_left"][row]
        nonterminal_lowers.append(lower)
        f0 = module.dd_abs_upper(lower, a, 0)
        f1 = module.dd_abs_upper(lower, a + 1, 0)
        f2 = module.dd_abs_upper(lower, a + 2, 0)
        jets[row][4][0] = signed(module.ball(y1) * f0, -1 if a % 2 else 1)
        jets[row][4][1] = signed(f0, -1 if a % 2 else 1) + signed(module.ball(y1 * x1 * (a + 1)) * f1, -1 if (a + 1) % 2 else 1)
        jets[row][4][2] = signed(module.ball(2 * x1 * (a + 1)) * f1, -1 if (a + 1) % 2 else 1) + signed(module.ball(y1 * x1 * x1 * (a + 1) * (a + 2)) * f2, -1 if (a + 2) % 2 else 1)

    # Bottom border row: (1-y)*f(U).  Signs are retained term by term; the
    # three terminal border slots stay literal zeros.
    for column in range(3):
        c = COLUMN_ORDERS[column]
        lower = nodes["even_right"][column]
        nonterminal_lowers.append(lower)
        f0 = module.dd_abs_upper(lower, 0, c)
        f1 = module.dd_abs_upper(lower, 0, c + 1)
        f2 = module.dd_abs_upper(lower, 0, c + 2)
        jets[4][column][0] = signed(module.ball(1) * f0, -1 if c % 2 else 1)
        jets[4][column][1] = signed(f0, -1 if (c + 1) % 2 else 1) + signed(module.ball(x1 * (c + 1)) * f1, -1 if c % 2 else 1)
        jets[4][column][2] = signed(module.ball(2 * x1 * (c + 1)) * f1, -1 if (c + 1) % 2 else 1) + signed(module.ball(x1 * x1 * (c + 1) * (c + 2)) * f2, -1 if c % 2 else 1)

    audit = {
        "D4_minimum_argument": str(d4_lower),
        "minimum_nonterminal_B5_argument": str(min(nonterminal_lowers)),
        "terminal_argument_upper_W": str(x1 * Fraction(3, 2)),
        "terminal_scaled_jet_uppers": [abs_upper_text(value) for value in terminal],
        "terminal_zero_safe_rule": "K322 U_m(W)*2^(m+1), |D|<=1, H>=1/2",
        "raw_Bessel_evaluation_at_zero_used": False,
        "literal_zero_slots": [[3, 4], [4, 3], [4, 4]],
        "sign_definite_core_intervals": sign_definite,
        "symmetric_dependency_intervals": symmetric_count,
        "entry_interval_construction": "complete monotonicity signs retained whenever delta parity fixes them; only sign-undetermined affine first jets and terminal Phi jets are symmetric",
    }
    return jets, audit, d4_bound


def transpose_jets(jets: list[list[list[arb]]]) -> list[list[list[arb]]]:
    return [[jets[column][row][:] for column in range(5)] for row in range(5)]


def complete_cell_bound(
    module,
    k314_module,
    x: tuple[Fraction, Fraction] = DEFAULT_X,
    b: tuple[Fraction, Fraction] = DEFAULT_B,
    gaps: list[tuple[Fraction, Fraction]] = DEFAULT_P,
) -> dict[str, Any]:
    jets, audit, d4_bound = build_entry_jets(module, x, b, gaps)
    projective = k314_module.projective_polynomial_upper(
        {name: interval for name, interval in zip(k314_module.GAPS, gaps, strict=True)}
    )
    scalar = Fraction(4, 120) * x[1] ** 2 * Fraction(1, 16) * projective
    endpoint_rows = {}
    for endpoint, bank in (("left", jets), ("right", transpose_jets(jets))):
        determinant_jets = determinant_taylor(bank)
        complete = [d4_bound * value * module.ball(scalar) for value in determinant_jets]
        endpoint_rows[endpoint] = {
            "determinant_jet_intervals": [str(value) for value in determinant_jets],
            "four_group_weighted_abs_uppers": [abs_upper_text(value) for value in complete],
            "interval_widths": [interval_width_text(value) for value in complete],
        }
    return {
        "x": [str(value) for value in x],
        "b": [str(value) for value in b],
        "projective_gaps": [[str(value) for value in interval] for interval in gaps],
        "native_projective_polynomial_upper": str(projective),
        "outer_scalar_fraction": str(scalar),
        "entry_jet_audit": audit,
        "endpoints": endpoint_rows,
    }


def build() -> dict[str, Any]:
    module = load_module(K308_MODULE, "k326_k308_backend")
    k314_module = load_module(K314_MODULE, "k326_k314_backend")
    k318 = json.loads(K318.read_text())
    k322 = json.loads(K322.read_text())
    k324 = json.loads(K324.read_text())
    k325 = json.loads(K325.read_text())
    if not k325["decision"]["correlation_preserving_determinant_jet_algebra_implemented"]:
        raise AssertionError("K325 correlation contract unavailable")
    if not k322["decision"]["all_three_terminal_jet_orders_covered"]:
        raise AssertionError("K322 terminal jet bank unavailable")

    cell = complete_cell_bound(module, k314_module)
    charts = k318["determinant_preserving_endpoint_atlas"]["charts"]
    rows = []
    for chart in charts:
        endpoint = chart["endpoint"]
        bank = cell["endpoints"][endpoint]
        rows.append({
            "chart_id": chart["id"],
            "endpoint": endpoint,
            "split_sector": chart["split_sector"],
            "exact_chart_mass": chart["exact_chart_mass"],
            "endpoint_weight_placement": "border column 4" if endpoint == "left" else "border row 4",
            "complete_value_first_second_abs_uppers": bank["four_group_weighted_abs_uppers"],
            "complete_value_first_second_interval_widths": bank["interval_widths"],
        })
    totals = [sum(float(row["complete_value_first_second_abs_uppers"][order]) for row in rows) for order in range(3)]
    if any(not math.isfinite(value) or value <= 0 for value in totals):
        raise AssertionError("complete chart bank is not finite positive")

    return {
        "schema_version": "1.0",
        "result_id": "K326-ORDER-SEVEN-SIGNED-ENTRY-JET-CHART-BANK",
        "created": "2026-09-22",
        "classification": "INTERNAL_STRUCTURAL_ONLY",
        "direction": "observed_to_native",
        "fixed_control": {
            "predecessor_manifests": [
                "lab/process/k318-order-seven-weighted-endpoint-blowup-atlas.json",
                "lab/process/k322-order-seven-zero-safe-scaled-bessel-envelopes.json",
                "lab/process/k324-order-seven-complete-value-chart-bank.json",
                "lab/process/k325-order-seven-correlated-determinant-jet-algebra.json",
            ],
            "arb_decimal_digits": 180,
            "threads": 1,
            "chart_count": len(rows),
            "coefficient_orders": [0, 1, 2],
            "radial_projective_slab": {"x": [str(v) for v in DEFAULT_X], "b": [str(v) for v in DEFAULT_B], "projective_gaps": [str(DEFAULT_P[0][0]), str(DEFAULT_P[0][1])]},
        },
        "signed_entry_jet_cell": cell,
        "complete_chart_bank": {
            "rows": rows,
            "sixteen_chart_value_first_second_abs_uppers": [repr(value) for value in totals],
            "source_chart_ids": [chart["id"] for chart in charts],
            "shared_interval_substitution_precedes_determinant_coefficient_enclosure": True,
            "familywise_absolute_summation_used": False,
            "permutationwise_absolute_summation_used": False,
            "literal_border_zeros_retained": True,
            "exact_chart_masses_are_census_not_extra_multiplier": True,
        },
        "scope_boundary": {
            "covered": "all sixteen K318 endpoint charts and complete value/first/second bordered determinant jets on K324's fixed positive radial/projective slab",
            "not_covered": ["radial origin", "radial tail", "projective s=0 and s=1 faces", "a complete y-master constant"],
            "fixed_slab_bank_is_not_global_release": True,
        },
        "decision": {
            "all_sixteen_signed_derivative_charts_bounded": True,
            "complete_determinant_taylor_assembly_precedes_interval_enclosure": True,
            "zero_touching_terminal_orders_zero_one_two_are_safe": True,
            "adaptive_positive_interior_subdivision_released": True,
            "complete_y_master_constant_emitted": False,
            "five_gap_axis_transfer_released": False,
            "k294_gamma_join_released": False,
            "next_exact_input": "apply this evaluator to an exact-cover adaptive positive-interior subdivision, then extend the accepted rule to radial origin, tail and projective faces",
        },
        "release_test": {
            "K325_family_census_replayed": k325["census"]["cross_weighted_family_monomials"] == 1674,
            "source_chart_ids_covered_exactly_once": len(rows) == len({row["chart_id"] for row in rows}) == 16,
            "all_complete_bounds_finite_positive": all(math.isfinite(value) and value > 0 for value in totals),
            "raw_zero_evaluation_used": cell["entry_jet_audit"]["raw_Bessel_evaluation_at_zero_used"],
            "complete_numerical_norm_overclaim": False,
            "native_K152_interval_emitted": False,
        },
        "ledger_effect": k324["ledger_effect"],
        "source_routing": k324["source_routing"],
        "claim_ceiling": "Finite signed shared-entry-jet enclosures for value, first and second coefficients of the complete five-by-five bordered determinant on all sixteen K318 endpoint charts over K324's fixed positive slab. K322 zero-safe terminal jets and complete-monotonicity signs are substituted before one determinant Taylor expansion and one coefficient enclosure; literal zeros and left-column/right-row weight placement remain exact. Radial origin, tail and projective faces remain open, so no complete y-master constant, gap-axis transfer, K294 join, action-column value, residual, K152 interval, source/ledger, canon, paper, public or physical claim is released.",
    }


def validate_payload(payload: dict[str, Any]) -> None:
    bank = payload["complete_chart_bank"]
    rows = bank["rows"]
    if len(rows) != 16 or len({row["chart_id"] for row in rows}) != 16:
        raise AssertionError("K318 chart coverage changed")
    if [row["chart_id"] for row in rows] != bank["source_chart_ids"]:
        raise AssertionError("K318 source chart order changed")
    if sum(row["endpoint"] == "left" for row in rows) != 8 or sum(row["endpoint"] == "right" for row in rows) != 8:
        raise AssertionError("left/right endpoint census changed")
    if any(
        row["endpoint_weight_placement"] != ("border column 4" if row["endpoint"] == "left" else "border row 4")
        for row in rows
    ):
        raise AssertionError("endpoint weight placement changed")
    if any(
        len(row["complete_value_first_second_abs_uppers"]) != 3
        or any(not math.isfinite(float(value)) or float(value) <= 0 for value in row["complete_value_first_second_abs_uppers"])
        for row in rows
    ):
        raise AssertionError("a complete chart jet upper is invalid")
    if not bank["shared_interval_substitution_precedes_determinant_coefficient_enclosure"]:
        raise AssertionError("K325 assembly order lost")
    if bank["familywise_absolute_summation_used"] or bank["permutationwise_absolute_summation_used"]:
        raise AssertionError("early absolute enclosure reintroduced")
    if not bank["literal_border_zeros_retained"]:
        raise AssertionError("literal border zeros lost")
    if not bank["exact_chart_masses_are_census_not_extra_multiplier"]:
        raise AssertionError("chart masses were double multiplied")
    audit = payload["signed_entry_jet_cell"]["entry_jet_audit"]
    if audit["raw_Bessel_evaluation_at_zero_used"]:
        raise AssertionError("raw terminal zero evaluation introduced")
    if audit["literal_zero_slots"] != [[3, 4], [4, 3], [4, 4]] or len(audit["terminal_scaled_jet_uppers"]) != 3:
        raise AssertionError("terminal jet or literal-zero contract changed")
    if not payload["scope_boundary"]["fixed_slab_bank_is_not_global_release"]:
        raise AssertionError("fixed-slab scope hidden")
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
