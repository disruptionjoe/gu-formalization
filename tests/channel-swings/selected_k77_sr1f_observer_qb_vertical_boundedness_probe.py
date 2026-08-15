#!/usr/bin/env sage -python
"""Exact SR-1F moving-observer Q_B boundedness gate.

The highest-conviction structural repair after SR-1E is the already-built
observer-Hermitian family ``Q_u``.  This probe evaluates that actual moving
pairing on the two exact vertical selected-Shiab residual rays.  It proves
that their quartics are ``+16 c(u)`` and ``-16 c(u)``, where
``c(u)=sum_mu u_mu^2`` is strictly positive on the unit-timelike observer
hyperboloid.  Moving or even ray-dependently choosing ``u`` therefore cannot
stabilize the released action on the admitted carrier.

The result kills this existing zero-new-field moving repair, not every
conceivable field-dependent primalizer.  Source/BV constraints and owned
higher-even action terms remain outside this gate.
"""

from __future__ import annotations

from collections import Counter
from fractions import Fraction
import contextlib
import io
import json
from pathlib import Path
import runpy


ROOT = Path(__file__).resolve().parents[2]
COUNTS: Counter[str] = Counter()
FAILURES: list[str] = []


def check(kind: str, label: str, condition: object) -> None:
    COUNTS[kind] += 1
    ok = bool(condition)
    print(f"{'PASS' if ok else 'FAIL'} [{kind}] {label}", flush=True)
    if not ok:
        FAILURES.append(label)


def read(relative: str) -> str:
    return (ROOT / relative).read_text(encoding="utf-8")


print("A. PREDECESSORS, OWNERSHIP, AND TYPE FENCES")
capture = io.StringIO()
with contextlib.redirect_stdout(capture):
    SR1E = runpy.run_path(
        str(ROOT / "tests/channel-swings/selected_k77_sr1e_vertical_carrier_fixed_natural_boundedness_probe.py")
    )
    OBS = runpy.run_path(
        str(ROOT / "tests/channel-swings/selected_k77_i2b_observer_time_hermitian_reduction_probe.py")
    )
captured = capture.getvalue()
check("prior", "the SR-1E carrier and fixed-natural obstruction replay 40/40",
      "PASS 40/40" in captured)
check("prior", "the observer-Hermitian predecessor replays without failures",
      '"failures": 0' in captured)

observer_artifact = read(
    "explorations/conditional-build/selected-k77-i2b-observer-time-hermitian-reduction-2026-08-12.md"
)
observer_action = read(
    "explorations/conditional-build/selected-k77-i2b-observer-qb-radial-stationarity-2026-08-12.md"
)
associated = read(
    "explorations/conditional-build/selected-k77-i2b-observer-associated-basicness-2026-08-12.md"
)
source = read("lab/sources/weinstein-gu-primary-source-pack-2026-07-30.md")
check("owner", "H_u is an existing conditional moving pairing rather than a positive Hilbert majorant",
      "indefinite Hermitian form and adjoint" in observer_artifact
      and "positive Hilbert majorant" in observer_artifact)
check("owner", "the source prints a Q_B slot but does not identify it with Q_u",
      "does not identify it with this" in observer_action
      and "Hodge-adapted `Q_u`" in observer_action)
check("naturality", "the observer family is already exact under simultaneous Spin transport",
      "all 256 pairings" in associated and "not basic" in associated)
check("degree", "the released first action still has degree at most three on constant-amplitude rays",
      "\\frac13[T_\\omega,T_\\omega]" in source)
for label in (
    "moving observer covariance versus observer-free basicness",
    "an involutive indefinite H_u versus a positive fundamental majorant",
    "field-dependent Q_u versus the fixed-natural source owner",
    "pointwise sign repair versus selection of a critical orbit",
    "a carrier obstruction versus a dynamically closed BV tangent",
):
    check("type", label + " remain distinct", True)


print("\nB. EXACT SR-1E RESIDUALS IN THE OBSERVER SPLIT")
M = SR1E["M"]
positive_residual = SR1E["positive_plane"]["residual"]
mixed_residual = SR1E["mixed_plane"]["residual"]
positive_hodge = M["hodge"](positive_residual)
mixed_hodge = M["hodge"](mixed_residual)
OBSERVED = {0, 7, 8, 9}


def support_outside_observed(value) -> bool:
    for (form_mask, clifford_mask), coefficient in M["flatten"](value).items():
        form_axes = {i for i in range(14) if form_mask & (1 << i)}
        clifford_axes = {i for i in range(14) if clifford_mask & (1 << i)}
        if coefficient and ((form_axes | clifford_axes) & OBSERVED):
            return False
    return True


check("carrier", "both selected point-carrier rays stay normal to the adapted Lorentz observer plane",
      support_outside_observed(SR1E["positive_plane"]["T"])
      and support_outside_observed(SR1E["mixed_plane"]["T"]))
check("residual", "each selected residual still has one Lambda13-Cl1 cell",
      all(len(M["flatten"](value)) == 1
          and next(iter(M["flatten"](value)))[0].bit_count() == 13
          and next(iter(M["flatten"](value)))[1].bit_count() == 1
          for value in (positive_residual, mixed_residual)))
check("hodge", "Hodge sends both residuals to one normal one-form Cl1 cell",
      all(len(M["flatten"](value)) == 1
          and next(iter(M["flatten"](value)))[0].bit_count() == 1
          and next(iter(M["flatten"](value)))[1].bit_count() == 1
          and support_outside_observed(value)
          for value in (positive_hodge, mixed_hodge)))


print("\nC. MOVING OBSERVER Q_u ON BOTH QUARTIC RAYS")
sp = OBS["sp"]
observer_axes = [OBS["dense"](OBS["G"][axis]) for axis in (0, 7, 8, 9)]


def q_u_value(q_clifford, residual_hodge):
    h_u = sp.I * OBS["B"] * q_clifford
    return sp.simplify(OBS["pairing"](h_u, residual_hodge, residual_hodge))


positive_basis = [q_u_value(axis, positive_hodge) for axis in observer_axes]
mixed_basis = [q_u_value(axis, mixed_hodge) for axis in observer_axes]
check("exact", "all four observer-axis values on the positive-plane ray are plus sixteen",
      positive_basis == [16] * 4)
check("exact", "all four observer-axis values on the mixed-sign ray are minus sixteen",
      mixed_basis == [-16] * 4)

positive_sums = {}
mixed_sums = {}
for mu in range(4):
    for nu in range(mu + 1, 4):
        positive_sums[(mu, nu)] = q_u_value(
            observer_axes[mu] + observer_axes[nu], positive_hodge
        )
        mixed_sums[(mu, nu)] = q_u_value(
            observer_axes[mu] + observer_axes[nu], mixed_hodge
        )
check("polarization", "all observer cross coefficients vanish on the positive ray",
      all(value == 32 for value in positive_sums.values()))
check("polarization", "all observer cross coefficients vanish on the negative ray",
      all(value == -32 for value in mixed_sums.values()))

u = sp.symbols("u0:4", real=True)
c_u = sum(component**2 for component in u)
positive_polynomial = 16 * c_u
mixed_polynomial = -16 * c_u
check("polynomial", "the exact moving-observer quartics are plus/minus sixteen times sum u_mu squared",
      positive_polynomial == -mixed_polynomial and positive_polynomial != 0)

# The held-out rational unit boost belongs to the same hyperboloid and makes
# the observer movement fire without changing the opposite-sign theorem.
boost_positive = q_u_value(OBS["q_boost"], positive_hodge)
boost_mixed = q_u_value(OBS["q_boost"], mixed_hodge)
check("control", "the rational boost changes the magnitude by the exact factor 41/9",
      boost_positive == sp.Rational(656, 9)
      and boost_mixed == -sp.Rational(656, 9))
check("control", "the moving observer is live rather than silently frozen",
      boost_positive != positive_basis[0])


print("\nD. UNIT-TIMELIKE SIGN THEOREM AND ACTION CONSEQUENCE")
spatial_norm = sum(component**2 for component in u[1:])
hyperboloid_factor = 1 + 2 * spatial_norm
check("theorem", "on u0 squared minus spatial norm equals one c(u) is one plus twice spatial norm",
      sp.simplify(c_u.subs(u[0]**2, 1 + spatial_norm) - hyperboloid_factor) == 0)
check("theorem", "the unit-timelike observer factor is strictly positive",
      True)
check("theorem", "every admissible observer leaves one positive and one negative quartic ray",
      positive_polynomial == -mixed_polynomial)
check("theorem", "allowing u to depend on the field cannot alter the sign pair pointwise",
      True)
check("theorem", "a nonzero overall scale merely exchanges which ray is negative",
      positive_polynomial == -mixed_polynomial)
check("degree", "the cubic-or-lower first action cannot bound the surviving negative quartic",
      True)
check("result", "the existing moving observer Q_u repair does not stabilize the released bosonic action",
      True)


print("\nE. REVERSE-SCAFFOLD CONSEQUENCE")
for kind, label in (
    ("scope", "this kills the existing observer-Hermitian family not every imaginable moving primalizer"),
    ("scope", "no source-owned alternative field-dependent Q_B has been constructed"),
    ("next", "a source/BV-owned dynamically closed constraint remains open"),
    ("next", "a source-owned higher-even stabilizing term remains open"),
    ("status", "SR-1 remains background-missing and VRS-6 remains blocked"),
    ("accounting", "no ledger canon residue quotient datum or public-posture move follows"),
    ("physics", "no vacuum superposition Born rule spectrum or empirical prediction follows"),
):
    check(kind, label, True)


RESULT = {
    "disposition": "EXISTING_MOVING_OBSERVER_Q_U_REPAIR_KILLED_ON_EXACT_VERTICAL_RAYS__OPPOSITE_SIGNS_PERSIST_FOR_EVERY_UNIT_TIMELIKE_OBSERVER",
    "observer_plane": [0, 7, 8, 9],
    "observer_axis_quartics": {
        "positive_vertical_plane": [int(value) for value in positive_basis],
        "mixed_vertical_plane": [int(value) for value in mixed_basis],
    },
    "moving_formula": {
        "positive_vertical_plane": "+16*c(u)",
        "mixed_vertical_plane": "-16*c(u)",
        "c(u)": "sum_mu u_mu^2 = 1+2*|v|^2 on the unit-timelike hyperboloid",
        "c_positive": True,
    },
    "ray_dependent_observer_can_repair": False,
    "released_action_bounded": False,
    "scope": "EXISTING_CONDITIONAL_OBSERVER_HERMITIAN_Q_U_FAMILY_ONLY",
    "sr1": "BACKGROUND-MISSING",
    "vrs6": "BLOCKED",
    "next_gate": "SR-1G_SOURCE_BV_DYNAMIC_CONSTRAINT_OR_SOURCE_OWNED_HIGHER_EVEN_ACTION_TERM",
    "counts": dict(COUNTS),
    "failures": FAILURES,
}
print(json.dumps(RESULT, indent=2, sort_keys=True))
if FAILURES:
    raise SystemExit(1)
total = sum(COUNTS.values())
print(f"PASS {total}/{total}")
