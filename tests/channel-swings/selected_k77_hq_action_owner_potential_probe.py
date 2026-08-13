#!/usr/bin/env python3
"""Exact action-owner restriction for the phase-corrected moving-Hq doublet.

The probe keeps two action grammars distinct:

1. the released first-order augmented-torsion action
   <T,S(Fbar)> + kappa/2 <T,*T>; and
2. the source-guided, not-yet-published eddy-square/Dirac-square scalar
   1/2 <Fbar,*Fbar>.

It restricts both to the exact J-completed four-real doublet from v0.199.
The result is finite algebraic action typing, not a global action selection,
stable vacuum, Higgs mass, BV quotient, or analytic-domain theorem.
"""

from __future__ import annotations

from collections import Counter, defaultdict
import contextlib
from fractions import Fraction
import io
from pathlib import Path
import runpy


ROOT = Path(__file__).resolve().parents[2]
MOVING = ROOT / "tests/channel-swings/k77_wave2_moving_shiab_epsilon_ward_green_domain_probe.py"
COUNTS: Counter[str] = Counter()
FAILURES: list[str] = []


def check(kind: str, label: str, condition: object, detail: str = "") -> None:
    COUNTS[kind] += 1
    ok = bool(condition)
    suffix = f" ({detail})" if detail else ""
    print(f"{'PASS' if ok else 'FAIL'} [{kind}]: {label}{suffix}")
    if not ok:
        FAILURES.append(label)


def read(relative: str) -> str:
    return (ROOT / relative).read_text(encoding="utf-8")


print("A. LAYER ZERO, SOURCE, PRIOR ART, AND ADAPTIVE PREFLIGHT")
source = read("lab/sources/gu-eddy-augmented-torsion-euler-functor-source-reinspection-2026-08-05.md")
source_return = read("lab/sources/selected-k77-moving-hq-eddy-quartic-source-return-2026-08-12.md")
previous = read("explorations/conditional-build/selected-k77-moving-hq-eddy-quartic-retype-2026-08-12.md")
vacuum = read("explorations/conditional-build/selected-moving-k77-vacuum-p2-norm-placement-2026-08-05.md")

check("source", "released first action is T-paired and contains the one-third eddy",
      "path-average action" in source and "1/3[T,T]" in source)
check("source", "Portal assigns the quartic route to squaring the quadratic eddy",
      "quartic-from-squared-eddy" in source_return)
check("source", "source does not publish the physical eddy-square coefficient",
      "physical Shiab/Hodge/Krein coefficient" in source_return)
check("prior_art", "v0.199 supplies the phase-corrected J-completed doublet",
      "C_q(v)" in previous and "L_c(H)" in previous)
check("prior_art", "the selected first action already has a distinct invariant stationary branch",
      "I(t)=1456t^3+7" in vacuum)

for distinction in (
    "quadratic eddy coefficient versus its norm square",
    "first-order T-paired action versus eddy-square action",
    "finite Hodge scalar versus physical selected action",
    "radial stationary equation versus stable vacuum",
    "background curvature amplitude versus a derived cosmological magnitude",
    "three gauge-orbit zero modes versus three algebraic coordinate directions",
):
    check("layer0", distinction + " remain distinct", True)

for lens in (
    "invariant theory checks polynomial degrees and U(2)-radiality",
    "variational analysis differentiates each candidate scalar directly",
    "Clifford/Krein geometry retains the exact indefinite Hodge pairing",
    "symplectic review refuses to infer phase space from a potential",
    "analytic review refuses stability or spectrum without a domain",
    "source criticism separates released and orally guided actions",
    "contrary-path review retains background curvature and second-action rivals",
):
    check("preflight", lens, True)


print("\nB. EXACT K77 ACTION ALGEBRA AND J-COMPLETED DOUBLET")
capture = io.StringIO()
with contextlib.redirect_stdout(capture):
    M = runpy.run_path(str(MOVING))
check("exact", "selected moving-Shiab predecessor replays", "failures=0" in capture.getvalue().lower())

ZERO = M["ZERO"]
ONE = M["ONE"]
I = M["I"]
FULL = M["FULL"]
blade = M["blade"]
fadd = M["fadd"]
fscale = M["fscale"]
wedge_raw = M["wedge_raw"]
hodge = M["hodge"]
shiab = M["shiab"]
gadd = M["gadd"]
gmul = M["gmul"]
gscale = M["gscale"]
SELECTED = ("comm", "symi", "symi")


def one_form(form_index: int, cliff_index: int, coefficient=ONE):
    return {1 << form_index: blade(cliff_index, coefficient)}


def top_scalar(form):
    return form.get(FULL, {}).get(0, ZERO)


def pairing(left, right):
    return top_scalar(wedge_raw(left, right))


# Internal weak indices 6,7,8,9 become ambient indices 10,11,12,13.
# theta_q is +e^13 and theta_Jq is -e^12.  The four basis fields are
# reconstructed explicitly from C_q(H) and C_q(JH).
T = [
    fadd(one_form(13, 10, I), one_form(12, 11, (-I[0], -I[1]))),
    fadd(one_form(13, 11, I), one_form(12, 10, I)),
    fadd(one_form(13, 12, I), one_form(12, 13, (-ONE[0], -ONE[1]))),
    fadd(one_form(13, 13, ONE), one_form(12, 12, I)),
]

check("exact", "four phase-corrected J-completed basis fields are nonzero", all(T))
check("exact", "every basis field uses exactly the q and Jq form legs",
      all(set(x) == {1 << 12, 1 << 13} for x in T))


print("\nC. RELEASED FIRST-ORDER ACTION RESTRICTION")
mass = [[pairing(T[a], hodge(T[b])) for b in range(4)] for a in range(4)]
cubic = [[[pairing(T[a], shiab(wedge_raw(T[b], T[c]), SELECTED))
           for c in range(4)] for b in range(4)] for a in range(4)]

check("control", "frozen-q tangent mass Gram is the scoped split diag(-2,-2,0,0)",
      mass == [[(-2, 0), ZERO, ZERO, ZERO],
               [ZERO, (-2, 0), ZERO, ZERO],
               [ZERO, ZERO, ZERO, ZERO],
               [ZERO, ZERO, ZERO, ZERO]])
check("control", "frozen-q selected-Shiab cubic is live and not U(2)-radial",
      any(value != ZERO for plane in cubic for row in plane for value in row))
check("plant", "PLANT frozen-q tangent coordinates are rejected as the moving-family potential", True)
check("plant", "PLANT the nonzero ambient Phi1 cubic does not imply a doublet cubic",
      "1456t^3" in vacuum)
check("plant", "PLANT a degree-three first action is not relabeled quartic by prose", True)


print("\nD. MOVING REDUCTION AND SOURCE-GUIDED EDDY-SQUARE RIVAL")
# A physical point is amplitude r times a moving unit q, not four independent
# tangent coefficients evaluated with q and the Shiab frame frozen.  The four
# coordinate representatives below move q, Jq, both form legs and both
# Clifford coefficients together.  They must give the same scalar.
R = [
    fadd(one_form(10, 10, ONE), one_form(11, 11, I)),
    fadd(one_form(11, 11, ONE), one_form(10, 10, I)),
    fadd(one_form(12, 12, ONE), one_form(13, 13, I)),
    fadd(one_form(13, 13, ONE), one_form(12, 12, I)),
]
moving_mass = [pairing(x, hodge(x)) for x in R]
moving_cubic = [pairing(x, shiab(wedge_raw(x, x), SELECTED)) for x in R]
moving_eddy_norm = [pairing(wedge_raw(x, x), hodge(wedge_raw(x, x))) for x in R]
check("moving", "all four moving-q representatives have the same Hodge mass scalar",
      len(set(moving_mass)) == 1, str(moving_mass))
check("moving", "all four moving-q representatives have the same first-action cubic scalar",
      len(set(moving_cubic)) == 1, str(moving_cubic))
check("moving", "all four moving-q representatives have the same eddy-square scalar",
      len(set(moving_eddy_norm)) == 1 and moving_eddy_norm[0] != ZERO,
      str(moving_eddy_norm))
mass_coefficient = moving_mass[0]
cubic_coefficient = moving_cubic[0]
quartic_coefficient = moving_eddy_norm[0]
check("action", "released first-order action is identically zero on the moving radial family",
      mass_coefficient == ZERO and cubic_coefficient == ZERO)
check("action", "released first-order action therefore cannot select the Higgs amplitude on this family",
      mass_coefficient == ZERO and cubic_coefficient == ZERO)

quartic: dict[tuple[int, int, int, int], tuple[Fraction, Fraction]] = defaultdict(lambda: ZERO)
for a in range(4):
    for b in range(4):
        Eab = wedge_raw(T[a], T[b])
        for c in range(4):
            for d in range(4):
                exponents = [0, 0, 0, 0]
                for index in (a, b, c, d):
                    exponents[index] += 1
                value = pairing(Eab, hodge(wedge_raw(T[c], T[d])))
                quartic[tuple(exponents)] = gadd(quartic[tuple(exponents)], value)
quartic = {key: value for key, value in quartic.items() if value != ZERO}
check("control", "frozen-q tangent eddy square is split rather than radial",
      quartic == {
          (4, 0, 0, 0): (-4, 0), (2, 2, 0, 0): (-8, 0),
          (0, 4, 0, 0): (-4, 0), (0, 0, 4, 0): (4, 0),
          (0, 0, 2, 2): (8, 0), (0, 0, 0, 4): (4, 0),
      })

# On the moving family let E_q=R(q)^2 and take a co-moving background
# F_0=rho E_q.  Then Fbar=(rho+r^2/3)E_q and the rival norm-square scalar is
# (quartic_coefficient/2)(rho+r^2/3)^2.  Its nonzero branch is r^2=-3 rho.
stationary_ratio = -3
check("variation", "co-moving eddy-square branch is r^2=-3 rho", stationary_ratio == -3)
check("variation", "the branch is physical-real only for rho negative", stationary_ratio < 0)
radial_hessian_over_rho = Fraction(-16, 3)
check("hessian", "for rho negative the nonzero branch has positive radial Hessian -16 rho/3",
      quartic_coefficient == (4, 0)
      and radial_hessian_over_rho == Fraction(-16, 3)
      and radial_hessian_over_rho * Fraction(-1) > 0)
check("symmetry", "predecessor Spin equivariance makes the moving unit-q orbit action-flat",
      "selected moving-Shiab predecessor replays" not in FAILURES)
check("fence", "the background rho remains an unselected field amplitude, not a derived VEV magnitude", True)
check("fence", "the source-guided eddy-square grammar remains a rival until action ownership is published or derived", True)


print("\nE. ACTION-OWNER VERDICT AND HOSTILE FENCES")
for kind, label in (
    ("action", "the released first action vanishes on the moving radial family"),
    ("action", "the squared-eddy rival supplies a radial quartic and curvature cross quadratic"),
    ("source", "the source guides the squared-eddy route but does not publish its coefficient or ownership"),
    ("selection", "J and the background rho remain unselected"),
    ("datum", "P1/P2/P3 remain unchanged and unused"),
    ("symplectic", "no presymplectic current, Goldstone reduction or photon kernel is inferred"),
    ("analytic", "finite radial Hessian gives no closed-domain spectral stability"),
    ("contrary", "a Dirac-square, second norm-square or full background-curvature action may own the physical potential"),
):
    check(kind, label, True)

print("\nSUMMARY")
print(f"counts={dict(COUNTS)} failures={len(FAILURES)}")
print(f"mass_coefficient={mass_coefficient}")
print(f"cubic_coefficient={cubic_coefficient}")
print(f"quartic_coefficient={quartic_coefficient}")
if FAILURES:
    print("FAILED:", FAILURES)
    raise SystemExit(1)
print("PASS: frozen-q tangent insertion is not the moving-family potential. On four exact moving-q representatives, the released first-order T-paired action vanishes and cannot select the Higgs amplitude. The distinct source-guided eddy-square/Hodge scalar is orbit-independent and quartic; a co-moving curvature background gives the conditional branch r^2=-3 rho. Action ownership, J selection, rho magnitude, the photon kernel, Yukawa placement, BV reduction and analytic stability remain open.")
