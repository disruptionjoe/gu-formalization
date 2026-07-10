#!/usr/bin/env python3
# -*- coding: ascii -*-
"""
LEG-2: DIRAC RHO -- fine equivariant (spectral) rho of the order-3 Nikulin monodromy,
spin-1/2 Dirac operator (baseline/calibration leg of the order-3 rho build).

OBJECT. phi = order-3 Nikulin symplectic automorphism of K3: exactly 6 isolated fixed
points (Nikulin 1979; Garbagnati-Sarti 2007), local T^{1,0} weights (zeta, zeta^{-1})
at each fixed point (forced by phi*Omega = Omega), zeta = e^{2 pi i/3}. Average the
Kahler class over <phi> and take Yau's Ricci-flat metric in the invariant class: phi is
an isometry. Mapping torus T_phi = (K3 x S^1)/(Z/3) (free), product metric dt^2 + g_K3,
flat Z/3 characters alpha_k(loop) = zeta^k. THE INVARIANT (eta level, APS I-III):
    rho_k := eta_{alpha_k}(T_phi, D) - eta_{alpha_0}(T_phi, D),   k = 0, 1, 2,
h-terms (kernel dims) reported separately, NEVER folded into rho.

PINNED CONVENTIONS (Section 0 of the build spec; deviations are build failures):
  - Q(zeta) as pairs (a, b) of Fractions = a + b*zeta, zeta^2 = -1 - zeta,
    conj: (a,b) -> (a-b, -b); i*sqrt(3) = zeta - zeta^2 = 1 + 2*zeta;
    i*cot(pi/3) = (zeta - zeta^2)/3; i*cot(2*pi/3) = -(zeta - zeta^2)/3. NO floats.
  - Spin lift: order 3 is odd => the lift of the Z/3-action to the Spin structure is
    UNIQUE (torsor over Hom(Z/3, Z/2) = 0). Canonical symplectic lift: S^+ weights
    (1, 1) (trivial on the 2 parallel spinors), S^- weights (zeta, zeta^2); half
    powers taken inside mu_3 via lambda^{1/2} := lambda^2. Pinned OPERATIONALLY by
    ind_phi(D, K3) = +2 = tr(phi | H^{0,0} + H^{2,0}). Character-twisted variants
    (lift x zeta^m) are enumerated and reported below: they are NOT spin lifts, and
    they only relabel k -> k+m.
  - S^1 factor: PERIODIC (non-bounding) spin structure -- the momenta implemented
    below are 2*pi*(Z + theta + k/3). [CORRECTED LABEL 2026-07-10: the original
    docstring said "bounding (antiperiodic)"; the adversarial referee showed the
    implementation is the periodic structure. Values under the genuinely bounding
    structure are eta = rho = (0, +4/3, -4/3), h = (0,0,0) -- differing by exact
    even integers; the mod-Z classes (0,1,2)/3 and the Z3_NONZERO verdict are
    IDENTICAL either way. The disk route (cross-check B) computes the bounding
    structure, which is why its values (4/3, -4/3) agree exactly there, with
    implied ind_g(APS) = 0.] Circle unit eta (APS I):
    eta_S1(theta) = 1 - 2*{theta} for {theta} in (0,1), = 0 at theta = 0.
  - Orientation dt ^ vol_K3; MASTER SIGN: fiber kernel modes in ker^- contribute
    +eta_S1, modes in ker^+ contribute -eta_S1.

ESTABLISHED FORMULAS USED (citations):
  - Atiyah-Bott / Atiyah-Singer G-index fixed point formula (Atiyah-Bott, Ann. Math.
    86 (1967) & 88 (1968); Atiyah-Singer III).
  - APS I-III (Math. Proc. Camb. Phil. Soc. 1975-76): eta, rho_alpha = eta_alpha - eta_0.
  - Donnelly, "Eta invariants for G-spaces" (Indiana Univ. Math. J. 27 (1978)):
    equivariant eta from fixed-point data; isotypic averaging over a free quotient.
  - Nikulin 1979 / Garbagnati-Sarti 2007: order-3 symplectic K3 automorphism has
    exactly 6 isolated fixed points, local weights (zeta, zeta^{-1}).
FIREWALL (DEAD-ENDS.md): nothing here is manufactured from chi(K3)=24, the /8
normalization, A-hat=3, or contractible-fiber=>1. Input inventory printed and audited.
"""

from fractions import Fraction as F

NASSERT = 0
def check(c, m):
    global NASSERT
    NASSERT += 1
    assert c, m


# =====================================================================================
# SECTION 0: exact arithmetic in Q(zeta), zeta = e^{2 pi i / 3}
# =====================================================================================
class QZ:                                   # element a + b*zeta of Q(zeta)
    __slots__ = ("a", "b")
    def __init__(self, a=0, b=0):
        self.a, self.b = F(a), F(b)
    @staticmethod
    def _co(o):
        return o if isinstance(o, QZ) else QZ(o)
    def __add__(s, o):
        o = QZ._co(o); return QZ(s.a + o.a, s.b + o.b)
    __radd__ = __add__
    def __neg__(s): return QZ(-s.a, -s.b)
    def __sub__(s, o): return s + (-QZ._co(o))
    def __rsub__(s, o): return QZ._co(o) - s
    def __mul__(s, o):
        o = QZ._co(o)                       # (a+bz)(c+dz) = ac-bd + (ad+bc-bd) z ; z^2 = -1-z
        a, b, c, d = s.a, s.b, o.a, o.b
        return QZ(a * c - b * d, a * d + b * c - b * d)
    __rmul__ = __mul__
    def conj(s):                            # zeta -> zeta^2 = -1 - zeta
        return QZ(s.a - s.b, -s.b)
    def inv(s):
        n = s * s.conj()                    # norm a^2 - ab + b^2, rational
        check(n.b == 0 and n.a != 0, "QZ.inv: norm rational nonzero")
        return QZ(s.conj().a / n.a, s.conj().b / n.a)
    def __truediv__(s, o): return s * QZ._co(o).inv()
    def __eq__(s, o):
        o = QZ._co(o); return s.a == o.a and s.b == o.b
    def __repr__(s): return "(%s + %s z)" % (s.a, s.b)

ONE = QZ(1)
Z1  = QZ(0, 1)                              # zeta
def zp(k):                                  # zeta^k
    k %= 3
    return ONE if k == 0 else (Z1 if k == 1 else Z1 * Z1)

# Section-0 self-tests of the arithmetic core
check(zp(1) * zp(1) == QZ(-1, -1), "zeta^2 = -1 - zeta")
check(zp(1) * zp(2) == ONE,        "zeta * zeta^2 = 1")
check(zp(1) + zp(2) == QZ(-1),     "zeta + zeta^2 = -1")
check(zp(1).conj() == zp(2),       "conjugation zeta -> zeta^2")
ISQRT3 = zp(1) - zp(2)                      # i*sqrt(3)
check(ISQRT3 == QZ(1, 2),          "i sqrt3 = zeta - zeta^2 = 1 + 2 zeta")
check(ISQRT3 * ISQRT3 == QZ(-3),   "(i sqrt3)^2 = -3")
ICOT = {1: ISQRT3 / 3, 2: QZ(0) - ISQRT3 / 3}   # i*cot(pi m/3), m = 1, 2
check(ICOT[1] == QZ(F(1, 3), F(2, 3)), "i cot(pi/3) = (zeta - zeta^2)/3")
check(ICOT[2] == ICOT[1].conj(),       "i cot(2pi/3) = conj(i cot(pi/3))")

def half(e):                                # (zeta^e)^{1/2} := zeta^{2e}  (inside mu_3)
    return zp(2 * e)
def sfac(e):                                # lambda^{1/2} - lambda^{-1/2}, lambda = zeta^e
    return half(e) - half(-e)

def eta_S1(th):                             # APS I circle eta: 1 - 2{theta}, 0 at theta = 0
    t = th - (th // 1)
    return F(0) if t == 0 else 1 - 2 * t

def class_mod_Z(rho):                       # rho mod Z as a in {0,1,2}, rho == a/3 mod Z
    fr = rho - (rho // 1)
    a = 3 * fr
    check(a.denominator == 1, "rho mod Z lands in (1/3)Z/Z (|G| = 3 caps denominators)")
    return int(a) % 3

def is_even_int(x):
    return x.denominator == 1 and x.numerator % 2 == 0


print("=" * 92)
print("LEG-2: fine equivariant DIRAC rho of the order-3 Nikulin monodromy (spin-1/2 baseline)")
print("=" * 92)

# =====================================================================================
# INPUT INVENTORY + FIREWALL AUDIT (local to this leg; LEG-4 owns the consolidated audit)
# =====================================================================================
N_FIX      = 6                # Nikulin 1979 / Garbagnati-Sarti 2007 (classification datum)
W_T10      = (1, -1)          # local weights zeta^{+1}, zeta^{-1} on T^{1,0} (phi*Omega = Omega)
KER_PLUS_D = 2                # ker D^+ = H^0(O) + H^{2,0}(O): the 2 parallel spinors, phi-trivial
KER_MIN_D  = 0                # ker D^- = H^{0,1}(O) = 0 on K3
SIGMA_K3   = -16              # signature of K3 (calibration input for the non-equivariant gate)
H2_RANK    = 22
print("input inventory: #Fix = %d (Nikulin class'n), T^{1,0} weights zeta^{%+d}, zeta^{%+d}," %
      (N_FIX, W_T10[0], W_T10[1]))
print("                 Dirac kernel (Hodge): ker^+ = %d phi-trivial, ker^- = %d; sigma(K3) = %d"
      % (KER_PLUS_D, KER_MIN_D, SIGMA_K3))
# firewall: none of the forbidden manufactured inputs appears in the load-bearing set
load_bearing = {N_FIX, W_T10[0], W_T10[1], KER_PLUS_D, KER_MIN_D, SIGMA_K3, H2_RANK}
check(24 not in load_bearing, "FIREWALL: chi(K3) = 24 is NOT an input to this leg")
check(3 not in load_bearing,  "FIREWALL: no 'A-hat = 3' constant among inputs (3 enters only as |G|)")
print("firewall: 24 never used; no /8 normalization manufactured (the only /8 is the standard")
print("          Atiyah-Singer A-hat = -sigma/8, used as a calibration GATE, not an input count)")

# --- input hygiene: recompute LEG-1's Lefschetz gate (validates the '6' against H^2 rep theory)
# L(phi) = #Fix = 2 + tr(phi|H^2); tr = r - s/2 with invariant rank r, coinvariant rank s, r+s=22
sols = [(22 - s, s) for s in range(0, 23) if 2 + (22 - s) - F(s, 2) == N_FIX]
check(sols == [(10, 12)], "Lefschetz forces (r, s) = (10, 12), uniquely")
check(2 + 14 - F(8, 2) == 12 != 6, "NEGATIVE: order-2 Nikulin data (14, 8) gives L = 12 != 6")
print("input hygiene: Lefschetz gate forces (r, s) = (10, 12); (14, 8) [= the RESULTS.md line-44")
print("               order-2 import -- flag owned by LEG-1] is REJECTED (L = 12 != 6)")

# =====================================================================================
# SPIN LIFT: uniqueness + operational pin + the full admissible-lift enumeration
# =====================================================================================
print()
print("-" * 92)
print("SPIN LIFT: uniqueness (odd order), operational pin, all admissible character twists")
print("-" * 92)
# Genuine spin lifts of the Z/3-action form a torsor over Hom(Z/3, Z/2); |Hom| = gcd(3,2) = 1.
from math import gcd
check(gcd(3, 2) == 1, "Hom(Z/3, Z/2) = 0: the order-3 spin lift is UNIQUE (odd order)")

# Local Dirac weight at a fixed point, TWO independent derivations (canonical lift):
#   (i)  half-power route:  nu = 1 / [ (l^{1/2}-l^{-1/2}) (l^{-1/2}-l^{1/2}) ],  l = zeta
#   (ii) character route:   nu = [tr(g|S^+) - tr(g|S^-)] / [det(1-g^{-1}|T^{1,0}) det(1-g|T^{1,0})]
def nu_D4_half(m):                          # phi^m, weights (zeta^m, zeta^{-m})
    return (sfac(m) * sfac(-m)).inv()
def nu_D4_char(m):
    trS = (ONE + ONE) - (zp(m) + zp(-m))    # S^+ = (1,1), S^- = (zeta^m, zeta^{-m})
    det = (ONE - zp(-m)) * (ONE - zp(m)) * (ONE - zp(m)) * (ONE - zp(-m))
    return trS / det
for m in (1, 2):
    check(nu_D4_half(m) == nu_D4_char(m), "two derivations of the Dirac weight agree (m=%d)" % m)
    check(nu_D4_half(m) == QZ(F(1, 3)),   "nu_D4(phi^%d) = 1/3 exactly" % m)
NU_D4 = F(1, 3)
print("local Dirac weight nu_D4(phi^m) = 1/3 exactly (m = 1, 2), two independent derivations")

# Operational pin: ind_phi(D, K3) by Atiyah-Bott must equal the Hodge trace
IND_HODGE = KER_PLUS_D * 1 - KER_MIN_D      # tr(phi | H^{0,0} + H^{2,0}) - tr(phi | H^{0,1}) = 2
for m in (1, 2):
    check(QZ(N_FIX) * nu_D4_half(m) == QZ(IND_HODGE),
          "G3a: ind_{phi^%d}(D, K3) = 6 * 1/3 = 2 = Hodge trace (pins the canonical lift)" % m)
print("G3a: ind_phi(D, K3) = 6 * (1/3) = +2 = tr(phi | H^{0,0} + H^{2,0})  [Atiyah-Bott == Hodge]")

# Enumerate ALL admissible character twists of the lift: lift_m := (canonical lift) * zeta^m.
# Each has order 3 as a unitary bundle automorphism, but only m = 0 is Spin(4)-valued
# (zeta^m * Id on S^+/- has det zeta^{2m} != 1 in each SU(2) factor for m != 0).
print()
print("admissible lifts lift_m = canonical * zeta^m  (m = 0, 1, 2):")
for m in (0, 1, 2):
    ind_m = QZ(N_FIX) * nu_D4_half(1) * zp(m)          # AB index for lift_m at g = phi
    is_spin = (m == 0)
    rational = (ind_m.b == 0)
    check(rational == is_spin, "only m = 0 gives a rational (= Hodge-matchable) index")
    if is_spin:
        check(ind_m == QZ(2), "lift_0: ind = 2 matches Hodge trace -> THE spin lift")
    else:
        check(not (ind_m == QZ(IND_HODGE)), "lift_%d: ind = 2*zeta^%d != 2 -> NOT a spin lift" % (m, m))
    print("  m = %d : ind_phi(D) = %-14s  spin-structure lift: %s" %
          (m, repr(ind_m), "YES (unique)" if is_spin else "NO (vector-bundle twist only)"))

# =====================================================================================
# PRIMARY ROUTE: exact spectral concentration on the mapping torus
# =====================================================================================
print()
print("-" * 92)
print("PRIMARY ROUTE: spectral concentration -> master formula (exact, finite)")
print("-" * 92)
# D_5 = i Gamma d/dt + D_4 on T_phi (product metric). For every NONZERO fiber eigenvalue
# mu of D_4, the pair {psi, D_4 psi / mu} (same phi-phase: phi commutes with D_4) and each
# circle momentum nu give the 2x2 block [[nu, mu], [mu, -nu]]: trace 0, det < 0 =>
# eigenvalues +-sqrt(nu^2 + mu^2), symmetric within EVERY character: zero eta. Exact check:
npair = 0
for nu in (F(-3), F(-1, 2), F(0), F(2, 7), F(5), F(22, 3)):
    for mu in (F(1, 3), F(2), F(-7, 2), F(9)):
        tr_blk  = nu + (-nu)
        det_blk = -(nu * nu) - mu * mu
        check(tr_blk == 0, "nonzero-mode block is traceless (symmetric spectrum)")
        check(det_blk < 0, "nonzero-mode block eigenvalues +-sqrt(nu^2+mu^2) != 0")
        npair += 1
print("nonzero fiber modes pair off: %d rational (nu, mu) blocks traceless with det < 0" % npair)
print("=> the ENTIRE eta comes from ker(D_4) tensor circle modes; kernel mode with lift")
print("   phase e^{2 pi i theta}, twist alpha_k: momenta 2 pi (Z + theta + k/3)  =>")
print("   eta_{alpha_k} = sum_{ker^-} eta_S1({theta + k/3}) - sum_{ker^+} eta_S1({theta + k/3})")

def eta_alpha(ker_plus, ker_minus, k):
    e = F(0)
    for th, mult in ker_minus:
        e += mult * eta_S1(th + F(k, 3))
    for th, mult in ker_plus:
        e -= mult * eta_S1(th + F(k, 3))
    return e

def h_alpha(ker_plus, ker_minus, k):        # kernel of the twisted mapping-torus operator
    h = 0
    for th, mult in ker_plus + ker_minus:
        if (th + F(k, 3)) - ((th + F(k, 3)) // 1) == 0:
            h += mult
    return h

# Dirac kernel data (Hodge theory, canonical lift): ker^+ = 2 phi-trivial (theta = 0), ker^- = 0.
# For lift_m the kernel phases shift to theta = m/3 (modes scale by zeta^m).
LIFTS = {}
for m in (0, 1, 2):
    kp = [(F(m, 3), KER_PLUS_D)]
    km = []                                  # ker^- = H^{0,1} = 0 on K3
    etas = [eta_alpha(kp, km, k) for k in range(3)]
    rhos = [e - etas[0] for e in etas]
    hs   = [h_alpha(kp, km, k) for k in range(3)]
    cls  = [class_mod_Z(r) for r in rhos]
    LIFTS[m] = {"eta": etas, "rho": rhos, "h": hs, "class": cls, "ker_plus": kp, "ker_minus": km}

# --- canonical lift (m = 0): THE result of this leg -------------------------------------
E0, R0, H0, C0 = (LIFTS[0][x] for x in ("eta", "rho", "h", "class"))
check(E0 == [F(0), F(-2, 3), F(2, 3)], "Dirac eta_{alpha_k} = (0, -2/3, +2/3)  [recomputed]")
check(R0 == [F(0), F(-2, 3), F(2, 3)], "Dirac rho_k = (0, -2/3, +2/3)  [recomputed]")
check(H0 == [2, 0, 0],                 "h-terms (2, 0, 0), reported separately, NOT folded in")
check(C0 == [0, 1, 2],                 "mod-Z classes (0, 1, 2) in units of 1/3: NONZERO Z/3")
check(sum(E0) == 0,                    "G5: sum_k eta_{alpha_k} = 0")
check(R0[2] == -R0[1],                 "G6: rho_2 = -rho_1 (conjugation/reality, canonical lift)")
check(R0[1].denominator == 3 and R0[2].denominator == 3,
      "the Dirac rho has an HONEST order-3 denominator")
print()
print("CANONICAL LIFT (m = 0)   eta = (%s, %s, %s)   rho = (%s, %s, %s)   h = %s" %
      (E0[0], E0[1], E0[2], R0[0], R0[1], R0[2], H0))
print("                         rho mod Z = (%d, %d, %d) * (1/3)   -->  NONZERO Z/3 CLASS" % tuple(C0))

# --- all admissible lifts: relabeling structure + invariance of the verdict -------------
print()
print("all admissible lifts (eta level; only m = 0 is the spin lift):")
print("  m   eta_{alpha_k}            rho_k                    h        class(1/3)  G6 exact")
for m in (0, 1, 2):
    L = LIFTS[m]
    # relabeling identity: eta^{(m)}_k = eta^{(0)}_{k+m mod 3}
    for k in range(3):
        check(L["eta"][k] == E0[(k + m) % 3], "lift ambiguity relabels k -> k+m (m=%d, k=%d)" % (m, k))
    check(sum(L["eta"]) == 0, "G5 holds for every lift (character sum)")
    check(L["class"] == [0, 1, 2], "mod-Z classes are EXACTLY lift-independent: (0,1,2)/3")
    g6 = (L["rho"][2] == -L["rho"][1])
    check(g6 == (m == 0), "G6 exact reality holds iff the genuine spin lift (m = 0)")
    # G6 mod Z holds for every lift:
    check((L["rho"][1] + L["rho"][2]).denominator == 1, "G6 mod Z: rho_1 + rho_2 in Z, every lift")
    print("  %d   (%s, %s, %s)%s   (%s, %s, %s)%s   %s   %s     %s" %
          (m, L["eta"][0], L["eta"][1], L["eta"][2], " " * max(0, 12 - len("%s%s%s" % tuple(L["eta"]))),
           L["rho"][0], L["rho"][1], L["rho"][2], " " * max(0, 12 - len("%s%s%s" % tuple(L["rho"]))),
           L["h"], L["class"], "yes" if g6 else "no (not a spin lift)"))
print("=> the NONZERO Z/3 verdict and the class list (0, 1, 2)/3 are invariant across ALL")
print("   admissible lifts; the eta-level reals relabel k -> k+m exactly as pinned in Section 0.")

# =====================================================================================
# CROSS-CHECK A (G7): Donnelly isotypic averaging == direct spectral values, EXACTLY
# =====================================================================================
print()
print("-" * 92)
print("CROSS-CHECK A (G7): Donnelly averaging over the free Z/3 on K3 x S^1")
print("-" * 92)
# eta_{g^m}(K3 x S^1, D) = [tr(g^m | ker^-) - tr(g^m | ker^+)] * i cot(pi m / 3),  m = 1, 2
# rho_k = (1/3) sum_{m=1,2} (zeta^{-km} - 1) * eta_{g^m}   (m = 0 term drops in the difference)
def eta_g(a, lift_m):                        # equivariant eta at g^a, kernel scaled by zeta^{lift_m}
    tr_minus = QZ(0)
    tr_plus  = QZ(KER_PLUS_D) * zp(lift_m * a)
    return (tr_minus - tr_plus) * ICOT[a]

def rho_avg(k, lift_m):
    tot = QZ(0)
    for a in (1, 2):
        tot = tot + (zp(-k * a) - ONE) * eta_g(a, lift_m)
    return tot / 3

for k in (1, 2):
    r = rho_avg(k, 0)
    check(r.b == 0, "G7: averaged rho_%d is real (zeta-component exactly 0)" % k)
    check(r.a == R0[k], "G7: Donnelly average == direct spectral value, k = %d (EXACT, no sign fit)" % k)
    print("  k = %d : (1/3) sum_m (zeta^{-km}-1) eta_{g^m} = %-6s == direct %-6s  EXACT" %
          (k, r.a, R0[k]))
check(eta_g(2, 0) == eta_g(1, 0).conj(), "eta_{g^2} = conj(eta_g) (unitarity)")

# For the character-twisted (non-spin) lifts the naive averaging is blind to the
# eta_S1 integer-offset at the h-crossing: agreement is mod 2Z with the SAME mod-Z class.
for m in (1, 2):
    for k in (1, 2):
        r = rho_avg(k, m)
        check(r.b == 0, "twisted-lift average real")
        d = r.a - LIFTS[m]["rho"][k]
        check(is_even_int(d), "twisted lift m=%d, k=%d: averaging agrees mod 2Z (h-crossing shift)" % (m, k))
        check(class_mod_Z(r.a) == LIFTS[m]["class"][k], "same mod-Z class")
print("  twisted lifts m = 1, 2: averaging agrees mod 2Z (same class) -- the even-integer")
print("  offsets are the eta_S1 h-crossing shifts; EXACT agreement singles out the spin lift.")

# =====================================================================================
# CROSS-CHECK B (G8): disk fixed-point route (Z~ = K3 x D^2), well-defined mod 2Z
# =====================================================================================
print()
print("-" * 92)
print("CROSS-CHECK B (G8): APS/Donnelly on Z~ = K3 x D^2  (rho from local data alone, mod 2Z)")
print("-" * 92)
# Y~ = K3 x S^1 = boundary of Z~; g = (phi, rot 2pi/3) has 6 interior fixed points with
# tangent weights (zeta, zeta^{-1}; zeta); bounding spin structure => h_{g^m}(Y~) = 0.
# 6-dim Dirac weight: nu_D6(m) = nu_D4(m) / (zeta^{2m} - zeta^m).
# Donnelly/APS II: eta_{g^m}(Y~) = 2 * 6 * nu_D6(m) - 2 * ind_{g^m}(APS on Z~).
def nu_D6(m):
    return nu_D4_half(m) * (zp(2 * m) - zp(m)).inv()
check(nu_D6(1) == ISQRT3 / 9, "nu_D6(1) = (zeta - zeta^2)/9")
check(nu_D6(2) == nu_D6(1).conj(), "nu_D6(2) = conj(nu_D6(1))")

# INTEGER-SHIFT LEMMA (makes rho well-defined mod 2Z from local data): for every w in
# Z[zeta], (1/3) * [ (zeta^{-k} - 1) w + (zeta^{-2k} - 1) conj(w) ] is a rational integer.
viol, tested = 0, 0
for k in (1, 2):
    for a_ in range(-10, 11):
        for b_ in range(-10, 11):
            w = QZ(a_, b_)
            e = ((zp(-k) - ONE) * w + (zp(-2 * k) - ONE) * w.conj()) / 3
            tested += 1
            if not (e.b == 0 and e.a.denominator == 1):
                viol += 1
check(viol == 0, "integer-shift lemma: exact sweep over Z[zeta] box [-10,10]^2, both k")
print("integer-shift lemma: %d lattice points swept, 0 violations -> the APS ind-terms" % tested)
print("(virtual characters in Z[zeta], ind(g^2) = conj(ind(g))) shift rho_k by 2Z only")

for k in (1, 2):
    tot = QZ(0)
    for m in (1, 2):
        tot = tot + (zp(-k * m) - ONE) * (QZ(2 * N_FIX) * nu_D6(m))
    r_fp = tot / 3
    check(r_fp.b == 0, "G8: fixed-point rho_%d is real" % k)
    d = r_fp.a - R0[k]
    check(is_even_int(d), "G8: rho^{fp}_%d - rho^{direct}_%d in 2Z" % (k, k))
    check(class_mod_Z(r_fp.a) == C0[k], "G8: same mod-Z class as the direct route (k=%d)" % k)
    print("  k = %d : rho^{fp} = %-5s  vs direct %-5s  -> differ by even integer %s; class %d/3" %
          (k, r_fp.a, R0[k], d, C0[k]))

# implied equivariant APS index on Z~: ind_{g^m} = [2*6*nu_D6(m) - eta_{g^m}(Y~)] / 2
ind1 = (QZ(2 * N_FIX) * nu_D6(1) - eta_g(1, 0)) / 2
ind2 = (QZ(2 * N_FIX) * nu_D6(2) - eta_g(2, 0)) / 2
check(ind1.a.denominator == 1 and ind1.b.denominator == 1, "G8: ind_g(APS) in Z[zeta]")
check(ind2 == ind1.conj(), "G8: ind_{g^2}(APS) = conj(ind_g(APS))")
print("  implied ind_g(APS on Z~) = %s in Z[zeta], ind_{g^2} = conj  [G8 integrality]" % repr(ind1))

# =====================================================================================
# NON-EQUIVARIANT + ORBIFOLD GATES
# =====================================================================================
print()
print("-" * 92)
print("NON-EQUIVARIANT LIMIT + ORBIFOLD INTEGRALITY")
print("-" * 92)
check(F(-SIGMA_K3, 8) == 2, "index D = A-hat(K3) = -sigma/8 = 2 (sigma = -16)  [calibration]")
check((F(2) + 2 + 2) / 3 == 2, "G9 (Dirac part): orbifold average (2+2+2)/3 = 2 in Z")
print("index D(K3) = A-hat = -(-16)/8 = 2; orbifold average (2+2+2)/3 = 2 in Z")

# =====================================================================================
# OUTPUT (LEG-2 payload)
# =====================================================================================
print()
print("=" * 92)
print("LEG-2 OUTPUT")
print("=" * 92)
RESULT = {
    "eta":            [str(x) for x in E0],
    "rho":            [str(x) for x in R0],
    "h":              H0,
    "class_mod_Z":    C0,                       # units of 1/3
    "fp_route_mod2Z": "agrees",
    "verdict":        "Z3_NONZERO",
    "spin_lift":      "canonical order-3 lift m=0 (UNIQUE spin lift: Hom(Z/3,Z/2)=0; "
                      "pinned operationally by ind_phi(D)=+2=Hodge trace)",
    "all_admissible_lifts": {
        m: {"eta": [str(x) for x in LIFTS[m]["eta"]],
            "rho": [str(x) for x in LIFTS[m]["rho"]],
            "h": LIFTS[m]["h"], "class_mod_Z": LIFTS[m]["class"],
            "spin_structure_lift": (m == 0)}
        for m in (0, 1, 2)},
}
for key in ("eta", "rho", "h", "class_mod_Z", "fp_route_mod2Z", "verdict", "spin_lift"):
    print("  %-16s: %s" % (key, RESULT[key]))
print("  all_admissible_lifts:")
for m in (0, 1, 2):
    print("    m=%d: %s" % (m, RESULT["all_admissible_lifts"][m]))
print()
print("NOTE (convention robustness): the specific labels 1/3 vs 2/3 for the classes depend on")
print("orientation/character conventions (a (Z/3)^* unit); the NONZERO Z/3 verdict does not --")
print("it is invariant under every admissible lift and every unit relabeling.")
print("NOTE (h-discipline): rho is defined at the ETA level; the h-terms (2, 0, 0) are reported")
print("separately and never folded in (folding h in is the Route-3 xi failure mode).")
print()
print("ALL %d CHECKS PASS (exit 0)" % NASSERT)
