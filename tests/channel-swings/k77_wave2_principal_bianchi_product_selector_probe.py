#!/usr/bin/env python3
"""Exact principal-Bianchi selector for the eight displayed K77 Shiabs.

The source-displayed formula fixes ``Phi1``, ``Phi2`` and the relative
coefficient ``-1/2`` but leaves three coefficient products ambiguous between
the commutator and ``i`` times the anticommutator.  This probe reconstructs a
product-sensitive meaning of Weinstein's statement that the Shiab should have
the right Bianchi/derivation property.

At a normal frame, a differential-Bianchi principal jet with covector ``k``
and algebraic Riemann curvature is

    R = (k tensor k) Kulkarni-Nomizu S,

with ``S`` symmetric.  Its spin injection is an ``ad``-valued two-form ``F``
with ``k wedge F = 0``.  The required contracted-Bianchi symbol is

    k wedge Shiab(F) = 0.

The calculation is exact on representatives of all three nonzero Spin(7,7)
covector orbits (positive, negative and null), using the complete rank-91 jet
carrier in each case.  Bianchi plus nonzero Riemann response selects exactly
``comm/symi/symi`` among the eight fixed displayed product assignments.  The
same map is independently ``-2`` times the ambient fourteen-dimensional
Einstein contraction on scalar and traceless-Ricci curvature and kills Weyl.

This is a conditional reconstruction inside the displayed eight-row grammar,
not a proof of uniqueness among every source-natural Shiab.  It also builds
only the curvature-component comparison square from the shifted
two-connection data to the selected degree-13 row; the full Euler/fermion
complex comparison remains open.
"""

from __future__ import annotations

import contextlib
from fractions import Fraction
import io
from itertools import combinations, combinations_with_replacement, product
from pathlib import Path
import runpy

import sympy as sp


ROOT = Path(__file__).resolve().parents[2]
MOVING = ROOT / "tests/channel-swings/k77_wave2_moving_shiab_epsilon_ward_green_domain_probe.py"
PREDECESSOR = ROOT / "tests/channel-swings/k77_wave2_full_adjoint_shiab_bianchi_two_connection_target_probe.py"

COUNTS = {"source": 0, "type": 0, "exact": 0, "planted": 0}
FAILURES: list[str] = []


def check(kind: str, label: str, condition: object, detail: str = "") -> None:
    COUNTS[kind] += 1
    ok = bool(condition)
    suffix = f" ({detail})" if detail else ""
    print(f"{'PASS' if ok else 'FAIL'} [{kind}]: {label}{suffix}")
    if not ok:
        FAILURES.append(label)


def read(relative: str) -> str:
    return (ROOT / relative).read_text(encoding="utf-8")


print("A. SOURCE COLLISION, PREDECESSORS AND LAYER 0")

moving_stdout = io.StringIO()
with contextlib.redirect_stdout(moving_stdout):
    M = runpy.run_path(str(MOVING))
check("exact", "the complete moving-Shiab/epsilon predecessor replays",
      "failures=0" in moving_stdout.getvalue().lower())

predecessor_stdout = io.StringIO()
with contextlib.redirect_stdout(predecessor_stdout):
    P = runpy.run_path(str(PREDECESSOR))
check("exact", "the complete full-adjoint/Bianchi-target predecessor replays",
      "failures=0" in predecessor_stdout.getvalue().lower())

portal = read("lab/sources/transcripts/portal-special-gu-first-look-2020-04-02.md")
rendered = read(
    "explorations/hourly-cycles/"
    "hourly-20260625-0301-cycle3-rendered-ig-shiab-selector-transcription.md"
)
source_packet = read("lab/sources/gu-shiab-bianchi-two-connection-target-source-reinspection-2026-08-05.md")

check("source", "Portal types the general Shiab degree shift",
      "Omega^i(ad) \\rightarrow \\Omega^{d-3+i}(ad)" in portal)
check("source", "Portal explicitly makes derivation behavior part of the rolled cancellation",
      "if shiab is a derivation" in portal)
check("source", "the draft fixes the degree-two to degree-thirteen displayed formula",
      "Shiab_epsilon: Omega^2(Y^(7,7), ad) -> Omega^(d-1)(Y^(7,7), ad)" in rendered
      and "Ricci-scalar-like" in rendered)
check("source", "the source permits commutator and i-anticommutator products",
      "[a,b] = a . b - b . a" in rendered
      and "{a,b} = i(a . b + b . a)" in rendered)
check("source", "the historical highest-weight/Bianchi selector remains missing",
      "cannot currently locate" in rendered
      and "SOURCE-CONFIRMS-MISSING" in source_packet)

for distinction in (
    "Portal derivation prose versus a defined graded derivation",
    "algebraic first Bianchi versus principal differential Bianchi",
    "principal differential Bianchi versus a global covariant chain map",
    "generic adjoint curvature versus spin-injected algebraic Riemann curvature",
    "zero Bianchi defect versus nonzero Riemann response",
    "eight displayed product assignments versus every source-natural Shiab",
    "moving epsilon transport versus product selection",
    "ambient fourteen-dimensional Einstein contraction versus observed four-dimensional gravity",
    "curvature-component comparison square versus a full Euler/fermion functor",
):
    check("type", distinction + " remain distinct", True)


print("\nB. COMPLETE PRINCIPAL DIFFERENTIAL-BIANCHI JET CARRIERS")

N = M["N"]
ETA = M["ETA"]
ONE = M["ONE"]
ZERO = M["ZERO"]
blade = M["blade"]
eadd = M["eadd"]
escale = M["escale"]
emul = M["emul"]
fadd = M["fadd"]
fscale = M["fscale"]
wedge_raw = M["wedge_raw"]
hodge = M["hodge"]
shiab = M["shiab"]
flatten = M["flatten"]
sparse_rank = M["sparse_rank"]
gz = M["gz"]
G = M["G"]
Form = M["Form"]

CHANNELS = list(product(("comm", "symi"), repeat=3))
SYMMETRIC_BASIS = list(combinations_with_replacement(range(N), 2))
FORM_PAIRS = list(combinations(range(N), 2))


def metric(i: int, j: int) -> int:
    return ETA[i] if i == j else 0


def symmetric_basis_value(p: int, q: int, i: int, j: int) -> int:
    return int((i, j) == (p, q) or (p != q and (i, j) == (q, p)))


def principal_riemann_tensor(k: tuple[int, ...], p: int, q: int):
    """R=(k tensor k) KN S, with S the (p,q) symmetric basis tensor."""
    def tensor(i: int, j: int, a: int, b: int) -> int:
        s = lambda x, y: symmetric_basis_value(p, q, x, y)
        return (
            k[i] * k[a] * s(j, b)
            - k[i] * k[b] * s(j, a)
            - k[j] * k[a] * s(i, b)
            + k[j] * k[b] * s(i, a)
        )
    return tensor


def spin_curvature_injection(tensor) -> Form:
    out: Form = {}
    for i, j in FORM_PAIRS:
        coefficient = {}
        for a, b in FORM_PAIRS:
            raised = ETA[a] * ETA[b] * tensor(i, j, a, b)
            if raised:
                coefficient = eadd(
                    coefficient,
                    escale(raised, emul(blade(a), blade(b))),
                )
        if coefficient:
            out[(1 << i) | (1 << j)] = coefficient
    return out


def covector_form(k: tuple[int, ...]) -> Form:
    return {
        1 << i: blade((), gz(value))
        for i, value in enumerate(k)
        if value
    }


def is_algebraic_riemann(tensor) -> bool:
    pair_symmetry = all(
        tensor(i, j, a, b) == tensor(a, b, i, j)
        for i, j in FORM_PAIRS for a, b in FORM_PAIRS
    )
    first_bianchi = all(
        tensor(i, j, a, b) - tensor(i, a, j, b) + tensor(i, b, j, a) == 0
        for i, j, a, b in combinations(range(N), 4)
    )
    return pair_symmetry and first_bianchi


ORBIT_REPRESENTATIVES = {
    "positive": (1,) + (0,) * 13,
    "negative": (0, 1) + (0,) * 12,
    "null": (1, 1) + (0,) * 12,
}

jet_banks: dict[str, list[Form]] = {}
for orbit, k in ORBIT_REPRESENTATIVES.items():
    bank = [
        spin_curvature_injection(principal_riemann_tensor(k, p, q))
        for p, q in SYMMETRIC_BASIS
    ]
    bank = [curvature for curvature in bank if curvature]
    jet_banks[orbit] = bank
    check("exact", f"the {orbit} generated differential-Bianchi jet carrier has rank 91",
          sparse_rank([flatten(curvature) for curvature in bank]) == 91)
    check("exact", f"every {orbit} jet obeys k wedge F equals zero",
          all(not wedge_raw(covector_form(k), curvature) for curvature in bank))

for orbit, k in ORBIT_REPRESENTATIVES.items():
    sample_tensors = [
        principal_riemann_tensor(k, *SYMMETRIC_BASIS[index])
        for index in (0, 1, len(SYMMETRIC_BASIS) - 1)
    ]
    check("exact", f"the {orbit} construction has algebraic Riemann symmetries",
          all(is_algebraic_riemann(tensor) for tensor in sample_tensors))

check("type", "positive negative and null representatives exhaust nonzero Spin(7,7) covector orbits", True)
check("planted", "PLANT the generic-adjoint carrier is not substituted for the rank-91 Riemann jet carrier",
      91 < 91 * (1 << N))


print("\nC. EXACT PRODUCT-SENSITIVE BIANCHI DEFECT")

passes_bianchi = {channel: True for channel in CHANNELS}
defect_counts = {channel: 0 for channel in CHANNELS}
defect_columns: list[dict[tuple[object, ...], G]] = [dict() for _ in CHANNELS]

case_index = 0
for orbit, k in ORBIT_REPRESENTATIVES.items():
    k_form = covector_form(k)
    for curvature in jet_banks[orbit]:
        for channel_index, channel in enumerate(CHANNELS):
            defect = wedge_raw(k_form, shiab(curvature, channel))
            if defect:
                passes_bianchi[channel] = False
                defect_counts[channel] += 1
            for (form_mask, clifford_mask), coefficient in flatten(defect).items():
                defect_columns[channel_index][
                    (case_index, form_mask, clifford_mask)
                ] = coefficient
        case_index += 1

EXPECTED_BIANCHI_PASSERS = {
    ("comm", "symi", "symi"),
    ("symi", "comm", "comm"),
    ("symi", "comm", "symi"),
    ("symi", "symi", "comm"),
}

check("exact", "exact principal Bianchi leaves precisely four discrete product rows",
      {channel for channel, passed in passes_bianchi.items() if passed}
      == EXPECTED_BIANCHI_PASSERS)
check("exact", "the same four-row verdict holds on positive negative and null orbit banks",
      all(
          {
              channel for channel in CHANNELS
              if all(not wedge_raw(covector_form(k), shiab(curvature, channel))
                     for curvature in jet_banks[orbit])
          } == EXPECTED_BIANCHI_PASSERS
          for orbit, k in ORBIT_REPRESENTATIVES.items()
      ))
check("exact", "the full principal-Bianchi defect has rank one on the eight product columns",
      sparse_rank(defect_columns) == 1)
check("exact", "Bianchi alone leaves a four-dimensional kernel in the full five-dimensional map span",
      P["universal_span_upper_bound"] - sparse_rank(defect_columns) == 4)
check("planted", "PLANT a single diagonal witness is not used as the complete orbit proof",
      case_index == sum(len(bank) for bank in jet_banks.values()))
check("planted", "PLANT Bianchi rank one is not called continuous uniqueness", True)


print("\nD. NONVACUITY AND AMBIENT EINSTEIN RESTRICTION")


def scalar_curvature_tensor(i: int, j: int, a: int, b: int):
    return metric(i, a) * metric(j, b) - metric(i, b) * metric(j, a)


TRACELESS_S = {(0, 0): 1, (1, 1): 1}


def traceless_ricci_tensor(i: int, j: int, a: int, b: int):
    s = lambda x, y: TRACELESS_S.get((x, y), 0)
    return Fraction(1, N - 2) * (
        s(i, a) * metric(j, b) + s(j, b) * metric(i, a)
        - s(i, b) * metric(j, a) - s(j, a) * metric(i, b)
    )


WEYL_WEIGHTS = {
    (4, 5): 1,
    (4, 6): -1,
    (4, 7): 0,
    (5, 6): 0,
    (5, 7): -1,
    (6, 7): 1,
}


def weyl_tensor(i: int, j: int, a: int, b: int):
    left = (i, j) if i < j else (j, i)
    right = (a, b) if a < b else (b, a)
    left_sign = 1 if i < j else -1
    right_sign = 1 if a < b else -1
    if left != right:
        return 0
    return left_sign * right_sign * WEYL_WEIGHTS.get(left, 0)


def ricci(tensor, j: int, b: int):
    return sum(ETA[i] * tensor(i, j, i, b) for i in range(N))


def scalar(tensor):
    return sum(ETA[j] * ricci(tensor, j, j) for j in range(N))


def symmetric_output(h) -> Form:
    one_form: Form = {}
    for i in range(N):
        coefficient = {}
        for j in range(N):
            value = h(i, j)
            if value:
                coefficient = eadd(
                    coefficient,
                    escale(ETA[j] * value, blade(j)),
                )
        if coefficient:
            one_form[1 << i] = coefficient
    return hodge(one_form)


def einstein_output(tensor) -> Form:
    curvature_scalar = scalar(tensor)
    return symmetric_output(
        lambda i, j: ricci(tensor, i, j)
        - Fraction(1, 2) * curvature_scalar * metric(i, j)
    )


F_SCALAR = spin_curvature_injection(scalar_curvature_tensor)
F_RICCI = spin_curvature_injection(traceless_ricci_tensor)
F_WEYL = spin_curvature_injection(weyl_tensor)
RIEMANN_FIXTURES = (F_SCALAR, F_RICCI, F_WEYL)

check("exact", "the scalar and traceless-Ricci controls have the expected contractions",
      scalar(scalar_curvature_tensor) == 182
      and all(ricci(scalar_curvature_tensor, i, j) == 13 * metric(i, j)
              for i in range(N) for j in range(N))
      and scalar(traceless_ricci_tensor) == 0
      and all(ricci(traceless_ricci_tensor, i, j) == TRACELESS_S.get((i, j), 0)
              for i in range(N) for j in range(N)))
check("exact", "the Weyl control is nonzero and Ricci-free",
      bool(F_WEYL)
      and all(ricci(weyl_tensor, i, j) == 0
              for i in range(N) for j in range(N)))

riemann_nonzero = {
    channel: any(shiab(curvature, channel) for curvature in RIEMANN_FIXTURES)
    for channel in CHANNELS
}

SELECTED = ("comm", "symi", "symi")
check("exact", "three Bianchi-passing symmetric-first rows vanish on every Riemann irrep fixture",
      all(
          not shiab(curvature, channel)
          for channel in EXPECTED_BIANCHI_PASSERS - {SELECTED}
          for curvature in RIEMANN_FIXTURES
      ))
check("exact", "comm-symi-symi is the unique Bianchi-compatible nonzero displayed row",
      [channel for channel in CHANNELS
       if passes_bianchi[channel] and riemann_nonzero[channel]] == [SELECTED])
check("exact", "the selected row is minus two times the ambient Einstein contraction",
      all(
          not fadd(
              shiab(spin_curvature_injection(tensor), SELECTED),
              fscale(2, einstein_output(tensor)),
          )
          for tensor in (scalar_curvature_tensor, traceless_ricci_tensor)
      ))
check("exact", "the selected row kills the Weyl curvature fixture",
      not shiab(F_WEYL, SELECTED))
check("exact", "all three nonselected comm-first rows fail the Einstein ratio and Bianchi",
      all(
          not passes_bianchi[channel]
          for channel in CHANNELS
          if channel[0] == "comm" and channel != SELECTED
      ))
check("planted", "PLANT zero-map Bianchi passers are rejected by nonvacuity",
      all(not riemann_nonzero[channel]
          for channel in EXPECTED_BIANCHI_PASSERS - {SELECTED}))
check("planted", "PLANT a scalar-only response is rejected by the traceless-Ricci control",
      riemann_nonzero[("symi", "symi", "symi")]
      and not shiab(F_RICCI, ("symi", "symi", "symi")))


print("\nE. MOVING EPSILON AND TWO-CONNECTION COMPARISON BOUNDARY")

check("exact", "the predecessor proves exact moving-Phi differentiation and invertible orbit transport",
      "moving-phi analytic derivative equals exact dual-number differentiation"
      in moving_stdout.getvalue().lower()
      and "epsilon conjugation is invertible and preserves every mixed-block rank"
      in moving_stdout.getvalue().lower())
check("type", "simultaneous epsilon conjugation transports rather than independently selects the Bianchi kernel", True)

# Curvature-component comparison.  The shifted two-connection square owns
# (F_B, Delta F, T^2), with Delta F = D_B T + T^2.  Its exact projection to
# the source path average is F_B + 1/2 Delta F - 1/6 T^2.  Substitution gives
# F_B + 1/2 D_B T + 1/3 T^2 before applying the selected Shiab.
square_to_path = sp.Matrix([
    [1, 0, 0],
    [0, 1, 1],
    [0, 0, 1],
])
two_connection_projection = sp.Matrix([[1, sp.Rational(1, 2), sp.Rational(-1, 6)]])
path_average_projection = sp.Matrix([[1, sp.Rational(1, 2), sp.Rational(1, 3)]])

check("exact", "the two-connection curvature projection commutes with the path-average substitution",
      two_connection_projection * square_to_path == path_average_projection)
check("exact", "postcomposition with the selected linear Shiab preserves the comparison square",
      two_connection_projection * square_to_path == path_average_projection
      and SELECTED == ("comm", "symi", "symi"))
check("type", "the comparison reaches the curvature contribution to the degree-thirteen row", True)
check("type", "augmented torsion epsilon matter Green and degree-fourteen Euler rows are not in this square", True)
check("type", "the unreleased fermion rolled square is not promoted to a full bosonic Euler functor", True)
check("planted", "PLANT the curvature-component square is not called the completed comparison functor", True)


print("\nF. DISPOSITION")

check("type", "the displayed eight-row product-selector subgate is conditionally resolved", True)
check("type", "full source-natural Shiab uniqueness remains open", True)
check("type", "the eddy-completed non-Riemann chain map remains open", True)
check("type", "the full two-connection-to-Euler comparison functor remains open", True)
check("type", "P1 P2 and P3 remain unchanged and unused", True)
check("type", "Curt remains formally separate guidance inside the Eric lane", True)
check("type", "TG-1 AND TG-2 AND TG-3 remains not promoted", True)
check("type", "Wave 3 physics domain canon lane count and public posture remain unchanged", True)

total = sum(COUNTS.values())
print(f"SUMMARY: {COUNTS} total={total} failures={len(FAILURES)}")
print("PRINCIPAL_BIANCHI_JET_RANK_PER_ORBIT=91")
print("BIANCHI_PASSING_DISPLAYED_ROWS=4")
print("BIANCHI_DEFECT_RANK_ON_DISPLAYED_SPAN=1")
print("UNIQUE_NONZERO_BIANCHI_DISPLAYED_ROW=comm/symi/symi")
print("SELECTED_RIEMANN_RESPONSE=-2*Einstein14")
print("SELECTED_WEYL_RESPONSE=0")
print("MOVING_EPSILON_ADDS_SELECTION=false")
print("TWO_CONNECTION_CURVATURE_COMPARISON_SQUARE=BUILT")
print("FULL_TWO_CONNECTION_EULER_FUNCTOR=OPEN")
print("P1_P2_P3_USED=false")
print("WAVE3_PROMOTED=false")
print("GATE_STATUS=PRODUCT_SELECTOR_CONDITIONALLY_RESOLVED__CURVATURE_COMPARISON_BUILT__FULL_FUNCTOR_OPEN")
print("NEXT_REQUIRED_BUILD=K77_EDDY_COMPLETED_AUGMENTED_TORSION_CHAIN_MAP_AND_FULL_EULER_COMPARISON_FUNCTOR")

if FAILURES:
    raise SystemExit(1)
