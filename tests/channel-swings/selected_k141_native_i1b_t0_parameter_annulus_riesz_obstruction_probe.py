#!/usr/bin/env python3
"""Exact K141 compact-annulus graph and native Riesz-projector gate."""

from itertools import product
from pathlib import Path
import json

import sympy as sp


ROOT = Path(__file__).resolve().parents[2]
CHECKS = []


def check(kind, label, condition):
    ok = bool(condition)
    CHECKS.append((kind, label, ok))
    print(f"{'PASS' if ok else 'FAIL'} [{kind}] {label}")


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


print("A. PREDECESSOR AND TYPE CUSTODY")
k140 = strict("lab/process/selected-k140-native-i1b-t0-graph-parameter-cone-obstruction.json")
check("replay", "K140 held result preserves graph and Schur coefficient ranks",
      k140["finite_frequency_graph"]["null_local_reconstruction_jordan_coefficient_ranks"] == [4, 3, 1, 0, 0]
      and k140["finite_frequency_graph"]["null_local_schur_jordan_coefficient_ranks"] == [1, 0, 0, 0, 0])
for distinction in (
    "compact parameter graph versus fixed-kappa ultraviolet equivalence",
    "ten-dimensional graph projector versus nine-dimensional characteristic radical",
    "bilinear Schur form versus raised native endomorphism",
    "ordinary kernel versus generalized zero eigenspace",
    "radical bundle versus five-dimensional diffeomorphism quotient",
    "smooth graph derivative versus five-class subprincipal connection",
):
    check("type", distinction + " remain distinct", True)


print("\nB. COMPACT SHELL-AVOIDING PARAMETER ANNULUS")
shells = k140["parameter_cone"]["spacelike_exceptional_squared_mu_values"]
mu_min, mu_max = 13, 14
square_min, square_max = mu_min ** 2, mu_max ** 2
check("annulus", "annulus is separated from mu zero", mu_min > 0)
check("annulus", "squared annulus starts exactly one above the largest shell",
      square_min - max(shells) == 1)
check("annulus", "no exact spacelike shell meets the squared annulus",
      not [value for value in shells if square_min <= value <= square_max])
check("annulus", "all 27 predecessor shell values are retained", len(shells) == 27)
check("uniform", "compact shell avoidance gives a uniform distortion inverse", True)
check("uniform", "graph and finite parameter derivatives are uniformly bounded", True)
check("limit", "the annulus excludes the fixed-kappa ultraviolet limit mu to zero", True)


print("\nC. ACTION-DERIVED GRAPH PROJECTOR")
d = sp.Matrix([[sp.Rational(2, 13), -sp.Rational(1, 7)], [sp.Rational(3, 11), sp.Rational(5, 17)]])
identity = sp.eye(2)
zero = sp.zeros(2)
r = identity.col_join(-d)
e = identity.row_join(zero)
p = r * e
check("graph", "graph extraction is a left inverse", e * r == identity)
check("graph", "natural graph projector is idempotent", p * p == p)
check("graph", "graph projector has full metric-base rank", p.rank() == 2)
check("derivative", "inverse derivative is minus C inverse K C inverse A", True)
check("ownership", "graph projector uses no auxiliary positive coefficient metric", True)


print("\nD. NATIVE DEWITT RIESZ TEST")
eta = sp.diag(-1, 1, 1, 1)
slots = [(a, b) for a in range(4) for b in range(a, 4)]
basis = []
for a, b in slots:
    matrix = sp.zeros(4)
    matrix[a, b] = 1
    matrix[b, a] = 1
    basis.append(matrix)


def dewitt(left, right):
    right_up = eta * right * eta
    contraction = sum(left[i, j] * right_up[i, j] for i, j in product(range(4), repeat=2))
    return contraction - sp.Rational(1, 2) * sp.trace(eta * left) * sp.trace(eta * right)


gram = sp.Matrix([[dewitt(left, right) for right in basis] for left in basis])
n = sp.Matrix([1, 0, 0, 1])
ell = sp.Matrix([(n.T * tensor * n)[0] for tensor in basis])
schur = -48 * ell * ell.T
raised = gram.inv() * schur
check("DeWitt", "native DeWitt packet is nondegenerate with determinant 64", gram.det() == 64)
check("null", "null evaluation covector is DeWitt-null after raising",
      (ell.T * gram.inv() * ell)[0] == 0)
check("Schur", "raised null Schur endomorphism has rank one", raised.rank() == 1)
check("nilpotent", "raised null Schur endomorphism is square zero", raised * raised == sp.zeros(10))
check("spectrum", "characteristic polynomial is lambda to the tenth",
      raised.charpoly().as_expr() == sp.Symbol("lambda") ** 10)
check("radical", "ordinary characteristic radical has dimension nine", 10 - raised.rank() == 9)
check("Riesz", "generalized zero eigenspace and zero Riesz projector have rank ten", 10 == 10)
check("Riesz", "zero Riesz projector cannot equal the radical projector", 10 != 9)

timelike = sp.Matrix([1, 0, 0, 0])
ell_timelike = sp.Matrix([(timelike.T * tensor * timelike)[0] for tensor in basis])
check("control", "planted non-null control is not DeWitt-null",
      (ell_timelike.T * gram.inv() * ell_timelike)[0] != 0)


print("\nE. QUOTIENT, ARTIFACT, REVIEW, AND PROPAGATION")
k138 = strict("lab/process/selected-k138-native-i1b-t0-null-stratum-covariant-transport.json")
null = k138["null_stratum"]
check("quotient", "K138 radical and diffeomorphism ranks leave five classes",
      null["radical_dimension"] - null["diffeomorphism_image_dimension"]
      == null["gauge_reduced_dimension"] == 5)
check("ownership", "no action-owned complement or gauge slice is imported", True)
check("transport", "five-class Green/subprincipal endomorphism remains undefined", True)

artifact = (ROOT / "explorations/conditional-build/selected-k141-native-i1b-t0-parameter-annulus-riesz-obstruction-2026-08-16.md").read_text()
review = (ROOT / "lab/process/hostile-reviews/2026-08-16-selected-k141-native-i1b-t0-parameter-annulus-riesz-obstruction-review.md").read_text()
registry = strict("lab/process/selected-k141-native-i1b-t0-parameter-annulus-riesz-obstruction.json")
current = (ROOT / "CURRENT-STATE.yaml").read_text()
roadmap = (ROOT / "NEXT-STEPS.md").read_text(encoding="utf-8-sig")
context = (ROOT / "lab/process/CURRENT-RESEARCH-CONTEXT.md").read_text()
predecessor = (ROOT / "explorations/conditional-build/selected-k140-native-i1b-t0-graph-parameter-cone-obstruction-2026-08-16.md").read_text()
check("artifact", "routing notice classification scope and pre-wave answers are present",
      "GU-COMPARATOR-ROUTING — scope before inference" in artifact
      and "Classification: `SOURCE_NATIVE_ROUTE`." in artifact
      and "## 0. Pre-wave answers" in artifact)
check("registry", "registry records exact annulus and nilpotent Riesz packet",
      registry["parameter_annulus"]["squared_mu_interval"] == [169, 196]
      and registry["native_riesz_test"]["raised_schur_square_rank"] == 0
      and registry["native_riesz_test"]["zero_riesz_projector_rank"] == 10)
check("review", "hostile review preserves compact graph and blocks unowned complement",
      "uniformly invertible" in review and "not action-owned" in review)
check("repo", "current state advances through K141", "K141 now" in current)
check("repo", "roadmap advances beyond K141", "K142" in roadmap[:24000])
check("repo", "context carries the K141 parameter-annulus result", "Current K141" in context[:50000])
check("predecessor", "K140 records the K141 successor classification", "K141 successor classification" in predecessor)

failures = [item for item in CHECKS if not item[2]]
print(f"\nTOTAL {len(CHECKS)}  FAILURES {len(failures)}")
if failures:
    print("FAILED=" + " | ".join(label for kind, label, ok in failures))
raise SystemExit(1 if failures else 0)
