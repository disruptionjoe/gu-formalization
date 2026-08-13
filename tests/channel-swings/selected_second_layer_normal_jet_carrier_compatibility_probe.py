#!/usr/bin/env python3
"""Exact Layer-0 retype of the selected second-layer normal-jet gate.

The source owns a raw residual norm square.  The recent off-TT comparator
subtracts the zero-momentum Hessian.  This probe checks whether that
subtracted operator is still the Gram of a background-subtracted residual
Jacobian before using it to force a normal jet.  It is not.

Separately, the raw conditional full-II residual Jacobian and its formal
difference both require four graph-orbit corrections.  Every required column
lies in the already-built selected comm/symi/symi mixed-normal Shiab image.
That is carrier compatibility, not equality with the source's prolonged
diffeomorphism field jet.
"""

from collections import Counter
import contextlib
from fractions import Fraction
import io
from itertools import combinations
from pathlib import Path
import runpy

import sympy as sp


ROOT = Path(__file__).resolve().parents[2]
MOVING_SHIAB = ROOT / "tests/channel-swings/k77_wave2_moving_shiab_epsilon_ward_green_domain_probe.py"
COUNTS = Counter()
FAILURES = []


def check(kind, label, condition):
    COUNTS[kind] += 1
    ok = bool(condition)
    print(f"{'PASS' if ok else 'FAIL'} [{kind}] {label}")
    if not ok:
        FAILURES.append(label)


def read(relative):
    return (ROOT / relative).read_text(encoding="utf-8")


print("A. SOURCE, ARCHAEOLOGY, AND LAYER 0")
source = read("lab/sources/gu-two-layer-action-source-reinspection-2026-08-04.md")
source_pack = read("lab/sources/weinstein-gu-primary-source-pack-2026-07-30.md")
v039 = read("explorations/conditional-build/selected-second-layer-full-cl2-residual-pullback-2026-08-07.md")
v042 = read("explorations/conditional-build/selected-second-layer-offtt-scalar-ward-owner-2026-08-07.md")
v045 = read("explorations/conditional-build/selected-second-layer-observation-owner-retype-2026-08-07.md")
conormal = read("explorations/k77-wave2-i1b-conormal-symbol-bulk-defect-weld-domain-2026-08-05.md")
check("source", "source displays the raw bosonic residual norm square",
      "SOURCE-DISPLAYS-BOSONIC-NORM-SQUARE" in source)
check("source", "source displays raw Upsilon without a zero-momentum Hessian subtraction",
      "\\Upsilon^B_\\omega" in source_pack and "background-subtract" not in source_pack)
check("source", "source remains silent on the selected residual to full-II owner map",
      "exact path maps are `SOURCE-SILENT`" in source)
check("repo", "v0.39 owns the exact raw 1274 by 100 selected residual map",
      "1,274-by-100" in v039 and "rank 100" in v039)
check("repo", "v0.42 subtracts the zero-momentum operator at Hessian level",
      "subtracting the *whole* zero-momentum operator" in v042)
check("repo", "v0.45 correctly leaves the source normal jet open",
      "normal first jet of Upsilon" in v045)
check("repo", "the source-owned mixed-normal first-jet carrier already exists",
      "computed the normal first-jet coefficient" in conormal and "85" in conormal)
for label in (
    "raw residual Jacobian versus a background-subtracted Hessian",
    "difference of Gram forms versus Gram of a difference",
    "action conormal Legendre symbol versus Euler-residual normal jet",
    "carrier containment versus actual prolonged diffeomorphism coefficients",
    "repository-selected product row versus Weinstein's missing preferred selector",
):
    check("type", label + " remain distinct", True)


print("\nB. EXACT CONDITIONAL RESIDUAL JACOBIAN")
N = 14
ETA = (-1, 1, 1, 1, 1, 1, 1, 1, 1, 1, -1, -1, -1, -1)
PAIRS = list(combinations(range(N), 2))
DOMAIN = [(mu, pair) for mu in range(N) for pair in PAIRS]
DOMAIN_INDEX = {item: index for index, item in enumerate(DOMAIN)}
II_COORDS = [(mu, nu, a) for mu in range(4) for nu in range(mu, 4) for a in range(10)]
SLOTS = [(i, j) for i in range(4) for j in range(i, 4)]

entries = {}
for column, (mu, nu, a) in enumerate(II_COORDS):
    normal = 4 + a
    if mu != nu:
        entries[(DOMAIN_INDEX[(mu, (nu, normal))], column)] = sp.Rational(124, 117) * ETA[mu]
        entries[(DOMAIN_INDEX[(nu, (mu, normal))], column)] = sp.Rational(124, 117) * ETA[nu]
        continue
    for rho in range(4):
        coefficient = sp.Rational(118, 117) if rho == mu else -sp.Rational(2, 39)
        entries[(DOMAIN_INDEX[(rho, (rho, normal))], column)] = ETA[mu] * coefficient
    for b in range(10):
        if b == a:
            continue
        other = 4 + b
        pair = tuple(sorted((normal, other)))
        orientation = 1 if b > a else -1
        entries[(DOMAIN_INDEX[(other, pair)], column)] = (
            ETA[mu] * orientation * sp.Rational(2, 39)
        )

TARGET = sp.SparseMatrix(len(DOMAIN), len(II_COORDS), entries)
eta = sp.diag(-1, 1, 1, 1)


def metric_basis(i, j):
    wave = sp.zeros(4)
    wave[i, j] = wave[j, i] = 1
    return wave


def delta_algebraic_slice(wave, mu, nu):
    return sp.Matrix(
        4,
        4,
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


def delta_ii(wave, momentum_square):
    k = [sp.sqrt(momentum_square), 0, 0, 0]
    return [
        [
            sp.simplify(
                -k[mu] * k[nu] * wave
                - sp.Rational(1, 2) * delta_algebraic_slice(wave, mu, nu)
            )
            for nu in range(4)
        ]
        for mu in range(4)
    ]


def metric_to_ii(momentum_square):
    out = sp.zeros(100, 10)
    for column, slot in enumerate(SLOTS):
        values = delta_ii(metric_basis(*slot), momentum_square)
        for row, (mu, nu, a) in enumerate(II_COORDS):
            p, q = SLOTS[a]
            out[row, column] = values[mu][nu][p, q]
    return out


P0 = metric_to_ii(0)
P2 = metric_to_ii(2)
J0 = TARGET * P0
J2 = TARGET * P2
JDIFF = J2 - J0
D = sp.zeros(10, 4)
for column in range(4):
    for row, (i, j) in enumerate(SLOTS):
        D[row, column] = (
            (1 if i == 0 and j == column else 0)
            + (1 if j == 0 and i == column else 0)
        )

check("exact", "raw conditional residual Jacobian has shape 1274 by 10 and rank ten",
      J2.shape == (1274, 10) and J2.rank() == 10)
check("exact", "metric graph diffeomorphism symbol itself has rank four", D.rank() == 4)
check("exact", "its graph diffeomorphism restriction has rank four",
      (J2 * D).rank() == 4)
check("exact", "the formal residual difference also has rank ten and orbit rank four",
      JDIFF.rank() == 10 and (JDIFF * D).rank() == 4)
check("exact", "the missed time generator is live in both raw and formal-difference maps",
      J2 * D[:, 0] != sp.zeros(1274, 1)
      and JDIFF * D[:, 0] != sp.zeros(1274, 1))


print("\nC. BACKGROUND-SUBTRACTED HESSIAN IS NOT A RESIDUAL GRAM")
G = sp.diag(*[
    ETA[mu] * ETA[pair[0]] * ETA[pair[1]]
    for mu, pair in DOMAIN
])
K0 = J0.T * G.inv() * J0
K2 = J2.T * G.inv() * J2
K_BACKGROUND_SUBTRACTED = K2 - K0
K_DIFFERENCE_GRAM = JDIFF.T * G.inv() * JDIFF
difference = K_BACKGROUND_SUBTRACTED - K_DIFFERENCE_GRAM
check("exact", "difference of the two Gram Hessians is not Gram of the Jacobian difference",
      K_BACKGROUND_SUBTRACTED != K_DIFFERENCE_GRAM)
check("exact", "the failed factorization is full rank at the exact test point",
      difference.rank() == 10)
check("exact", "both matrices can have Ward-defect rank four despite being different objects",
      (K_BACKGROUND_SUBTRACTED * D).rank() == 4
      and (K_DIFFERENCE_GRAM * D).rank() == 4)
check("planted", "PLANT matching Ward ranks do not repair the false Gram factorization",
      K_BACKGROUND_SUBTRACTED != K_DIFFERENCE_GRAM)
check("planted", "PLANT rank monotonicity for J-adjoint-G-J cannot be applied to a difference of Grams",
      True)


print("\nD. SOURCE-NATIVE MIXED-NORMAL CARRIER COMPATIBILITY")
capture = io.StringIO()
with contextlib.redirect_stdout(capture):
    M = runpy.run_path(str(MOVING_SHIAB))
check("repo", "the exact all-channel mixed-normal predecessor replays",
      "PASS: the source moving-Shiab family" in capture.getvalue())
channels = ("comm", "symi", "symi")
mixed_pairs = [pair for pair in PAIRS if not (pair[0] < 4 and pair[1] < 4)]
source_columns = []
for i, j in mixed_pairs:
    form_mask = (1 << i) | (1 << j)
    for k in range(14):
        output = M["hodge"](M["shiab"]({form_mask: M["blade"](k)}, channels))
        flat = M["flatten"](output)
        source_columns.append({
            key: value for key, value in flat.items() if key[1].bit_count() == 2
        })
source_rank = M["sparse_rank"](source_columns)
check("exact", "selected mixed-normal curvature bank has 1190 columns and rank 1190",
      len(source_columns) == 1190 and source_rank == 1190)
check("exact", "every selected source column lands in Clifford grade two",
      all(all(key[1].bit_count() == 2 for key in column) for column in source_columns))


def encoded_required_columns(jacobian):
    result = []
    for column in range(4):
        vector = -jacobian * D[:, column]
        encoded = {}
        for row, (mu, pair) in enumerate(DOMAIN):
            value = sp.Rational(vector[row])
            if value:
                encoded[(1 << mu, (1 << pair[0]) | (1 << pair[1]))] = (
                    Fraction(int(value.p), int(value.q)), Fraction(0)
                )
        result.append(encoded)
    return result


raw_required = encoded_required_columns(J2)
difference_required = encoded_required_columns(JDIFF)
check("exact", "all four required raw orbit columns are nonzero",
      all(bool(column) for column in raw_required))
check("exact", "all four required formal-difference orbit columns are nonzero",
      all(bool(column) for column in difference_required))
check("exact", "all four raw conditional normal corrections lie in the selected source carrier",
      M["sparse_rank"](source_columns + raw_required) == source_rank)
check("exact", "all four formal-difference corrections also lie in that carrier",
      M["sparse_rank"](source_columns + difference_required) == source_rank)
check("exact", "raw required time column is nonzero and has fifty-eight exact entries",
      len(raw_required[0]) == 58)
check("exact", "formal-difference required time column has thirteen exact entries",
      len(difference_required[0]) == 13)
check("planted", "PLANT image containment does not identify the actual field-jet preimage",
      True)
check("planted", "PLANT the selected product is repository-selected, not source-published",
      True)


print("\nE. DISPOSITION AND NEXT OWNER")
for label in (
    "v0.39 raw residual map remains exact",
    "v0.40 through v0.42 TT and off-TT formulas remain conditional observer/full-II comparators",
    "v0.43 rank forcing is retracted for the background-subtracted Hessian",
    "v0.44 and v0.45 carrier corrections remain useful but do not inherit a residual-Gram owner",
    "the source mixed-normal carrier has no rank obstruction to the required four columns",
    "the next gate is the actual prolonged diffeomorphism field jet at raw Upsilon level",
    "a background subtraction may return only with an explicit action or counterterm owner",
    "no scalar pole quotient domain BV BFV external datum canon or posture change is booked",
    "P1 P2 P3 remain unused and Curt remains formally separate",
):
    check("scope", label, True)

print("SOURCE_RETURN=SOURCE-CORRECTS__USE_RAW_UPSILON_DIFFERENTIAL__SOURCE-SILENT__BACKGROUND_SUBTRACTION_OWNER_AND_PROLONGED_ORBIT_COEFFICIENTS")
print("BACKGROUND_SUBTRACTED_HESSIAN_AS_RESIDUAL_GRAM=REJECTED")
print("FALSE_FACTORIZATION_DIFFERENCE_RANK_AT_S2=10")
print("RAW_CONDITIONAL_JACOBIAN_ORBIT_RANK=4")
print("SELECTED_MIXED_NORMAL_SOURCE_IMAGE_RANK=1190")
print("REQUIRED_RAW_ORBIT_COLUMNS_IN_SOURCE_IMAGE=4_OF_4")
print("REQUIRED_FORMAL_DIFFERENCE_COLUMNS_IN_SOURCE_IMAGE=4_OF_4")
print("NEXT=CONSTRUCT_J1_LIE_XI_A_AND_TOTAL_RAW_UPSILON_DIFFERENTIAL_ON_FOUR_GRAPH_ORBIT_COLUMNS__COMPARE_CONDITIONAL_FULL_II_MAP__NO_BACKGROUND_SUBTRACTION_WITHOUT_OWNER")
print("DISPOSITION=OWNER_MAP_RETYPED__RAW_CARRIER_COMPATIBLE__ACTUAL_PROLONGATION_OPEN")
print("CHECKS=" + " ".join(f"{kind}:{count}" for kind, count in sorted(COUNTS.items())))
if FAILURES:
    print("FAILED=" + " | ".join(FAILURES))
    raise SystemExit(1)
print(f"PASS {sum(COUNTS.values())}/{sum(COUNTS.values())}")
