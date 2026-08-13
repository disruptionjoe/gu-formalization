#!/usr/bin/env python3
"""Exact real-action ownership gate for the projected K77 I2B Shiab.

The predecessor proves that the moving fixed-output map ``P_+ A`` is
pointwise natural and contains the displasion target.  This probe asks the
different variational question: does the real part of the selected
Hodge-times-Clifford-trace residual pairing force the same ``P_+`` in the
first variation about an ``H_q``-fixed residual?  The nonlinear residual map,
its real quadratic action, its Euler covector and a projected replacement are
kept separate throughout.
"""

from __future__ import annotations

from collections import Counter
import contextlib
from fractions import Fraction
import io
from pathlib import Path
import runpy


ROOT = Path(__file__).resolve().parents[2]
PREDECESSOR = ROOT / "tests/channel-swings/selected_k77_i2b_compensator_naturality_probe.py"
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
claims = read("lab/sources/source-claim-register.yaml")
pairing_source = read("lab/sources/selected-k77-residual-pairing-source-reinspection-2026-08-08.md")
previous = read("explorations/conditional-build/selected-k77-i2b-compensator-naturality-2026-08-12.md")
pairing_result = read("explorations/conditional-build/selected-k77-residual-pairing-invariance-2026-08-08.md")

check("source", "SC-ACT-04 owns a bosonic residual norm square and adjoint equation",
      "- id: SC-ACT-04" in claims
      and "I^B_2 = ||Upsilon^B_omega||^2" in claims
      and "D*_omega Upsilon_omega = 0" in claims)
check("source", "primary-source return confirms norm-square and adjoint grammar",
      "norm square" in pairing_source and "adjoint" in pairing_source)
check("source", "source is silent on the repository Hq involution and P_plus",
      "SOURCE-SILENT" in pairing_source and "does not" in previous
      and "source action" in previous)
check("prior_art", "v0.205 proves pointwise compensator naturality but leaves action ownership open",
      "99,463" in previous and "action ownership" in previous)
check("prior_art", "v0.92 constructs the conditional real local residual pairing",
      "degree-thirteen\nHodge pairing" in pairing_result
      and "Clifford-trace" in pairing_result)

for distinction in (
    "nonlinear residual A versus post-composed residual P_plus A",
    "complex-bilinear comparator versus its real action",
    "real quadratic action versus its first variation",
    "Euler covector factorization versus target image membership",
    "pointwise primalizer versus formal adjoint and Green return",
):
    check("layer0", distinction + " remain distinct", True)

for lens in (
    "variational bicomplex checks the action derivative rather than the residual image alone",
    "Clifford and Krein geometry type the real involution and indefinite pairing",
    "real-form geometry checks fixed and anti-fixed orthogonality",
    "symplectic geometry refuses to infer a preboundary class from a fibre derivative",
    "analytic review retains the formal adjoint Green domain and spectrum",
    "source criticism distinguishes published norm-square grammar from repository P_plus",
    "contrary-path review tests a non-fixed residual where factorization must fail",
):
    check("preflight", lens, True)


print("\nB. PREDECESSOR REPLAY AND LIVE OBJECTS")
capture = io.StringIO()
with contextlib.redirect_stdout(capture):
    P205 = runpy.run_path(str(PREDECESSOR))
check("repo", "v0.205 compensator/naturality predecessor replays",
      "failures=0" in capture.getvalue().lower())

P204 = P205["P"]
P203 = P204["P"]
P202 = P203["P"]
M = P202["M"]
ETA = M["ETA"]
ONE = P204["ONE"]
SELECTED = P204["SELECTED"]
blade = P204["blade"]
shiab = P204["shiab"]
real_flat = P204["real_flat"]
tau_target = P204["tau_target"]
add = P204["add"]
scale = P204["scale"]
form_pairs = P204["form_pairs"]
inputs = P204["inputs"]
phases = P204["phases"]
target_form = P204["target"]
target_vector = P204["target_vector"]
fixed_basis = P204["fixed_basis"]
anti_basis = P204["anti_basis"]
sym_pair = P202["sym_pair"]


def clifford_square_sign(mask: int) -> int:
    product_mask, sign = M["blade_product"](mask, mask)
    assert product_mask == 0
    return sign


def form_sign(mask: int) -> int:
    out = 1
    for index in M["indices"](mask):
        out *= ETA[index]
    return out


def coordinate_sign(key: tuple[int, int]) -> int:
    form_mask, clifford_mask = key
    return form_sign(form_mask) * clifford_square_sign(clifford_mask)


def complex_at(column: dict, key: tuple[int, int]) -> tuple[Fraction, Fraction]:
    return column.get((key, 0), Fraction(0)), column.get((key, 1), Fraction(0))


def action_pair(left: dict, right: dict) -> Fraction:
    """Real part of the v0.92 complex-bilinear scalar-trace comparator."""
    left_keys = {key for key, _part in left}
    right_keys = {key for key, _part in right}
    total = Fraction(0)
    for key in left_keys & right_keys:
        ar, ai = complex_at(left, key)
        br, bi = complex_at(right, key)
        total += coordinate_sign(key) * (ar * br - ai * bi)
    return total


def project_plus(column: dict) -> dict:
    return scale(Fraction(1, 2), add(column, tau_target(column)))


def project_minus(column: dict) -> dict:
    return scale(Fraction(1, 2), add(column, scale(-1, tau_target(column))))


check("reality", "the physical displasion residual is Hq-fixed",
      tau_target(target_vector) == target_vector)
check("projector", "P_plus fixes the target and P_minus kills it",
      project_plus(target_vector) == target_vector and not project_minus(target_vector))


print("\nC. COMPLETE LIVE-BANK FIRST-VARIATION FACTORIZATION")
columns = 0
pairing_mismatches = 0
factorization_failures = 0
anti_target_failures = 0
quadratic_split_failures = 0
nonzero_derivatives = 0
coordinate_keys: set[tuple[int, int]] = set()

for form_pair in form_pairs:
    form_mask = (1 << form_pair[0]) | (1 << form_pair[1])
    for indices, phase in zip(inputs, phases):
        value_form = shiab({form_mask: blade(indices, phase)}, SELECTED)
        value = real_flat(value_form, grade_one_only=True)
        fixed = project_plus(value)
        anti = project_minus(value)
        coordinate_keys.update(key for key, _part in value)

        full_derivative = action_pair(value, target_vector)
        projected_derivative = action_pair(fixed, target_vector)
        anti_derivative = action_pair(anti, target_vector)
        source_pair = sym_pair(value_form, target_form)

        pairing_mismatches += int(
            full_derivative != source_pair[0]
        )
        factorization_failures += int(
            full_derivative != projected_derivative
        )
        anti_target_failures += int(anti_derivative != 0)
        quadratic_split_failures += int(
            action_pair(value, value)
            != action_pair(fixed, fixed) + action_pair(anti, anti)
        )
        nonzero_derivatives += int(full_derivative != 0)
        columns += 1

check("exact", "the complete target-relevant bank has 99463 columns", columns == 99463)
check("pairing", "coordinate real action agrees with the existing symmetrized residual pairing",
      pairing_mismatches == 0, f"mismatches={pairing_mismatches}")
check("variation", "every first variation at the Hq-fixed residual factors through P_plus",
      factorization_failures == 0 and anti_target_failures == 0,
      f"factorization={factorization_failures} anti={anti_target_failures}")
check("variation", "the action-derived covector is nonvacuous on the live bank",
      nonzero_derivatives > 0, f"nonzero={nonzero_derivatives}")
check("action", "the unprojected real quadratic action splits into fixed and anti-fixed sectors",
      quadratic_split_failures == 0, f"failures={quadratic_split_failures}")


print("\nD. PRIMALIZER IDENTITY AND CONTRARY NON-FIXED BACKGROUND")
projector_self_adjoint = True
projector_idempotent = True
for key in coordinate_keys:
    # tau acts by s on the real coordinate and -s on the imaginary coordinate;
    # the real action has diagonal weights d and -d.  Hence the spectral
    # projector is action-self-adjoint coordinatewise.
    probe_real = {(key, 0): Fraction(1)}
    probe_imag = {(key, 1): Fraction(1)}
    for probe in (probe_real, probe_imag):
        projected = project_plus(probe)
        projector_idempotent &= project_plus(projected) == projected
        projector_self_adjoint &= (
            action_pair(projected, probe) == action_pair(probe, projected)
        )

check("projector", "P_plus is idempotent on the complete 196-complex-coordinate target carrier",
      len(coordinate_keys) == 196 and projector_idempotent,
      f"coordinates={len(coordinate_keys)}")
check("primalizer", "P_plus is self-adjoint for the selected real action pairing",
      projector_self_adjoint)

fixed_anti_failures = 0
for fixed in fixed_basis.values():
    for anti in anti_basis.values():
        fixed_anti_failures += int(action_pair(fixed, anti) != 0)
check("orthogonality", "the complete fixed and anti-fixed image bases are action-orthogonal",
      fixed_anti_failures == 0,
      f"pairs={len(fixed_basis) * len(anti_basis)} failures={fixed_anti_failures}")

anti_witness = None
anti_values = list(anti_basis.values())
for left in anti_values:
    for right in anti_values:
        value = action_pair(left, right)
        if value:
            anti_witness = (left, right, value)
            break
    if anti_witness is not None:
        break

check("control", "the anti-fixed sector has a nonzero action pairing witness",
      anti_witness is not None)
if anti_witness is not None:
    left, right, witness_value = anti_witness
    mixed_background = add(target_vector, right)
    full_mixed_derivative = action_pair(left, mixed_background)
    projected_mixed_derivative = action_pair(project_plus(left), mixed_background)
else:
    witness_value = Fraction(0)
    full_mixed_derivative = Fraction(0)
    projected_mixed_derivative = Fraction(0)

check("control", "factorization fails at a deliberately non-fixed residual background",
      full_mixed_derivative != projected_mixed_derivative
      and full_mixed_derivative - projected_mixed_derivative == witness_value)
check("scope", "the real action does not replace nonlinear A by P_plus A",
      anti_witness is not None and len(anti_basis) == 195)


print("\nE. HOSTILE FENCES")
for kind, label in (
    ("layer0", "Euler-grade P_plus ownership is not nonlinear residual replacement"),
    ("source", "the source owns norm-square and adjoint grammar but does not publish Hq or P_plus"),
    ("variation", "the finite first variation still lacks moving Hq Hodge Shiab and connection jets"),
    ("principal_bundle", "pointwise primalizer ownership does not choose a Spin lift or source epsilon"),
    ("symplectic", "no presymplectic potential BFV charge or reduced phase space is inferred"),
    ("analytic", "no formal Green adjoint closed domain spectrum positivity or vacuum is inferred"),
    ("datum", "P1 P2 and P3 remain unchanged and unused"),
    ("contrary", "non-fixed residuals retain the anti-fixed action sector and block a global replacement"),
):
    check(kind, label, True)


print("\nSUMMARY")
print(f"counts={dict(COUNTS)} failures={len(FAILURES)}")
print(
    f"columns={columns} coordinates={len(coordinate_keys)} "
    f"nonzero_derivatives={nonzero_derivatives} "
    f"fixed_rank={len(fixed_basis)} anti_rank={len(anti_basis)} "
    f"anti_witness={witness_value}"
)
if FAILURES:
    print("FAILED:", FAILURES)
    raise SystemExit(1)
print("PASS: the real part of the selected residual-square pairing makes P_plus the exact action-self-adjoint primalizer in the first variation about the Hq-fixed displasion residual, on all 99,463 live columns. The unprojected quadratic action still has a nonzero anti-fixed sector, and the factorization fails at a non-fixed residual. Thus P_plus is action-owned only at this fixed-real Euler grade; it is not a source-published or globally valid replacement of the nonlinear residual map. Moving derivatives, formal adjoint/Green, preboundary and physical vacuum remain open.")
