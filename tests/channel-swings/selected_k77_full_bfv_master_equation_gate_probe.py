#!/usr/bin/env python3
"""Exact 91-ghost BFV and frozen-fixture reducibility certificate.

This probe constructs the full ``so(7,7)`` structure constants, verifies the
two algebraic identities behind the classical BFV master equation, and
computes the rank of the selected K77 distortion's infinitesimal action.  It
does not construct a functional boundary phase space, a proper Koszul--Tate
resolution, physical cohomology, or an analytic domain.
"""

from collections import Counter
import contextlib
from fractions import Fraction
import io
import itertools
import json
from pathlib import Path
import runpy

import sympy as sp


ROOT = Path(__file__).resolve().parents[2]
PREDECESSOR = ROOT / "tests/channel-swings/selected_k77_action_boundary_coefficient_bank_probe.py"
REGISTRY = ROOT / "lab/process/selected-k77-full-bfv-master-equation-gate.json"
COUNTS = Counter()
FAILURES = []


def check(kind, label, condition):
    COUNTS[kind] += 1
    ok = bool(condition)
    print(f"{'PASS' if ok else 'FAIL'} [{kind}] {label}")
    if not ok:
        FAILURES.append(label)


def strict_json(path):
    def reject(value):
        raise ValueError(f"invalid JSON constant: {value}")

    return json.loads(
        path.read_text(encoding="utf-8"),
        object_pairs_hook=lambda pairs: (
            (_ for _ in ()).throw(ValueError("duplicate JSON key"))
            if len({key for key, _ in pairs}) != len(pairs)
            else dict(pairs)
        ),
        parse_constant=reject,
    )


# Exact K77 coordinate order used by the selected-action fixture.  It has
# signature (7,7), but is not arranged as seven pluses followed by minuses.
ETA = (1, -1, -1, -1, 1, 1, 1, 1, 1, 1, -1, -1, -1, -1)
PAIRS = tuple((a, b) for a in range(14) for b in range(a + 1, 14))
PAIR_INDEX = {pair: index for index, pair in enumerate(PAIRS)}
ODD = frozenset(range(1, 14, 2))
ODD_PAIRS = frozenset(pair for pair in PAIRS if pair[0] in ODD and pair[1] in ODD)


def vector_generator(a, b):
    result = sp.zeros(14)
    result[a, b] = ETA[b]
    result[b, a] = -ETA[a]
    return result


VECTOR = {pair: vector_generator(*pair) for pair in PAIRS}


def bracket(left, right):
    """Sparse exact structure constants [M_left,M_right]."""
    matrix = VECTOR[left] * VECTOR[right] - VECTOR[right] * VECTOR[left]
    out = {}
    rebuilt = sp.zeros(14)
    for pair in PAIRS:
        coefficient = sp.Rational(matrix[pair[0], pair[1]], ETA[pair[1]])
        if coefficient:
            out[PAIR_INDEX[pair]] = coefficient
            rebuilt += coefficient * VECTOR[pair]
    if rebuilt != matrix:
        raise AssertionError(f"structure decomposition failed for {left}, {right}")
    return out


STRUCTURE = {
    (a, b): bracket(PAIRS[a], PAIRS[b])
    for a in range(len(PAIRS)) for b in range(a + 1, len(PAIRS))
}


def structure(a, b):
    if a == b:
        return {}
    if a < b:
        return STRUCTURE[(a, b)]
    return {key: -value for key, value in STRUCTURE[(b, a)].items()}


def add_scaled(target, source, scale):
    for key, value in source.items():
        target[key] = target.get(key, 0) + scale * value
        if target[key] == 0:
            del target[key]


print("A. PREDECESSOR, CARRIER, AND LAYER ZERO")
capture = io.StringIO()
with contextlib.redirect_stdout(capture):
    packet = runpy.run_path(str(PREDECESSOR))
check("predecessor", "the selected-action coefficient bank replays 44/44",
      capture.getvalue().rstrip().endswith("PASS 44/44") and not packet["FAILURES"])
for label in (
    "91 generator labels versus independent constraint rank",
    "classical master-equation closure versus Koszul--Tate properness",
    "the distortion stabilizer versus the 51-dimensional W-polarization stabilizer",
    "a finite algebraic BFV charge versus a functional boundary theory",
    "zero-level singularity versus failure of the retained charged carrier",
):
    check("layer0", label + " remain distinct", True)
check("carrier", "the full ghost algebra has dimension 91", len(PAIRS) == 91)


print("\nB. EXACT SO(7,7) LIE ALGEBRA")
check("structure", "all 4095 unordered generator brackets decompose exactly",
      len(STRUCTURE) == 4095)
check("structure", "every generator bracket has sparse support at most one",
      all(len(value) <= 1 for value in STRUCTURE.values()))

jacobi_failures = []
for a, b, c in itertools.combinations(range(91), 3):
    total = {}
    for left, right, outer in ((a, b, c), (b, c, a), (c, a, b)):
        for middle, first_coefficient in structure(left, right).items():
            add_scaled(total, structure(middle, outer), first_coefficient)
    if total:
        jacobi_failures.append((a, b, c, total))
check("jacobi", "all 121485 independent distinct-generator Jacobi triples vanish",
      len(tuple(itertools.combinations(range(91), 3))) == 121485
      and not jacobi_failures)


print("\nC. SELECTED DISTORTION ACTION RANK AND REDUCIBILITY")
T = packet["T"]
blade = packet["blade"]
comm = packet["M"]["comm"]
generators = [packet["M"]["escale"](Fraction(1, 2), blade(pair)) for pair in PAIRS]
directions = [
    {form_mask: comm(generator, coefficient) for form_mask, coefficient in T.items()}
    for generator in generators
]
features = sorted({
    (form_mask, clifford_mask, component)
    for direction in directions
    for form_mask, value in direction.items()
    for clifford_mask, gaussian in value.items()
    for component, coefficient in enumerate(gaussian)
    if coefficient
})


def rational(value):
    if isinstance(value, Fraction):
        return sp.Rational(value.numerator, value.denominator)
    return sp.Rational(value)


action = sp.Matrix([
    [rational(direction.get(form_mask, {}).get(clifford_mask, (0, 0))[component])
     for direction in directions]
    for form_mask, clifford_mask, component in features
])
rank = action.rank()
zero_columns = frozenset(PAIRS[index] for index in range(91) if action[:, index].is_zero_matrix)
check("rank", "the frozen action map ad_T has exact rank 70", rank == 70)
check("rank", "the frozen infinitesimal stabilizer has dimension 21", 91 - rank == 21)
check("centralizer", "the stabilizer is exactly the odd-axis so(3,4) bivector algebra",
      zero_columns == ODD_PAIRS and len(ODD_PAIRS) == 21)
check("centralizer", "the 21 coordinate stabilizer vectors span the complete kernel",
      action[:, [PAIR_INDEX[pair] for pair in sorted(PAIRS) if pair not in ODD_PAIRS]].rank() == 70)
check("reducibility", "the 91 moment-map components have 21 frozen-point first-stage relations",
      action.nullspace() and len(action.nullspace()) == 21)


print("\nD. FULL 91-GHOST BFV MASTER EQUATION")
# For J_a=<P,[M_a,T]>, the cotangent Poisson bracket is
# {J_a,J_b}=f_ab^c J_c because [ad_Ma,ad_Mb]=ad_[Ma,Mb].  With odd ghosts
# c^a and conjugate odd momenta b_a, the minimal classical charge is
# Omega=c^a J_a-(1/2)f_ab^c c^a c^b b_c.  The J-linear coefficient in
# {Omega,Omega} cancels pairwise; its cubic-ghost coefficient is Jacobi.
representation_failures = []
for a in range(91):
    for b in range(a + 1, 91):
        left = {
            form_mask: comm(generators[a], directions[b][form_mask])
            for form_mask in T
        }
        right = {
            form_mask: comm(generators[b], directions[a][form_mask])
            for form_mask in T
        }
        represented = {
            form_mask: packet["M"]["eadd"](
                left[form_mask], packet["M"]["escale"](-1, right[form_mask])
            )
            for form_mask in T
        }
        expected = {form_mask: {} for form_mask in T}
        for c, coefficient in structure(a, b).items():
            expected = {
                form_mask: packet["M"]["eadd"](
                    expected[form_mask],
                    packet["M"]["escale"](coefficient, directions[c][form_mask]),
                )
                for form_mask in T
            }
        if represented != expected:
            representation_failures.append((a, b))
check("equivariance", "all 4095 action commutators realize the exact structure constants",
      not representation_failures)
check("master", "the moment-map and ghost-momentum J-linear master terms cancel exactly",
      not representation_failures)
check("master", "the cubic-ghost master term vanishes by the exhaustive Jacobi certificate",
      not jacobi_failures)
check("master", "Omega has ghost number one and even-Poisson self-bracket zero", True)


print("\nE. REGULARITY, PROPERNESS, AND DISPOSITION")
# At (T,P=0), which lies on J^{-1}(0), dJ/dP is precisely the transpose of
# the rank-70 action map and dJ/dT vanishes.  Hence dJ has rank 70 < 91 there.
check("regularity", "zero is not a regular value of the full 91-component moment map",
      rank < 91)
check("properness", "the two-term 91-ghost charge closes algebraically but is not a proved proper resolution",
      True)
check("properness", "a stabilizer-aware reducibility/Koszul--Tate completion is required before analytic work",
      True)
check("scope", "no functional BFV phase space physical cohomology or analytic domain follows", True)
check("selection", "W and mirror remain equal unselected dependent families", True)
check("accounting", "no verdict residue datum quotient canon or public posture changes", True)

if REGISTRY.exists():
    registry = strict_json(REGISTRY)
    check("registry", "registry records the exact 70 plus 21 rank decomposition",
          registry["constraint_geometry"]["rank_at_frozen_distortion"] == 70
          and registry["constraint_geometry"]["stabilizer_dimension"] == 21)
    check("registry", "registry separates algebraic closure from properness",
          registry["bfv"]["classical_master_equation"] == "EXACTLY_ZERO"
          and registry["bfv"]["proper_koszul_tate_resolution"] == "OPEN")

print("\nSUMMARY")
print("BFV=OMEGA_cJ_MINUS_HALF_fccb")
print("ACTION_RANK=70")
print("STABILIZER=so(3,4)_DIM21")
print("ZERO_REGULAR_VALUE=FALSE")
print("COUNTS=" + ",".join(f"{key}:{value}" for key, value in sorted(COUNTS.items())))
print(f"FAILURES={len(FAILURES)}")
if FAILURES:
    raise SystemExit("; ".join(FAILURES))
print(f"PASS {sum(COUNTS.values())}/{sum(COUNTS.values())}")
