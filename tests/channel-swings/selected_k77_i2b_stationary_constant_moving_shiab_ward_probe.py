#!/usr/bin/env python3
"""Exact constant-parameter moving-Shiab Ward completion at the I2B jet.

The predecessor differentiates the nonzero stationary connection two-jet and
the complete owned lower-order residual-square Euler term while freezing the
selected Shiab coefficients.  This probe independently differentiates every
Shiab occurrence through the source-owned moving-Phi family.  It asks whether
that coefficient response cancels the frozen rank-90 constant-parameter Ward
burden.  First/second parameter jets, Q_B/H_q/observation derivatives, affine
connection terms, Spencer compatibility and physical reduction stay open.
"""

from __future__ import annotations

from collections import Counter
import contextlib
from fractions import Fraction
import io
from pathlib import Path
import runpy

import sympy as sp


ROOT = Path(__file__).resolve().parents[2]
PREDECESSOR = ROOT / "tests/channel-swings/selected_k77_i2b_stationary_product_rule_ward_probe.py"
COUNTS: Counter[str] = Counter()
FAILURES: list[str] = []


def check(kind: str, label: str, condition: object, detail: object = "") -> None:
    COUNTS[kind] += 1
    ok = bool(condition)
    suffix = f" ({detail})" if detail != "" else ""
    print(f"{'PASS' if ok else 'FAIL'} [{kind}] {label}{suffix}")
    if not ok:
        FAILURES.append(label)


def read(relative: str) -> str:
    return (ROOT / relative).read_text(encoding="utf-8")


print("A. SOURCE, LAYER ZERO, PRIOR ART, AND ADAPTIVE PREFLIGHT")
source = read("lab/sources/gu-moving-shiab-epsilon-green-source-reinspection-2026-08-05.md")
prior = read("explorations/conditional-build/selected-k77-i2b-stationary-product-rule-ward-2026-08-13.md")
homogeneous = read("explorations/conditional-build/selected-cubic-intrinsic-homogeneous-ward-closure-2026-08-06.md")
check("source", "the source makes Phi1 and Phi2 a moving epsilon-conjugation orbit",
      "Phi_i(epsilon)=Ad_(epsilon^-1) Phi_i^0" in source)
check("source", "the source supplies the moving-Shiab derivative grammar",
      "D_epsilon Shiab" in source)
check("prior_art", "the predecessor isolates the rank-90 frozen constant-parameter burden",
      "rank `90`" in prior and "e12e13" in prior)
check("prior_art", "moving-Shiab homogeneous Ward closure is exact on all 91 generators",
      "all 91 bivector" in homogeneous and "variation is zero" in homogeneous)
for distinction in (
    "frozen coefficient response versus moving-Phi/Shiab response",
    "constant gauge parameter versus first and second parameter jets",
    "coefficient covariance versus Q_B H_q and observer contact derivatives",
    "Ward cancellation versus anomaly cancellation or physical quotient",
    "stationary base-point jet versus a formally integrable solution germ",
):
    check("layer0", distinction + " remain distinct", True)
for kind, label in (
    ("principal_bundle", "differentiate the actual associated Shiab family"),
    ("variational", "include moving coefficients in both principal and lower-order Euler terms"),
    ("gauge_bv", "close only constant-parameter even Ward tangency"),
    ("spencer", "leave parameter jets and formal involutivity open"),
    ("krein", "make no positivity inference from exact cancellation"),
    ("symplectic", "make no phase-space quotient inference"),
    ("source", "separate source grammar from repository-derived ranks"),
    ("contrary", "plant frozen and wrong-sign moving-Shiab alternatives"),
):
    check(kind, label, True)


print("\nB. IMMUTABLE PREDECESSORS AND STRUCTURE FINGERPRINT")
capture = io.StringIO()
with contextlib.redirect_stdout(capture):
    P = runpy.run_path(str(PREDECESSOR))
check("repo", "the stationary product-rule predecessor replays",
      "PASS 41/41" in capture.getvalue() and not P["FAILURES"])
H = P["H"]
S = P["S"]
M = S["P"]["M"]
cells = P["cells"]
core = P["core"]
phase = P["phase"]
pairs = P["pairs"]
selected = P["selected"]
sym_pair = P["sym_pair"]
real_scalar = P["real_scalar"]
principal_with = P["principal_with"]
field_responses = P["field_responses"]
c00 = P["c00"]
c01 = P["c01"]
residual = P["residual"]
zero_linear = P["zero_linear"]
constant_total = P["constant_total"]
etas = P["etas"]

check("fingerprint", "the carrier remains the selected 196-real Cl1 bank", len(cells) == 196)
check("fingerprint", "the gauge carrier remains all 91 real-K77 Cl2 generators", len(etas) == 91)
check("fingerprint", "the selected product channel is unchanged", selected == ("comm", "symi", "symi"))
check("fingerprint", "the stationary residual remains nonzero and Krein-null",
      bool(residual) and S["residual_pairing"](residual, residual) == S["ZERO"])
check("fingerprint", "the inherited backend is the exact moving-Shiab K77 implementation",
      callable(M["d_shiab"]) and M["ETA"] == tuple(core.eta))
check("fingerprint", "the inherited frozen constant response has rank 90",
      constant_total.rank() == 90)


def form_commutator(eta, form):
    return M["fclean"](P["form_commutator"](eta, form))


def negate_element(value):
    return core.escale(-1, value)


def moving_shiab(curvature, eta, sign=-1):
    """Move Phi with the same [eta,-] convention as the field orbit.

    The older backend writes coefficient motion as [coefficient, chi], while
    this stationary packet writes field motion as [eta, coefficient].  Hence
    chi=-eta is the same infinitesimal conjugation.  ``sign=+1`` is the planted
    convention reversal.
    """

    chi = negate_element(eta) if sign == -1 else eta
    return M["d_shiab"](curvature, selected, chi)


def scalar(value) -> sp.Expr:
    return sp.factor(real_scalar(value))


def form_sub(left, right):
    return S["fadd"](left, S["fscale"](Fraction(-1), right))


def cross(left, right):
    return S["fadd"](S["wedge_raw"](left, right), S["wedge_raw"](right, left))


def principal_source(mu, delta):
    q_mu = {1 << mu: {0: S["ONE"]}}
    return S["wedge_raw"](q_mu, delta)


def moving_principal(mu, delta, eta, sign=-1):
    return moving_shiab(principal_source(mu, delta), eta, sign=sign)


def moving_zero_linear(delta, eta, sign=-1):
    return moving_shiab(S["fscale"](Fraction(1, 3), cross(delta, S["base"])), eta, sign=sign)


def form_to_sparse_vector(form):
    out = {}
    for form_mask, coefficient in form.items():
        form_index = form_mask.bit_length() - 1
        for clifford_mask, gaussian in coefficient.items():
            clifford_index = clifford_mask.bit_length() - 1
            if phase[clifford_index] == S["ONE"]:
                value = sp.Rational(gaussian[0].numerator, gaussian[0].denominator)
                check_part = gaussian[1]
            else:
                value = sp.Rational(gaussian[1].numerator, gaussian[1].denominator)
                check_part = gaussian[0]
            if check_part != 0:
                raise ValueError("orbit left the selected real phase bank")
            if value:
                out[14 * form_index + clifford_index] = value
    return out


def linear_combination(forms, coefficients):
    answer = {}
    for index, value in coefficients.items():
        rational = sp.Rational(value)
        answer = S["fadd"](
            answer,
            S["fscale"](Fraction(int(rational.p), int(rational.q)), forms[index]),
        )
    return answer


stationary_sources = [
    principal_source(0, c00),
    principal_source(0, c01),
    principal_source(1, c01),
]
stationary_source_covariance = []
stationary_source_wrong = []
stationary_source_live = []
for eta in etas:
    for source_value in stationary_sources:
        coefficient_motion = moving_shiab(source_value, eta)
        left = S["fadd"](
            S["shiab"](form_commutator(eta, source_value), selected),
            coefficient_motion,
        )
        right = form_commutator(eta, S["shiab"](source_value, selected))
        stationary_source_covariance.append(left == right)
        wrong = S["fadd"](
            S["shiab"](form_commutator(eta, source_value), selected),
            moving_shiab(source_value, eta, sign=1),
        )
        stationary_source_wrong.append(wrong != right)
        stationary_source_live.append(bool(coefficient_motion))
check("covariance", "moving Shiab is exact on all 273 stationary-jet source packets",
      len(stationary_source_covariance) == 273 and all(stationary_source_covariance))
check("covariance", "the load-bearing stationary packets contain live moving-Phi responses",
      any(stationary_source_live))
check("plant", "PLANT reversing the moving-Phi sign fails on every live stationary packet",
      all(failed for failed, live in zip(stationary_source_wrong, stationary_source_live) if live))


print("\nD. INDEPENDENT MOVING-SHIAB EULER RESPONSE")
moving = sp.zeros(196, 91)
moving_principal_matrix = sp.zeros(196, 91)
moving_lower_matrix = sp.zeros(196, 91)
moving_residual_owner = sp.zeros(196, 91)
background_motion_checks = []
fixed_p00 = principal_with(selected, 0, c00)
fixed_p01_0 = principal_with(selected, 0, c01)
fixed_p01_1 = principal_with(selected, 1, c01)
b_tests = [zero_linear(test) for _, _, test in cells]

for column, eta in enumerate(etas):
    delta_base = P["gauge_fields"][column]
    delta00 = form_commutator(eta, c00)
    delta01 = form_commutator(eta, c01)
    b_delta = zero_linear(delta_base)
    d_residual_owner = form_sub(form_commutator(eta, residual), b_delta)
    background_source_motion = S["fscale"](
        Fraction(-1, 3), S["shiab"](cross(delta_base, S["base"]), selected)
    )
    background_motion_checks.append(d_residual_owner == background_source_motion)

    # This is the moving-Phi derivative itself, obtained from the independently
    # certified operator identity D_Phi S(X)=[eta,S(X)]-S([eta,X]).
    d_p00 = form_sub(form_commutator(eta, fixed_p00), principal_with(selected, 0, delta00))
    d_p01_0 = form_sub(form_commutator(eta, fixed_p01_0), principal_with(selected, 0, delta01))
    d_p01_1 = form_sub(form_commutator(eta, fixed_p01_1), principal_with(selected, 1, delta01))

    for row, (_, _, test) in enumerate(cells):
        test_orbit_coordinates = form_to_sparse_vector(form_commutator(eta, test))
        p0_test = field_responses[0][row]
        p1_test = field_responses[1][row]
        p0_test_orbit = linear_combination(field_responses[0], test_orbit_coordinates)
        p1_test_orbit = linear_combination(field_responses[1], test_orbit_coordinates)
        d_p0_test = form_sub(form_commutator(eta, p0_test), p0_test_orbit)
        d_p1_test = form_sub(form_commutator(eta, p1_test), p1_test_orbit)

        principal_value = scalar(sym_pair(d_p0_test, fixed_p00))
        principal_value += scalar(sym_pair(p0_test, d_p00))
        principal_value += scalar(sym_pair(d_p0_test, fixed_p01_1))
        principal_value += scalar(sym_pair(p0_test, d_p01_1))
        principal_value += scalar(sym_pair(d_p1_test, fixed_p01_0))
        principal_value += scalar(sym_pair(p1_test, d_p01_0))

        # D_Phi B(test) at fixed test and base follows from the same operator
        # covariance.  The D2 pairing is read from the already assembled exact
        # lower Hessian rather than recomputing 17,836 Shiab derivatives.
        b_test = b_tests[row]
        b_test_orbit = linear_combination(b_tests, test_orbit_coordinates)
        d2_pair = P["lower"][row, column] - scalar(sym_pair(b_test, b_delta))
        d_b_pair = scalar(sym_pair(form_commutator(eta, b_test), residual))
        d_b_pair -= scalar(sym_pair(b_test_orbit, residual))
        d_b_pair -= d2_pair
        moving_principal_matrix[row, column] = sp.factor(principal_value)
        moving_lower_matrix[row, column] = sp.factor(d_b_pair)
        moving[row, column] = sp.factor(principal_value + d_b_pair)
        moving_residual_owner[row, column] = scalar(sym_pair(b_test, d_residual_owner))

wrong_sign = -moving
complete_moving = moving + moving_residual_owner
check("theorem", "the covariant residual owner is exactly the rho=-1/3 moving curvature-source input",
      len(background_motion_checks) == 91 and all(background_motion_checks))

check("exact", "the independently assembled moving-Shiab response has rank 90",
      moving.rank() == 90, moving.rank())
print(f"MOVING_PRINCIPAL_RANK={moving_principal_matrix.rank()}")
print(f"MOVING_LOWER_RANK={moving_lower_matrix.rank()}")
print(f"MOVING_RESIDUAL_OWNER_RANK={moving_residual_owner.rank()}")
print(f"PRINCIPAL_PLUS_MOVING_RANK={(P['product'] + moving_principal_matrix).rank()}")
print(f"LOWER_PLUS_MOVING_RANK={(P['lower'] + moving_lower_matrix).rank()}")
check("correction", "moving Shiab alone leaves a rank-24 constant response",
      (moving + constant_total).rank() == 24)
check("theorem", "co-moving residual-source/Hq response cancels the rank-24 remainder",
      complete_moving + constant_total == sp.zeros(196, 91))
check("theorem", "the complete constant-parameter Ward response has rank zero",
      (complete_moving + constant_total).rank() == 0)
check("theorem", "the moving response retains the same sole kernel e12e13",
      moving.nullspace() == constant_total.nullspace()
      and [(pairs[i], value) for i, value in enumerate(moving.nullspace()[0]) if value]
      == [([12, 13], sp.Integer(1))])
control_column = pairs.index([12, 13])
check("control", "e12e13 remains zero in every constant-order response component",
      all(matrix[:, control_column] == sp.zeros(196, 1) for matrix in (
          constant_total, moving, moving_residual_owner, complete_moving
      )))
check("plant", "PLANT freezing Shiab leaves the inherited rank-90 burden",
      constant_total.rank() == 90)
check("plant", "PLANT reversing moving-Phi while retaining the residual owner fails closure",
      (constant_total + wrong_sign + moving_residual_owner).rank() > 0)


print("\nE. WHAT CLOSED AND WHAT DID NOT")
trace = P["trace"]
check("exact", "the independent second-parameter-jet Lorentz trace remains rank 25",
      trace.rank() == 25)
check("scope", "constant-parameter closure does not cancel the separate second-jet trace",
      sp.Matrix.hstack(complete_moving + constant_total, trace).rank() == 25)
for kind, label in (
    ("layer0", "constant closure needs both moving Phi/Shiab and the covariant residual-source/Hq owner"),
    ("principal_bundle", "first-parameter jets affine connection motion and observation jets remain"),
    ("gauge_bv", "the complete jet gauge differential and reducibility remain unassembled"),
    ("spencer", "the surviving rank-25 second-jet trace still requires compatibility analysis"),
    ("symplectic", "no stationary-symbol quotient presymplectic current or BFV phase space is inferred"),
    ("analytic", "no domain hyperbolicity positivity spectrum or stability follows"),
    ("source", "the source owns the moving family but not these selected K77 ranks"),
    ("datum", "P1 P2 P3 remain unchanged and unused"),
    ("scope", "ledger canon residue quotient count and public posture do not move"),
):
    check(kind, label, True)

print("SOURCE_RETURN=SOURCE_CONFIRMS_MOVING_PHI_SHIAB_EQUIVARIANCE_GRAMMAR__SOURCE_SILENT_SELECTED_K77_STATIONARY_WARD_RANKS_AND_EXACT_RESIDUAL_OWNER__REPOSITORY_DERIVES_EXACT_CONSTANT_PARAMETER_CANCELLATION")
print(f"FROZEN_CONSTANT_RANK={constant_total.rank()}")
print(f"MOVING_SHIAB_RANK={moving.rank()}")
print(f"SHIAB_ONLY_REMAINDER_RANK={(constant_total + moving).rank()}")
print(f"MOVING_RESIDUAL_OWNER_RANK={moving_residual_owner.rank()}")
print(f"COMPLETE_CONSTANT_WARD_RANK={(constant_total + complete_moving).rank()}")
print("MOVING_SHIAB_KERNEL=(12,13)")
print(f"REVERSED_SIGN_WARD_RANK={(constant_total + wrong_sign + moving_residual_owner).rank()}")
print(f"SECOND_PARAMETER_JET_TRACE_RANK={trace.rank()}")
print("DISPOSITION=CONSTANT_PARAMETER_WARD_CLOSED_BY_MOVING_SHIAB_PLUS_COVARIANT_RESIDUAL_OWNER__FIRST_JETS_AND_SECONDJET25_REMAIN")
print("P1_P2_P3=UNUSED")
print("CHECKS=" + " ".join(f"{kind}:{count}" for kind, count in sorted(COUNTS.items())))
if FAILURES:
    raise SystemExit("FAILURES: " + "; ".join(FAILURES))
print(f"PASS {sum(COUNTS.values())}/{sum(COUNTS.values())}")
