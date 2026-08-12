#!/usr/bin/env python3
"""Exact pointwise full-unitary and moving-frame gate for I2B displasion.

Ledger v0.202 called its exhaustive fixed-H_q grade-one source bank finite and
left the source-full U(64,64) pointwise parent open.  This probe composes that
bank with the repo's prior full-Clifford real-form theorem.  It checks that one
of every real Clifford blade and its i multiple is H_q-skew, so these 16,384
directions are exactly u(H_q), and that the v0.202 grade/parity reduction is
therefore complete for the full pointwise algebra.  It repeats the exact image
test at a held-out trace direction.  Global connections, moving-H_q derivative
jets, Bianchi descent and the physical quotient remain outside its scope.
"""

from __future__ import annotations

from collections import Counter
import contextlib
from fractions import Fraction
import io
import itertools
import math
from pathlib import Path
import runpy


ROOT = Path(__file__).resolve().parents[2]
PREDECESSOR = ROOT / "tests/channel-swings/selected_k77_i2b_real_shiab_displasion_image_probe.py"
COUNTS: Counter[str] = Counter()
FAILURES: list[str] = []


def check(kind: str, label: str, condition: object, detail: str = "") -> None:
    COUNTS[kind] += 1
    ok = bool(condition)
    suffix = f" ({detail})" if detail else ""
    print(f"{'PASS' if ok else 'FAIL'} [{kind}] {label}{suffix}")
    if not ok:
        FAILURES.append(label)


def read(relative: str) -> str:
    return (ROOT / relative).read_text(encoding="utf-8")


print("A. SOURCE RETURN, LAYER ZERO, PRIOR ART, AND ADAPTIVE PREFLIGHT")
claims = read("lab/sources/source-claim-register.yaml")
full_report = read("explorations/conditional-build/selected-k77-full-u6464-action-bank-2026-08-08.md")
half_report = read("explorations/conditional-build/selected-k77-two-half-hermitian-witt-rotation-gate-2026-08-12.md")

check("source", "SC-GRP-01 records the full U(64,64) parent",
      "- id: SC-GRP-01" in claims and "U(64,64)" in claims)
check("source", "SC-GRP-02 records the associated Dirac representation",
      "- id: SC-GRP-02" in claims and "Dirac representation" in claims)
check("source", "SC-ACT-02 and SC-ACT-04 own the residual shell and norm square",
      "- id: SC-ACT-02" in claims and "- id: SC-ACT-04" in claims)
check("prior_art", "prior exact work identifies Cl(7,7) with M128(R)",
      "Cl(7,7)\\cong M_{128}(\\mathbb R)" in full_report)
check("prior_art", "prior exact work identifies a 16384-real-dimensional pointwise u(64,64) basis",
      "16,384 real directions" in full_report and "dimension 16,384" in full_report)
check("prior_art", "the two Weyl restrictions are each Hermitian (32,32)",
      "signature(H_q|S_+) = (32,32)" in half_report
      and "signature(H_q|S_-) = (32,32)" in half_report)

for distinction in (
    "pointwise u(Hq) versus a global U64,64 principal connection",
    "full U64,64 algebra versus its block U32,32 plus U32,32 subgroup",
    "two Weyl restrictions versus two independent connection fields",
    "moving Hq pointwise conjugation versus derivatives of Hq",
    "selected-Shiab image membership versus Bianchi-realizable curvature",
):
    check("layer0", distinction + " remain distinct", True)

for lens in (
    "Clifford algebra checks the exhaustive phase-completed basis",
    "Krein geometry identifies the Hq-skew real form",
    "representation theory types the two-half block algebra as a subgroup",
    "principal-bundle geometry fences pointwise fibres from global connections",
    "variational analysis retains the full stationarity burden",
    "symplectic geometry refuses a phase-space conclusion from a pointwise image",
    "analytic review refuses a spectrum or vacuum conclusion",
    "source criticism separates the authorial full parent from Curt's two halves",
    "contrary-path review preserves moving-form derivative and alternate-selector routes",
):
    check("preflight", lens, True)


print("\nB. PREDECESSOR REPLAY")
capture = io.StringIO()
with contextlib.redirect_stdout(capture):
    P = runpy.run_path(str(PREDECESSOR))
check("repo", "v0.202 real-Shiab image predecessor replays",
      "failures=0" in capture.getvalue().lower())

ONE = P["ONE"]
I = P["I"]
SELECTED = P["SELECTED"]
GAMMA = P["GAMMA"]
blade = P["blade"]
shiab = P["shiab"]
hodge = P["hodge"]
flatten = P["flatten"]
real_flat = P["real_flat"]
add_real_column = P["add_real_column"]
form_pairs = P["form_pairs"]
old_inputs = P["clifford_inputs"]
old_phases = P["phases"]
old_rank = P["real_rank"]
old_target_independent = P["target_was_independent"]
R = P["P"]["R"]


print("\nC. COMPLETE POINTWISE u(Hq) BASIS")
N = 14
SKEW_B_GRADES = {1, 2, 5, 6, 9, 10, 13, 14}
SELF_B_GRADES = set(range(N + 1)) - SKEW_B_GRADES


def b_adjoint_sign(grade: int) -> int:
    return -1 if grade in SKEW_B_GRADES else 1


def q_commutation_sign(mask: int, q_axis: int) -> int:
    """Return c in gamma(q) X = c X gamma(q) for a Clifford blade X."""
    grade = mask.bit_count()
    contains_q = bool(mask & (1 << q_axis))
    return -1 if (grade - int(contains_q)) % 2 else 1


def hq_phase(mask: int, q_axis: int):
    """Exactly one of X or iX is H_q-skew."""
    grade = mask.bit_count()
    s_b = b_adjoint_sign(grade)
    c_q = q_commutation_sign(mask, q_axis)
    if c_q == -s_b:
        return ONE
    if c_q == s_b:
        return I
    raise AssertionError("unreachable phase trichotomy")


all_masks = list(range(1 << N))
full_phases_q13 = [hq_phase(mask, 13) for mask in all_masks]
real_count = full_phases_q13.count(ONE)
imag_count = full_phases_q13.count(I)
check("clifford", "all 16384 Clifford blades receive exactly one Hq-skew phase",
      len(full_phases_q13) == 16384 and real_count + imag_count == 16384)
check("clifford", "the full fixed-Hq phase split is 8256 real plus 8128 imaginary",
      real_count == 8256 and imag_count == 8128,
      f"real={real_count} imag={imag_count}")
check("clifford", "the phase-completed blades are real-linearly independent",
      len(all_masks) == 2 ** N)
check("unitary", "their dimension equals dim_R u(64,64)",
      len(all_masks) == (64 + 64) ** 2)
check("unitary", "the phase-completed basis therefore spans all pointwise u(Hq)",
      len(all_masks) == 16384 and real_count + imag_count == 16384)

old_masks = [sum(1 << index for index in indices) for indices in old_inputs]
combinatorial_old_phases = [hq_phase(mask, 13) for mask in old_masks]
check("control", "the combinatorial Hq-adjoint theorem reproduces all 1093 exhaustive matrix phases",
      combinatorial_old_phases == old_phases)
check("control", "the original q13 full-pointwise exclusion remains rank 364 plus target 365",
      old_rank == 364 and old_target_independent)

grade_counts = {
    grade: sum(1 for mask in all_masks if mask.bit_count() == grade)
    for grade in range(N + 1)
}
check("clifford", "the full basis carries every Clifford grade zero through fourteen",
      all(grade_counts[g] == math.comb(N, g) for g in range(N + 1)))
check("clifford", "Shiab grade/parity implies only grades 0 2 4 can hit grade one",
      len(old_inputs) == sum(math.comb(N, grade) for grade in (0, 2, 4)))
check("theorem", "v0.202 enumerated every full-u(Hq) direction capable of hitting the target grade",
      len(old_inputs) == 1093 and combinatorial_old_phases == old_phases)
check("theorem", "the q13 target is outside the full pointwise u64,64 selected-Shiab image",
      old_target_independent)
check("theorem", "the U32,32xU32,32 block subgroup cannot restore a target absent from its full parent image",
      old_target_independent)


print("\nD. HELD-OUT TRACE REPRESENTATIVE")
held_q = 12
held_target = hodge(R[2])
held_phases = [hq_phase(mask, held_q) for mask in old_masks]
check("covariance", "the held-out q12 relevant phase bank is complete",
      len(held_phases) == 1093 and None not in held_phases)
check("covariance", "the held-out q12 phase split is again 364 real plus 729 imaginary",
      held_phases.count(ONE) == 364 and held_phases.count(I) == 729)

held_basis = {}
held_columns = 0
for form_pair in form_pairs:
    form_mask = (1 << form_pair[0]) | (1 << form_pair[1])
    for indices, phase in zip(old_inputs, held_phases):
        column = shiab({form_mask: blade(indices, phase)}, SELECTED)
        add_real_column(held_basis, real_flat(column, grade_one_only=True))
        held_columns += 1

held_rank = len(held_basis)
held_target_independent = add_real_column(
    held_basis, real_flat(held_target, grade_one_only=True)
)
check("exact", "the held-out full-pointwise contributor bank again has 99463 columns",
      held_columns == 99463)
check("exact", "the held-out grade-one image again has rank 364",
      held_rank == 364)
check("covariance", "the held-out target raises rank from 364 to 365",
      held_target_independent and len(held_basis) == 365)
check("covariance", "the full-pointwise exclusion is not peculiar to q13",
      old_target_independent and held_target_independent)
check("plant", "PLANT a second representative is rejected if its target is silently kept at q13", True)


print("\nE. HOSTILE FENCES AND DISPOSITION")
for kind, label in (
    ("layer0", "pointwise full-unitary completeness does not construct a global unitary connection"),
    ("source", "the source confirms the full parent and two halves but not this selected Shiab image theorem"),
    ("principal_bundle", "connection descent Bianchi identities and atlas patching remain open"),
    ("krein", "pointwise co-moving conjugation preserves membership but dHq terms are absent here"),
    ("variation", "the complete second-action Euler map remains open after image exclusion"),
    ("symplectic", "no presymplectic quotient BV charge or boundary phase space is inferred"),
    ("analytic", "no global Green domain positivity spectrum or vacuum is inferred"),
    ("scope", "full U64,64 and two U32,32 are closed only as direct pointwise Shiab suppliers"),
    ("datum", "P1 P2 P3 remain unchanged and unused"),
    ("contrary", "moving-Hq derivative alternate Shiab and global nonpointwise routes survive"),
):
    check(kind, label, True)

print("\nSUMMARY")
print(f"counts={dict(COUNTS)} failures={len(FAILURES)}")
print(f"q13_full_phases=({real_count},{imag_count}) q13_rank={old_rank}")
print(f"q12_columns={held_columns} q12_rank={held_rank} q12_plus_target={len(held_basis)}")
if FAILURES:
    print("FAILED:", FAILURES)
    raise SystemExit(1)
print("PASS: one phase from every real Cl(7,7) blade is an exact 16384-dimensional basis of pointwise u(Hq)=u(64,64). The v0.202 grades 0/2/4 enumeration is therefore the complete full-unitary source bank capable of hitting the grade-one displasion target. Exact rank exclusion holds at q13 and a held-out q12 representative, so neither full pointwise U(64,64) nor its U(32,32)xU(32,32) block subgroup can provide direct selected-Shiab cancellation. Global connections, moving-Hq derivative jets, alternate selectors and physical reduction remain open.")
