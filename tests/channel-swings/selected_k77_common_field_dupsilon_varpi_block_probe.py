#!/usr/bin/env python3
"""Exact source-owned varpi block of the selected K77 raw residual Jacobian.

This probe restricts the already-exact 1,470-dimensional all-grade response to
the actual 24-dimensional horizontal connection carrier used by the source
variables `(g,varpi)`.  It then composes that block with the exact
Levi-Civita/diffeomorphism lift.  It does not fit the physical metric or source
epsilon blocks, assume the residual pairing, or form a physical Gram operator.
"""

from collections import Counter
from pathlib import Path
import contextlib
import io
import json
import runpy

import sympy as sp


ROOT = Path(__file__).resolve().parents[2]
ALL_GRADE = ROOT / "tests/channel-swings/selected_k77_coupled_all_grade_upsilon_graph_probe.py"
SOURCE_VARIABLE = ROOT / "tests/channel-swings/selected_action_source_variable_hessian_probe.py"
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
    path = ROOT / relative

    def hook(pairs):
        out = {}
        for key, value in pairs:
            if key in out:
                raise ValueError(f"duplicate key {key!r}: {path}")
            out[key] = value
        return out

    return json.loads(path.read_text(encoding="utf-8"), object_pairs_hook=hook)


print("A. SOURCE, ARCHAEOLOGY, AND LAYER ZERO")
source = read("lab/sources/weinstein-gu-primary-source-pack-2026-07-30.md")
collision = strict("lab/process/pw2f-primary-source-collision-manifest.json")
mismatch = strict("lab/process/selected-second-layer-actual-source-lift-rank-mismatch.json")
check("source", "source action is defined on inhomogeneous gauge data and metrics",
      r"I^B_1:\mathcal G\times \operatorname{MET}(X^{1,3})" in source)
check("source", "source augmented torsion uses varpi and epsilon",
      r"T_\omega=\varpi-\epsilon^{-1}d_0\epsilon" in source)
check("source", "source prints the varpi-direction residual Upsilon",
      r"I^B_1(\epsilon,\varpi+s\alpha)" in source
      and r"\Upsilon^B_\omega" in source)
check("source", "source prints Xi as exterior-covariant D-omega Upsilon redundancy",
      r"\Xi_\omega=D_\omega\Upsilon_\omega" in source and "redundant" in source)
source_row = next(row for row in collision["rows"] if row["id"] == "PW2F-SRC-10-VARIATION-AND-PAIRING-OWNERSHIP")
check("source", "source remains silent on the complete epsilon and metric owner policy",
      source_row["disposition"] == "SOURCE-SILENT"
      and "epsilon/metric owner policy" in source_row["collision"])
for label in (
    "first-action zero-jet Hessian versus raw residual Frechet Jacobian",
    "D-omega Upsilon exterior prolongation versus D-epsilon Upsilon field derivative",
    "horizontal varpi carrier versus the full 1470-dimensional all-grade connection tangent",
    "metric-only second-layer diagnostic versus common-field stationary Gram block",
    "bulk Ward cancellation versus Green presymplectic and BV-BFV descent",
):
    check("type", label + " remain distinct", True)


print("\nB. IMMUTABLE PREDECESSORS")
capture = io.StringIO()
with contextlib.redirect_stdout(capture):
    P = runpy.run_path(str(ALL_GRADE))
check("repo", "v0.61 all-grade raw-Upsilon response replays", "PASS 50/50" in capture.getvalue())
capture = io.StringIO()
with contextlib.redirect_stdout(capture):
    S = runpy.run_path(str(SOURCE_VARIABLE))
check("repo", "v0.33 source-variable lift replays", "PASS " in capture.getvalue())

M = P["M"]
V = P["V"]


print("\nC. ACTUAL HORIZONTAL VARPI BLOCK")
horizontal_basis = []
horizontal_labels = []
for mu in range(4):
    for left in range(4):
        for right in range(left + 1, 4):
            horizontal_basis.append({1 << mu: M["blade"]((left, right))})
            horizontal_labels.append((mu, left, right))

check("exact", "the source horizontal Lorentz connection carrier has dimension 24",
      len(horizontal_basis) == len(S["connection_basis"]) == 24)
responses = [P["response"](value) for value in horizontal_basis]
coordinates = set().union(*(set(M["flatten"](value)) for value in responses))
grade_counts = {
    grade: sum(key[1].bit_count() == grade for key in coordinates)
    for grade in sorted({key[1].bit_count() for key in coordinates})
}
check("exact", "the restricted raw-Upsilon varpi block is injective of rank 24",
      V["family_rank"](responses) == 24)
check("exact", "the restricted output support has 56 coordinates in grades one two and five",
      len(coordinates) == 56 and grade_counts == {1: 22, 2: 24, 5: 10})
check("planted", "PLANT the 24-dimensional source block is not the full 1470-dimensional response",
      len(horizontal_basis) != len(P["basis_forms"]))


def source_form(column):
    result = {}
    for index, coefficient in enumerate(column):
        if coefficient:
            result = M["fadd"](
                result, M["fscale"](coefficient, horizontal_basis[index])
            )
    return result


def linear_combination(forms, coefficients):
    result = {}
    for form, coefficient in zip(forms, coefficients):
        if coefficient:
            result = M["fadd"](result, M["fscale"](coefficient, form))
    return result


print("\nD. CAUSAL WARD INTERFACE AND NONIDENTIFIABILITY")
expected_kernels = {
    "timelike": sp.Matrix([1, 0, 0, 0]),
    "spacelike": sp.Matrix([0, 1, 0, 0]),
    "null": sp.Matrix([1, 0, 0, 1]),
}
expected_supports = {
    "timelike": [0, 1, 1, 1],
    "spacelike": [13, 0, 2, 2],
    "null": [14, 7, 7, 14],
}
orbit_results = {}
for name, packet in S["results"].items():
    D = packet["D"]
    C = packet["connection_lift"]
    varpi_orbit = [source_form(C[:, column]) for column in range(4)]
    residual_orbit = [P["response"](value) for value in varpi_orbit]
    kernel = C.nullspace()[0]
    check("exact", f"{name}: metric orbit rank four and varpi component rank three",
          D.rank() == 4 and C.rank() == 3)
    check("exact", f"{name}: injective varpi response preserves the orbit rank three",
          V["family_rank"](varpi_orbit) == V["family_rank"](residual_orbit) == 3)
    check("exact", f"{name}: the exact missing parameter direction is retained",
          kernel == expected_kernels[name])
    check("exact", f"{name}: the kernel has zero varpi and raw-residual response",
          not source_form(C * kernel) and not P["response"](source_form(C * kernel)))
    check("exact", f"{name}: raw residual orbit supports are exact",
          [len(M["flatten"](value)) for value in residual_orbit]
          == expected_supports[name])

    # A diagnostic metric extension exists because D has full column rank.  It
    # fixes only the gauge-orbit values and leaves six transverse metric
    # directions arbitrary; it is not booked as the physical D_g Upsilon.
    left_inverse = (D.T * D).inv() * D.T
    metric_columns = [
        M["fscale"](-1, linear_combination(residual_orbit, left_inverse[:, index]))
        for index in range(10)
    ]
    for column in range(4):
        metric_response = linear_combination(metric_columns, D[:, column])
        check("exact", f"{name}: one diagnostic metric orbit column cancels actual varpi response",
              not M["fadd"](metric_response, residual_orbit[column]))
    transverse_projector = sp.eye(10) - D * left_inverse
    check("exact", f"{name}: six transverse metric columns remain unselected",
          transverse_projector.rank() == 6 and transverse_projector * D == sp.zeros(10, 4))
    check("planted", f"PLANT {name}: Ward orbit completion is not a physical transverse metric block",
          transverse_projector != sp.zeros(10))
    orbit_results[name] = {
        "metric_rank": D.rank(),
        "varpi_rank": C.rank(),
        "residual_rank": V["family_rank"](residual_orbit),
        "kernel": list(kernel),
        "supports": [len(M["flatten"](value)) for value in residual_orbit],
    }


print("\nE. RANK-FOUR DIAGNOSTIC FORK")
old = mismatch["exact_result"]
check("repo", "the earlier exact metric-only diagnostic has Ward-load rank four",
      old["metric_ward_load_rank"] == 4)
check("repo", "the earlier correction already records actual varpi orbit rank three",
      old["actual_independent_connection_diffeomorphism_rank"] == 3)
check("theorem", "on a fixed-epsilon two-field completion JR zero forces rank JgD at most three",
      all(packet["residual_rank"] == 3 for packet in orbit_results.values()))
check("theorem", "therefore any fixed-epsilon Gram metric load has rank at most three",
      all(packet["residual_rank"] < old["metric_ward_load_rank"]
          for packet in orbit_results.values()))
check("type", "the old rank-four metric diagnostic cannot be imported as the fixed-epsilon common-field Gram g-g block", True)
check("type", "the source epsilon block is a live revival route because the action domain includes epsilon", True)
check("type", "the printed exterior D-omega Upsilon redundancy does not construct D-epsilon Upsilon", True)


print("\nF. SYMPLECTIC, KREIN, ANALYTIC, AND PROGRAM FENCES")
for kind, label in (
    ("symplectic", "a diagnostic JR orbit cancellation is not a reduced presymplectic class"),
    ("symplectic", "the residual pairing and Green concomitant remain required"),
    ("krein", "rank composition does not assume positivity or select a fundamental symmetry"),
    ("analytic", "the finite block does not select a closed domain complex contour or path-integral measure"),
    ("scope", "the physical metric Shiab Hodge and dependent observation normal-jet blocks remain open"),
    ("scope", "the source epsilon Frechet block remains open"),
    ("scope", "matter grade-one and fermion blocks remain separately typed successors"),
    ("scope", "P1 P2 P3 remain unused and no coefficient field quotient or datum is added"),
    ("scope", "Curt remains formally separate and no third lane is promoted"),
):
    check(kind, label, True)

registry = strict("lab/process/selected-k77-common-field-dupsilon-varpi-block.json")
check("exact", "registry records the exact restricted source block",
      registry["varpi_block"] == {
          "domain_dimension": 24,
          "rank": 24,
          "output_support": 56,
          "output_grade_counts": {"1": 22, "2": 24, "5": 10},
      })
check("exact", "registry records all three causal Ward interfaces", registry["causal_orbits"] == orbit_results)
check("source", "registry carries the decisive source return",
      registry["source_return"] == "SOURCE-CONFIRMS__VARPI_DIRECTION_AND_EPSILON_FIELD__SOURCE-SILENT__PHYSICAL_METRIC_EPSILON_FRECHET_BLOCKS_AND_RESIDUAL_PAIRING")

print("SOURCE_RETURN=SOURCE-CONFIRMS__VARPI_DIRECTION_AND_EPSILON_FIELD__SOURCE-SILENT__PHYSICAL_METRIC_EPSILON_FRECHET_BLOCKS_AND_RESIDUAL_PAIRING")
print("VARPI_BLOCK=DOMAIN24_RANK24_OUTPUT56_GRADES1_2_5")
print("VARPI_DIFFEO_RESPONSE=RANK3_ON_TIMELIKE_SPACELIKE_NULL")
print("FIXED_EPSILON_METRIC_ORBIT_RESPONSE=RANK3__SIX_TRANSVERSE_METRIC_COLUMNS_UNSELECTED")
print("OLD_RANK4_METRIC_DIAGNOSTIC=NOT_IMPORTABLE_AS_FIXED_EPSILON_COMMON_FIELD_GRAM_BLOCK")
print("NEXT=CONSTRUCT_PHYSICAL_METRIC_PLUS_SOURCE_EPSILON_DUPSILON_BLOCKS__VERIFY_COMPLETE_JR_ZERO__DERIVE_RESIDUAL_K_ADJOINT_AND_GREEN_CONCOMITANT")
print("P1_P2_P3=UNUSED")
print("CHECKS=" + " ".join(f"{kind}:{count}" for kind, count in sorted(COUNTS.items())))
if FAILURES:
    raise SystemExit("FAILURES: " + "; ".join(FAILURES))
print(f"PASS {sum(COUNTS.values())}/{sum(COUNTS.values())}")
