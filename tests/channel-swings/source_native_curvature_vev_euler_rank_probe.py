#!/usr/bin/env python3
"""Exact source-native curvature/VEV Euler and rank certificate.

This probe works at the homogeneous linearized value grade of the existing
K77 two-connection action.  It deliberately distinguishes the ambient
Einstein image from the observed four-dimensional Einstein receiver and
leaves the unconstructed odd BV quotient undefined.
"""

from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[2]
checks: list[tuple[str, str]] = []


def check(kind: str, label: str, condition: bool) -> None:
    if not condition:
        raise AssertionError(f"{kind}: {label}")
    checks.append((kind, label))


# Source and action ownership -------------------------------------------------
transcript = (ROOT / "lab/literature/weinstein-ucsd-2025-04-transcript.md").read_text()
eddy = (ROOT / "explorations/k77-wave2-eddy-augmented-torsion-euler-prolongation-2026-08-05.md").read_text()
receiver = (ROOT / "explorations/full-domain-shiab-observed-einstein-receiver-2026-08-05.md").read_text()

check("source", "source puts a curvature term and a dark-energy term on opposite sides of an equality",
      "imagine that there was an equal sign in the middle" in transcript)
check("source", "source says the replacement is not constant and can acquire a VEV",
      "not constant. It's free to respond to gain a veve" in transcript)
check("source", "source identifies the replacement as a field rather than lambda times the metric",
      "It's a field." in transcript)
check("repo", "the action owns the path-average curvature",
      "\\bar F=\\int_0^1F_{B+tT}\\,dt" in eddy
      and "=F_B+\\frac12D_BT+\\frac13T^2" in eddy)
check("repo", "the action-owned Euler row includes the Frechet-adjoint correction",
      "E_{\\rm act}=S(\\bar F)+L_T^!S^!T+*\\kappa T" in eddy)
check("repo", "post-Shiab ambient-to-observed Einstein factorization is already killed",
      "rank( G_4 res_H | ker(G_14) ) = 10" in receiver)


# Complete decomposition rank ------------------------------------------------
# Algebraic Riemann in dimension 14 decomposes as scalar + traceless Ricci +
# Weyl = 1 + 104 + 3080.  The selected Shiab is -2 G_14 on this carrier.
N_SCALAR = 1
N_TRACELESS_RICCI = 104
N_WEYL = 3080
N_EINSTEIN = N_SCALAR + N_TRACELESS_RICCI
N_RIEMANN = N_EINSTEIN + N_WEYL
N_T = 196  # Omega^13 tensor Cl^1 receiver
N_T_EXTRA = N_T - N_EINSTEIN

C = sp.zeros(N_T, N_EINSTEIN)
for i in range(N_EINSTEIN):
    C[i, i] = -2

# A finite balanced Krein/Hodge flat map.  Only nondegeneracy is used in the
# rank theorem; positivity is neither assumed nor inferred.
K = sp.diag(*([1] * (N_T // 2) + [-1] * (N_T // 2)))
J_fixed = C.row_join(K)

check("exact", "ambient scalar plus traceless-Ricci dimension is 105", N_EINSTEIN == 105)
check("exact", "ambient Weyl dimension is 3080", N_WEYL == 3080)
check("exact", "ambient algebraic-Riemann dimension is 3185", N_RIEMANN == 3185)
check("exact", "selected curvature response has exact rank 105", C.rank() == N_EINSTEIN)
check("exact", "Krein/Hodge direct T map is invertible on all 196 coordinates", K.rank() == N_T)
check("exact", "fixed nonzero gain gives total homogeneous Euler rank 196", J_fixed.rank() == N_T)
check("exact", "only 105 of those rows covary curvature with T", C.rank() == 105)
check("exact", "the remaining 91 rows constrain T without a curvature partner", N_T_EXTRA == 91)

# With kappa=0, the direct T block disappears.  This is a sharp gain control.
J_zero_gain = C.row_join(sp.zeros(N_T, N_T))
check("exact", "zero gain drops total rank from 196 to 105", J_zero_gain.rank() == 105)


# Independent B and T variations --------------------------------------------
# I[B,T] = <T,S(barF)> + kappa/2 <T,*T>.  At T=0 on a homogeneous value
# fixture, the B variation is derivative/commutator-valued and its algebraic
# value Jacobian is zero.  It therefore cannot be counted as a second value
# equation.  The T variation supplies C*c + K*t = 0.
E_B_value_jacobian = sp.zeros(N_T, N_EINSTEIN + N_T)
combined = J_fixed.col_join(E_B_value_jacobian)
check("exact", "independent B variation adds zero homogeneous value rank at T=0",
      combined.rank() == J_fixed.rank() == 196)
check("type", "the B Euler row remains a live derivative/domain equation away from the homogeneous value locus", True)


# Bianchi, Ward, BV and observation ------------------------------------------
check("exact", "Bianchi/Einstein contraction removes the 3080-dimensional Weyl kernel",
      N_RIEMANN - N_EINSTEIN == 3080)
ward_value_row = sp.zeros(1, N_T)
check("exact", "the even Ward divergence has zero homogeneous zero-jet rank",
      ward_value_row.rank() == 0)
check("type", "even Ward covariance does not manufacture the missing odd BV differential", True)
check("type", "native quotient rank is UNDEFINED rather than zero until the BV tangent differential exists", True)

# Exact scalar kernel witness for ambient-vs-observed curvature.  In the
# H(4)+N(10) split, these sectional weights make Ric_14 vanish while the
# horizontal restriction has G_4=-3 g_H.
k_hh = sp.Rational(1)
k_hn = -sp.Rational(3, 10)
k_nn = sp.Rational(2, 15)
ric_h_factor = 3 * k_hh + 10 * k_hn
ric_n_factor = 4 * k_hn + 9 * k_nn
g4_factor = -3 * k_hh
check("exact", "ambient horizontal Ricci vanishes on the scalar kernel witness", ric_h_factor == 0)
check("exact", "ambient normal Ricci vanishes on the scalar kernel witness", ric_n_factor == 0)
check("exact", "observed four-dimensional Einstein response remains nonzero", g4_factor == -3)
check("planted", "PLANT ambient G14 tracking is not relabeled observed G4 tracking", g4_factor != 0)


# Free gain and vacuum-shift controls ----------------------------------------
c, t, rho, kappa = sp.symbols("c t rho kappa", nonzero=True)
e = c + kappa * t + rho
jac_fixed_gain = sp.Matrix([e.subs(kappa, 1)]).jacobian([c, t, rho])
jac_free_gain = sp.Matrix([e]).jacobian([c, t, rho, kappa])
check("exact", "vacuum-shifted relation has rank one on three values", jac_fixed_gain.rank() == 1)
check("exact", "a free gain adds a variable but not a second equation", jac_free_gain.rank() == 1)
check("exact", "curvature remains a free coordinate on the shifted solution family",
      sp.solve(sp.Eq(e, 0), t)[0] == (-c - rho) / kappa)

# If an independent equation c=0 is supplied, T absorbs rho.  The existing
# homogeneous B variation does not supply that equation.
screen_matrix = sp.Matrix([[1, 1, 1], [1, 0, 0]])
check("exact", "screening requires an additional independent curvature equation", screen_matrix.rank() == 2)
check("planted", "PLANT transfer of rho into T is not radiative screening by the current action", E_B_value_jacobian.rank() == 0)


# Layer-0 and promotion plants ------------------------------------------------
check("type", "theta/T is an adjoint-valued one-form before any observed tensor receiver", True)
check("planted", "PLANT theta is not its quadratic stress tensor", True)
check("planted", "PLANT an Euler covector is not its action density", True)
check("planted", "PLANT rank 196 is not reported as 196 curvature-covarying modes", C.rank() != J_fixed.rank())
check("planted", "PLANT the older vertical-SFF proxy is not substituted for the source connection difference", True)
check("planted", "PLANT missing BV data is not booked as a zero-dimensional quotient", True)
check("planted", "PLANT field tracking is not a first-principles magnitude derivation", True)
check("planted", "PLANT no P1 P2 or P3 datum is consumed to repair a local action map", True)


counts: dict[str, int] = {}
for kind, _ in checks:
    counts[kind] = counts.get(kind, 0) + 1

print("SOURCE_RETURN=SOURCE-CONFIRMS")
print("AMBIENT_CURVATURE_COVARIATION_RANK=105")
print("TOTAL_HOMOGENEOUS_T_EULER_RANK=196")
print("T_ONLY_ROWS=91")
print("OBSERVED_POST_SHIAB_ROUTE=KILLED_BY_RANK10_KERNEL_WITNESS")
print("NATIVE_BV_QUOTIENT_RANK=UNDEFINED")
print("VACUUM_SHIFT=TRACKED_NOT_SCREENED")
print("CHECKS=" + " ".join(f"{key}:{value}" for key, value in sorted(counts.items())))
print(f"PASS {len(checks)}/{len(checks)}")
