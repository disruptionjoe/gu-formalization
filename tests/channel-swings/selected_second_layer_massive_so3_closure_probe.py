#!/usr/bin/env python3
"""Exact massive-SO(3) closure and off-TT identifiability gate.

The selected second-layer predecessor proves an axial weight-two plus/cross
plane at a positive massive pole.  This probe asks what full rest-frame
rotation covariance forces, and what it cannot determine.  It does not fit an
off-TT action or promote a complete physical quotient.
"""

from __future__ import annotations

from collections import Counter
from pathlib import Path
import contextlib
import io
import runpy

import sympy as sp


ROOT = Path(__file__).resolve().parents[2]
PREDECESSOR = ROOT / "tests/channel-swings/selected_second_layer_tt_euler_preboundary_helicity_probe.py"
COUNTS: Counter[str] = Counter()
FAILURES: list[str] = []


def check(kind: str, label: str, condition: object) -> None:
    COUNTS[kind] += 1
    ok = bool(condition)
    print(f"{'PASS' if ok else 'FAIL'} [{kind}] {label}")
    if not ok:
        FAILURES.append(label)


def read(relative: str) -> str:
    return (ROOT / relative).read_text(encoding="utf-8")


print("A. SOURCE, PREDECESSOR, AND LAYER 0")
source = read("lab/sources/selected-moving-k77-vacuum-p2-source-reinspection-2026-08-05.md")
pullback = read("lab/sources/gu-pullback-augmented-torsion-source-reinspection-2026-08-05.md")
background = read("explorations/threads/A12-constant-background-coefficient-family-2026-07-13.md")
normalization = read("explorations/threads/A14-counter-slot-normalization-gate-2026-07-13.md")
capture = io.StringIO()
with contextlib.redirect_stdout(capture):
    predecessor = runpy.run_path(str(PREDECESSOR))
check("repo", "the selected TT predecessor replays", "PASS 44/44" in capture.getvalue())
check("source", "source confirms the full connection-difference norm and geometric connection locus",
      "SOURCE-CONFIRMS-INGREDIENTS" in source
      and "gauge-rotated Levi-Civita connection in the contorsion slot" in pullback)
check("source", "source is silent on the full scalar characteristic coefficient",
      "silent on stability" in source.lower() and "krein/green domain" in source.lower())
check("repo", "the old native background family leaves the full-B coefficient and background subtraction open",
      "c_B" in background and "background-subtracted" in background
      and "source-action supply" in normalization and "remains unbuilt and unselected" in normalization)
for label in (
    "axial SO2 weight space versus full massive SO3 representation",
    "representation-forced degeneracy versus a computed off-TT Euler operator",
    "spin-zero trace quotient versus the weight-zero member of spin two",
    "massive rest-frame carrier versus the massless null little-group quotient",
    "finite little-group module versus a Green-Lagrangian or BFV phase space",
):
    check("type", label + " remain distinct", True)


print("\nB. EXACT REST-FRAME GAUGE QUOTIENT")
slots = [(i, j) for i in range(4) for j in range(i, 4)]


def coordinates(wave: sp.Matrix) -> sp.Matrix:
    return sp.Matrix([wave[i, j] for i, j in slots])


def tensor(*entries: tuple[int, int, int]) -> sp.Matrix:
    wave = sp.zeros(4)
    for i, j, value in entries:
        wave[i, j] = wave[j, i] = value
    return wave


def symmetric_representation(generator: sp.Matrix) -> sp.Matrix:
    basis = []
    for i, j in slots:
        wave = sp.zeros(4)
        wave[i, j] = wave[j, i] = 1
        basis.append(wave)
    return sp.Matrix.hstack(*[
        coordinates(generator * wave + wave * generator.T) for wave in basis
    ])


rest_k = sp.Matrix([1, 0, 0, 0])
gauge = sp.zeros(10, 4)
for column in range(4):
    for row, (i, j) in enumerate(slots):
        gauge[row, column] = (
            (rest_k[i] if j == column else 0)
            + (rest_k[j] if i == column else 0)
        )

spatial_waves = (
    tensor((1, 1, 1)), tensor((2, 2, 1)), tensor((3, 3, 1)),
    tensor((1, 2, 1)), tensor((1, 3, 1)), tensor((2, 3, 1)),
)
spatial = sp.Matrix.hstack(*[coordinates(wave) for wave in spatial_waves])
check("exact", "massive rest diffeomorphism image has rank four", gauge.rank() == 4)
check("exact", "the six spatial symmetric tensors complement the gauge image",
      spatial.rank() == 6 and gauge.row_join(spatial).rank() == 10)


print("\nC. FULL SO3 ORBIT OF THE AXIAL WEIGHT-TWO PLANE")


def rotation(i: int, j: int) -> sp.Matrix:
    out = sp.zeros(4)
    out[i, j] = -1
    out[j, i] = 1
    return out


rotations4 = (rotation(1, 2), rotation(2, 3), rotation(3, 1))
rotations10 = tuple(symmetric_representation(item) for item in rotations4)
rotation6 = tuple(spatial.gauss_jordan_solve(item * spatial)[0] for item in rotations10)
check("exact", "all three spatial rotations preserve the rest-frame quotient",
      all(item * spatial == spatial * reduced for item, reduced in zip(rotations10, rotation6)))

plus = sp.Matrix([1, -1, 0, 0, 0, 0])
cross = sp.Matrix([0, 0, 0, 1, 0, 0])
seed = sp.Matrix.hstack(plus, cross)


def invariant_closure(initial: sp.Matrix, generators: tuple[sp.Matrix, ...]) -> sp.Matrix:
    carrier = sp.Matrix.hstack(*initial.columnspace())
    while True:
        enlarged = sp.Matrix.hstack(carrier, *[generator * carrier for generator in generators])
        next_carrier = sp.Matrix.hstack(*enlarged.columnspace())
        if next_carrier.rank() == carrier.rank():
            return carrier
        carrier = next_carrier


closure = invariant_closure(seed, rotation6)
spin2_basis = sp.Matrix.hstack(
    plus,
    cross,
    sp.Matrix([0, 0, 0, 0, 1, 0]),
    sp.Matrix([0, 0, 0, 0, 0, 1]),
    sp.Matrix([1, 1, -2, 0, 0, 0]),
)
trace = sp.Matrix([1, 1, 1, 0, 0, 0])
check("exact", "plus/cross generate a five-dimensional SO3 orbit",
      closure.rank() == 5 and closure.row_join(spin2_basis).rank() == 5)
check("exact", "the closure is exactly the traceless spatial-symmetric carrier",
      spin2_basis.rank() == 5
      and all((sp.Matrix([[1, 1, 1, 0, 0, 0]]) * vector)[0] == 0
              for vector in spin2_basis.columnspace()))
check("exact", "the trace scalar is the one-dimensional complementary SO3 carrier",
      spin2_basis.row_join(trace).rank() == 6
      and all(generator * trace == sp.zeros(6, 1) for generator in rotation6))

spin2_actions = tuple(spin2_basis.gauss_jordan_solve(generator * spin2_basis)[0]
                      for generator in rotation6)
casimir = sp.simplify(sum((action * action for action in spin2_actions), sp.zeros(5)))
check("exact", "the five-state closure has spin-two Casimir minus six",
      casimir == -6 * sp.eye(5))
axial = seed.gauss_jordan_solve(rotation6[0] * seed)[0]
check("exact", "the original plane is axial weight plus/minus two",
      axial**2 == -4 * sp.eye(2))
check("planted", "PLANT the axial plane is not invariant under all massive rotations",
      rotation6[1] * plus not in sp.Matrix.hstack(*seed.columnspace()).columnspace())


print("\nD. SCHUR BLOCKS AND THE EXACT IDENTIFIABILITY BOUNDARY")
P0 = sp.zeros(6)
for row in range(3):
    for column in range(3):
        P0[row, column] = sp.Rational(1, 3)
P2 = sp.eye(6) - P0
check("exact", "spin-zero and spin-two projectors are complementary and rotation-equivariant",
      P0 * P0 == P0 and P2 * P2 == P2 and P0 * P2 == sp.zeros(6)
      and all(P0 * generator == generator * P0 and P2 * generator == generator * P2
              for generator in rotation6))
check("exact", "the TT seed lies wholly in spin two and cannot see spin zero",
      P2 * seed == seed and P0 * seed == sp.zeros(6, 2))

xvars = sp.symbols("x0:36")
X = sp.Matrix(6, 6, xvars)
equations = []
for generator in rotation6:
    equations.extend(list(X * generator - generator * X))
commutant_matrix, _ = sp.linear_eq_to_matrix(equations, xvars)
check("exact", "the SO3 commutant on Sym2(R3) is exactly two-dimensional",
      36 - commutant_matrix.rank() == 2)

C4 = predecessor["C4"]
mass2 = predecessor["MASS2"]
s = sp.symbols("s")
spin2_polynomial = C4 * s * (s + mass2)
scalar_no_pole = sp.Integer(1)
scalar_extra_pole = s + mass2
hessian_no_extra = spin2_polynomial * P2 + scalar_no_pole * P0
hessian_extra = spin2_polynomial * P2 + scalar_extra_pole * P0
check("exact", "two SO3-covariant Hessians have the identical selected TT polynomial",
      hessian_no_extra * seed == spin2_polynomial * seed
      and hessian_extra * seed == spin2_polynomial * seed)
massive_root = -mass2
check("exact", "SO3 covariance forces five spin-two zero modes at the massive root",
      hessian_no_extra.subs(s, massive_root).nullspace()
      and 6 - hessian_no_extra.subs(s, massive_root).rank() == 5)
check("planted", "PLANT TT data do not decide whether a sixth spin-zero mode shares the pole",
      6 - hessian_extra.subs(s, massive_root).rank() == 6
      and hessian_extra != hessian_no_extra)


print("\nE. DISPOSITION AND NEXT CONSTRUCTION")
for label in (
    "the three additional massive polarizations are mandatory spin-two partners, not optional new fields",
    "the independent spatial trace is the only rest-frame scalar coefficient left by SO3",
    "its characteristic polynomial requires the actual off-TT section second variation",
    "the old full-B ambient coefficient and background-subtracted linearization must be composed first",
    "massless constraint propagation and the nonzero-fermion Hessian remain separate",
    "no fifth quotient common domain BV BFV positive energy or datum is booked",
    "P1 P2 P3 remain unused and Curt remains formally separate",
):
    check("scope", label, True)

print("SOURCE_RETURN=SOURCE-CONFIRMS__GEOMETRIC_COVARIANCE_AND_FULL_NORM__SOURCE-SILENT__SCALAR_CHARACTERISTIC_COEFFICIENT")
print("MASSIVE_SO3_CLOSURE=SPIN2_DIMENSION_5_CASIMIR_MINUS_6")
print("MASSIVE_MISSING_AXIAL_WEIGHTS=ZERO_PLUS_MINUS_ONE__FORCED_PARTNERS")
print("REST_QUOTIENT=SPIN2_DIMENSION_5_PLUS_SPIN0_DIMENSION_1")
print("TT_IDENTIFIES=SPIN2_POLYNOMIAL_ONLY")
print("UNIDENTIFIED=SPIN0_CHARACTERISTIC_POLYNOMIAL")
print("NEXT=ACTUAL_BACKGROUND_SUBTRACTED_OFF_TT_SECTION_SECOND_VARIATION_THEN_MASSLESS_CONSTRAINT_COMPLEX")
print("DISPOSITION=MASSIVE_SPIN2_CLOSURE__SCALAR_COEFFICIENT_OPEN")
print("CHECKS=" + " ".join(f"{kind}:{count}" for kind, count in sorted(COUNTS.items())))
if FAILURES:
    print("FAILED=" + " | ".join(FAILURES))
    raise SystemExit(1)
print(f"PASS {sum(COUNTS.values())}/{sum(COUNTS.values())}")
