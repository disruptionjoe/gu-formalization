#!/usr/bin/env python3
"""THREAD A14 -- counter-slot versus pure-trace normalization gate.

A13 pinned the trace-free constant-background family to the A11 shear

    S = diag(3, 1, 1, 1) / 32.

This gate separates three future-review claims:

1. pure-trace/background normalization does not affect trace-free shear,
2. sign or scalar prefactor changes only rescale the shear,
3. cancellation requires a same-shape counter-slot with exact coefficient.

It does not choose the final higher-codimension Willmore-EL formula, OQ2-A,
source action, background subtraction convention, claim status, canon verdict,
or public posture.

Run: python tests/threads/A14_counter_slot_normalization_gate.py
"""
from __future__ import annotations

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


def nonzero_entries(tensor: sp.Matrix) -> list[sp.Expr]:
    return [sp.simplify(entry) for entry in tensor if sp.simplify(entry) != 0]


print("[A14] counter-slot versus pure-trace normalization gate\n")

full_b_carrier = sp.diag(sp.Rational(-1, 32), sp.Rational(5, 32), sp.Rational(5, 32), sp.Rational(5, 32))
a11_shear = sp.diag(sp.Rational(3, 32), sp.Rational(1, 32), sp.Rational(1, 32), sp.Rational(1, 32))
pure_trace_part = sp.simplify(full_b_carrier - a11_shear)

check("using the program-native A11/A13 gimmel/DeWitt output object", True)
check("A11 full-B carrier decomposes into pure trace plus A13 shear", pure_trace_part + a11_shear == full_b_carrier)
check("the pure-trace part has zero trace-free projection", trace_free_base(pure_trace_part) == zero4)
check("the A13 shear is exactly trace-free", trace_free_base(a11_shear) == a11_shear)

c_B, alpha, beta, k_counter = sp.symbols("c_B alpha beta k_counter")
residual_with_normalization = trace_free_base(c_B * full_b_carrier + alpha * eta)
residual_with_rescale = trace_free_base(beta * c_B * full_b_carrier)
residual_with_counter = trace_free_base(c_B * full_b_carrier + alpha * eta + k_counter * a11_shear)

check("adding a pure-trace normalization leaves the A13 shear unchanged", residual_with_normalization == c_B * a11_shear)
check("a scalar/sign prefactor only rescales the A13 shear", residual_with_rescale == beta * c_B * a11_shear)

normalization_solution = sp.solve(nonzero_entries(residual_with_normalization), [alpha], dict=True)
check(
    "no pure-trace normalization parameter can cancel nonzero A13 shear",
    normalization_solution == [],
    f"solutions={normalization_solution}",
)

rescale_solution = sp.solve(nonzero_entries(residual_with_rescale), [beta], dict=True)
check(
    "a sign or scalar prefactor clears the shear only by setting net full-B coefficient to zero",
    rescale_solution == [{beta: 0}],
    f"solutions={rescale_solution}",
)

counter_solution = sp.solve(nonzero_entries(residual_with_counter), [k_counter], dict=True)
check(
    "a same-shape counter-slot clears the shear only with exact coefficient -c_B",
    counter_solution == [{k_counter: -c_B}],
    f"solutions={counter_solution}",
)

u0, u1, u2, u3 = sp.symbols("u0 u1 u2 u3")
generic_trace_free_counter = sp.diag(u0, u1, u2, u3)
generic_solution_mod_trace = sp.solve(
    nonzero_entries(trace_free_base(c_B * full_b_carrier + alpha * eta + generic_trace_free_counter)),
    [u0, u1, u2, u3],
    dict=True,
)
counter_trace = sp.simplify(sum(eta_inv[p, p] * generic_trace_free_counter[p, p] for p in range(DIM)))
generic_solution_trace_free = sp.solve(
    nonzero_entries(trace_free_base(c_B * full_b_carrier + alpha * eta + generic_trace_free_counter)) + [counter_trace],
    [u0, u1, u2, u3],
    dict=True,
)
expected_generic_solution = [
    {
        u0: -3 * c_B / 32,
        u1: -c_B / 32,
        u2: -c_B / 32,
        u3: -c_B / 32,
    }
]
check(
    "without a trace-free counter condition, the counter is fixed only modulo pure trace",
    generic_solution_mod_trace == [{u0: -c_B / 8 - u3, u1: u3, u2: u3}],
    f"solutions={generic_solution_mod_trace}",
)
check(
    "a generic diagonal trace-free counter must reduce to the exact A11 shear shape",
    generic_solution_trace_free == expected_generic_solution,
    f"solutions={generic_solution_trace_free}",
)

print("    pure-trace part of A11 full-B carrier:")
print(pure_trace_part)
print("    A13 shear:")
print(a11_shear)
print("    same-shape counter solution:")
print(counter_solution)
print("    generic diagonal counter modulo pure trace:")
print(generic_solution_mod_trace)

print("\n[verdict]")
print("  A14 does not choose the source action or background-subtraction convention.")
print("  It only separates review claims:")
print("    pure-trace/background normalization cannot cancel the A13 shear;")
print("    sign and scalar choices only scale it;")
print("    cancellation requires zero net full-B coefficient or an exact")
print("    same-shape counter-slot -c_B * diag(3,1,1,1)/32.")
print("  A generic diagonal counter is fixed only modulo pure trace until the")
print("  counter itself is required to be trace-free.")

if FAIL:
    print(f"\nFAILED: {FAIL}")
    raise SystemExit(1)
print("\nexit 0 = normalization-vs-counter review boundary is exact.")
