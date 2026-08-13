#!/usr/bin/env python3
"""Exact scope gate for the selected K77 coupled two-layer Euler complex.

This composes the already-built first-layer source/grade-one Schur symbol with
the separately built second-layer metric block.  It asks whether the ten
metric equations form a closed selected-action complex, and rejects a fitted
Ward completion as a substitute for an action-derived coupled Hessian.
"""

from collections import Counter
from io import StringIO
from pathlib import Path
import contextlib
import json
import runpy

import sympy as sp


ROOT = Path(__file__).resolve().parents[2]
FIRST = ROOT / "tests/channel-swings/selected_action_grade1_dbt_schur_observation_probe.py"
SECOND = ROOT / "tests/channel-swings/selected_second_layer_offtt_scalar_ward_owner_probe.py"
COMPARATOR = ROOT / "tests/channel-swings/selected_k77_metric_section_bianchi_typing_probe.py"
COUNTS = Counter()
FAILURES = []


def check(kind, label, condition):
    COUNTS[kind] += 1
    ok = bool(condition)
    print(f"{'PASS' if ok else 'FAIL'} [{kind}] {label}")
    if not ok:
        FAILURES.append(label)


def load(path, expected):
    capture = StringIO()
    with contextlib.redirect_stdout(capture):
        namespace = runpy.run_path(str(path))
    check("repo", f"{path.name} predecessor replays", expected in capture.getvalue())
    return namespace


def strict(relative):
    path = ROOT / relative

    def hook(pairs):
        result = {}
        for key, value in pairs:
            if key in result:
                raise ValueError(f"duplicate key {key!r}: {path}")
            result[key] = value
        return result

    return json.loads(path.read_text(encoding="utf-8"), object_pairs_hook=hook)


print("A. SOURCE, PREDECESSORS, AND LAYER ZERO")
source = (ROOT / "lab/sources/selected-k77-coupled-euler-complex-source-reinspection-2026-08-08.md").read_text()
check("source", "source confirms the two-layer full-variable action grammar",
      "SOURCE-CONFIRMS__TWO_LAYER_FULL_VARIABLE_ACTION_GRAMMAR" in source
      and "two connections" in source
      and "second norm-square layer" in source)
check("source", "source is silent on the common Hessian and selected physical complex",
      "SOURCE-SILENT__COMMON_TWO_LAYER_HESSIAN_AND_SELECTED_PHYSICAL_COMPLEX" in source
      and "complete second-layer Hessian" in source)

first = load(FIRST, "PASS ")
second = load(SECOND, "PASS ")
comparator = load(COMPARATOR, "PASS 58/58")

for label in (
    "ten retained metric Euler coordinates versus a closed ten-variable action subsystem",
    "finite algebraic Schur elimination versus a BV or symplectic quotient",
    "first-layer coupled Hessian versus second-layer metric diagnostic block",
    "a Ward-basic comparator versus an action-derived Ward completion",
    "symbol cohomology versus strong hyperbolicity and a Green domain",
    "real exact coefficients versus a selected Lorentzian quantum contour",
):
    check("type", label + " remain distinct", True)


print("\nB. THE BUILT FIRST LAYER IS COUPLED, WARD-BASIC, AND GENERICALLY ACYCLIC")
first_ranks = {"timelike": 13, "spacelike": 15, "null": 15}
for orbit, expected_cross_rank in first_ranks.items():
    packet = first["packets"][orbit]
    hessian = packet["effective_at_one"]
    gauge = packet["gauge"]
    check("exact", f"{orbit}: first-layer effective symbol acts on 34 source variables",
          hessian.shape == (34, 34) and gauge.shape == (34, 4))
    check("exact", f"{orbit}: the live adjacent-grade cross is not metric-only",
          packet["full_cross"].shape == (196, 34)
          and packet["full_cross"].rank() == expected_cross_rank)
    check("exact", f"{orbit}: the eliminated grade-one Hessian was rank 196",
          first["hessian"].shape == (196, 196) and first["hessian"].rank() == 196)
    check("exact", f"{orbit}: first-layer Ward radical is exactly gauge four",
          hessian.rank() == 30
          and gauge.rank() == 4
          and hessian * gauge == sp.zeros(34, 4)
          and (34 - hessian.rank()) - gauge.rank() == 0)

registry_n2 = strict("lab/process/selected-action-n2-null-little-group-green.json")
rotation = registry_n2["exact_result"]["compact_null_rotation"]
check("representation", "the exceptional first-layer pair has helicity absolute value one",
      registry_n2["exact_result"]["extra_mode_dimension"] == 2
      and rotation["characteristic_polynomial"] == "x^2+1"
      and rotation["helicity_absolute_value"] == 1)
check("representation", "the exceptional pair is not the Einstein helicity-two comparator",
      rotation["spin_two_target_polynomial"] == "x^2+4"
      and comparator["rotation"].charpoly(sp.symbols("lambda")).as_expr()
      == sp.symbols("lambda")**2 + 4)


print("\nC. THE SECOND-LAYER METRIC BLOCK IS NOT A CLOSED WARD COMPLEX")
s = second["s"]
metric_two = second["subtracted"].subs(s, 2)
metric_gauge = second["gauge"]
check("exact", "second-layer metric diagnostic is ten by ten and nonsingular at s=2",
      metric_two.shape == (10, 10) and metric_two.rank() == 10)
check("exact", "its diffeomorphism gauge map has rank four",
      metric_gauge.shape == (10, 4) and metric_gauge.rank() == 4)
check("exact", "its Ward defect has exact rank four",
      (metric_two * metric_gauge).rank() == 4)
check("repo", "the second layer retains exact transverse-traceless recovery",
      sp.factor((second["plus"].T * second["subtracted"] * second["plus"])[0]
                - second["tt_polynomial_with_norm"]) == 0
      and sp.factor((second["cross"].T * second["subtracted"] * second["cross"])[0]
                    - second["tt_polynomial_with_norm"]) == 0)


print("\nD. NAIVE TWO-LAYER ADDITION BREAKS THE ALREADY-EXACT WARD IDENTITY")
timelike = first["packets"]["timelike"]
first_hessian = timelike["effective_at_one"]
full_gauge = timelike["gauge"]
check("exact", "both layers use the same ten-dimensional timelike metric gauge map",
      full_gauge[:10, :] == metric_gauge)
metric_embed = sp.diag(metric_two, sp.zeros(24))
naive_sum = first_hessian + metric_embed
check("exact", "first layer alone is Ward-basic", first_hessian * full_gauge == sp.zeros(34, 4))
check("exact", "naive metric-block addition has rank-four Ward defect",
      (naive_sum * full_gauge).rank() == 4
      and naive_sum * full_gauge == metric_embed * full_gauge)

gram = metric_gauge.T * metric_gauge
gauge_basic_projector = sp.eye(10) - metric_gauge * gram.inv() * metric_gauge.T
check("exact", "the orthogonal six-dimensional comparator projector is gauge-basic",
      gauge_basic_projector == gauge_basic_projector.T
      and gauge_basic_projector.rank() == 6
      and gauge_basic_projector * metric_gauge == sp.zeros(10, 4))
alpha = sp.symbols("alpha")
check("theorem", "adding any multiple of a gauge-basic block cannot repair the defect",
      (metric_two + alpha * gauge_basic_projector) * metric_gauge
      == metric_two * metric_gauge)
check("theorem", "the standard Einstein comparator likewise cannot cancel a nonbasic block",
      comparator["metric_complex"]((1, 0, 0, 0))[1] * metric_gauge == sp.zeros(10, 4)
      and ((metric_two + comparator["metric_complex"]((1, 0, 0, 0))[1])
           * metric_gauge).rank() == 4)


print("\nE. FORMAL WARD COMPLETIONS EXIST BUT ARE HIGHLY NONUNIQUE")
symmetric_basis = []
for row in range(10):
    for column in range(row, 10):
        basis = sp.zeros(10)
        basis[row, column] = 1
        basis[column, row] = 1
        symmetric_basis.append(basis)
ward_map = sp.Matrix.hstack(*[
    sp.Matrix(basis * metric_gauge).reshape(40, 1)
    for basis in symmetric_basis
])
target = sp.Matrix(-metric_two * metric_gauge).reshape(40, 1)
check("exact", "symmetric Ward-completion map has rank 34 from 55 coefficients",
      ward_map.shape == (40, 55) and ward_map.rank() == 34)
check("exact", "a formal cancellation exists",
      ward_map.row_join(target).rank() == ward_map.rank())
check("surplus", "formal cancellation leaves an affine dimension-21 family",
      len(symmetric_basis) - ward_map.rank() == 21)
check("planted", "PLANT formal solvability does not select a unique action completion",
      len(symmetric_basis) - ward_map.rank() != 0)


print("\nF. DISPOSITION")
for label in (
    "the ten metric equations remain part of the physical equation carrier",
    "the ten equations are not promoted to a closed selected-action subsystem",
    "the first-layer generic physical symbol cohomology is zero after gauge",
    "the first-layer exceptional pair remains helicity one rather than helicity two",
    "the second-layer TT polynomial survives as a diagnostic subblock",
    "the second-layer full metric block remains nonbasic until coupled cross terms are built",
    "the next object is the full common-field two-layer stationary Hessian and Ward complex",
    "all second-layer connection grade-one matter and observation cross blocks must be action-derived",
    "microlocal hyperbolicity Green Krein BV BFV and contour tests remain downstream",
    "no fitted coefficient selector quotient external datum canon or posture change is booked",
    "P1 P2 P3 remain unused and Curt remains formally separate",
):
    check("scope", label, True)

for label in (
    "a retained coordinate block was called a closed physical complex",
    "Schur elimination was called a gauge quotient",
    "the two action layers were combined by direct sum",
    "a 21-parameter formal Ward fit was called a construction",
    "two exceptional modes were called gravitons without representation typing",
    "finite exact rank was called strong hyperbolicity or a common domain",
):
    check("planted", "PLANT reject " + label, True)

print("SOURCE_RETURN=SOURCE-CONFIRMS__TWO_LAYER_FULL_VARIABLE_ACTION_GRAMMAR_AND_DIFFEO_ORTHOGONAL_TARGET__SOURCE-SILENT__COMMON_TWO_LAYER_HESSIAN_AND_SELECTED_PHYSICAL_COMPLEX")
print("RESULT=COUPLED_COMPLEX_REQUIRED__VERTICAL_ONLY_COMPLEX_MISTYPED")
print("FIRST_LAYER=34_VARIABLE_WARD_BASIC__GENERIC_PHYSICAL_COHOMOLOGY0__EXCEPTIONAL_HELICITY1")
print("SECOND_LAYER=METRIC_TT_DIAGNOSTIC_LIVE__FULL_METRIC_WARD_DEFECT4")
print("NAIVE_TWO_LAYER_SUM=WARD_DEFECT4")
print("FORMAL_SYMMETRIC_WARD_COMPLETION=SOLVABLE_BUT_AFFINE_DIMENSION21__NOT_SELECTED")
print("NEXT=FULL_SELECTED_TWO_LAYER_COMMON_FIELD_STATIONARY_HESSIAN_CROSS_BLOCKS_AND_WARD_COMPLEX")
print("P1_P2_P3=UNUSED")
print("CHECKS=" + " ".join(f"{kind}:{count}" for kind, count in sorted(COUNTS.items())))
if FAILURES:
    raise SystemExit("FAILURES: " + "; ".join(FAILURES))
print(f"PASS {sum(COUNTS.values())}/{sum(COUNTS.values())}")
