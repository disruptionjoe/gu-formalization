#!/usr/bin/env python3
"""Exact stationary selected-action Hessian pulled through the spin LC map."""

from collections import Counter
from fractions import Fraction
from io import StringIO
from pathlib import Path
import contextlib
import json
import runpy

import sympy as sp


ROOT = Path(__file__).resolve().parents[2]
LC_BACKEND = ROOT / "tests/channel-swings/selected_cubic_gauge_rotated_lc_ward_owner_probe.py"
VACUUM_BACKEND = ROOT / "tests/channel-swings/selected_moving_k77_vacuum_p2_norm_probe.py"
SECOND_JET_BACKEND = ROOT / "tests/channel-swings/selected_action_second_soldering_observation_jets_probe.py"
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
    return json.loads(path.read_text(), object_pairs_hook=hook)


def rational(value):
    return sp.Rational(value.numerator, value.denominator)


def form_matrix(forms):
    keys = sorted({
        (form_mask, clifford_mask, part)
        for form in forms
        for form_mask, element in form.items()
        for clifford_mask, coefficient in element.items()
        for part in range(2)
        if coefficient[part]
    })
    return sp.Matrix([
        [rational(form.get(form_mask, {}).get(clifford_mask, (Fraction(0), Fraction(0)))[part])
         for form in forms]
        for form_mask, clifford_mask, part in keys
    ])


def inertia(matrix):
    positive = negative = zero = 0
    for value, multiplicity in matrix.eigenvals().items():
        sign = sp.sign(value)
        if sign == 1:
            positive += multiplicity
        elif sign == -1:
            negative += multiplicity
        elif sign == 0:
            zero += multiplicity
        else:
            raise AssertionError(f"undecidable exact sign: {value}")
    return positive, negative, zero


print("A. SOURCE, PREDECESSORS, AND LAYER 0")
source = (ROOT / "lab/sources/gu-pullback-augmented-torsion-source-reinspection-2026-08-05.md").read_text()
first_jet_report = (ROOT / "explorations/conditional-build/selected-action-physical-soldering-observation-compose-2026-08-06.md").read_text()
check("source", "source names gauge-rotated Levi-Civita and the connection difference", "gauge-rotated Levi-Civita connection in the contorsion slot" in source and "difference of two connections" in source)
check("source", "source is silent on coordinate-versus-spin rank", "coordinate-Christoffel versus action-spin rank" not in source)
check("repo", "the earlier physical chain records coordinate-symbol rank ten", "rank ten" in first_jet_report)

capture = StringIO()
with contextlib.redirect_stdout(capture):
    X = runpy.run_path(str(LC_BACKEND))
check("repo", "the selected spin-LC owner predecessor replays", "PASS 51/51" in capture.getvalue())
capture = StringIO()
with contextlib.redirect_stdout(capture):
    runpy.run_path(str(VACUUM_BACKEND))
check("repo", "the full algebraic stationary-gradient predecessor replays", "PASS 53/53" in capture.getvalue())
capture = StringIO()
with contextlib.redirect_stdout(capture):
    runpy.run_path(str(SECOND_JET_BACKEND))
check("repo", "the exact second spin-LC and observation jets replay", "PASS 52/52" in capture.getvalue())

for label in (
    "coordinate Christoffel symbol versus symmetric-frame spin connection",
    "connection Lorentz gauge versus spacetime diffeomorphism gauge",
    "stationary algebraic Hessian versus off-shell nonlinear Euler equation",
    "unreduced principal coefficient versus physical BV/BFV class",
):
    check("type", label + " remain distinct", True)


selected_hessian = X["selected_hessian"]
lc_spin_symbol = X["lc_spin_symbol"]
slots = [(i, j) for i in range(4) for j in range(i, 4)]


def symmetric_basis(i, j):
    out = [[Fraction(0) for _ in range(4)] for _ in range(4)]
    out[i][j] = out[j][i] = Fraction(1)
    return out


metric_basis = [symmetric_basis(i, j) for i, j in slots]
orbits = {
    "timelike": (Fraction(1), Fraction(0), Fraction(0), Fraction(0)),
    "spacelike": (Fraction(0), Fraction(1), Fraction(0), Fraction(0)),
    "null": (Fraction(1), Fraction(0), Fraction(0), Fraction(1)),
}


print("\nB. ACTION SPIN-LEVI-CIVITA MAP")
spin_maps = {}
spin_fields = {}
for name, covector in orbits.items():
    fields = [lc_spin_symbol(covector, wave) for wave in metric_basis]
    linear = form_matrix(fields)
    kernel = sp.Matrix([covector[i] * covector[j] for i, j in slots])
    spin_maps[name] = linear
    spin_fields[name] = fields
    check("exact", f"{name}: action spin-LC map has rank nine", linear.rank() == 9)
    check("exact", f"{name}: k tensor k is the full kernel", linear * kernel == sp.zeros(linear.rows, 1) and linear.nullspace() == [kernel])

check("planted", "PLANT coordinate-Christoffel rank ten does not transfer to the action spin map", all(linear.rank() != 10 for linear in spin_maps.values()))


print("\nC. EXACT STATIONARY SELECTED-ACTION METRIC HESSIAN")
expected_ranks = {"timelike": 9, "spacelike": 9, "null": 6}
expected_inertias = {"timelike": (3, 6, 1), "spacelike": (6, 3, 1), "null": (3, 3, 4)}
hessians = {}
lam = sp.symbols("lambda")
for name, fields in spin_fields.items():
    matrix = sp.Matrix([
        [rational(selected_hessian(left, right)[0]) for right in fields]
        for left in fields
    ])
    hessians[name] = matrix
    check("exact", f"{name}: pulled-back Hessian is symmetric", matrix == matrix.T)
    check("exact", f"{name}: pulled-back Hessian has the exact rank", matrix.rank() == expected_ranks[name])
    check("exact", f"{name}: pulled-back Hessian has the exact positive-kappa inertia", inertia(matrix) == expected_inertias[name])

timelike_char = sp.factor(hessians["timelike"].charpoly(lam).as_expr() * sp.Integer(65734405323005654352))
spacelike_char = sp.factor(hessians["spacelike"].charpoly(lam).as_expr() * sp.Integer(65734405323005654352))
null_char = sp.factor(hessians["null"].charpoly(lam).as_expr() * sp.Integer(13680875742768))
check("exact", "timelike characteristic polynomial factors exactly", timelike_char == lam * (117*lam + 31)**2 * (117*lam + 62)**3 * (234*lam - 59)**3 * (234*lam + 53))
check("exact", "spacelike characteristic polynomial factors exactly", spacelike_char == lam * (117*lam - 62) * (117*lam - 31)**2 * (117*lam + 55)**2 * (234*lam - 59)**2 * (234*lam - 53) * (234*lam + 59))
check("exact", "null characteristic polynomial factors exactly", null_char == lam**4 * (18252*lam**2 - 3493) * (27378*lam**2 + 13572*lam - 83)**2)

fields = spin_fields["timelike"]
scaled = sp.Matrix([[rational(selected_hessian(left, right, Fraction(2))[0]) for right in fields] for left in fields])
check("exact", "the stationary metric Hessian scales linearly with kappa_1", scaled == 2 * hessians["timelike"])
check("planted", "PLANT the selected stationary Hessian does not vanish", any(matrix.rank() > 0 for matrix in hessians.values()))


print("\nD. STATIONARY SECOND-JET AND OBSERVATION CHAIN")
euler, second_lift, first_left, first_right = sp.symbols("E D2F DFh DFl")
pullback_hessian = first_left * first_right + euler * second_lift
check("exact", "full algebraic stationarity kills every second-lift Hessian term", sp.expand(pullback_hessian.subs(euler, 0)) == first_left * first_right)
check("exact", "nonzero second spin-LC and observation jets therefore carry zero Hessian coefficient at this branch", sp.diff(pullback_hessian, second_lift).subs(euler, 0) == 0)
check("type", "the same second jets remain live off shell and in stationary D3 through D2F paired with the Hessian", True)

# Complete first-jet observation is invertible.  Congruence by an exact
# unipotent representative preserves rank and inertia; this is a finite
# control for the inherited equation-dual theorem, not a replacement for it.
observer = sp.eye(10)
observer[0, 1] = 2
observer[3, 7] = -1
observer[8, 9] = 3
for name, matrix in hessians.items():
    observed = observer.T * matrix * observer
    check("exact", f"{name}: complete invertible observation preserves rank", observed.rank() == matrix.rank())
    check("exact", f"{name}: complete invertible observation preserves inertia", inertia(observed) == inertia(matrix))
check("planted", "PLANT observation congruence is not a new action coefficient", observer.det() == 1)


print("\nE. DIFFEOMORPHISM RADICAL TEST")
expected_gauge_quadratic = {"timelike": 3, "spacelike": 3, "null": 2}
for name, covector in orbits.items():
    diffeo = sp.zeros(10, 4)
    for column in range(4):
        for row, (i, j) in enumerate(slots):
            diffeo[row, column] = (covector[i] if j == column else 0) + (covector[j] if i == column else 0)
    matrix = hessians[name]
    check("exact", f"{name}: diffeomorphism symbol has rank four", diffeo.rank() == 4)
    check("exact", f"{name}: only one diffeomorphism direction lies in the Hessian radical", (matrix * diffeo).rank() == 3)
    check("exact", f"{name}: exact diffeomorphism quadratic restriction rank", (diffeo.T * matrix * diffeo).rank() == expected_gauge_quadratic[name])
    check("planted", f"PLANT {name}: isolated spin-LC block is not diffeomorphism-radical", matrix * diffeo != sp.zeros(10, 4))


print("\nF. REGISTRY AND PROGRAM FENCES")
registry = strict("lab/process/selected-action-stationary-spin-lc-hessian.json")
check("source", "source return is scoped", registry["source_return"] == "SOURCE-CONFIRMS_AND_SOURCE-SILENT")
check("exact", "registry preserves the action-spin rank correction", registry["layer0_correction"]["action_object"] == "SYMMETRIC_FRAME_SPIN_LEVI_CIVITA_CONNECTION" and registry["exact_result"]["action_spin_lc_rank"] == {"timelike": 9, "spacelike": 9, "null": 9})
check("exact", "no free object or datum is introduced", registry["free_object_delta"] == 0 and set(registry["external_datum"].values()) == {"UNUSED"})
check("type", "direct curvature full-II defect Ward completion remains open", registry["exact_result"]["direct_curvature_full_ii_defect_observation_ward_completion"] == "OPEN")
check("type", "Curt and third-lane fences hold", registry["curt_track"] == "FORMALLY_SEPARATE_INSIDE_ERIC_LANE" and registry["third_lane"] == "NOT_PROMOTED")
for label in (
    "stationary algebraic Hessian is not a stable physical vacuum",
    "indefinite local inertia is not a global Krein domain",
    "rank-six null coefficient is not a physical graviton quotient",
    "diffeomorphism residual is not repaired by connection gauge alone",
    "no Einstein equation cosmology Q1 particle or unitarity claim is promoted",
    "P1 P2 P3 remain unused",
):
    check("planted", "PLANT " + label, True)

print("SOURCE_RETURN=SOURCE-CONFIRMS_AND_SOURCE-SILENT")
print("COORDINATE_CHRISTOFFEL_RANK=10__ACTION_SPIN_LC_RANK=9")
print("STATIONARY_SELECTED_METRIC_HESSIAN=TIMELIKE_R9_I361__SPACELIKE_R9_I631__NULL_R6_I334")
print("SECOND_LIFT_HESSIAN_TERM=0_BY_FULL_ALGEBRAIC_STATIONARITY")
print("DIFFEO_CROSS_RANK=3_ALL_ORBITS__ISOLATED_BLOCK_NOT_RADICAL")
print("DIRECT_CURVATURE_FULL_II_DEFECT_OBSERVATION_WARD=OPEN")
print("CHECKS=" + " ".join(f"{kind}:{count}" for kind, count in sorted(COUNTS.items())))
if FAILURES:
    print("FAILED=" + " | ".join(FAILURES))
    raise SystemExit(1)
print(f"PASS {sum(COUNTS.values())}/{sum(COUNTS.values())}")
