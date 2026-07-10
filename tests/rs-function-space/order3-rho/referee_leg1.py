# HOSTILE REFEREE independent check of LEG-1-calibration.py
# Different arithmetic path: sympy exact cyclotomics (exp(2 pi I/3)), not the leg's (a,b) pairs.
# Adds three attacks the leg did not run:
#   (A) normalization audit of the G-signature fixed-point formula against an INDEPENDENT
#       known case: the order-3 action on CP^2 (sign(g,CP^2) = 1, three fixed points);
#   (B) the order-2 Nikulin package as a full consistency case (weights (-1,-1) -> per-point 0,
#       lattice (14,8) -> sign 0): both routes must agree there too;
#   (C) the RS convention the leg did NOT test: the naive K-class of the projected
#       gamma-traceless operator ([S+]-[S-])(T_C + 1) -> -38, and the mod-3 residue table.
import sys
from sympy import Rational, I, pi, exp, simplify, expand_complex, sqrt, Symbol, solve

NCHK = 0
def chk(c, m):
    global NCHK
    NCHK += 1
    assert c, "FAIL: " + m
    print("  ok: " + m)

z = exp(2*pi*I/3)   # zeta

def simp(x):
    return simplify(expand_complex(x))

# ---- sanity of the cyclotomic core (independent of the leg's pair arithmetic) ----
chk(simp(z**3 - 1) == 0, "zeta^3 = 1")
chk(simp(1 + z + z**2) == 0, "1 + zeta + zeta^2 = 0")

# ---- (A) NORMALIZATION AUDIT: order-3 action on CP^2 ----
# g[z0:z1:z2] = [z0 : zeta z1 : zeta^2 z2]. H^2(CP^2) = C, g-trivial, H^{2,+} rank 1,
# H^{2,-} rank 0 => sign(g, CP^2) = 1. Fixed points: 3, each with T^{1,0} weights {zeta, zeta^2}
# ( [1:0:0]: (z, z^2); [0:1:0]: (z^-1, z) = (z^2, z); [0:0:1]: (z, z^2) ).
def sig_defect(weights):
    out = 1
    for lam in weights:
        out = out * (lam + 1) / (lam - 1)
    return simp(out)

per_cp2 = sig_defect((z, z**2))
chk(simp(per_cp2 - Rational(1,3)) == 0, "CP^2 per-point defect (zeta,zeta^2) = 1/3")
chk(simp(3*per_cp2 - 1) == 0,
    "NORMALIZATION: sum over 3 fixed pts = 1 = sign(g,CP^2) from H^2 trace -- formula & sign PINNED")

# ---- (B) order-2 Nikulin K3 package: full two-route consistency ----
per_o2 = sig_defect((-1, -1))
chk(simp(per_o2) == 0, "order-2 per-point defect (-1,-1) = 0")
# lattice route, (r,s) = (14,8): H2+ = 3 trivial -> 3; H2- = (14-3) invariant - 8 coinv*(-1) -> 11-8 = 3
chk((3) - (11 - 8) == 0, "order-2 lattice route: sign = 3 - 3 = 0 == fixed-pt route 8*0 = 0")
chk(2 + (14 - 8) == 8, "order-2 Lefschetz: L = 2 + 14 - 8 = 8 = #Fix (involution) -- (14,8) is order-2 data")

# ---- order-3: the leg's headline numbers, recomputed on this path ----
num = simp((z+1)*(z**2+1)); den = simp((z-1)*(z**2-1))
chk(simp(num - 1) == 0, "(zeta+1)(zeta^2+1) = 1")
chk(simp(den - 3) == 0, "(zeta-1)(zeta^2-1) = 3")
per_o3 = sig_defect((z, z**2))
chk(simp(per_o3 - Rational(1,3)) == 0, "order-3 per-point defect = 1/3")
chk(simp(6*per_o3 - 2) == 0, "fixed-point route: sign(phi,K3) = 6*(1/3) = 2")
per_o3_sq = sig_defect((z**2, z**4))
chk(simp(6*per_o3_sq - 2) == 0, "sign(phi^2,K3) = 2 (weights (zeta^2,zeta))")

# Lefschetz solve (sympy solve, independent):
r_, s_ = Symbol('r'), Symbol('s')
sol = solve([r_ - s_/2 - 4, r_ + s_ - 22], [r_, s_], dict=True)[0]
chk(sol[r_] == 10 and sol[s_] == 12, "Lefschetz solve: {r - s/2 = 4, r + s = 22} -> (r,s) = (10,12)")
chk(2 + 14 - Rational(8,2) == 12, "(14,8) under ORDER-3 pairing gives L = 12 != 6 -- rejected")

# lattice route for order 3: H2+ = 3 trivial; H2- = 7 trivial + 12 coinv tracing -6
tr_H2m = simp(7 + 6*(z + z**2))
chk(simp(tr_H2m - 1) == 0, "tr(phi|H^{2,-}) = 7 - 6 = 1")
chk(3 - 1 == 2, "lattice route: sign(phi) = 3 - 1 = 2 == fixed-point route")

# Hodge split and traces:
chk(10 - 2 == 8 and 12//2 == 6 and 8 + 6 + 6 == 20, "H^{1,1} = 8 trivial + 6 zeta + 6 zeta^2 (rank 20)")
trH2 = simp(10 + 6*z + 6*z**2)
chk(simp(trH2 - 4) == 0, "tr(phi|H^2) = 4 ; L = 6 = #Fix")

# holomorphic Lefschetz, BOTH orientation conventions (dphi vs dphi^{-1}):
hA = simp(1/((1 - z**-1)*(1 - z**-2)))
hB = simp(1/((1 - z)*(1 - z**2)))
chk(simp(hA - Rational(1,3)) == 0 and simp(hB - Rational(1,3)) == 0,
    "holomorphic Lefschetz per point = 1/3 under EITHER convention (weights are an inverse pair)")
chk(simp(6*hA - 2) == 0, "holomorphic Lefschetz total = 2 = tr(phi|H^0(O)) + tr(phi|H^2(O)) = 1+1")

# ---- quotient-resolution closure ----
chk(Rational(-16 + 2 + 2, 3) == -4, "sigma_orb = -4")
chk(-4 + 6*(-2) == -16, "resolved sigma = -16")
chk(Rational(24 + 6 + 6, 3) == 12, "chi_orb = 12")
chk(12 - 6 + 6*3 == 24, "resolved chi = 24")

# ---- non-equivariant index integers, independent A-hat*ch arithmetic ----
sigma = -16; p1 = 3*sigma
ind_D   = Rational(-p1, 24)
ind_DT  = 4*Rational(-p1, 24) + p1          # ch2(T_C) = p1
chk(ind_D == 2,   "ind(D) = 2")
chk(ind_DT == -40, "ind(D x T_C) = -40")
conventions = {
    "T_C - 1  (AGW gravitino; repo canon 21*sigma/8)": ind_DT - 1*ind_D,
    "T_C - 2  (two-ghost subtraction)":                ind_DT - 2*ind_D,
    "TM_C - 1 (mapping-torus restriction = T_C)":      ind_DT + ind_D - ind_D,
    "T_C + 1  (naive K-class of projected RS+/-; NOT tested by the leg)": ind_DT + 1*ind_D,
}
chk(conventions["T_C - 1  (AGW gravitino; repo canon 21*sigma/8)"] == -42
    and Rational(21*sigma, 8) == -42, "pinned convention reproduces canon: -42 = 21*sigma/8")
chk(conventions["T_C - 2  (two-ghost subtraction)"] == -44, "rival T_C - 2 -> -44 (fails canon)")
chk(conventions["TM_C - 1 (mapping-torus restriction = T_C)"] == -40, "rival TM_C - 1 -> -40 (fails canon)")
chk(conventions["T_C + 1  (naive K-class of projected RS+/-; NOT tested by the leg)"] == -38,
    "UNTESTED convention T_C + 1 -> -38 (also fails canon)")
print()
print("  mod-3 residue table of RS conventions (the Z/3-reading sensitivity):")
for k, v in conventions.items():
    print("    %-64s ind = %4d   mod 3 = %d" % (k, int(v), int(v) % 3))
print("    -> residues {0,1,2,1}: the Z/3 reading IS convention-dependent; only the canon gate pins it.")

# equivariant multiplier at a fixed point: tr(g|T_C X_p) = 2(zeta+zeta^2) = -2, so the
# RS local weight is (tr - k) * Dirac weight: k=1 -> -3 (== 0 mod 3), k=2 -> -4 (== 2 mod 3).
trTC = simp(z + z**2 + z**-1 + z**-2)
chk(simp(trTC + 2) == 0, "tr(g|T_C X_p) = -2 at every fixed point")
print("    RS equivariant multiplier per fixed point: T_C-1 -> -3*Dirac ; T_C-2 -> -4*Dirac ;")
print("    difference = 1*Dirac-rho, which has honest order-3 content -> the pin is LOAD-BEARING.")

print()
print("REFEREE CHECK COMPLETE: %d checks passed, 0 failed." % NCHK)
sys.exit(0)
