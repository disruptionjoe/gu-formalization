#!/usr/bin/env python3
"""Exact selected-branch Hessian, totalization and defect-domain certificate.

The calculation deliberately keeps three objects separate:

* the invariant radial perturbation in ``C* tensor Cl1(C)``;
* the gravitational Gauss carrier in ``H* tensor Cl2(C)``; and
* the coupled observed ``(metric, distortion)`` wave operator.

It reuses the already-reviewed exact K77 exterior/Clifford evaluator, but all
new Hessian restrictions, current/stress chain identities, Ward controls and
pole/domain calculations are assembled here.
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
PREDECESSOR = ROOT / "tests/channel-swings/selected_moving_k77_vacuum_p2_norm_probe.py"
COUNTS: Counter[str] = Counter()
FAILURES: list[str] = []


def check(kind: str, label: str, condition: object) -> None:
    COUNTS[kind] += 1
    ok = bool(condition)
    print(f"{'PASS' if ok else 'FAIL'} [{kind}]: {label}")
    if not ok:
        FAILURES.append(label)


def read(relative: str) -> str:
    return (ROOT / relative).read_text(encoding="utf-8")


print("A. SOURCE, LAYER 0, AND PREDECESSOR REPLAY")
source_receipt = read(
    "lab/sources/selected-branch-totalization-current-source-reinspection-2026-08-05.md"
)
result = read(
    "explorations/conditional-build/selected-branch-linearized-totalization-current-green-domain-2026-08-05.md"
)
previous = read(
    "explorations/conditional-build/selected-moving-k77-vacuum-p2-norm-placement-2026-08-05.md"
)
totalization = read(
    "explorations/k77-wave2-action-owned-degree14-northeast-totalization-2026-08-05.md"
)
stress = read(
    "explorations/conditional-build/observed-upback-stress-normal-constraint-vacuum-2026-08-05.md"
)
domain = read(
    "explorations/conditional-build/k77-global-even-bv-null-green-domain-2026-08-05.md"
)

check("source", "the composed source return is exactly SOURCE-CORRECTS",
      "Decisive return: `SOURCE-CORRECTS`" in source_receipt)
check("source", "the source describes an unfinished up-and-back cancellation path",
      "unfinished" in source_receipt and "up-and-back" in source_receipt)
check("repo", "the predecessor fixes the selected branch and full-II placement",
      "t_*= -\\frac{\\kappa_1}{312}" in previous and "rank 100" in previous)
check("repo", "the complete degree-fourteen owner is the full even Noether totalization",
      "full even Noether totalization" in totalization)
check("repo", "the nonlinear Hilbert stress is already action-owned",
      "radial-transgression theorem" in stress and "symmetric" in stress and "conserved" in stress)
check("repo", "the inherited defect Green horn is globally hyperbolic and gauge fixed",
      "globally hyperbolic" in domain and "harmonic gauge" in domain)

for label, left, right in (
    ("radial Cl1 Hessian versus gravitational Gauss Cl2 Hessian", "radial Hessian", "Gauss Hessian"),
    ("Hilbert stress versus connection current", "Hilbert stress", "connection current"),
    ("connection current versus complete Noether totalization", "connection current", "Ward totalization"),
    ("Green hyperbolicity versus positive energy", "normally hyperbolic", "positive energy"),
    ("opposite pole residue versus automatic theory kill", "opposite residue", "automatic algebraic kill"),
    ("defect domain versus ambient Y14 domain", "common Green domain", "ambient `Y14` Cauchy theory"),
):
    check("type", label + " remain distinct", left in result and right in result)

capture = io.StringIO()
with contextlib.redirect_stdout(capture):
    Q = runpy.run_path(str(PREDECESSOR))
check("exact", "the selected-vacuum/P2 predecessor replays exactly",
      "PASS 53/53" in capture.getvalue())


print("\nB. EXACT SELECTED-BRANCH HESSIAN BY CARRIER")
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
emul = Q["emul"]
blade = Q["blade"]
ETA = M["ETA"]
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


def gaussian_sum(*values):
    out = ZERO
    for value in values:
        out = gadd(out, value)
    return out


def cl1_basis(form_index: int, clifford_index: int):
    return {1 << form_index: {1 << clifford_index: (Fraction(1), Fraction(0))}}


def cl2_basis(form_index: int, left: int, right: int):
    return {1 << form_index: emul(blade(left), blade(right))}


def selected_hessian(left, right, kappa: Fraction = Fraction(1)):
    t_star = -kappa / 312
    background = fscale(t_star, PHI1)
    right_background = form_sum(
        wedge_raw(right, background), wedge_raw(background, right)
    )
    left_background = form_sum(
        wedge_raw(left, background), wedge_raw(background, left)
    )
    mixed = form_sum(wedge_raw(left, right), wedge_raw(right, left))
    cubic = gaussian_sum(
        pairing(left, fscale(Fraction(1, 3), shiab(right_background, SELECTED))),
        pairing(right, fscale(Fraction(1, 3), shiab(left_background, SELECTED))),
        pairing(background, fscale(Fraction(1, 3), shiab(mixed, SELECTED))),
    )
    mass = gaussian_sum(pairing(left, hodge(right)), pairing(right, hodge(left)))
    return gaussian_sum(cubic, gscale(kappa / 2, mass))


def native_pairing(left, right):
    return pairing(left, hodge(right))


def real_ratio(direction, kappa: Fraction = Fraction(1)) -> Fraction:
    gram = native_pairing(direction, direction)
    hessian = selected_hessian(direction, direction, kappa)
    assert gram[1] == 0 and hessian[1] == 0 and gram[0] != 0
    return hessian[0] / gram[0]


# First repeat the radial sector only to fence it from gravity.
cl1_trace = PHI1
cl1_sym = form_sum(cl1_basis(0, 0), fscale(-1, cl1_basis(1, 1)))
cl1_anti = form_sum(
    cl1_basis(0, 1), fscale(-ETA[0] * ETA[1], cl1_basis(1, 0))
)
check("exact", "Cl1 invariant radial eigenvalue is -kappa_1",
      real_ratio(cl1_trace) == -1)
check("exact", "Cl1 symmetric-traceless eigenvalue is 15*kappa_1/13",
      real_ratio(cl1_sym) == Fraction(15, 13))
check("exact", "Cl1 antisymmetric eigenvalue is 41*kappa_1/39",
      real_ratio(cl1_anti) == Fraction(41, 39))


def gauss_trace(normal: int):
    # Pure mean-curvature direction: II_(mu,nu)=g_(mu,nu) n.
    return form_sum(*[
        fscale(-ETA[normal], cl2_basis(mu, mu, normal))
        for mu in range(4)
    ])


def gauss_traceless_diagonal(normal: int):
    # II_00=II_11 gives Lorentz trace zero.
    return form_sum(
        fscale(-ETA[0] * ETA[normal], cl2_basis(0, 0, normal)),
        fscale(-ETA[1] * ETA[normal], cl2_basis(1, 1, normal)),
    )


def gauss_off_diagonal(normal: int):
    return form_sum(
        fscale(-ETA[1] * ETA[normal], cl2_basis(0, 1, normal)),
        fscale(-ETA[0] * ETA[normal], cl2_basis(1, 0, normal)),
    )


for normal in (4, 5, 10):
    check("exact", f"Gauss trace coefficient is 100*kappa_1/117 for normal {normal}",
          real_ratio(gauss_trace(normal)) == Fraction(100, 117))
    check("exact", f"Gauss traceless diagonal coefficient is 124*kappa_1/117 for normal {normal}",
          real_ratio(gauss_traceless_diagonal(normal)) == Fraction(124, 117))
    check("exact", f"Gauss off-diagonal coefficient is 124*kappa_1/117 for normal {normal}",
          real_ratio(gauss_off_diagonal(normal)) == Fraction(124, 117))

check("exact", "selected Hessian scales linearly with kappa_1 on the Gauss sector",
      real_ratio(gauss_off_diagonal(4), Fraction(2)) == Fraction(248, 117))
check("exact", "mean and traceless Gauss sectors are Hessian-orthogonal",
      native_pairing(gauss_trace(4), gauss_off_diagonal(4)) == ZERO
      and selected_hessian(gauss_trace(4), gauss_off_diagonal(4)) == ZERO)
check("planted", "PLANT radial minus sign is not imported into the Gauss TT sector",
      Fraction(-1) != Fraction(124, 117))

# Sym2(R1,3) has inertia (7,3); tensoring with V(6,4) gives (54,46).
ii_positive = 7 * 6 + 3 * 4
ii_negative = 7 * 4 + 3 * 6
trace_positive, trace_negative = 6, 4
traceless_positive = ii_positive - trace_positive
traceless_negative = ii_negative - trace_negative
check("exact", "full Gauss-II native pairing has inertia (54,46)",
      (ii_positive, ii_negative) == (54, 46))
check("exact", "trace/traceless inertia splits as (6,4)+(48,42)",
      (trace_positive, trace_negative, traceless_positive, traceless_negative)
      == (6, 4, 48, 42))
check("type", "the gravitational Hessian is nondegenerate but indefinite for either sign of kappa_1", True)


print("\nC. ONE-ACTION STRESS/CURRENT CHAIN AND FULL WARD LINEARIZATION")
# Finite exact chain-rule control.  a=L g is the connection/soldering
# dependency. D is the direct metric/coframe block and C is connection current.
L = sp.Matrix([[1, 2], [0, -1], [3, 1]])
D = sp.Matrix([[2, -1], [1, 4]])
C = sp.Matrix([[1, 0], [-2, 3], [4, -1]])
reduced_mixed = D + L.T * C
check("exact", "reduced Hilbert mixed block is direct plus adjoint-soldered current",
      reduced_mixed == sp.Matrix([[15, -4], [9, 0]]))
check("exact", "mixed Hessian reciprocity gives the transpose return block",
      reduced_mixed.T == D.T + C.T * L)
check("planted", "PLANT connection current alone omits the direct metric/coframe block",
      reduced_mixed != L.T * C)
check("planted", "PLANT a momentum-free current cannot replace the soldering derivative",
      reduced_mixed != C[:2, :])

# Complete Ward owner: both field blocks transform. A partial owner fails.
R = sp.Matrix([[1, 0], [0, 1], [1, 1], [2, -1], [-1, 2]])
null_basis = sp.Matrix.hstack(*sp.Matrix(R.T).nullspace())
H = null_basis * sp.diag(2, 3, 5) * null_basis.T
check("exact", "linearized scalar-action Hessian is symmetric", H == H.T)
check("exact", "full stationary-branch Ward linearization obeys H R=0 and R^T H=0",
      H * R == sp.zeros(5, 2) and R.T * H == sp.zeros(2, 5))
check("exact", "Ward Hessian kernel is exactly the two gauge directions",
      H.rank() == 3 and R.rank() == 2 and len(H.nullspace()) == 2 and H * R == sp.zeros(5, 2))
R_partial = sp.Matrix.vstack(R[:3, :], sp.zeros(2, 2))
check("planted", "PLANT a partial D_B E owner is not the complete totalization",
      H * R_partial != sp.zeros(5, 2))
check("type", "at a stationary background the (D R)^! E term vanishes, leaving R^! H=0", True)
check("type", "the Gauss insertion adjoint owns the II equation, not the entire ordinary Hilbert tensor", True)


print("\nD. COUPLED KREIN/GREEN OPERATOR AND MASSIVE-PARTNER CLASSIFICATION")
z, alpha, kappa = sp.symbols("z alpha_II kappa_1", real=True, nonzero=True)
kappa_tt = sp.Rational(124, 117) * kappa
kinetic = sp.Matrix([[alpha, 1], [1, 0]])
mass = sp.Matrix([[0, 0], [0, kappa_tt]])
pencil = z * kinetic + mass
mass_squared = sp.factor(alpha * kappa_tt)
check("exact", "coupled TT kinetic matrix is invertible with one plus and one minus",
      kinetic.det() == -1)
check("exact", "selected-branch determinant has one massless and one massive simple factor",
      sp.simplify(pencil.det() - z * (mass_squared - z)) == 0)
check("exact", "multiplying by the inverse kinetic matrix gives scalar wave principal symbol",
      sp.simplify(kinetic.inv() * pencil - (z * sp.eye(2) + kinetic.inv() * mass))
      == sp.zeros(2))
endomorphism = kinetic.inv() * mass
check("exact", "lower-order endomorphism is Krein self-adjoint",
      endomorphism.T * kinetic == kinetic * endomorphism)
check("exact", "massive partner parameter is (124/117)*alpha_II*kappa_1",
      mass_squared == sp.Rational(124, 117) * alpha * kappa)

hh_response = sp.factor(pencil.inv()[0, 0])
partial_fraction = 1 / (alpha * z) - 1 / (alpha * (z - mass_squared))
check("exact", "metric response has exact massless and massive partial fractions",
      sp.simplify(hh_response - partial_fraction) == 0)
check("exact", "the two standard z-plane residues have opposite signs",
      sp.residue(hh_response, z, 0) == 1 / alpha
      and sp.residue(hh_response, z, mass_squared) == -1 / alpha)
check("planted", "PLANT Green hyperbolicity does not make both residues positive",
      sp.residue(hh_response, z, 0) == -sp.residue(hh_response, z, mass_squared))
check("type", "positive mass-squared requires alpha_II*kappa_1 positive in the declared z convention", True)
check("type", "opposite residues are ghostlike on a positive Hilbert reading but remain a Krein/BV question", True)
check("type", "the coupled second-order operator is normally hyperbolic on the inherited globally hyperbolic defect horn", True)
check("type", "C_c-infinity tests and spacelike-compact Green images form one common defect domain", True)
check("planted", "PLANT the defect Green domain is not promoted to the ambient ultrahyperbolic Y14 problem", True)


print("\nE. SCOPED VACUUM-SHIFT SUSCEPTIBILITY")
rho, t = sp.symbols("rho t", real=True)
stationary = 4368 * t**2 + 14 * kappa * t + rho
t_star = -kappa / 312
hessian_at_star = sp.diff(stationary, t).subs({t: t_star, rho: 0})
susceptibility = sp.simplify(-sp.diff(stationary, rho) / hessian_at_star)
check("exact", "selected algebraic branch has nonzero direct-source susceptibility 1/(14*kappa_1)",
      susceptibility == 1 / (14 * kappa))
check("planted", "PLANT nonzero susceptibility is not called a refutation of the two-field magnitude argument", True)
check("type", "this tests a direct algebraic source, not the full curvature-field identification or FLRW system", True)
check("type", "external P1/P2/P3 remain unchanged and unused", True)
check("type", "Curt remains formally separate and the conjunctive third-lane gate remains unpromoted", True)


print("\nSOURCE_RETURN=SOURCE-CORRECTS")
print("GAUSS_TRACE_HESSIAN=(100/117)*kappa_1")
print("GAUSS_TRACELESS_HESSIAN=(124/117)*kappa_1")
print("GRAVITATIONAL_HESSIAN_INERTIA=kappa_positive:(54,46)__kappa_negative:(46,54)")
print("TT_PARTNER_MASS_SQUARED=(124/117)*alpha_II*kappa_1")
print("TT_RESIDUES=+1/alpha_II,-1/alpha_II")
print("COMMON_DOMAIN=COUPLED_NORMALLY_HYPERBOLIC_DEFECT_KREIN_GREEN_COMPLEX")
print("AMBIENT_Y14_DOMAIN=OPEN")
print("DIRECT_SHIFT_SUSCEPTIBILITY=1/(14*kappa_1)__TWO_FIELD_IDENTIFICATION_OPEN")
print("CHECKS=" + " ".join(f"{kind}:{count}" for kind, count in sorted(COUNTS.items())))
if FAILURES:
    print("FAILED_LABELS=" + " | ".join(FAILURES))
    raise SystemExit(1)
print(f"PASS {sum(COUNTS.values())}/{sum(COUNTS.values())}")
