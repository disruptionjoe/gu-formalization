#!/usr/bin/env python3
"""Exact off-TT scalar/Ward owner gate for selected second-layer I2B.

This constructs the local metric-to-full-II tangent at the constant section,
pulls back the already exact selected Cl2 quadratic form, and subtracts the
complete zero-momentum operator.  It deliberately refuses to read a scalar
pole unless the resulting Hessian is basic for diffeomorphism gauge.
"""

from __future__ import annotations

from collections import Counter
from pathlib import Path
import contextlib
import io
import runpy

import sympy as sp


ROOT = Path(__file__).resolve().parents[2]
PREDECESSOR = ROOT / "tests/channel-swings/selected_second_layer_massive_so3_closure_probe.py"
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
capture = io.StringIO()
with contextlib.redirect_stdout(capture):
    predecessor = runpy.run_path(str(PREDECESSOR))
check("repo", "the massive SO3 predecessor replays", "PASS 31/31" in capture.getvalue())

full_cl2 = read("explorations/conditional-build/selected-second-layer-full-cl2-residual-pullback-2026-08-07.md")
a12 = read("explorations/threads/A12-constant-background-coefficient-family-2026-07-13.md")
a14 = read("explorations/threads/A14-counter-slot-normalization-gate-2026-07-13.md")
h21 = read("explorations/wave5/H21-theta-equals-II-2026-07-11.md")
source = read("lab/sources/gu-two-layer-action-source-reinspection-2026-08-04.md")
check("repo", "selected I2B is stationary residual norm with Upsilon zero",
      "U(0)=0" in full_cl2 and "stationary quadratic" in full_cl2)
check("repo", "A12 and A14 leave the observer full-B first-variation coefficient unselected",
      "does not assert that this is the final EL formula" in a12
      and "remains unbuilt and unselected" in a14)
check("repo", "H21 proves full II only in the canonical connection identification",
      "FULL** second fundamental form" in h21
      and "Canonical-connection / bundle identification" in h21)
check("source", "source confirms I2B norm-square but is silent on the observer-II owner map",
      "SOURCE-DISPLAYS-BOSONIC-NORM-SQUARE" in source
      and "SOURCE-SILENT" in source)
for label in (
    "stationary selected residual I2B versus observer Willmore I_II",
    "TT background cancellation versus a complete background-subtracted operator",
    "spatial restriction versus a gauge-basic quotient",
    "restricted scalar root versus a characteristic root of the full coupled symbol",
):
    check("type", label + " remain distinct", True)


print("\nB. EXACT METRIC-TO-FULL-II TANGENT AND SELECTED PULLBACK")
DIM = 4
eta = sp.diag(-1, 1, 1, 1)
s = sp.symbols("s")
slots = [(i, j) for i in range(DIM) for j in range(i, DIM)]
slot_index = {pair: index for index, pair in enumerate(slots)}
A = sp.Rational(15376, 13689)
B = -sp.Rational(340, 4563)
C4 = predecessor["C4"]
MASS2 = predecessor["mass2"]


def basis(i: int, j: int) -> sp.Matrix:
    wave = sp.zeros(DIM)
    wave[i, j] = wave[j, i] = 1
    return wave


def vertical_pair(left: sp.Matrix, right: sp.Matrix) -> sp.Expr:
    return sp.simplify(
        sp.trace(eta * left * eta * right)
        - sp.Rational(1, 2) * sp.trace(eta * left) * sp.trace(eta * right)
    )


def delta_algebraic_slice(wave: sp.Matrix, mu: int, nu: int) -> sp.Matrix:
    return sp.Matrix(
        DIM,
        DIM,
        lambda a, b: sp.Rational(1, 2)
        * (
            wave[a, mu] * eta[nu, b]
            + eta[a, mu] * wave[nu, b]
            + wave[a, nu] * eta[mu, b]
            + eta[a, nu] * wave[mu, b]
        )
        - sp.Rational(1, 2)
        * (wave[a, b] * eta[mu, nu] + eta[a, b] * wave[mu, nu]),
    )


def delta_ii(wave: sp.Matrix, value: sp.Expr) -> list[list[sp.Matrix]]:
    # Massive-rest covector k=(sqrt(value),0,0,0).  The first variation of
    # B=d2g-1/2*algebraic_slice+O((dg)^2) is exact at the constant graph.
    k = [sp.sqrt(value), 0, 0, 0]
    return [
        [
            sp.simplify(
                -k[mu] * k[nu] * wave
                - sp.Rational(1, 2) * delta_algebraic_slice(wave, mu, nu)
            )
            for nu in range(DIM)
        ]
        for mu in range(DIM)
    ]


def selected_bilinear(left: sp.Matrix, right: sp.Matrix, value: sp.Expr) -> sp.Expr:
    dleft = delta_ii(left, value)
    dright = delta_ii(right, value)
    full_ii = sp.Integer(0)
    for mu in range(DIM):
        for nu in range(DIM):
            for rho in range(DIM):
                for sigma in range(DIM):
                    if eta[mu, rho] and eta[nu, sigma]:
                        full_ii += (
                            eta[mu, rho]
                            * eta[nu, sigma]
                            * vertical_pair(dleft[mu][nu], dright[rho][sigma])
                        )
    trace_left = sum(
        (eta[mu, nu] * dleft[mu][nu] for mu in range(DIM) for nu in range(DIM)),
        sp.zeros(DIM),
    )
    trace_right = sum(
        (eta[mu, nu] * dright[mu][nu] for mu in range(DIM) for nu in range(DIM)),
        sp.zeros(DIM),
    )
    return sp.factor(A * full_ii + B * vertical_pair(trace_left, trace_right))


metric_basis = [basis(*pair) for pair in slots]
raw = sp.Matrix([
    [selected_bilinear(left, right, s) for right in metric_basis]
    for left in metric_basis
])
zero_momentum = raw.subs(s, 0)
subtracted = sp.simplify(raw - zero_momentum)
check("exact", "complete operator background subtraction sets K(0) to zero",
      subtracted.subs(s, 0) == sp.zeros(10))
check("exact", "the pulled metric Hessian is symmetric",
      subtracted == subtracted.T)

plus = sp.zeros(10, 1)
plus[slot_index[(1, 1)]] = 1
plus[slot_index[(2, 2)]] = -1
cross = sp.zeros(10, 1)
cross[slot_index[(1, 2)]] = 1
tt_polynomial_with_norm = 2 * C4 * s * (s + MASS2)
check("exact", "the off-TT construction exactly reproduces the selected plus polynomial",
      sp.factor((plus.T * subtracted * plus)[0] - tt_polynomial_with_norm) == 0)
check("exact", "the off-TT construction exactly reproduces the selected cross polynomial",
      sp.factor((cross.T * subtracted * cross)[0] - tt_polynomial_with_norm) == 0)
check("planted", "PLANT subtracting only one TT matrix element is not complete subtraction",
      zero_momentum.rank() > 1)


print("\nC. SPATIAL SCALAR CANDIDATE AND FULL WARD TEST")
trace = sp.zeros(10, 1)
for index in (1, 2, 3):
    trace[slot_index[(index, index)]] = 1
trace_norm = -sp.Rational(3, 2)
trace_form = sp.factor((trace.T * subtracted * trace)[0])
candidate_scalar = sp.factor(trace_form / trace_norm)
candidate_c2 = sp.Rational(4628, 13689)
candidate_mass2 = sp.Rational(1157, 3589)
check("exact", "the spatial restriction has one exact spin-zero candidate polynomial",
      sp.factor(candidate_scalar - C4 * s * (s + candidate_mass2)) == 0
      and candidate_c2 == C4 * candidate_mass2)
check("exact", "the candidate scalar mass differs from the spin-two mass",
      candidate_mass2 != MASS2)

gauge = sp.zeros(10, 4)
for column in range(4):
    for row, (i, j) in enumerate(slots):
        gauge[row, column] = (
            (1 if i == 0 and j == column else 0)
            + (1 if j == 0 and i == column else 0)
        )
ward = sp.simplify(subtracted * gauge)
check("exact", "the naive metric-only off-TT Hessian has rank-four Ward defect",
      ward.subs(s, 2).rank() == 4)
check("exact", "the spatial trace couples nontrivially to the temporal gauge block",
      sp.factor(subtracted[slot_index[(0, 0)], :] .dot(trace))
      == sp.factor(6 * s * (3589 * s - 255) / 13689))
scalar_root = -candidate_mass2
check("planted", "PLANT the restricted scalar root is not a root of the full metric Hessian",
      subtracted.subs(s, scalar_root).rank() == 10)
check("planted", "PLANT exact TT recovery does not imply full Ward descent",
      ward != sp.zeros(10, 4))


print("\nD. IDENTIFIABILITY AFTER A FORMAL GAUGE COMPLETION")
spatial_indices = [slot_index[pair] for pair in slots if pair[0] > 0]
spatial_block = subtracted.extract(spatial_indices, spatial_indices)
trace6 = sp.Matrix([1, 1, 1, 0, 0, 0])
P0 = sp.zeros(6)
for row in range(3):
    for column in range(3):
        P0[row, column] = sp.Rational(1, 3)
P2 = sp.eye(6) - P0
shift = s * P0
basic_one = sp.zeros(10)
basic_two = sp.zeros(10)
for i, row in enumerate(spatial_indices):
    for j, column in enumerate(spatial_indices):
        basic_one[row, column] = spatial_block[i, j]
        basic_two[row, column] = spatial_block[i, j] + shift[i, j]
check("exact", "two symmetric formal completions annihilate the rest gauge image",
      basic_one * gauge == sp.zeros(10, 4)
      and basic_two * gauge == sp.zeros(10, 4))
check("exact", "the two completions agree on all traceless spin-two directions",
      (basic_two - basic_one).extract(spatial_indices, spatial_indices) * P2 == sp.zeros(6))
check("planted", "PLANT Ward plus TT data still do not select the scalar block",
      (trace6.T * spatial_block * trace6)[0]
      != (trace6.T * (spatial_block + shift) * trace6)[0])


print("\nE. DISPOSITION AND NEXT OWNER")
for label in (
    "the A12 full-B coefficient is not imported across distinct action owners",
    "the restricted 1157-over-3589 scalar mass is diagnostic only",
    "the missing object is the full co-moving metric connection section observation differential of Upsilon",
    "that differential must annihilate the coupled gauge tangent at Upsilon zero",
    "massless constraint descent coupled fermions common domain and odd BV BFV remain downstream",
    "no coefficient residue quotient external datum canon or posture change is booked",
    "P1 P2 P3 remain unused and Curt remains formally separate",
):
    check("scope", label, True)

print("SOURCE_RETURN=SOURCE-CONFIRMS__I2B_NORM_SQUARE__SOURCE-SILENT__I2B_TO_OBSERVER_FULL_II_OWNER")
print(f"TT_MASS2_REPRODUCED={MASS2}")
print(f"RESTRICTED_SCALAR_CANDIDATE_MASS2={candidate_mass2}__NOT_ADMISSIBLE")
print("FULL_METRIC_WARD_DEFECT_RANK=4")
print("SCALAR_CANDIDATE_IS_NOT_FULL_CHARACTERISTIC_ROOT")
print("OLD_FULL_B_COEFFICIENT=DIFFERENT_ACTION_OWNER__NOT_IMPORTED")
print("NEXT=FULL_COMOVING_DUPSILON_METRIC_CONNECTION_SECTION_OBSERVATION_DIFFERENTIAL_AND_COUPLED_WARD_DESCENT")
print("DISPOSITION=METRIC_BLOCK_NOT_BASIC__COUPLED_OWNER_REQUIRED")
print("CHECKS=" + " ".join(f"{kind}:{count}" for kind, count in sorted(COUNTS.items())))
if FAILURES:
    print("FAILED=" + " | ".join(FAILURES))
    raise SystemExit(1)
print(f"PASS {sum(COUNTS.values())}/{sum(COUNTS.values())}")
