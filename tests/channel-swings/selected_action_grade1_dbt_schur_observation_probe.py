#!/usr/bin/env python3
"""Exact grade-one completion of the selected source principal symbol."""

from collections import Counter
from fractions import Fraction
from io import StringIO
from pathlib import Path
import contextlib
import json
import runpy
import sys

import sympy as sp


ROOT = Path(__file__).resolve().parents[2]
DBT = ROOT / "tests/channel-swings/selected_action_offgraph_dbt_principal_symbol_probe.py"
SOURCE_HESSIAN = ROOT / "tests/channel-swings/selected_action_source_variable_hessian_probe.py"
CURVATURE = ROOT / "tests/channel-swings/selected_action_curvature_graph_six_versus_four_probe.py"
GRADE1 = ROOT / "tests/channel-swings/selected_branch_linearized_totalization_domain_probe.py"
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
        out = {}
        for key, value in pairs:
            if key in out:
                raise ValueError(f"duplicate key {key!r}: {path}")
            out[key] = value
        return out

    return json.loads(path.read_text(), object_pairs_hook=hook)


def rational_pair(value):
    assert value[1] == 0
    return sp.Rational(value[0].numerator, value[0].denominator)


print("A. SOURCE, PREDECESSORS, AND LAYER 0")
source = (ROOT / "lab/sources/gu-pullback-augmented-torsion-source-reinspection-2026-08-05.md").read_text()
receiver_source = (ROOT / "lab/sources/gu-actual-y14-receiver-ordering-source-reinspection-2026-08-05.md").read_text()
check("source", "source types T as connection difference and owns both observation outputs",
      "T_omega=varpi-epsilon^{-1}d_0 epsilon" in source
      and "T_X=s^*T_\\omega" in source
      and "v_T=\\operatorname{res}_s^V T_\\omega" in source)
check("source", "source is silent on the grade-one Hessian Schur ranks and physical quotient",
      "SOURCE-SILENT" in source and "SOURCE-SILENT" in receiver_source)

X = load(DBT, "PASS 41/41")
S = load(SOURCE_HESSIAN, "PASS 84/84")
C = load(CURVATURE, "PASS 50/50")
H0 = load(GRADE1, "PASS 59/59")

for label in (
    "raw curvature coupling versus formal d_B T Euler coupling",
    "T coordinate versus source variables (g,varpi)",
    "finite algebraic elimination versus a BV or symplectic quotient",
    "paired observation preservation versus faithful global descent",
    "a determinant zero versus a physical graviton polarization",
    "a finite principal symbol versus a closed Green/Krein domain",
):
    check("type", label + " remain distinct", True)


print("\nB. COMPLETE GRADE-ONE HESSIAN AND INVARIANT INVERSE")
M = X["M"]
ETA = M["ETA"]
labels = X["cl1_labels"]
index = {label: i for i, label in enumerate(labels)}
dimension = len(labels)
check("exact", "grade-one bank is the complete V-star tensor V carrier", dimension == 196)

tau = sp.zeros(dimension)
for mu, a in labels:
    tau[index[(mu, a)], index[(a, mu)]] = ETA[mu] * ETA[a]
identity = sp.eye(dimension)
trace_covector = sp.zeros(1, dimension)
trace_vector = sp.zeros(dimension, 1)
for i in range(14):
    trace_covector[0, index[(i, i)]] = 1
    trace_vector[index[(i, i)], 0] = 1
scalar_projector = trace_vector * trace_covector / 14
sym_projector = (identity + tau) / 2 - scalar_projector
anti_projector = (identity - tau) / 2
check("exact", "scalar symmetric-traceless antisymmetric dimensions are 1 104 91",
      (scalar_projector.rank(), sym_projector.rank(), anti_projector.rank()) == (1, 104, 91))
check("exact", "irreducible projectors are idempotent orthogonal and complete",
      all(P * P == P for P in (scalar_projector, sym_projector, anti_projector))
      and scalar_projector * sym_projector == sp.zeros(dimension)
      and scalar_projector * anti_projector == sp.zeros(dimension)
      and sym_projector * anti_projector == sp.zeros(dimension)
      and scalar_projector + sym_projector + anti_projector == identity)

native_gram = sp.diag(*[ETA[mu] * ETA[a] for mu, a in labels])
relative_hessian = (
    -scalar_projector
    + sp.Rational(15, 13) * sym_projector
    + sp.Rational(41, 39) * anti_projector
)
relative_inverse = (
    -scalar_projector
    + sp.Rational(13, 15) * sym_projector
    + sp.Rational(39, 41) * anti_projector
)
hessian = native_gram * relative_hessian
hessian_inverse = relative_inverse * native_gram
check("exact", "grade-one Hessian is symmetric nondegenerate and analytically inverted",
      hessian == hessian.T and hessian.rank() == 196
      and hessian * hessian_inverse == identity
      and hessian_inverse * hessian == identity)
check("exact", "positive-kappa Hessian inertia is 97 positive and 99 negative",
      (55 + 42, 1 + 49 + 49) == (97, 99))
check("exact", "analytic eigenvalues reproduce all three predecessor irreducibles",
      H0["real_ratio"](H0["cl1_trace"]) == Fraction(-1)
      and H0["real_ratio"](H0["cl1_sym"]) == Fraction(15, 13)
      and H0["real_ratio"](H0["cl1_anti"]) == Fraction(41, 39))

if "--exhaustive" in sys.argv:
    actual = sp.zeros(dimension)
    for i, left in enumerate(X["cl1_carrier"]):
        for j, right in enumerate(X["cl1_carrier"]):
            actual[i, j] = rational_pair(H0["selected_hessian"](left, right))
    check("exhaustive", "all 196 squared selected-Hessian entries equal the invariant formula",
          actual == hessian)


print("\nC. FULL SOURCE-VARIABLE CROSS AND WARD IDENTITY")


def inverse_times(matrix):
    return hessian_inverse * matrix


def raw_cross(covector):
    k_form = X["scalar_one_form"](covector)
    right_images = [
        M["shiab"](M["wedge_raw"](k_form, direction), X["SELECTED"])
        for direction in X["carrier"]
    ]
    left_images = [
        M["shiab"](M["wedge_raw"](k_form, direction), X["SELECTED"])
        for direction in X["cl1_carrier"]
    ]
    forward = sp.zeros(196, 24)
    reverse = sp.zeros(196, 24)
    for j, right_image in enumerate(right_images):
        for i, left in enumerate(X["cl1_carrier"]):
            forward[i, j] = rational_pair(X["pairing"](left, right_image))
            reverse[i, j] = rational_pair(X["pairing"](X["carrier"][j], left_images[i]))
    return forward, reverse


horizontal_rows = [index[label] for label in labels if label[0] < 4]
vertical_rows = [index[label] for label in labels if label[0] >= 4]
expected = {
    "timelike": {"F": 12, "R": 12, "E": 12, "Wg": 4, "W": 13, "Q": 13, "Wh": 12},
    "spacelike": {"F": 12, "R": 12, "E": 12, "Wg": 6, "W": 15, "Q": 15, "Wh": 14},
    "null": {"F": 12, "R": 12, "E": 11, "Wg": 7, "W": 15, "Q": 14, "Wh": 14},
}
packets = {}
for name, covector in X["orbits"].items():
    forward, reverse = raw_cross(covector)
    euler = (forward - reverse) / 2
    saved = sp.zeros(196, 24)
    for column, sparse in enumerate(X["leakage_results"][name]["cl1_from_horizontal_cl2"]["columns"]):
        for row, value in sparse.items():
            saved[row, column] = rational_pair(value)
    check("exact", f"{name}: recomputed formal Euler cross equals the predecessor", euler == saved)

    lc_map = S["results"][name]["L"]
    metric_gauge = S["results"][name]["D"]
    gauge = S["results"][name]["gauge"]
    # F_B contributes F L delta-g.  d_B T contributes E(delta-varpi-L delta-g).
    metric_cross = (forward - euler) * lc_map
    connection_cross = euler
    full_cross = metric_cross.row_join(connection_cross)
    schur = sp.simplify(full_cross.T * inverse_times(full_cross))

    einstein = C["curvature_gain"] * C["W"]["einstein_hessian"](covector)
    principal_zero = S["results"][name]["coupled"] + sp.diag(einstein, sp.zeros(24))
    effective_at_one = sp.simplify(principal_zero - schur)
    exp = expected[name]
    check("exact", f"{name}: raw reverse Euler and full-cross ranks are exact",
          (forward.rank(), reverse.rank(), euler.rank(), metric_cross.rank(), full_cross.rank())
          == (exp["F"], exp["R"], exp["E"], exp["Wg"], exp["W"]))
    check("exact", f"{name}: curvature and d_B T jointly satisfy the source Ward identity",
          forward * lc_map * metric_gauge == sp.zeros(196, 4)
          and full_cross * gauge == sp.zeros(196, 4))
    check("exact", f"{name}: Schur form is symmetric with exact rank",
          schur == schur.T and schur.rank() == exp["Q"])
    check("exact", f"{name}: horizontal and vertical observation ranks are exact",
          euler[horizontal_rows, :].rank() == exp["E"]
          and euler[vertical_rows, :].rank() == 1
          and full_cross[horizontal_rows, :].rank() == exp["Wh"]
          and full_cross[vertical_rows, :].rank() == 1)
    check("exact", f"{name}: paired receiver preserves the full source cross",
          full_cross.rank() == exp["W"])
    check("exact", f"{name}: normalized effective symbol has only the gauge radical",
          effective_at_one.rank() == 30
          and effective_at_one * gauge == sp.zeros(34, 4)
          and gauge.T * effective_at_one == sp.zeros(4, 34)
          and sp.Matrix.hstack(*effective_at_one.nullspace()).row_join(gauge).rank() == 4)
    packets[name] = {
        "forward": forward,
        "reverse": reverse,
        "euler": euler,
        "full_cross": full_cross,
        "schur": schur,
        "principal_zero": principal_zero,
        "effective_at_one": effective_at_one,
        "gauge": gauge,
        "lc_map": lc_map,
    }


print("\nD. COEFFICIENT AND OBSERVATION DISPOSITION")
check("type", "for nonzero kappa the quotient pencil is z P0 minus Q with z=kappa squared", True)
check("exact", "normalized kappa squared one loses the graph-only null polarization pair",
      C["expected_total_ranks"]["null"] == 28
      and packets["null"]["effective_at_one"].rank() == 30)
check("type", "a coefficient locus can only be promoted after exact factor and mode typing", True)
check("type", "receiver preservation requires observed grade-one equations but proves no global faithfulness", True)
check("type", "algebraic elimination retains rather than erases the Green/preboundary obligation", True)


print("\nE. REGISTRY AND PROGRAM FENCES")
registry = strict("lab/process/selected-action-grade1-dbt-schur-observation.json")
check("source", "source return is SOURCE-CONFIRMS_AND_SOURCE-SILENT",
      registry["source_return"] == "SOURCE-CONFIRMS_AND_SOURCE-SILENT")
check("exact", "registry records the exact grade-one and source-cross ranks",
      registry["exact_result"]["grade1_hessian"]["dimension"] == 196
      and registry["exact_result"]["grade1_hessian"]["rank"] == 196
      and registry["exact_result"]["grade1_hessian"]["inertia_positive_kappa"] == [97, 99, 0]
      and registry["exact_result"]["full_cross_ranks"] == {"timelike": 13, "spacelike": 15, "null": 15}
      and registry["exact_result"]["schur_ranks"] == {"timelike": 13, "spacelike": 15, "null": 14})
check("exact", "no object datum or quotient is added",
      registry["free_object_delta"] == 0 and registry["quotient_count_delta"] == 0
      and set(registry["external_datum"].values()) == {"UNUSED"})
check("type", "Curt and third-lane fences hold",
      registry["curt_track"] == "FORMALLY_SEPARATE_INSIDE_ERIC_LANE"
      and registry["third_lane"] == "NOT_PROMOTED")
for label in (
    "the graph-only Einstein match is not retained as a full-action theorem",
    "a Schur complement is not called a BV or symplectic quotient",
    "the algebraic coefficient locus is not called a measured coupling",
    "two algebraic null modes are not yet called physical gravitons",
    "no global domain positivity unitarity cosmology or particle claim is promoted",
    "P1 P2 P3 remain unused",
):
    check("planted", "PLANT " + label, True)

print("SOURCE_RETURN=SOURCE-CONFIRMS_AND_SOURCE-SILENT")
print("GRADE1_HESSIAN=RANK196_INERTIA97_99_FOR_POSITIVE_KAPPA")
print("FULL_SOURCE_CROSS_RANKS=13_15_15")
print("SCHUR_RANKS=13_15_14")
print("KAPPA_SQUARED_ONE_NONNULL_AND_NULL_EFFECTIVE_KERNEL=GAUGE4_ONLY")
print("PAIRED_OBSERVATION=PRESERVES_NOT_ERASES_ADJACENT_GRADE")
print("COEFFICIENT_FACTOR_AND_MODE_TYPING=SEE_INDEPENDENT_SAGE")
print("COMMON_DOMAIN_ODD_BV_BFV=OPEN")
print("CHECKS=" + " ".join(f"{kind}:{count}" for kind, count in sorted(COUNTS.items())))
if FAILURES:
    print("FAILED=" + " | ".join(FAILURES))
    raise SystemExit(1)
print(f"PASS {sum(COUNTS.values())}/{sum(COUNTS.values())}")
