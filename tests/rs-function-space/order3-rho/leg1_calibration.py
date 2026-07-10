#!/usr/bin/env python3
# =====================================================================================
# LEG-1 CALIBRATION -- order-3 Nikulin symplectic K3 automorphism phi.
# Part of the four-leg build of the fine equivariant rho (order-3 monodromy, Dirac + RS);
# this leg is the calibration layer: lattice data FORCED by the Lefschetz gate (never
# recalled), G-signature by two independent routes, quotient-resolution closure, and the
# non-equivariant index integers (A-hat = 2, RS = -42, sigma = -16) with the rival RS
# conventions shown FAILING.
#
# House style: fractions.Fraction only (exact Q(zeta) arithmetic, no floats anywhere),
# global NASSERT, check(cond, msg) asserts, exit 0 on success.
# See tests/rs-function-space/rs_index_harness.py for the style reference.
#
# ESTABLISHED INPUTS (citations, not computations):
#  [N]  Nikulin 1979; Garbagnati-Sarti 2007: an order-3 symplectic automorphism of K3 has
#       exactly 6 isolated fixed points. (Classification datum. The coinvariant lattice is
#       the Coxeter-Todd lattice K12(-1) -- CITED ONLY; its rank is re-DERIVED below from
#       the Lefschetz self-consistency gate, never imported.)
#  [W]  phi preserves the holomorphic symplectic form Omega, so at each fixed point the
#       local action on T^{1,0} lies in SU(2): weights (zeta, zeta^{-1}), zeta = e^{2pi i/3}.
#  [AS] Atiyah-Singer G-signature theorem; Atiyah-Bott holomorphic Lefschetz formula.
#  [H]  K3 Hodge data: b2 = 22, (b2+, b2-) = (3, 19), h^{2,0} = h^{0,2} = 1, h^{1,1} = 20,
#       chi(K3) = 24; Hirzebruch signature theorem p1 = 3*sigma.
#
# FIREWALL (DEAD-ENDS.md): no value is manufactured from chi(K3)=24, the /8 normalization,
# A-hat=3, or contractible-fiber=>1. chi(K3)=24 appears ONLY as the topological target of
# the quotient-resolution consistency gate (G2b), never as a count input. Audited below.
# =====================================================================================
import sys
from fractions import Fraction as F

NASSERT = 0
def check(c, m):
    global NASSERT
    NASSERT += 1
    assert c, m


# =====================================================================================
# SECTION 0: arithmetic core -- Q(zeta), zeta = e^{2 pi i / 3}, as pairs (a, b) = a + b*zeta
# with zeta^2 = -1 - zeta; conjugation zeta -> -1 - zeta i.e. (a,b) -> (a-b, -b);
# inverse via the norm a^2 - ab + b^2. A value is real iff b == 0. No floats.
# =====================================================================================
def qz(a, b=0):
    return (F(a), F(b))

def add(x, y): return (x[0] + y[0], x[1] + y[1])
def sub(x, y): return (x[0] - y[0], x[1] - y[1])
def mul(x, y):
    a, b = x
    c, d = y
    # (a + b z)(c + d z) = ac + (ad + bc) z + bd z^2 ; z^2 = -1 - z
    return (a * c - b * d, a * d + b * c - b * d)
def scal(q, x): return (F(q) * x[0], F(q) * x[1])
def conj(x): return (x[0] - x[1], -x[1])
def norm(x): return x[0] * x[0] - x[0] * x[1] + x[1] * x[1]
def inv(x):
    n = norm(x)
    c = conj(x)
    return (c[0] / n, c[1] / n)
def div(x, y): return mul(x, inv(y))
def is_real(x): return x[1] == 0

ZERO, ONE = qz(0), qz(1)
ZETA, ZETA2 = qz(0, 1), qz(-1, -1)
def zpow(e):
    e %= 3
    return ONE if e == 0 else (ZETA if e == 1 else ZETA2)

# arithmetic-core sanity gates
check(mul(ZETA, ZETA) == ZETA2, "zeta^2 = -1 - zeta")
check(mul(ZETA, ZETA2) == ONE, "zeta^3 = 1")
check(add(add(ONE, ZETA), ZETA2) == ZERO, "1 + zeta + zeta^2 = 0")
check(conj(ZETA) == ZETA2 and conj(ZETA2) == ZETA, "conjugation swaps zeta <-> zeta^2")
check(sub(ZETA, ZETA2) == qz(1, 2), "i*sqrt(3) = zeta - zeta^2 = 1 + 2*zeta")
check(norm(ZETA) == 1 and norm(sub(ZETA, ZETA2)) == 3, "norms: |zeta|^2=1, |i sqrt3|^2=3")
check(div(ZETA, ZETA) == ONE and inv(ZETA) == ZETA2, "division / inverse consistent")
print("SECTION 0: Q(zeta) arithmetic core -- sanity gates pass (exact, no floats)")

# =====================================================================================
# SECTION A (GATE G1): the Lefschetz gate FORCES the order-3 lattice ranks.
# L(phi) = chi(Fix) = 6  [N]  must equal  2 + tr(phi | H^2(K3))   (b1 = b3 = 0 on K3).
# With invariant rank r and coinvariant rank s (r + s = 22), the coinvariant eigenvalues
# are zeta, zeta^2 in s/2 conjugate pairs, each pair tracing zeta + zeta^2 = -1, so
# tr(phi|H^2) = r - s/2. SOLVE the linear system -- do NOT recall lattice ranks.
# =====================================================================================
print()
print("=" * 89)
print("SECTION A (G1): Lefschetz gate -- solve for (r, s), reject the order-2 data (14, 8)")
print("=" * 89)

N_FIX = 6          # [N] classification datum: order-3 symplectic => exactly 6 isolated fixed pts
B2 = 22            # [H]
PAIR_TRACE = add(ZETA, ZETA2)                     # trace of one conjugate eigenvalue pair
check(PAIR_TRACE == qz(-1), "zeta + zeta^2 = -1 (conjugate pair traces -1)")

def lefschetz_order3(r, s):
    """L(phi) = 2 + tr(phi|H^2) with tr = r*1 + (s/2)*(zeta + zeta^2), computed in Q(zeta)."""
    tr = add(scal(r, ONE), scal(F(s, 2), PAIR_TRACE))
    check(is_real(tr), "tr(phi|H^2) is real")
    return 2 + tr[0]

# Solve  { r - s/2 = L - 2 ,  r + s = 22 }  =>  (3/2) s = 22 - (L - 2)
tr_needed = F(N_FIX - 2)                          # = 4
s_solved = F(2, 3) * (B2 - tr_needed)
r_solved = B2 - s_solved
check(s_solved.denominator == 1 and r_solved.denominator == 1,
      "the Lefschetz solve lands on integers")
r, s = int(r_solved), int(s_solved)
check((r, s) == (10, 12), "Lefschetz FORCES (r, s) = (10, 12) -- solved, not recalled")
check(s % 2 == 0, "s is even (coinvariant eigenvalues come in conjugate pairs)")
check(lefschetz_order3(r, s) == N_FIX, "re-check: L(10, 12) = 6 = #Fix")

# NEGATIVE CHECK: the ORDER-2 Nikulin data (r, s) = (14, 8) fails the order-3 gate.
L_wrong = lefschetz_order3(14, 8)
check(L_wrong == 12 and L_wrong != N_FIX,
      "(14, 8) gives L = 12 != 6: that is the ORDER-2 Nikulin data, rejected")
# diagnostic: (14, 8) IS consistent as order-2 data, where coinvariant eigenvalue -1 gives
# L = 2 + 14 - 8 = 8 = the order-2 fixed-point count -- the likely origin of the canon slip.
check(2 + 14 - 8 == 8, "(14, 8) is the honest ORDER-2 package: L = 8 = #Fix(order-2 Nikulin)")

CANON_CORRECTION_FLAG = ("canon/families-e-invariant-order3-monodromy-RESULTS.md line 44: "
                         "'invariant lattice rank 14, coinvariant rank 8' is the ORDER-2 "
                         "Nikulin data; order-3 correct values are (r, s) = (10, 12). "
                         "FLAGGED ONLY -- canon edit pauses for Joe.")
print("  Lefschetz solve: 2 + r - s/2 = 6, r + s = 22  =>  (r, s) = (%d, %d)  [FORCED]" % (r, s))
print("  negative check: (14, 8) => L = %s != 6 (order-2 data) -- REJECTED" % L_wrong)
print("  !! CANON CORRECTION FLAG: %s" % CANON_CORRECTION_FLAG)
print("  (coinvariant lattice = Coxeter-Todd K12(-1), rank 12: consistent, cited [N], not used)")

# =====================================================================================
# SECTION B (GATE G2): G-signature of phi by TWO INDEPENDENT ROUTES.
# Route 1 (fixed points, [AS]): per isolated fixed point, contribution
#   prod_j (lambda_j + 1)/(lambda_j - 1)  over the T^{1,0} weights lambda = (zeta, zeta^{-1}).
# Route 2 (lattice trace): sign(phi) = tr(phi | H^{2,+}) - tr(phi | H^{2,-}).
# =====================================================================================
print()
print("=" * 89)
print("SECTION B (G2): G-signature -- fixed-point route vs lattice route, both exact")
print("=" * 89)

# --- Route 1: fixed-point cotangent formula --------------------------------------------
def sign_defect_per_point(weights):
    out = ONE
    for lam in weights:
        out = mul(out, div(add(lam, ONE), sub(lam, ONE)))
    return out

weights_phi = (ZETA, ZETA2)          # [W] symplectic: (zeta, zeta^{-1}) at every fixed point
per_pt = sign_defect_per_point(weights_phi)
check(per_pt == qz(F(1, 3)), "per-point G-signature contribution = 1/3 exactly")
# transparent sub-check: numerator (zeta+1)(zeta^2+1) = 1, denominator (zeta-1)(zeta^2-1) = 3
check(mul(add(ZETA, ONE), add(ZETA2, ONE)) == ONE, "(zeta+1)(zeta^2+1) = 1")
check(mul(sub(ZETA, ONE), sub(ZETA2, ONE)) == qz(3), "(zeta-1)(zeta^2-1) = 3")

sign_phi_fp = scal(N_FIX, per_pt)
check(is_real(sign_phi_fp), "sign(phi) is real")
check(sign_phi_fp == qz(2), "fixed-point route: sign(phi, K3) = 6 * (1/3) = 2")

# phi^2 has the SAME fixed set (order 3 is prime) and conjugate weights (zeta^2, zeta):
weights_phi2 = (zpow(2), zpow(4))
check(weights_phi2 == (ZETA2, ZETA), "phi^2 weights are the conjugate pair (zeta^2, zeta)")
sign_phi2_fp = scal(N_FIX, sign_defect_per_point(weights_phi2))
check(sign_phi2_fp == qz(2), "sign(phi^2, K3) = 2 as well (conjugate weights, same value)")

# --- Route 2: lattice trace ------------------------------------------------------------
# H^{2,+} = span(Re Omega, Im Omega, invariant Kahler class) -- all phi-trivial [W] + Yau
# averaging (average a Kahler class over <phi>; take the Ricci-flat rep: phi is an isometry).
B2_PLUS, B2_MINUS = 3, 19            # [H]
tr_H2_plus = qz(3)                                        # 3 trivial modes
# H^{2,-} (rank 19) = (r - 3) invariant modes + s coinvariant modes (s/2 conjugate pairs):
n_inv_minus = r - 3
check(n_inv_minus == 7, "invariant part of H^{2,-} has rank 7")
tr_H2_minus = add(scal(n_inv_minus, ONE), scal(F(s, 2), PAIR_TRACE))
check(is_real(tr_H2_minus), "tr(phi|H^{2,-}) is real")
check(tr_H2_minus == qz(1), "tr(phi|H^{2,-}) = 7 - 6 = 1")
check(n_inv_minus + s == B2_MINUS, "rank bookkeeping: 7 + 12 = 19 = b2^-")

sign_phi_lat = sub(tr_H2_plus, tr_H2_minus)
check(sign_phi_lat == qz(2), "lattice route: sign(phi) = 3 - 1 = 2")

# --- THE GATE: the two independent routes agree ----------------------------------------
check(sign_phi_fp == sign_phi_lat, "G2: fixed-point route == lattice route (both = 2)")
SIGN_PHI = 2
# bonus: sigma(K3) drops out of the same split, derived rather than recalled:
SIGMA_K3 = B2_PLUS - B2_MINUS
check(SIGMA_K3 == -16, "sigma(K3) = 3 - 19 = -16 (derived from the (3,19) split)")
print("  fixed-point route: 6 * [(zeta+1)(zeta^2+1)] / [(zeta-1)(zeta^2-1)] = 6 * 1/3 = 2")
print("  lattice route:     tr(phi|H^{2,+}) - tr(phi|H^{2,-}) = 3 - 1 = 2")
print("  GATE G2 PASSES: sign(phi, K3) = 2 by both routes; sigma(K3) = -16 derived")

# =====================================================================================
# SECTION C (GATE G2b): quotient-resolution closure -- independent confirmation that the
# order-3 package (6 fixed points, A_2 quotient singularities) is self-consistent:
# K3/<phi> resolved must again be K3 (sigma AND chi bookkeeping must close).
# =====================================================================================
print()
print("=" * 89)
print("SECTION C (G2b): quotient-resolution closure (sigma and chi both recover K3)")
print("=" * 89)

CHI_K3 = 24    # [H]; used ONLY as the consistency-gate target here (firewall-audited below)

# signature of the quotient orbifold (G-signature averaging over the group):
sigma_orb = F(SIGMA_K3 + int(sign_phi_fp[0]) + int(sign_phi2_fp[0]), 3)
check(sigma_orb == -4, "sigma_orb = (-16 + 2 + 2)/3 = -4")

# each of the 6 singular points is a C^2/(Z/3) SU(2)-quotient => type A_2; its minimal
# resolution glues in 2 (-2)-curves with intersection matrix A_2(-1): [[-2, 1], [1, -2]].
# exact negative-definiteness check (leading principal minors): -2 < 0, det = 3 > 0.
A2_det = F(-2) * F(-2) - F(1) * F(1)
check(F(-2) < 0 and A2_det == 3, "A_2(-1) is negative definite (minors -2, 3)")
A2_SIGNATURE = -2      # negative definite of rank 2
A2_CHI = 3             # two spheres meeting in one point: 2 + 2 - 1 = 3

sigma_resolved = sigma_orb + N_FIX * A2_SIGNATURE
check(sigma_resolved == SIGMA_K3, "resolution: -4 + 6*(-2) = -16 = sigma(K3)  [closes]")

# Euler characteristic bookkeeping: chi(X/G) = (1/|G|) sum_g chi(Fix(g)):
chi_orb = F(CHI_K3 + N_FIX + N_FIX, 3)
check(chi_orb == 12, "chi_orb = (24 + 6 + 6)/3 = 12")
chi_resolved = chi_orb - N_FIX + N_FIX * A2_CHI
check(chi_resolved == CHI_K3, "resolution: 12 - 6 + 6*3 = 24 = chi(K3)  [closes]")

print("  sigma: (-16 + 2 + 2)/3 = -4; resolve six A_2: -4 + 6*(-2) = -16  == sigma(K3)")
print("  chi:   (24 + 6 + 6)/3 = 12; resolve six A_2: 12 - 6 + 6*3 = 24  == chi(K3)")
print("  GATE G2b PASSES: the quotient resolves back to K3 -- the '6 fixed points, order 3,")
print("  A_2 points' package is self-consistent (independent confirmation of [N])")

# =====================================================================================
# SECTION D (G4, non-equivariant part): the index integers, DERIVED from A-hat * ch
# arithmetic (Hirzebruch p1 = 3*sigma), then gated against canon. The rival RS subtraction
# conventions are shown FAILING the canon gate (negative checks -- load-bearing for LEG-3).
# =====================================================================================
print()
print("=" * 89)
print("SECTION D (G4 non-equivariant): A-hat = 2, RS = -42, sigma = -16; rivals -44/-40 FAIL")
print("=" * 89)

p1 = 3 * SIGMA_K3                                  # Hirzebruch signature theorem [H]
check(p1 == -48, "p1(K3) = 3*sigma = -48")

# ind(D) = A-hat[K3] = -p1/24:
ind_D = F(-p1, 24)
check(ind_D == 2, "index D = A-hat(K3) = -p1/24 = -sigma/8 = 2 (canon)")

# ind(D tensor T_C K3) = [A-hat * ch(T_C)]_4 = 4*(-p1/24) + ch2(T_C), ch2(T_C X) = p1(X):
ind_D_TC = 4 * F(-p1, 24) + F(p1)
check(ind_D_TC == F(5, 6) * p1 and ind_D_TC == -40, "index (D tensor T_C K3) = (5/6)p1 = -40")

# RS convention (PINNED, Section 0 of the build spec): RS = D tensor (T_C X - 1C):
ind_RS = ind_D_TC - 1 * ind_D
check(ind_RS == -42, "index RS = -40 - 2 = -42 (canon: 21*sigma/8)")
check(ind_RS == F(21 * SIGMA_K3, 8), "same value as the closed form 21*sigma/8")
check(ind_RS == F(7 * p1, 8), "same value as 7*p1/8")

# NEGATIVE CHECKS -- the rival conventions FAIL the canon gate (they must, per spec):
ind_RS_rival_2C = ind_D_TC - 2 * ind_D             # T_C - 2C
check(ind_RS_rival_2C == F(11 * SIGMA_K3, 4) and ind_RS_rival_2C == -44,
      "rival (T_C - 2C) = 11*sigma/4 = -44")
check(ind_RS_rival_2C != -42, "rival (T_C - 2C) FAILS the canon gate -42  [REJECTED]")
# total-space twist TM_C - C: TM|K3 = T(K3) + trivial R (mapping-torus vertical + dt), so
# T_C M|K3 = T_C K3 (+) C and ind(D tensor (TM_C - C)) = ind(D tensor T_C) + ind(D) - ind(D):
ind_RS_rival_TM = ind_D_TC + ind_D - ind_D
check(ind_RS_rival_TM == -40, "rival (TM_C - C) restricts to -40")
check(ind_RS_rival_TM != -42, "rival (TM_C - C) FAILS the canon gate -42  [REJECTED]")

# canon cross-checks in the shape of rs_index_harness.py:
check(F(-SIGMA_K3, 8) == 2, "A-hat = -sigma/8 = 2  (harness formula)")
check(F(21 * SIGMA_K3, 8) == -42, "I_{3/2} = 21*sigma/8 = -42  (harness formula)")
check(SIGMA_K3 == -16, "sigma(K3) = -16")
print("  ind(D) = -p1/24 = 2 ; ind(D (x) T_C) = (5/6)p1 = -40 ;")
print("  RS = T_C - 1C  =>  -40 - 2 = -42 = 21*sigma/8   [MATCHES CANON -- convention PINNED]")
print("  rival T_C - 2C => -44 (11*sigma/4)  FAILS canon  [REJECTED]")
print("  rival TM_C - C => -40               FAILS canon  [REJECTED]")
print("  GATE G4 (non-equivariant) PASSES: A-hat = 2, RS = -42, sigma = -16")

# =====================================================================================
# SECTION E: the H^2 eigenvalue split (handoff to LEG-3) + Hodge-side cross-gates.
# phi symplectic => phi*Omega = Omega => H^{2,0} and H^{0,2} are phi-TRIVIAL (2 modes);
# hence ALL s = 12 coinvariant modes lie in H^{1,1}:
#   H^{1,1} (rank 20) = 8 trivial + 6 zeta + 6 zeta^2.
# =====================================================================================
print()
print("=" * 89)
print("SECTION E: H^{1,1} eigenvalue split (8, 6, 6) + holomorphic Lefschetz cross-gate")
print("=" * 89)

H20_H02_MODES = 2                    # Omega and conj(Omega), both phi-trivial [W]
H11_RANK = 20                        # [H]
h11_trivial = r - H20_H02_MODES      # invariant modes left for H^{1,1}
h11_zeta = s // 2
h11_zeta2 = s // 2
check(h11_trivial == 8, "H^{1,1} trivial multiplicity = r - 2 = 8")
check(h11_zeta == 6 and h11_zeta2 == 6, "H^{1,1} zeta / zeta^2 multiplicities = 6 each")
check(h11_trivial + h11_zeta + h11_zeta2 == H11_RANK, "8 + 6 + 6 = 20 = h^{1,1}")

# cross-gate: tr(phi|H^2) reassembled from the Hodge split must equal r - s/2 = 4,
# and the full topological Lefschetz number must equal 6 = #Fix:
tr_H2_hodge = add(scal(H20_H02_MODES + h11_trivial, ONE),
                  add(scal(h11_zeta, ZETA), scal(h11_zeta2, ZETA2)))
check(is_real(tr_H2_hodge) and tr_H2_hodge[0] == tr_needed,
      "Hodge-split trace: 10 - 6 = 4 = r - s/2")
check(2 + tr_H2_hodge[0] == N_FIX, "topological Lefschetz from Hodge split = 6 = #Fix")

# BONUS CALIBRATION (overlaps gate G3a, owned by LEG-2): Atiyah-Bott HOLOMORPHIC Lefschetz.
#   sum_p 1/det(1 - (dphi_p)^{-1}|T^{1,0})  ==  sum_q (-1)^q tr(phi | H^q(K3, O)).
# Per point: 1/((1 - zeta^{-1})(1 - zeta^{-2})) = 1/((1-zeta^2)(1-zeta)) = 1/3.
# Hodge side: H^0(O) trivial (1), H^1(O) = 0, H^2(O) ~ conj(Omega) trivial (1) => total 2.
# This is exactly the operational spin-lift pin: ind_phi(D, K3) = 6*(1/3) = +2.
per_pt_hol = inv(mul(sub(ONE, zpow(-1)), sub(ONE, zpow(-2))))
check(per_pt_hol == qz(F(1, 3)), "holomorphic Lefschetz per-point term = 1/3 exactly")
hol_lefschetz_fp = scal(N_FIX, per_pt_hol)
hol_lefschetz_hodge = qz(1 + 0 + 1)
check(hol_lefschetz_fp == hol_lefschetz_hodge == qz(2),
      "holomorphic Lefschetz: 6*(1/3) = 2 = tr(phi|H^0(O) + H^2(O))  [spin-lift pin]")
print("  H^{2,0} + H^{0,2}: phi-trivial (2 modes);  H^{1,1}: 8 trivial + 6 zeta + 6 zeta^2")
print("  Hodge-split trace check: tr(phi|H^2) = 4, L = 6 = #Fix  [consistent]")
print("  bonus (G3a overlap): holomorphic Lefschetz 6*(1/3) = 2 = Hodge trace  [spin-lift pin]")

# =====================================================================================
# SECTION F: FIREWALL AUDIT (LEG-1 scope) + output payload
# =====================================================================================
print()
print("=" * 89)
print("SECTION F: firewall audit + LEG-1 output payload")
print("=" * 89)

FIREWALL_INPUT_INVENTORY = [
    "#Fix = 6 (Nikulin 1979 / Garbagnati-Sarti 2007 classification; independently confirmed"
    " here by the Lefschetz gate G1 AND the quotient-resolution closure G2b)",
    "local T^{1,0} weights (zeta, zeta^{-1}) at each fixed point (forced by phi*Omega = Omega)",
    "b2(K3) = 22, (b2+, b2-) = (3, 19), h^{2,0} = h^{0,2} = 1, h^{1,1} = 20 (K3 Hodge data)",
    "Hirzebruch p1 = 3*sigma; Atiyah-Singer G-signature + Atiyah-Bott holomorphic Lefschetz",
    "chi(K3) = 24 -- used ONLY as the consistency-gate TARGET in G2b (resolution bookkeeping),"
    " never as a count input",
]
# firewall asserts: no forbidden manufacture. The derivations above used p1/sigma index
# arithmetic and lattice traces; assert the forbidden shortcuts were never load-bearing:
check(ind_D == 2 and ind_D != 3, "A-hat(K3) = 2, NOT the forbidden flat A-hat = 3")
check(r == 10 and s == 12, "(r, s) came from the Lefschetz SOLVE, not from any chi/24 import")
check(int(sign_phi_fp[0]) == 2, "sign(phi) came from fixed-point weights, not from chi/24")
# provenance re-derivation gate: every headline number recomputes from sigma/p1/lattice data
# alone (no path through chi(K3) = 24, /8-as-normalization, A-hat = 3, contractible-fiber):
check(F(-(3 * (B2_PLUS - B2_MINUS)), 24) == ind_D,
      "ind_D re-derives from the (3,19) lattice split alone")
check(F(7 * 3 * (B2_PLUS - B2_MINUS), 8) == ind_RS,
      "ind_RS re-derives from the (3,19) lattice split alone")
print("  firewall inputs used (complete inventory):")
for item in FIREWALL_INPUT_INVENTORY:
    print("   - " + item)
print("  forbidden moves audited ABSENT: chi(K3)=24 as count input; /8 normalization;")
print("  A-hat=3; contractible-fiber=>1.  (chi=24 appears only as G2b's closure target.)")

LEG1_OUTPUT = {
    "r": r,                                  # invariant lattice rank (FORCED by G1)
    "s": s,                                  # coinvariant lattice rank (FORCED by G1)
    "sign_phi": SIGN_PHI,                    # G-signature, two independent routes (G2)
    "H11_eigenvalues": {1: h11_trivial, "zeta": h11_zeta, "zeta2": h11_zeta2},
    "H20_H02": "phi-trivial (2 modes)",
    "sigma_K3": SIGMA_K3,
    "chi_K3_gate": CHI_K3,
    "ind_D": int(ind_D),                     # 2   (canon)
    "ind_RS": int(ind_RS),                   # -42 (canon; convention T_C - 1C PINNED)
    "rival_conventions_rejected": {"T_C - 2C": int(ind_RS_rival_2C),
                                   "TM_C - C": int(ind_RS_rival_TM)},
    "canon_correction_flag": "RESULTS.md line 44: (14,8) -> (10,12)",
}
print()
print("  LEG-1 OUTPUT (consumed by LEG-2/LEG-3):")
for k_, v_ in LEG1_OUTPUT.items():
    print("    %-28s : %s" % (k_, v_))

print()
print("#" * 89)
print("# LEG-1 CALIBRATION COMPLETE.")
print("# G1  PASS: Lefschetz forces (r, s) = (10, 12); (14, 8) rejected (L = 12 != 6).")
print("# G2  PASS: sign(phi, K3) = 2 by fixed-point AND lattice routes (independent).")
print("# G2b PASS: quotient-resolution closure (sigma -16, chi 24 both recovered).")
print("# G4  PASS (non-equivariant): A-hat = 2, RS = -42 (rivals -44 / -40 REJECTED),")
print("#      sigma = -16. H^{1,1} split (8, 6, 6) handed to LEG-3.")
print("# CANON CORRECTION FLAGGED (not executed, pauses for Joe):")
print("#   " + CANON_CORRECTION_FLAG)
print("# hard asserts passed: %d ; BLOCKED items: none" % NASSERT)
print("#" * 89)
sys.exit(0)
