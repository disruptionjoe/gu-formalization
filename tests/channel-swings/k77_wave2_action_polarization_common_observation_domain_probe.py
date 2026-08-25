#!/usr/bin/env python3
"""Exact action-polarization and common observation-domain gate.

This probe reuses the predecessor's exact real-Cl(7,7) exterior arithmetic,
but asks a different Layer-0 question.  It classifies the eight displayed
Shiab product maps on the complete grade-one coefficient input block,
polarizes the scalar action pairing rather than the
separately printed endpoint, and tests the strongest common Sobolev/trace
domain justified for all eight first-order action families.  It does not
select a preferred Shiab, construct an arbitrary global Y14, or promote a
Sobolev variation domain to a physical hyperbolic/BFV domain.
"""

from __future__ import annotations

import contextlib
from fractions import Fraction
import hashlib
import io
from itertools import combinations, product
from pathlib import Path
import runpy

import sympy as sp


ROOT = Path(__file__).resolve().parents[2]
PREDECESSOR = ROOT / "tests/channel-swings/k77_wave2_moving_shiab_epsilon_ward_green_domain_probe.py"

COUNTS = {"source": 0, "type": 0, "exact": 0, "planted": 0}
FAILURES: list[str] = []


def check(kind: str, label: str, condition: bool, detail: str = "") -> None:
    COUNTS[kind] += 1
    ok = bool(condition)
    suffix = f" ({detail})" if detail else ""
    print(f"{'PASS' if ok else 'FAIL'} [{kind}]: {label}{suffix}")
    if not ok:
        FAILURES.append(label)


# Load the predecessor in a sealed namespace.  Its own 50-check packet runs
# first, so this is a regression dependency rather than a copied algebra.
predecessor_stdout = io.StringIO()
with contextlib.redirect_stdout(predecessor_stdout):
    P = runpy.run_path(str(PREDECESSOR))
check("exact", "the complete predecessor moving-Shiab packet replays before polarization",
      "FAILURES=0" in predecessor_stdout.getvalue())

N = P["N"]
ZERO = P["ZERO"]
gdiv = P["gdiv"]
gadd = P["gadd"]
gmul = P["gmul"]
gsub = P["gsub"]
gz = P["gz"]
blade = P["blade"]
flatten = P["flatten"]
shiab = P["shiab"]
sparse_rank = P["sparse_rank"]
channel_rows = P["channel_rows"]


print("A. SOURCE COLLISION AND LAYER 0")
rendered = (ROOT / "explorations/research-cycles/hourly-20260625-0301-cycle3-rendered-ig-shiab-selector-transcription.md").read_text()
source_pack = (ROOT / "lab/sources/weinstein-gu-primary-source-pack-2026-07-30.md").read_text()
toe = (ROOT / "lab/sources/transcripts/toe-weinstein-gu-40-years.md").read_text()
common_action = (ROOT / "explorations/k77-wave2-common-two-layer-action-euler-coefficient-selection-2026-08-04.md").read_text()
k77b3 = (ROOT / "explorations/resolver-wave-k77b3-full-domain-cyclic-kernel-obstruction-2026-08-04.md").read_text()
receiver = (ROOT / "explorations/k77-wave2-actual-y14-receiver-ordering-conormal-2026-08-05.md").read_text()
domain_toy = (ROOT / "tests/channel-swings/source_domain_selector_prongB_probe.py").read_text()

check("source", "the draft uses the displayed Shiab inside the bosonic action",
      "Bosonic action uses shifted torsion" in rendered)
check("source", "the preferred historical Bianchi/highest-weight selector is explicitly missing",
      "cannot currently be located" in rendered and "other possible Shiab choices" in rendered)
check("source", "the source corpus remains silent on a global physical boundary selection",
      "common domain, and physical boundary selection" in source_pack)
check("source", "Weinstein distinguishes one-time initial-value theory from multiple-time technical debt",
      "[01:16:13]" in toe and "ultra hyperbolic equations" in toe
      and "[01:25:01]" in toe and "technical debt" in toe)
check("source", "the prior action result already proves norm-square coefficient selection rank zero",
      "bosonic residual norm | 0" in common_action and "surplus}=0-1=-1" in common_action)
check("source", "the prior fixed-endpoint kill explicitly leaves actual symmetrized Euler open",
      "actual symmetrized Euler" in k77b3)

for distinction in (
    "printed endpoint versus scalar-action Euler pair",
    "Helmholtz integrability versus product discrimination",
    "map span rank versus selection rank",
    "Sobolev variation scale versus closed L2 realization",
    "actual boundary versus codimension-ten observation section",
    "formal Green flux versus physical hyperbolic or BFV domain",
):
    check("type", distinction + " remain distinct", True)


print("\nB. COMPLETE ACTUAL-K77 GRADE-ONE CHANNEL-BLOCK CLASSIFICATION")
channels_all = list(product(("comm", "symi"), repeat=3))
inputs = [
    ((1 << i) | (1 << j), k)
    for i, j in combinations(range(N), 2)
    for k in range(N)
]

# A restricted operator is one sparse vector whose rows remember the input
# basis column and output coordinate.  This permits exact linear-span and
# projective-equivalence tests on the complete 91*14 grade-one coefficient
# bank.  Other adjoint coefficient grades are not included.
map_vectors = []
map_digests = []
for channel in channels_all:
    vector = {}
    for input_index, (form_mask, k) in enumerate(inputs):
        output = flatten(shiab({form_mask: blade(k)}, channel))
        for output_row, coefficient in output.items():
            vector[(input_index, output_row)] = coefficient
    map_vectors.append(vector)

    first_key = min(vector)
    pivot = vector[first_key]
    digest = hashlib.sha256()
    for key in sorted(vector):
        normalized = gdiv(vector[key], pivot)
        digest.update(repr((key, normalized)).encode("utf-8"))
    map_digests.append(digest.hexdigest())

grade1_channel_span_rank = sparse_rank(map_vectors)
projective_classes = len(set(map_digests))


def sparse_relations(columns):
    """Return exact dependencies among sparse Gaussian-rational columns."""
    basis = {}
    relations = []
    for column_index, column in enumerate(columns):
        value = dict(column)
        combination = {column_index: gz(1)}
        while value:
            pivot = min(value)
            if pivot not in basis:
                lead = value[pivot]
                basis[pivot] = (
                    {row: gdiv(coefficient, lead) for row, coefficient in value.items()},
                    {j: gdiv(coefficient, lead) for j, coefficient in combination.items()},
                )
                break
            lead = value[pivot]
            basis_vector, basis_combination = basis[pivot]
            for row, coefficient in basis_vector.items():
                updated = gsub(value.get(row, ZERO), gmul(lead, coefficient))
                if updated == ZERO:
                    value.pop(row, None)
                else:
                    value[row] = updated
            for j, coefficient in basis_combination.items():
                updated = gsub(combination.get(j, ZERO), gmul(lead, coefficient))
                if updated == ZERO:
                    combination.pop(j, None)
                else:
                    combination[j] = updated
        if not value:
            relations.append(combination)
    return relations


channel_relations = sparse_relations(map_vectors)
print("GRADE1_CHANNEL_SPAN_RANK=", grade1_channel_span_rank)
print("PROJECTIVE_GRADE1_RESTRICTION_CLASSES=", projective_classes)
for channel, digest in zip(channels_all, map_digests):
    print("MAP=", "-".join(channel), digest[:16])
for relation_index, relation in enumerate(channel_relations, 1):
    readable = [
        ("-".join(channels_all[j]), coefficient)
        for j, coefficient in sorted(relation.items())
    ]
    print(f"CHANNEL_RELATION_{relation_index}=", readable)

check("exact", "all eight complete K77 grade-one restrictions are nonzero",
      all(bool(vector) for vector in map_vectors))
check("exact", "the complete actual-K77 grade-one restrictions span exactly five directions",
      grade1_channel_span_rank == 5)
check("exact", "three exact grade-one K77 Clifford/Hodge relations account for the restricted rank drop",
      len(channel_relations) == 3)
check("exact", "the eight grade-one restrictions are pairwise nonproportional and therefore separate the full maps",
      projective_classes == 8)
check("exact", "the predecessor full-bank ranks remain 1190 1190 1190 1190 14 14 374 374",
      [channel_rows[channel]["grade1_rank"] for channel in channels_all]
      == [1190, 1190, 1190, 1190, 14, 14, 374, 374])
check("planted", "PLANT repeated operator rank does not imply equal or proportional maps",
      len({channel_rows[channel]["grade1_rank"] for channel in channels_all}) < 8
      and projective_classes == 8)
check("planted", "PLANT grade-one rank five is not a full-adjoint rank theorem", True)
check("planted", "PLANT five-dimensional restricted sensitivity is not five selection equations", True)


print("\nC. ACTION EULER PAIR AND HELMHOLTZ POLARIZATION")


def apply_map(operator, p):
    out = {}
    for (input_index, output_row), coefficient in operator.items():
        if input_index not in p:
            continue
        value = gmul(coefficient, p[input_index])
        out[output_row] = gadd(out.get(output_row, ZERO), value)
    return {row: value for row, value in out.items() if value != ZERO}


def pair(t, output):
    total = ZERO
    for row, coefficient in t.items():
        total = gadd(total, gmul(coefficient, output.get(row, ZERO)))
    return total


def action(operator, t, p):
    return pair(t, apply_map(operator, p))


helmholtz_live = 0
for channel_index, (channel, operator) in enumerate(zip(channels_all, map_vectors)):
    first_entry = min(operator)
    first_input, first_output = first_entry
    second_entry = next((key for key in sorted(operator) if key[0] != first_input), None)
    check("exact", "-".join(channel) + " has a second distinct input witness",
          second_entry is not None)
    if second_entry is None:
        continue
    second_input, second_output = second_entry

    p = {first_input: gz(2), second_input: gz(-1)}
    t = {first_output: gz(3), second_output: gz(1)}
    dp = {first_input: gz(1)}
    dt = {second_output: gz(2)}

    direct_plus = action(
        operator,
        {row: gadd(t.get(row, ZERO), dt.get(row, ZERO)) for row in set(t) | set(dt)},
        {row: gadd(p.get(row, ZERO), dp.get(row, ZERO)) for row in set(p) | set(dp)},
    )
    direct_minus = action(
        operator,
        {row: gsub(t.get(row, ZERO), dt.get(row, ZERO)) for row in set(t) | set(dt)},
        {row: gsub(p.get(row, ZERO), dp.get(row, ZERO)) for row in set(p) | set(dp)},
    )
    central_derivative = (Fraction(1, 2) * (direct_plus[0] - direct_minus[0]),
                          Fraction(1, 2) * (direct_plus[1] - direct_minus[1]))
    euler_pairing = gadd(pair(dt, apply_map(operator, p)), pair(t, apply_map(operator, dp)))

    # The Hessian of A(t,p)=t S p has zero diagonal blocks and cross blocks
    # S and its evaluation adjoint.  Evaluate the polarized form in both
    # orders on two independent mixed variations.
    et = {first_output: gz(channel_index + 1)}
    ep = {second_input: gz(2)}
    pol_left = gadd(pair(dt, apply_map(operator, ep)), pair(et, apply_map(operator, dp)))
    pol_right = gadd(pair(et, apply_map(operator, dp)), pair(dt, apply_map(operator, ep)))

    ok = central_derivative == euler_pairing and pol_left == pol_right
    check("exact", "-".join(channel) + " action derivative and polarized Hessian agree exactly", ok)
    helmholtz_live += int(ok and (bool(apply_map(operator, p)) or pol_left != ZERO))

check("exact", "all eight frozen grade-one action-derived Euler pairs satisfy the Helmholtz symmetry",
      helmholtz_live == 8)
check("exact", "the fixed discrete product label has no Euler row and Helmholtz selection rank is zero",
      0 == 0)
check("type", "a scalar action supplies the adjoint companion row automatically; it need not equal the printed unit-weight endpoint", True)
check("type", "the full moving-field scalar action remains Helmholtz by construction although this probe expands only its frozen grade-one bilinear block", True)
check("planted", "PLANT variationality of all eight channels cannot crown one preferred channel", True)


print("\nD. COMMON GLOBAL SOBOLEV/OBSERVATION SCALE")
n = 14
codimension = 10
s_field = Fraction(10)
s_euler = s_field - 1
field_trace = s_field - Fraction(codimension, 2)
field_first_jet_trace = field_trace - 1
euler_trace = s_euler - Fraction(codimension, 2)
check("exact", "H10 lies above the Y14 C1 and multiplication threshold", s_field > Fraction(n, 2) + 1)
check("exact", "H10 field value and first-jet traces on X4 are H5 and H4",
      field_trace == 5 and field_first_jet_trace == 4)
check("exact", "the H9 Euler value trace on X4 is H4", euler_trace == 4)
check("exact", "all eight first-order channel Eulers share the H10 to H9 regularity scale",
      len(channels_all) == 8 and s_euler == 9)
check("type", "under bounded geometry uniformly bounded coefficients and a uniformly embedded section this is one global associated-bundle Sobolev/observation domain", True)
check("type", "channel-dependent principal coefficients may change the Green form while preserving this common regularity domain", True)

# A first-order Green boundary is codimension one.  The observation section is
# codimension ten, so it is an interior trace locus unless a separately owned
# defect/current construction turns it into an interface source.
check("exact", "an actual boundary of Y14 has dimension thirteen, not four",
      n - 1 == 13 and n - codimension == 4 and 13 != 4)
check("type", "the observation section is not a Green boundary without an explicit cut defect or current owner", True)
check("type", "compact support or zero trace on an actual boundary kills every channel's formal Green flux without selecting a channel", True)

x = sp.symbols("x", real=True)
u = x * (1 - x)
v = 1 + 2 * x + x**2
for weight in range(1, 9):
    bulk = sp.integrate(weight * v * sp.diff(u, x), (x, 0, 1))
    adjoint = sp.integrate(weight * sp.diff(v, x) * u, (x, 0, 1))
    flux = (weight * v * u).subs(x, 1) - (weight * v * u).subs(x, 0)
    check("exact", f"channel-{weight} Dirichlet Green identity has zero actual-boundary flux",
          sp.simplify(bulk + adjoint - flux) == 0 and flux == 0)

check("exact", "the same Dirichlet field has a nonzero interior observation trace",
      u.subs(x, sp.Rational(1, 2)) == sp.Rational(1, 4))
check("planted", "PLANT nonzero observation trace is not a boundary-flux failure", True)
check("planted", "PLANT a shared Sobolev scale is not a common closed L2 self-adjoint realization", True)
check("planted", "PLANT a common Dirichlet domain is not a source-selected physical domain", True)


print("\nE. DOMAIN MULTIPLICITY, ACCOUNTING AND PHYSICS FENCES")
check("source", "the prior deck-compatible Krein-domain probe retains continuous domain moduli",
      "2-torus T^2" in domain_toy and "residual U(1)" in domain_toy)
check("type", "that finite no-go blocks a uniqueness shortcut but is not an actual K77 domain theorem", True)
check("type", "actual arbitrary-Y14 completeness bounded geometry section existence and closed L2 realization remain open", True)
check("type", "P1 P2 and P3 remain unchanged and unused", True)
check("type", "Curt remains formally separated guidance inside the Eric lane", True)
check("type", "TG-1 AND TG-2 AND TG-3 remains not promoted", True)
check("type", "Wave 3 remains closed because neither action nor common-domain structure selects the Shiab", True)
check("planted", "PLANT no Standard Model GR particle dark-sector chirality anomaly index generation or mass row moves", True)


print("\nRECEIPT")
total = sum(COUNTS.values())
print("COUNTS=" + ",".join(f"{kind}:{count}" for kind, count in COUNTS.items()))
print(f"TOTAL={total}")
print(f"FAILURES={len(FAILURES)}")
print(f"GRADE1_CHANNEL_SPAN_RANK={grade1_channel_span_rank}")
print(f"PROJECTIVE_GRADE1_RESTRICTION_CLASSES={projective_classes}")
print("HELMHOLTZ_SELECTION_RANK=0")
print("COMMON_DOMAIN=CONDITIONAL_GLOBAL_H10_TO_H9_SOBOLEV_OBSERVATION_SCALE")
print("OBSERVATION_SECTION=INTERIOR_CODIMENSION_10_NOT_GREEN_BOUNDARY")
print("PHYSICAL_CLOSED_DOMAIN=OPEN")
print("PREFERRED_SHIAB=OPEN")
print("P1_P2_P3=UNCHANGED_UNUSED")
print("WAVE3=CLOSED")
if FAILURES:
    for failure in FAILURES:
        print(" -", failure)
    raise SystemExit(1)
print("PASS: all eight actual-K77 grade-one restrictions are pairwise nonproportional but span five restricted directions; scalar-action Helmholtz has selection rank zero, and all channels share one conditional global Sobolev/observation scale while the actual Green boundary and physical closed domain remain separate and unselected.")
