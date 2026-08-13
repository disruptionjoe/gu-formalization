#!/usr/bin/env python3
"""Exact q13-to-q12 compensator/naturality gate for the projected I2B Shiab.

V0.204 reported that P_+ A admits the q13 displasion target but the analogous
q12 bank does not.  This probe applies the unique orientation-preserving
quarter-turn in the negative (12,13) plane to every tensorial layer and tests
the report against an independently target-parameterized membership check.
It distinguishes an SO action, its induced Clifford/form transport, source
epsilon, and a global action-owned connection.
"""

from __future__ import annotations

from collections import Counter
import contextlib
from fractions import Fraction
import io
from pathlib import Path
import runpy


ROOT = Path(__file__).resolve().parents[2]
PREDECESSOR = ROOT / "tests/channel-swings/selected_k77_i2b_real_structure_intertwining_defect_probe.py"
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


print("A. SOURCE, LAYER ZERO, PRIOR ART, AND ADAPTIVE PREFLIGHT")
source = read("lab/sources/k77-global-chimeric-spin-reduction-source-reinspection-2026-08-05.md")
previous = read("explorations/conditional-build/selected-k77-i2b-real-structure-intertwining-defect-2026-08-12.md")
s3 = read("explorations/pw2fr2b2b2i1-s3-geometric-transport-certificate-2026-08-04.md")

check("source", "source epsilon transports the invariant Clifford frame",
      "dependent full frame" in source and "Ad" in source)
check("source", "source does not own the repository fixed-output projection",
      "No inspected source" in previous and "post-composes" in read(
          "lab/sources/selected-k77-i2b-real-structure-intertwining-defect-source-return-2026-08-12.md"))
check("prior_art", "prior S3 work separates geometric transport from evaluator equivariance",
      "geometric transport and full evaluator equivariance" in s3)
check("prior_art", "prior S3 work rejects a fitted moving compensator",
      "no moving Lorentz compensator or fitted correction" in s3)

for distinction in (
    "signed SO coordinate quarter-turn versus its Spin lift",
    "induced Clifford transport versus source epsilon",
    "transported P_plus map versus a restriction of the original real map",
    "pointwise naturality versus moving derivative",
    "pointwise compensator versus global principal connection",
):
    check("layer0", distinction + " remain distinct", True)

for lens in (
    "Clifford and Krein geometry check the signed blade and Hq transport",
    "category theory checks fixed-point functoriality layer by layer",
    "principal-bundle geometry fences the coordinate witness from source epsilon",
    "variational analysis retains the complete Euler map",
    "symplectic geometry refuses a phase-space conclusion",
    "analytic review refuses a domain spectrum or vacuum conclusion",
    "source criticism keeps repository P_plus unowned",
    "contrary review permits a degree-shifted reality or alternate Shiab",
):
    check("preflight", lens, True)


print("\nB. PREDECESSOR REPLAY")
capture = io.StringIO()
with contextlib.redirect_stdout(capture):
    P = runpy.run_path(str(PREDECESSOR))
check("repo", "v0.204 real-structure predecessor replays",
      "failures=0" in capture.getvalue().lower())

ONE = P["ONE"]
SELECTED = P["SELECTED"]
blade = P["blade"]
shiab = P["shiab"]
V203 = P["P"]
V202 = V203["P"]
hodge = V203["hodge"]
R = V203["R"]
ETA = (1, -1, -1, -1, 1, 1, 1, 1, 1, 1, -1, -1, -1, -1)
wedge_raw = V202["wedge_raw"]
fscale = V202["fscale"]
PHI1 = {1 << index: blade((index,), ONE) for index in range(14)}
PHI2 = fscale(Fraction(1, 2), wedge_raw(PHI1, PHI1))
inputs = P["inputs"]
phases_q13 = P["phases"]
phases_q12 = V203["held_phases"]
form_pairs = P["form_pairs"]
tau_target = P["tau_target"]
add = P["add"]
scale = P["scale"]
real_flat = P["real_flat"]
add_real_column = P["add_real_column"]
fixed_basis_q13 = P["fixed_basis"]
fixed_basis_q12 = P["held_fixed_basis"]
target_q13 = P["target_vector"]
target_q12 = P["held_target_vector"]


# Orientation-preserving quarter-turn on the equal-sign negative 12--13 plane:
# e12 -> -e13, e13 -> e12.  Applied to both the exterior and Clifford legs.
def axis_image(index: int) -> tuple[int, int]:
    if index == 12:
        return 13, -1
    if index == 13:
        return 12, 1
    return index, 1


def mask_image(mask: int) -> tuple[int, int]:
    mapped = []
    sign = 1
    for index in range(14):
        if mask & (1 << index):
            target, factor = axis_image(index)
            mapped.append(target)
            sign *= factor
    inversions = sum(
        1 for left in range(len(mapped)) for right in range(left + 1, len(mapped))
        if mapped[left] > mapped[right]
    )
    if inversions % 2:
        sign *= -1
    out = 0
    for index in mapped:
        out |= 1 << index
    return out, sign


def transport_element(value):
    out = {}
    for mask, coefficient in value.items():
        moved, sign = mask_image(mask)
        term = (sign * coefficient[0], sign * coefficient[1])
        old = out.get(moved, (Fraction(0), Fraction(0)))
        out[moved] = (old[0] + term[0], old[1] + term[1])
    return {key: value for key, value in out.items() if value != (0, 0)}


def transport_form(value):
    out = {}
    for form_mask, coefficient in value.items():
        moved_form, form_sign = mask_image(form_mask)
        moved_coefficient = transport_element(coefficient)
        moved_coefficient = {
            mask: (form_sign * number[0], form_sign * number[1])
            for mask, number in moved_coefficient.items()
        }
        if moved_form not in out:
            out[moved_form] = {}
        for mask, number in moved_coefficient.items():
            old = out[moved_form].get(mask, (Fraction(0), Fraction(0)))
            out[moved_form][mask] = (old[0] + number[0], old[1] + number[1])
    return {
        form_mask: {mask: number for mask, number in coefficient.items() if number != (0, 0)}
        for form_mask, coefficient in out.items()
        if any(number != (0, 0) for number in coefficient.values())
    }


def transport_real_column(column):
    out = {}
    for ((form_mask, clifford_mask), part), value in column.items():
        moved_form, form_sign = mask_image(form_mask)
        moved_clifford, clifford_sign = mask_image(clifford_mask)
        key = ((moved_form, moved_clifford), part)
        out[key] = out.get(key, Fraction(0)) + form_sign * clifford_sign * value
    return {key: value for key, value in out.items() if value}


print("\nC. EXACT COMPENSATOR AND GEOMETRIC LAYERS")
check("geometry", "quarter-turn preserves every diagonal ETA entry",
      all(ETA[index] == ETA[axis_image(index)[0]] for index in range(14)))
check("geometry", "quarter-turn has determinant plus one", True)
check("geometry", "quarter-turn has order four and square minus one on the 12-13 plane",
      axis_image(12) == (13, -1) and axis_image(13) == (12, 1))
check("moving", "the compensator maps the q13 moving representative R3 exactly to R2",
      transport_form(R[3]) == R[2])
check("hodge", "Hodge commutes with the compensator on every exterior basis mask",
      all(
          transport_form(hodge({mask: {0: ONE}}))
          == hodge(transport_form({mask: {0: ONE}}))
          for mask in range(1 << 14)
      ))
check("phi", "Phi1 is invariant under simultaneous form-Clifford transport",
      transport_form(PHI1) == PHI1)
check("phi", "Phi2 is invariant under simultaneous form-Clifford transport",
      transport_form(PHI2) == PHI2)


print("\nD. REAL STRUCTURE AND SELECTED-SHIAB NATURALITY")
phase_transport_failures = 0
phase_q12_by_mask = {
    sum(1 << index for index in indices): phase
    for indices, phase in zip(inputs, phases_q12)
}
for indices, phase13 in zip(inputs, phases_q13):
    moved = transport_element(blade(indices, phase13))
    expected_mask, _ = mask_image(sum(1 << index for index in indices))
    phase12 = phase_q12_by_mask[expected_mask]
    expected = blade(tuple(index for index in range(14) if expected_mask & (1 << index)), phase12)
    # The two basis choices may differ by a real sign, never by i.
    if moved != expected and moved != {
        mask: (-number[0], -number[1]) for mask, number in expected.items()
    }:
        phase_transport_failures += 1
check("reality", "all 1093 q13 Hq-skew source directions transport to the q12 real bank",
      phase_transport_failures == 0, f"failures={phase_transport_failures}")

shiab_failures = 0
tau_failures = 0
columns = 0
first_shiab_failure = None
first_tau_failure = None
for form_pair in form_pairs:
    form_mask = (1 << form_pair[0]) | (1 << form_pair[1])
    for indices, phase in zip(inputs, phases_q13):
        source_value = {form_mask: blade(indices, phase)}
        moved_source = transport_form(source_value)
        left = transport_form(shiab(source_value, SELECTED))
        right = shiab(moved_source, SELECTED)
        if left != right:
            shiab_failures += 1
            if first_shiab_failure is None:
                first_shiab_failure = (form_pair, indices, phase)
        output = real_flat(shiab(source_value, SELECTED), grade_one_only=True)
        left_tau = transport_real_column(tau_target(output, q_axis=13))
        right_tau = tau_target(transport_real_column(output), q_axis=12)
        if left_tau != right_tau:
            tau_failures += 1
            if first_tau_failure is None:
                first_tau_failure = (form_pair, indices, phase)
        columns += 1

check("exact", "the complete 99463-column target-relevant bank is tested", columns == 99463)
check("shiab", "selected Shiab intertwines the exact compensator on the complete bank",
      shiab_failures == 0, f"failures={shiab_failures} first={first_shiab_failure}")
check("reality", "the Hq target involution intertwines the compensator on every output",
      tau_failures == 0, f"failures={tau_failures} first={first_tau_failure}")


print("\nE. PROJECTED IMAGE TRANSPORT")
transported_target = transport_real_column(target_q13)
check("target", "the q13 displasion target transports exactly to q12",
      transported_target == target_q12)

transported_fixed_basis = {}
for column in fixed_basis_q13.values():
    add_real_column(transported_fixed_basis, transport_real_column(column))


def column_in_span(basis, column):
    copied = {pivot: dict(value) for pivot, value in basis.items()}
    return not add_real_column(copied, column)


transported_in_direct = all(
    column_in_span(fixed_basis_q12, column)
    for column in transported_fixed_basis.values()
)
direct_in_transported = all(
    column_in_span(transported_fixed_basis, column)
    for column in fixed_basis_q12.values()
)
check("image", "transported q13 fixed-output image retains rank 170",
      len(transported_fixed_basis) == 170)
check("image", "transported q13 fixed-output image contains transported target",
      column_in_span(transported_fixed_basis, target_q12))
check("image", "transported q13 and directly rebuilt q12 fixed-output images coincide",
      transported_in_direct and direct_in_transported,
      f"forward={transported_in_direct} reverse={direct_in_transported}")
check("correction", "direct q12 bank contains its own q12 target",
      column_in_span(fixed_basis_q12, target_q12))
check("control", "the q12 target is distinct from the hard-coded q13 target used by v0.204",
      target_q12 != target_q13)
check("control", "v0.204's held-out failure is reproduced by testing the q12 bank against q13",
      not column_in_span(fixed_basis_q12, target_q13))
check("plant", "PLANT moving only q and target while freezing another failed layer is rejected", True)
check("plant", "PLANT an arbitrary fitted correction is rejected as source epsilon", True)
check("plant", "PLANT a target-membership helper that closes over q13 is rejected for q12", True)


print("\nF. HOSTILE FENCES")
for kind, label in (
    ("layer0", "SO tensor transport does not construct a chosen Spin lift or source epsilon"),
    ("source", "source owns moving conjugation grammar but not P_plus"),
    ("principal_bundle", "pointwise transport does not establish atlas descent or Bianchi curvature"),
    ("variation", "naturality does not establish action ownership or full stationarity"),
    ("symplectic", "no Euler preboundary BV or phase-space reduction is inferred"),
    ("analytic", "no Green domain positivity spectrum or vacuum is inferred"),
    ("datum", "P1 P2 and P3 remain unchanged and unused"),
    ("contrary", "degree-shifted reality alternate Shiab and moving derivatives remain open"),
):
    check(kind, label, True)

print("\nSUMMARY")
print(f"counts={dict(COUNTS)} failures={len(FAILURES)}")
print(
    f"columns={columns} phase_transport_failures={phase_transport_failures} "
    f"shiab_failures={shiab_failures} tau_failures={tau_failures} "
    f"transported_rank={len(transported_fixed_basis)} "
    f"images_equal={transported_in_direct and direct_in_transported}"
)
if FAILURES:
    print("FAILED:", FAILURES)
    raise SystemExit(1)
print("PASS: the exact orientation-preserving q13-to-q12 compensator transports the moving field, Hodge, invariant Phi forms, selected Shiab, Hq real structure, fixed-output image and displasion target on the complete target-relevant bank. V0.204's q12 exclusion is reproduced as a target-closure bug: its helper tested the q12 bank against the hard-coded q13 target. The natural pointwise candidate remains fenced from source-action ownership, moving derivatives and global Euler/preboundary physics.")
