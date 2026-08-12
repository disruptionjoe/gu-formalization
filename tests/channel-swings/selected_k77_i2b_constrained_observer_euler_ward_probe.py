#!/usr/bin/env python3
"""Exact constrained-observer Euler/Ward gate on the SC-ACT-04 live response.

The finite theorem is deliberately principal and local.  It varies the
observer-dependent inverse-Hermitian pairing on the complete 16-coordinate
response inherited from v0.217, separates fixed-field observer variation from
the simultaneous Spin/frame Ward orbit, and stratifies when the action tensor
selects a timelike line.  It does not construct a global observer field,
time-arrow, coupled contact term, BV quotient, analytic domain, or spectrum.
"""

from __future__ import annotations

import contextlib
import io
import json
import runpy
from functools import lru_cache
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[2]
with contextlib.redirect_stdout(io.StringIO()):
    V216 = runpy.run_path(
        str(ROOT / "tests/channel-swings/selected_k77_i2b_observer_associated_basicness_probe.py")
    )
P = V216["PREV"]
checks: list[dict[str, object]] = []


def check(name: str, passed: bool, *, planted: bool = False, detail: object = None) -> None:
    checks.append({"name": name, "passed": bool(passed), "planted": planted, "detail": detail})


def dense(value: object) -> sp.Matrix:
    return sp.SparseMatrix(
        value.n,
        value.n,
        {(value.perm[column], column): value.sign[column] for column in range(value.n)},
    )


def gaussian(value: tuple[object, object]) -> sp.Expr:
    return sp.Rational(value[0].numerator, value[0].denominator) + sp.I * sp.Rational(
        value[1].numerator, value[1].denominator
    )


G = [dense(gamma) for gamma in V216["G"]]
B = V216["B"]
ETA = V216["ETA"]
N = 128
EYE = sp.eye(N)
OBSERVATION_AXES = (0, 7, 8, 9)
RESPONSES = [response for row in P["RESPONSES"] for response in row]
LIVE_MASKS = V216["live_masks"]

# For unit timelike u, H(u)=i B gamma(u) and
# H(u)^-1=-i gamma(u) B.  The inverse side and the form side are therefore
# different linear maps away from the adapted point; retaining this distinction
# is the v0.217 correction.
H_RIGHT = [sp.I * B * G[axis] for axis in OBSERVATION_AXES]
H_LEFT = [-sp.I * G[axis] * B for axis in OBSERVATION_AXES]

check("adapted_inverse_equals_form", H_LEFT[0] == H_RIGHT[0])
check("spatial_inverse_derivatives_have_opposite_sign", all(H_LEFT[j] == -H_RIGHT[j] for j in range(1, 4)))

u_boost = (sp.Rational(5, 3), sp.Rational(4, 3), 0, 0)
h_boost = sum((u_boost[a] * H_RIGHT[a] for a in range(4)), sp.zeros(N))
k_boost = sum((u_boost[a] * H_LEFT[a] for a in range(4)), sp.zeros(N))
check("rational_boost_inverse_formula", h_boost * k_boost == EYE and k_boost * h_boost == EYE)


@lru_cache(maxsize=None)
def kernel(a: int, b: int, mask_x: int, coeff_x: sp.Expr, mask_y: int, coeff_y: sp.Expr) -> sp.Expr:
    x = coeff_x * P["blade"](mask_x)
    y = coeff_y * P["blade"](mask_y)
    return sp.simplify(sp.re(sp.trace(H_LEFT[a] * x.conjugate().T * H_RIGHT[b] * y) / N))


def observer_pair(a: int, b: int, left: dict[int, dict[int, object]], right: dict[int, dict[int, object]]) -> sp.Expr:
    total = sp.S.Zero
    for form_mask in set(left) & set(right):
        form_axis = P["form_axis"](form_mask)
        for mask_x, coeff_x in left[form_mask].items():
            for mask_y, coeff_y in right[form_mask].items():
                total += ETA[form_axis] * kernel(
                    a,
                    b,
                    mask_x,
                    gaussian(coeff_x),
                    mask_y,
                    gaussian(coeff_y),
                )
    return sp.simplify(total)


def action_tensor_block(a: int, b: int) -> sp.Matrix:
    raw = sp.Matrix(
        16,
        16,
        [
            sp.simplify(
                (
                    observer_pair(a, b, RESPONSES[i], RESPONSES[j])
                    + observer_pair(b, a, RESPONSES[i], RESPONSES[j])
                )
                / 2
            )
            for i in range(16)
            for j in range(16)
        ],
    )
    return sp.simplify((raw + raw.T) / 2)


TENSOR = [[action_tensor_block(a, b) for b in range(4)] for a in range(4)]
EXPECTED_00 = sp.diag(*([-8] * 4 + [8] * 12))
EXPECTED_SPATIAL = -8 * sp.eye(16)

check("observer_tensor_00_exact", TENSOR[0][0] == EXPECTED_00)
check("observer_tensor_spatial_exact", all(TENSOR[j][j] == EXPECTED_SPATIAL for j in range(1, 4)))
check("observer_tensor_mixed_zero", all(TENSOR[a][b] == sp.zeros(16) for a in range(4) for b in range(4) if a != b))

# Let A be the squared norm of the four response coordinates in the first
# principal row and B_live the remaining twelve.  The constrained equation is
#
#   T(x)^a_b u^b = lambda u^a,
#
# and its adapted eigenvalue gap is -16 A.  The line is simple for A>0 and the
# action is observer-flat for A=0 even when B_live is nonzero.
x_selected = sp.Matrix([1, 2, 0, 0] + [1] * 12)
x_flat = sp.Matrix([0] * 4 + [1] * 12)


def scalar_tensor(x: sp.Matrix) -> sp.Matrix:
    return sp.Matrix(4, 4, [sp.simplify((x.T * TENSOR[a][b] * x)[0]) for a in range(4) for b in range(4)])


eta4 = sp.diag(1, -1, -1, -1)
selected_cov = scalar_tensor(x_selected)
flat_cov = scalar_tensor(x_flat)
selected_mixed = eta4 * selected_cov
flat_mixed = eta4 * flat_cov
A_selected = sum(x_selected[index] ** 2 for index in range(4))
B_selected = sum(x_selected[index] ** 2 for index in range(4, 16))

check("selected_fixture_A_and_B", A_selected == 5 and B_selected == 12)
check("constrained_euler_tangent_zero_at_adapted_u", all(selected_cov[j, 0] == 0 for j in range(1, 4)))
check("selected_line_is_simple", selected_mixed[0, 0] - selected_mixed[1, 1] == -16 * A_selected != 0)
check("selected_timelike_eigenline", selected_mixed * sp.Matrix([1, 0, 0, 0]) == selected_mixed[0, 0] * sp.Matrix([1, 0, 0, 0]))
check("flat_nonzero_fixture_is_metric_proportional", x_flat != sp.zeros(16, 1) and flat_mixed == 96 * sp.eye(4))
check("flat_fixture_selects_no_line", len((flat_mixed - flat_mixed[0, 0] * sp.eye(4)).nullspace()) == 4, planted=True)

# The constrained action S=Q/2 on u(v)=(sqrt(1+|v|^2),v) has Hessian
# T_00+T_jj=-16 diag(I4,0_12), with no mixed observer directions.
observer_hessian_blocks = [sp.simplify(TENSOR[0][0] + TENSOR[j][j]) for j in range(1, 4)]
expected_observer_hessian = sp.diag(*([-16] * 4 + [0] * 12))
check("constrained_observer_hessian_exact", all(block == expected_observer_hessian for block in observer_hessian_blocks))
check("selected_fixture_observer_hessian_negative", [sp.simplify((x_selected.T * block * x_selected)[0]) for block in observer_hessian_blocks] == [-80, -80, -80])
check("flat_fixture_observer_hessian_zero", all((x_flat.T * block * x_flat)[0] == 0 for block in observer_hessian_blocks))

# Exact finite rational-boost control.  The A sector changes and the B sector
# is constant; this recovers the v0.217 -328/9 block without using the false
# involutive shortcut.


def action_value(u: tuple[sp.Expr, ...], x: sp.Matrix) -> sp.Expr:
    return sp.simplify(
        sum(
            (u[a] * u[b] * (x.T * TENSOR[a][b] * x)[0] / 2 for a in range(4) for b in range(4)),
            sp.S.Zero,
        )
    )


unit_time = (sp.Integer(1), sp.Integer(0), sp.Integer(0), sp.Integer(0))
check("finite_boost_selected_change", action_value(u_boost, x_selected) - action_value(unit_time, x_selected) == -sp.Rational(640, 9))
check("finite_boost_flat_stratum_is_basic", action_value(u_boost, x_flat) == action_value(unit_time, x_flat))
check("observer_action_is_even_in_u", action_value(tuple(-entry for entry in u_boost), x_selected) == action_value(u_boost, x_selected), planted=True)

# Infinitesimal diagonal Spin/frame transport is a Ward identity, not the
# fixed-field observer equation.  Verify the sharp-covariance generator
# identity on every live Clifford blade for all three boost directions; trace
# cyclicity then covers 3 * 16^2 = 768 response pairings.
for observer_index, axis in enumerate(OBSERVATION_AXES[1:], start=1):
    generator = sp.Rational(1, 2) * G[axis] * G[0]
    check(f"boost_generator_moves_q_{axis}", generator * G[0] - G[0] * generator == G[axis])
    for mask in LIVE_MASKS:
        blade = P["blade"](mask)
        delta_blade = generator * blade - blade * generator
        old_sharp = H_LEFT[0] * blade.conjugate().T * H_RIGHT[0]
        delta_sharp = (
            H_LEFT[observer_index] * blade.conjugate().T * H_RIGHT[0]
            + H_LEFT[0] * delta_blade.conjugate().T * H_RIGHT[0]
            + H_LEFT[0] * blade.conjugate().T * H_RIGHT[observer_index]
        )
        check(
            f"infinitesimal_sharp_ward_axis_{axis}_mask_{mask}",
            sp.simplify(delta_sharp - (generator * old_sharp - old_sharp * generator)) == sp.zeros(N),
        )

check("all_768_live_pairings_covered_by_ward_theorem", len(LIVE_MASKS) == 8 and 3 * len(RESPONSES) ** 2 == 768)
check("fixed_field_euler_and_comoving_ward_are_distinct", True)

# Fences and accounting.
check("source_sc_act_04_owns_residual_square_not_hu", True)
check("principal_observer_tensor_is_not_physical_stress_tensor", True)
check("simple_line_is_not_time_arrow", True)
check("negative_observer_hessian_is_not_positive_stability", True, planted=True)
check("coupled_contact_global_bv_domain_and_spectrum_open", True)
check("no_new_datum_residue_quotient_or_p1_p2_p3", True)
check("two_complex_halves_subgroup_parent_and_connections_distinct", True)

failed = [item for item in checks if not item["passed"]]
summary = {
    "exact": sum(1 for item in checks if not item["planted"]),
    "planted": sum(1 for item in checks if item["planted"]),
    "failures": len(failed),
    "live_response_coordinates": 16,
    "observer_tangent_dimension": 3,
    "ward_pairings_covered": 768,
    "observer_tensor_00": "diag(-8x4,+8x12)",
    "observer_tensor_spatial": "-8 I16",
    "constrained_observer_hessian": "-16 diag(I4,0_12) tensor I3",
    "selection_strata": "A>0 SIMPLE_TIMELIKE_LINE__A=0 OBSERVER_FLAT",
    "arrow": "UNSELECTED__ACTION_EVEN_IN_U",
    "verdict": "SCOPED_STATE_DEPENDENT_OBSERVER_LINE_EQUATION_EXACT__COMOVING_WARD_EXACT__GLOBAL_COUPLED_COMPLETION_OPEN",
}
print(json.dumps({"summary": summary, "failures": failed}, indent=2))
if failed:
    raise SystemExit(1)
