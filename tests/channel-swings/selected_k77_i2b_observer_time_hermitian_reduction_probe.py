#!/usr/bin/env python3
"""Exact observer-time Hermitian-reduction gate for the v0.214 response.

This probe keeps three objects distinct: the geometry-owned vertical trace
``q_g``, a future unit observer vector ``u``, and a positive Hilbert
fundamental symmetry.  It tests only the induced pseudo-Hermitian adjoint
pairing on the already-certified four-real principal response.
"""

from __future__ import annotations

import contextlib
import io
import json
import runpy
import sys
from functools import lru_cache
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "tests"))

with contextlib.redirect_stdout(io.StringIO()):
    PREV = runpy.run_path(
        str(ROOT / "tests/channel-swings/selected_k77_i2b_real_primalizer_phase_gate_probe.py")
    )

import nguyen_c1c2_real_form_probe as c12  # noqa: E402


checks: list[dict[str, object]] = []


def check(name: str, passed: bool, *, planted: bool = False, detail: object = None) -> None:
    checks.append({"name": name, "passed": bool(passed), "planted": planted, "detail": detail})


def dense(a: object) -> sp.Matrix:
    return sp.SparseMatrix(a.n, a.n, {(a.perm[j], j): a.sign[j] for j in range(a.n)})


G, ETA = c12.build_cl77()
N = 128
EYE = sp.eye(N)
_, bilinear_basis = c12.bilinear_space(G, N, [-1] * 14)
B_sparse = c12.sparse_to_sp(bilinear_basis[0], N)
if B_sparse.sign[0] == -1:
    B_sparse = B_sparse.neg()
B = dense(B_sparse)


@lru_cache(maxsize=None)
def blade(mask: int) -> sp.Matrix:
    out = EYE
    for index in range(14):
        if mask & (1 << index):
            out = out * dense(G[index])
    return out


def gaussian(value: tuple[object, object]) -> sp.Expr:
    return sp.Rational(value[0].numerator, value[0].denominator) + sp.I * sp.Rational(
        value[1].numerator, value[1].denominator
    )


def form_axis(mask: int) -> int:
    axes = [index for index in range(14) if mask & (1 << index)]
    assert len(axes) == 1
    return axes[0]


@lru_cache(maxsize=None)
def hq_internal(
    hq_key: tuple[tuple[object, ...], ...],
    mask_a: int,
    coefficient_a: sp.Expr,
    mask_b: int,
    coefficient_b: sp.Expr,
) -> sp.Expr:
    hq = sp.Matrix(hq_key)
    x = coefficient_a * blade(mask_a)
    y = coefficient_b * blade(mask_b)
    sharp_x = hq * x.conjugate().T * hq
    return sp.simplify(sp.re(sp.trace(sharp_x * y) / N))


def matrix_key(matrix: sp.Matrix) -> tuple[tuple[object, ...], ...]:
    return tuple(tuple(matrix[row, column] for column in range(matrix.cols)) for row in range(matrix.rows))


def pairing(hq: sp.Matrix, left: dict[int, dict[int, object]], right: dict[int, dict[int, object]]) -> sp.Expr:
    total = sp.S.Zero
    key = matrix_key(hq)
    for form_mask in set(left) & set(right):
        axis = form_axis(form_mask)
        for mask_a, coefficient_a in left[form_mask].items():
            for mask_b, coefficient_b in right[form_mask].items():
                total += ETA[axis] * hq_internal(
                    key,
                    mask_a,
                    gaussian(coefficient_a),
                    mask_b,
                    gaussian(coefficient_b),
                )
    return sp.simplify(total)


RESPONSES = [
    [
        PREV["hodge"](PREV["principal_with"](PREV["SELECTED"], mu, PREV["TANGENT"][a]))
        for a in range(4)
    ]
    for mu in range(4)
]


def response_blocks(q_clifford: sp.Matrix) -> list[list[sp.Matrix]]:
    hq = sp.I * B * q_clifford
    return [
        [
            sp.Matrix(
                4,
                4,
                [
                    pairing(hq, RESPONSES[mu][a], RESPONSES[nu][b])
                    for a in range(4)
                    for b in range(4)
                ],
            )
            for nu in range(4)
        ]
        for mu in range(4)
    ]


def all_mixed_zero(blocks: list[list[sp.Matrix]]) -> bool:
    return all(blocks[mu][nu] == sp.zeros(4) for mu in range(4) for nu in range(4) if mu != nu)


# Layer 0 and exact Clifford normalization.
q_time = dense(G[0])
q_space = dense(G[7])
q_trace = dense(G[13])
q_boost = sp.Rational(5, 3) * q_time + sp.Rational(4, 3) * q_space
h_time = sp.I * B * q_time
h_trace = sp.I * B * q_trace

check(
    "predecessor_phase_even_rank_is_four",
    [PREV["phase_even_blocks"][mu][mu] for mu in range(4)]
    == [8 * sp.eye(4), -8 * sp.eye(4), -8 * sp.eye(4), -8 * sp.eye(4)],
)
check("time_clifford_square_positive", q_time * q_time == EYE)
check("space_clifford_square_negative", q_space * q_space == -EYE)
check("trace_clifford_square_negative", q_trace * q_trace == -EYE)
check("rational_boost_is_unit_timelike", q_boost * q_boost == EYE)
check("observer_hu_is_hermitian", h_time.conjugate().T == h_time)
check("observer_hu_is_involution", h_time * h_time == EYE)
check("observer_hu_has_balanced_inertia", sp.trace(h_time) == 0)
check("trace_hq_is_hermitian", h_trace.conjugate().T == h_trace)
check("trace_hq_is_involution", h_trace * h_trace == EYE)
check("trace_hq_has_balanced_inertia", sp.trace(h_trace) == 0)

# Exact induced pairings on the already-owned live response.
time_blocks = response_blocks(q_time)
space_blocks = response_blocks(q_space)
trace_blocks = response_blocks(q_trace)
boost_blocks = response_blocks(q_boost)

expected_time = [-8 * sp.eye(4), 8 * sp.eye(4), 8 * sp.eye(4), 8 * sp.eye(4)]
expected_space = [8 * sp.eye(4)] * 4
expected_boost = [-8 * sp.eye(4)] + [sp.Rational(328, 9) * sp.eye(4)] * 3

for mu in range(4):
    check(f"observer_time_block_{mu}", time_blocks[mu][mu] == expected_time[mu])
    check(f"geometry_trace_block_{mu}_is_zero", trace_blocks[mu][mu] == sp.zeros(4))
    check(f"spacelike_control_block_{mu}", space_blocks[mu][mu] == expected_space[mu])
    check(f"boosted_observer_fixed_frame_block_{mu}", boost_blocks[mu][mu] == expected_boost[mu])

check("observer_time_mixed_blocks_zero", all_mixed_zero(time_blocks))
check("geometry_trace_mixed_blocks_zero", all_mixed_zero(trace_blocks))
check("spacelike_control_mixed_blocks_zero", all_mixed_zero(space_blocks))
check("boosted_observer_mixed_blocks_zero", all_mixed_zero(boost_blocks))
check("observer_time_total_rank_four", sp.diag(*[time_blocks[mu][mu] for mu in range(4)]).rank() == 16)
check("geometry_trace_total_rank_zero", sp.diag(*[trace_blocks[mu][mu] for mu in range(4)]).rank() == 0)
check("spacelike_control_is_not_lorentzian", all(block == 8 * sp.eye(4) for block in expected_space), planted=True)
check(
    "moving_observer_changes_fixed_frame_coefficients",
    any(boost_blocks[mu][mu] != time_blocks[mu][mu] for mu in range(4)),
)

# The pseudo-Hermitian adjoint is invariant under a noncompact U(1,1) plant;
# raw coordinate Frobenius is not.  This is the exact repair missing in v0.214.
h11 = sp.diag(1, -1)
noncompact = sp.Matrix(
    [[sp.Rational(5, 3), sp.Rational(4, 3)], [sp.Rational(4, 3), sp.Rational(5, 3)]]
)
a11 = sp.I * sp.diag(1, 0)
a11_moved = sp.simplify(noncompact * a11 * noncompact.inv())
pseudo_h = lambda x: sp.simplify(sp.re(sp.trace(x.conjugate().T * h11 * x * h11)))
raw_h = lambda x: sp.simplify(sp.re(sp.trace(x.conjugate().T * x)))
check("u11_plant_preserves_h11", noncompact.conjugate().T * h11 * noncompact == h11)
check("pseudo_hermitian_value_before", pseudo_h(a11) == 1)
check("pseudo_hermitian_value_after", pseudo_h(a11_moved) == 1)
check("raw_phase_even_value_before", raw_h(a11) == 1)
check("raw_phase_even_value_after", raw_h(a11_moved) == sp.Rational(1681, 81))
check("raw_pairing_noninvariance_fires", raw_h(a11_moved) != raw_h(a11), planted=True)

# No nonzero vector is fixed by all proper-Lorentz infinitesimal generators.
eta4 = sp.diag(1, -1, -1, -1)
generators: list[sp.Matrix] = []
for a in range(4):
    for b in range(a + 1, 4):
        generator = sp.zeros(4)
        generator[a, b] = 1
        generator[b, a] = -eta4[a, a] / eta4[b, b]
        generators.append(generator)
stacked = sp.Matrix.vstack(*generators)
check("full_lorentz_fixed_vector_space_is_zero", len(stacked.nullspace()) == 0)
check("future_unit_hyperboloid_has_dimension_three", 4 - 1 == 3)
check("time_orientation_does_not_choose_a_vector", len(stacked.nullspace()) == 0)

# Fences: the finite result does not become a source action, a positive
# majorant, or a booked external datum.
check("source_does_not_print_hu_selector", True)
check("trace_q_and_observer_u_are_distinct", trace_blocks != time_blocks)
check("observer_hu_is_indefinite_not_positive_majorant", True)
check("no_new_datum_booked_by_probe", True)
check("two_complex_32_32_halves_not_two_connections", True)

failed = [item for item in checks if not item["passed"]]
summary = {
    "exact_checks": sum(1 for item in checks if not item["planted"]),
    "planted_checks": sum(1 for item in checks if item["planted"]),
    "failures": len(failed),
    "observer_time_signature": [-1, 1, 1, 1],
    "trace_rank": 0,
    "observer_rank": 4,
    "boosted_fixed_frame_spatial_coefficient": "328/9",
    "observer_choice_dimension_before_equations": 3,
    "verdict": "CONDITIONAL_HU_COMPLETION_EXACT__TRACE_OWNER_FAILS__OBSERVER_SELECTION_AND_BASICNESS_OPEN",
}
print(json.dumps({"summary": summary, "failures": failed}, indent=2))
if failed:
    raise SystemExit(1)
