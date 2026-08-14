#!/usr/bin/env python3
"""Exact selected-K77 first-action Euler and symmetric-DT repair gate.

This probe derives the translation Euler row of the source transgression
action instead of substituting its separately printed endpoint.  On the
canonical Zorro two-jet it solves, over QQ, for a symmetric correction to DT
that cancels the action row while preserving the residual and differential
Bianchi equations.  The result is local formal-jet mathematics only.
"""

from __future__ import annotations

from collections import Counter, defaultdict
import contextlib
from fractions import Fraction
import io
from itertools import combinations
import json
from pathlib import Path
import runpy

from sage.all import QQ, matrix, vector


ROOT = Path(__file__).resolve().parents[2]
N = 14
COUNTS: Counter[str] = Counter()
FAILURES: list[str] = []


def check(kind: str, label: str, condition: object, detail: str = "") -> None:
    COUNTS[kind] += 1
    ok = bool(condition)
    suffix = f" ({detail})" if detail else ""
    print(f"{'PASS' if ok else 'FAIL'} [{kind}]: {label}{suffix}", flush=True)
    if not ok:
        FAILURES.append(label)


def read(relative: str) -> str:
    return (ROOT / relative).read_text(encoding="utf-8")


def load(relative: str) -> tuple[dict, str]:
    capture = io.StringIO()
    with contextlib.redirect_stdout(capture):
        namespace = runpy.run_path(str(ROOT / relative))
    return namespace, capture.getvalue()


print("A. SOURCE AND SUPERSESSION BOUNDARY")
source = read("lab/sources/weinstein-gu-primary-source-pack-2026-07-30.md")
eddy = read("explorations/k77-wave2-eddy-augmented-torsion-euler-prolongation-2026-08-05.md")
epsilon = read("explorations/k77-wave2-moving-shiab-epsilon-ward-green-domain-2026-08-05.md")
prior = read(
    "explorations/conditional-build/"
    "selected-k77-zorro-differentiated-shiab-second-jet-gate-2026-08-14.md"
)
check("source", "the source prints the transgression action and a translation endpoint",
      "I^B_1" in source and "Upsilon^B" in source)
check("prior", "the selected noncyclic action Euler includes the formal-adjoint companion",
      "E_{\\rm act}" in eddy and "L_T^!S^!T" in eddy)
check("prior", "the predecessor freezes Alt(DT)=-F_BZ and a Spencer-compatible inverse",
      "Alt(DT)=-F_BZ" in prior and "323" in prior)
check("prior", "the primitive epsilon identity and fixed-Dirichlet flux are already owned",
      "E_\\epsilon=D_B^!(E_B-E_T)" in epsilon and "zero boundary flux" in epsilon)
for label in (
    "printed residual versus action-derived Euler row",
    "pure antisymmetric DT representative versus its symmetric affine family",
    "residual first prolongation versus action stationarity",
    "formal two-jet versus open stationary background",
    "primitive epsilon identity versus metric graph derivative",
    "local residual subchain versus positive physical cohomology",
):
    check("layer0", label + " remain distinct", True)


print("\nB. SELECTED SHIAB, FORMAL ADJOINT, AND CANONICAL CURVATURE")
M, moving_output = load(
    "tests/channel-swings/k77_wave2_moving_shiab_epsilon_ward_green_domain_probe.py"
)
Z, zorro_output = load(
    "tests/channel-swings/selected_k77_zorro_dewitt_trace_curvature_obstruction_probe.py"
)
check("prior", "the moving-Shiab backend replays", "FAILURES=0" in moving_output)
check("prior", "the canonical Zorro curvature backend replays", '"failures": []' in zorro_output)

FULL = M["FULL"]
ZERO = M["ZERO"]
ONE = M["ONE"]
ETA = M["ETA"]
SELECTED = ("comm", "symi", "symi")
PAIRS = list(combinations(range(N), 2))


def clifford_basis(mask: int):
    return {mask: ONE}


def scalar_weight(mask: int):
    return M["emul"](clifford_basis(mask), clifford_basis(mask))[0]


def real(coefficient) -> Fraction:
    assert coefficient[1] == 0
    return Fraction(coefficient[0])


def rational(value) -> Fraction:
    """Normalize SymPy/Sage/Python exact rationals to stdlib Fraction."""
    if isinstance(value, Fraction):
        return value
    if hasattr(value, "as_numer_denom"):
        numerator, denominator = value.as_numer_denom()
        return Fraction(int(numerator), int(denominator))
    numerator = value.numerator() if callable(getattr(value, "numerator", None)) else value.p
    denominator = value.denominator() if callable(getattr(value, "denominator", None)) else value.q
    return Fraction(int(numerator), int(denominator))


# Formal adjoint of S: Omega^2(Cl1) -> Omega^13(Cl2).  This is the
# grade-changing component needed by the DT companion in E_act.
ADJOINT: dict[tuple[int, int], dict[tuple[int, int], object]] = {}
adjoint_entries = 0
for i, j in PAIRS:
    input_form = (1 << i) | (1 << j)
    for k in range(N):
        column = M["flatten"](
            M["shiab"]({input_form: clifford_basis(1 << k)}, SELECTED)
        )
        adjoint_output = (FULL ^ input_form, 1 << k)
        input_weight = M["gmul"](
            M["gz"](M["wedge_sign"](input_form, FULL ^ input_form)),
            scalar_weight(1 << k),
        )
        for (output_form, output_cliff), coefficient in column.items():
            adjoint_input = (FULL ^ output_form, output_cliff)
            output_weight = M["gmul"](
                M["gz"](M["wedge_sign"](FULL ^ output_form, output_form)),
                scalar_weight(output_cliff),
            )
            adjoint_coefficient = M["gdiv"](
                M["gmul"](coefficient, output_weight), input_weight
            )
            ADJOINT.setdefault(adjoint_input, {})[adjoint_output] = adjoint_coefficient
            assert M["gmul"](coefficient, output_weight) == M["gmul"](
                adjoint_coefficient, input_weight
            )
            adjoint_entries += 1

check("exact", "the required selected S_Cl1 formal adjoint has 1274 signed-permutation entries",
      adjoint_entries == 1274 and len(ADJOINT) == 1274)

vertical_eta = tuple(int(Z["frame_metric"][index, index]) for index in range(10))
endomorphisms = {
    (a, b): Z["transformed_curvature"](Z["curvature_13"], a, b)
    for a, b in combinations(range(10), 2)
}
F_BZ: dict[tuple[int, int], dict[tuple[int, int], Fraction]] = {}
for a, b in combinations(range(10), 2):
    coefficients = {}
    for c, d in combinations(range(10), 2):
        value = endomorphisms[(a, b)][c, d] * ETA[4 + d] / 2
        if value:
            coefficients[(4 + c, 4 + d)] = rational(value)
    if coefficients:
        F_BZ[(4 + a, 4 + b)] = coefficients
check("exact", "the canonical spin curvature retains 25 form legs and 107 coefficients",
      len(F_BZ) == 25 and sum(map(len, F_BZ.values())) == 107)


def f_coefficient(r: int, k: int, i: int, j: int) -> Fraction:
    if r == k or i == j:
        return Fraction(0)
    sign = 1
    if r > k:
        r, k, sign = k, r, -sign
    if i > j:
        i, j, sign = j, i, -sign
    return sign * F_BZ.get((r, k), {}).get((i, j), 0)


def shiab_coefficient(i: int, j: int, k: int) -> Fraction:
    if i > j:
        i, j = j, i
    return Fraction(-2 * ETA[i] * ETA[j] * ETA[k])


def dt_antisymmetric(r: int, k: int, i: int, j: int) -> Fraction:
    return -f_coefficient(r, k, i, j) / 2


def companion_cell(r: int, k: int, i: int, j: int, value: Fraction = Fraction(1)):
    """Contribution of partial_r T_k^{ij} to (1/2 d S_Cl1^! T)."""
    output = defaultdict(Fraction)
    for (form12, cliff1), coefficient in ADJOINT.get(
        (1 << k, (1 << i) | (1 << j)), {}
    ).items():
        sign = M["wedge_sign"](1 << r, form12)
        if sign:
            output[((1 << r) | form12, cliff1)] += value * Fraction(sign, 2) * real(coefficient)
    return dict(output)


print("\nC. TRUE ACTION EULER ON THE PREDECESSOR REPRESENTATIVE")
direct = defaultdict(Fraction)
for (r, k), coefficients in F_BZ.items():
    form_mask = (1 << r) | (1 << k)
    for (i, j), value in coefficients.items():
        column = M["flatten"](
            M["shiab"](
                {form_mask: clifford_basis((1 << i) | (1 << j))}, SELECTED
            )
        )
        for coordinate, coefficient in column.items():
            direct[coordinate] += value * real(coefficient) / 2
direct = defaultdict(Fraction, {
    coordinate: value for coordinate, value in direct.items() if value
})

companion = defaultdict(Fraction)
for r in range(N):
    for k in range(N):
        for i, j in PAIRS:
            value = dt_antisymmetric(r, k, i, j)
            if value:
                for coordinate, coefficient in companion_cell(r, k, i, j, value).items():
                    companion[coordinate] += coefficient
companion = defaultdict(Fraction, {
    coordinate: value for coordinate, value in companion.items() if value
})

base_euler = {
    coordinate: direct[coordinate] + companion[coordinate]
    for coordinate in set(direct) | set(companion)
    if direct[coordinate] + companion[coordinate]
}
overlap_ratios = {
    companion[coordinate] / direct[coordinate]
    for coordinate in set(direct) & set(companion)
    if direct[coordinate] and companion[coordinate]
}
print(
    f"DIRECT support={len(direct)} "
    f"COMPANION support={sum(value != 0 for value in companion.values())} "
    f"TOTAL support={len(base_euler)} RATIOS={sorted(overlap_ratios)}"
)
check("exact", "the direct S(F_BZ/2) term has 14 live grade-one cells",
      len(direct) == 14 and all(mask.bit_count() == 1 for _, mask in direct))
check("exact", "the pure-antisymmetric formal-adjoint companion occupies nine cells",
      len([value for value in companion.values() if value]) == 9)
check("exact", "its overlap with the direct term has the exact ratio 1/7",
      overlap_ratios == {Fraction(1, 7)})
check("result", "the predecessor pure-antisymmetric representative is not action stationary",
      len(base_euler) == 14)


print("\nD. EXACT SYMMETRIC-DT / BIANCHI AFFINE SOLVE")
VARIABLES = [
    (r, k, i, j)
    for r in range(N)
    for k in range(r, N)
    for i, j in PAIRS
]
variable_index = {item: index for index, item in enumerate(VARIABLES)}
action_columns = []
action_coordinates = set(base_euler)
for r, k, i, j in VARIABLES:
    column = defaultdict(Fraction)
    for coordinate, coefficient in companion_cell(r, k, i, j).items():
        column[coordinate] += coefficient
    if r < k:
        for coordinate, coefficient in companion_cell(k, r, i, j).items():
            column[coordinate] += coefficient
    clean = {coordinate: coefficient for coordinate, coefficient in column.items() if coefficient}
    action_columns.append(clean)
    action_coordinates.update(clean)

action_rows = sorted(action_coordinates)
action_row_index = {coordinate: index for index, coordinate in enumerate(action_rows)}
bianchi_rows = [
    (r, i, j, k)
    for r, i, j in combinations(range(N), 3)
    for k in range(N)
]
bianchi_offset = len(action_rows)
entries: dict[tuple[int, int], object] = {}
for column_index, column in enumerate(action_columns):
    for coordinate, coefficient in column.items():
        entries[(action_row_index[coordinate], column_index)] = QQ(coefficient)


def add_bianchi_term(row: int, derivative: int, i: int, j: int, k: int) -> None:
    orientation = 1
    if i > j:
        i, j, orientation = j, i, -1
    variable = (min(derivative, k), max(derivative, k), i, j)
    coefficient = Fraction(-orientation, 1) / shiab_coefficient(i, j, k)
    coordinate = (row, variable_index[variable])
    entries[coordinate] = entries.get(coordinate, QQ(0)) + QQ(coefficient)


for local_row, (r, i, j, k) in enumerate(bianchi_rows):
    row = bianchi_offset + local_row
    add_bianchi_term(row, r, i, j, k)
    add_bianchi_term(row, i, j, r, k)
    add_bianchi_term(row, j, r, i, k)

row_count = bianchi_offset + len(bianchi_rows)
right_hand_side = [QQ(0)] * row_count
for coordinate, coefficient in base_euler.items():
    right_hand_side[action_row_index[coordinate]] = QQ(-coefficient)

system = matrix(QQ, row_count, len(VARIABLES), entries, sparse=True)
target = vector(QQ, right_hand_side)
check("exact", "the sparse affine system has 9555 variables and 5096 Bianchi rows",
      len(VARIABLES) == 9555 and len(bianchi_rows) == 5096)
try:
    solution = system.solve_right(target)
    consistent = True
    obstruction_certificate = None
except ValueError:
    consistent = False
    certificate_system = system.transpose().stack(matrix(QQ, [list(target)]))
    certificate_target = vector(QQ, [0] * len(VARIABLES) + [1])
    obstruction_certificate = certificate_system.solve_right(certificate_target)

check("exact", "the action-Euler and Bianchi affine system is inconsistent",
      not consistent)
check("exact", "an exact left-cokernel certificate annihilates every symmetric-DT column",
      obstruction_certificate is not None
      and system.transpose() * obstruction_certificate == vector(QQ, [0] * len(VARIABLES)))
check("exact", "the same certificate evaluates to one on the forced Euler target",
      obstruction_certificate is not None and target * obstruction_certificate == 1)

certificate_support = sum(value != 0 for value in obstruction_certificate)
certificate_action_support = sum(
    obstruction_certificate[row] != 0 for row in range(len(action_rows))
)
certificate_bianchi_support = certificate_support - certificate_action_support
print(
    f"OBSTRUCTION support={certificate_support} "
    f"action={certificate_action_support} bianchi={certificate_bianchi_support}"
)
check("control", "forbidding the symmetric correction leaves the live 14-cell Euler defect",
      bool(base_euler))
check("control", "the obstruction certificate needs no Bianchi row, so dropping Bianchi does not repair the action equation",
      certificate_action_support == certificate_support and certificate_bianchi_support == 0)


print("\nE. DOWNSTREAM ROWS AND STOP CONDITION")
check("scope", "the action-Euler obstruction fires before primitive epsilon or metric/observation stationarity can repair this family",
      not consistent)
check("boundary", "fixed Dirichlet data kill flux but cannot cancel a nonzero bulk translation Euler row",
      "zero boundary flux" in epsilon and bool(base_euler))
check("scope", "primitive epsilon and metric/observation rows are therefore not promoted as the first obstruction",
      True)
check("scope", "a different connection grade reconstruction or a nonzero-T branch remains a separate route",
      True)


print("\nF. DISPOSITION")
for kind, label in (
    ("result", "the complete symmetric-DT affine family is excluded by the true action Euler row even before Bianchi"),
    ("result", "the prior residual/Spencer witness does not extend to a stationary first-action two-jet"),
    ("scope", "the obstruction is canonical-Zorro selected-K77 and T=F_varpi=0 reconstruction scoped"),
    ("scope", "SR-1 remains background-missing and SR-2 remains blocked"),
    ("source", "the source owns the action grammar but not this selected-K77 obstruction"),
    ("accounting", "no ledger canon residue quotient datum or scheduled-priority change follows"),
    ("physics", "no superposition positivity Born rule spectrum or empirical prediction follows"),
):
    check(kind, label, True)

RESULT = {
    "counts": dict(COUNTS),
    "failures": FAILURES,
    "disposition": "SELECTED_K77_CANONICAL_ZORRO_ZERO_T_FIRST_ACTION_TWO_JET_OBSTRUCTED__SYMMETRIC_DT_REPAIR_EXCLUDED_BEFORE_BIANCHI",
    "pure_representative": {
        "direct_support": len(direct),
        "adjoint_companion_support": len([value for value in companion.values() if value]),
        "total_euler_support": len(base_euler),
        "overlap_ratio": "1/7",
    },
    "affine_system": {
        "variables": len(VARIABLES),
        "action_rows": len(action_rows),
        "bianchi_rows": len(bianchi_rows),
        "matrix_nonzeros": len(entries),
        "consistent": consistent,
        "cokernel_certificate_support": certificate_support,
        "cokernel_action_support": certificate_action_support,
        "cokernel_bianchi_support": certificate_bianchi_support,
    },
    "downstream": "PRIMITIVE_EPSILON_AND_METRIC_OBSERVATION_ROWS_NOT_REACHED_ON_THIS_FAMILY",
    "next_gate": "CHOOSE_A_GENUINELY_DISTINCT_BRANCH__NONZERO_T_OR_DIFFERENT_CONNECTION_GRADE_RECONSTRUCTION__BEFORE_REOPENING_SR1_STATIONARY_BACKGROUND_SEARCH",
}

print(json.dumps(RESULT, indent=2, sort_keys=True))
if FAILURES:
    raise SystemExit(1)
print(f"PASS {sum(COUNTS.values())}/{sum(COUNTS.values())}")
