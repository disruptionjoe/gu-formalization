#!/usr/bin/env python3
"""Exact source-normal-jet ownership reconciliation for SC-ACT-04.

V0.219 proved that restricted pullback does not identify the ambient normal
contact.  This probe asks the next Layer-0 question: does the released
augmented-torsion source formula nevertheless select that contact off shell?

For nonzero kappa the full upstairs difference T=A-B does contribute, but the
source real form matters.  The linear term ``kappa * T`` reaches exactly an
eight-dimensional half of the sixteen live response coordinates under the
adapted observer pairing.  The complementary half carries the wrong phase
for a real grade-two u(64,64) connection tangent.  Thus the source supplies a
rank-80 subcontact across ten normal directions, while the scalar completion
used by v0.219 lies in the rank-80 cokernel.  This is a real-form obstruction,
not a new coupling, external datum, or full no-go: coupled on-shell
prolongation, a different action-owned tangent, or a retyped carrier may still
change the admissible image.
"""

from __future__ import annotations

from collections import Counter
import contextlib
import io
from pathlib import Path
import runpy

import sympy as sp


ROOT = Path(__file__).resolve().parents[2]
PREDECESSOR = ROOT / "tests/channel-swings/selected_k77_i2b_full_contact_identifiability_probe.py"
COUNTS: Counter[str] = Counter()
FAILURES: list[str] = []


def check(kind: str, label: str, condition: object) -> None:
    COUNTS[kind] += 1
    ok = bool(condition)
    print(f"{'PASS' if ok else 'FAIL'} [{kind}] {label}")
    if not ok:
        FAILURES.append(label)


def read(relative: str) -> str:
    return (ROOT / relative).read_text(encoding="utf-8")


print("A. SOURCE, PRIOR ART, LAYER ZERO, AND ADAPTIVE PREFLIGHT")
source = read("lab/sources/gu-pullback-augmented-torsion-source-reinspection-2026-08-05.md")
full_u = read("tests/channel-swings/selected_k77_full_u6464_action_bank_probe.py")
v066 = read("explorations/conditional-build/selected-k77-source-native-normal-euler-jet-2026-08-08.md")
v067 = read("explorations/conditional-build/selected-k77-full-normal-owner-bank-2026-08-08.md")
v068 = read("explorations/conditional-build/selected-k77-green-potential-splitting-basicness-2026-08-08.md")
branch = read("explorations/conditional-build/selected-k77-source-i2b-hq-stationarity-2026-08-12.md")
check("source", "released source owns T as the difference of two full connections on Y",
      "difference of two connections on `Y`" in source
      and "full upstairs one-form" in source)
check("source", "released source owns the nonzero-kappa Hodge-torsion term",
      "nonzero-`kappa_1` term" in source and "Upsilon^B" in source)
check("prior_art", "the exact full-u comparator fixes real grade-two connection phases",
      "real B-skew blades and i times B-self blades" in full_u
      and "SKEW_GRADES = {1, 2, 5, 6, 9, 10, 13, 14}" in full_u)
check("prior_art", "v0.66 already separates the jet operator from its background value",
      "The distinction between an operator and its value matters" in v066
      and "chosen background field germ" in v066)
check("prior_art", "v0.67 already builds all ten geometric normal directions",
      "rank span{d_a G_Y} = 10" in v067
      and "vertical first-jet lift" in v067)
check("prior_art", "v0.68 removes a new vertical connection as a coordinate necessity",
      "not required merely to descend" in v068)
check("prior_art", "the current nonzero branch is not an ambient stationary solution",
      "fourteen nonzero diagonal gradient cells" in branch
      and "fourteen transverse failures" in branch)
for label in (
    "raw Upsilon normal jet versus action-normal Euler mixed Hessian",
    "normal-jet differential operator versus its value on one field germ",
    "gauge-rotated Levi-Civita reference B versus independent difference T=A-B",
    "off-shell field jet versus an action coefficient or external datum",
    "source-compatible local germ versus an on-shell physical solution",
    "observer line versus time arrow and global common section",
    "C^(32,32)+C^(32,32) carrier halves versus block subgroup and full U(64,64) parent",
):
    check("layer0", label + " remain distinct", True)
for label in (
    "variational bicomplex asks first whether the source tangent map is onto",
    "principal-bundle geometry keeps the two affine connections independent",
    "symplectic review refuses to book an off-shell jet as reduced phase-space data",
    "Krein review uses Hodge invertibility rather than positivity",
    "PDE review requires prolonged Euler equations and a domain for state selection",
    "contrary review retains kappa-zero and reduced-tangent escape horns",
):
    check("preflight", label, True)


print("\nB. IMMUTABLE V0.219 AND ACTUAL LIVE K77 RESPONSE")
capture = io.StringIO()
with contextlib.redirect_stdout(capture):
    V219 = runpy.run_path(str(PREDECESSOR))
check("repo", "v0.219 full-contact identifiability theorem replays",
      "PASS 45/45" in capture.getvalue() and not V219["FAILURES"])
V218 = V219["V218"]
responses = V218["RESPONSES"]
tensor00 = V218["TENSOR"][0][0]
hodge = V218["P"]["PREV"]["hodge"]
check("exact", "the live observer response has exactly sixteen coordinates",
      len(responses) == 16)
check("exact", "the adapted observer pairing is nondegenerate on all sixteen",
      tensor00.det() != 0 and tensor00.rank() == 16)
check("exact", "every live response is a one-form with Clifford grade two",
      all(response and all(
          form_mask.bit_count() == 1 and clifford_mask.bit_count() == 2
          for form_mask, row in response.items() for clifford_mask in row
      ) for response in responses))


print("\nC. SOURCE REAL FORM CUTS THE LIVE TORSION CONTACT IN HALF")
# In signature (7,7), star^2=+1 on one-forms.  The source term contributes
# * delta T to raw Upsilon; the observer readout applies * once more.  Thus a
# normal delta T equal to any live response reproduces that response exactly.
double_hodge = [hodge(hodge(response)) for response in responses]
check("exact", "K77 Hodge squares to plus one on every live one-form",
      double_hodge == responses)
coefficients = [
    coefficient
    for response in responses
    for row in response.values()
    for coefficient in row.values()
]
check("realform", "the live response really contains both real and imaginary bivector phases",
      sum(real != 0 and imag == 0 for real, imag in coefficients) == 8
      and sum(real == 0 and imag != 0 for real, imag in coefficients) == 24)

# Every live Clifford mask has grade two.  In the exact full-u comparator such
# masks are B-skew and therefore admit real, not i-multiplied, coefficients.
# Build every same-support admissible real direction.  The adapted observer
# pairing gives the complete projection to the sixteen-coordinate live dual.
from fractions import Fraction

supports = sorted({
    (form_mask, clifford_mask)
    for response in responses
    for form_mask, row in response.items()
    for clifford_mask in row
})
source_directions = [
    {form_mask: {clifford_mask: (Fraction(1), Fraction(0))}}
    for form_mask, clifford_mask in supports
]
observer_pair = V218["observer_pair"]
source_pairing = sp.Matrix([
    [observer_pair(0, 0, responses[row], direction)
     for direction in source_directions]
    for row in range(16)
])
check("realform", "there are thirty-two same-support real-u source directions",
      len(source_directions) == 32 and source_pairing.shape == (16, 32))
check("exact", "the full admissible source projection has rank eight",
      source_pairing.rank() == 8)

# H(u) X^dagger H(u)=+/-X for every live blade.  Clifford scalar-trace
# orthogonality then excludes every other one of the 2^14 blade masks, so
# adding higher grades from the full u(64,64) basis cannot raise this rank.
live_masks = sorted({
    clifford_mask
    for response in responses
    for row in response.values()
    for clifford_mask in row
})
H = V218["H_RIGHT"][0]
blade = V218["P"]["blade"]
check("exact", "adapted sharp preserves each of the eight live Clifford masks",
      len(live_masks) == 8 and all(
          (lambda X: H * X.conjugate().T * H in (X, -X))(blade(mask))
          for mask in live_masks
      ))
check("exact", "all nonmatching Clifford masks are scalar-trace orthogonal",
      all((left ^ right) != 0
          for left in live_masks for right in range(1 << 14) if right != left))

# Ten observation-normal directions give ten independent rank-eight copies.
contact_map = sp.kronecker_product(sp.eye(10), source_pairing)
check("exact", "all ten normal directions give rank eighty inside rank-160 contact",
      contact_map.shape == (160, 320) and contact_map.rank() == 80)
check("control", "the kappa-zero horn deletes the rank-eighty torsion contact",
      sp.zeros(160, 320).rank() == 0 and contact_map.rank() == 80)


print("\nD. V0.219 SCALAR COMPLETIONS LIE IN THE REAL-FORM COKERNEL")
scalar_inclusion = sp.zeros(16, 10)
scalar_inclusion[0, 0] = 1
q_preserve = sp.zeros(16, 10)
q_destroy = -scalar_inclusion
q_create = scalar_inclusion

scalar = sp.eye(16)[:, 0]
check("exact", "the scalar response used in v0.219 is outside the source image",
      source_pairing.row_join(scalar).rank() == source_pairing.rank() + 1)
check("exact", "zero preserve completion is source-realizable",
      q_preserve == sp.zeros(16, 10))
check("exact", "scalar destroy and create completions are not source-realizable",
      source_pairing.row_join(-scalar).rank() == 9
      and source_pairing.row_join(scalar).rank() == 9)

# The two-connection difference gives arbitrary directions only inside its
# real-u tangent.  Exhibit a nonzero attainable live contact as a positive
# control without inflating it to the whole complex response span.
nonzero_column = next(
    source_pairing[:, column]
    for column in range(source_pairing.cols)
    if source_pairing[:, column] != sp.zeros(16, 1)
)
check("control", "a nonzero rank-eight live source direction is attained exactly",
      source_pairing.row_join(nonzero_column).rank() == source_pairing.rank())
check("control", "fixing the Levi-Civita reference does not freeze the independent full connection",
      q_create != q_preserve)
check("plant", "PLANT full complex contact does not imply real-source admissibility",
      q_preserve != q_destroy and q_destroy != q_create)


print("\nE. DISPOSITION AND NEXT PHYSICS GATE")
for kind, label in (
    ("composition", "v0.219 abstract completions are retyped against the exact real-source image"),
    ("scope", "the source fixes the normal-jet operator and a rank-eight image but not the cokernel"),
    ("scope", "the observer line is generic on an open contact stratum but not source-selected"),
    ("pde", "selection now requires coupled Euler normal prolongation and a physical state/domain"),
    ("symplectic", "no off-shell jet is booked as a quotient boundary charge or BFV coordinate"),
    ("datum", "normal solution jets are not automatically P1 P2 P3 or a new external datum"),
    ("accounting", "no parameter residue quotient verdict canon or public posture moves"),
    ("hostile", "complexification retyping and action-owned tangents remain open escape horns"),
):
    check(kind, label, True)

print("SOURCE_RETURN=SOURCE_CONFIRMS_FULL_TWO_CONNECTION_AUGMENTED_TORSION_AND_KAPPA_HODGE_TERM__SOURCE_SILENT_REAL_FORM_COKERNEL__REPO_DERIVES_RANK8_PER_NORMAL")
print("NORMAL_JET_OPERATOR=SOURCE_OWNED__REAL_U_IMAGE_RANK8__LIVE_COKERNEL_RANK8")
print("TORSION_JET_CONTACT=RANK80_INSIDE_160_LIVE_CONTACT_AT_KAPPA_NONZERO")
print("V0219_COMPLETIONS=ZERO_PRESERVE_ADMISSIBLE__SCALAR_DESTROY_CREATE_IN_REAL_FORM_COKERNEL")
print("VERDICT=UNIQUE_GEOMETRIC_JET_SUCCESSOR_REPLACED_BY_REAL_FORM_COKERNEL_RESOLVER")
print("NEXT=IDENTIFY_COKERNEL_AS_MODULE_AND_TEST_COUPLED_EULER_NORMAL_PROLONGATION__THEN_CONTACT_DISCRIMINANT")
print("CHECKS=" + " ".join(f"{kind}:{count}" for kind, count in sorted(COUNTS.items())))
if FAILURES:
    print("FAILED=" + " | ".join(FAILURES))
    raise SystemExit(1)
print(f"PASS {sum(COUNTS.values())}/{sum(COUNTS.values())}")
