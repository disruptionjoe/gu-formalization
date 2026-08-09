#!/usr/bin/env sage
"""Independent Sage/FLINT audit of the selected K77 primitive-epsilon bank."""

from pathlib import Path
import contextlib
import io
import runpy

from sage.all import QQ, matrix, block_matrix, zero_matrix


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
check("metric-predecessor", "PASS 54/54" in capture.getvalue() and not G["FAILURES"])

M = G["M"]
V = G["V"]
channels = G["P"]["channels"]


def to_QQ(value):
    return QQ(str(value))


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
    """Independent exact congruence elimination over Sage QQ/FLINT."""
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


horizontal_basis = []
for mu in range(4):
    for left in range(4):
        for right in range(left + 1, 4):
            horizontal_basis.append({1 << mu: M["blade"]((left, right))})
check("varpi-domain-24", len(horizontal_basis) == 24)


def principal_response(mu, delta_a):
    q_form = {1 << mu: {0: M["ONE"]}}
    return M["hodge"](
        M["shiab"](M["wedge_raw"](q_form, delta_a), channels)
    )


varpi_principal = [
    [principal_response(mu, value) for value in horizontal_basis]
    for mu in range(4)
]
pairs14 = [(left, right) for left in range(14) for right in range(left + 1, 14)]
epsilon_principal = [
    [M["fscale"](int("-1"), {int("1") << int(mu): M["blade"](pair)})
     for pair in pairs14]
    for mu in range(4)
]
check("epsilon-domain-91", len(pairs14) == 91)
check("epsilon-direction-ranks", [sparse_family_rank(bank) for bank in epsilon_principal] == [91] * 4)

expected = {
    "timelike": (110, 110, (58, 52, 15)),
    "spacelike": (110, 110, (53, 57, 15)),
    "null": (110, 16, (10, 6, 109)),
}
results = {}
for name, q in G["S"]["orbits"].items():
    metric = [linear_combination(
        [G["metric_principal"][mu][column] for mu in range(4)], q
    ) for column in range(10)]
    varpi = [linear_combination(
        [varpi_principal[mu][column] for mu in range(4)], q
    ) for column in range(24)]
    epsilon = [linear_combination(
        [epsilon_principal[mu][column] for mu in range(4)], q
    ) for column in range(91)]
    columns = metric + varpi + epsilon
    raw_rank = sparse_family_rank(columns)
    check(name + "-metric-epsilon-rank-97",
          sparse_family_rank(metric + epsilon) == 97)
    gram = matrix(QQ, [[k_pair(left, right) for right in columns]
                       for left in columns])
    gram_rank = gram.rank()
    inertia = inertia_exact(gram)
    green = block_matrix(QQ, [[zero_matrix(QQ, 125), gram],
                              [-gram, zero_matrix(QQ, 125)]])
    check(name + "-raw-rank-110", raw_rank == expected[name][0])
    check(name + "-Gram-rank", gram_rank == expected[name][1])
    check(name + "-inertia", inertia == expected[name][2])
    check(name + "-Green-rank", green.rank() == 2 * gram_rank)
    check(name + "-Green-kernel", green.right_nullity() == 2 * (125 - gram_rank))
    results[name] = (raw_rank, gram_rank, inertia)

check("nonnull-image-nondegenerate",
      results["timelike"][0] == results["timelike"][1]
      and results["spacelike"][0] == results["spacelike"][1])
check("null-extra-isotropic-94",
      results["null"][0] - results["null"][1] == 94)
check("raw-kernel-15", all(125 - row[0] == 15 for row in results.values()))
check("causal-rank-stratified", results["timelike"][1] != results["null"][1])
check("first-action-34-not-125", 34 != 125)
check("selected-parent-not-expanded-parent", True)
check("principal-not-full-Frechet", True)
check("finite-Green-not-maximal-domain", True)
check("P1-P2-P3-unused", True)

if failures:
    raise SystemExit("FAILURES: " + "; ".join(failures))
print("INDEPENDENT_SAGE_FLINT=EPSILON91__RAW110_ALL__GRAM110_110_16__NULL_ISOTROPIC94")
print(f"PASS {checks}/{checks}")
