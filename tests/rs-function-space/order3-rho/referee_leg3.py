#!/usr/bin/env python3
"""
HOSTILE REFEREE CHECK for LEG-3 (RS rho of the order-3 Nikulin monodromy).
Independent implementation: arithmetic in Q(i*sqrt3) as x + y*s (s^2 = -3), NOT the leg's
a + b*zeta pairs; equivariant indices derived LIFT-FREE via holomorphic Lefschetz (K3 has
K = O trivial, phi acts trivially on K since phi*Omega = Omega), NOT via half-power spin
factors; the mod-Z class derived STRUCTURALLY (rho_k == -(k/3)*ind mod Z), NOT via the
leg's twist-character argument. Also computes the G-SIGNATURE gate the leg script omitted.
Exact Fractions only.
"""
from fractions import Fraction as F

N = 0
def check(c, m):
    global N
    N += 1
    assert c, "REFEREE FAIL: " + m

# ---------- arithmetic: Q(i sqrt 3) as x + y*s, s = i*sqrt(3), s^2 = -3 -------------------
class QS:
    __slots__ = ("x", "y")
    def __init__(self, x=0, y=0):
        self.x, self.y = F(x), F(y)
    @staticmethod
    def co(o): return o if isinstance(o, QS) else QS(o)
    def __add__(s, o): o = QS.co(o); return QS(s.x + o.x, s.y + o.y)
    __radd__ = __add__
    def __neg__(s): return QS(-s.x, -s.y)
    def __sub__(s, o): return s + (-QS.co(o))
    def __rsub__(s, o): return QS.co(o) - s
    def __mul__(s, o):
        o = QS.co(o)
        return QS(s.x * o.x - 3 * s.y * o.y, s.x * o.y + s.y * o.x)
    __rmul__ = __mul__
    def conj(s): return QS(s.x, -s.y)
    def inv(s):
        n = (s * s.conj()).x            # x^2 + 3 y^2
        check(n != 0, "division by zero in QS")
        return QS(s.x / n, -s.y / n)
    def __truediv__(s, o): return s * QS.co(o).inv()
    def __eq__(s, o): o = QS.co(o); return s.x == o.x and s.y == o.y
    def __repr__(s): return "(%s + %s*s)" % (s.x, s.y)

S = QS(0, 1)                              # i*sqrt(3)
ZETA = QS(F(-1, 2), F(1, 2))              # e^{2 pi i/3} = -1/2 + (1/2) i sqrt 3
def zp(e):
    e %= 3
    return QS(1) if e == 0 else (ZETA if e == 1 else ZETA.conj())
check(zp(1) * zp(2) == QS(1), "zeta * zeta^2 = 1")
check(zp(1) + zp(2) == QS(-1), "zeta + zeta^2 = -1")
check(zp(1) * zp(1) == zp(2), "zeta^2 correct in QS rep")

print("== referee arithmetic core OK (independent Q(i sqrt3) representation)")

# ---------- 1. Lefschetz solve + G-SIGNATURE GATE (omitted by the leg script) -------------
# K3: b2 = 22, signature -16 (lattice (3,19)). L(phi) = 2 + tr(phi|H^2) = #Fix = 6.
sols = [(22 - s_, s_) for s_ in range(0, 23, 2) if F(2) + (22 - s_) - F(s_, 2) == 6]
check(sols == [(10, 12)], "Lefschetz forces (r,s) = (10,12)")
r_inv, s_co = sols[0]
# order-2 import (14,8) must fail:
check(2 + 14 - F(8, 2) == 12 and 12 != 6, "(14,8) gives L = 12 != 6: order-2 data rejected")

# G-signature, route A (Atiyah-Singer G-signature theorem, isolated fps on a 4-manifold):
#   sign(g, X) = sum_p prod_j (lam_j + 1)/(lam_j - 1),  lam_j = eigenvalues of dg on T^{1,0}.
lam = [zp(1), zp(2)]
w_sig = (lam[0] + 1) / (lam[0] - 1) * ((lam[1] + 1) / (lam[1] - 1))
sig_fp = QS(6) * w_sig
# route B (Hodge): H^+ = <Omega, conj Omega, invariant Kahler form> all phi-trivial: tr = 3.
#   H^- : dim 19 = (r_inv - 3) trivial + 6 zeta + 6 zeta^2  -> tr = 7 - 6 = 1.
sig_hodge = QS(3) - (QS(r_inv - 3) + QS(6) * zp(1) + QS(6) * zp(2))
check(sig_fp == sig_hodge == QS(2), "G-SIGNATURE GATE: fixed-point route == Hodge route == 2")
print("== G-signature gate (leg omitted it): sign(phi,K3) = 2 by BOTH routes  -- PASSES")

# ---------- 2. LIFT-FREE equivariant indices via holomorphic Lefschetz --------------------
# On a Kahler surface, Dirac = Dolbeault twisted by K^{1/2}; on K3 K^{1/2} = O with TRIVIAL
# phi-action (phi*Omega = Omega pins the square root). Atiyah-Bott holomorphic Lefschetz:
#   ind_phi(D (x) V) = sum_p tr(phi|V_p) * tr(phi|K^{1/2}_p) / det_C(1 - dphi_p^{-1}|T^{1,0})
# NO spin half-power factors are used anywhere in this route.
det_1m = (QS(1) - zp(-1)) * (QS(1) - zp(-2))   # det(1 - dphi^{-1}) on T^{1,0}
check(det_1m == QS(3), "det(1 - dphi^{-1}) = 3 at each fixed point")
ind_D = QS(6) * (QS(1) / det_1m)               # V = O, K^{1/2} = O trivial
check(ind_D == QS(2), "LIFT-FREE: ind_phi(D) = 6 * 1/3 = 2 (== Hodge: h^{0,0}+h^{0,2} trivial)")
# both powers:
det_1m2 = (QS(1) - zp(-2)) * (QS(1) - zp(-4))
check(det_1m2 == QS(3) and QS(6) * (QS(1) / det_1m2) == QS(2), "same for phi^2")
# this independently CONFIRMS the leg's nu_D4 = 1/3 and pins the canonical lift (trivial on ker).

# RS twist: tr(phi|T_C - C) at each fp = (zeta + zeta^2) + (zeta^2 + zeta) - 1 = -3:
c1 = zp(1) + zp(2) + zp(2) + zp(1) - 1
check(c1 == QS(-3), "RS twist character c(g) = -3 (independent rep)")
ind_RS = QS(6) * (c1 / det_1m)
check(ind_RS == QS(-6), "ind_phi(RS) = 6 * (-3)/3 = -6")
print("== lift-free holomorphic-Lefschetz route: ind_phi(D) = 2, ind_phi(RS) = -6  -- CONFIRMED")

# ---------- 3. Kernel data, forced two ways (independent re-derivation) -------------------
# Hodge: ker^-(D x T^{1,0}) = H^1(Theta) ~= H^1(Omega^1) = H^{1,1} (phi-equivariantly, via
# Omega-contraction), split (r_inv - 2) trivial + 6 z + 6 z^2 = 8 + 6 + 6; H^0 = H^2 = 0
# (no vector fields, h^{1,0} = 0). T^{0,1} adds the conjugate rep. Dirac: ker^+ = 2 trivial.
km = {0: 2 * (r_inv - 2), 1: 12, 2: 12}          # theta index p: phase p/3; ker^-(D x T_C)
# RS = (D x T_C) MINUS D, so eta(RS) = eta(DxT_C) - eta(D): the Dirac kernel (2, in ker^+,
# phi-trivial) enters the virtual RS ker^+ with multiplicity -2. (+2 here would ADD eta(D).)
kp = {0: -2, 1: 0, 2: 0}                         # virtual ker^+(RS) = 0 - ker^+(D)
check(km == {0: 16, 1: 12, 2: 12}, "ker^- = 16 trivial + 12 zeta + 12 zeta^2")
# integer forcing, independent sweep:
force = [(m0, m1) for m0 in range(0, 200) for m1 in range(0, 200)
         if -2 - (m0 + 2 * m1) == -42 and -2 - (m0 - m1) == -6]
check(force == [(16, 12)], "multiplicity solve unique on a BIGGER box (200x200): (16,12)")
# non-equivariant gates from sigma only:
sigma = -16; p1 = 3 * sigma
check(F(-sigma, 8) == 2, "ind D = 2")
check(F(5 * p1, 6) == -40, "ind D x T_C = -40")
check(F(5 * p1, 6) - F(-sigma, 8) == -42 == F(21 * sigma, 8), "ind RS = -42 = 21 sigma/8")
print("== kernel data forced (Hodge + independent integer sweep): {16,12,12} minus Dirac {2}")

# ---------- 4. Direct eta + STRUCTURAL mod-Z law (my derivation, not the leg's) -----------
def eta_S1(t):
    t %= 1
    return F(0) if t == 0 else 1 - 2 * t

# eta_S1(x) == x mod Z for x in (1/3)Z: 1 - 2x + 3x - 1 = x ... check exhaustively:
for p in range(3):
    x = F(p, 3)
    check((eta_S1(x) - x) % 1 == 0, "eta_S1(x) == x mod Z on (1/3)Z")

def eta_k(kp, km, k, chir=+1, orient=+1):
    """chir = +1: ker^- gets +eta; orient = +1: holonomy theta + k/3, else theta - k/3."""
    e = F(0)
    for p in range(3):
        arg = F(p, 3) + orient * F(k, 3)
        e += chir * (km[p] - kp[p]) * eta_S1(arg)
    return e

# pinned conventions reproduce the leg exactly:
ETA_RS = [eta_k(kp, km, k) for k in range(3)]
ETA_D = [eta_k({0: 0, 1: 0, 2: 0}, {0: -2, 1: 0, 2: 0}, k) for k in range(3)]
# (Dirac written as virtual ker^- = -2 trivial == ker^+ = +2 trivial; same object)
check(ETA_RS == [F(0), F(2), F(-2)], "RS eta = (0, +2, -2) INDEPENDENTLY REPRODUCED")
check(ETA_D == [F(0), F(-2, 3), F(2, 3)], "Dirac eta = (0, -2/3, +2/3) reproduced")

# STRUCTURAL LAW (referee's own): rho_k = sum +-m_j [eta_S1(th_j + k/3) - eta_S1(th_j)]
#   == sum +-m_j * (k/3)  mod Z  = (k/3)(N_- - N_+) = -(k/3) * ind(fiber op)  mod Z.
# So: class a_k = (-k * ind) mod 3. RS: ind = -42, 3 | 42 -> a_k = 0 (this is ROKHLIN
# resurfacing: 21 sigma/8 == 0 mod 3 for every spin 4-manifold). Dirac: ind = 2 -> a_k = k.
ind_fiber_RS = -42
ind_fiber_D = 2
for k in range(3):
    rho_rs = ETA_RS[k] - ETA_RS[0]
    rho_d = ETA_D[k] - ETA_D[0]
    check((rho_rs - F(-k * ind_fiber_RS, 3)) % 1 == 0, "structural law holds (RS), k=%d" % k)
    check((rho_d - F(-k * ind_fiber_D, 3)) % 1 == 0, "structural law holds (Dirac), k=%d" % k)
    check(int((3 * rho_rs) % 3) == (-k * ind_fiber_RS) % 3 == 0, "RS class 0 = -k*(-42) mod 3")
    check(int((3 * rho_d) % 3) == (-k * ind_fiber_D) % 3 == (-2 * k) % 3, "Dirac class = -2k mod 3")
print("== STRUCTURAL: class a_k = (-k * ind_fiber) mod 3; RS killed because 3 | 42 (Rokhlin),")
print("   Dirac survives because 3 does not divide 2. Independent of the twist-character route.")

# ---------- 5. FULL convention sweep: 2 chir x 2 orient x 3 relabel = 12 variants ----------
def classes(kp, km, chir, orient, relab):
    kp2 = {(p + relab) % 3: kp[p] for p in range(3)}
    km2 = {(p + relab) % 3: km[p] for p in range(3)}
    es = [eta_k(kp2, km2, k, chir, orient) for k in range(3)]
    return sorted(int((3 * (e - es[0])) % 3) for e in es), [e - es[0] for e in es]

flip_found = False
for chir in (+1, -1):
    for orient in (+1, -1):
        for relab in range(3):
            cR, rR = classes(kp, km, chir, orient, relab)
            cD, rD = classes({0: 0, 1: 0, 2: 0}, {0: -2, 1: 0, 2: 0}, chir, orient, relab)
            check(cR == [0, 0, 0], "RS class (0,0,0) under chir=%+d orient=%+d relab=%d" % (chir, orient, relab))
            check(cD == [0, 1, 2], "Dirac class multiset {0,1,2} under chir=%+d orient=%+d relab=%d" % (chir, orient, relab))
            check(all(x.denominator == 1 for x in rR),
                  "RS rho INTEGER in every convention (class 0; exact values are lift-anchored)")
            if relab == 0:
                check(sorted(abs(x) for x in rR) == [0, 2, 2],
                      "with the pinned (unique order-3) lift, RS rho = {0, +-2} for both chir/orient")
            if cR != [0, 0, 0]:
                flip_found = True
check(not flip_found, "NO convention variant flips the RS Z/3 reading")
print("== 12-variant convention sweep: RS rho always INTEGER (class (0,0,0)); with the pinned")
print("   unique order-3 lift the values are {0,+-2}. Dirac always carries the full {0,1,2}")
print("   class multiset. The Z/3 reading is convention-IMMUNE.")

# ---------- 6. h-folding immunity: even the xi = (eta+h)/2 convention cannot make a 1/3 ----
H_RS = [14, 12, 12]        # virtual h as reported
for k in range(3):
    xi_shift = F(H_RS[k] - H_RS[0], 2)          # what folding h/2 would add to rho_k
    check((3 * xi_shift) % 1 == 0 and (xi_shift % 1) in (F(0), F(1, 2)),
          "h-folding adds only half-integers: it can NEVER create a Z/3 part")
print("== h-folding (xi convention) adds half-integers only: Z/3 part immune to that choice too")

# ---------- 7. Donnelly identity re-check in the independent representation ----------------
# eta_g(circle, rotation w) = (1+w)/(1-w); on the product only ker D_4 contributes (Gamma
# pairs +-mu equivariantly). Isotypic: eta_{alpha_k} = (1/3) sum_m zeta^{-km} eta_{g^m}.
for name, KP, KM, ETA in (("RS", kp, km, ETA_RS),
                          ("Dirac", {0: 0, 1: 0, 2: 0}, {0: -2, 1: 0, 2: 0}, ETA_D)):
    for k in range(3):
        tot = QS(0)
        for m in (1, 2):
            w = zp(m)
            icot = (QS(1) + w) / (QS(1) - w)
            trm = QS(0)
            for p in range(3):
                trm = trm + QS(KM[p] - KP[p]) * zp(p * m)
            tot = tot + zp(-k * m) * trm * icot
        avg = QS(tot.x / 3, tot.y / 3)           # * 1/3
        check(avg.y == 0, "%s k=%d isotypic average real" % (name, k))
        check(avg.x == ETA[k], "%s k=%d Donnelly == direct (independent rep)" % (name, k))
print("== Donnelly isotypic identity re-verified in the independent Q(i sqrt3) representation")

# ---------- 8. rival conventions really fail the canon gate ---------------------------------
check(F(5 * p1, 6) - 2 * F(-sigma, 8) == -44 != -42, "T_C - 2C fails canon gate (-44)")
check(F(5 * p1, 6) == -40 != -42, "TM_C - C (restricts to T_C) fails canon gate (-40)")
print("== rivals fail the -42 gate as claimed; only T_C - 1C is admissible")

print()
print("#" * 94)
print("# REFEREE VERDICT: could NOT refute LEG-3. All load-bearing numbers independently")
print("# reproduced (different arithmetic rep, lift-free index route, structural mod-Z law,")
print("# 12-variant convention sweep). The omitted G-signature gate PASSES (2 == 2).")
print("# referee asserts passed: %d" % N)
print("#" * 94)
