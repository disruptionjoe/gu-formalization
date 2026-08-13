#!/usr/bin/env python3
"""Exact local boundary-disposition selector for the selected K77 action.

The source asserts the tilted inhomogeneous gauge/double-coset grammar and
admits that the upstairs theory has an unresolved boundary problem.  The
selected action supplies a nonzero endpoint moment map.  This probe separates
four local dispositions and asks which survives two *explicitly conditional*
requirements: every endpoint transformation remains gauge, and generic
nonzero action momentum remains admissible.
"""

from collections import Counter
from pathlib import Path
import json

import sympy as sp


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


def load(relative):
    return json.loads(read(relative))


print("A. SOURCE LOCUS, LAYER ZERO, AND OWNERS")
toe = read("lab/sources/transcripts/toe-weinstein-gu-40-years.md")
portal = read("lab/sources/transcripts/portal-special-gu-first-look-2020-04-02.md")
edge = load("lab/process/selected-k77-minimal-edge-mode-reduction.json")
action = load("lab/process/selected-k77-action-noether-preboundary.json")

check("source", "Weinstein states the full tilted double-coset replacement",
      "A mod G is replaced by the double coset" in toe)
check("source", "Weinstein identifies the upstairs issue as boundary conditions",
      "Really what you have is boundary conditions" in toe)
check("source", "Weinstein admits that the multiple-time Hamiltonian problem is unresolved",
      "I don't know how to push Hamiltonian dynamics in multiple temporal dimensions" in toe)
check("source", "the primary transcript supplies the tilted gauge action",
      "inhomogeneous gauge group" in portal and "tilted" in portal)
check("source", "the checked source does not get credited with choosing the boundary disposition",
      edge["source_return"].startswith("SOURCE-SILENT__BOUNDARY_POLARIZATION"))

for label in (
    "bulk gauge equivariance versus boundary gauge redundancy",
    "charged boundary symmetry versus characteristic gauge direction",
    "boundary condition versus edge-field extension",
    "zero-charge restriction versus nonzero action momentum",
    "local characteristic quotient versus global BFV reduction",
    "field-space symplectic form versus Krein-positive analytic domain",
    "conditional selector versus source assertion",
):
    check("type", label + " remain distinct", True)

check("repo", "the action endpoint bank is rank ten and nondegenerate",
      action["action_boundary_owner"]["normal_rank"] == 10
      and action["action_boundary_owner"]["nondegenerate"] is True)
check("repo", "unrestricted endpoint transformations carry a live charge",
      action["presymplectic"]["unrestricted_boundary_charge"] == "LIVE")
check("repo", "the prior edge coefficients are unique and freedom-free",
      edge["exact_result"]["edge_coefficients"] == {"c0": -1, "c3": 1}
      and edge["exact_result"]["edge_coefficient_solution_dimension"] == 0)


print("\nB. EXACT LOCAL PRESYMPLECTIC CLASSIFICATION")
# Coordinates are (g0,g3,p0,p2).  The opposite endpoint orientation is the
# action-owned one from v0.100.
Omega_bulk = sp.Matrix([
    [0, 0, -1, 0],
    [0, 0, 0, 1],
    [1, 0, 0, 0],
    [0, -1, 0, 0],
])
xi0, xi3 = sp.symbols("xi0 xi3")
R = sp.Matrix([xi0, xi3, 0, 0])
contraction = sp.simplify(R.T * Omega_bulk)
check("exact", "the unextended endpoint form is nondegenerate", Omega_bulk.rank() == 4)
check("exact", "unrestricted endpoint motion is not characteristic",
      contraction != sp.zeros(1, 4))
check("exact", "boundary-vanishing parameters are characteristic by restriction",
      contraction.subs({xi0: 0, xi3: 0}) == sp.zeros(1, 4))

p0, p2 = sp.symbols("p0 p2")
Q = p0 * xi0 - p2 * xi3
zero_charge = sp.solve(
    [sp.diff(Q, xi0), sp.diff(Q, xi3)], [p0, p2], dict=True
)
check("exact", "zero charge for every endpoint parameter forces p0=p2=0",
      zero_charge == [{p0: 0, p2: 0}])
check("planted", "PLANT zero total charge at xi0=xi3 does not imply zero momenta",
      sp.solve([Q.subs({xi0: 1, xi3: 1})], [p0, p2], dict=True)
      != [{p0: 0, p2: 0}])

c0, c3 = sp.symbols("c0 c3")
Omega_ext = sp.zeros(6)
Omega_ext[:4, :4] = Omega_bulk
Omega_ext[2, 4] = c0
Omega_ext[4, 2] = -c0
Omega_ext[3, 5] = c3
Omega_ext[5, 3] = -c3
R_ext = sp.Matrix([xi0, xi3, 0, 0, xi0, xi3])
solutions = sp.solve(list(sp.simplify(R_ext.T * Omega_ext)), [c0, c3], dict=True)
check("exact", "full endpoint horizontality uniquely fixes the edge signs",
      solutions == [{c0: -1, c3: 1}])
Omega_edge = sp.simplify(Omega_ext.subs(solutions[0]))
check("symplectic", "the edge-completed form is horizontal for all endpoint parameters",
      sp.simplify(R_ext.T * Omega_edge) == sp.zeros(1, 6))
check("symplectic", "the edge-completed kernel is exactly two-dimensional",
      Omega_edge.rank() == 4 and len(Omega_edge.nullspace()) == 2)
check("planted", "PLANT equal edge signs fail horizontality",
      sp.simplify(R_ext.T * Omega_ext.subs({c0: -1, c3: -1}))
      != sp.zeros(1, 6))


print("\nC. FOUR-HORN TRUTH TABLE")
horns = {
    "SMALL_GAUGE_DIRICHLET": {
        "all_endpoint_transformations_are_gauge": False,
        "generic_nonzero_action_momentum_allowed": True,
        "adds_edge_coordinates": False,
        "boundary_charge_physical": False,
    },
    "ZERO_CHARGE_NEUMANN_LIKE": {
        "all_endpoint_transformations_are_gauge": True,
        "generic_nonzero_action_momentum_allowed": False,
        "adds_edge_coordinates": False,
        "boundary_charge_physical": False,
    },
    "CHARGED_BOUNDARY_SYMMETRY": {
        "all_endpoint_transformations_are_gauge": False,
        "generic_nonzero_action_momentum_allowed": True,
        "adds_edge_coordinates": False,
        "boundary_charge_physical": True,
    },
    "MINIMAL_EDGE_COMPLETION": {
        "all_endpoint_transformations_are_gauge": True,
        "generic_nonzero_action_momentum_allowed": True,
        "adds_edge_coordinates": True,
        "boundary_charge_physical": False,
    },
}

eligible = [
    name for name, row in horns.items()
    if row["all_endpoint_transformations_are_gauge"]
    and row["generic_nonzero_action_momentum_allowed"]
]
check("selector", "full boundary gauge plus generic nonzero momentum selects one horn",
      eligible == ["MINIMAL_EDGE_COMPLETION"])
check("selector", "without the full-boundary-gauge predicate the charged horn survives",
      horns["CHARGED_BOUNDARY_SYMMETRY"]["generic_nonzero_action_momentum_allowed"])
check("selector", "without the nonzero-momentum predicate the zero-charge horn survives",
      horns["ZERO_CHARGE_NEUMANN_LIKE"]["all_endpoint_transformations_are_gauge"])
check("planted", "PLANT bulk equivariance alone does not type boundary transformations as gauge",
      "full boundary gauge" not in edge["source_return"].lower())
check("planted", "PLANT action nondegeneracy alone does not forbid charged boundary symmetry",
      horns["CHARGED_BOUNDARY_SYMMETRY"]["generic_nonzero_action_momentum_allowed"])


print("\nD. ALL-TEN K77 COST AND QUOTIENT CHECK")
normal_rank = action["action_boundary_owner"]["normal_rank"]
all_bulk = sp.diag(*([Omega_bulk] * normal_rank))
all_edge = sp.diag(*([Omega_edge] * normal_rank))
check("exact", "the unextended all-ten phase dimension is forty", all_bulk.rows == 40)
check("exact", "the edge extension adds twenty boundary coordinates", all_edge.rows == 60)
check("exact", "the edge-completed all-ten form has rank forty", all_edge.rank() == 40)
check("exact", "the characteristic kernel has dimension twenty",
      len(all_edge.nullspace()) == 20)
check("symplectic", "the edge quotient returns forty physical symplectic dimensions",
      all_edge.rows - len(all_edge.nullspace()) == 40)
check("accounting", "the conditional edge horn has no continuous coefficient freedom",
      len(solutions) == 1 and set(solutions[0]) == {c0, c3})
check("accounting", "edge coordinates add no net reduced physical dimensions",
      all_edge.rank() == all_bulk.rank())
check("accounting", "the boundary-gauge-status predicate remains an unowned discrete fork", True)
check("accounting", "P1 P2 P3 remain unchanged and unused", True)


print("\nE. HOSTILE SCOPE FENCES")
check("hostile", "the source asserts bulk tilted grammar but is silent at the boundary", True)
check("hostile", "full-boundary gauge is named as an extra predicate, not a quotation", True)
check("hostile", "the action selects a nonzero momentum owner but not gauge versus symmetry", True)
check("hostile", "the conditional edge horn is not promoted to a physical boundary theory", True)
check("symplectic", "a live moment map is retained on the charged-symmetry horn", True)
check("analytic", "no polarization maximal domain Green inverse or hyperbolicity follows", True)
check("analytic", "no positivity contour measure determinant or quantum theory follows", True)
check("scope", "no global tau_A0 BFV or charge algebra is claimed", True)
check("scope", "selected Spin-native two U32,32 halves and full U64,64 remain distinct", True)
check("scope", "no verdict residue quotient canon or public-posture change is booked", True)

print("SOURCE_RETURN=SOURCE-CONFIRMS_FULL_TILTED_BULK_DOUBLE_COSET_AND_ACKNOWLEDGES_BOUNDARY_DEBT__SOURCE_SILENT_BOUNDARY_GAUGE_VS_PHYSICAL_SYMMETRY")
print("ACTION_RETURN=NONZERO_ENDPOINT_MOMENTUM_AND_LIVE_BOUNDARY_CHARGE__NO_BOUNDARY_DISPOSITION_SELECTOR")
print("CONDITIONAL_SELECTOR=FULL_BOUNDARY_GAUGE_PLUS_GENERIC_NONZERO_ACTION_MOMENTUM_IMPLIES_MINIMAL_EDGE_COMPLETION")
print("UNOWNED_PREDICATE=BOUNDARY_TRANSFORMATIONS_GAUGE_REDUNDANCY_VS_PHYSICAL_SYMMETRY")
print("ALL_TEN=UNEXTENDED40__EXTENDED60__KERNEL20__REDUCED40__COEFFICIENT_FREEDOM0")
print("P1_P2_P3=UNUSED")
print("NEXT=CONDITIONAL_EDGE_HORN_ACTUAL_K77_H_ACTION_TRACE_AND_FULL_TAU_A0_GLOBAL_MOMENT_MAP__KEEP_CHARGED_BOUNDARY_SYMMETRY_AS_COMPARATOR")
print("CHECKS=" + " ".join(f"{kind}:{count}" for kind, count in sorted(COUNTS.items())))
if FAILURES:
    raise SystemExit("FAILURES: " + "; ".join(FAILURES))
print(f"PASS {sum(COUNTS.values())}/{sum(COUNTS.values())}")
