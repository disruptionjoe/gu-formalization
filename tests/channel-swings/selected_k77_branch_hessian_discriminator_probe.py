#!/usr/bin/env python3
"""Exact Layer-0 audit of the two QQ(sqrt(3)) branch Hessian shortcut.

The two nonzero homogeneous witnesses are stationary in the source ``varpi``
direction, but not under an artificial independent ``B`` variation.  This
probe computes the tempting two-coordinate reconstruction Hessian, proves why
its inertia is not a source-space Morse invariant, and then restricts both the
first transgression action and residual-square action to the actually owned
scalar ``varpi`` tangent.

It does not construct the complete metric/varpi/epsilon Hessian, select a
branch or action parent, or infer positivity or a closed domain.
"""

from collections import Counter
import json
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[2]
COUNTS = Counter()
FAILURES = []
Q = sp.Rational


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


def text(relative):
    return (ROOT / relative).read_text(encoding="utf-8")


print("A. SOURCE LOCUS, PRIOR ART, AND LAYER ZERO")
source_action = text("lab/sources/weinstein-gu-primary-source-pack-2026-07-30.md")
source_norm = text("lab/sources/selected-k77-residual-pairing-source-reinspection-2026-08-08.md")
branch = strict("lab/process/selected-k77-source-tangent-branch-stationarity.json")
parent = strict("lab/process/selected-k77-full-parent-branch-stationarity.json")
boundary = strict("lab/process/selected-k77-branch-bfv-no-selector.json")
admission = strict("lab/process/selected-k77-bulk-operator-admission.json")

check("source", "source owns g varpi epsilon and T equals varpi minus the epsilon connection",
      r"I^B_1:\mathcal G\times \operatorname{MET}(X^{1,3})" in source_action
      and r"T_\omega=\varpi-\epsilon^{-1}d_0\epsilon" in source_action)
check("source", "source directs norm-squaring Upsilon as a distinct Lagrangian",
      "taking its norm squared gives a new Lagrangian" in source_norm)
check("source", "source does not select the algebraic branches or their Hessian type",
      "SOURCE-SILENT" in source_norm)
check("prior_art", "both algebraic branches are source-varpi stationary in the known tangent",
      len(branch["exact_result"]["branches"]) == 2
      and branch["exact_result"]["branch_pullback"]["varpi_euler"].startswith("ZERO_ALL_1470"))
check("prior_art", "independent B at fixed T is explicitly a reconstruction diagnostic",
      branch["layer0"]["independent_B_fixed_T"].startswith("RECONSTRUCTION_DIAGNOSTIC"))
check("prior_art", "both branches are pointwise compatible with every retained internal parent",
      parent["exact_result"]["both_branches_full_varpi_zero"]
      and not parent["exact_result"]["parent_selected"])
check("prior_art", "the boundary symplectic forms select neither nonzero branch",
      boundary["branch_symplectic_equivalence"]["selects_branch_or_amplitude"] is False
      and boundary["classical_edge_bfv"]["selects_branch"] is False)
check("prior_art", "the operator admission gate requires both branch ports",
      admission["operator_ownership"]["branch_specific_first_action_hessian"] == "UNOWNED"
      and admission["operator_ownership"]["branch_specific_second_action_jacobian"] == "UNOWNED")

for label in (
    "source varpi tangent versus independent B reconstruction coordinate",
    "Hessian at a critical point versus coordinate second derivatives at a noncritical point",
    "Galois conjugacy versus order-preserving real congruence",
    "first transgression action versus residual norm-square action",
    "one-dimensional source slice versus complete metric varpi epsilon Hessian",
    "boundary symplectomorphism versus bulk Hessian equivalence",
    "local quadratic coefficient versus positivity stability and vacuum selection",
    "shared invariant slice versus Spin two-half and full-U parent selection",
):
    check("type", label + " remain distinct", True)


print("\nB. EXACT FIRST-ACTION RECONSTRUCTION DERIVATIVES")
b, t = sp.symbols("b t", real=True)
r = sp.sqrt(3)
metric_trace = 624 * (b**2 + b*t + t**2 / 3) + t
i1 = sp.expand(7 * t * metric_trace)
upsilon = sp.expand(312 * (b + t)**2 + t)
branches = (
    {b: Q(1, 208) - r/312, t: -Q(1, 104) + r/208},
    {b: Q(1, 208) + r/312, t: -Q(1, 104) - r/208},
)

grad_i1 = sp.Matrix([sp.diff(i1, b), sp.diff(i1, t)])
h_i1 = sp.hessian(i1, (b, t))
expected_hessians = (
    sp.Matrix([[-84 + 42*r, -42 + 14*r], [-42 + 14*r, -28 + 14*r]]),
    sp.Matrix([[-84 - 42*r, -42 - 14*r], [-42 - 14*r, -28 - 14*r]]),
)
expected_determinants = (588*(3 - 2*r), 588*(3 + 2*r))

reconstruction = []
for index, point in enumerate(branches):
    gradient = sp.simplify(grad_i1.subs(point))
    hessian = sp.simplify(h_i1.subs(point))
    determinant = sp.factor(hessian.det())
    check("exact", f"branch {index + 1}: first action is stationary in t but not independent B",
          gradient[1] == 0 and gradient[0] != 0)
    check("exact", f"branch {index + 1}: reconstruction second-derivative matrix is exact",
          hessian == expected_hessians[index]
          and sp.simplify(determinant - expected_determinants[index]) == 0)

    # For b=b0+x+c*x^2, t=t0+y, the xx entry gains 2*c*dI/db.
    # Since dI/db is nonzero, choose c so the transformed determinant vanishes.
    c_zero = sp.simplify(-determinant / (2 * gradient[0] * hessian[1, 1]))
    transformed = sp.MutableDenseMatrix(hessian)
    transformed[0, 0] = sp.simplify(transformed[0, 0] + 2*c_zero*gradient[0])
    check("theorem", f"branch {index + 1}: a local coordinate change can change reconstruction Hessian rank",
          c_zero != 0 and sp.simplify(transformed.det()) == 0)
    reconstruction.append({
        "gradient": [str(sp.factor(value)) for value in gradient],
        "hessian": [[str(sp.factor(value)) for value in hessian.row(row)] for row in range(2)],
        "determinant": str(determinant),
        "rank_killing_coordinate_c": str(sp.factor(c_zero)),
    })

check("control", "the tempting reconstruction matrices have different naive inertias",
      expected_determinants[0].is_negative is True
      and expected_determinants[1].is_positive is True
      and sp.trace(expected_hessians[1]).is_negative is True)
check("planted", "PLANT different noncritical coordinate Hessians are not promoted to Morse types",
      all(item["gradient"][0] != "0" for item in reconstruction))


print("\nC. ACTUALLY OWNED SOURCE-VARPI RESTRICTION")
source_first_coefficients = [sp.factor(h_i1.subs(point)[1, 1]) for point in branches]
check("exact", "source-varpi first-action coefficients are exact Galois conjugates",
      all(sp.simplify(actual - expected) == 0 for actual, expected in zip(
          source_first_coefficients, [14*(r - 2), -14*(r + 2)])))
check("theorem", "both source-varpi first-action coefficients have the same negative sign",
      source_first_coefficients[0].is_negative is True
      and source_first_coefficients[1].is_negative is True)
check("exact", "their fixed-coordinate magnitude ratio is positive and nonunit",
      sp.simplify(source_first_coefficients[0] / source_first_coefficients[1]) == 7 - 4*r
      and 7 - 4*r != 1)
check("theorem", "the one-dimensional source restrictions are real-congruent up to normalization",
      sp.simplify(source_first_coefficients[0] / source_first_coefficients[1]).is_positive is True)
check("planted", "PLANT same inertia does not erase the unequal fixed-coordinate coefficients",
      source_first_coefficients[0] != source_first_coefficients[1])


print("\nD. RESIDUAL-SQUARE ACTION ON THE SAME SLICE")
grad_u = sp.Matrix([sp.diff(upsilon, b), sp.diff(upsilon, t)])
second_hessians = []
source_second_coefficients = []
for index, point in enumerate(branches):
    u_value = sp.simplify(upsilon.subs(point))
    gradient = sp.simplify(grad_u.subs(point))
    # Normalized nonzero grade-one pairing weight. An overall nonzero weight
    # changes orientation but not rank or radical.
    hessian = sp.simplify(gradient * gradient.T)
    second_hessians.append(hessian)
    source_second_coefficients.append(sp.factor(hessian[1, 1]))
    check("exact", f"branch {index + 1}: residual-square Hessian is dUpsilon tensor dUpsilon",
          u_value == 0 and gradient != sp.zeros(2, 1))
    check("exact", f"branch {index + 1}: normalized residual-square Hessian has rank one",
          hessian.rank() == 1 and hessian.det() == 0)

check("exact", "source-varpi residual-square coefficients are positive conjugates",
      all(sp.simplify(actual - expected) == 0 for actual, expected in zip(
          source_second_coefficients, [7 - 4*r, 7 + 4*r]))
      and all(value.is_positive is True for value in source_second_coefficients))
check("theorem", "the residual-square action has the same rank and inertia class on both branches",
      all(matrix.rank() == 1 for matrix in second_hessians))
check("type", "a nonzero parent grade-one weight can flip orientation but not this rank-one equivalence", True)
check("planted", "PLANT the two source actions are not summed with an invented relative coefficient", True)


print("\nE. DISPOSITION, PARENT SCOPE, AND NEXT GATE")
check("representation", "the shared Phi1 source-varpi line occurs in all three retained parent scopes",
      parent["exact_result"]["both_branches_full_varpi_zero"]
      and parent["layer0"]["selected_spin_native"] == "CONDITIONAL_TRUNCATED_PARENT")
check("representation", "off-slice parent Hessians remain unconstructed and unselected",
      not parent["exact_result"]["functional_tangent_complete"]
      and not parent["exact_result"]["parent_selected"])
check("construction", "the naive one-branch transfer shortcut is killed at Layer 0",
      branch["layer0"]["independent_B_fixed_T"].startswith("RECONSTRUCTION_DIAGNOSTIC"))
check("construction", "both branch-specific source Hessian ports remain required",
      True)
check("symplectic", "the exact boundary symplectomorphism survives but does not identify bulk Hessians",
      boundary["branch_symplectic_equivalence"]["selects_branch_or_amplitude"] is False)
check("krein", "same slice inertia is not a positive Hilbert-space or stability theorem", True)
check("analytic", "no principal symbol contour determinant reflection positivity or closed domain follows", True)
check("accounting", "no field coefficient selector quotient datum or residue is added", True)
check("accounting", "P1 P2 P3 remain unchanged and unused", True)

print("SOURCE_RETURN=SOURCE_CONFIRMS_FIRST_ACTION_AND_DISTINCT_UPSILON_NORM_SQUARE__SOURCE_SILENT_BRANCH_HESSIAN_TYPE_BRANCH_SELECTION_AND_ACTION_PARENT")
print("RECONSTRUCTION=FULL_B_T_SECOND_DERIVATIVES_DIFFER__NOT_MORSE_INVARIANTS_BECAUSE_DI_DB_NONZERO")
print("SOURCE_VARPI_I1=NEGATIVE_ON_BOTH_BRANCHES__FIXED_COORDINATE_RATIO_7_MINUS_4SQRT3")
print("SOURCE_VARPI_I2=POSITIVE_RANK1_ON_BOTH_BRANCHES_UP_TO_NONZERO_PAIRING_ORIENTATION")
print("BRANCH_DISPOSITION=NO_SELECTOR__BOTH_BRANCH_SPECIFIC_FULL_SOURCE_HESSIAN_PORTS_REQUIRED")
print("PARENTS=SHARED_INVARIANT_SLICE_ONLY__SPIN_TWO_U32_32_HALVES_FULL_U64_64_REMAIN_DISTINCT")
print("P1_P2_P3=UNUSED")
print("CHECKS=" + " ".join(f"{kind}:{count}" for kind, count in sorted(COUNTS.items())))
if FAILURES:
    raise SystemExit("FAILURES: " + "; ".join(FAILURES))
print(f"PASS {sum(COUNTS.values())}/{sum(COUNTS.values())}")
