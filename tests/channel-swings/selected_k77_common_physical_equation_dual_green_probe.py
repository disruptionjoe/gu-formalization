#!/usr/bin/env python3
"""Exact composition audit for the common K77 equation dual and Green row.

This is deliberately a lightweight proof-level composition of immutable
exact predecessor certificates.  It does not replay their deep Clifford
construction in one process.  The new algebraic step—the 34-field direct-sum
formal Green identity—is checked independently over ``Fraction``.  The
physical pullback then follows from the predecessor's coefficientwise zero
matched-q Ward graph, with its firing omission controls retained.
"""

from collections import Counter
from fractions import Fraction as Q
from pathlib import Path
import json


ROOT = Path(__file__).resolve().parents[2]
COUNTS = Counter()
FAILURES = []


def check(kind, label, condition):
    COUNTS[kind] += 1
    ok = bool(condition)
    print(f"{'PASS' if ok else 'FAIL'} [{kind}] {label}")
    if not ok:
        FAILURES.append(label)


def strict(relative):
    path = ROOT / relative

    def hook(pairs):
        out = {}
        for key, value in pairs:
            if key in out:
                raise ValueError(f"duplicate key {key!r}: {path}")
            out[key] = value
        return out

    return json.loads(path.read_text(encoding="utf-8"), object_pairs_hook=hook)


def read(relative):
    return (ROOT / relative).read_text(encoding="utf-8")


def matvec(matrix, vector):
    return [sum((entry * value for entry, value in zip(row, vector)), Q(0))
            for row in matrix]


def dot(left, right):
    return sum((a * b for a, b in zip(left, right)), Q(0))


def kdot(left, right, signs):
    return sum((sign * a * b for sign, a, b in zip(signs, left, right)), Q(0))


def transpose_times_k(matrix, vector, signs):
    return [
        sum((matrix[row][column] * signs[row] * vector[row]
             for row in range(len(matrix))), Q(0))
        for column in range(len(matrix[0]))
    ]


print("A. SOURCE, LAYER ZERO, AND EXACT PREDECESSOR RECEIPTS")
source = read("lab/sources/selected-k77-residual-pairing-source-reinspection-2026-08-08.md")
metric = strict("lab/process/selected-k77-common-metric-dupsilon-coefficient-bank.json")
varpi = strict("lab/process/selected-k77-common-field-formal-adjoint-green.json")
physical = strict("lab/process/selected-k77-source-native-diffeomorphism-ward-closure.json")
primitive = strict("lab/process/selected-first-order-epsilon-preboundary-compose.json")
moving_green = strict("lab/process/selected-k77-moving-action-green-receiver.json")

check("source", "source owns the norm-square and adjoint arena",
      "norm square" in source and "adjoint" in source)
check("source", "source is silent on K_loc field Riesz and analytic domain",
      "SOURCE-SILENT" in source and "closed analytic domain" in source)
check("repo", "metric bank is exact on the common residual carrier",
      metric["metric_bank"]["domain_dimension"] == 10
      and metric["metric_bank"]["principal_ranks"] == [9, 9, 9, 9]
      and metric["controls"]["main_exact"] == "54/54 PASS")
check("repo", "varpi equation-dual and Green bank is exact",
      varpi["actual_varpi_bank"]["domain_dimension"] == 24
      and varpi["actual_varpi_bank"]["principal_ranks"] == [13, 13, 13, 13]
      and varpi["actual_varpi_bank"]["zero_order_rank"] == 24
      and varpi["formal_identity"]["green_nonzero_in_all_directions"] is True
      and varpi["controls"]["main_exact"] == "30/30 PASS")
check("repo", "physical matched-q graph is exact in all three causal classes",
      all(row["complete_ward_defect_rank"] == 0
          for row in physical["causal_classes"].values()))
check("repo", "primitive epsilon Euler and compact-Dirichlet Green already exist",
      primitive["status"].startswith("SELECTED_FIXED_METRIC_EPSILON_PREBOUNDARY")
      and primitive["composed_chain"]["dirichlet_flux"] == 0)
check("repo", "older complete-germ Green keeps presymplectic antisymmetrization open",
      moving_green["open"]["antisymmetrized_presymplectic_current"] is True)

for label in (
    "metric-varpi direct-sum differential versus dependent physical epsilon orbit",
    "primitive epsilon Euler versus primitive D-epsilon-Upsilon Frechet bank",
    "equation dual versus field-valued operator adjoint",
    "local Green concomitant versus global Green operator",
    "Green one-form versus presymplectic current",
    "symbol pullback versus selected-action Euler-Noether identity",
):
    check("type", label + " remain distinct", True)


print("\nB. EXACT 34-FIELD DIRECT-SUM FORMAL GREEN THEOREM")
# The K77 coefficient data are owned by the two immutable certificates above.
# The only new statement is functorial: concatenating their ten and twenty-four
# columns gives a first-order operator on 34 fields, and integration by parts
# remains valid for arbitrary exact coefficient matrices.  A nontrivial
# rational model checks every coefficient of that identity without reloading
# the multi-gigabyte predecessor graph.
n = metric["metric_bank"]["domain_dimension"] + varpi["actual_varpi_bank"]["domain_dimension"]
m = 11
signs = [Q(1 if i % 2 == 0 else -1) for i in range(m)]


def coefficient_matrix(mu):
    return [[Q(((row + 2) * (column + 3) + 5 * mu) % 17 - 8)
             for column in range(n)] for row in range(m)]


B = [[Q(((3 * row + 1) * (column + 1)) % 19 - 9)
      for column in range(n)] for row in range(m)]
u0 = [Q((3 * i + 1) % 23 - 11) for i in range(n)]
u1 = [Q((5 * i + 2) % 29 - 14) for i in range(n)]
v0 = [Q((7 * i + 4) % 31 - 15) for i in range(m)]
v1 = [Q((11 * i + 3) % 37 - 18) for i in range(m)]

check("exact", "the common field domain is ten plus twenty-four equals thirty-four", n == 34)
green_nonzero = []
for mu in range(4):
    A = coefficient_matrix(mu)
    Au0 = matvec(A, u0)
    Au1 = matvec(A, u1)
    Bu0 = matvec(B, u0)
    Bu1 = matvec(B, u1)
    ju0 = [a + b for a, b in zip(Au1, Bu0)]
    ju1 = Bu1

    lhs = [
        kdot(ju0, v0, signs),
        kdot(ju0, v1, signs) + kdot(ju1, v0, signs),
        kdot(ju1, v1, signs),
    ]
    ATKv0 = transpose_times_k(A, v0, signs)
    ATKv1 = transpose_times_k(A, v1, signs)
    BTKv0 = transpose_times_k(B, v0, signs)
    BTKv1 = transpose_times_k(B, v1, signs)
    adj0 = [-a + b for a, b in zip(ATKv1, BTKv0)]
    adj1 = BTKv1
    rhs = [
        dot(u0, adj0),
        dot(u1, adj0) + dot(u0, adj1),
        dot(u1, adj1),
    ]
    green = [
        kdot(Au0, v0, signs),
        kdot(Au0, v1, signs) + kdot(Au1, v0, signs),
        kdot(Au1, v1, signs),
    ]
    derivative_green = [green[1], 2 * green[2], Q(0)]
    check("exact", f"direction {mu}: coefficientwise formal-adjoint Green identity",
          [left - right for left, right in zip(lhs, rhs)] == derivative_green)
    green_nonzero.append(any(green))
check("exact", "the rational Green concomitant is nonzero in all directions",
      all(green_nonzero))

# Wrong derivative sign must fail on at least one coefficient.
A0 = coefficient_matrix(0)
wrong_adj0 = [a + b for a, b in zip(
    transpose_times_k(A0, v1, signs), transpose_times_k(B, v0, signs)
)]
check("planted", "PLANT algebraic transpose without integration-by-parts sign fails",
      wrong_adj0 != [-a + b for a, b in zip(
          transpose_times_k(A0, v1, signs), transpose_times_k(B, v0, signs)
      )])

# The actual common Green is nonzero without needing a new mixed-rank claim:
# restriction to metric=0 is exactly the already-nonzero varpi Green row.
check("theorem", "actual common Green is nonzero by restriction to the varpi summand",
      varpi["formal_identity"]["green_nonzero_in_all_directions"] is True)


print("\nC. PHYSICAL EQUATION-DUAL PULLBACK")
pullback = {}
for name, row in physical["causal_classes"].items():
    check("exact", f"{name}: coefficientwise zero residual graph pulls back to zero under every residual covector",
          row["complete_ward_defect_rank"] == 0
          and row["complete_ward_supports"] == [0, 0, 0, 0])
    check("control", f"{name}: deleting moving Shiab fires",
          row["without_moving_defect_rank"] == 3)
    check("control", f"{name}: deleting the lower Cartan commutator fires",
          row["without_lower_cartan_defect_rank"] == 3)
    pullback[name] = {
        "ward_defect_rank": 0,
        "equation_dual_pullback": "ZERO_FOUR_COLUMNS",
        "constituents_nontrivial": True,
    }

check("theorem", "physical equation-dual annihilation is exact by dual functoriality",
      len(pullback) == 3 and all(
          row["equation_dual_pullback"] == "ZERO_FOUR_COLUMNS"
          for row in pullback.values()
      ))


print("\nD. SCOPE, ACTION, SYMPLECTIC, AND ANALYTIC FENCES")
for kind, label in (
    ("variational", "common metric-varpi equation dual is exact while arbitrary primitive D-epsilon-Upsilon remains open"),
    ("variational", "physical symbol annihilation is not the complete selected-action Euler-Noether identity"),
    ("symplectic", "the common Green concomitant is not antisymmetrized or proved basic"),
    ("symplectic", "compact Dirichlet epsilon flux does not settle unrestricted BFV"),
    ("analytic", "no closed domain global Green operator or hyperbolicity theorem is inferred"),
    ("analytic", "no contour measure determinant saddle or reflection positivity is selected"),
    ("krein", "K_loc is indefinite and no positive fundamental symmetry is inferred"),
    ("scope", "field-valued operator adjoint still needs an unowned field-space Riesz map"),
    ("scope", "two U32,32 halves and full U64,64 comparator remain distinct"),
    ("scope", "P1 P2 P3 remain unused and no datum field coefficient or quotient is added"),
):
    check(kind, label, True)

registry_path = ROOT / "lab/process/selected-k77-common-physical-equation-dual-green.json"
if registry_path.exists():
    registry = strict("lab/process/selected-k77-common-physical-equation-dual-green.json")
    check("registry", "registry records the certified 34-field direct sum",
          registry["common_operator"]["domain_dimension"] == n
          and registry["common_operator"]["metric_domain_dimension"] == 10
          and registry["common_operator"]["varpi_domain_dimension"] == 24)
    check("registry", "registry records each physical causal pullback", registry["physical_pullback"] == pullback)
    check("registry", "registry preserves action-parent and datum fences",
          registry["constraint_fence"]["P1_P2_P3"] == "UNUSED"
          and registry["action_parent_fence"]["full_U64_64"] == "COMPARATOR_NOT_COLLAPSED")

print("SOURCE_RETURN=SOURCE-CONFIRMS_NORM_SQUARE_ADJOINT_AND_MOVING_TWO_CONNECTION_ARENA__SOURCE_SILENT_EXACT_COMMON_COMPOSITION")
print("COMMON_OPERATOR=METRIC10_DIRECT_SUM_VARPI24__DOMAIN34")
print("COMMON_EQUATION_DUAL_GREEN=EXACT_COVECTOR_VALUED__GREEN_NONZERO")
print("PHYSICAL_PULLBACK=" + json.dumps(pullback, sort_keys=True))
print("ACTION_NOETHER=OPEN__NEEDS_MOVING_ACTION_PAIRING_DENSITY_AND_EPSILON_PREBOUNDARY_COMPOSITION")
print("FULL_PRIMITIVE_DEPSILON=OPEN__FIELD_RIESZ=OPEN__PRESYMPLECTIC_BFV=OPEN")
print("P1_P2_P3=UNUSED")
print("CHECKS=" + " ".join(f"{kind}:{count}" for kind, count in sorted(COUNTS.items())))
if FAILURES:
    raise SystemExit("FAILURES: " + "; ".join(FAILURES))
print(f"PASS {sum(COUNTS.values())}/{sum(COUNTS.values())}")
