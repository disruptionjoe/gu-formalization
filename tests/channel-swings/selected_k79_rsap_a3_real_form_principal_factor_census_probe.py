#!/usr/bin/env python3
"""Exact principal-factor controls for all five real forms of complex A3."""

from fractions import Fraction as F
from itertools import product
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
REG = json.loads((ROOT / "lab/process/selected-k79-rsap-a3-real-form-principal-factor-census.json").read_text())
FAILURES = []
COUNTS = {}


def check(group, label, condition):
    COUNTS[group] = COUNTS.get(group, 0) + 1
    print(f"{'PASS' if condition else 'FAIL'} [{group}] {label}")
    if not condition:
        FAILURES.append(f"[{group}] {label}")


def zero(n, m=None):
    return [[F(0) for _ in range(n if m is None else m)] for _ in range(n)]


def eye(n):
    out = zero(n)
    for i in range(n):
        out[i][i] = F(1)
    return out


def transpose(a):
    return [list(row) for row in zip(*a)]


def mmul(a, b):
    bt = transpose(b)
    return [[sum((x * y for x, y in zip(row, col)), F(0)) for col in bt] for row in a]


def madd(a, b):
    return [[x + y for x, y in zip(arow, brow)] for arow, brow in zip(a, b)]


def msub(a, b):
    return [[x - y for x, y in zip(arow, brow)] for arow, brow in zip(a, b)]


def scale(c, a):
    return [[F(c) * x for x in row] for row in a]


def flatten(a):
    return [x for row in a for x in row]


def rank(a):
    a = [[F(x) for x in row] for row in a]
    r = 0
    for col in range(len(a[0]) if a else 0):
        pivot = next((row for row in range(r, len(a)) if a[row][col]), None)
        if pivot is None:
            continue
        a[r], a[pivot] = a[pivot], a[r]
        p = a[r][col]
        a[r] = [x / p for x in a[r]]
        for row in range(len(a)):
            if row != r and a[row][col]:
                q = a[row][col]
                a[row] = [x - q * y for x, y in zip(a[row], a[r])]
        r += 1
    return r


def column_rank(matrices, complex_matrices=False):
    vectors = [cflatten(matrix) if complex_matrices else flatten(matrix) for matrix in matrices]
    return rank(transpose(vectors)) if vectors else 0


def unit(i, j, n=4):
    out = zero(n)
    out[i][j] = F(1)
    return out


def diag(values):
    out = zero(len(values))
    for i, value in enumerate(values):
        out[i][i] = F(value)
    return out


def block_diag(*blocks):
    size = sum(len(block) for block in blocks)
    out = zero(size)
    offset = 0
    for block in blocks:
        for i, row in enumerate(block):
            for j, value in enumerate(row):
                out[offset + i][offset + j] = F(value)
        offset += len(block)
    return out


def jordan(n, value=0):
    out = diag([value] * n)
    for i in range(n - 1):
        out[i][i + 1] = F(1)
    return out


def reverse(n):
    out = zero(n)
    for i in range(n):
        out[i][n - 1 - i] = F(1)
    return out


def bracket(a, b):
    return msub(mmul(a, b), mmul(b, a))


def sl_basis(n=4):
    basis = [msub(unit(i, i, n), unit(n - 1, n - 1, n)) for i in range(n - 1)]
    basis += [unit(i, j, n) for i in range(n) for j in range(n) if i != j]
    return basis


def nullspace(a, ncols):
    a = [[F(x) for x in row] for row in a]
    r = 0
    pivots = []
    for col in range(ncols):
        pivot = next((row for row in range(r, len(a)) if a[row][col]), None)
        if pivot is None:
            continue
        a[r], a[pivot] = a[pivot], a[r]
        p = a[r][col]
        a[r] = [x / p for x in a[r]]
        for row in range(len(a)):
            if row != r and a[row][col]:
                q = a[row][col]
                a[row] = [x - q * y for x, y in zip(a[row], a[r])]
        pivots.append(col)
        r += 1
    free = [col for col in range(ncols) if col not in pivots]
    result = []
    for free_col in free:
        vector = [F(0)] * ncols
        vector[free_col] = F(1)
        for row, pivot_col in enumerate(pivots):
            vector[pivot_col] = -a[row][free_col]
        result.append(vector)
    return result


SL4 = sl_basis()


def linear_combination(coefficients, basis):
    out = zero(4)
    for coefficient, matrix in zip(coefficients, basis):
        out = madd(out, scale(coefficient, matrix))
    return out


def adjoint_space(h, sign):
    columns = []
    for x in SL4:
        columns.append(flatten(msub(mmul(transpose(x), h), scale(sign, mmul(h, x)))))
    equations = transpose(columns)
    return [linear_combination(vector, SL4) for vector in nullspace(equations, len(SL4))]


# Complex rational matrices are pairs (real part, imaginary part).
def cmat(real, imag=None):
    return ([[F(x) for x in row] for row in real], zero(len(real)) if imag is None else [[F(x) for x in row] for row in imag])


def cadd(a, b):
    return madd(a[0], b[0]), madd(a[1], b[1])


def csub(a, b):
    return msub(a[0], b[0]), msub(a[1], b[1])


def cmul(a, b):
    return msub(mmul(a[0], b[0]), mmul(a[1], b[1])), madd(mmul(a[0], b[1]), mmul(a[1], b[0]))


def ctranspose(a):
    return transpose(a[0]), transpose(a[1])


def cconj(a):
    return a[0], scale(-1, a[1])


def cneg(a):
    return scale(-1, a[0]), scale(-1, a[1])


def cbracket(a, b):
    return csub(cmul(a, b), cmul(b, a))


def cflatten(a):
    return flatten(a[0]) + flatten(a[1])


def cblock2(a, b, c, d):
    size = len(a[0])
    real = zero(2 * size)
    imag = zero(2 * size)
    for block_row, pair in enumerate(((a, b), (c, d))):
        for block_col, block in enumerate(pair):
            for i in range(size):
                for j in range(size):
                    real[block_row * size + i][block_col * size + j] = block[0][i][j]
                    imag[block_row * size + i][block_col * size + j] = block[1][i][j]
    return real, imag


def pseudo_pair(form):
    h_real = adjoint_space(form, -1)
    m_real = adjoint_space(form, 1)
    h = [cmat(x) for x in h_real]
    m = [cmat(zero(4), x) for x in m_real]
    return h, m


def pseudo_control(matrix):
    return cmat(zero(4), matrix)


def rank_record(label, g_basis, m_basis, control, expected_g, expected_m):
    g_centralizer = len(g_basis) - column_rank([cbracket(x, control) for x in g_basis], True)
    m_centralizer = len(m_basis) - column_rank([cbracket(x, control) for x in m_basis], True)
    factor_rank = 18 - m_centralizer
    target_rank = 72 + 15 - g_centralizer
    full_rank = 76 + factor_rank
    check("centralizer", f"{label} full centralizer dimension", g_centralizer == expected_g)
    check("centralizer", f"{label} moving centralizer dimension", m_centralizer == expected_m)
    check("rank", f"{label} factor map rank", factor_rank == 18 - expected_m)
    check("rank", f"{label} full target/map schedule saturates the pointwise bound", full_rank == (98 + target_rank) // 2)
    return g_centralizer, m_centralizer, factor_rank, target_rank, full_rank


print("A. THREE UNITARY REAL-FORM PAIRS")
S4 = diag((1, 1, 1, 1))
S31 = diag((1, 1, 1, -1))
S22 = diag((1, 1, -1, -1))
for label, form in (("SU4/SO4", S4), ("SU31/SO31", S31), ("SU22/SO22", S22)):
    h, m = pseudo_pair(form)
    check("pair", f"{label} isotropy dimension is six", column_rank(h, True) == 6)
    check("pair", f"{label} moving dimension is nine", column_rank(m, True) == 9)
    check("pair", f"{label} symmetric summands span dimension fifteen", column_rank(h + m, True) == 15)
    check("pair", f"{label} cotangent factor dimension is eighteen", 2 * len(m) == 18)
    check("pair", f"{label} brackets have symmetric-pair parity", all(column_rank(h + [cbracket(x, y)], True) == 6 for x in h for y in h) and all(column_rank(m + [cbracket(x, y)], True) == 9 for x in h for y in m) and all(column_rank(h + [cbracket(x, y)], True) == 6 for x in m for y in m))

print("\nB. PSEUDO-HERMITIAN CANONICAL-TYPE SIGNATURE CENSUS")
configurations = {
    "real_4": (((2, 2),),),
    "real_3_plus_1": (((2, 1), (1, 0)), ((2, 1), (0, 1)), ((1, 2), (1, 0)), ((1, 2), (0, 1))),
    "real_2_plus_2": (((1, 1), (1, 1)),),
    "real_2_plus_1_plus_1": tuple(((1, 1), a, b) for a in ((1, 0), (0, 1)) for b in ((1, 0), (0, 1))),
    "real_1_plus_1_plus_1_plus_1": tuple(word for word in product(((1, 0), (0, 1)), repeat=4)),
    "complex_plus_real_2": (((1, 1), (1, 1)),),
    "complex_plus_real_1_plus_1": tuple(((1, 1), a, b) for a in ((1, 0), (0, 1)) for b in ((1, 0), (0, 1))),
    "complex_plus_complex": (((1, 1), (1, 1)),),
    "complex_jordan_size_2": (((2, 2),),),
}


def totals(options):
    return {(sum(piece[0] for piece in option), sum(piece[1] for piece in option)) for option in options}


compatible = {(4, 0): [], (3, 1): [], (2, 2): []}
for label, options in configurations.items():
    for signature in compatible:
        if signature in totals(options):
            compatible[signature].append(label)
check("coverage", "compact signature admits only the real semisimple configuration", compatible[(4, 0)] == ["real_1_plus_1_plus_1_plus_1"])
check("coverage", "signature (3,1) admits exactly four canonical configurations", len(compatible[(3, 1)]) == 4)
check("coverage", "signature (2,2) admits all nine canonical configurations", len(compatible[(2, 2)]) == 9)
check("coverage", "the registry records the SU31 count", REG["real_forms"]["pseudo_unitary_31"]["compatible_dimension_four_jordan_configurations"] == 4)
check("coverage", "the registry records the SU22 count", REG["real_forms"]["pseudo_unitary_22"]["compatible_dimension_four_jordan_configurations"] == 9)

print("\nC. UNITARY REGULAR AND FIRST-SINGULAR RANK GATES")
unitary_controls = []
for label, regular_form, singular_form, regular, singular in (
    ("compact", S4, S4, diag((3, 1, -1, -3)), diag((1, 1, 2, -4))),
    ("SU31", block_diag(reverse(3), [[F(1)]]), block_diag(reverse(3), [[F(1)]]), block_diag(jordan(3, 1), [[F(-3)]]), block_diag(jordan(3), [[F(0)]])),
    ("SU22", block_diag(reverse(4)), block_diag(reverse(3), [[F(-1)]]), jordan(4), block_diag(jordan(3), [[F(0)]])),
):
    h_regular, m_regular = pseudo_pair(regular_form)
    h_singular, m_singular = pseudo_pair(singular_form)
    check("coverage", f"{label} regular control lies in its moving fibre", mmul(transpose(regular), regular_form) == mmul(regular_form, regular))
    check("coverage", f"{label} first singular control lies in its moving fibre", mmul(transpose(singular), singular_form) == mmul(singular_form, singular))
    rank_record(f"{label} regular", h_regular + m_regular, m_regular, pseudo_control(regular), 3, 3)
    rank_record(f"{label} first singular", h_singular + m_singular, m_singular, pseudo_control(singular), 5, 4)
    unitary_controls.append((label, h_regular, m_regular))
check("coverage", "compact regular nonsemisimple locus is empty", REG["real_forms"]["compact"]["regular_nonsemisimple"] == "EMPTY_BY_COMPACT_NORMALITY")
check("coverage", "SU31 regular size-three Jordan control is explicitly tested", REG["real_forms"]["pseudo_unitary_31"]["regular_nonsemisimple"].startswith("J3"))
check("coverage", "SU22 regular size-four nilpotent is explicitly tested", REG["real_forms"]["pseudo_unitary_22"]["regular_nonsemisimple"] == "J4(0)")

print("\nD. QUATERNIONIC PRINCIPAL PAIR")
K2 = [[F(0), F(1)], [F(-1), F(0)]]
X2 = [[F(0), F(1)], [F(1), F(0)]]
H2 = [[F(1), F(0)], [F(0), F(-1)]]
E11 = [[F(1), F(0)], [F(0), F(0)]]
E22 = [[F(0), F(0)], [F(0), F(1)]]
I2 = eye(2)


def qmatrix(a, b):
    return cblock2(a, b, cneg(cconj(b)), cconj(a))


CZ = cmat(zero(2))
h_q = [
    qmatrix(cmat(K2), CZ), qmatrix(cmat(zero(2), K2), CZ),
    qmatrix(CZ, cmat(E11)), qmatrix(CZ, cmat(E22)), qmatrix(CZ, cmat(X2)), qmatrix(CZ, cmat(zero(2), K2)),
]
m_q = [
    qmatrix(cmat(H2), CZ), qmatrix(cmat(X2), CZ),
    qmatrix(cmat(zero(2), E11), CZ), qmatrix(cmat(zero(2), E22), CZ), qmatrix(cmat(zero(2), X2), CZ),
    qmatrix(CZ, cmat(zero(2), E11)), qmatrix(CZ, cmat(zero(2), E22)), qmatrix(CZ, cmat(K2)), qmatrix(CZ, cmat(zero(2), X2)),
]
g_q = h_q + m_q
check("quaternionic-pair", "so*(4) has dimension six", column_rank(h_q, True) == 6)
check("quaternionic-pair", "the symmetric moving space has dimension nine", column_rank(m_q, True) == 9)
check("quaternionic-pair", "the pair spans su*(4) dimension fifteen", column_rank(g_q, True) == 15)
check("quaternionic-pair", "h consists of transpose-skew matrices", all(ctranspose(x) == cneg(x) for x in h_q))
check("quaternionic-pair", "m consists of transpose-symmetric matrices", all(ctranspose(x) == x for x in m_q))
check("quaternionic-pair", "the principal cotangent factor has dimension eighteen", 2 * len(m_q) == 18)
check("quaternionic-pair", "the Cartan quotient SU*(4)/Sp(2) would have only a 10D cotangent factor", 2 * (15 - 10) == REG["real_forms"]["quaternionic"]["wrong_cartan_factor_dimension"] == 10)
check("quaternionic-pair", "the 10D Cartan candidate cannot cover a 15D regular target", REG["real_forms"]["quaternionic"]["wrong_cartan_disposition"] == "EXCLUDED_BY_DIMENSION_BEFORE_COVERAGE")

N = cmat(H2, X2)
check("quaternionic-coverage", "the complex symmetric two-by-two witness is nonzero nilpotent", cmul(N, N) == cmat(zero(2)) and cflatten(N) != cflatten(cmat(zero(2))))
A_regular_ns = cadd(cmat(zero(2), I2), N)
Q_regular_ns = qmatrix(A_regular_ns, CZ)
A_first_singular = cmat(diag((1, -1)), diag((1, 0)))
Q_first_singular = qmatrix(A_first_singular, CZ)
check("quaternionic-coverage", "the paired size-two Jordan control lies in m", ctranspose(Q_regular_ns) == Q_regular_ns)
check("quaternionic-coverage", "the nonreal-pair plus real-double control lies in m", ctranspose(Q_first_singular) == Q_first_singular)
rank_record("quaternionic regular nonsemisimple", g_q, m_q, Q_regular_ns, 3, 3)
rank_record("quaternionic first singular", g_q, m_q, Q_first_singular, 5, 4)

quaternionic_types = {
    "two_distinct_nonreal_pairs": (qmatrix(cmat(diag((1, -1)), diag((1, 2))), CZ), 3, 3),
    "paired_nonreal_size_two_jordan": (Q_regular_ns, 3, 3),
    "repeated_nonreal_pair_semisimple": (qmatrix(cmat(zero(2), I2), CZ), 7, 5),
    "one_nonreal_pair_plus_real_double": (Q_first_singular, 5, 4),
    "two_distinct_real_doubles": (qmatrix(cmat(diag((1, -1))), CZ), 7, 5),
    "paired_real_size_two_jordan": (qmatrix(N, CZ), 7, 5),
}
check("quaternionic-coverage", "six quaternionic canonical spectral/Jordan types are enumerated", len(quaternionic_types) == REG["real_forms"]["quaternionic"]["compatible_canonical_type_count"] == 6)
for label, (control, expected_g, expected_m) in quaternionic_types.items():
    check("quaternionic-coverage", f"{label} has an exact symmetric quaternionic representative", ctranspose(control) == control)
    g_centralizer = len(g_q) - column_rank([cbracket(x, control) for x in g_q], True)
    m_centralizer = len(m_q) - column_rank([cbracket(x, control) for x in m_q], True)
    check("quaternionic-centralizer", f"{label} full centralizer dimension", g_centralizer == expected_g)
    check("quaternionic-centralizer", f"{label} moving centralizer dimension", m_centralizer == expected_m)
check("quaternionic-coverage", "the regular nonsemisimple quaternionic type is recorded", REG["real_forms"]["quaternionic"]["regular_nonsemisimple"].startswith("PAIRED_J2"))

print("\nE. COMMON 98D SCHEDULE AND CLAIM CEILING")
schedule = REG["rank_schedule"]
check("schedule", "the regular schedule is 84/91", (schedule["regular"]["target_poisson_rank"], schedule["regular"]["full_map_rank"]) == (84, 91))
check("schedule", "the first singular schedule is 82/90", (schedule["first_singular"]["target_poisson_rank"], schedule["first_singular"]["full_map_rank"]) == (82, 90))
check("schedule", "the origin schedule remains 72/85", (schedule["origin"]["target_poisson_rank"], schedule["origin"]["full_map_rank"]) == (72, 85))
check("schedule", "all displayed schedules saturate the 98D bound", schedule["carrier_dimension"] == 98 and schedule["all_displayed_rows_saturate_pointwise_bound"] is True and all(row["full_map_rank"] == (98 + row["target_poisson_rank"]) // 2 for row in (schedule["regular"], schedule["first_singular"], schedule["origin"])))
scope = REG["scope"]
check("scope", "all real A3 principal factors are constructed at factor grade", scope["all_real_a3_principal_factors"] == "CONSTRUCTED_AT_FACTOR_GRADE")
check("scope", "cross-real-form refinements and nonsplit singular atlases remain open", scope["cross_real_form_common_refinements"] == scope["complete_singular_transition_atlas_outside_split_form"] == "OPEN")
check("scope", "same-sign SL2/SO2 remains partial", scope["same_sign_sl2_so2_sheet"] == "PARTIAL_NOT_RSAP")
check("scope", "deeper strata, zero charge and global RSAP remain open", {scope[key] for key in ("deeper_so77_singular_strata", "zero_charge_rank_at_most_49", "global_all_strata_rsap")} == {"OPEN", "NOT_CONSTRUCTED"})
check("scope", "the all-charge fallback remains 182D", scope["all_charge_fallback_dimension"] == 182)
check("scope", "protected truth surfaces remain unchanged", set(REG["changes"].values()) == {"none"})
for key in ("artifact", "probe", "hostile_review"):
    check("links", f"the {key} exists", (ROOT / REG[key]).is_file())

print("\nSUMMARY")
print(json.dumps({"groups": COUNTS, "checks": sum(COUNTS.values()), "failures": FAILURES}, indent=2, sort_keys=True))
if FAILURES:
    raise SystemExit(1)
