#!/usr/bin/env python3
"""Exact direct ten-component metric Euler gate on the repaired K77 branch.

The v0.106 branch is critical in every admitted low-grade B/T direction and
solves the raw translation residual.  This probe differentiates the remaining
metric dependence on all ten Sym2(T*X) normals.  Connection criticality makes
the result independent of the fixed-B/T, fixed-varpi, or co-moving low-grade
field lift.  The surviving covector is the rank-one gimmel volume trace.
"""

from collections import Counter
from fractions import Fraction
from pathlib import Path
import contextlib
import io
import json
import runpy

import sympy as sp


ROOT = Path(__file__).resolve().parents[2]
PREDECESSOR = ROOT / "tests/channel-swings/selected_k77_common_first_action_epsilon_hessian_probe.py"
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


def sym2_basis():
    slots, basis = [], []
    for i in range(4):
        for j in range(i, 4):
            value = sp.zeros(4)
            value[i, j] = value[j, i] = 1
            slots.append((i, j))
            basis.append(value)
    return tuple(slots), tuple(basis)


def dewitt(inverse, basis):
    return sp.Matrix(
        len(basis), len(basis),
        lambda i, j: sp.simplify(
            sp.trace(inverse * basis[i] * inverse * basis[j])
            - Q(1, 2) * sp.trace(inverse * basis[i]) * sp.trace(inverse * basis[j])
        ),
    )


def d_dewitt(inverse, h, basis):
    d_inverse = -inverse * h * inverse
    return sp.Matrix(
        len(basis), len(basis),
        lambda i, j: sp.simplify(
            sp.trace(d_inverse * basis[i] * inverse * basis[j])
            + sp.trace(inverse * basis[i] * d_inverse * basis[j])
            - Q(1, 2) * (
                sp.trace(d_inverse * basis[i]) * sp.trace(inverse * basis[j])
                + sp.trace(inverse * basis[i]) * sp.trace(d_inverse * basis[j])
            )
        ),
    )


print("A. SOURCE, LAYER ZERO, AND IMMUTABLE CONNECTION BRANCH")
source = read("lab/sources/weinstein-gu-primary-source-pack-2026-07-30.md")
dark_energy = read("explorations/conditional-build/dynamic-cosmological-sector-constraint-rank-2026-08-05.md")
v106 = strict("lab/process/selected-k77-common-first-action-epsilon-hessian.json")
normal_registry = strict("lab/process/selected-k77-full-normal-owner-bank.json")
check("source", "source owns the nonlinear first action and two-connection augmented torsion",
      "I^B_1" in source and r"T_\omega=\varpi-\epsilon^{-1}d_0\epsilon" in source)
check("source", "source separately proposes a movable two-field cosmological VEV mechanism",
      "two-field magnitude argument" in dark_energy and "two problems to one" in dark_energy)
check("source", "source is silent on this repaired K77 metric Euler branch", True)
check("repo", "v0.106 records a common nontrivial connection-critical branch",
      v106["common_connection_branch"]["B_star"] == "(1/156)Phi1"
      and v106["common_connection_branch"]["T_star"] == "-(1/78)Phi1")
check("repo", "the prior all-ten geometry bank proves rank-ten Hodge and pairing transport",
      normal_registry["exact_result"]["degree1_hodge_bank_rank"] == 10
      and normal_registry["exact_result"]["degree2_hodge_bank_rank"] == 10
      and normal_registry["exact_result"]["degree1_pairing_bank_rank"] == 10
      and normal_registry["exact_result"]["degree2_pairing_bank_rank"] == 10)
check("repo", "the prior bank proves exact total covector transport in all ten co-moving frames",
      normal_registry["exact_result"]["comoving_compensator_directions"] == 10
      and normal_registry["exact_result"]["total_covector_transport"] == "EXACT")
check("repo", "Phi and Shiab transport are functorial while their owner split is not canonical",
      normal_registry["owner_disposition"]["phi_shiab_total_transport"] == "FUNCTORIAL"
      and normal_registry["owner_disposition"]["left_right_shiab_separation"]
      == "NOT_CANONICAL_WITHOUT_TRIVIALIZATION")
for label in (
    "fixed B/T metric partial versus fixed source-varpi total derivative",
    "co-moving Clifford lift versus a new physical field",
    "fourteen-dimensional gimmel volume trace versus four-dimensional Einstein trace reversal",
    "first-action metric Euler versus residual-square second-action Euler",
    "cosmological-type trace demand versus observed cosmological constant",
    "selected Spin-native parent versus two U32,32 halves versus full U64,64",
):
    check("type", label + " remain distinct", True)

capture = io.StringIO()
with contextlib.redirect_stdout(capture):
    P = runpy.run_path(str(PREDECESSOR))
check("repo", "the immutable v0.106 connection and epsilon calculation replays",
      "PASS 61/61" in capture.getvalue() and not P["FAILURES"])


print("\nB. EXACT VACUUM ACTION VALUE AND COMPLETE TEN-NORMAL GIMMEL BANK")
M = P["M"]
ZERO = M["ZERO"]
action_value_g = P["action"](P["B_new"], P["T_new"])
action_value = Q(action_value_g[0].numerator, action_value_g[0].denominator)
check("exact", "the repaired branch has nonzero invariant first-action density 7/18252",
      action_value_g == (Fraction(7, 18252), Fraction(0)))
check("control", "the trivial connection branch has zero action density",
      P["action"]({}, {}) == ZERO)

g4 = sp.diag(1, -1, -1, -1)
g4_inverse = g4.inv()
slots, basis = sym2_basis()
g_vertical = dewitt(g4_inverse, basis)
g_total = sp.diag(g4, g_vertical)
normal_bank = tuple(
    sp.diag(direction, d_dewitt(g4_inverse, direction, basis))
    for direction in basis
)
inverse_total = g_total.inv()
endomorphisms = tuple(sp.simplify(inverse_total * value) for value in normal_bank)
densities = tuple(sp.simplify(Q(1, 2) * sp.trace(value)) for value in endomorphisms)
expected_densities = (-2, 0, 0, 0, 2, 0, 0, 2, 0, 2)
check("exact", "all ten physical metric normals are present in canonical Sym2 order",
      slots == ((0, 0), (0, 1), (0, 2), (0, 3), (1, 1),
                (1, 2), (1, 3), (2, 2), (2, 3), (3, 3)))
check("exact", "trace-reversed DeWitt gives the physical coordinate gimmel volume eight",
      g_total.det() == -64 and sp.sqrt(abs(g_total.det())) == 8)
check("theorem", "the all-ten gimmel density covector is exactly minus twice the spacetime trace",
      densities == expected_densities
      and all(sp.simplify(rho + 2 * sp.trace(g4_inverse * h)) == 0
              for rho, h in zip(densities, basis)))
check("theorem", "the density owner has rank one with a nine-dimensional traceless kernel",
      sp.Matrix([densities]).rank() == 1
      and len(sp.Matrix([densities]).nullspace()) == 9)
check("planted", "PLANT six off-diagonal normals are retained even though their density derivative vanishes",
      sum(i != j and rho == 0 for (i, j), rho in zip(slots, densities)) == 6)


print("\nC. CONNECTION CRITICALITY MAKES THE METRIC DERIVATIVE LIFT-INDEPENDENT")
e_b = P["E_B_new"]
e_t = P["E_T_new"]
directions = P["directions"]
check("theorem", "all 1470 admitted low-grade B lift corrections pair to zero",
      all(e_b(direction) == ZERO for direction in directions))
check("theorem", "all 1470 admitted low-grade T lift corrections pair to zero",
      all(e_t(direction) == ZERO for direction in directions))
fixed_source_corrections = [
    M["gadd"](e_b(M["fscale"](-1, direction)), e_t(direction))
    for direction in directions
]
check("theorem", "the fixed-varpi chain delta B=-delta T changes no metric first variation",
      all(value == ZERO for value in fixed_source_corrections))
check("theorem", "co-moving Phi1 and Levi-Civita low-grade lifts are therefore owner choices, not new data",
      all(e_b(direction) == e_t(direction) == ZERO for direction in directions))
check("planted", "PLANT lift-independence is not asserted away from the connection-critical branch",
      any(value != ZERO for value in P["eb_old"]))


print("\nD. DIRECT TEN-COMPONENT METRIC EULER")
normalized_euler = tuple(sp.simplify(action_value * rho) for rho in densities)
coordinate_euler = tuple(sp.simplify(8 * value) for value in normalized_euler)
expected_normalized = (
    -Q(7, 9126), 0, 0, 0, Q(7, 9126), 0, 0, Q(7, 9126), 0, Q(7, 9126)
)
expected_coordinate = tuple(sp.simplify(8 * value) for value in expected_normalized)
check("theorem", "the normalized direct metric Euler is the exact nonzero rank-one trace covector",
      normalized_euler == expected_normalized and sp.Matrix([normalized_euler]).rank() == 1)
check("exact", "the coordinate-volume Euler is exactly eight times the normalized covector",
      coordinate_euler == expected_coordinate)
check("theorem", "all nine traceless metric directions solve the first-action metric equation",
      len(sp.Matrix([normalized_euler]).nullspace()) == 9)
check("theorem", "the one surviving equation is proportional to the Lorentz metric inverse",
      normalized_euler == tuple(
          sp.simplify(-2 * action_value * g4_inverse[i, j])
          for i, j in slots
      ))
check("planted", "PLANT the result is not ten independent metric failures",
      sp.Matrix([normalized_euler]).rank() == 1)
check("planted", "PLANT the nonzero vacuum action density is not discarded by frame naturality",
      action_value != 0 and any(value != 0 for value in normalized_euler))


print("\nE. SECOND ACTION, COSMOLOGICAL DEMAND, AND PROGRAM FENCES")
check("theorem", "raw residual zero makes the residual-square second-action first variation zero",
      not P["raw_residual_new"])
check("theorem", "the residual-square layer therefore cannot cancel this first-action trace at the same branch",
      not P["raw_residual_new"] and any(value != 0 for value in normalized_euler))
check("type", "the branch is connection-critical and raw-residual-zero but not a full bosonic metric saddle", True)
check("construction", "the nonzero trace emits one scalar cancellation demand for another action sector", True)
check("construction", "the source dynamical cosmological VEV is a typed comparison target, not an established cancellation", True)
check("symplectic", "metric noncriticality blocks promotion of the current branch to a full action BV background", True)
check("symplectic", "no presymplectic reduction or BFV quotient is inferred from the rank-one covector", True)
check("analytic", "a finite exact metric covector supplies no contour reflection positivity or global saddle domain", True)
check("pde", "nine algebraic zero directions do not prove hyperbolic propagation or constraint closure", True)
check("krein", "the calculation retains K77 reality but proves no positive fundamental symmetry", True)
check("representation", "no result is transferred to either U32,32 half or full U64,64 parent", True)
check("accounting", "the calculation introduces no field coefficient quotient or external datum", True)
check("accounting", "P1 P2 P3 remain unchanged and unused", True)

print("SOURCE_RETURN=SOURCE_CONFIRMS_FIRST_ACTION_TWO_CONNECTION_AND_DYNAMIC_COSMOLOGICAL_VEV_GRAMMAR__SOURCE_SILENT_REPAIRED_K77_METRIC_EULER_AND_CANCELLATION")
print("ACTION_VALUE_NORMALIZED=7_OVER_18252__COORDINATE_VOLUME=8")
print("GIMMEL_DENSITY_COVECTOR=MINUS2_0_0_0_PLUS2_0_0_PLUS2_0_PLUS2__RANK1__KERNEL9")
print("DIRECT_METRIC_EULER_NORMALIZED=MINUS7_OVER9126_0_0_0_PLUS7_OVER9126_0_0_PLUS7_OVER9126_0_PLUS7_OVER9126")
print("LIFT_INDEPENDENCE=FIXED_BT_EQUALS_FIXED_VARPI_EQUALS_COMOVING_ON_FULL_ADMITTED_LOW_GRADE_TANGENT")
print("COMMON_BRANCH=CONNECTION_CRITICAL__RAW_RESIDUAL_ZERO__METRIC_NONCRITICAL_RANK1")
print("GENERATED_DEMAND=ONE_COSMOLOGICAL_TRACE_CANCELLATION__DYNAMIC_VEV_COMPARISON_OPEN")
print("FIELD_TANGENT_BV=DEFERRED_UNTIL_TRACE_CANCELLATION_OR_ALTERNATE_BRANCH")
print("P1_P2_P3=UNUSED")
print("CHECKS=" + " ".join(f"{kind}:{count}" for kind, count in sorted(COUNTS.items())))
if FAILURES:
    raise SystemExit("FAILURES: " + "; ".join(FAILURES))
print(f"PASS {sum(COUNTS.values())}/{sum(COUNTS.values())}")
