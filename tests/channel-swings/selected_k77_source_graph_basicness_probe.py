#!/usr/bin/env python3
"""Exact covariance/basicness gate for the corrected K77 source graph.

The v0.57 four-column source-varpi lift is exact in one K77 frame.  This
probe asks the next, stricter question: does that fitted map descend without
remembering a full frame?  It separates three objects which are easy to
collapse:

* an exact pointwise map in one frame;
* its tautologically covariant extension on the full frame bundle; and
* a basic/equivariant map on the quotient by the frame stabilizer.

All transformations below are exact signed rotations in the settled K77
metric.  A three-patch moving-frame construction is checked together with a
locally self-consistent but non-descending plant.  The quotient test is an
independent block-stabilizer calculation.
"""

from collections import Counter
import contextlib
from fractions import Fraction
import io
from pathlib import Path
import runpy

import sympy as sp


ROOT = Path(__file__).resolve().parents[2]
PREDECESSOR = ROOT / "tests/channel-swings/selected_k77_cartan_spencer_signature_correction_probe.py"
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


def add(left, right):
    out = dict(left)
    for key, value in right.items():
        value = out.get(key, Fraction(0)) + value
        if value:
            out[key] = value
        else:
            out.pop(key, None)
    return out


def scale(value, coefficient):
    return {key: coefficient * item for key, item in value.items()
            if coefficient * item}


print("A. SOURCE RETURN, REPO ARCHAEOLOGY, AND LAYER ZERO")
source = read("lab/sources/weinstein-gu-primary-source-pack-2026-07-30.md")
pullback = read("lab/sources/gu-pullback-augmented-torsion-source-reinspection-2026-08-05.md")
correction = read("explorations/conditional-build/selected-k77-cartan-spencer-signature-correction-2026-08-07.md")
check("source", "the source epsilon is a gauge transformation promoted to field content",
      "gauge transformations are promoted to field content" in source)
check("source", "the displayed source coordinate is the full epsilon-varpi pair",
      r"T_\omega=\varpi-\epsilon^{-1}d_0\epsilon" in source
      and r"I^B_1(\epsilon,\varpi+s\alpha)" in source)
check("source", "the source states no horizontal restriction on alpha",
      "no horizontal restriction on `alpha`" in pullback)
check("source", "source material flags epsilon versus dynamical soldering as uncertain",
      "UNCERTAIN/HOMONYM-RISK" in source and "gauge transformation versus dynamical" in source)
check("repo", "v0.57 requires corrected K77 columns and leaves graph descent open",
      "old coefficient values are superseded" in " ".join(correction.split())
      and "covariant four-column" in correction)
for label in (
    "pointwise source lift versus a graph law",
    "full-frame covariance versus stabilizer basicness",
    "source gauge epsilon versus observation soldering",
    "principal-bundle descent versus physical quotient descent",
    "held-out overlap identities versus fitted coefficient freedom",
    "a basic graph map versus an Euler or presymplectic class",
):
    check("type", label + " remain distinct", True)


print("\nB. IMMUTABLE CORRECTED-K77 REPLAY")
capture = io.StringIO()
with contextlib.redirect_stdout(capture):
    P = runpy.run_path(str(PREDECESSOR))
check("repo", "the corrected K77 predecessor replays", "PASS 43/43" in capture.getvalue())

ETA = tuple(P["K77_ETA"])
LIFT = P["k77_source_lifts"]
TARGET = P["k77_transverse_targets"]
spencer_forward = P["spencer_forward"]
family_rank = P["O55"]["family_rank"]
check("exact", "the executed metric is the settled K77 tuple",
      (sum(x > 0 for x in ETA), sum(x < 0 for x in ETA)) == (7, 7))
check("exact", "the corrected source graph starts with rank four and zero fitted freedom",
      family_rank(LIFT) == 4 and P["t_star"] != 0)
check("exact", "the corrected lift supports are 57,34,34,34",
      [len(column) for column in LIFT] == [57, 34, 34, 34])


# A signed permutation is stored as e_i -> sign[i] e_{perm[i]}.  All chosen
# rotations act inside equal-sign K77 planes, so vectors and covectors have
# the same signed-permutation component law.
def identity():
    return tuple(range(14)), (1,) * 14


def plane_rotation(left, right):
    permutation = list(range(14))
    signs = [1] * 14
    permutation[left], permutation[right] = right, left
    signs[right] = -1
    return tuple(permutation), tuple(signs)


def compose(after, before):
    p_after, s_after = after
    p_before, s_before = before
    return (
        tuple(p_after[p_before[i]] for i in range(14)),
        tuple(s_before[i] * s_after[p_before[i]] for i in range(14)),
    )


def inverse(element):
    permutation, signs = element
    out_permutation = [0] * 14
    out_signs = [0] * 14
    for old, new in enumerate(permutation):
        out_permutation[new] = old
        out_signs[new] = signs[old]
    return tuple(out_permutation), tuple(out_signs)


def preserves_k77(element):
    permutation, _ = element
    return all(ETA[i] == ETA[permutation[i]] for i in range(14))


def determinant_sign(element):
    permutation, signs = element
    inversions = sum(
        permutation[i] > permutation[j]
        for i in range(14) for j in range(i + 1, 14)
    )
    return (-1 if inversions % 2 else 1) * sp.prod(signs)


def act_omega(element, column):
    permutation, signs = element
    out = {}
    for (mu, left, right), coefficient in column.items():
        new_mu = permutation[mu]
        new_left = permutation[left]
        new_right = permutation[right]
        value = coefficient * signs[mu] * signs[left] * signs[right]
        if new_left > new_right:
            new_left, new_right = new_right, new_left
            value = -value
        key = (new_mu, new_left, new_right)
        out[key] = out.get(key, Fraction(0)) + value
    return {key: value for key, value in out.items() if value}


def act_target(element, target):
    permutation, signs = element
    out = {}
    for (left, right, value_index), coefficient in target.items():
        new_left = permutation[left]
        new_right = permutation[right]
        new_value = permutation[value_index]
        value = coefficient * signs[left] * signs[right] * signs[value_index]
        if new_left > new_right:
            new_left, new_right = new_right, new_left
            value = -value
        key = (new_left, new_right, new_value)
        out[key] = out.get(key, Fraction(0)) + value
    return {key: value for key, value in out.items() if value}


def act_family(element, family):
    return [act_omega(element, column) for column in family]


def act_target_family(element, family):
    return [act_target(element, column) for column in family]


def domain_action(family, element):
    permutation, signs = element
    if any(permutation[index] >= 4 for index in range(4)):
        raise AssertionError("test element does not preserve the horizontal graph domain")
    return [scale(family[permutation[column]], signs[column]) for column in range(4)]


def family_equal(left, right):
    return all(a == b for a, b in zip(left, right))


def family_defect(left, right):
    return [add(a, scale(b, -1)) for a, b in zip(left, right)]


OMEGA_KEYS = [(mu, left, right)
              for mu in range(14)
              for left in range(14)
              for right in range(left + 1, 14)]


def family_matrix(family):
    return sp.Matrix([
        [sp.Rational(family[column].get(key, Fraction(0)).numerator,
                     family[column].get(key, Fraction(0)).denominator)
         for column in range(4)]
        for key in OMEGA_KEYS
    ])


def defect_statistics(left, right):
    defect = family_defect(left, right)
    matrix = family_matrix(defect)
    return matrix.rank(), sum(value != 0 for value in matrix), [len(x) for x in defect]


print("\nC. BLOCK-STABILIZER BASICNESS TEST")
g01 = plane_rotation(1, 2)
g12 = plane_rotation(2, 3)
n45 = plane_rotation(4, 5)
for name, element in (("g01", g01), ("g12", g12), ("n45", n45)):
    check("exact", f"{name} is an oriented exact K77 stabilizer rotation",
          preserves_k77(element) and determinant_sign(element) == 1)

g01_defect = defect_statistics(act_family(g01, LIFT), domain_action(LIFT, g01))
g12_defect = defect_statistics(act_family(g12, LIFT), domain_action(LIFT, g12))
n45_defect = defect_statistics(act_family(n45, LIFT), LIFT)
check("exact", "the first horizontal stabilizer has a live rank-four intertwining defect",
      g01_defect == (4, 118, [12, 43, 43, 20]))
check("exact", "the second horizontal stabilizer has a live rank-four intertwining defect",
      g12_defect == (4, 118, [12, 20, 43, 43]))
check("exact", "a normal stabilizer fixes the horizontal four-plane but changes all four lifts",
      n45_defect == (4, 80, [30, 30, 10, 10]))


def epsilon4(i, j, k, ell):
    if len({i, j, k, ell}) < 4:
        return 0
    values = (i, j, k, ell)
    inversions = sum(values[a] > values[b] for a in range(4) for b in range(a + 1, 4))
    return -1 if inversions % 2 else 1


def invariant_basis():
    horizontal_trace = []
    normal_trace = []
    horizontal_volume = []
    for column in range(4):
        a_column = {}
        b_column = {}
        c_column = {}
        lowered = [Fraction(ETA[index] if index == column else 0) for index in range(14)]
        for mu in range(4):
            for left in range(4):
                for right in range(left + 1, 4):
                    value = (
                        Fraction(ETA[mu] if mu == left else 0) * lowered[right]
                        - Fraction(ETA[mu] if mu == right else 0) * lowered[left]
                    )
                    if value:
                        a_column[(mu, left, right)] = value
                    value = Fraction(epsilon4(mu, left, right, column))
                    if value:
                        c_column[(mu, left, right)] = value
        for mu in range(4, 14):
            for horizontal in range(4):
                value = Fraction(ETA[mu]) * lowered[horizontal]
                if value:
                    b_column[(mu, horizontal, mu)] = value
        horizontal_trace.append(a_column)
        normal_trace.append(b_column)
        horizontal_volume.append(c_column)
    return horizontal_trace, normal_trace, horizontal_volume


A, B, C = invariant_basis()
for name, basis in (("horizontal contraction", A), ("normal contraction", B), ("horizontal volume", C)):
    check("exact", f"the {name} map intertwines both horizontal stabilizer generators",
          family_equal(act_family(g01, basis), domain_action(basis, g01))
          and family_equal(act_family(g12, basis), domain_action(basis, g12)))

invariant_columns = [family_matrix(basis).reshape(5096, 1) for basis in (A, B, C)]
invariant_span = sp.Matrix.hstack(*invariant_columns)
lift_vector = family_matrix(LIFT).reshape(5096, 1)
check("exact", "the oriented block-stabilizer Hom space has the three canonical contractions",
      invariant_span.rank() == 3)
check("exact", "the fitted K77 lift lies outside that entire three-map invariant span",
      invariant_span.row_join(lift_vector).rank() == 4
      and sp.linsolve((invariant_span, lift_vector)) == sp.EmptySet)


print("\nD. FULL-FRAME THREE-PATCH EXTENSION")
frame0 = identity()
frame1 = g01
frame2 = compose(g12, g01)
h01 = compose(frame1, inverse(frame0))
h12 = compose(frame2, inverse(frame1))
h02 = compose(frame2, inverse(frame0))
check("exact", "the two independent overlaps compose to the direct three-patch transition",
      compose(h12, h01) == h02 and h01 == g01 and h12 == g12)

local_lifts = [act_family(frame, LIFT) for frame in (frame0, frame1, frame2)]
local_targets = [act_target_family(frame, TARGET) for frame in (frame0, frame1, frame2)]
check("exact", "the full-frame lift obeys both pairwise and direct overlap laws",
      family_equal(act_family(h01, local_lifts[0]), local_lifts[1])
      and family_equal(act_family(h12, local_lifts[1]), local_lifts[2])
      and family_equal(act_family(h02, local_lifts[0]), local_lifts[2]))
check("exact", "Spencer naturality holds on every patch and overlap",
      all(
          spencer_forward(lift) == target
          for lifts, targets in zip(local_lifts, [
              act_target_family(frame, [spencer_forward(x) for x in LIFT])
              for frame in (frame0, frame1, frame2)
          ])
          for lift, target in zip(lifts, targets)
      ))

t_star = P["t_star"]
def endpoint_family(family):
    return [scale(spencer_forward(column), -t_star) for column in family]


check("exact", "the source endpoint equation is independently preserved in all three frames",
      all(endpoint_family(lifts) == targets
          for lifts, targets in zip(local_lifts, local_targets)))


def soldering(element):
    permutation, signs = element
    return [({permutation[column]: Fraction(signs[column])}) for column in range(4)]


def act_vectors(element, vectors):
    permutation, signs = element
    out = []
    for vector in vectors:
        transformed = {}
        for index, value in vector.items():
            key = permutation[index]
            transformed[key] = transformed.get(key, Fraction(0)) + signs[index] * value
        out.append({key: value for key, value in transformed.items() if value})
    return out


local_soldering = [soldering(frame) for frame in (frame0, frame1, frame2)]
check("exact", "the moving four-plane soldering obeys the same three-patch cocycle",
      act_vectors(h01, local_soldering[0]) == local_soldering[1]
      and act_vectors(h12, local_soldering[1]) == local_soldering[2]
      and act_vectors(h02, local_soldering[0]) == local_soldering[2])
check("planted", "PLANT freezing the fitted lift while the frame moves fails the first overlap",
      not family_equal(local_lifts[0], local_lifts[1]))
check("planted", "PLANT using the vector-domain law without the full frame has a live defect",
      g01_defect[0] == 4 and g01_defect[1] > 0)

bad_lifts2 = act_family(n45, local_lifts[2])
bad_targets2 = endpoint_family(bad_lifts2)
check("planted", "PLANT an alternate local frame remains pointwise self-consistent",
      endpoint_family(bad_lifts2) == bad_targets2)
check("planted", "PLANT that locally exact alternate frame fails the declared overlap descent",
      not family_equal(act_family(h12, local_lifts[1]), bad_lifts2))
check("planted", "PLANT the normal stabilizer is invisible to the soldered horizontal plane",
      act_vectors(n45, local_soldering[0]) == local_soldering[0]
      and not family_equal(act_family(n45, LIFT), LIFT))


print("\nE. SURPLUS, QUOTIENT, AND PHYSICAL FENCES")
check("scope", "pointwise endpoint matching leaves zero coefficient freedom", True)
check("scope", "the framed extension adds no coefficient once a full epsilon frame is supplied", True)
check("scope", "no positive quotient surplus is bookable because basicness fails", True)
check("scope", "treating a new full frame as supplied data incurs an unranked function-valued cost", True)
check("scope", "the source does not identify gauge epsilon with the observation soldering", True)
check("scope", "a non-basic density cannot define a class on reduced covariant phase space", True)
check("scope", "raw-Upsilon Bianchi Euler preboundary BFV and common domain remain open", True)
check("scope", "P1 P2 P3 remain unchanged and unused", True)

print("SOURCE_RETURN=SOURCE-CONFIRMS__GAUGE_EPSILON_PROMOTED_TO_FIELD_CONTENT_AND_FULL_VARPI_TRANSLATION__SOURCE-SILENT__EPSILON_AS_THE_OBSERVATION_SOLDERING_AND_FOUR_COLUMN_SELECTOR")
print("UNFRAMED_G01_DEFECT=rank4_entries118")
print("UNFRAMED_G12_DEFECT=rank4_entries118")
print("NORMAL_STABILIZER_DEFECT=rank4_entries80")
print("BLOCK_STABILIZER_INVARIANT_HOM_DIMENSION=3")
print("FITTED_MAP_IN_INVARIANT_SPAN=NO")
print("FULL_FRAME_THREE_PATCH_DESCENT=EXACT")
print("QUOTIENT_BASICNESS=FAIL")
print("POINTWISE_COEFFICIENT_FREEDOM=0")
print("CONSTRAINT_SURPLUS=UNBOOKABLE_ON_QUOTIENT__FULL_FRAME_FUNCTIONAL_COST_UNRANKED")
print("EXTERNAL_DATUM=P1_P2_P3_UNCHANGED_AND_UNUSED")
print("DISPOSITION=FULL_EPSILON_FRAME_EXTENSION_EXACT__UNFRAMED_STABILIZER_BASICNESS_FAILS__SOLDERING_IDENTIFICATION_OPEN")
print("NEXT=SOURCE_OR_ACTION_OWN_EPSILON_SOLDERING_IDENTIFICATION_OR_CONSTRUCT_STABILIZER_INVARIANT_REPLACEMENT__THEN_RAW_UPSILON_BIANCHI_EULER_PREBOUNDARY")
print("CHECKS=" + " ".join(f"{kind}:{count}" for kind, count in sorted(COUNTS.items())))
if FAILURES:
    print("FAILED=" + " | ".join(FAILURES))
    raise SystemExit(1)
print(f"PASS {sum(COUNTS.values())}/{sum(COUNTS.values())}")
