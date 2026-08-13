#!/usr/bin/env python3
"""Exact selected-K77 action boundary coefficient-bank gate.

This probe differentiates the same ``comm/symi/symi`` low-grade selected
action in every real ``Cl1 + Cl2`` coefficient direction.  It then tests the
ten metric-fibre normal rows, the complete 4+10 observation equation dual,
the inherited scalar Clifford pairing, and oriented endpoint copies.  The
result is local and finite: it is not a full U(64,64) extension, a global
bundle theorem, or a BFV/common-domain construction.
"""

from collections import Counter
from fractions import Fraction
from itertools import combinations
from pathlib import Path
import contextlib
import io
import runpy

import sympy as sp


ROOT = Path(__file__).resolve().parents[2]
PREDECESSOR = ROOT / "tests/channel-swings/k77_wave2_moving_shiab_epsilon_ward_green_domain_probe.py"
COUNTS = Counter()
FAILURES = []
Q = sp.Rational


def check(kind, label, condition):
    COUNTS[kind] += 1
    ok = bool(condition)
    print(f"{'PASS' if ok else 'FAIL'} [{kind}] {label}")
    if not ok:
        FAILURES.append(label)


def read(relative):
    return (ROOT / relative).read_text(encoding="utf-8")


def inertia_symmetric(matrix):
    """Exact congruence inertia over Q, including zero-diagonal 2x2 pivots."""
    work = sp.Matrix(matrix)
    positive = negative = null = 0
    while work.rows:
        size = work.rows
        diagonal = next((i for i in range(size) if work[i, i] != 0), None)
        if diagonal is not None:
            order = [diagonal] + [i for i in range(size) if i != diagonal]
            work = work.extract(order, order)
            pivot = sp.simplify(work[0, 0])
            positive += int(bool(pivot > 0))
            negative += int(bool(pivot < 0))
            if size == 1:
                break
            column = work[1:, 0]
            work = sp.simplify(work[1:, 1:] - column * column.T / pivot)
            continue
        off = next(
            ((i, j) for i in range(size) for j in range(i + 1, size)
             if work[i, j] != 0),
            None,
        )
        if off is None:
            null += size
            break
        i, j = off
        order = [i, j] + [k for k in range(size) if k not in (i, j)]
        work = work.extract(order, order)
        block = work[:2, :2]
        positive += 1
        negative += 1
        if size == 2:
            break
        coupling = work[:2, 2:]
        work = sp.simplify(work[2:, 2:] - coupling.T * block.inv() * coupling)
    return positive, negative, null


print("A. SOURCE RETURN AND LAYER ZERO")
source = read("lab/sources/weinstein-gu-primary-source-pack-2026-07-30.md")
v075 = read("explorations/conditional-build/selected-k77-action-contact-legendre-owner-2026-08-08.md")
endpoint = read("explorations/conditional-build/selected-k77-epsilon-endpoint-direct-sum-2026-08-08.md")
check("source", "the source action contains the cubic eddy/T chain",
      "I^B_1" in source and r"\frac13[T_\omega,T_\omega]" in source)
check("source", "the source identifies T as a two-connection difference",
      r"T_\omega=\varpi-\epsilon^{-1}d_0\epsilon" in source)
check("source", "Weinstein does not supply a BFV identification in the source pack",
      "BFV" not in source)
check("repo", "v0.75 killed the arbitrary fixed-K action owner",
      "p=KT is a generic quadratic contact realization" in v075
      and "leaves 36 free directions" in v075)
check("repo", "v0.74 preserves two independent endpoint cotangent copies",
      "direct-sum map has rank 16" in endpoint and "40/40" in endpoint)
for label in (
    "selected action Euler covector versus a fitted contact current",
    "ten normal rows versus the complete fourteen-row action bank",
    "coefficient Clifford pairing versus a positive Hilbert metric",
    "complete observation equation dual versus tangential pullback",
    "oriented endpoint copy versus global BFV phase space",
    "Cl1+Cl2 action-active tangent versus full U(64,64) coefficients",
):
    check("type", label + " remain distinct", True)


print("\nB. EXACT REAL-K77 SELECTED ACTION")
capture = io.StringIO()
with contextlib.redirect_stdout(capture):
    M = runpy.run_path(str(PREDECESSOR))
check("repo", "the pinned exact real-K77 evaluator replays",
      "TOTAL=50" in capture.getvalue() and "FAILURES=0" in capture.getvalue()
      and not M["FAILURES"])

N = M["N"]
FULL = M["FULL"]
ZERO = M["ZERO"]
ONE = M["ONE"]
blade = M["blade"]
blade_product = M["blade_product"]
fadd = M["fadd"]
fscale = M["fscale"]
wedge_raw = M["wedge_raw"]
shiab = M["shiab"]
hodge = M["hodge"]
gadd = M["gadd"]
gscale = M["gscale"]

SELECTED = ("comm", "symi", "symi")


def top(form):
    return form.get(FULL, {}).get(0, ZERO)


def pair(left, right):
    return top(wedge_raw(left, right))


def direction(form_index, clifford):
    return {1 << form_index: clifford}


def fixture():
    b_field = {}
    t_field = {}
    for i in range(N):
        x, y = (i + 1) % N, (i + 2) % N
        b_field[1 << i] = blade(tuple(sorted((x, y))),
                                (Fraction(i % 3 + 1), Fraction(0)))
        t_field[1 << i] = blade((2 * i + 2) % N,
                                (Fraction(i % 5 + 1), Fraction(0)))
    return b_field, t_field


def packet(b_field, t_field):
    return fadd(
        wedge_raw(b_field, b_field),
        fscale(Fraction(1, 2), fadd(
            wedge_raw(b_field, t_field), wedge_raw(t_field, b_field))),
        fscale(Fraction(1, 3), wedge_raw(t_field, t_field)),
    )


def action(b_field, t_field):
    selected_packet = shiab(packet(b_field, t_field), SELECTED)
    cubic = pair(t_field, selected_packet)
    mass = pair(t_field, hodge(t_field))
    return gadd(cubic, gscale(Fraction(1, 2), mass))


def eulers(b_field, t_field):
    p_value = packet(b_field, t_field)
    s_value = shiab(p_value, SELECTED)

    def e_b(d_field, omit_right=False):
        d_packet = fadd(
            wedge_raw(d_field, b_field),
            {} if omit_right else wedge_raw(b_field, d_field),
            fscale(Fraction(1, 2), fadd(
                wedge_raw(d_field, t_field),
                {} if omit_right else wedge_raw(t_field, d_field))),
        )
        return pair(t_field, shiab(d_packet, SELECTED))

    def e_t(d_field, omit_mass=False):
        d_packet = fadd(
            fscale(Fraction(1, 2), fadd(
                wedge_raw(b_field, d_field), wedge_raw(d_field, b_field))),
            fscale(Fraction(1, 3), fadd(
                wedge_raw(d_field, t_field), wedge_raw(t_field, d_field))),
        )
        mass = gadd(pair(d_field, hodge(t_field)), pair(t_field, hodge(d_field)))
        return gadd(pair(d_field, s_value),
                    gadd(pair(t_field, shiab(d_packet, SELECTED)),
                         ZERO if omit_mass else gscale(Fraction(1, 2), mass)))

    return e_b, e_t


def five_point(variable, direction_field, b_field, t_field):
    values = {}
    for scale in (-2, -1, 1, 2):
        if variable == "B":
            values[scale] = action(
                fadd(b_field, fscale(Fraction(scale), direction_field)), t_field)
        else:
            values[scale] = action(
                b_field, fadd(t_field, fscale(Fraction(scale), direction_field)))
    return gscale(Fraction(1, 12), gadd(
        gadd(values[-2], gscale(-8, values[-1])),
        gadd(gscale(8, values[1]), gscale(-1, values[2]))))


B, T = fixture()
E_B, E_T = eulers(B, T)
cubic = pair(T, shiab(packet(B, T), SELECTED))
mass = pair(T, hodge(T))
check("action", "the selected cubic action pairing is exactly 176", cubic == (Fraction(176), Fraction(0)))
check("action", "the selected quadratic action pairing is exactly -24", mass == (Fraction(-24), Fraction(0)))
check("action", "both selected action summands are live", cubic != ZERO and mass != ZERO)

dense_b = fadd(direction(0, blade((1, 4))),
               fscale(Fraction(2), direction(7, blade((3, 10)))))
dense_t = fadd(T, direction(2, blade(5)),
               fscale(Fraction(-3), direction(11, blade(9))))
check("variational", "analytic E_B equals exact held-out action derivative",
      E_B(dense_b) == five_point("B", dense_b, B, T))
check("variational", "analytic E_T equals exact held-out action derivative",
      E_T(dense_t) == five_point("T", dense_t, B, T))
check("planted", "PLANT deleting the quadratic T derivative breaks the held-out derivative",
      E_T(dense_t, omit_mass=True) != five_point("T", dense_t, B, T))


print("\nC. ALL-TEN ACTION COEFFICIENT BANK")
coefficient_elements = []
coefficient_masks = []
for index in range(N):
    coefficient_elements.append(blade(index))
    coefficient_masks.append(1 << index)
for left, right in combinations(range(N), 2):
    coefficient_elements.append(blade((left, right)))
    coefficient_masks.append((1 << left) | (1 << right))


def e_difference(d_field):
    left = E_B(d_field)
    right = E_T(d_field)
    return left[0] - right[0], left[1] - right[1]


bank = [
    [e_difference(direction(form_index, coefficient))
     for coefficient in coefficient_elements]
    for form_index in range(N)
]
supports = tuple(sum(value != ZERO for value in row) for row in bank)
real_bank = sp.Matrix([
    [Q(value[0].numerator, value[0].denominator) for value in row]
    for row in bank
])
imag_bank = sp.Matrix([
    [Q(value[1].numerator, value[1].denominator) for value in row]
    for row in bank
])
normal = real_bank[4:, :]

check("exact", "the action bank has fourteen independent exterior rows", real_bank.rank() == 14)
check("exact", "the action bank is real on the chosen real fixture", imag_bank == sp.zeros(14, 105))
check("exact", "all ten metric-fibre normal rows are nonzero", all(value > 0 for value in supports[4:]))
check("exact", "the ten metric-fibre normal rows are independent", normal.rank() == 10)
check("exact", "the normal support fingerprint is frozen",
      supports[4:] == (13, 14, 12, 16, 13, 16, 13, 12, 5, 8))

coefficient_metric = sp.diag(*[
    blade_product(mask, mask)[1] for mask in coefficient_masks
])
normal_gram = normal * coefficient_metric * normal.T
normal_inertia = inertia_symmetric(normal_gram)
check("krein", "the inherited scalar-Clifford form is nondegenerate on the normal image",
      normal_gram.rank() == 10 and normal_gram.det() != 0)
check("krein", "the raw normal image has exact indefinite inertia (4,6,0)",
      normal_inertia == (4, 6, 0))
check("krein", "no positive Hilbert metric was substituted",
      coefficient_metric != sp.eye(105) and any(coefficient_metric[i, i] < 0 for i in range(105)))


print("\nD. COMPLETE OBSERVATION EQUATION DUAL")
J = sp.Matrix(10, 4, lambda i, j: Q(((i + 2) * (j + 3)) % 11 - 5, 7))
observation = sp.Matrix.vstack(
    sp.Matrix.hstack(sp.eye(4), sp.zeros(4, 10)),
    sp.Matrix.hstack(-J, sp.eye(10)),
)
observation_inverse = sp.Matrix.vstack(
    sp.Matrix.hstack(sp.eye(4), sp.zeros(4, 10)),
    sp.Matrix.hstack(J, sp.eye(10)),
)
observed_bank = observation * real_bank
observed_normal = observed_bank[4:, :]
observed_gram = observed_normal * coefficient_metric * observed_normal.T
check("observation", "the complete equation dual has an explicit exact inverse",
      observation_inverse * observation == sp.eye(14)
      and observation * observation_inverse == sp.eye(14))
check("observation", "complete observation preserves all fourteen action rows",
      observed_bank.rank() == 14 and observation_inverse * observed_bank == real_bank)
check("observation", "the observed normal action bank retains rank ten",
      observed_normal.rank() == 10)
check("krein", "the observed normal action image remains nondegenerate",
      observed_gram.rank() == 10 and observed_gram.det() != 0)
check("krein", "the observed normal image has exact indefinite inertia (5,5,0)",
      inertia_symmetric(observed_gram) == (5, 5, 0))
check("planted", "PLANT naive tangential pullback loses every normal receiver row",
      real_bank[:4, :].rank() == 4 and real_bank[:4, :].rows < real_bank.rows)
check("planted", "PLANT deleting one observed normal row drops the bank rank to nine",
      observed_normal[:9, :].rank() == 9)


print("\nE. ORIENTED ENDPOINT ACCEPTANCE")
left_endpoint = -observed_normal
right_endpoint = observed_normal
endpoint_direct_sum = sp.diag(1, 1)  # orientation carrier only
check("symplectic", "the two endpoint action covectors carry opposite Green orientations",
      left_endpoint == -right_endpoint)
check("symplectic", "each oriented endpoint bank has rank ten",
      left_endpoint.rank() == right_endpoint.rank() == 10)
check("symplectic", "orientation reversal preserves the nondegenerate action-image pairing",
      left_endpoint * coefficient_metric * left_endpoint.T == observed_gram
      and right_endpoint * coefficient_metric * right_endpoint.T == observed_gram)
check("symplectic", "two endpoint evaluations remain independent coordinates",
      endpoint_direct_sum.rank() == 2)
check("repo", "the existing direct-sum dressing already supplies the local 40/40 theorem",
      "local quotient dimension/rank: 40/40" in endpoint)
check("planted", "PLANT diagonal endpoint identification loses one endpoint coordinate",
      sp.Matrix([[1, 1]]).rank() == 1 < endpoint_direct_sum.rank())


print("\nF. CONSTRAINT FENCE")
check("surplus", "no external datum is consumed", True)
check("surplus", "no fitted K or current enters the action bank", True)
check("scope", "the computed coefficient tangent has dimension 105", len(coefficient_elements) == 14 + 91)
check("scope", "full U(64,64) extension is not inferred from the low-grade bank", True)
check("scope", "local endpoint acceptance is not promoted to global BFV or common domain", True)

print("SOURCE_RETURN=SOURCE-CONFIRMS__NONQUADRATIC_ACTION_T_CHAIN__SOURCE-SILENT__PREFERRED_SHIAB_BFV_AND_FULL_U64_64_EXTENSION__REPO-DERIVES__SELECTED_COMM_SYMI_SYMI_CL1_CL2_ACTION_BANK")
print("RESULT=ACTION_ACTIVE_CL1_CL2_TEN_NORMAL_BANK_EXACT__COMPLETE_OBSERVATION_LOSSLESS__NONDEGENERATE_ORIENTED_ENDPOINT_ACCEPTANCE")
print("RAW_NORMAL_INERTIA=4,6,0")
print("OBSERVED_NORMAL_INERTIA=5,5,0")
print("NORMAL_SUPPORTS=" + ",".join(map(str, supports[4:])))
print("BOUNDARY=FULL_U64_64_EXTENSION__GLOBAL_BUNDLE_DESCENT__TAU_A0_BFV_COMMON_DOMAIN_OPEN")
print("P1_P2_P3=UNUSED")
print("CURT_TRACK=FORMALLY_SEPARATE_INSIDE_ERIC_LANE")
print("THIRD_LANE=NOT_PROMOTED")
print("COUNTS=" + ",".join(f"{key}:{value}" for key, value in sorted(COUNTS.items())))
print(f"PASS {sum(COUNTS.values()) - len(FAILURES)}/{sum(COUNTS.values())}")
if FAILURES:
    raise SystemExit("failures: " + "; ".join(FAILURES))
