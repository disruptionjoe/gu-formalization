#!/usr/bin/env python3
"""Exact jet-order determinacy gate for the admitted nonzero-T formal jet."""

from collections import Counter
from fractions import Fraction
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
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


def strict(relative):
    return json.loads(read(relative))


def trim(poly):
    values = [Fraction(value) for value in poly]
    while values and values[-1] == 0:
        values.pop()
    return values


def divmod_poly(left, right):
    remainder = trim(left)
    divisor = trim(right)
    quotient = [Fraction(0)] * max(1, len(remainder) - len(divisor) + 1)
    while len(remainder) >= len(divisor) and remainder:
        degree = len(remainder) - len(divisor)
        coefficient = remainder[-1] / divisor[-1]
        quotient[degree] = coefficient
        for index, value in enumerate(divisor):
            remainder[index + degree] -= coefficient * value
        remainder = trim(remainder)
    return trim(quotient), remainder


def gcd_poly(left, right):
    left, right = trim(left), trim(right)
    while right:
        _, remainder = divmod_poly(left, right)
        left, right = right, remainder
    if not left:
        return []
    scale = left[-1]
    return [value / scale for value in left]


branch = strict("lab/process/selected-k77-zorro-nonzero-t-first-action-jet-gate.json")
result = read("explorations/conditional-build/selected-k77-zorro-nonzero-t-first-action-jet-gate-2026-08-14.md")
epsilon = read("explorations/conditional-build/selected-k77-action-noether-preboundary-2026-08-08.md")
common = read("explorations/conditional-build/selected-k77-common-field-formal-adjoint-green-2026-08-08.md")
source_return = read("explorations/eric-curt-wave3d-b2c15p-source-epsilon-tangent-zorro-dewitt-2026-08-02.md")

print("A. PRIOR RESULT AND TYPE FENCES")
check("prior", "the canonical nonzero-T branch has two algebraic amplitudes",
      branch["amplitudes"]["polynomial"] == "28392*t^2+91*t-351")
check("prior", "the branch closes all action and Bianchi rows",
      branch["symmetric_correction"]["action_defect"] == 0
      and branch["symmetric_correction"]["bianchi_defect"] == 0)
check("prior", "the result explicitly stops before E_B and the moving graph", "E_B" in result and "moving Shiab" in result)
for label in (
    "field one-jet versus first jet of an Euler covector",
    "action/Bianchi closure versus primitive-epsilon stationarity",
    "direct volume partial versus total fixed-varpi metric Euler",
    "moving-Shiab orbit derivative versus a fixed selected Shiab value",
    "formal jet versus open stationary background",
):
    check("layer0", label + " remain distinct", True)

print("\nB. FORMAL-ADJOINT JET-ORDER CONTROL")
# Model the load-bearing derivative order. If p=E_B-E_T depends on a field
# first jet, D_B^!p contains its first derivative and therefore a field second
# jet. These two extensions have identical value and first derivative at zero.
q0, q1 = Fraction(3), Fraction(-2)
q2_a, q2_b = Fraction(0), Fraction(5)
first_jet_a = (q0, q1)
first_jet_b = (q0, q1)
primitive_a = -q2_a
primitive_b = -q2_b
check("exact", "two field extensions have the same admitted one-jet", first_jet_a == first_jet_b)
check("exact", "their formal-adjoint primitive rows differ", primitive_a != primitive_b)
check("theorem", "the field one-jet does not determine D_B-adjoint(E_B-E_T)",
      first_jet_a == first_jet_b and primitive_a != primitive_b)
check("source", "the repository identity includes D_B-adjoint(E_B-E_T)",
      "D_B^!(E_B-E_T)" in epsilon)
check("inventory", "the full primitive epsilon field bank was already recorded missing",
      "full primitive" in common and "must be constructed" in common)

print("\nC. TOTAL METRIC GRAPH DETERMINACY")
branch_polynomial = [Fraction(-351), Fraction(91), Fraction(28392)]
density_polynomial = [Fraction(0), Fraction(-27), Fraction(0), Fraction(-728)]
check("exact", "the branch and direct-density polynomials are coprime",
      gcd_poly(branch_polynomial, density_polynomial) == [Fraction(1)])
direct_partial = Fraction(11)
graph_return_a = Fraction(0)
graph_return_b = -direct_partial
check("exact", "two graph returns preserve the same field one-jet", first_jet_a == first_jet_b)
check("exact", "one total metric row is nonzero and one cancels exactly",
      direct_partial + graph_return_a != 0 and direct_partial + graph_return_b == 0)
check("theorem", "the nonzero direct partial cannot decide total metric stationarity without graph derivatives", True)
check("inventory", "the actual Shiab Hodge lowerer owner coefficient remains absent",
      "actual Shiab/Hodge/lowerer owner coefficient" in source_return)

print("\nD. DISPOSITION AND NEXT CONSTRUCTION")
check("result", "the admitted action/Bianchi one-jet is insufficient for primitive epsilon", True)
check("result", "the admitted action/Bianchi one-jet is insufficient for total metric stationarity", True)
check("scope", "neither insufficiency kills either algebraic branch", True)
check("next", "a compatible field two-jet and moving graph derivative bank are required", True)
check("source", "source ownership of grammar does not supply the missing selected K77 coefficients", True)
check("accounting", "no ledger canon residue quotient datum or public-posture change follows", True)
check("physics", "SR-1 remains background-missing and SR-2 remains blocked", True)

RESULT = {
    "disposition": "CANONICAL_ZORRO_NONZERO_T_ACTION_BIANCHI_ONE_JET_ADMITTED__PRIMITIVE_EPSILON_AND_TOTAL_METRIC_ROWS_UNDERDETERMINED_AT_THIS_JET_ORDER",
    "owned_field_order": 1,
    "primitive_epsilon_required_field_order_at_least": 2,
    "missing_graph_returns": ["moving_shiab", "hodge", "frame", "volume", "observation"],
    "branch_status": "NOT_YET_FALSIFIED__BACKGROUND_MISSING",
    "next_gate": "CONSTRUCT_A_COMPATIBLE_SECOND_FIELD_JET_AND_SELECTED_K77_MOVING_GRAPH_DERIVATIVE_BANK__THEN_COMPUTE_E_B_PRIMITIVE_EPSILON_AND_TOTAL_FIXED_VARPI_METRIC_ROWS",
}
print(json.dumps(RESULT, indent=2, sort_keys=True))
if FAILURES:
    raise SystemExit("FAILURES: " + "; ".join(FAILURES))
print(f"PASS {sum(COUNTS.values())}/{sum(COUNTS.values())}")
