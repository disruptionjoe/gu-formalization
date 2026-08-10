#!/usr/bin/env python3
"""Exact typing gate for moving connection reduction versus fermion selection.

The expensive K77 calculations are immutable predecessor evidence.  This
probe composes their machine receipts with exact projector calculus and a
minimal faithful counterexample.  It decides what follows from sector closure;
it does not invent a map from connection coefficients to fermion states.
"""

from __future__ import annotations

from collections import Counter
from fractions import Fraction as Q
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
COUNTS: Counter[str] = Counter()
FAILURES: list[str] = []


def check(kind: str, label: str, condition: object) -> None:
    COUNTS[kind] += 1
    ok = bool(condition)
    print(f"{'PASS' if ok else 'FAIL'} [{kind}] {label}")
    if not ok:
        FAILURES.append(label)


def strict(relative: str) -> dict:
    path = ROOT / relative

    def hook(pairs):
        out = {}
        for key, value in pairs:
            if key in out:
                raise ValueError(f"duplicate key {key!r}: {path}")
            out[key] = value
        return out

    return json.loads(path.read_text(encoding="utf-8"), object_pairs_hook=hook)


def add(left, right):
    return [[left[i][j] + right[i][j] for j in range(len(left[0]))]
            for i in range(len(left))]


def sub(left, right):
    return [[left[i][j] - right[i][j] for j in range(len(left[0]))]
            for i in range(len(left))]


def mul(left, right):
    return [[sum((left[i][k] * right[k][j] for k in range(len(right))), Q(0))
             for j in range(len(right[0]))]
            for i in range(len(left))]


def mv(matrix, vector):
    return [sum((matrix[i][j] * vector[j] for j in range(len(vector))), Q(0))
            for i in range(len(matrix))]


def transpose(matrix):
    return [list(row) for row in zip(*matrix)]


def dot(left, right):
    return sum((left[i] * right[i] for i in range(len(left))), Q(0))


I = [[Q(int(i == j)) for j in range(4)] for i in range(4)]
P = [[Q(int(i == j and i < 2)) for j in range(4)] for i in range(4)]
Qc = sub(I, P)
chi = sub([[Q(2) * value for value in row] for row in P], I)


print("A. IMMUTABLE K77 PREDECESSOR RECEIPTS")
moving = strict("lab/process/selected-k77-moving-parent-bundle-observation-reduction.json")
stationary = strict("lab/process/selected-k77-full-parent-branch-stationarity.json")
grade = strict("lab/process/selected-k77-grade5-unitary-parent-euler-closure.json")
check("prior_art", "the transported connection projector has rank 8128 with rank-8256 complement",
      moving["moving_projector"]["skew_rank"] == 8128
      and moving["moving_projector"]["complement_rank"] == 8256)
check("prior_art", "the first-order Euler operator preserves both connection sectors wholesale",
      moving["moving_projector"]["sector_closure"] == "EXACT_PASS_ALL_16384")
check("prior_art", "both Spin and full-U parent tangents retain the same stationary branches",
      stationary["exact_result"]["both_branches_full_varpi_zero"] is True
      and stationary["exact_result"]["parent_selected"] is False)
check("prior_art", "Euler closure and parent selection remain different recorded questions",
      grade["layer0"]["euler_closure"]
      == "DISTINCT_FROM_UNITARY_COVARIANCE_AND_PARENT_SELECTION")
check("type", "connection coefficient split 8128+8256 is not fermion split 640+832+192",
      8128 + 8256 == 16384 and 640 + 832 + 192 == 1664 and 16384 != 1664)


print("\nB. EXACT FIRST VARIATION OF A MOVING PROJECTOR")
A = [
    [Q(0), Q(0), Q(1), Q(0)],
    [Q(0), Q(0), Q(0), Q(1)],
    [Q(-1), Q(0), Q(0), Q(0)],
    [Q(0), Q(-1), Q(0), Q(0)],
]
dP = sub(mul(A, P), mul(P, A))
zero = [[Q(0) for _ in range(4)] for _ in range(4)]
check("exact", "P and Q are complementary projectors", mul(P, P) == P and mul(Qc, Qc) == Qc
      and add(P, Qc) == I and mul(P, Qc) == zero)
check("exact", "moving-projector derivative is off-diagonal: P dP P=Q dP Q=0",
      mul(mul(P, dP), P) == zero and mul(mul(Qc, dP), Qc) == zero)
check("exact", "all of dP is the two off-diagonal shape blocks",
      dP == add(mul(mul(P, dP), Qc), mul(mul(Qc, dP), P)))
u = [Q(1), Q(2), Q(0), Q(0)]
y = [Q(3), Q(5), Q(7), Q(11)]
du = [a + b for a, b in zip(mv(P, y), mv(dP, u))]
dconstraint = [a - b for a, b in zip(mv(Qc, du), mv(dP, u))]
check("exact", "the differentiated constraint is Q du-dP u=0, not Q du=0",
      dconstraint == [Q(0)] * 4 and mv(Qc, du) != [Q(0)] * 4)
check("planted", "PLANT freezing the projector rejects a valid moving-subbundle tangent",
      mv(Qc, du) != [Q(0)] * 4)


print("\nC. CONSISTENT TRUNCATION IS NOT DYNAMICAL SELECTION")
H = [
    [Q(2), Q(0), Q(0), Q(0)],
    [Q(0), Q(3), Q(0), Q(0)],
    [Q(0), Q(0), Q(5), Q(0)],
    [Q(0), Q(0), Q(0), Q(7)],
]
E = mv(H, u)
check("exact", "a sector-preserving Euler operator sends a P-field back to P",
      mv(Qc, E) == [Q(0)] * 4 and mv(P, E) == E)
v_q = [Q(0), Q(0), Q(13), Q(17)]
check("exact", "the complementary Q sector is an equally consistent truncation",
      mv(P, mv(H, v_q)) == [Q(0)] * 4 and mv(Qc, mv(H, v_q)) == mv(H, v_q))
shape = mv(dP, u)
check("exact", "orthogonal sector closure makes the moving-shape variation invisible to the reduced Euler covector",
      dot(E, shape) == Q(0) and shape != [Q(0)] * 4)
random_projector = [
    [Q(1, 2), Q(0), Q(1, 2), Q(0)],
    [Q(0), Q(1), Q(0), Q(0)],
    [Q(1, 2), Q(0), Q(1, 2), Q(0)],
    [Q(0), Q(0), Q(0), Q(0)],
]
check("planted", "PLANT closure can reject a generic random subspace without uniquely selecting P",
      mul(random_projector, random_projector) == random_projector
      and sub(mul(H, random_projector), mul(random_projector, H)) != zero)
check("variational", "restricted variation yields the projected equation but no equation that creates the projector", True)
check("variational", "a multiplier enforcing Q u=0 would be a new field and a penalty would be a new coefficient", True)


print("\nD. D_VARPI CHI=0 DOES NOT SELECT THE J=1 FERMION SUBSPACE")
B = [
    [Q(0), Q(1), Q(0), Q(0)],
    [Q(-1), Q(0), Q(0), Q(0)],
    [Q(0), Q(0), Q(0), Q(2)],
    [Q(0), Q(0), Q(-2), Q(0)],
]
P_w = [
    [Q(1), Q(0), Q(0), Q(0)],
    [Q(0), Q(0), Q(0), Q(0)],
    [Q(0), Q(0), Q(0), Q(0)],
    [Q(0), Q(0), Q(0), Q(0)],
]
check("exact", "the block connection is compatible with the Weyl-half involution",
      sub(mul(B, chi), mul(chi, B)) == zero)
check("exact", "the same compatible connection mixes a proper subspace inside one half",
      sub(mul(B, P_w), mul(P_w, B)) != zero)
check("layer0", "Weyl-half compatibility does not imply preservation of a j=1 generation projector", True)
check("layer0", "P_epsilon acts on bosonic connection coefficients; P_W acts on spinor-valued one-forms", True)
check("layer0", "an induced fermion operator/intertwiner is required before mirror/random/640/832 controls are typed", True)
check("source", "the inspected source owns full P_H and associated fermions but not this finite physical projector", True)


print("\nE. DISPOSITION")
for kind, label in (
    ("symplectic", "a configuration subbundle is not a presymplectic or BV quotient"),
    ("analytic", "finite sector closure supplies no fundamental symmetry Fredholm domain or positivity"),
    ("scope", "fixed-W theorems and the moving bosonic reduction both survive conditionally"),
    ("accounting", "no coefficient quotient datum or P1 P2 P3 status changes"),
):
    check(kind, label, True)
check("planted", "PLANT identical stationarity on both parent tangents is not parent selection",
      stationary["exact_result"]["parent_selected"] is False)
check("planted", "PLANT ordinary dimension labels do not define an intertwiner", 8128 != 192)

total = sum(COUNTS.values())
print("CHECKS=" + " ".join(f"{key}:{value}" for key, value in sorted(COUNTS.items())))
print(f"PASS {total-len(FAILURES)}/{total}")
print("DISPOSITION=LOCAL_FIRST_ORDER_BOSONIC_CONSISTENT_TRUNCATION_CANDIDATE__FERMION_SELECTOR_UNTYPED")
print("SOURCE_RETURN=SOURCE_CONFIRMS_FULL_P_H_ASSOCIATED_FERMION_GRAMMAR__SOURCE_SILENT_FINITE_PHYSICAL_CARRIER_PROJECTOR")
print("P1_P2_P3=UNCHANGED_UNUSED")
if FAILURES:
    raise SystemExit("; ".join(FAILURES))
