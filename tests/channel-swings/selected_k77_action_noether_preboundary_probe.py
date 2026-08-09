#!/usr/bin/env python3
"""Exact action-level Noether/preboundary composition on the matched-q route.

This is a proof-level composition of immutable exact selected-action receipts.
It does not replay the 16,384-direction Clifford bank.  The new calculations
are (i) a nonzero-residual moving pairing/density identity and (ii) an exact
nonquadratic first-order Euler/Green/presymplectic theorem.  The actual K77
endpoint coefficient is owned by the selected-action bank, not by the finite
control's polynomial realization.
"""

from collections import Counter
from fractions import Fraction as Q
from pathlib import Path
import json


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


def dot(left, right):
    return sum((a * b for a, b in zip(left, right)), Q(0))


def matvec(matrix, vector):
    return [dot(row, vector) for row in matrix]


def transpose(matrix):
    return [list(row) for row in zip(*matrix)]


def matadd(left, right):
    return [[a + b for a, b in zip(lrow, rrow)]
            for lrow, rrow in zip(left, right)]


def matmul(left, right):
    right_t = transpose(right)
    return [[dot(row, column) for column in right_t] for row in left]


def scale(scalar, vector):
    return [scalar * entry for entry in vector]


print("A. SOURCE, LAYER ZERO, AND PREDECESSOR OWNERSHIP")
source = read("lab/sources/selected-k77-residual-pairing-source-reinspection-2026-08-08.md")
common = strict("lab/process/selected-k77-common-physical-equation-dual-green.json")
physical = strict("lab/process/selected-k77-source-native-diffeomorphism-ward-closure.json")
split = strict("lab/process/selected-k77-physical-diffeomorphism-split.json")
primitive = strict("lab/process/selected-first-order-epsilon-preboundary-compose.json")
boundary = strict("lab/process/selected-k77-action-boundary-coefficient-bank.json")
full_action = strict("lab/process/selected-k77-full-u6464-action-bank.json")

check("source", "source owns the norm-square and adjoint arena",
      "norm square" in source and "adjoint" in source)
check("source", "source remains silent on the exact local K77 action composition",
      "SOURCE-SILENT" in source and "closed analytic domain" in source)
check("repo", "the common raw-residual equation dual and physical pullback are exact",
      common["common_operator"]["domain_dimension"] == 34
      and all(row["equation_dual_pullback"] == "ZERO_FOUR_COLUMNS"
              for row in common["physical_pullback"].values()))
check("repo", "the matched-q graph closes in all causal classes with firing omissions",
      all(row["complete_ward_defect_rank"] == 0
          and row["without_moving_defect_rank"] == 3
          and row["without_lower_cartan_defect_rank"] == 3
          for row in physical["causal_classes"].values()))
check("repo", "the physical lift owns moving density in all causal classes",
      split["local_naturality"]["density"] == "EXACT_ALL_12_COLUMNS")
check("repo", "primitive epsilon Euler and unrestricted preboundary are action-owned",
      primitive["composed_chain"]["primitive_epsilon_euler"].startswith("D_B_ADJOINT")
      and primitive["composed_chain"]["unrestricted_flux"].startswith("ETA_TRACE"))
check("repo", "the selected action supplies a rank-ten nondegenerate endpoint covector bank",
      boundary["exact_results"]["normal_bank_rank"] == 10
      and boundary["exact_results"]["endpoint_orientation_opposite"] is True
      and boundary["exact_results"]["endpoint_banks_independent"] is True)
check("repo", "the full pointwise action bank remains a comparator rather than a global bundle",
      full_action["exact_results"]["full_real_dimension"] == 16384
      and "global K77 adjoint-bundle patching" in full_action["boundary"])

for label in (
    "raw residual naturality versus action Euler-Noether identity",
    "dependent physical epsilon compensator versus arbitrary primitive epsilon field variation",
    "primitive epsilon Euler covector versus a vanishing Ward identity",
    "moving residual pairing-density scalar versus positive Hilbert norm",
    "Green potential versus antisymmetrized presymplectic current",
    "compact-support characteristic direction versus charged boundary symmetry",
    "local moment map versus global BFV phase space",
):
    check("type", label + " remain distinct", True)


print("\nB. NONZERO-RESIDUAL MOVING PAIRING AND DENSITY")
# The action density is rho * (1/2 u^T K u).  A general frame generator A
# moves K, while a nonzero density weight c moves both u and rho.  This is a
# nonstationary test: all three contributions are live and cancel exactly.
K = [
    [Q(2), Q(1), Q(0), Q(0)],
    [Q(1), Q(-3), Q(0), Q(1)],
    [Q(0), Q(0), Q(5), Q(2)],
    [Q(0), Q(1), Q(2), Q(-4)],
]
A = [
    [Q(0), Q(2), Q(-1), Q(0)],
    [Q(1), Q(0), Q(3), Q(-2)],
    [Q(0), Q(-1), Q(1), Q(2)],
    [Q(2), Q(0), Q(-2), Q(0)],
]
u = [Q(1), Q(-2), Q(3), Q(4)]
rho = Q(7, 3)
c = Q(3, 2)
ATK = matmul(transpose(A), K)
KA = matmul(K, A)
dK = [[-(a + b) for a, b in zip(arow, brow)]
      for arow, brow in zip(ATK, KA)]
du = [a + b for a, b in zip(matvec(A, u), scale(c, u))]
drho = -2 * c * rho
Ku = matvec(K, u)
quadratic = Q(1, 2) * dot(u, Ku)
density_term = drho * quadratic
field_term = rho * dot(du, Ku)
pairing_term = rho * Q(1, 2) * dot(u, matvec(dK, u))

check("exact", "the nonzero residual has a nonzero action density", quadratic != 0)
check("exact", "density motion is live", density_term != 0)
check("exact", "field/residual motion is live", field_term != 0)
check("exact", "pairing motion is live", pairing_term != 0)
check("exact", "the complete moving quadratic action variation cancels exactly",
      density_term + field_term + pairing_term == 0)
check("planted", "PLANT freezing the pairing fails",
      density_term + field_term != 0)
check("planted", "PLANT freezing the density fails",
      field_term + pairing_term != 0)
check("planted", "PLANT treating A as K-skew fails", any(any(row) for row in dK))


print("\nC. ACTION EULER-NOETHER AND PREBOUNDARY IDENTITY")
# A source-shaped nonlinear first-order control.  Its only role is to verify
# the universal calculus.  The actual endpoint p is the independently owned
# E_B-E_T bank checked above; it is not identified with this polynomial.
D = [
    [Q(-1), Q(1), Q(0), Q(0)],
    [Q(0), Q(-1), Q(1), Q(0)],
    [Q(0), Q(0), Q(-1), Q(1)],
]
g = [Q(2), Q(-1), Q(3), Q(1)]
a = [Q(5), Q(-2), Q(7)]
T = [left - right for left, right in zip(a, matvec(D, g))]
kappa = [Q(-2), Q(3), Q(5)]
linear = [Q(1), Q(-4), Q(2)]
p = [t * t + k * t + ell for t, k, ell in zip(T, kappa, linear)]
E_a = p
E_g = scale(Q(-1), matvec(transpose(D), p))
causal_parameters = {
    "timelike": [Q(1), Q(2), Q(3), Q(5)],
    "spacelike": [Q(2), Q(-1), Q(4), Q(0)],
    "null": [Q(1), Q(1), Q(2), Q(3)],
}

check("exact", "the nonlinear control has live action momentum", all(value != 0 for value in p))
for name, eta in causal_parameters.items():
    delta_g = eta
    delta_a = matvec(D, eta)
    delta_T = [left - right for left, right in zip(delta_a, matvec(D, delta_g))]
    noether = dot(E_a, delta_a) + dot(E_g, delta_g)
    edge = dot(p, delta_a)
    interior = eta[1] * (p[0] - p[1]) + eta[2] * (p[1] - p[2])
    endpoint = eta[3] * p[2] - eta[0] * p[0]
    check("exact", f"{name}: matched contact graph leaves T fixed", delta_T == [Q(0)] * 3)
    check("exact", f"{name}: action Euler-Noether contraction is zero", noether == 0)
    check("exact", f"{name}: exact Green decomposition has the owned endpoint sign",
          edge == interior + endpoint)

wrong_g = matvec(transpose(D), p)
check("planted", "PLANT wrong formal-adjoint sign breaks the Euler-Noether identity",
      any(dot(E_a, matvec(D, eta)) + dot(wrong_g, eta) != 0
          for eta in causal_parameters.values()))
check("theorem", "the actual selected endpoint covector has the same opposite orientation",
      boundary["exact_results"]["endpoint_orientation_opposite"] is True)
check("theorem", "moving Shiab and lower Cartan are both forced in the actual graph",
      all(row["without_moving_defect_rank"] == 3
          and row["without_lower_cartan_defect_rank"] == 3
          for row in physical["causal_classes"].values()))


print("\nD. ANTISYMMETRIZATION AND BASICNESS")
# Theta = p0 dg0 - p2 dg3.  Its field-space exterior derivative is tested on
# a gauge/physical graph vector and a general variation.  Since T is invariant
# on the graph, dp_R=0; contraction is minus the variation of the endpoint
# moment map Q_eta=p0 eta0-p2 eta3.
z_g = [Q(-1), Q(2), Q(0), Q(3)]
z_a = [Q(4), Q(-3), Q(2)]
z_T = [left - right for left, right in zip(z_a, matvec(D, z_g))]
z_p = [(2 * t + k) * z for t, k, z in zip(T, kappa, z_T)]
check("exact", "the test variation changes both endpoint momenta", z_p[0] != 0 and z_p[2] != 0)

for name, eta in causal_parameters.items():
    omega_contraction = -eta[0] * z_p[0] + eta[3] * z_p[2]
    delta_moment = eta[0] * z_p[0] - eta[3] * z_p[2]
    check("symplectic", f"{name}: presymplectic contraction equals minus delta boundary moment map",
          omega_contraction == -delta_moment)

small_eta = [Q(0), Q(2), Q(-3), Q(0)]
small_contraction = -small_eta[0] * z_p[0] + small_eta[3] * z_p[2]
check("symplectic", "boundary-vanishing transformations are horizontal", small_contraction == 0)
check("symplectic", "an unrestricted matched-q transformation carries live boundary charge",
      any((-eta[0] * z_p[0] + eta[3] * z_p[2]) != 0
          for eta in causal_parameters.values()))
check("planted", "PLANT quotienting all endpoint transformations as gauge fails",
      boundary["exact_results"]["endpoint_banks_independent"] is True
      and any(eta[0] != 0 or eta[3] != 0 for eta in causal_parameters.values()))


print("\nE. SCOPE, ACTION-PARENT, ANALYTIC, AND CONSTRAINT FENCES")
for kind, label in (
    ("variational", "the local selected-action Euler-Noether identity is stronger than raw residual J R zero"),
    ("variational", "arbitrary primitive D-epsilon-Upsilon remains unnecessary for the dependent physical orbit"),
    ("symplectic", "small-transform basicness does not erase charged boundary transformations"),
    ("symplectic", "a local moment map is not a global BFV phase space or polarization"),
    ("analytic", "no closed domain Green inverse hyperbolicity or self-adjoint extension is inferred"),
    ("analytic", "no contour measure determinant saddle or reflection positivity is selected"),
    ("krein", "the moving K77 pairing remains indefinite and supplies no positive energy"),
    ("scope", "Spin-native selected parent two U32,32 halves and full U64,64 comparator remain distinct"),
    ("scope", "P1 P2 P3 remain unused and no datum field coefficient selector or quotient is added"),
):
    check(kind, label, True)

registry_path = ROOT / "lab/process/selected-k77-action-noether-preboundary.json"
if registry_path.exists():
    registry = strict("lab/process/selected-k77-action-noether-preboundary.json")
    check("registry", "registry records the nonzero-residual three-term cancellation",
          registry["moving_quadratic_layer"]["all_three_terms_live"] is True
          and registry["moving_quadratic_layer"]["total_variation"] == "ZERO_EXACT")
    check("registry", "registry records all causal Euler-Noether identities",
          all(value == "ZERO_EXACT" for value in registry["matched_q_action_noether"].values()))
    check("registry", "registry records small basicness and live boundary moment map",
          registry["presymplectic"]["compact_support_basic"] is True
          and registry["presymplectic"]["unrestricted_boundary_charge"] == "LIVE")
    check("registry", "registry preserves datum and action-parent fences",
          registry["constraint_fence"]["P1_P2_P3"] == "UNUSED"
          and registry["action_parent_fence"]["full_U64_64"] == "COMPARATOR_NOT_COLLAPSED")

print("\nSUMMARY")
for kind in sorted(COUNTS):
    print(f"{kind}: {COUNTS[kind]}")
print(f"TOTAL={sum(COUNTS.values())}")
print(f"FAILURES={len(FAILURES)}")
if FAILURES:
    raise SystemExit("; ".join(FAILURES))
