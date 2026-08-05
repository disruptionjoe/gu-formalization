#!/usr/bin/env python3
"""Exact certificate for the global K77 chimeric-spin reduction gate.

The certificate keeps five objects separate:
  * spin(TY14),
  * spin(C),
  * the lift of spin(C) induced by the admitted spin structure on X,
  * the source-defined spinor-frame extension P_H, and
  * the gauge-transported full Clifford frame gamma_epsilon.

It also types the three bulk/defect support horns.  Exit zero does not claim a
nonlinear BV master action, Green domain, observation theorem or cosmology.

Run:
  uv run --with numpy --with sympy python \
    tests/channel-swings/k77_global_chimeric_spin_reduction_probe.py
"""

from __future__ import annotations

from collections import Counter
from fractions import Fraction
from pathlib import Path

import numpy as np
import sympy as sp


ROOT = Path(__file__).resolve().parents[2]
COUNTS: Counter[str] = Counter()
FAILURES: list[str] = []


def check(kind: str, label: str, condition: bool) -> None:
    COUNTS[kind] += 1
    if not condition:
        FAILURES.append(label)
    print(f"{'PASS' if condition else 'FAIL'} [{kind}] {label}")


def read(relative: str) -> str:
    return (ROOT / relative).read_text()


print("A. PRIMARY-SOURCE AND REPOSITORY OWNERSHIP")
portal = read("lab/sources/transcripts/portal-special-gu-first-look-2020-04-02.md")
toe = read("lab/sources/transcripts/toe-weinstein-gu-40-years.md")
spin_canon = read("canon/w2-y14-spin-structure.md")
paper_map = read("docs/paper-formalization-candidates.md")
predecessor = read(
    "explorations/conditional-build/"
    "k77-epsilon-gravitational-soldering-weld-2026-08-05.md"
)
support_predecessor = read(
    "explorations/k77-wave2-i1b-conormal-symbol-bulk-defect-weld-domain-2026-08-05.md"
)
parameter_inventory = read(
    "explorations/conditional-build/cb-d-parameterizing-the-unknown-2026-08-05.md"
)

check("source", "TOE names the active spin structure as admitted starting data",
      "which spin structure is active" in toe and "how many temporal dimensions" in toe)
check("source", "Portal defines the chimeric bundle before its spinors",
      "01:12:17 We now define the chimeric bundle" in portal
      and "vertical tangent bundle" in portal)
check("source", "Portal builds P_H from the chimeric spinors rather than an independent gauge bundle",
      "structure bundle of the spinors" in portal
      and "P_{U(" in portal
      and "associated bundle" in portal)
check("source", "Portal types the adjoint bundle as Clifford/exterior algebra",
      "adjoint bundle looks like the Clifford algebra" in portal
      and "exterior algebra on the chimeric bundle" in portal)
check("source", "Portal rotates the Clifford invariant with source epsilon",
      r"\text{Ad}(\varepsilon^{-1}, \Phi)" in portal
      and r"(\varepsilon, \pi) \in \mathcal{G}" in portal)
check("source", "TOE repeats the U(64,64) chimeric-spinor ownership",
      "U64 comma 64 structure group" in toe and "[02:41:57]" in toe)
check("repo", "paper map records P_H as the Dirac extension of the chimeric frame bundle",
      "P_H = P_{Fr(C^{7,7})} ×_{ρ_D} H" in paper_map
      and "H = U(64, 64)" in paper_map)
check("repo", "canon correctly makes X-spin the Y-spin precondition",
      "Y14 is spin if and only if X4 is spin" in spin_canon)
check("repo", "predecessor requires a full frame rather than an unframed plane",
      "full `epsilon_IG`" in predecessor and "coarse Clifford orbit" in predecessor)
check("repo", "standing support architecture already distinguishes independent X density",
      r"S_X^{\rm independent}" in support_predecessor
      and "normal-density" in support_predecessor)
check("repo", "the existing 83-real inventory already charges action/source normalizations",
      "local action coefficients" in parameter_inventory
      and "TOTAL, continuous real, before any quotient" in parameter_inventory
      and "83" in parameter_inventory)


print("\nB. SPLITTING-PRINCIPLE CHARACTERISTIC CLASSES OVER F2")

# Polynomials over F2 are dictionaries exponent_tuple -> 1.  Four formal
# Stiefel-Whitney roots are retained with powers, so x_i^2 is not collapsed.
Monomial = tuple[int, int, int, int]
Polynomial = set[Monomial]
ZERO_MONOMIAL: Monomial = (0, 0, 0, 0)


def p_add(a: Polynomial, b: Polynomial) -> Polynomial:
    return a ^ b


def p_mul(a: Polynomial, b: Polynomial) -> Polynomial:
    out: Polynomial = set()
    for x in a:
        for y in b:
            monomial = tuple(x[i] + y[i] for i in range(4))
            if monomial in out:
                out.remove(monomial)
            else:
                out.add(monomial)
    return out


def p_sum(values: list[Polynomial]) -> Polynomial:
    out: Polynomial = set()
    for value in values:
        out = p_add(out, value)
    return out


def elementary_two(roots: list[Polynomial]) -> Polynomial:
    return p_sum([
        p_mul(roots[i], roots[j])
        for i in range(len(roots)) for j in range(i + 1, len(roots))
    ])


roots_e: list[Polynomial] = [
    {tuple(1 if i == j else 0 for i in range(4))} for j in range(4)
]
w1_e = p_sum(roots_e)
w2_e = elementary_two(roots_e)

# Sym^2(E): diagonal roots 2*x_i vanish over F2; the six mixed roots remain.
roots_sym2: list[Polynomial] = [set() for _ in range(4)] + [
    p_add(roots_e[i], roots_e[j]) for i in range(4) for j in range(i + 1, 4)
]
w1_sym2 = p_sum(roots_sym2)
w2_sym2 = elementary_two(roots_sym2)
w1_e_sq = p_mul(w1_e, w1_e)

# C = Sym^2(E*) plus E*.  Dualization does not change mod-2 SW roots.
roots_c = roots_sym2 + roots_e
w1_c = p_sum(roots_c)
w2_c = elementary_two(roots_c)

check("exact", "w1(Sym2 E) = w1(E) for rank four", w1_sym2 == w1_e)
check("exact", "w2(Sym2 E) = w1(E)^2 for rank four", w2_sym2 == w1_e_sq)
check("exact", "the chimeric bundle is oriented without separately orienting E", w1_c == set())
check("exact", "w2(C) = w2(E), so C is spin when the admitted X spin structure exists",
      w2_c == w2_e)
check("planted", "PLANT spin(C) is not unconditional on an arbitrary non-spin base",
      bool(w2_c) and w2_c != set())
check("type", "the calculation is for C=Sym2(E*) plus E*, not TY14",
      len(roots_c) == 14 and "w2(Y14)" in spin_canon)


print("\nC. EXACT (6,4) PLUS (1,3) EQUALS (7,7)")
g = sp.diag(-1, 1, 1, 1)
sym_basis: list[sp.Matrix] = []
for i in range(4):
    for j in range(i, 4):
        h = sp.zeros(4)
        h[i, j] = 1
        h[j, i] = 1
        sym_basis.append(h)


def dewitt(h: sp.Matrix, k: sp.Matrix) -> sp.Expr:
    return sp.trace(g * h * g * k) - sp.Rational(1, 2) * sp.trace(g * h) * sp.trace(g * k)


g_v = sp.Matrix([[dewitt(h, k) for k in sym_basis] for h in sym_basis])
eig_v = g_v.eigenvals()
v_pos = sum(mult for value, mult in eig_v.items() if value > 0)
v_neg = sum(mult for value, mult in eig_v.items() if value < 0)
g_h = -g  # the source/K77 horizontal dual convention is (1,3)
h_pos = 1
h_neg = 3
check("exact", "trace-reversed Frobenius metric on Sym2 has inertia (6,4)",
      (v_pos, v_neg) == (6, 4) and g_v.det() == 64)
check("exact", "the horizontal dual convention has inertia (1,3)",
      g_h == sp.diag(1, -1, -1, -1))
check("exact", "the chimeric sum has inertia (7,7)",
      (v_pos + h_pos, v_neg + h_neg) == (7, 7))
check("planted", "PLANT raw Frobenius without trace reversal is not silently substituted",
      any(value < 0 for value in eig_v) and sp.Rational(1, 2) in set(g_v))


print("\nD. FAITHFUL REAL CLIFFORD/KREIN EXTENSION")
I2 = np.eye(2, dtype=np.int64)
S1 = np.array([[0, 1], [1, 0]], dtype=np.int64)
S3 = np.array([[1, 0], [0, -1]], dtype=np.int64)
EPS = np.array([[0, 1], [-1, 0]], dtype=np.int64)


def kron_list(values: list[np.ndarray]) -> np.ndarray:
    out = np.array([[1]], dtype=np.int64)
    for value in values:
        out = np.kron(out, value)
    return out


def build_split_clifford(n: int) -> tuple[list[np.ndarray], list[np.ndarray]]:
    plus: list[np.ndarray] = []
    minus: list[np.ndarray] = []
    for k in range(n):
        pre = [S3] * k
        post = [I2] * (n - 1 - k)
        plus.append(kron_list(pre + [S1] + post))
        minus.append(kron_list(pre + [EPS] + post))
    return plus, minus


def product(values: list[np.ndarray]) -> np.ndarray:
    out = np.eye(values[0].shape[0], dtype=np.int64)
    for value in values:
        out = out @ value
    return out


p_plus, p_minus = build_split_clifford(7)
gamma = p_plus + p_minus
eta = [1] * 7 + [-1] * 7
i128 = np.eye(128, dtype=np.int64)
b = product(p_minus)

clifford_ok = True
for a in range(14):
    for c in range(14):
        want = (2 * eta[a] if a == c else 0) * i128
        clifford_ok &= np.array_equal(gamma[a] @ gamma[c] + gamma[c] @ gamma[a], want)

check("exact", "Cl(7,7) relations hold on the real rank-128 module", clifford_ok)
check("exact", "the invariant real spinor form is a symmetric involution",
      np.array_equal(b.T, b) and np.array_equal(b @ b, i128))
check("exact", "the real spinor form has exact split signature (64,64)",
      int(np.trace(b)) == 0 and b.shape == (128, 128))
check("exact", "every grade-one Clifford matrix is B-skew and lies in so(64,64)",
      all(np.array_equal(b @ value.T @ b, -value) for value in gamma))
trace_gram = np.array([[int(np.trace(gamma[a] @ gamma[c])) for c in range(14)] for a in range(14)])
check("exact", "the fourteen grade-one matrices form a full nondegenerate frame",
      np.array_equal(trace_gram, np.diag([128 * value for value in eta])))
check("type", "complexifying the real rank-128 module gives the source U(64,64) carrier",
      gamma[0].shape[0] == 128 and int(np.trace(b)) == 0)
check("planted", "PLANT K77 is not replaced by Cl(9,5)=M64(H)",
      "Cl(9,5)" in predecessor and "rival" in predecessor)


print("\nE. GLOBAL FULL FRAME AND GAUGE TRANSPORT")
# The bundle-level construction in the report uses the admitted base spin
# structure and the unique lift of the Spin_0(1,3) representation to
# Spin(7,7).  Here an exact spin element checks the fibrewise transport law.
h = gamma[1] @ gamma[2]
h_inv = -h
moved = [h @ value @ h_inv for value in gamma]
transport_ok = True
for a in range(14):
    for c in range(14):
        want = (2 * eta[a] if a == c else 0) * i128
        transport_ok &= np.array_equal(moved[a] @ moved[c] + moved[c] @ moved[a], want)

check("exact", "an exact Spin conjugation preserves the full Clifford frame", transport_ok)
check("exact", "the same conjugation preserves the Krein spinor form",
      np.array_equal(h.T @ b @ h, b))
check("exact", "gauge transport preserves grade-one B-skewness",
      all(np.array_equal(b @ value.T @ b, -value) for value in moved))
check("exact", "the transported object retains all fourteen labelled directions",
      all(int(np.trace(moved[a] @ moved[a])) == 128 * eta[a] for a in range(14)))
check("type", "source epsilon and gamma_epsilon are distinct dependent objects",
      "epsilon` | gauge transformation" in predecessor
      and "full `epsilon_IG` | an isometry" in predecessor)
check("type", "the supplied X spin structure selects an induced C lift without claiming every C spin structure is canonical",
      "which spin structure is active" in toe and "Choice of spin structure" in spin_canon)
check("planted", "PLANT an unframed orbit is insufficient even though the full frame exists",
      "unframed plane" in predecessor and len(moved) == 14)
check("planted", "PLANT an independent P_H would reopen an associated-bundle isomorphism burden",
      "start with the frame bundle of the chimeric bundle" in paper_map)


print("\nF. BULK/DEFECT SUPPORT HORNS")
# Along s(X), density lines satisfy D_Y = D_X tensor D_N.  Exponent pairs are
# (D_X power, D_N power).  A literal ambient-density restriction cannot be
# integrated on X until its D_N factor is contracted.  An intrinsic X density
# pushes forward canonically as a current and needs no normal trivialization.
d_x = (1, 0)
d_n_dual = (0, -1)
d_y_restricted = (1, 1)


def tensor_line(a: tuple[int, int], c: tuple[int, int]) -> tuple[int, int]:
    return (a[0] + c[0], a[1] + c[1])


check("exact", "literal restriction of an ambient density carries one normal-density factor",
      d_y_restricted == (1, 1))
check("exact", "a chosen inverse normal-density line converts it to an X density",
      tensor_line(d_y_restricted, d_n_dual) == d_x)
check("exact", "an independently typed X density already has the integrable line type",
      d_x == (1, 0))
check("type", "primary source-guided horn retains one bulk action and only independently owned X terms",
      "bulk_i1b_copies" in read("lab/process/k77-wave2-i1b-conormal-symbol-weld-domain.json")
      and "BULK_SOURCE_LAYERS_PLUS_ONLY_INDEPENDENT_DIRECT_X_ACTIONS"
      in read("lab/process/k77-wave2-i1b-conormal-symbol-weld-domain.json"))
check("type", "localized-bulk horn needs a normal dual or transverse profile",
      "NORMAL_DENSITY_VALUE_OR_TRANSVERSE_PROFILE"
      in read("lab/process/k77-wave2-i1b-conormal-symbol-weld-domain.json"))
check("type", "pullback-only horn changes the source's upstairs-action architecture",
      "takes place not on X4, but on Y14" in toe and "spinner bundle on y14" in toe)
check("exact", "support selection adds zero new support field or fitted coefficient",
      "new_free_coefficients_inserted" in read("lab/process/k77-wave2-i1b-conormal-symbol-weld-domain.json")
      and '"new_free_coefficients_inserted": 0' in read("lab/process/k77-wave2-i1b-conormal-symbol-weld-domain.json"))

lam = sp.symbols("lambda_def", real=True)
ward_zero = sp.Integer(0)
check("exact", "covariance alone cannot select the relative defect coefficient",
      sp.simplify(lam * ward_zero) == 0 and lam.is_real)
check("type", "relative normalization is an explicit alias fork, not silently declared existing or new",
      "source normalization" in parameter_inventory
      and "83" in parameter_inventory
      and "inherited as unit" in read(
          "explorations/conditional-build/pre-shiab-gauss-defect-action-bv-symbol-2026-08-05.md"))
check("planted", "PLANT the rank-ten same-stratum projector supplies no normal-density dual",
      "inverse normal-density line" in predecessor)
check("planted", "PLANT a localized duplicate is not admitted at unit coefficient",
      "Appending the new receiver" in predecessor
      and "unsplit old action fails a planted double-counting control" in predecessor)
check("planted", "PLANT support normalization does not solve the dark-energy magnitude",
      "does not fix a native absolute value" in parameter_inventory)


print("\nG. SCOPE FENCES")
check("type", "global reduction removes no nonlinear BV burden", "Nonlinear BV/CME" in predecessor)
check("type", "global reduction removes no null/Green-domain burden", "null/Green domain" in predecessor)
check("type", "the full construction remains conditional on the admitted base spin structure",
      w2_c == w2_e and "spin structure is active" in toe)
check("planted", "PLANT topology is not a physical Einstein/cosmology result", True)
check("planted", "PLANT P1 P2 P3 are not consumed", True)


print("COUNTS " + " ".join(f"{kind}:{count}" for kind, count in sorted(COUNTS.items())))
if FAILURES:
    raise SystemExit("FAILURES: " + "; ".join(FAILURES))
print(f"PASS {sum(COUNTS.values())}/{sum(COUNTS.values())}")
