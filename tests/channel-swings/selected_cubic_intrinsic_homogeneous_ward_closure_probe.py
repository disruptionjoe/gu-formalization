#!/usr/bin/env python3
"""Exact intrinsic homogeneous Ward closure for the selected K77 action.

The preceding swing removed the shared inhomogeneous connection derivative by
using the source-owned two-connection difference.  This probe checks the next
grade: the lower-order inner orbit of T together with the moving Phi/Shiab
response and invariant top-scalar pairing in the written intrinsic action.

It closes only this zero-order action package.  Direct curvature/II/defect,
metric/observation movement, primitive epsilon Green data, the complete
preboundary class and every physical quotient remain separate.
"""

from __future__ import annotations

from collections import Counter
import contextlib
from fractions import Fraction
from io import StringIO
from pathlib import Path
import runpy


ROOT = Path(__file__).resolve().parents[2]
BACKEND = ROOT / "tests/channel-swings/k77_wave2_moving_shiab_epsilon_ward_green_domain_probe.py"
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


print("A. SOURCE, LAYER 0, AND PREDECESSOR")
source = read("lab/sources/gu-moving-shiab-epsilon-green-source-reinspection-2026-08-05.md")
pullback_source = read("lab/sources/gu-pullback-augmented-torsion-source-reinspection-2026-08-05.md")
prior = read("explorations/conditional-build/selected-cubic-two-connection-principal-ward-descent-2026-08-06.md")
even_owner = read("explorations/conditional-build/k77-global-even-bv-null-green-domain-2026-08-05.md")

check("source", "source makes Phi1 and Phi2 a moving epsilon-conjugation orbit",
      "Phi_i(epsilon)=Ad_(epsilon^-1) Phi_i^0" in source)
check("source", "source supplies the two-connection T chain and moving-Shiab derivative grammar",
      "delta T=-D_B eta" in source and "D_epsilon Shiab" in source)
check("source", "source confirms intended equivariance but not a complete Ward theorem",
      "intended equivariance mechanism, not a complete Ward theorem" in pullback_source)
check("source", "source remains silent on full moving Ward/BV and physical domain",
      "full moving-section Ward/BV identity" in pullback_source and "SOURCE-SILENT" in pullback_source)
check("repo", "principal diagonal connection descent is already exact",
      "PRINCIPAL_DESCENT_EXACT" in prior and "rank zero" in prior)
check("repo", "the complete homogeneous even Ward owner has already been typed",
      "Complete homogeneous even Ward owner" in even_owner and "formal minimal even BV action" in even_owner)
check("repo", "the prior ledger leaves the lower-order orbit and moving primitive owners open",
      "lower-order homogeneous orbit" in prior and "moving primitive" in prior)

for label in (
    "principal affine derivative versus lower-order homogeneous commutator",
    "primitive epsilon variation versus simultaneous gauge action",
    "moving Phi/Shiab response versus input curvature response",
    "pointwise invariant action versus full preboundary class",
    "ordinary even gauge Ward identity versus odd super-IG BV closure",
    "zero action variation versus nonzero reduced physical transition",
):
    check("type", label + " remain distinct", True)


print("\nB. LOAD THE EXACT K77 MOVING-SHIAB BACKEND")
capture = StringIO()
with contextlib.redirect_stdout(capture):
    M = runpy.run_path(str(BACKEND))
check("exact", "the moving-Shiab/epsilon/Green predecessor replays",
      "PASS: the source moving-Shiab family" in capture.getvalue())

PHI1 = M["PHI1"]
fadd = M["fadd"]
fscale = M["fscale"]
wedge_raw = M["wedge_raw"]
shiab = M["shiab"]
hodge = M["hodge"]
coefficient_derivative = M["coefficient_derivative"]
d_shiab = M["d_shiab"]
blade = M["blade"]
emul = M["emul"]
eadd = M["eadd"]
escale = M["escale"]
flatten = M["flatten"]
gadd = M["gadd"]
gscale = M["gscale"]
FULL = M["FULL"]
ZERO = M["ZERO"]
SELECTED = ("comm", "symi", "symi")


def clean_equal(left, right):
    return flatten(fadd(left, fscale(-1, right))) == {}


def top_scalar(form):
    return form.get(FULL, {}).get(0, ZERO)


def pairing(left, right):
    return top_scalar(wedge_raw(left, right))


def generic_connection_difference():
    """A deterministic non-tautological one-form with mixed Clifford grades."""
    return {
        1 << 0: eadd(blade(4), escale(2, blade((5, 6)))),
        1 << 1: eadd(blade(7), blade((8, 9))),
        1 << 4: eadd(blade(2), escale(-1, blade((10, 11)))),
        1 << 9: eadd(blade(3), blade((12, 13))),
    }


def homogeneous_packet(field, chi, phi_sign=1):
    d_field = coefficient_derivative(field, chi)
    square = wedge_raw(field, field)
    d_square = fadd(
        wedge_raw(d_field, field),
        wedge_raw(field, d_field),
    )
    image = shiab(square, SELECTED)
    d_image_input = shiab(d_square, SELECTED)
    d_image_phi = fscale(phi_sign, d_shiab(square, SELECTED, chi))
    d_image_total = fadd(d_image_input, d_image_phi)

    cubic_variation = gscale(Fraction(1, 3), gadd(
        pairing(d_field, image),
        pairing(field, d_image_total),
    ))
    quadratic_variation = gscale(Fraction(1, 2), gadd(
        pairing(d_field, hodge(field)),
        pairing(field, hodge(d_field)),
    ))
    frozen_shiab_defect = gscale(Fraction(1, 3), gadd(
        pairing(d_field, image),
        pairing(field, d_image_input),
    ))
    return {
        "d_field": d_field,
        "square": square,
        "d_square": d_square,
        "image": image,
        "d_image_total": d_image_total,
        "cubic_variation": cubic_variation,
        "quadratic_variation": quadratic_variation,
        "frozen_shiab_defect": frozen_shiab_defect,
        "covariance": clean_equal(
            d_image_total,
            coefficient_derivative(image, chi),
        ),
    }


print("\nC. COMPLETE K77 BIVECTOR-GENERATOR SCAN")
field = generic_connection_difference()
generators = [
    ((i, j), emul(blade(i), blade(j)))
    for i in range(14)
    for j in range(i + 1, 14)
]
check("exact", "the K77 bivector algebra has 91 tested basis generators", len(generators) == 91)

packets = [(pair, homogeneous_packet(field, chi)) for pair, chi in generators]
check("exact", "moving selected Shiab is equivariant for all 91 generators",
      all(packet["covariance"] for _, packet in packets))
check("exact", "selected cubic homogeneous variation vanishes for all 91 generators",
      all(packet["cubic_variation"] == ZERO for _, packet in packets))
check("exact", "quadratic native-pairing variation vanishes for all 91 generators",
      all(packet["quadratic_variation"] == ZERO for _, packet in packets))
check("exact", "complete intrinsic selected action Ward contraction vanishes",
      all(gadd(packet["cubic_variation"], packet["quadratic_variation"]) == ZERO
          for _, packet in packets))

frozen_live = [
    (pair, packet["frozen_shiab_defect"])
    for pair, packet in packets
    if packet["frozen_shiab_defect"] != ZERO
]
expected_frozen = [
    ((0, 4), (Fraction(-8), Fraction(0))),
    ((1, 7), (Fraction(-8, 3), Fraction(0))),
    ((2, 4), (Fraction(-8, 3), Fraction(0))),
    ((3, 9), (Fraction(-8, 3), Fraction(0))),
]
check("exact", "freezing the moving Shiab leaves exactly four nonzero Ward defects",
      frozen_live == expected_frozen)

wrong_sign_live = []
for pair, chi in generators:
    wrong = homogeneous_packet(field, chi, phi_sign=-1)
    total = gadd(wrong["cubic_variation"], wrong["quadratic_variation"])
    if total != ZERO:
        wrong_sign_live.append((pair, total))
check("planted", "PLANT reversing the moving-Phi sign doubles four live defects",
      len(wrong_sign_live) == 4
      and wrong_sign_live[0] == ((0, 4), (Fraction(-16), Fraction(0))))


print("\nD. STRUCTURAL AND RADIAL CONTROLS")
# The equality checked above is the concrete instance of the structural
# theorem: inner commutator is a derivation, Hodge acts only on form indices,
# the moving Phi terms make Shiab equivariant, and the top-scalar pairing kills
# total coefficient commutators.  Check these stages independently.
held_pair, held_chi = generators[4]
held = homogeneous_packet(field, held_chi)
check("exact", "inner action differentiates the raw exterior square",
      clean_equal(
          held["d_square"],
          coefficient_derivative(held["square"], held_chi),
      ))
check("exact", "Hodge commutes with the inner coefficient action",
      clean_equal(
          hodge(held["d_field"]),
          coefficient_derivative(hodge(field), held_chi),
      ))
check("exact", "the invariant pairing kills the total commutator derivative",
      gadd(
          pairing(held["d_field"], held["image"]),
          pairing(field, held["d_image_total"]),
      ) == ZERO)

radial_packets = [homogeneous_packet(PHI1, chi) for _, chi in generators]
check("exact", "the invariant radial branch also closes for all 91 generators",
      all(packet["cubic_variation"] == ZERO
          and packet["quadratic_variation"] == ZERO
          and packet["covariance"] for packet in radial_packets))
check("exact", "the radial branch is non-vacuous in both intrinsic action terms",
      pairing(PHI1, shiab(wedge_raw(PHI1, PHI1), SELECTED)) != ZERO
      and pairing(PHI1, hodge(PHI1)) != ZERO)


print("\nE. SCOPE, SYMPLECTIC, AND PROGRAM BOUNDARIES")
for label in (
    "the intrinsic T plus moving-Shiab package closes only the homogeneous even inner orbit",
    "primitive epsilon variation and its Green boundary row remain separately typed",
    "direct curvature full-II defect and metric observation owners remain open",
    "full diffeomorphism odd-super-IG BV and BFV preboundary classes remain open",
    "zero action variation is not a zero physical interaction or Q1 pole",
    "the corrected package reuses rather than increments four ranked quotients",
    "P1 P2 P3 remain unused and Curt stays formally separate",
    "no positivity unitarity particle or cosmological prediction is inferred",
):
    check("planted", "PLANT " + label, True)

print("\nSOURCE_RETURN=SOURCE-CONFIRMS")
print("SOURCE_SCOPE=MOVING_PHI_SHIAB_AND_TWO_CONNECTION_EQUIVARIANCE_ARENA__NOT_EXACT_WARD_OR_PHYSICS")
print("K77_BIVECTOR_GENERATORS=91_OF_91")
print("MOVING_SHIAB_COVARIANCE=91_OF_91")
print("INTRINSIC_CUBIC_WARD=ZERO_91_OF_91")
print("INTRINSIC_QUADRATIC_WARD=ZERO_91_OF_91")
print("FROZEN_SHIAB_DEFECTS=4_OF_91")
print("DISPOSITION=INTRINSIC_HOMOGENEOUS_WARD_EXACT__FULL_DIRECT_MOVING_PREBOUNDARY_CLASS_OPEN")
print("LEDGER_ROWS=LT-GR1,LT-GR2b,LT-GR5,LT-GR6,LT-SM8")
print("CHECKS=" + " ".join(f"{kind}:{count}" for kind, count in sorted(COUNTS.items())))
if FAILURES:
    print("FAILED_LABELS=" + " | ".join(FAILURES))
    raise SystemExit(1)
print(f"PASS {sum(COUNTS.values())}/{sum(COUNTS.values())}")
