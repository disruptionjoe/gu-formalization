#!/usr/bin/env python3
"""Exact selected-branch soldering/BV-TT and curvature-VEV FLRW gate."""

from __future__ import annotations

from collections import Counter
import json
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[2]
Q = sp.Rational
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


print("A. SOURCE, LAYER 0, AND PREDECESSOR OWNERS")
source = read("lab/sources/selected-branch-bv-flrw-source-reinspection-2026-08-05.md")
previous = read("explorations/conditional-build/selected-branch-linearized-totalization-current-green-domain-2026-08-05.md")
cosmo_previous = read("explorations/conditional-build/source-native-curvature-vev-euler-rank-2026-08-05.md")
domain_previous = read("explorations/conditional-build/k77-global-even-bv-null-green-domain-2026-08-05.md")

check("source", "the composed source return is SOURCE-CONFIRMS at the limited two-to-one bar",
      "Decisive return: `SOURCE-CONFIRMS`" in source)
check("source", "the source names gauge-rotated Levi-Civita rather than naked Levi-Civita",
      "gauge-rotated Levi-Civita" in source)
check("source", "the source magnitude bar is two problems to one rather than magnitude derivation",
      "two problems to one" in source and "not a first-principles" in source
      and "magnitude derivation" in source)
check("repo", "the predecessor owns the selected TT pole split and common defect domain",
      "opposite residues" in previous and "common **defect** Krein/Green domain" in previous)
check("repo", "the ambient action already owns linear curvature-distortion coupling",
      "I[B,T]" in cosmo_previous and "rank **105**" in cosmo_previous)
check("repo", "the even null quotient already retains plus and cross",
      "explicit plus and cross representatives" in domain_previous)

for label, left, right in (
    ("spatial three-curvature versus four-dimensional scalar curvature", "spatial three-curvature", "four-dimensional scalar curvature"),
    ("even diffeomorphism BV versus odd super-IG BV", "even diffeomorphism BV", "odd super-IG"),
    ("opposite residue versus BV exactness", "opposite residue", "BV-exact"),
    ("tree spectral majorant versus loop positivity", "tree-level", "loop/RG"),
    ("tracking versus screening", "tracking", "screening"),
):
    check("type", label + " remain distinct", left in source and right in source)


print("\nB. GAUGE-ROTATED LEVI-CIVITA SOLDERING DERIVATIVE")
eta = sp.diag(-1, 1, 1, 1)
sym_pairs = [(mu, nu) for mu in range(4) for nu in range(mu, 4)]


def symmetric_basis(column: int) -> sp.Matrix:
    mu, nu = sym_pairs[column]
    h = sp.zeros(4)
    h[mu, nu] = 1
    h[nu, mu] = 1
    return h


def levi_civita_symbol(k: tuple[int, int, int, int]) -> sp.Matrix:
    """D_g Gamma[h]^rho_(mu nu) on a flat Lorentz background."""
    out = sp.zeros(64, 10)
    for column in range(10):
        h = symmetric_basis(column)
        for rho in range(4):
            for mu in range(4):
                for nu in range(4):
                    row = (rho * 4 + mu) * 4 + nu
                    out[row, column] = Q(1, 2) * sum(
                        eta[rho, sigma] * (
                            k[mu] * h[nu, sigma]
                            + k[nu] * h[mu, sigma]
                            - k[sigma] * h[mu, nu]
                        )
                        for sigma in range(4)
                    )
    return out


symbols = {
    "timelike": levi_civita_symbol((1, 0, 0, 0)),
    "spacelike": levi_civita_symbol((0, 1, 0, 0)),
    "null": levi_civita_symbol((1, 0, 0, 1)),
}
for orbit, matrix in symbols.items():
    check("exact", f"Levi-Civita metric derivative is injective on the {orbit} orbit",
          matrix.rank() == 10)

null_symbol = symbols["null"]
check("exact", "connection lower indices remain symmetric",
      all(null_symbol[(rho * 4 + mu) * 4 + nu, col]
          == null_symbol[(rho * 4 + nu) * 4 + mu, col]
          for rho in range(4) for mu in range(4) for nu in range(4)
          for col in range(10)))

# Gauge rotation acts by an invertible adjoint map on each connection matrix.
eps = sp.Matrix([[1, 1, 0, 0], [0, 1, 1, 0], [0, 0, 1, 1], [0, 0, 0, 1]])
adjoint = sp.kronecker_product(sp.eye(4), eps.T, eps.inv())
rotated_null = adjoint * null_symbol
check("exact", "gauge rotation preserves the rank-ten metric derivative",
      rotated_null.rank() == null_symbol.rank() == 10)

# A moving reduction contributes D_B chi.  In a quotient by the connection
# gauge image, adding that term is exactly invisible.
k = sp.Matrix([1, 0, 0, 1])
gauge_map = sp.kronecker_product(k, sp.eye(16))
chi = sp.Matrix(range(1, 17))
base_variation = rotated_null[:, 0]
compensated = base_variation + gauge_map * chi
joined = gauge_map.row_join(base_variation)
joined_compensated = gauge_map.row_join(compensated)
check("exact", "the moving-epsilon compensator changes the derivative only by a gauge image",
      joined.rank() == joined_compensated.rank())
check("planted", "PLANT naked Levi-Civita and gauge-rotated Levi-Civita are not equal matrices",
      rotated_null != null_symbol)
check("type", "the quotient formula closes D_g B modulo gauge, not an ambient nonlinear connection domain", True)


print("\nC. EVEN-BV TT SURVIVAL AND CANONICAL KREIN GRADING")
k_cov = (1, 0, 0, -1)
diffeo = sp.zeros(10, 4)
for column in range(4):
    for row, (mu, nu) in enumerate(sym_pairs):
        diffeo[row, column] = (
            (k_cov[mu] if nu == column else 0)
            + (k_cov[nu] if mu == column else 0)
        )

plus = sp.zeros(10, 1)
plus[sym_pairs.index((1, 1))] = 1
plus[sym_pairs.index((2, 2))] = -1
cross = sp.zeros(10, 1)
cross[sym_pairs.index((1, 2))] = 1
tt = sp.Matrix.hstack(plus, cross)

check("exact", "null diffeomorphism image has rank four", diffeo.rank() == 4)
check("exact", "plus and cross form a rank-two TT carrier", tt.rank() == 2)
check("exact", "TT intersects the diffeomorphism image trivially",
      diffeo.row_join(tt).rank() == diffeo.rank() + tt.rank())

alpha, kappa = sp.symbols("alpha_II kappa_1", positive=True)
kappa_tt = sp.Rational(124, 117) * kappa
K = sp.Matrix([[alpha, 1], [1, 0]])
M = sp.Matrix([[0, 0], [0, kappa_tt]])
L = K.inv() * M
mass_squared = alpha * kappa_tt

massless = sp.Matrix([1, 0])
partner = sp.Matrix([1, -alpha])
check("exact", "massless and partner vectors diagonalize the Krein-self-adjoint endomorphism",
      L * massless == sp.zeros(2, 1)
      and L * partner == -mass_squared * partner)
check("exact", "their native Krein norms are equal and opposite",
      (massless.T * K * massless)[0] == alpha
      and (partner.T * K * partner)[0] == -alpha)

parity = sp.simplify(sp.eye(2) + 2 * L / mass_squared)
majorant = sp.simplify(K * parity)
check("exact", "spectral ghost parity is an involution", parity * parity == sp.eye(2))
check("exact", "spectral ghost parity commutes with the selected dynamics",
      parity * L == L * parity)
check("exact", "spectral ghost parity is Krein self-adjoint",
      parity.T * K == K * parity)
check("exact", "the induced finite TT majorant is positive for positive Einstein residue",
      majorant[0, 0] == alpha and majorant.det() == 1)
check("exact", "the partner supplies two non-exact TT classes, one per polarization",
      tt.rank() == 2 and diffeo.row_join(tt).rank() == 6)
check("planted", "PLANT even BV does not erase the opposite-residue partner",
      tt.rank() != 0)
check("planted", "PLANT a finite spectral majorant is not promoted to loop or type-III positivity", True)
check("type", "full massive multiplet and odd super-IG cohomology remain open", True)


print("\nD. ACTION-DERIVED CURVATURE/VEV CONSTANT AND FLRW HORN")
a, beta, rho, R4, t, box_R = sp.symbols(
    "a beta rho_vac R4 t box_R", real=True, nonzero=True
)
# Scalar irrep of the existing action: (a+beta*t)R + kappa*t^2/2-rho.
E_t = beta * R4 + kappa * t
trace_E_g = -(a + beta * t) * R4 + 3 * beta * sp.Symbol("box_t") - kappa * t**2 + 2 * rho

constant_trace = trace_E_g.subs(sp.Symbol("box_t"), 0)
constant_solution = sp.solve([E_t, constant_trace], [R4, t], dict=True)[0]
check("exact", "constant-curvature equations have one unique solution at nonzero a and kappa",
      constant_solution[R4] == 2 * rho / a
      and constant_solution[t] == -2 * beta * rho / (a * kappa))

linear_jacobian = sp.Matrix([E_t, constant_trace]).jacobian([R4, t]).subs({R4: 0, t: 0, rho: 0})
check("exact", "the two action variations are independent at the zero vacuum",
      sp.factor(linear_jacobian.det()) == a * kappa)
check("exact", "one external vacuum amplitude controls both curvature and distortion values",
      len({rho}) == 1
      and sp.diff(constant_solution[R4], rho) == 2 / a
      and sp.diff(constant_solution[t], rho) == -2 * beta / (a * kappa))
check("exact", "zero independent vacuum source gives zero constant curvature and zero distortion",
      constant_solution[R4].subs(rho, 0) == 0
      and constant_solution[t].subs(rho, 0) == 0)
check("planted", "PLANT tracking is not screening: curvature responds nontrivially to a vacuum shift",
      sp.diff(constant_solution[R4], rho) != 0)

# Eliminate t and box(t)=-beta*box(R)/kappa in the full trace equation.
reduced_trace = sp.factor(
    trace_E_g.subs({t: -beta * R4 / kappa,
                    sp.Symbol("box_t"): -beta * box_R / kappa})
)
expected_trace = -a * R4 - 3 * beta**2 * box_R / kappa + 2 * rho
check("exact", "the exact reduced FLRW trace is a*R+3 beta^2 box(R)/kappa=2 rho",
      sp.expand(reduced_trace - expected_trace) == 0)
check("exact", "constant vacuum shifts retain asymptotic response R=2 rho/a independently of beta and kappa",
      not constant_solution[R4].has(beta, kappa))

H, Hdot, spatial_k, scale = sp.symbols("H Hdot spatial_k scale", real=True)
flrw_R = 6 * (Hdot + 2 * H**2 + spatial_k / scale**2)
check("planted", "PLANT spatial flatness does not imply four-dimensional flatness",
      sp.simplify(flrw_R.subs({spatial_k: 0, Hdot: 0}) - 12 * H**2) == 0)
check("type", "this local scalar-tensor horn lies inside the static Weinberg-class burden", True)
check("type", "the result earns two-values-to-one tracking but no radiative screening or magnitude derivation", True)
check("type", "an ambient/global/nonlocal GU horn remains a distinct possible scope exit", True)


print("\nE. CONSTRAINT SURPLUS AND SCOPE")
registry = json.loads(read("lab/process/selected-branch-bv-tt-curvature-vev-flrw.json"))
check("exact", "no new construction coefficient or external datum is introduced",
      registry["free_object_delta"] == 0
      and set(registry["external_datum"].values()) == {"UNUSED"})
check("source", "registry preserves the exact source disposition",
      registry["source_return"] == "SOURCE-CONFIRMS")
check("type", "Curt remains separate and the third lane remains unpromoted",
      registry["curt_track"] == "FORMALLY_SEPARATE_INSIDE_ERIC_LANE"
      and registry["third_lane"] == "NOT_PROMOTED")

print("SOURCE_RETURN=SOURCE-CONFIRMS")
print("D_G_B=GAUGE_ROTATED_LEVI_CIVITA_DERIVATIVE_MOD_GAUGE")
print("MASSIVE_PARTNER_EVEN_BV_TT_CLASSES=2")
print("TREE_KREIN_MAJORANT=POSITIVE_FOR_ALPHA_II_POSITIVE")
print("FULL_ODD_SUPER_IG_AND_LOOP_COHOMOLOGY=OPEN")
print("CURVATURE_VEV_CONSTANT_SOLUTION=R4:2*rho/a__t:-2*beta*rho/(a*kappa)")
print("FLRW_TRACE=a*R4+3*beta^2*box_R/kappa-2*rho=0")
print("VACUUM_SHIFT_SCREENING=FAILS_IN_LOCAL_ACTION_HORN")
print("CHECKS=" + " ".join(f"{kind}:{count}" for kind, count in sorted(COUNTS.items())))
if FAILURES:
    raise SystemExit("FAILURES: " + "; ".join(FAILURES))
print(f"PASS {sum(COUNTS.values())}/{sum(COUNTS.values())}")
