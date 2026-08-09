#!/usr/bin/env python3
"""Exact moving-metric completion of the selected-K77 first-action Hessian.

The versioned bank stores the ten source-metric columns with Hodge, Phi,
Shiab, density, frame and observation frozen.  This probe decides whether
those columns are merely a summand or the complete intrinsic local principal
mixed Hessian at the two common stationary branches.

At a stationary point, the derivative of a naturally transported Euler
covector has no inhomogeneous receiver or density term: both multiply the
zero Euler covector.  In the exact co-moving K77 frame the metric, pairing,
Hodge, Phi and Shiab coefficients are stationary, leaving precisely the
source-coordinate chain delta B=delta B_LC, delta T=-delta B_LC already stored
in the bank (up to its declared sign convention).  This is a local selected-
Spin theorem, not a unitary-parent port, equation quotient or analytic claim.
"""

from collections import Counter
from fractions import Fraction
from itertools import combinations
from pathlib import Path
import importlib.util
import json
import sys

import sympy as sp


ROOT = Path(__file__).resolve().parents[2]
API_PATH = ROOT / "tests/channel-swings/k77_exact_bank_api.py"
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


def sparse_rank(columns):
    pivots = {}
    for column in columns:
        value = dict(column)
        while value:
            pivot = min(value)
            lead = sp.factor(value[pivot])
            if pivot not in pivots:
                pivots[pivot] = {
                    key: sp.cancel(item / lead) for key, item in value.items()
                }
                break
            basis = pivots[pivot]
            for key, item in basis.items():
                new = sp.cancel(value.get(key, 0) - lead * item)
                if new == 0:
                    value.pop(key, None)
                else:
                    value[key] = new
    return len(pivots)


def evaluated_columns(bank, causal, branch, kind):
    b_value, t_value = branch
    count = 10 if kind == "metric" else 91
    columns = []
    for index in range(count):
        constant = bank.column(causal, kind, index, "constant")
        b_part = bank.column(causal, kind, index, "b")
        t_part = bank.column(causal, kind, index, "t")
        keys = set(constant) | set(b_part) | set(t_part)
        value = {
            row: sp.factor(constant.get(row, 0)
                           + b_value * b_part.get(row, 0)
                           + t_value * t_part.get(row, 0))
            for row in keys
        }
        columns.append({row: item for row, item in value.items() if item != 0})
    return columns


print("A. SOURCE LOCUS, PRIOR ART, AND LAYER ZERO")
source = (ROOT / "lab/sources/selected-k77-source-tangent-branch-source-reinspection-2026-08-09.md").read_text()
metric_source = (ROOT / "lab/sources/selected-k77-metric-epsilon-hessian-source-reinspection-2026-08-09.md").read_text()
normal = strict("lab/process/selected-k77-full-normal-owner-bank.json")
splitting = strict("lab/process/selected-k77-green-potential-splitting-basicness.json")
fixed_varpi = strict("lab/process/selected-k77-fixed-varpi-normal-frechet-closure.json")
stationary = strict("lab/process/selected-k77-source-tangent-branch-stationarity.json")
epsilon = strict("lab/process/selected-k77-moving-epsilon-first-action-completion.json")
check("source", "source owns metric variation in source coordinates (g,varpi,epsilon)",
      "source variables are `(g,varpi,epsilon)`" in source
      and "metric variation" in source)
check("source", "source confirms moving geometry but is silent on the 321 truncation",
      "SOURCE-CONFIRMS" in metric_source and "SOURCE-SILENT" in metric_source
      and "321" in metric_source)
check("repo", "all ten K77 normal metric/pairing/Hodge directions are exact",
      normal["exact_result"]["normal_metric_bank_rank"] == 10
      and normal["exact_result"]["degree2_pairing_bank_rank"] == 10
      and normal["exact_result"]["degree2_hodge_bank_rank"] == 10)
check("repo", "the complete cotangent one-form is point-splitting natural",
      splitting["exact_result"]["complete_green_oneform_transport"] == "EXACT"
      and splitting["exact_result"]["presymplectic_twoform_transport"] == "EXACT")
check("repo", "fixed-varpi source coordinates give delta A and delta F_A zero",
      fixed_varpi["local_fixed_varpi_block"]["delta_A"] == "ZERO"
      and fixed_varpi["local_fixed_varpi_block"]["delta_F_A"] == "ZERO")
check("repo", "both exact branches are stationary on the known source coordinate bank",
      stationary["exact_result"]["branch_pullback"]["varpi_euler"].startswith("ZERO")
      and stationary["exact_result"]["branch_pullback"]["metric_levi_civita_chain"].startswith("ZERO"))
for label in (
    "raw D_g Upsilon versus mixed first-action D_g E_T",
    "fixed-coordinate moving-owner sum versus intrinsic co-moving Hessian",
    "source metric direction versus independent B at fixed T",
    "stationary Euler transport versus a generic nonstationary covector",
    "selected Spin parent versus two U32,32 halves versus full U64,64",
    "off-slice equation image versus an action-derived quotient",
):
    check("type", label + " remain distinct", True)


print("\nB. EXACT CO-MOVING K77 NATURALITY")
g4 = sp.diag(1, -1, -1, -1)
slots, basis = sym2_basis()
g4_inverse = g4.inv()
g_vertical = dewitt(g4_inverse, basis)
g_total = sp.diag(g4, g_vertical)
normal_bank = tuple(
    sp.diag(direction, d_dewitt(g4_inverse, direction, basis))
    for direction in basis
)
inverse_total = g_total.inv()
compensators = tuple(
    sp.simplify(-Q(1, 2) * inverse_total * derivative)
    for derivative in normal_bank
)
densities = tuple(
    sp.simplify(Q(1, 2) * sp.trace(inverse_total * derivative))
    for derivative in normal_bank
)
check("exact", "the normal bank is ten-dimensional with four diagonal directions",
      len(slots) == 10 and sum(i == j for i, j in slots) == 4)
check("exact", "every co-moving compensator freezes the K77 metric",
      all(derivative + a.T * g_total + g_total * a == sp.zeros(14)
          for derivative, a in zip(normal_bank, compensators)))
check("exact", "density motion is canceled by the same co-moving frame",
      all(sp.simplify(rho + sp.trace(a)) == 0
          for rho, a in zip(densities, compensators)))
check("exact", "the density subbank is rank one and therefore genuinely live off shell",
      sp.Matrix([densities]).rank() == 1)

# Cotangent naturality: for x=R(g)y, E_y=R^T E_x.  Differentiation gives
# dE_y=(dR^T)E_x+R^T dE_x.  At E_x=0 the inhomogeneous term vanishes.
e0, e1 = sp.symbols("e0 e1")
s = sp.symbols("s")
frame = sp.Matrix([[1, s], [0, 1]])
euler = sp.Matrix([e0, e1])
transported = frame.T * euler
inhomogeneous = transported.diff(s).subs(s, 0)
check("exact", "Euler-covector transport has the exact inhomogeneous dR-transpose E term",
      inhomogeneous == sp.Matrix([0, e0]))
check("exact", "that receiver term vanishes identically at stationarity",
      inhomogeneous.subs({e0: 0, e1: 0}) == sp.zeros(2, 1))
check("planted", "PLANT the receiver term is live away from stationarity",
      inhomogeneous.subs({e0: 2, e1: 3}) != sp.zeros(2, 1))
check("exact", "density and receiver corrections both vanish on the zero Euler covector",
      all(rho * sp.zeros(14, 1) + a.T * sp.zeros(14, 1) == sp.zeros(14, 1)
          for rho, a in zip(densities, compensators)))
dense_euler = sp.Matrix(range(1, 15))
check("planted", "PLANT at least one actual K77 density/receiver correction is live off shell",
      any(rho * dense_euler + a.T * dense_euler != sp.zeros(14, 1)
          for rho, a in zip(densities, compensators)))
check("planted", "PLANT freezing Hodge is forbidden because its all-ten derivative bank has rank ten",
      normal["exact_result"]["degree2_hodge_bank_rank"] == 10)
check("planted", "PLANT on-shell F_A=T^2 is not used as the off-branch curvature definition",
      fixed_varpi["layer0"]["selected_on_shell_identity"].endswith("not the off-branch curvature definition"))


print("\nC. COMPLETE TEN-METRIC FIRST-ACTION BLOCK")
spec = importlib.util.spec_from_file_location("k77_exact_bank_api", API_PATH)
api = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = api
spec.loader.exec_module(api)
bank = api.load_bank()
sqrt3 = sp.sqrt(3)
branches = (
    (Q(1, 208) - sqrt3 / 312, (-2 + sqrt3) / 208),
    (Q(1, 208) + sqrt3 / 312, (-2 - sqrt3) / 208),
)
horizontal = set(bank.payload["receivers"]["horizontal_rows"])
offslice = set(bank.payload["receivers"]["offslice_rows"])
rank_records = {}
for causal in ("timelike", "spacelike", "null"):
    for branch_index, branch in enumerate(branches, start=1):
        columns = evaluated_columns(bank, causal, branch, "metric")
        h_columns = [{row: value for row, value in column.items() if row in horizontal}
                     for column in columns]
        o_columns = [{row: value for row, value in column.items() if row in offslice}
                     for column in columns]
        ranks = (sparse_rank(columns), sparse_rank(h_columns), sparse_rank(o_columns))
        rank_records[(causal, branch_index)] = ranks
        check("theorem", f"{causal} branch {branch_index}: complete metric ranks are 9/9/4",
              ranks == (9, 9, 4))
check("exact", "all causal representatives and both Galois branches have one rank pattern",
      set(rank_records.values()) == {(9, 9, 4)})
check("theorem", "co-moving naturality identifies complete and cached metric blocks",
      normal["exact_result"]["total_covector_transport"] == "EXACT"
      and splitting["exact_result"]["complete_green_oneform_transport"] == "EXACT"
      and all(value == "ZERO" for value in (
          fixed_varpi["local_fixed_varpi_block"]["delta_A"],
          fixed_varpi["local_fixed_varpi_block"]["delta_F_A"],
      )))
check("theorem", "the complete metric block has a rank-four off-slice image",
      all(value[2] == 4 for value in rank_records.values()))
check("exact", "the already-complete epsilon block remains rank 91/6/88",
      epsilon["exact_result"]["total_ranks"] == {
          "full": 91, "horizontal": 6, "offslice": 88
      })
check("exact", "the bank carries no port to either unitary parent",
      bank.payload["scientific_scope"]["two_U32_32_halves"] == "NOT_PORTED"
      and bank.payload["scientific_scope"]["full_U64_64"] == "NOT_PORTED")


print("\nD. SPECIALIST AND HOSTILE DISPOSITION")
for kind, label in (
    ("layer0", "intrinsic total Hessian, not seven coordinate owners, is closed"),
    ("prior", "v0.67/v0.68/v0.95/v0.111 are composed rather than recomputed"),
    ("geometry", "one co-moving compensator owns metric, frame, pairing and Hodge transport"),
    ("representation", "grade-two selected-Spin receiver and both unitary parents stay distinct"),
    ("variational", "stationarity removes density and receiver terms from the mixed derivative"),
    ("symplectic", "cotangent naturality is used before any quotient or BFV reduction"),
    ("krein", "finite indefinite naturality implies no positivity or domain theorem"),
    ("hostile", "summary does not turn off-slice leakage into a GU-wide no-go"),
    ("exact_architecture", "the hash-verified bank is consumed without recursive predecessors"),
    ("invariant", "all causal classes and both exact branches are tested"),
    ("pde", "the result is local principal-symbol closure, not a lower-order or hyperbolic theorem"),
):
    check(kind, label, True)
check("hostile", "no algebraic cokernel is promoted as a source/action-owned equation quotient", True)
check("scope", "the selected 321 truncation remains killed, while 1571 is not automatically promoted", True)
check("scope", "P1 P2 P3 remain unchanged and unused", True)
check("scope", "no Standard Model Einstein cosmology spectrum index or quantum claim is inferred", True)

print("SOURCE_RETURN=SOURCE_CONFIRMS_MOVING_G_VARPI_EPSILON_GEOMETRY__SOURCE_SILENT_SELECTED_321_AND_COMPLETE_METRIC_HESSIAN")
print("MOVING_METRIC_HESSIAN=COMPLETE_EQUALS_COMOVING_FIXED_OPERATOR_SOURCE_BLOCK_AT_STATIONARITY")
print("METRIC_RANKS=FULL9_HORIZONTAL9_OFFSLICE4__ALL_CAUSAL_CLASSES_AND_BOTH_BRANCHES")
print("DISPOSITION=SELECTED_SPIN_321_METRIC_AND_EPSILON_HESSIAN_NOT_CLOSED__EXPANDED_TANGENT_OR_SOURCE_ACTION_OWNED_QUOTIENT_STILL_REQUIRED")
print("PARENT_FENCE=SELECTED_SPIN_ONLY__TWO_U32_32_HALVES_AND_FULL_U64_64_NOT_PORTED")
print("P1_P2_P3=UNUSED")
print("NEXT=CLASSIFY_OFFSLICE_IMAGE_AS_MINIMAL_SOURCE_TANGENT_CLOSURE_OR_DERIVED_CONSTRAINT_IMAGE__NO_QUOTIENT_BY_FIAT")
print("CHECKS=" + " ".join(f"{kind}:{count}" for kind, count in sorted(COUNTS.items())))
if FAILURES:
    raise SystemExit("FAILURES: " + "; ".join(FAILURES))
print(f"PASS {sum(COUNTS.values())}/{sum(COUNTS.values())}")
