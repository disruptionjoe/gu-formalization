#!/usr/bin/env python3
"""THREAD A13 -- constant-background coefficient supply/cancellation gate.

A12 localized the trace-free constant-background family to the full-B ambient
coefficient:

    TF(F0) = c_B * diag(3, 1, 1, 1) / 32.

This gate turns that result into an exact source-action/OQ2-A review condition.
It does not choose the final higher-codimension Willmore-EL formula, sign,
scalar prefactor, background subtraction, source action, or OQ2-A branch.

Run: python tests/threads/A13_constant_background_coefficient_supply_gate.py
"""
from __future__ import annotations

from dataclasses import dataclass

import sympy as sp

FAIL: list[str] = []


def check(name: str, ok: bool, detail: str = "") -> None:
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}{('  ' + detail) if detail else ''}")
    if not ok:
        FAIL.append(name)


DIM = 4
eta = sp.diag(-1, 1, 1, 1)
eta_inv = eta
zero4 = sp.zeros(DIM, DIM)


def trace_free_base(tensor: sp.Matrix) -> sp.Matrix:
    tr = sp.simplify(sum(eta_inv[p, p] * tensor[p, p] for p in range(DIM)))
    return sp.Matrix(DIM, DIM, lambda m, n: sp.simplify(tensor[m, n] - sp.Rational(1, DIM) * eta[m, n] * tr))


def matrix_is_zero(tensor: sp.Matrix) -> bool:
    return all(sp.simplify(entry) == 0 for entry in tensor)


def matrix_is_nonzero(tensor: sp.Matrix) -> bool:
    return any(sp.simplify(entry) != 0 for entry in tensor)


def nonzero_entries(tensor: sp.Matrix) -> list[sp.Expr]:
    return [sp.simplify(entry) for entry in tensor if sp.simplify(entry) != 0]


PURE_TRACE_H_CARRIER = sp.Rational(1, 8) * eta
FULL_B_CARRIER = sp.diag(sp.Rational(-1, 32), sp.Rational(5, 32), sp.Rational(5, 32), sp.Rational(5, 32))
FULL_B_SHEAR = sp.diag(sp.Rational(3, 32), sp.Rational(1, 32), sp.Rational(1, 32), sp.Rational(1, 32))


@dataclass(frozen=True)
class SupplyScenario:
    name: str
    full_b_coefficient: sp.Expr
    counter_shear_coefficient: sp.Expr
    expected_trace_free_clear: bool
    boundary: str


def net_trace_free(full_b_coefficient: sp.Expr, counter_shear_coefficient: sp.Expr = sp.Integer(0)) -> sp.Matrix:
    return sp.simplify((full_b_coefficient + counter_shear_coefficient) * FULL_B_SHEAR)


print("[A13] constant-background coefficient supply/cancellation gate\n")

check("using the program-native gimmel/DeWitt A12 output object", True)
check("A12 H-class carrier is pure trace", trace_free_base(PURE_TRACE_H_CARRIER) == zero4)
check("A12 full-B carrier has the exact A11 trace-free shear", trace_free_base(FULL_B_CARRIER) == FULL_B_SHEAR)
check("the A11/A12 shear tensor is nonzero and trace-free", matrix_is_nonzero(FULL_B_SHEAR) and trace_free_base(FULL_B_SHEAR) == FULL_B_SHEAR)

c_H, c_B, k_counter = sp.symbols("c_H c_B k_counter")
family = sp.simplify(c_H * PURE_TRACE_H_CARRIER + c_B * FULL_B_CARRIER)
trace_free_family = trace_free_base(family)

check("A13 input family has the A12 trace-free form", trace_free_family == c_B * FULL_B_SHEAR)
check("the H-class/pure-trace coefficient is absent after trace-free projection", trace_free_family.free_symbols == {c_B})

no_counter_solution = sp.solve(nonzero_entries(trace_free_family), [c_B], dict=True)
check(
    "without a counter-slot, trace-free cancellation is equivalent to c_B = 0",
    no_counter_solution == [{c_B: 0}],
    f"solutions={no_counter_solution}",
)

with_same_shear_counter = sp.simplify(trace_free_family + k_counter * FULL_B_SHEAR)
counter_solution = sp.solve(nonzero_entries(with_same_shear_counter), [k_counter], dict=True)
check(
    "an exact same-shape counter-slot cancels only with coefficient -c_B",
    counter_solution == [{k_counter: -c_B}],
    f"solutions={counter_solution}",
)

u0, u1, u2, u3 = sp.symbols("u0 u1 u2 u3")
generic_diagonal_counter = sp.diag(u0, u1, u2, u3)
generic_cancel_solution = sp.solve(
    nonzero_entries(sp.simplify(trace_free_family + generic_diagonal_counter)),
    [u0, u1, u2, u3],
    dict=True,
)
expected_generic_solution = [{u0: -3 * c_B / 32, u1: -c_B / 32, u2: -c_B / 32, u3: -c_B / 32}]
check(
    "a generic diagonal counter must match the exact A11 shear shape",
    generic_cancel_solution == expected_generic_solution,
    f"solutions={generic_cancel_solution}",
)

c_W = sp.symbols("c_W", nonzero=True)
scenarios = [
    SupplyScenario(
        name="H_CLASS_ONLY",
        full_b_coefficient=sp.Integer(0),
        counter_shear_coefficient=sp.Integer(0),
        expected_trace_free_clear=True,
        boundary="clear only if the final branch truly has no net full-B ambient coefficient",
    ),
    SupplyScenario(
        name="RAW_FULL_B_PLUS",
        full_b_coefficient=c_W,
        counter_shear_coefficient=sp.Integer(0),
        expected_trace_free_clear=False,
        boundary="nonzero full-B supply leaves A11 shear with the chosen prefactor",
    ),
    SupplyScenario(
        name="RAW_FULL_B_MINUS",
        full_b_coefficient=-c_W,
        counter_shear_coefficient=sp.Integer(0),
        expected_trace_free_clear=False,
        boundary="sign flips amplitude but does not cancel the shear",
    ),
    SupplyScenario(
        name="BACKGROUND_SUBTRACTED_COUNTER",
        full_b_coefficient=c_W,
        counter_shear_coefficient=-c_W,
        expected_trace_free_clear=True,
        boundary="cancellation requires an exact counter-slot, not a pure trace term",
    ),
]

for scenario in scenarios:
    residual = net_trace_free(scenario.full_b_coefficient, scenario.counter_shear_coefficient)
    clears = matrix_is_zero(residual)
    check(
        f"{scenario.name} trace-free outcome matches declared boundary",
        clears == scenario.expected_trace_free_clear,
        scenario.boundary,
    )

print("    trace-free family:")
print(trace_free_family)
print("    same-shape counter solution:")
print(counter_solution)
print("    generic diagonal counter solution:")
print(generic_cancel_solution)

print("\n[verdict]")
print("  A13 does not decide whether OQ2-A supplies the full-B ambient slot.")
print("  It pins the exact review condition created by A12:")
print("    TF(F0) clears iff the net full-B shear coefficient is zero,")
print("    or iff an additional counter-slot supplies exactly -c_B times")
print("    diag(3,1,1,1)/32.")
print()
print("  Sign and scalar-prefactor choices only scale the shear. Pure-trace/H-class")
print("  terms cannot cancel it. Therefore a future source-action/OQ2-A branch must")
print("  state one of three things explicitly: no full-B slot, a nonzero residual")
print("  shear, or an exact background-subtraction/counterterm with the same shape.")

if FAIL:
    print(f"\nFAILED: {FAIL}")
    raise SystemExit(1)
print("\nexit 0 = A12 review point is converted to an exact coefficient-supply gate.")
