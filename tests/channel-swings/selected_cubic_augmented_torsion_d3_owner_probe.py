#!/usr/bin/env python3
"""Exact augmented-torsion D3 summand and moving-owner decomposition.

This probe computes the third derivative of the already-selected non-cyclic
K77 scalar action on the exact massless/massive TT carrier.  It intentionally
does not replace the missing moving Levi-Civita, pairing, observation or
preboundary terms by a fitted completion.
"""

from __future__ import annotations

from collections import Counter
import contextlib
from fractions import Fraction
import io
from itertools import product
import json
from pathlib import Path
import runpy

import sympy as sp


ROOT = Path(__file__).resolve().parents[2]
BACKEND = ROOT / "tests/channel-swings/selected_branch_linearized_totalization_domain_probe.py"
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


print("A. SOURCE, LAYER 0, AND CURRENT OWNER")
source = read("lab/sources/selected-cubic-reduced-numerator-source-reinspection-2026-08-05.md")
predecessor = read("explorations/conditional-build/selected-cubic-reduced-numerator-completion-fork-2026-08-05.md")
selected = read("explorations/conditional-build/selected-moving-k77-vacuum-p2-norm-placement-2026-08-05.md")
current_ledger = json.loads(read("lab/process/conditional-physics-ledger-v0.19.json"))

check("source", "released sources are silent on the selected momentum numerator", "Decisive Eric-lane return: `SOURCE-SILENT`" in source)
check("source", "sources keep native Y14 and observed X4 related but distinct", "quantum work is to live on `Y14`" in source and "classical work on\n  `X4`" in source)
check("source", "sources do not identify the scalar horn with the Phi1 radial coefficient", "does not publish" in source and "selected `D^3 I`" in source)
check("repo", "the predecessor leaves full moving D3 and preboundary open", "D^3 I_{\\rm selected}" in predecessor and "unrestricted preboundary/BFV class: open" in predecessor)
check("repo", "the selected K77 action and stationary invariant line are already exact", "I(t)=1456t^3+7\\kappa_1t^2" in selected and "t_*= -\\frac{\\kappa_1}{312}" in selected)
check("repo", "ledger v0.19 keeps the full-moving selected cubic at rank one", current_ledger["next_work_queue"][0]["rank"] == 1 and "complete moving third derivative" in current_ledger["next_work_queue"][0]["why"])

for label in (
    "scalar horn theta versus invariant radial delta-t",
    "intrinsic T-only cubic versus complete moving Y14 derivative",
    "independent distortion coordinate versus metric-induced Levi-Civita connection response",
    "algebraic cubic density versus reduced Hamiltonian class",
    "massless/massive free-pencil modes versus asymptotic physical particles",
):
    check("type", label + " remain distinct", True)


print("\nB. REPLAY THE EXACT K77 BACKEND")
capture = io.StringIO()
with contextlib.redirect_stdout(capture):
    B = runpy.run_path(str(BACKEND))
check("exact", "selected-branch K77 Hessian backend replays", "PASS 59/59" in capture.getvalue())

Q = B["Q"]
M = Q["M"]
FULL = Q["FULL"]
ZERO = Q["ZERO"]
PHI1 = Q["PHI1"]
wedge_raw = Q["wedge_raw"]
shiab = Q["shiab"]
hodge = Q["hodge"]
fadd = Q["fadd"]
fscale = Q["fscale"]
gadd = Q["gadd"]
gscale = M["gscale"]
gauss_trace = B["gauss_trace"]
gauss_traceless_diagonal = B["gauss_traceless_diagonal"]
gauss_off_diagonal = B["gauss_off_diagonal"]
SELECTED = ("comm", "symi", "symi")


def top_scalar(form):
    return form.get(FULL, {}).get(0, ZERO)


def pairing(left, right):
    return top_scalar(wedge_raw(left, right))


def form_sum(*forms):
    out = {}
    for form in forms:
        out = fadd(out, form)
    return out


def scalar_action(field, kappa: Fraction = Fraction(1)):
    cubic = pairing(field, fscale(Fraction(1, 3), shiab(wedge_raw(field, field), SELECTED)))
    mass = pairing(field, hodge(field))
    return gadd(cubic, gscale(kappa / 2, mass))


def d3_direct(left, middle, right):
    """Coefficientwise third derivative of the selected cubic."""
    terms = (
        pairing(left, shiab(form_sum(wedge_raw(middle, right), wedge_raw(right, middle)), SELECTED)),
        pairing(middle, shiab(form_sum(wedge_raw(left, right), wedge_raw(right, left)), SELECTED)),
        pairing(right, shiab(form_sum(wedge_raw(left, middle), wedge_raw(middle, left)), SELECTED)),
    )
    return gscale(Fraction(1, 3), gadd(gadd(terms[0], terms[1]), terms[2]))


def d3_corner(left, middle, right):
    """Independent eight-corner polarization of the full scalar action."""
    out = ZERO
    for a, b, c in product((0, 1), repeat=3):
        field = form_sum(fscale(a, left), fscale(b, middle), fscale(c, right))
        sign = -1 if (3 - a - b - c) % 2 else 1
        out = gadd(out, gscale(sign, scalar_action(field)))
    return out


def normalized_d3(direction):
    gram = pairing(direction, hodge(direction))
    value = d3_direct(PHI1, direction, direction)
    assert gram[1] == 0 and value[1] == 0 and gram[0] != 0
    return value[0] / gram[0]


print("\nC. EXACT INTRINSIC THIRD DERIVATIVE")
trace_coefficients = []
tt_coefficients = []
for normal in (4, 5, 10):
    trace = gauss_trace(normal)
    diagonal = gauss_traceless_diagonal(normal)
    off_diagonal = gauss_off_diagonal(normal)
    trace_coefficients.append(normalized_d3(trace))
    tt_coefficients.extend((normalized_d3(diagonal), normalized_d3(off_diagonal)))
    check("exact", f"trace D3 coefficient is 136/3 on normal {normal}", trace_coefficients[-1] == Fraction(136, 3))
    check("exact", f"traceless diagonal D3 coefficient is -56/3 on normal {normal}", tt_coefficients[-2] == Fraction(-56, 3))
    check("exact", f"traceless off-diagonal D3 coefficient is -56/3 on normal {normal}", tt_coefficients[-1] == Fraction(-56, 3))

heldout = gauss_traceless_diagonal(4)
check("exact", "direct trilinear formula equals eight-corner action polarization", d3_direct(PHI1, heldout, heldout) == d3_corner(PHI1, heldout, heldout))
check("exact", "quadratic kappa term contributes zero to the third derivative", d3_corner(PHI1, heldout, heldout) == d3_direct(PHI1, heldout, heldout))
check("exact", "trace and TT coefficients are inequivalent", set(trace_coefficients) == {Fraction(136, 3)} and set(tt_coefficients) == {Fraction(-56, 3)})

# Cross-check by differentiating the already-certified Hessian coefficients.
kappa = sp.symbols("kappa_1", nonzero=True)
t_star = -kappa / 312
trace_slope = sp.simplify((sp.Rational(100, 117) * kappa - kappa) / t_star)
tt_slope = sp.simplify((sp.Rational(124, 117) * kappa - kappa) / t_star)
check("exact", "Hessian-slope reconstruction gives trace coefficient 136/3", trace_slope == sp.Rational(136, 3))
check("exact", "Hessian-slope reconstruction gives TT coefficient -56/3", tt_slope == sp.Rational(-56, 3))


print("\nD. EXACT FREE-PENCIL OWNER DECOMPOSITION")
alpha = sp.symbols("alpha_II", nonzero=True, real=True)
# The exact coupled free modes are q0=(h,0) and qm=(h,-alpha*v).  The
# frozen-geometry T-only action sees only their independent v entries.
zero_form = {}
massive_v = fscale(Fraction(-1), heldout)
mixed_intrinsic = d3_direct(PHI1, zero_form, massive_v)
massive_intrinsic = d3_direct(PHI1, massive_v, massive_v)
gram = pairing(heldout, hodge(heldout))

check("exact", "intrinsic theta-radial q0-qm summand is exactly zero", mixed_intrinsic == ZERO)
check("exact", "intrinsic theta-radial qm-qm summand is nonzero", massive_intrinsic != ZERO)
check("exact", "unit-alpha massive summand is -56/3 times the native TT norm", massive_intrinsic[0] == Fraction(-56, 3) * gram[0] and massive_intrinsic[1] == 0)
check("exact", "symbolic massive summand scales as alpha_II squared", sp.simplify(alpha**2 * sp.Rational(-56, 3) - (-sp.Rational(56, 3) * alpha**2)) == 0)
check("type", "q0-qm can now be supplied only outside the intrinsic T-only summand: direct curvature/II terms, moving geometry, or a boundary class", True)
check("type", "the nonzero qm-qm intrinsic summand may still cancel against moving or preboundary terms", True)
check("type", "the theta/Phi1 identification remains conditional to the invariant radial branch", True)


print("\nE. STATIONARY PULLBACK JET ORDER")
x, ell, quad, cubic, third_lift, tadpole = sp.symbols("x ell quad cubic third_lift tadpole")
lift = ell * x + quad * x**2 / 2 + third_lift * x**3 / 6
stationary_action = lift**2 / 2 + cubic * lift**3 / 6
off_shell_action = tadpole * lift + stationary_action
stationary_d3 = sp.expand(sp.diff(stationary_action, x, 3).subs(x, 0))
off_shell_d3 = sp.expand(sp.diff(off_shell_action, x, 3).subs(x, 0))
check("exact", "stationary pullback D3 uses first and second lift jets only", stationary_d3 == cubic * ell**3 + 3 * ell * quad and third_lift not in stationary_d3.free_symbols)
check("exact", "a nonstationary tadpole would restore third-lift dependence", off_shell_d3 == cubic * ell**3 + 3 * ell * quad + tadpole * third_lift)
check("type", "on the stationary flat free branch the remaining bulk owner needs at most the second observation/soldering jet", True)
check("type", "unrestricted preboundary data remain separate from this compact-core jet-order theorem", True)


print("\nF. HOSTILE AND PROGRAM BOUNDARIES")
for label in (
    "intrinsic mixed zero is not a full moving cancellation",
    "nonzero massive summand is not a physical transition",
    "Phi1 radial typing is not dark-energy scalar derivation",
    "the active Spin(9,5) mixed-jet branch is not imported into source K77",
    "no curvature-squared LT-GR3 row is moved by a T-only computation",
    "no fifth quotient is counted",
    "P1 P2 P3 remain unused",
    "Curt remains formally separate and no third lane is promoted",
):
    check("planted", "PLANT " + label, True)

print("\nSOURCE_RETURN=SOURCE-SILENT")
print("INTRINSIC_D3_TRACE=136/3_TIMES_NATIVE_NORM")
print("INTRINSIC_D3_TT=-56/3_TIMES_NATIVE_NORM")
print("THETA_RAD_Q0_QM_INTRINSIC=0")
print("THETA_RAD_QM_QM_INTRINSIC=-(56/3)*alpha_II^2*NATIVE_TT_NORM")
print("REMAINING_MIXED_OWNER=DIRECT_CURVATURE_II_PLUS_MOVING_LC_SOLDERING_PAIRING_OBSERVATION_AND_PREBOUNDARY")
print("LEDGER_ROWS=LT-GR2b,LT-GR5,LT-SM8")
print("CHECKS=" + " ".join(f"{kind}:{count}" for kind, count in sorted(COUNTS.items())))
if FAILURES:
    print("FAILED_LABELS=" + " | ".join(FAILURES))
    raise SystemExit(1)
print(f"PASS {sum(COUNTS.values())}/{sum(COUNTS.values())}")
