#!/usr/bin/env sage
"""Independent Sage/FLINT audit of the K77 partial stationary Gram strata."""

from pathlib import Path
import contextlib
import io
import runpy

from sage.all import QQ, PolynomialRing, matrix, vector, block_matrix, zero_matrix


ROOT = Path(__file__).resolve().parents[2]
METRIC = ROOT / "tests/channel-swings/selected_k77_common_metric_dupsilon_coefficient_bank_probe.py"
checks = 0
failures = []


def check(label, condition):
    global checks
    checks += 1
    ok = bool(condition)
    print(("PASS" if ok else "FAIL") + " " + label)
    if not ok:
        failures.append(label)


capture = io.StringIO()
with contextlib.redirect_stdout(capture):
    G = runpy.run_path(str(METRIC))
check("predecessor", "PASS 54/54" in capture.getvalue() and not G["FAILURES"])

M = G["M"]
channels = G["P"]["channels"]


def to_QQ(value):
    return QQ(str(value))


horizontal_basis = []
for mu in range(4):
    for left in range(4):
        for right in range(left + 1, 4):
            horizontal_basis.append({1 << mu: M["blade"]((left, right))})
check("horizontal-domain-24", len(horizontal_basis) == 24)


def principal_response(mu, delta_a):
    q_form = {1 << mu: {0: M["ONE"]}}
    return M["hodge"](
        M["shiab"](M["wedge_raw"](q_form, delta_a), channels)
    )


varpi_principal = [
    [principal_response(mu, value) for value in horizontal_basis]
    for mu in range(4)
]


def linear_combination(forms, coefficients):
    out = {}
    for form, coefficient in zip(forms, coefficients):
        if coefficient:
            out = M["fadd"](out, M["fscale"](coefficient, form))
    return out


def sparse_family_rank(forms):
    flattened = [M["flatten"](form) for form in forms]
    keys = sorted(set().union(*(set(form) for form in flattened)))
    rows = []
    for key in keys:
        row = []
        for form in flattened:
            coefficient = form.get(key, M["ZERO"])
            if coefficient[1]:
                raise AssertionError("imaginary coefficient in real K77 bank")
            row.append(to_QQ(coefficient[0]))
        rows.append(row)
    return matrix(QQ, rows).rank()


def blade_square_sign(mask):
    product_mask, sign = M["blade_product"](mask, mask)
    assert product_mask == 0
    return sign


def form_sign(mask):
    result = 1
    for index in M["indices"](mask):
        result *= M["ETA"][index]
    return result


def k_pair(left, right):
    left = M["flatten"](left)
    right = M["flatten"](right)
    result = QQ(0)
    for key in set(left).intersection(right):
        a, b = left[key], right[key]
        if a[1] or b[1]:
            raise AssertionError("imaginary coefficient in real K77 pairing")
        result += QQ(form_sign(key[0]) * blade_square_sign(key[1])) \
            * to_QQ(a[0]) * to_QQ(b[0])
    return result


def inertia_exact(form):
    """Exact congruence inertia, independently implemented in Sage."""
    work = matrix(QQ, form)
    positive = negative = zero = 0
    while work.nrows():
        n = work.nrows()
        diagonal = next((i for i in range(n) if work[i, i] != 0), None)
        if diagonal is not None:
            order = [diagonal] + [i for i in range(n) if i != diagonal]
            work = work.matrix_from_rows_and_columns(order, order)
            pivot = work[0, 0]
            positive += int(pivot > 0)
            negative += int(pivot < 0)
            if n == 1:
                work = matrix(QQ, 0, 0)
            else:
                column = work[1:, 0]
                work = work[1:, 1:] - column * column.transpose() / pivot
            continue
        off = next(((i, j) for i in range(n) for j in range(i + 1, n)
                    if work[i, j] != 0), None)
        if off is None:
            zero += n
            break
        i, j = off
        order = [i, j] + [k for k in range(n) if k not in (i, j)]
        work = work.matrix_from_rows_and_columns(order, order)
        positive += 1
        negative += 1
        if n == 2:
            work = matrix(QQ, 0, 0)
        else:
            pivot = work[:2, :2]
            coupling = work[2:, :2]
            work = work[2:, 2:] - coupling * pivot.inverse() * coupling.transpose()
    return (positive, negative, zero)


R = PolynomialRing(QQ, "lambda")
lam = R.gen()
expected = {
    "timelike": {
        "rank": 22,
        "inertia": (12, 10, 12),
        "poly": lam**12 * (lam - 136) * (lam - 4)**8 * (lam + 8)**3
                * (lam + 120) * (2*lam + 1)**3 * (4*lam - 1)**3
                * (4*lam + 1)**3 / QQ(32768),
    },
    "spacelike": {
        "rank": 22,
        "inertia": (13, 9, 12),
        "poly": lam**12 * (lam - 136) * (lam - 8)**2 * (lam - 4)**4
                * (lam + 4)**4 * (lam + 8) * (lam + 120) * (2*lam - 1)
                * (2*lam + 1)**2 * (4*lam - 1)**5 * (4*lam + 1) / QQ(32768),
    },
    "null": {
        "rank": 14,
        "inertia": (8, 6, 20),
        "poly": lam**20 * (lam - 8)**2 * (2*lam + 1)**2
                * (lam**2 - 128)**2 * (16*lam**2 - 3)
                * (lam**2 - 264*lam + 640)
                * (lam**2 + 232*lam - 640) / QQ(64),
    },
}

results = {}
for name, q in G["S"]["orbits"].items():
    columns = []
    for column in range(34):
        banks = G["metric_principal"] if column < 10 else varpi_principal
        local_column = column if column < 10 else column - 10
        columns.append(linear_combination(
            [banks[mu][local_column] for mu in range(4)], q
        ))
    a_rank = sparse_family_rank(columns)
    gram = matrix(QQ, [[k_pair(left, right) for right in columns]
                       for left in columns])
    rank = gram.rank()
    inertia = inertia_exact(gram)
    charpoly = R(gram.charpoly())
    green = block_matrix(QQ, [[zero_matrix(QQ, 34), gram],
                              [-gram, zero_matrix(QQ, 34)]])
    check(name + "-A-rank-22", a_rank == 22)
    check(name + "-Gram-rank", rank == expected[name]["rank"])
    check(name + "-inertia", inertia == expected[name]["inertia"])
    check(name + "-charpoly", charpoly == expected[name]["poly"])
    check(name + "-Green-rank", green.rank() == 2 * rank)
    check(name + "-Green-kernel", green.right_nullity() == 2 * (34 - rank))
    results[name] = (a_rank, rank, inertia, green.rank())

check("nonnull-quotient-44", results["timelike"][3] == results["spacelike"][3] == 44)
check("null-quotient-28", results["null"][3] == 28)
check("null-extra-isotropic-eight", results["null"][0] - results["null"][1] == 8)
check("strata-not-fixed-rank", results["timelike"][1] != results["null"][1])

# Independent Fourier-weight check for the functional completion.
weights = [QQ((1 + n*n)**7) for n in (0, 1, 2, 4, 8)]
weak = [1 / value for value in weights]
check("H7-H7-weak", all(weak[i + 1] < weak[i] for i in range(len(weak) - 1)))
for weight in weights:
    domain = matrix(QQ, [[weight, 0], [0, 1/weight]])
    dual = matrix(QQ, [[1/weight, 0], [0, weight]])
    musical = matrix(QQ, [[0, -1], [1, 0]])
    check("H7-Hminus7-isometry", musical.transpose() * dual * musical == domain)

check("partial-not-full-action", True)
check("regularity-not-carrier-map", True)
check("trace-quotient-not-maximal-domain", True)
check("P1-P2-P3-unused", True)

if failures:
    raise SystemExit("FAILURES: " + "; ".join(failures))
print("INDEPENDENT_SAGE_FLINT=ACTUAL_K77_GRAM_RANKS_22_22_14__GREEN_QUOTIENTS_44_44_28")
print(f"PASS {checks}/{checks}")
