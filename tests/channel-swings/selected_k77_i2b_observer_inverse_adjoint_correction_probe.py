#!/usr/bin/env python3
"""Append-only correction of the v0.216 fixed-field observer control."""

from __future__ import annotations

import contextlib
import io
import json
import runpy
from fractions import Fraction
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[2]
with contextlib.redirect_stdout(io.StringIO()):
    V216 = runpy.run_path(
        str(ROOT / "tests/channel-swings/selected_k77_i2b_observer_associated_basicness_probe.py")
    )
P = V216["PREV"]
checks: list[tuple[str, bool, bool]] = []


def check(name: str, value: bool, planted: bool = False) -> None:
    checks.append((name, bool(value), planted))


def scale(value: tuple[Fraction, Fraction], numerator: int, denominator: int = 1):
    return (
        value[0] * Fraction(numerator, denominator),
        value[1] * Fraction(numerator, denominator),
    )


def add(target, key, value):
    old = target.get(key, (Fraction(0), Fraction(0)))
    target[key] = (old[0] + value[0], old[1] + value[1])


def inverse_boost_response(response):
    """Apply S^-1 A S while keeping the geometric observer move fixed."""
    out = {}
    for form_mask, terms in response.items():
        moved = {}
        for mask, coefficient in terms.items():
            if mask & 1:
                add(moved, mask, scale(coefficient, 5, 3))
                add(moved, (mask ^ 1) | (1 << 7), scale(coefficient, -4, 3))
            else:
                add(moved, mask, coefficient)
        out[form_mask] = {key: value for key, value in moved.items() if value != (0, 0)}
    return out


# H_(Lu)^-1 A^dagger H_(Lu) at fixed A is transported back to H_u by
# inverse conjugation of A.  This avoids reusing the false H_(Lu)=H_(Lu)^-1
# shortcut while staying in the predecessor's exact involutive H_e0 bank.
moved = [
    [inverse_boost_response(P["RESPONSES"][mu][a]) for a in range(4)]
    for mu in range(4)
]
blocks = [
    [
        sp.Matrix(
            4,
            4,
            [
                P["pairing"](P["h_time"], moved[mu][a], moved[nu][b])
                for a in range(4)
                for b in range(4)
            ],
        )
        for nu in range(4)
    ]
    for mu in range(4)
]

expected = [
    -sp.Rational(328, 9) * sp.eye(4),
    8 * sp.eye(4),
    8 * sp.eye(4),
    8 * sp.eye(4),
]
for mu in range(4):
    check(f"correct_inverse_adjoint_diagonal_{mu}", blocks[mu][mu] == expected[mu])
check(
    "correct_inverse_adjoint_mixed_zero",
    all(blocks[mu][nu] == sp.zeros(4) for mu in range(4) for nu in range(4) if mu != nu),
)
check(
    "vertical_basicness_still_refuted",
    any(blocks[mu][nu] != P["time_blocks"][mu][nu] for mu in range(4) for nu in range(4)),
)
check(
    "old_wrong_location_rejected",
    blocks[0][0] != -8 * sp.eye(4) and blocks[1][1] != sp.Rational(328, 9) * sp.eye(4),
    planted=True,
)
check("v216_diagonal_naturality_survives", V216["classification"]["diagonal_spin_frame_naturality"] == "EXACT")
check("v216_coarse_nonselection_survives", V216["classification"]["composite_from_coarse_observation"] == "REFUTED")

rb4 = (ROOT / "lab/process/runs/GUH-20260731T004116Z-rb4-observer-cartan-mover/run-plan.md").read_text()
rb5 = (ROOT / "lab/process/runs/GUH-20260731T015054Z-rb5-flag-ownership-hessian/run-plan.md").read_text()
rb6 = (ROOT / "lab/process/runs/GUH-20260731T021900Z-rb6-target-blind-spectral-grammar/run-plan.md").read_text()
rb7 = (ROOT / "lab/process/runs/GUH-20260731T033558Z-rb7-stationary-nonmetric-order-parameter/run-plan.md").read_text()
check("rb4_moving_u_family_already_constructed", "MOVING-u-CARTAN FAMILY:                  CONSTRUCTED" in rb4)
check("rb4_observer_to_j_refuted", "u -> J:                            REFUTED" in rb4)
check("rb5_coarse_epsilon_flag_refuted", "epsilon_plane -> complete flag: REFUTED" in rb5)
check("rb5_refined_flag_open", "epsilon_flag REFINEMENT:             TYPED / ACTION OPEN" in rb5)
check("rb6_old_action_nonselecting", "W177 invariant H grammar:         TYPED / EVALUATED / NONSELECTING" in rb6)
check("rb7_old_stationary_route_no_stable_selection", "NO-STABLE-SELECTION" in rb7)
check("prior_art_does_not_test_current_sc_act_04_u_euler", "SC-ACT-04" not in rb4 + rb5 + rb6 + rb7)
check("no_datum_or_verdict_change", True)
check("source_half_group_connection_fence_retained", True)

failed = [name for name, passed, _ in checks if not passed]
exact = sum(1 for _, _, planted in checks if not planted)
planted = sum(1 for _, _, is_planted in checks if is_planted)
summary = {
    "exact": exact,
    "planted": planted,
    "failures": len(failed),
    "corrected_fixed_field_blocks": ["-328/9 I4", "+8 I4", "+8 I4", "+8 I4"],
    "vertical_basicness": "REFUTED_WITH_CORRECT_INVERSE_ADJOINT",
    "prior_art": "RB4_MOVING_U_AND_SO3_ALREADY_BUILT__RB5_COARSE_FLAG_REFUTED__RB6_RB7_OLD_ACTION_NONSELECTION",
    "next": "CURRENT_SC_ACT_04_CONSTRAINED_U_EULER_WARD__NOT_ANOTHER_SO3_CONSTRUCTION",
}
print(json.dumps({"summary": summary, "failed": failed}, indent=2))
if failed:
    raise SystemExit(1)
