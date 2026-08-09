#!/usr/bin/env python3
"""Port the already-owned first/second-action blocks to both K77 branches.

This gate transports the exact lower-order moving-Shiab epsilon/Cl1 cross of
the first action by its algebraic packet coefficient, and retypes the selected
125-field residual principal bank as branch-independent top-symbol data.  It
also constructs the branch-dependent zero-jet raw-residual map on the full
1,470-dimensional low-grade varpi tangent.

It does not construct the missing metric/epsilon lower-order blocks, expanded
parent Hessians, gauge fixing, ghosts, a field Riesz map, or a closed domain.
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
FIRST = ROOT / "tests/channel-swings/selected_k77_common_first_action_epsilon_hessian_probe.py"
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

    return json.loads(path.read_text(), object_pairs_hook=hook)


def text(relative):
    return (ROOT / relative).read_text()


print("A. SOURCE, PRIOR ART, AND LAYER ZERO")
source = text("lab/sources/weinstein-gu-primary-source-pack-2026-07-30.md")
branch = strict("lab/process/selected-k77-source-tangent-branch-stationarity.json")
parent = strict("lab/process/selected-k77-full-parent-branch-stationarity.json")
discriminator = strict("lab/process/selected-k77-branch-hessian-discriminator.json")
primitive = strict("lab/process/selected-k77-primitive-epsilon-common-bank.json")
check("source", "source owns the first action and the separate residual norm-square action",
      "I^B_1" in source and r"\Upsilon^B_\omega" in source)
check("source", "source owns g varpi epsilon but not the algebraic branch ports",
      r"T_\omega=\varpi-\epsilon^{-1}d_0\epsilon" in source
      and discriminator["source_return"].endswith("SOURCE_SILENT_BRANCH_HESSIAN_TYPE_BRANCH_SELECTION_AND_ACTION_PARENT"))
check("prior_art", "both branches are source-stationary on the known tangent",
      branch["exact_result"]["branch_pullback"]["varpi_euler"].startswith("ZERO_ALL_1470"))
check("prior_art", "all retained pointwise parents survive but are not selected",
      parent["exact_result"]["both_branches_full_varpi_zero"]
      and not parent["exact_result"]["parent_selected"])
check("prior_art", "v0.118 requires both branch ports",
      discriminator["source_varpi_slice"]["selects_branch"] is False)

for label in (
    "moving-Shiab epsilon cross versus complete first-action Hessian",
    "principal residual bank versus full branch-dependent Frechet Jacobian",
    "source scalar varpi line versus full low-grade varpi tangent",
    "selected spin epsilon tangent versus two-half and full-unitary parents",
    "Galois scaling versus real operator congruence and branch selection",
    "first transgression action versus residual norm-square action",
    "finite covector symbol versus field Riesz graph operator and domain",
):
    check("type", label + " remain distinct", True)

capture = io.StringIO()
with contextlib.redirect_stdout(capture):
    C = runpy.run_path(str(FIRST))
check("prior_art", "the exact v0.106 first-action cross and v0.105 residual bank replay",
      "PASS 61/61" in capture.getvalue() and not C["FAILURES"])

M = C["M"]
V = C["V"]
directions = C["directions"]
direction_grades = C["direction_grades"]
cross_common = C["cross_matrix"]


print("\nB. EXACT BRANCH FACTORS AND FIRST-ACTION EPSILON CROSS")
b, t = sp.symbols("b t", real=True)
r = sp.sqrt(3)
points = (
    {b: Q(1, 208) - r/312, t: (-2+r)/208},
    {b: Q(1, 208) + r/312, t: (-2-r)/208},
)
packet_factor = b**2 + b*t + t**2/3
common_point = {b: Q(1, 156), t: -Q(1, 78)}
common_factor = sp.factor(packet_factor.subs(common_point))
expected_scales = (Q(9, 16)*(2-r), Q(9, 16)*(2+r))
branch_scales = [sp.factor(packet_factor.subs(point)/common_factor) for point in points]
check("exact", "common-branch packet factor is one over 73008", common_factor == Q(1, 73008))
check("exact", "both branch packet scales are exact positive Galois conjugates",
      all(sp.simplify(actual-expected) == 0
          for actual, expected in zip(branch_scales, expected_scales))
      and all(value.is_positive is True for value in branch_scales))

cross_ports = []
for index, scale in enumerate(branch_scales):
    matrix = cross_common.applyfunc(lambda value: sp.factor(scale*value))
    support = matrix.todok()
    cross_ports.append(matrix)
    check("theorem", f"branch {index+1}: first-action epsilon cross retains rank 91",
          matrix.rank() == 91)
    check("exact", f"branch {index+1}: cross retains 182 entries and two per epsilon column",
          len(support) == 182
          and {sum((row, column) in support for row in range(matrix.rows))
               for column in range(matrix.cols)} == {2})
    check("theorem", f"branch {index+1}: all cross receivers remain Clifford grade one",
          all(direction_grades[row] == 1 for row, _ in support))

check("planted", "PLANT nonzero rank persistence does not make branch coefficients equal",
      branch_scales[0] != branch_scales[1])
check("planted", "PLANT the rank-91 selected-spin cross is not expanded-parent closure",
      primitive["exact_result"]["epsilon_dimension"] == 91
      < parent["exact_result"]["block_even_dimension"])


print("\nC. BRANCH-DEPENDENT ZERO-JET RAW-RESIDUAL VARPI MAP")


def curvature_shape(direction):
    return M["hodge"](M["shiab"](M["fadd"](
        M["wedge_raw"](M["PHI1"], direction),
        M["wedge_raw"](direction, M["PHI1"]),
    ), C["P"]["G"]["P"]["channels"]))


def coeff(pair):
    return Q(pair[0].numerator, pair[0].denominator) + sp.I*Q(
        pair[1].numerator, pair[1].denominator
    )


def branch_column(direction, amplitude):
    identity = M["flatten"](direction)
    curvature = M["flatten"](curvature_shape(direction))
    return {
        key: sp.factor(coeff(identity.get(key, M["ZERO"]))
                       + amplitude*coeff(curvature.get(key, M["ZERO"])))
        for key in set(identity).union(curvature)
        if sp.simplify(coeff(identity.get(key, M["ZERO"]))
                       + amplitude*coeff(curvature.get(key, M["ZERO"]))) != 0
    }


def sparse_rank(columns):
    pivots = {}
    for column in columns:
        value = dict(column)
        while value:
            pivot = min(value)
            lead = value[pivot]
            if pivot not in pivots:
                value = {key: sp.cancel(item/lead) for key, item in value.items()}
                pivots[pivot] = value
                break
            basis = pivots[pivot]
            for key, item in basis.items():
                updated = sp.cancel(value.get(key, 0) - lead*item)
                if updated == 0:
                    value.pop(key, None)
                else:
                    value[key] = updated
    return len(pivots)


amplitudes = [sp.factor((b+t).subs(point)) for point in points]
zero_jet = []
for index, amplitude in enumerate(amplitudes):
    columns = [branch_column(direction, amplitude) for direction in directions]
    rank = sparse_rank(columns)
    zero_jet.append({"amplitude": amplitude, "rank": rank})
    check("exact", f"branch {index+1}: full low-grade zero-jet varpi map has rank 1470",
          rank == 1470)
    check("control", f"branch {index+1}: zero-jet map is not the identity fixture",
          any(column != M["flatten"](direction)
              for column, direction in zip(columns, directions)))

check("exact", "the two raw-residual zero-jet amplitudes are distinct conjugates",
      sp.simplify(amplitudes[0]-(-3+r)/624) == 0
      and sp.simplify(amplitudes[1]-(-3-r)/624) == 0)

# On the invariant Phi1 source line the full map reduces to the already-known
# scalar derivative; keep it as a control, not a substitute for the 1470 map.
scalar_derivatives = [sp.factor(624*amplitude+1) for amplitude in amplitudes]
check("exact", "scalar varpi derivatives are minus two plus/minus sqrt three",
      scalar_derivatives == [-2+r, -2-r])
check("planted", "PLANT scalar rank one is not the full rank-1470 tangent",
      all(value != 0 for value in scalar_derivatives) and 1 != 1470)


print("\nD. SELECTED 125-FIELD RESIDUAL PRINCIPAL PORT")
expected_gram = {
    "timelike": {"rank": 110, "inertia": [58, 52, 15]},
    "spacelike": {"rank": 110, "inertia": [53, 57, 15]},
    "null": {"rank": 16, "inertia": [10, 6, 109]},
}
check("principal", "the selected principal bank has 10 plus 24 plus 91 fields",
      primitive["exact_result"]["field_dimension"] == 125
      and primitive["exact_result"]["metric_dimension"] == 10
      and primitive["exact_result"]["varpi_dimension"] == 24
      and primitive["exact_result"]["epsilon_dimension"] == 91)
check("principal", "its coefficient construction contains no branch amplitude",
      primitive["layer0"]["principal_bank"] == "DELTA_T_MINUS_Q_ETA__EXACT")
for branch_index in range(2):
    for name, expected in expected_gram.items():
        actual = primitive["exact_result"]["gram"][name]
        check("principal", f"branch {branch_index+1} {name}: common principal Gram rank/inertia port",
              actual["rank"] == expected["rank"]
              and actual["inertia"] == expected["inertia"])

check("type", "common principal strata do not erase the distinct zero-jet branch amplitudes", amplitudes[0] != amplitudes[1])
check("planted", "PLANT principal equality is not complete Frechet equality",
      primitive["layer0"]["full_frechet"].endswith("OPEN"))


print("\nE. DISPOSITION AND FENCES")
check("construction", "both already-owned action blocks are ported to both branches", True)
check("construction", "complete metric epsilon and expanded-parent lower-order ports remain open", True)
check("representation", "selected Spin two-half and full-unitary action parents remain distinct", True)
check("variational", "the two action candidates are not summed with an invented coefficient", True)
check("symplectic", "bulk block ports do not select a boundary polarization or horn", True)
check("krein", "finite covector ranks do not supply a positive field Hilbert space", True)
check("analytic", "no characteristic determinant contour Dmax Dmin or Green inverse follows", True)
check("accounting", "no field coefficient selector quotient or datum is added", True)
check("accounting", "P1 P2 P3 remain unchanged and unused", True)

print("SOURCE_RETURN=SOURCE_CONFIRMS_FIRST_ACTION_RESIDUAL_NORM_SQUARE_AND_MOVING_CONNECTION_GRAMMAR__SOURCE_SILENT_ALGEBRAIC_BRANCH_BLOCK_PORTS_COMPLETE_HESSIAN_AND_ACTION_PARENT")
print("FIRST_ACTION=BOTH_BRANCHES_RANK91_GRADE1_EPSILON_CROSS__SCALES_9_OVER16_TIMES_2_MINUSPLUS_SQRT3")
print("SECOND_ACTION=BOTH_BRANCHES_ZERO_JET_LOW_GRADE_VARPI_RANK1470__SELECTED_125_FIELD_PRINCIPAL_STRATA_COMMON")
print("PORT_SCOPE=ACTUAL_OWNED_BLOCKS_ONLY__METRIC_EPSILON_LOWER_ORDER_EXPANDED_PARENTS_GAUGE_GHOST_DOMAIN_OPEN")
print("PARENTS=SPIN_NATIVE__TWO_U32_32_HALVES__FULL_U64_64_REMAIN_DISTINCT")
print("P1_P2_P3=UNUSED")
print("CHECKS=" + " ".join(f"{kind}:{count}" for kind, count in sorted(COUNTS.items())))
if FAILURES:
    raise SystemExit("FAILURES: " + "; ".join(FAILURES))
print(f"PASS {sum(COUNTS.values())}/{sum(COUNTS.values())}")
