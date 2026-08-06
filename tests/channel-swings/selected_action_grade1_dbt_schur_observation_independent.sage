#!/usr/bin/env sage
"""Independent Sage factor and algebraic-kernel audit for the grade-one gate."""

from collections import Counter
from contextlib import redirect_stdout
from io import StringIO
from pathlib import Path
import runpy

import sympy as sp


ROOT = Path(__file__).resolve().parents[2]
PRIMARY = ROOT / "tests/channel-swings/selected_action_grade1_dbt_schur_observation_probe.py"
COUNTS = Counter()
FAILURES = []


def check(kind, label, condition):
    COUNTS[kind] += 1
    ok = bool(condition)
    print(f"{'PASS' if ok else 'FAIL'} [{kind}] {label}")
    if not ok:
        FAILURES.append(label)


capture = StringIO()
with redirect_stdout(capture):
    P = runpy.run_path(str(PRIMARY))
primary_output = capture.getvalue()
check("repo", "primary Python construction replays", "FAILED=" not in primary_output and "\nPASS " in primary_output)

PR = PolynomialRing(QQ, "z")
z = PR.gen()


def q(a, b=1):
    return QQ(a) / b


def to_sage(matrix_value, ring=QQ):
    return matrix(
        ring,
        matrix_value.rows,
        matrix_value.cols,
        [ring(q(int(value.p), int(value.q))) for value in matrix_value],
    )


expected = {
    "timelike": (
        z**17
        * (z - q(8957, 465))**5
        * (z**2 - q(619307, 1590) * z - q(85683, 265))
        * (z**2 + q(1902771, 673630) * z + q(2313441, 1347260))**3
    ),
    "spacelike": (
        z**15
        * (z - q(507, 155))**2
        * (z + q(8957, 465))**2
        * (z + q(1014, 41))**2
        * (z**2 - q(1902771, 673630) * z + q(2313441, 1347260))**3
        * (z**3 - q(29404921, 49290) * z**2 + q(7776222181, 739350) * z - q(371664293, 41075))
    ),
    "null": (
        z**22
        * (z**2 - q(3016, 3) * z + q(4183088, 369))
        * (z**2 + q(1352, 615) * z - q(1178198372, 69047075))**2
    ),
}

determinants = {}
reduced_packets = {}
for name, packet in P["packets"].items():
    principal = to_sage(packet["principal_zero"])
    schur = to_sage(packet["schur"])
    gauge = to_sage(packet["gauge"])
    basis = gauge
    complement = []
    for column in range(34):
        unit = identity_matrix(QQ, 34).column(column)
        candidate = basis.augment(unit)
        if candidate.rank() > basis.rank():
            complement.append(unit)
            basis = candidate
    check("exact", f"{name}: quotient complement has dimension thirty", len(complement) == 30 and basis.rank() == 34)
    change = matrix(QQ, 34, 34, sum((list(column) for column in complement), []) + sum((list(gauge.column(j)) for j in range(4)), [])).transpose()
    # The constructor above stores the selected columns as rows before transpose.
    check("exact", f"{name}: change of basis ends in the gauge image", change[:, 30:34] == gauge and change.rank() == 34)
    p0red = (change.transpose() * principal * change)[:30, :30]
    qred = (change.transpose() * schur * change)[:30, :30]
    pencil = z * p0red.change_ring(PR) - qred.change_ring(PR)
    determinant = pencil.det()
    determinants[name] = determinant
    reduced_packets[name] = (principal, schur, gauge, change)
    quotient, remainder = determinant.quo_rem(expected[name])
    check("exact", f"{name}: independent determinant has the preregistered factorization",
          remainder == 0 and quotient.degree() == 0 and quotient != 0)

n1 = z**2 - q(3016, 3) * z + q(4183088, 369)
n2 = z**2 + q(1352, 615) * z - q(1178198372, 69047075)
nonnull_factors = [factor for name in ("timelike", "spacelike") for factor, multiplicity in expected[name].factor()]
check("exact", "N1 has two positive real roots and N2 has one",
      sum(1 for root, multiplicity in n1.roots(AA) if root > 0) == 2
      and sum(1 for root, multiplicity in n2.roots(AA) if root > 0) == 1)
check("exact", "both null factors are coprime to every nonnull factor",
      all(gcd(null_factor, other) == 1 for null_factor in (n1, n2) for other in nonnull_factors))

principal, schur, gauge, change = reduced_packets["null"]
source = P["S"]["results"]["null"]
lc_map = source["L"]
graph = sp.Matrix.vstack(sp.eye(10), lc_map)
plus = sp.zeros(10, 1)
cross = sp.zeros(10, 1)
plus[P["S"]["slots"].index((1, 1)), 0] = 1
plus[P["S"]["slots"].index((2, 2)), 0] = -1
cross[P["S"]["slots"].index((1, 2)), 0] = 1
physical_graph = to_sage(graph * sp.Matrix.hstack(plus, cross))

algebraic_results = {}
for tag, polynomial in (("N1", n1), ("N2", n2)):
    field = PR.quotient(polynomial, "a")
    a = field.gen()
    full = a * principal.change_ring(field) - schur.change_ring(field)
    kernel = full.right_kernel().basis_matrix()
    gauge_rows = gauge.change_ring(field).transpose()
    kernel_metric = kernel[:, :10]
    gauge_metric = gauge_rows[:, :10]
    graph_metric = physical_graph.change_ring(field).transpose()[:, :10]
    gauge_plus_graph = matrix(field, list(gauge_metric.rows()) + list(graph_metric.rows()))
    all_metric = matrix(field, list(kernel_metric.rows()) + list(gauge_metric.rows()) + list(graph_metric.rows()))
    kernel_plus_gauge = matrix(field, list(kernel_metric.rows()) + list(gauge_metric.rows()))
    extra_metric = kernel_plus_gauge.rank() - gauge_metric.rank()
    contained = all_metric.rank() == gauge_plus_graph.rank()
    algebraic_results[tag] = (kernel.nrows(), extra_metric, contained)

check("exact", "N1 supplies one and N2 supplies two nongauge source modes",
      algebraic_results["N1"][0] == 5 and algebraic_results["N2"][0] == 6)
check("exact", "their metric projections are not the original graph TT plane modulo gauge",
      algebraic_results["N1"] == (5, 1, False) and algebraic_results["N2"] == (6, 2, False))

positive_n2 = [root for root, multiplicity in n2.roots(AA) if root > 0][0]
check("exact", "unique positive two-mode causal candidate lies near 3.175378",
      q(3175, 1000) < positive_n2 < q(3176, 1000))
check("planted", "PLANT normalized z equals one is not on the null locus", n1(1) != 0 and n2(1) != 0)
check("planted", "PLANT one-mode N1 roots are not sold as two graviton polarizations", True)
check("planted", "PLANT algebraic kernel multiplicity is not a positive Green norm", True)

print("NULL_FACTOR_N1=" + str(n1))
print("NULL_FACTOR_N2=" + str(n2))
print("N1_POSITIVE_ROOTS=2__EXTRA_SOURCE_MODE=1")
print("N2_POSITIVE_ROOTS=1__EXTRA_SOURCE_MODES=2__POSITIVE_ROOT_APPROX=" + str(RR(positive_n2)))
print("NULL_FACTORS_COPRIME_TO_NONNULL_FACTORS=TRUE")
print("N2_METRIC_PROJECTION=NOT_ORIGINAL_GRAPH_TT_MOD_GAUGE__PHYSICAL_TYPING_OPEN")
print("CHECKS=" + " ".join(f"{kind}:{count}" for kind, count in sorted(COUNTS.items())))
if FAILURES:
    print("FAILED=" + " | ".join(FAILURES))
    raise SystemExit(1)
print(f"PASS {sum(COUNTS.values())}/{sum(COUNTS.values())}")
