#!/usr/bin/env python3
"""Build an outward regularized operator for the K307 order-seven y master.

The operator extracts the full odd-node Vandermondes from D4 and the
first-three even-node Vandermondes from the coherent bordered B5.  The
remaining matrices are evaluated through mixed divided differences.  On a
positive two-radius cell, complete monotonicity of 2*K1 gives rigorous Arb
upper bounds for values and the first two y derivatives of every transformed
entry.  Determinant jets are then bounded by the complete column-replacement
formula used by K305.
"""

from __future__ import annotations

import argparse
import itertools
import json
import math
from fractions import Fraction
from pathlib import Path
from typing import Any

from flint import arb, ctx


ROOT = Path(__file__).resolve().parents[2]
K302 = ROOT / "lab/process/k302-order-seven-split-weighted-peano-jet.json"
K305 = ROOT / "lab/process/k305-order-seven-coherent-bordered-functional-compiler.json"
K307 = ROOT / "lab/process/k307-order-seven-two-radius-joint-chart.json"
OUTPUT = ROOT / "lab/process/k308-order-seven-regularized-y-master-operator.json"

ctx.dps = 180
ctx.threads = 1


def ball(value: Fraction | int) -> arb:
    if isinstance(value, int):
        return arb(value)
    return arb(f"{value.numerator}/{value.denominator}")


def upper_text(value: arb) -> str:
    numeric = float(value.upper())
    return repr(math.nextafter(numeric, math.inf))


def determinant(matrix: list[list[Any]]):
    total = matrix[0][0] * 0
    for permutation in itertools.permutations(range(len(matrix))):
        inversions = sum(
            permutation[i] > permutation[j]
            for i in range(len(permutation))
            for j in range(i + 1, len(permutation))
        )
        term = matrix[0][0] * 0 + (-1 if inversions % 2 else 1)
        for row, column in enumerate(permutation):
            term *= matrix[row][column]
        total += term
    return total


def positive_vandermonde(nodes: list[Any]):
    total = nodes[0] * 0 + 1
    for left, right in itertools.combinations(nodes, 2):
        total *= left - right
    return total


def row_newton(matrix: list[list[Any]], nodes: list[Any], count: int) -> list[list[Any]]:
    work = [row[:] for row in matrix]
    for order in range(1, count):
        for row in range(count - 1, order - 1, -1):
            divisor = nodes[row] - nodes[row - order]
            work[row] = [
                (entry - previous) / divisor
                for entry, previous in zip(work[row], work[row - 1])
            ]
    return work


def column_newton(matrix: list[list[Any]], nodes: list[Any], count: int) -> list[list[Any]]:
    transposed = [list(column) for column in zip(*matrix)]
    transformed = row_newton(transposed, nodes, count)
    return [list(row) for row in zip(*transformed)]


def f(value: arb) -> arb:
    return 2 * value.bessel_k(1)


def bessel_derivative_abs(argument: arb, order: int) -> arb:
    total = arb(0)
    for index in range(order + 1):
        nu = abs(1 - order + 2 * index)
        total += math.comb(order, index) * argument.bessel_k(nu)
    return arb(2) ** (1 - order) * total


def dd_abs_upper(argument_lower: Fraction, row_order: int, column_order: int, y_order: int = 0) -> arb:
    total_order = row_order + column_order + y_order
    return bessel_derivative_abs(ball(argument_lower), total_order) / (
        math.factorial(row_order) * math.factorial(column_order)
    )


def exact_fraction_determinant(matrix: list[list[Fraction]]) -> Fraction:
    work = [row[:] for row in matrix]
    result = Fraction(1)
    for column in range(len(work)):
        pivot = next((row for row in range(column, len(work)) if work[row][column]), None)
        if pivot is None:
            return Fraction(0)
        if pivot != column:
            work[column], work[pivot] = work[pivot], work[column]
            result = -result
        value = work[column][column]
        result *= value
        work[column] = [entry / value for entry in work[column]]
        for row in range(column + 1, len(work)):
            factor = work[row][column]
            work[row] = [entry - factor * base for entry, base in zip(work[row], work[column])]
    return result


def rational_factorization_control() -> dict[str, Any]:
    left_odd = [Fraction(31, 7), Fraction(23, 7), Fraction(13, 7), Fraction(5, 7)]
    right_odd = [Fraction(37, 11), Fraction(29, 11), Fraction(17, 11), Fraction(7, 11)]
    left_even = [Fraction(41, 13), Fraction(30, 13), Fraction(18, 13), Fraction(6, 13)]
    right_even = [Fraction(43, 17), Fraction(33, 17), Fraction(20, 17), Fraction(8, 17)]
    y = Fraction(2, 5)
    kernel = lambda value: Fraction(2, 1) / value
    d4 = [[kernel(a + b) for b in right_odd] for a in left_odd]
    b5 = [[kernel(a + b) for b in right_even] for a in left_even]
    lvec = [y * kernel(value) for value in left_even[:3]] + [Fraction(0)]
    rvec = [(1 - y) * kernel(value) for value in right_even[:3]] + [Fraction(0)]
    bordered = [row + [lvec[index]] for index, row in enumerate(b5)]
    bordered.append(rvec + [Fraction(0)])
    d4_reg = column_newton(row_newton(d4, left_odd, 4), right_odd, 4)
    b5_reg = column_newton(row_newton(bordered, left_even, 3), right_even, 3)
    d4_direct = exact_fraction_determinant(d4)
    b5_direct = exact_fraction_determinant(bordered)
    d4_factored = positive_vandermonde(left_odd) * positive_vandermonde(right_odd) * exact_fraction_determinant(d4_reg)
    b5_factored = positive_vandermonde(left_even[:3]) * positive_vandermonde(right_even[:3]) * exact_fraction_determinant(b5_reg)
    return {
        "kernel": "2/s exact Cauchy model",
        "D4_factorization_exact": d4_direct == d4_factored,
        "bordered_B5_factorization_exact": b5_direct == b5_factored,
        "joint_factorization_exact": d4_direct * b5_direct == d4_factored * b5_factored,
        "D4_regularized_determinant_nonzero": exact_fraction_determinant(d4_reg) != 0,
        "bordered_B5_regularized_determinant_nonzero": exact_fraction_determinant(b5_reg) != 0,
    }


def arb_factorization_control(scale: Fraction) -> dict[str, Any]:
    left_odd = [scale * Fraction(v, 19) for v in (41, 31, 19, 7)]
    right_odd = [scale * Fraction(v, 23) for v in (43, 32, 18, 8)]
    left_even = [scale * Fraction(v, 29) for v in (47, 35, 21, 9)]
    right_even = [scale * Fraction(v, 31) for v in (49, 37, 22, 10)]
    y = Fraction(3, 8)
    d4 = [[f(ball(a + b)) for b in right_odd] for a in left_odd]
    core = [[f(ball(a + b)) for b in right_even] for a in left_even]
    lvec = [ball(y) * f(ball(value)) for value in left_even[:3]] + [arb(0)]
    rvec = [ball(1 - y) * f(ball(value)) for value in right_even[:3]] + [arb(0)]
    bordered = [row + [lvec[index]] for index, row in enumerate(core)]
    bordered.append(rvec + [arb(0)])
    d4_reg = column_newton(row_newton(d4, [ball(v) for v in left_odd], 4), [ball(v) for v in right_odd], 4)
    b5_reg = column_newton(row_newton(bordered, [ball(v) for v in left_even], 3), [ball(v) for v in right_even], 3)
    d4_difference = determinant(d4) - positive_vandermonde([ball(v) for v in left_odd]) * positive_vandermonde([ball(v) for v in right_odd]) * determinant(d4_reg)
    b5_difference = determinant(bordered) - positive_vandermonde([ball(v) for v in left_even[:3]]) * positive_vandermonde([ball(v) for v in right_even[:3]]) * determinant(b5_reg)
    return {
        "scale": str(scale),
        "D4_difference_contains_zero": d4_difference.contains(0),
        "bordered_B5_difference_contains_zero": b5_difference.contains(0),
        "D4_difference": str(d4_difference),
        "bordered_B5_difference": str(b5_difference),
    }


CELL = {
    "x": (Fraction(1, 16), Fraction(1, 8)),
    "b": (Fraction(1, 32), Fraction(1, 8)),
    "y": (Fraction(1, 4), Fraction(3, 4)),
    "p": (Fraction(1, 8), Fraction(5, 24)),
    "split": (Fraction(1, 4), Fraction(3, 4)),
}


def node_lower_bounds() -> dict[str, list[Fraction]]:
    x0, _ = CELL["x"]
    b0, _ = CELL["b"]
    y0, y1 = CELL["y"]
    p0, _ = CELL["p"]
    _, split1 = CELL["split"]
    return {
        "odd_left": [x0 * y0 + b0 * p0 * count for count in (3, 2, 1, 0)],
        "odd_right": [x0 * (1 - y1) + b0 * p0 * count for count in (3, 2, 1, 0)],
        "even_left": [
            x0 * y0 + b0 * p0 * Fraction(9, 4),
            x0 * y0 + b0 * p0 * Fraction(5, 4),
            x0 * y0 + b0 * p0 * Fraction(1, 4),
            x0 * y0 * (1 - split1),
        ],
        "even_right": [
            x0 * (1 - y1) + b0 * p0 * Fraction(9, 4),
            x0 * (1 - y1) + b0 * p0 * Fraction(5, 4),
            x0 * (1 - y1) + b0 * p0 * Fraction(1, 4),
            x0 * (1 - y1) * (1 - split1),
        ],
    }


def determinant_abs_bound(columns: list[list[arb]]) -> arb:
    size = len(columns)
    total = arb(0)
    for permutation in itertools.permutations(range(size)):
        term = arb(1)
        for row, column in enumerate(permutation):
            term *= columns[column][row]
        total += term
    return total


def determinant_jet_bounds(column_jets: list[list[list[arb]]]) -> list[arb]:
    base_columns = [jets[0] for jets in column_jets]
    value = determinant_abs_bound(base_columns)
    first = arb(0)
    second = arb(0)
    for column in range(len(column_jets)):
        replaced = base_columns[:]
        replaced[column] = column_jets[column][1]
        first += determinant_abs_bound(replaced)
        replaced = base_columns[:]
        replaced[column] = column_jets[column][2]
        second += determinant_abs_bound(replaced)
    for left in range(len(column_jets)):
        for right in range(left + 1, len(column_jets)):
            replaced = base_columns[:]
            replaced[left] = column_jets[left][1]
            replaced[right] = column_jets[right][1]
            second += 2 * determinant_abs_bound(replaced)
    return [value, first, second]


def outward_cell_bank() -> dict[str, Any]:
    nodes = node_lower_bounds()
    x1 = CELL["x"][1]
    y1 = CELL["y"][1]
    split0, split1 = CELL["split"]

    d4_matrix = []
    for row_order in range(4):
        row = []
        for column_order in range(4):
            argument_lower = min(nodes["odd_left"]) + min(nodes["odd_right"])
            row.append(dd_abs_upper(argument_lower, row_order, column_order))
        d4_matrix.append(row)
    d4_columns = [list(column) for column in zip(*d4_matrix)]
    d4_bound = determinant_abs_bound(d4_columns)

    row_orders = [0, 1, 2, 0]
    column_orders = [0, 1, 2, 0]
    column_jets: list[list[list[arb]]] = []
    for column_index in range(5):
        jets = [[arb(0) for _ in range(5)] for _ in range(3)]
        if column_index < 4:
            b = column_orders[column_index]
            for row_index in range(4):
                a = row_orders[row_index]
                argument_lower = nodes["even_left"][row_index] + nodes["even_right"][column_index]
                if row_index < 3 and column_index < 3:
                    delta = Fraction(0)
                elif row_index < 3:
                    delta = x1 * split1
                elif column_index < 3:
                    delta = x1 * split1
                else:
                    delta = x1 * (split1 - split0)
                for order in range(3):
                    jets[order][row_index] = ball(delta) ** order * dd_abs_upper(argument_lower, a, b, order)
            # Bottom bordered row: (1-y)*f(U), transformed in U.
            argument_lower = nodes["even_right"][column_index]
            base = dd_abs_upper(argument_lower, 0, b)
            next1 = dd_abs_upper(argument_lower, 0, b + 1)
            next2 = dd_abs_upper(argument_lower, 0, b + 2)
            jets[0][4] = ball(1 - CELL["y"][0]) * base
            jets[1][4] = base + ball((1 - CELL["y"][0]) * x1 * (b + 1)) * next1
            jets[2][4] = ball(2 * x1 * (b + 1)) * next1 + ball((1 - CELL["y"][0]) * x1**2 * (b + 1) * (b + 2)) * next2
        else:
            # Last bordered column: y*f(T), transformed in T; terminal row is literal zero.
            for row_index in range(3):
                a = row_orders[row_index]
                argument_lower = nodes["even_left"][row_index]
                base = dd_abs_upper(argument_lower, a, 0)
                next1 = dd_abs_upper(argument_lower, a + 1, 0)
                next2 = dd_abs_upper(argument_lower, a + 2, 0)
                jets[0][row_index] = ball(y1) * base
                jets[1][row_index] = base + ball(y1 * x1 * (a + 1)) * next1
                jets[2][row_index] = ball(2 * x1 * (a + 1)) * next1 + ball(y1 * x1**2 * (a + 1) * (a + 2)) * next2
        column_jets.append(jets)
    b5_jets = determinant_jet_bounds(column_jets)
    product = [d4_bound * value for value in b5_jets]
    return {
        "cell": {key: [str(value[0]), str(value[1])] for key, value in CELL.items()},
        "node_argument_lower_bounds": {key: [str(value) for value in values] for key, values in nodes.items()},
        "D4_regularized_abs_upper": upper_text(d4_bound),
        "bordered_B5_regularized_y_jet_abs_upper": [upper_text(value) for value in b5_jets],
        "D4_times_bordered_B5_regularized_y_jet_abs_upper": [upper_text(value) for value in product],
        "column_replacement_counts": {"value": 1, "first": 5, "second_pure": 5, "second_cross": 10},
        "outward_backend": "python-flint Arb at 180 decimal digits; monotone K-Bessel derivative bounds at exact rational argument lowers",
    }


def build() -> dict[str, Any]:
    k302 = json.loads(K302.read_text())
    k305 = json.loads(K305.read_text())
    k307 = json.loads(K307.read_text())
    rational = rational_factorization_control()
    if not all(rational.values()):
        raise AssertionError("exact regularized factorization failed")
    arb_rows = [arb_factorization_control(scale) for scale in (Fraction(1), Fraction(1, 64), Fraction(1, 4096))]
    if not all(row["D4_difference_contains_zero"] and row["bordered_B5_difference_contains_zero"] for row in arb_rows):
        raise AssertionError("Arb regularized replay failed")
    bank = outward_cell_bank()
    if any(float(value) <= 0 or not math.isfinite(float(value)) for value in bank["D4_times_bordered_B5_regularized_y_jet_abs_upper"]):
        raise AssertionError("outward y-master bank is not finite positive")
    return {
        "schema_version": "1.0",
        "result_id": "K308-ORDER-SEVEN-REGULARIZED-Y-MASTER-OPERATOR",
        "created": "2026-09-22",
        "classification": "INTERNAL_STRUCTURAL_ONLY",
        "direction": "observed_to_native",
        "fixed_control": {
            "predecessor_manifests": [
                "lab/process/k302-order-seven-split-weighted-peano-jet.json",
                "lab/process/k305-order-seven-coherent-bordered-functional-compiler.json",
                "lab/process/k307-order-seven-two-radius-joint-chart.json",
            ],
            "arb_decimal_digits": 180,
            "threads": 1,
            "master_axis": "y",
            "maximum_y_derivative_order": 2,
        },
        "regularized_operator": {
            "D4_row_column_orders": [0, 1, 2, 3],
            "bordered_B5_row_column_orders": [0, 1, 2, "terminal_raw"],
            "D4_extracted_factor": "V(T1,T3,T5,T7)*V(U1,U3,U5,U7)",
            "bordered_B5_extracted_factor": "V(T2,T4,T6)*V(U2,U4,U6)",
            "mixed_divided_difference_bound": "abs(f[T_0..T_a;U_0..U_b]) <= abs(f^(a+b)(s_min))/(a!*b!)",
            "kernel_derivative_recurrence": "abs((2*K1)^(m)(s))=2^(1-m)*sum_k binom(m,k) K_|1-m+2k|(s)",
            "y_derivative_commutes_with_regularization": True,
            "reason": "the extracted first-three even-node differences are independent of y, while every remaining y dependence is an affine common shift or terminal affine coefficient",
            "determinant_jet_rule": k305["bordered_determinant_theorem"]["differentiation_rule"],
            "exact_rational_control": rational,
            "arb_scale_controls": arb_rows,
        },
        "outward_positive_cell": bank,
        "terminal_face_adapter": {
            "source": "lab/process/k302-order-seven-split-weighted-peano-jet.json",
            "weighted_terminal_jets": k302["universal_weighted_bounds"],
            "insertion_point": "the transformed bordered-B5 terminal row/column entry inside the complete column-replacement determinant",
            "detached_unregularized_cofactor_forbidden": True,
            "complete_terminal_face_constant_composed": False,
            "remaining_reason": "the positive-cell operator is outward and face-stable in q/projective variables, but the two-radius origin and terminal split must still be covered by a joint weighted cell decomposition rather than one global pointwise argument lower bound",
        },
        "decision": {
            "outward_regularized_y_master_operator_implemented": True,
            "exact_factorization_controls_pass": True,
            "small_scale_arb_controls_pass": True,
            "finite_positive_cell_constants_emitted": True,
            "complete_y_peano_norm_emitted": False,
            "five_gap_axes_released_for_structural_transfer_audit": True,
            "k294_gamma_join_released": False,
            "next_exact_input": "transfer the same divided-difference operator to the five affine Duffy axes, then construct the joint two-radius/terminal boundary cell decomposition needed for complete finite constants",
        },
        "release_test": {
            "D4_exactly_regularized": rational["D4_factorization_exact"],
            "bordered_B5_exactly_regularized": rational["bordered_B5_factorization_exact"],
            "three_small_scale_arb_replays": len(arb_rows) == 3,
            "complete_column_replacement_formula_used": True,
            "pointwise_K290_bank_reused": False,
            "complete_numerical_norm_overclaim": False,
            "radial_gamma_join_emitted": False,
            "native_K152_interval_emitted": False,
        },
        "ledger_effect": k307["ledger_effect"],
        "claim_ceiling": "First executable outward interval operator for the K305 coherent y master after exact Vandermonde regularization. It extracts the full odd-node D4 factors and the first-three even-node bordered-B5 factors, evaluates the regularizers by mixed divided differences, and emits finite Arb value/first/second-y-derivative constants on an explicit positive two-radius cell. Exact rational and three shrinking-scale Bessel controls reproduce the unregularized determinants. K302 remains the terminal weighted adapter inside the determinant. The complete boundary-cell composition, global y Peano norm, five gap-axis constants, K294 gamma join, action-column value, residual, native K152 interval, source/ledger move, canon, paper, public and physical claims remain open.",
    }


def validate_payload(payload: dict[str, Any]) -> None:
    operator = payload["regularized_operator"]
    if operator["D4_row_column_orders"] != [0, 1, 2, 3]:
        raise AssertionError("D4 regularization orders changed")
    if operator["bordered_B5_row_column_orders"] != [0, 1, 2, "terminal_raw"]:
        raise AssertionError("bordered regularization orders changed")
    if not operator["y_derivative_commutes_with_regularization"]:
        raise AssertionError("y derivative no longer commutes")
    decision = payload["decision"]
    if not decision["outward_regularized_y_master_operator_implemented"]:
        raise AssertionError("operator missing")
    if decision["complete_y_peano_norm_emitted"] or decision["k294_gamma_join_released"]:
        raise AssertionError("numerical closure overclaim")
    if not payload["terminal_face_adapter"]["detached_unregularized_cofactor_forbidden"]:
        raise AssertionError("K304 failure mode reintroduced")


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
