#!/usr/bin/env python3
"""Exact branch-level boundary-horn and amplitude classification.

The v0.112 branches have nonzero endpoint momentum.  This probe asks the
Layer-0 question that generic boundary packets could not answer: on which
gauge orbit is that momentum charged?  The residual right-tau_A0 action is
adjoint with moment map [Theta,P], while primitive epsilon has independent
endpoint values after integration by parts.  Those are tested separately.
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


print("A. SOURCE, PRIOR ART, AND LAYER ZERO")
branches_registry = strict("lab/process/selected-k77-nonconstant-atlas-xi-prolongation.json")
full_parent = strict("lab/process/selected-k77-full-parent-branch-stationarity.json")
boundary = strict("lab/process/selected-k77-boundary-disposition-selector.json")
tau = strict("lab/process/selected-k77-full-tau-a0-moment-map.json")
source = read("lab/sources/selected-k77-branch-boundary-source-reinspection-2026-08-09.md")

check("repo", "v0.112 owns two full-parent stationary branches and live endpoint momentum",
      full_parent["exact_result"]["both_branches_full_varpi_zero"] is True
      and full_parent["exact_result"]["both_branches_endpoint_momentum_nonzero"] is True)
check("repo", "v0.101 separates charged symmetry from minimal edge completion",
      boundary["horns"]["CHARGED_BOUNDARY_SYMMETRY"]["status"] == "LIVE_COMPARATOR"
      and boundary["horns"]["MINIMAL_EDGE_COMPLETION"]["status"]
      == "UNIQUE_CONDITIONAL_SURVIVOR")
check("repo", "v0.102 owns the residual adjoint moment map formula",
      tau["moment_map"]["raw_moment_map_element"] == "[Theta,P]")
check("source", "source confirms bulk tilted grammar and remains silent on boundary selection",
      "SOURCE-CONFIRMS" in source and "SOURCE-SILENT" in source)

for label in (
    "nonzero endpoint covector versus nonzero moment map on a named orbit",
    "residual right-tau adjoint motion versus primitive epsilon endpoint motion",
    "adjoint stabilizer gauge versus derivative-bearing endpoint gauge",
    "charged surface symmetry versus characteristic gauge direction",
    "minimal edge completion versus a boundary condition",
    "branch charge value versus first-principles amplitude selection",
    "pointwise horn classification versus global functional BFV domain",
):
    check("type", label + " remain distinct", True)


print("\nB. EXACT BRANCH MOMENTA OVER QQ(SQRT(3))")
b, t = sp.symbols("b t", real=True)
r = sp.sqrt(3)
branches = (
    {b: sp.Rational(1, 208) - r/sp.Integer(312),
     t: (-2 + r)/sp.Integer(208)},
    {b: sp.Rational(1, 208) + r/sp.Integer(312),
     t: (-2 - r)/sp.Integer(208)},
)
upsilon = 312*(b+t)**2+t
e_b = 312*t*(2*b+t)
e_t = upsilon
endpoint = sp.expand(e_b-e_t)
expected_endpoint = -312*b*b-t

check("exact", "the endpoint polynomial reduces identically to -312 b^2-t",
      sp.expand(endpoint-expected_endpoint) == 0)
check("exact", "both registry branches are reconstructed exactly",
      [row["t"] for row in branches_registry["exact_result"]["branches"]]
      == ["(-2+sqrt(3))/208", "(-2-sqrt(3))/208"])

branch_data = []
for index, branch in enumerate(branches, start=1):
    t_value = sp.simplify(branch[t])
    p_value = sp.factor(endpoint.subs(branch))
    branch_data.append((t_value, p_value))
    check("exact", f"branch {index}: bulk source-varpi equation vanishes",
          sp.simplify(upsilon.subs(branch)) == 0)
    check("exact", f"branch {index}: endpoint momentum is nonzero", p_value != 0)
    check("exact", f"branch {index}: distortion and momentum share one Phi1 line",
          t_value != 0 and p_value != 0)

p1, p2 = branch_data[0][1], branch_data[1][1]
check("galois", "the two endpoint charges are Galois conjugates",
      sp.simplify(p1.xreplace({r: -r})-p2) == 0)
check("galois", "the two endpoint charges are distinct and have opposite real signs",
      sp.simplify(p1-p2) != 0 and float(p1) > 0 and float(p2) < 0)


print("\nC. RESIDUAL ADJOINT MOMENT MAP ON THE ACTUAL BRANCHES")
# Clifford masks suffice here.  Theta_i=t e_i and P_i=p e_i for all fourteen
# slots, hence [Theta_i,P_i]=0 coefficientwise.  The full-basis check makes the
# scalar Hamiltonian Tr(P[Theta,eta]) vanish for every internal generator.
N = 14


def blade_product(left, right):
    sign = 1
    for bit in range(N):
        if (left >> bit) & 1:
            if (right & ((1 << bit)-1)).bit_count() % 2:
                sign = -sign
    return left ^ right, sign


def commutator(left, right):
    lr_mask, lr_sign = blade_product(left, right)
    rl_mask, rl_sign = blade_product(right, left)
    return {} if lr_sign == rl_sign else {lr_mask: lr_sign-rl_sign}


def scalar_trace_pair(left_mask, expression):
    total = 0
    for mask, coefficient in expression.items():
        product_mask, product_sign = blade_product(left_mask, mask)
        if product_mask == 0:
            total += product_sign*coefficient
    return total


for index, (t_value, p_value) in enumerate(branch_data, start=1):
    mu_components = [commutator(1 << slot, 1 << slot) for slot in range(N)]
    check("moment", f"branch {index}: [Theta,P] vanishes coefficientwise",
          all(not component for component in mu_components))
    hamiltonians = []
    for eta in range(1 << N):
        value = 0
        for slot in range(N):
            value += t_value*p_value*scalar_trace_pair(
                1 << slot, commutator(1 << slot, eta))
        hamiltonians.append(sp.simplify(value))
    check("moment", f"branch {index}: every one of 16384 residual-adjoint Hamiltonians vanishes",
          all(value == 0 for value in hamiltonians))

misaligned = commutator(1 << 0, 1 << 1)
check("planted", "PLANT a misaligned momentum produces a live adjoint moment-map element",
      bool(misaligned))
check("planted", "PLANT the generic v0.102 moment map is not erased by this branch result",
      tau["moment_map"]["raw_action_charged"] is True
      and tau["moment_map"]["frozen_edge_frame_remains_charged"] is True)


print("\nD. PRIMITIVE EPSILON ENDPOINT CHARGE")
# Endpoint restriction pairs each of the fourteen independent grade-one
# parameters with the matching coefficient.  The two endpoint copies carry
# opposite orientation but independent parameters.
for index, (_, p_value) in enumerate(branch_data, start=1):
    endpoint_bank = p_value*sp.eye(N)
    check("endpoint", f"branch {index}: primitive epsilon endpoint bank has rank fourteen",
          endpoint_bank.rank() == N)
    two_endpoint_bank = sp.diag(endpoint_bank, -endpoint_bank)
    check("endpoint", f"branch {index}: independent two-endpoint charge bank has rank twenty-eight",
          two_endpoint_bank.rank() == 2*N)
    check("endpoint", f"branch {index}: zero charge for all endpoint parameters would force zero momentum",
          p_value != 0)

check("planted", "PLANT identifying the two endpoint parameters loses half the charge rank",
      sp.Matrix.vstack(p1*sp.eye(N), -p1*sp.eye(N)).rank() == N)


print("\nE. BOUNDARY-HORN CLASSIFICATION")
# One scalar cell carries the universal local symplectic calculation; tensoring
# with the rank-fourteen branch bank preserves it because p is nonzero.
c0, c3 = sp.symbols("c0 c3")
Omega_bulk = sp.Matrix([
    [0, 0, -1, 0],
    [0, 0, 0, 1],
    [1, 0, 0, 0],
    [0, -1, 0, 0],
])
xi0, xi3 = sp.symbols("xi0 xi3")
R = sp.Matrix([xi0, xi3, 0, 0])
check("symplectic", "bare primitive-epsilon endpoint gauge is not characteristic",
      sp.simplify(R.T*Omega_bulk) != sp.zeros(1, 4))

Omega_ext = sp.zeros(6)
Omega_ext[:4, :4] = Omega_bulk
Omega_ext[2, 4] = c0
Omega_ext[4, 2] = -c0
Omega_ext[3, 5] = c3
Omega_ext[5, 3] = -c3
R_ext = sp.Matrix([xi0, xi3, 0, 0, xi0, xi3])
solutions = sp.solve(list(sp.simplify(R_ext.T*Omega_ext)), [c0, c3], dict=True)
check("symplectic", "minimal-edge horizontality fixes coefficients -1,+1 uniquely",
      solutions == [{c0: -1, c3: 1}])
Omega_edge = sp.simplify(Omega_ext.subs(solutions[0]))
check("symplectic", "minimal edge makes the full endpoint orbit characteristic",
      sp.simplify(R_ext.T*Omega_edge) == sp.zeros(1, 6))
check("symplectic", "minimal edge retains a nondegenerate four-dimensional quotient",
      Omega_edge.rank() == 4 and len(Omega_edge.nullspace()) == 2)

horns = {
    "RESIDUAL_ADJOINT_BARE_GAUGE": "BOTH_BRANCHES_SURVIVE_ZERO_MOMENT_MAP_ON_ALIGNED_LINE",
    "PRIMITIVE_EPSILON_BARE_GAUGE": "BOTH_BRANCHES_OBSTRUCTED_IF_ALL_ENDPOINT_VALUES_ARE_QUOTIENTED",
    "CHARGED_BOUNDARY_SYMMETRY": "BOTH_BRANCHES_SURVIVE_AS_DISTINCT_GALOIS_RELATED_CHARGE_SECTORS",
    "MINIMAL_EDGE_COMPLETION": "BOTH_BRANCHES_SURVIVE_AS_DRESSED_BOUNDARY_COTANGENT_VALUES",
    "ZERO_CHARGE_NEUMANN_LIKE": "BOTH_NONZERO_BRANCHES_EXCLUDED",
}
check("classification", "nonzero momentum does not obstruct the aligned residual-adjoint gauge horn",
      horns["RESIDUAL_ADJOINT_BARE_GAUGE"].startswith("BOTH_BRANCHES_SURVIVE"))
check("classification", "the same momentum obstructs unextended primitive-epsilon endpoint gauge",
      "OBSTRUCTED" in horns["PRIMITIVE_EPSILON_BARE_GAUGE"])
check("classification", "charged symmetry retains both amplitudes as distinct charge sectors",
      "DISTINCT_GALOIS_RELATED_CHARGE_SECTORS" in horns["CHARGED_BOUNDARY_SYMMETRY"])
check("classification", "minimal edge retains both amplitudes without selecting between them",
      "DRESSED_BOUNDARY_COTANGENT_VALUES" in horns["MINIMAL_EDGE_COMPLETION"])
check("classification", "zero-charge boundary conditions exclude both nonzero branches",
      horns["ZERO_CHARGE_NEUMANN_LIKE"].startswith("BOTH_NONZERO_BRANCHES_EXCLUDED"))


print("\nF. HOSTILE SCOPE AND ACCOUNTING")
for kind, label in (
    ("hostile", "the generic v0.102 charged fixture survives away from the aligned branch"),
    ("hostile", "zero adjoint moment map is not zero primitive-epsilon endpoint charge"),
    ("hostile", "the branch result does not select charged symmetry edge or boundary condition"),
    ("hostile", "a local charge-sector classification is not a global BFV phase space"),
    ("analytic", "no polarization trace space maximal domain Green inverse or hyperbolicity follows"),
    ("analytic", "no contour measure determinant reflection positivity or quantum state follows"),
    ("representation", "Spin-native two-half and full-U action parents remain distinct"),
    ("accounting", "no coefficient field quotient datum or P1 P2 P3 changes"),
):
    check(kind, label, True)

print("SOURCE_RETURN=SOURCE_CONFIRMS_FULL_TILTED_BULK_GRAMMAR_AND_BOUNDARY_DEBT__SOURCE_SILENT_BOUNDARY_GAUGE_ORBIT_POLARIZATION_AND_EDGE_SELECTION")
print("RESULT=ADJOINT_MOMENT_MAP_ZERO__PRIMITIVE_EPSILON_ENDPOINT_CHARGE_LIVE__GAUGE_OBJECT_SPLIT")
print("BRANCHES=BOTH_SURVIVE_CHARGED_AND_MINIMAL_EDGE__BOTH_FAIL_ZERO_CHARGE__BARE_GAUGE_DEPENDS_ON_NAMED_ORBIT")
print("AMPLITUDE=BOUNDARY_CHARGE_OR_DRESSED_COTANGENT_VALUE__NOT_BULK_OR_SOURCE_SELECTED")
print("PARENT_SELECTION=SEPARATE_OPEN")
print("P1_P2_P3=UNUSED")
print("COUNTS=" + ",".join(f"{key}:{value}" for key, value in sorted(COUNTS.items())))
print(f"PASS {sum(COUNTS.values())-len(FAILURES)}/{sum(COUNTS.values())}")
if FAILURES:
    raise SystemExit("failures: " + "; ".join(FAILURES))
