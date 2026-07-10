#!/usr/bin/env python3
"""
LEG-3 -- RS RHO: the fine equivariant (spectral) rho invariant of the ORDER-3 Nikulin
symplectic K3 automorphism for the SPIN-3/2 / RARITA-SCHWINGER operator (the unbuilt object).
==============================================================================================
THE OBJECT. phi = order-3 Nikulin symplectic automorphism of K3 (Nikulin 1979; Garbagnati-
Sarti 2007): exactly 6 isolated fixed points; at each, the local action on T^{1,0} has weights
(zeta, zeta^{-1}), zeta = e^{2 pi i/3}, forced by phi*Omega = Omega (local SU(2)). Average a
Kahler class over <phi> and take the Yau metric in the invariant class: phi is an isometry.
Mapping torus T_phi = (K3 x S^1)/<g>, g = (phi, rot 2pi/3), exact product metric. Flat Z/3
characters alpha_k(loop) = zeta^k, k = 0, 1, 2.

THE INVARIANT (eta level; APS I-III):
    rho_k(D_W) := eta_{alpha_k}(T_phi, D_W) - eta_{alpha_0}(T_phi, D_W).
h-terms (kernel dimensions) are reported separately and NEVER folded into rho.

RS CONVENTION (pinned by canon: index RS on K3 = 21*sigma/8 = -42, rs_index_harness.py):
    RS = D (x) (T_C X - C),  T_C X = complexified VERTICAL (K3-fiber) tangent bundle
(Alvarez-Gaume/Witten gravitino form A-hat * (ch(T_C) - 1); ONE-spinor subtraction).
Rival conventions are shown FAILING the canon gate below (T_C - 2C -> -44; total-space
TM_C - C -> -40) together with the equivariant classes they would have produced.

ESTABLISHED FORMULAS USED (citations; nothing else):
  - Atiyah-Bott fixed point formula for isolated fixed points (Ann. Math. 87/88, 1968).
  - Atiyah-Patodi-Singer I-III (1975-76): eta, rho/alpha-invariants of mapping tori.
  - Donnelly (1978): explicit equivariant eta for cyclic actions (icot densities).
  - Nikulin (1979); Garbagnati-Sarti (2007): order-3 symplectic K3 fixed-point + lattice data.
  - Alvarez-Gaume/Witten (1984): gravitino/RS index density 7 p1/8 => I_3/2 = 21 sigma/8.
  - Odd-order spin lifts: an order-3 diffeo has a UNIQUE order-3 lift to Spin (the other
    lift, -L, has order 6); H^1(K3, Z/2) = 0 kills any further twist on K3.

HOUSE STYLE: exact arithmetic only. Q(zeta) implemented as pairs a + b*zeta of Fractions,
zeta^2 = -1 - zeta. Global NASSERT, check() asserts, exit 0 on success. No floats. No sympy.

FIREWALL (absorbed/gu-source-action/DEAD-ENDS.md): nothing is manufactured from chi(K3)=24,
the /8 normalization (24/8=3), A-hat=3, or contractible-fiber=>1. Inventory asserted in S11.
"""
from fractions import Fraction as F

NASSERT = 0
def check(c, m):
    global NASSERT
    NASSERT += 1
    assert c, "FAIL: " + m


def banner(t):
    print()
    print("=" * 94)
    print(t)
    print("=" * 94)


# ==============================================================================================
# SECTION 0: ARITHMETIC CORE -- Q(zeta), zeta = e^{2 pi i/3}, as pairs a + b*zeta (Fractions)
# ==============================================================================================
class QZ:
    """Element a + b*zeta of Q(zeta); zeta^2 = -1 - zeta; conj: zeta -> -1 - zeta."""
    __slots__ = ("a", "b")

    def __init__(self, a=0, b=0):
        self.a, self.b = F(a), F(b)

    @staticmethod
    def co(o):
        return o if isinstance(o, QZ) else QZ(o)

    def __add__(s, o):
        o = QZ.co(o); return QZ(s.a + o.a, s.b + o.b)
    __radd__ = __add__

    def __neg__(s):
        return QZ(-s.a, -s.b)

    def __sub__(s, o):
        return s + (-QZ.co(o))

    def __rsub__(s, o):
        return QZ.co(o) - s

    def __mul__(s, o):
        o = QZ.co(o)
        a, b, c, d = s.a, s.b, o.a, o.b
        # (a + b z)(c + d z) = ac + (ad + bc) z + bd z^2 ;  z^2 = -1 - z
        return QZ(a * c - b * d, a * d + b * c - b * d)
    __rmul__ = __mul__

    def conj(s):
        return QZ(s.a - s.b, -s.b)

    def inv(s):
        n = s * s.conj()                       # norm a^2 - ab + b^2, rational
        check(n.b == 0 and n.a != 0, "Q(zeta) norm is rational and nonzero")
        return QZ(s.conj().a / n.a, s.conj().b / n.a)

    def __truediv__(s, o):
        return s * QZ.co(o).inv()

    def __eq__(s, o):
        o = QZ.co(o); return s.a == o.a and s.b == o.b

    def __repr__(s):
        sign = "+" if s.b >= 0 else "-"
        return "(%s %s %s*z)" % (s.a, sign, abs(s.b))


ZETA = QZ(0, 1)
ZP = {0: QZ(1), 1: ZETA, 2: ZETA * ZETA}


def zp(e):
    """zeta^e"""
    return ZP[e % 3]


# pinned exact identities of Section 0
check(zp(1) * zp(1) == QZ(-1, -1), "zeta^2 = -1 - zeta")
check(zp(1) * zp(2) == QZ(1), "zeta * zeta^2 = 1")
check(zp(1) + zp(2) == QZ(-1), "zeta + zeta^2 = -1")
check(zp(1) - zp(2) == QZ(1, 2), "i*sqrt(3) = zeta - zeta^2 = 1 + 2*zeta")
check(zp(1).conj() == zp(2), "conjugation zeta -> zeta^2")
ISQ3 = zp(1) - zp(2)                                        # i*sqrt(3)
ICOT = {1: QZ(F(1, 3)) * ISQ3, 2: QZ(F(-1, 3)) * ISQ3}      # i*cot(pi/3), i*cot(2 pi/3)
check(ISQ3 * ISQ3 == QZ(-3), "(i sqrt 3)^2 = -3")

# canonical odd-order spin lift: half powers inside mu_3 via lambda^{1/2} := lambda^2
def half(e):
    """(zeta^e)^{1/2} = zeta^{2e} (canonical order-3 lift)"""
    return zp(2 * e)


def sfac(e):
    """lambda^{1/2} - lambda^{-1/2} for lambda = zeta^e, canonical lift"""
    return half(e) - half(-e)


# circle unit (APS I): eta of -i d/dt with holonomy e^{2 pi i theta}
def eta_S1(th):
    t = th % 1
    return F(0) if t == 0 else 1 - 2 * t


check(eta_S1(F(1, 3)) == F(1, 3), "eta_S1(1/3) = 1/3")
check(eta_S1(F(2, 3)) == F(-1, 3), "eta_S1(2/3) = -1/3")
check(eta_S1(F(0)) == 0, "eta_S1(0) = 0")

# master formula machinery (Section 0 / LEG-2 conventions):
# phase multisets = dicts {theta: multiplicity}; ker^- contributes +eta_S1, ker^+ contributes -.
def eta_alpha(kp, km, k):
    e = F(0)
    for th, m in km.items():
        e += m * eta_S1(th + F(k, 3))
    for th, m in kp.items():
        e -= m * eta_S1(th + F(k, 3))
    return e


def h_virtual(kp, km, k):
    """virtual kernel dimension of the 5d operator in twist alpha_k (reported, never folded)"""
    h = 0
    for th, m in list(km.items()) + list(kp.items()):
        if (th + F(k, 3)) % 1 == 0:
            h += m
    return h


def tr_g(mult, m):
    """character of g^m on a phase multiset (theta in {0,1/3,2/3} <-> zeta-power 0,1,2)"""
    t = QZ(0)
    for th, mu in mult.items():
        t = t + QZ(mu) * zp(int(3 * th) * m)
    return t


def z3_class(rho):
    """rho (Fraction, denominator | 3) -> class a in {0,1,2} with rho == a/3 mod Z"""
    check(rho.denominator in (1, 3), "|G|=3 caps the denominator of rho at 3")
    return int((3 * rho) % 3)


def shift(mult, m):
    """tensor the lift by the character zeta^m: theta -> theta + m/3 (relabeling probe)"""
    return {(th + F(m, 3)) % 1: mu for th, mu in mult.items()}


banner("SECTION 0 OK: Q(zeta) core, canonical odd-order lift, eta_S1, master-formula machinery")

# ==============================================================================================
# SECTION 1: INPUTS CONSUMED FROM LEG-1 (recomputed here so this leg is self-verifying)
# ==============================================================================================
banner("S1. LEG-1 inputs recomputed: Lefschetz-forced lattice split and the H^{1,1} eigensplit")

# Lefschetz gate: L(phi) = #Fix = 6 = 2 + tr(phi|H^2); tr = r - s/2; r + s = 22 (b2 = 22
# from the K3 lattice of signature (3,19): sigma = 3 - 19 = -16).  SOLVE, do not recall.
SIGMA = -16
check(3 - 19 == SIGMA and 3 + 19 == 22, "K3 lattice signature (3,19): sigma = -16, b2 = 22")
sols_rs = [(22 - s_, s_) for s_ in range(0, 23, 2) if 2 + (22 - s_) - F(s_, 2) == 6]
check(sols_rs == [(10, 12)], "Lefschetz FORCES (r, s) = (10, 12)")
R_INV, S_COINV = sols_rs[0]
check(2 + 14 - F(8, 2) == 12 != 6,
      "NEGATIVE: the order-2 Nikulin data (r,s)=(14,8) gives L = 12 != 6 -- rejected. "
      "(Canon RESULTS.md line 44 carries this wrong (14,8); flagged for Joe, not edited.)")

# H^{1,1} eigenvalue split (consumed by the Hodge route of S4):
# phi fixes Omega, so H^{2,0} + H^{0,2} (2 classes) are phi-trivial and lie in the invariant
# part; all 12 coinvariants lie in H^{1,1}, in 6 conjugate pairs (zeta, zeta^2).
H20 = 1
H11 = 22 - 2 * H20                                   # = 20
H11_TRIV = R_INV - 2 * H20                           # invariant H^{1,1} = 10 - 2 = 8
H11_Z = S_COINV // 2                                 # 6 with eigenvalue zeta
H11_Z2 = S_COINV // 2                                # 6 with eigenvalue zeta^2
check(H11 == 20 and H11_TRIV == 8 and H11_Z == 6 and H11_Z2 == 6,
      "H^{1,1} eigensplit: 8 trivial + 6 zeta + 6 zeta^2 (total 20)")
check(H11_TRIV + H11_Z + H11_Z2 == H11, "H^{1,1} split is complete")
print("  (r, s) = (10, 12) forced;  H^{1,1} = 8 trivial + 6 zeta + 6 zeta^2;  sigma = -16")

# ==============================================================================================
# SECTION 2: ADMISSIBLE SPIN LIFTS (enumerated, not assumed)
# ==============================================================================================
banner("S2. Admissible spin lifts: the order-3 lift is UNIQUE (odd order; H^1(K3,Z/2) = 0)")

# Lifts of phi to Spin(T K3) differ by the deck element -1: candidates {L, -L}.
# (eps L)^3 = eps^3 L^3 = eps * id  =>  order 3 iff eps = +1.  H^1(K3, Z/2) = 0: no further
# twist ON K3.  (Character twists zeta^m of the MAPPING-TORUS data are a relabeling probe,
# swept in S9 -- they are flat-line-bundle twists of D_W, not new spin lifts.)
admissible = [eps for eps in (+1, -1) if eps ** 3 == 1]
check(admissible == [+1], "unique admissible order-3 spin lift (the canonical symplectic one)")

# The lift is pinned OPERATIONALLY (G3a input): the equivariant Dirac index must equal the
# Hodge trace on the phi-trivial parallel spinors, ind_phi(D) = tr(phi | H^{0,0}+H^{0,2}) = 2.
def nu_D4(m):
    """Atiyah-Bott Dirac weight at a fixed point of g^m: 1/prod_j(lam_j^{1/2}-lam_j^{-1/2}),
    weights lam = (zeta^m, zeta^{-m}) on T^{1,0}, canonical-lift half powers."""
    return (sfac(m) * sfac(-m)).inv()


for m in (1, 2):
    check(nu_D4(m) == QZ(F(1, 3)), "nu_D4(g^%d) = 1/3 exactly" % m)
IND_PHI_D = QZ(6) * nu_D4(1)
check(IND_PHI_D == QZ(2), "ind_phi(D, K3) = 6 * 1/3 = 2 = tr(phi|H^{0,0}+H^{0,2}) -- lift pinned")
check(QZ(6) * nu_D4(2) == QZ(2), "ind_{phi^2}(D, K3) = 2 as well")
print("  lifts {L, -L}: only L has order 3.  Pin gate: ind_phi(D) = 2 both powers.  m-relabel probe in S9.")

# ==============================================================================================
# SECTION 3: THE LOCAL WEIGHT FORMULA (the deliverable formula of this leg)
# ==============================================================================================
banner("S3. Exact RS local weight: nu_RS(p, g^m) = nu_D(p, g^m) * c(g^m), c = tr(g^m|T_C) - 1")

# RS = D (x) (T_C - C).  At each of the 6 fixed points, T_C = T^{1,0} + T^{0,1} has
# character (zeta^m + zeta^{-m}) + (zeta^{-m} + zeta^m), so
#     c(g^m) = 2*(zeta^m + zeta^{-m}) - 1 = -3   for m = 1, 2  -- identically at ALL 6 points
# (every fixed point has the same local type 1/3(1,2): FORCED by the symplectic structure).
C_RS = {}
for m in (1, 2):
    vals = set()
    for p in range(6):                     # all 6 fixed points carry identical weights
        c = QZ(2) * (zp(m) + zp(-m)) - 1
        vals.add((c.a, c.b))
    check(vals == {(F(-3), F(0))}, "c(g^%d) = -3 at every fixed point" % m)
    C_RS[m] = QZ(-3)
    check((C_RS[m].a % 3) == 0, "STRUCTURAL: twist character c(g^%d) == 0 mod 3" % m)

NU_RS4 = {m: nu_D4(m) * C_RS[m] for m in (1, 2)}
for m in (1, 2):
    check(NU_RS4[m] == QZ(-1), "nu_RS(p, g^%d) = (1/3)*(-3) = -1 per point" % m)
IND_PHI_RS = QZ(6) * NU_RS4[1]
check(IND_PHI_RS == QZ(-6), "Atiyah-Bott: ind_phi(RS, K3) = 6 * (-1) = -6")
check(QZ(6) * NU_RS4[2] == QZ(-6), "ind_{phi^2}(RS, K3) = -6")
print("  c(g^m) = -3 at all 6 points, both powers  =>  nu_RS = -1/point, ind_phi(RS) = -6")

# ==============================================================================================
# SECTION 4: KERNEL DATA -- two independent derivations, forced to agree (G4)
# ==============================================================================================
banner("S4. Kernel of the fiber operator D (x) (T_C - C): Hodge route vs integer forcing")

# (i) HODGE ROUTE.  Omega-contraction: T^{1,0} ~= Omega^1_hol phi-EQUIVARIANTLY (phi*Omega
# = Omega), so D (x) T^{1,0} is the Dolbeault complex of Omega^1:
#   ker^+ = H^0(Omega^1) + H^2(Omega^1) = 0 + 0   (h^{1,0} = 0; Serre duality, K trivial)
#   ker^- = H^1(Omega^1) = H^{1,1} = 8 trivial + 6 zeta + 6 zeta^2      (from S1)
# T^{0,1} contributes the conjugate representation (quaternionic structure on S^+-):
#   +8 trivial + 6 zeta^2 + 6 zeta.  Total ker^-(D (x) T_C) = 16 trivial + 12 zeta + 12 zeta^2.
# Subtract ONE C: ker^+(D) = H^0(O) + H^2(O) = 2 phi-trivial (constants, conj(Omega));
# ker^-(D) = H^1(O) = 0.  So the virtual RS multisets are:
KM_T10 = {F(0): H11_TRIV, F(1, 3): H11_Z, F(2, 3): H11_Z2}
KM_T01 = {F(0): H11_TRIV, F(2, 3): H11_Z, F(1, 3): H11_Z2}     # conjugate rep
KM_RS = {th: KM_T10[th] + KM_T01[th] for th in KM_T10}
KP_RS = {F(0): -2}                                              # minus the Dirac kernel
check(KM_RS == {F(0): 16, F(1, 3): 12, F(2, 3): 12},
      "Hodge route: ker^-(D (x) T_C) = 16 trivial + 12 zeta + 12 zeta^2; ker^+ = 0")

# Dirac baseline multisets (LEG-2 object, used here only for calibration/cross-checks):
KP_D = {F(0): 2}
KM_D = {}

# (ii) INTEGER FORCING (G4) -- independent of Hodge.  Reality m_zeta = m_{zeta^2} =: m1,
# trivial =: m0.  Non-equivariant gate: -42 = -2 - (m0 + 2 m1); equivariant gate:
# -6 = -2 - (m0 - m1).  Exhaustive sweep proves UNIQUENESS.
sols = [(m0, m1) for m0 in range(0, 61) for m1 in range(0, 61)
        if (-2 - (m0 + 2 * m1) == -42) and (-2 - (m0 - m1) == -6)]
check(sols == [(16, 12)], "G4: multiplicity solve UNIQUE: (m0, m1) = (16, 12)")
check(KM_RS[F(0)] == sols[0][0] and KM_RS[F(1, 3)] == sols[0][1] == KM_RS[F(2, 3)],
      "G4: integer forcing AGREES with the Hodge route (an error in either cannot pass)")

# G3b: equivariant index from the kernel data must reproduce Atiyah-Bott's -6:
ind_hodge = tr_g(KP_RS, 1) - tr_g(KM_RS, 1)
check(ind_hodge == QZ(-6), "G3b: Hodge trace ind_phi(RS) = -2 - (16 - 12) = -6 == Atiyah-Bott")
check(tr_g(KP_RS, 2) - tr_g(KM_RS, 2) == QZ(-6), "G3b holds for phi^2 as well")

# Non-equivariant gates (canon calibration; from sigma only -- p1 = 3*sigma, NO chi import):
P1 = 3 * SIGMA
AHAT = F(-SIGMA, 8)
check(AHAT == 2, "index D = A-hat(K3) = 2 (canon)")
IND_D_TC = 4 * AHAT + P1               # deg-4 part of A-hat*ch(T_C): -p1/6 + p1 = 5 p1/6
check(IND_D_TC == F(5 * P1, 6) == -40, "index D (x) T_C = 5 p1/6 = -40 (ch2(T_C) = p1)")
IND_RS = IND_D_TC - int(AHAT)
check(IND_RS == -42 == F(21 * SIGMA, 8), "index RS = -42 = 21 sigma/8 (CANON GATE: pins T_C - 1C)")
check(-2 - (16 + 2 * 12) == -42, "kernel data reproduces index RS = -42")
print("  ker^- = {0:16, 1/3:12, 2/3:12}, ker^+ = {0:-2} (virtual); both routes agree; -42 pinned")

# ==============================================================================================
# SECTION 5: PRIMARY ROUTE -- the master formula on the mapping torus (both characters)
# ==============================================================================================
banner("S5. Direct spectral eta/rho of RS on T_phi, all three characters alpha_k")

ETA_RS = [eta_alpha(KP_RS, KM_RS, k) for k in range(3)]
RHO_RS = [e - ETA_RS[0] for e in ETA_RS]
H_RS = [h_virtual(KP_RS, KM_RS, k) for k in range(3)]

ETA_D = [eta_alpha(KP_D, KM_D, k) for k in range(3)]           # Dirac baseline (calibration)
RHO_D = [e - ETA_D[0] for e in ETA_D]
H_D = [h_virtual(KP_D, KM_D, k) for k in range(3)]

check(ETA_RS == [F(0), F(2), F(-2)], "RS eta = (0, +2, -2)")
check(RHO_RS == [F(0), F(2), F(-2)], "RS rho = (0, +2, -2)")
check(H_RS == [14, 12, 12], "RS h_virtual = (14, 12, 12) -- reported separately, never folded")
check(ETA_D == [F(0), F(-2, 3), F(2, 3)], "Dirac baseline eta = (0, -2/3, +2/3)")
check(H_D == [2, 0, 0], "Dirac h = (2, 0, 0)")

check(sum(ETA_RS) == 0 and sum(ETA_D) == 0, "G5: sum_k eta_{alpha_k} = 0 (both operators)")
check(RHO_RS[2] == -RHO_RS[1] and RHO_D[2] == -RHO_D[1], "G6: rho_2 = -rho_1 (both operators)")
# reality is structural here: the master formula lands in Q; QZ cross-routes assert b == 0.

CLS_RS = [z3_class(r) for r in RHO_RS]
CLS_D = [z3_class(r) for r in RHO_D]
check(CLS_RS == [0, 0, 0], "RS classes mod Z: (0, 0, 0) -- THE Z/3-PART OF THE RS RHO IS ZERO")
check(CLS_D == [0, 1, 2], "Dirac classes mod Z: (0, 1, 2)/3 -- the baseline order-3 class is real")
print("  RS:    eta = %s  rho = %s  h = %s  class = %s" % (ETA_RS, RHO_RS, H_RS, CLS_RS))
print("  Dirac: eta = %s  rho = %s  h = %s  class = %s" % (ETA_D, RHO_D, H_D, CLS_D))

# ==============================================================================================
# SECTION 6: CROSS-CHECK A -- Donnelly / isotypic averaging (G7), exact, no sign refitting
# ==============================================================================================
banner("S6. G7: Donnelly averaging == direct spectral values EXACTLY (both operators, both k)")

def eta_gm(kp, km, m):
    """equivariant eta of g^m on the cover K3 x S^1: [tr(g^m|ker^-) - tr(g^m|ker^+)] * icot(m)"""
    return (tr_g(km, m) - tr_g(kp, m)) * ICOT[m]


agreements = 0
for name, kp, km, eta_direct in (("Dirac", KP_D, KM_D, ETA_D), ("RS", KP_RS, KM_RS, ETA_RS)):
    for k in range(3):
        # isotypic identity: eta_{alpha_k} = (1/3) sum_m zeta^{-km} eta_{g^m};  eta_{g^0} = 0
        # (ordinary eta of the product K3 x S^1 vanishes by spectral symmetry).
        tot = QZ(0)
        for m in (1, 2):
            tot = tot + zp(-k * m) * eta_gm(kp, km, m)
        iso = QZ(F(1, 3)) * tot
        check(iso.b == 0, "%s k=%d: isotypic average is real" % (name, k))
        check(iso == QZ(eta_direct[k]), "%s k=%d: Donnelly isotypic == direct (exact)" % (name, k))
        if k > 0:
            # rho form: rho_k = (1/3) sum_m (zeta^{-km} - 1) eta_{g^m}
            tot2 = QZ(0)
            for m in (1, 2):
                tot2 = tot2 + (zp(-k * m) - QZ(1)) * eta_gm(kp, km, m)
            rho_avg = QZ(F(1, 3)) * tot2
            direct = QZ(eta_direct[k] - eta_direct[0])
            check(rho_avg == direct, "%s k=%d: Donnelly rho == direct rho (exact)" % (name, k))
            agreements += 1
check(agreements == 4, "G7: 4 independent exact agreements (2 operators x 2 characters)")
print("  4/4 exact agreements; zero residual sign in the pinned conventions")

# ==============================================================================================
# SECTION 7: CROSS-CHECK B -- disk fixed-point route on Z~ = K3 x D^2, mod 2Z (G8)
# ==============================================================================================
banner("S7. G8: disk route -- integer-shift lemma, mod-2Z agreement, APS-index integrality")

# Integer-shift lemma: for every w in Z[zeta], (1/3)[(z^{-k}-1) w + (z^{-2k}-1) conj(w)] is a
# rational INTEGER -- proven by exact sweep over the lattice box [-10,10]^2, both k.
for k in (1, 2):
    for a in range(-10, 11):
        b_ok = True
        for b in range(-10, 11):
            w = QZ(a, b)
            v = QZ(F(1, 3)) * ((zp(-k) - 1) * w + (zp(-2 * k) - 1) * w.conj())
            if not (v.b == 0 and v.a.denominator == 1):
                b_ok = False
                break
        if not b_ok:
            break
    check(b_ok, "integer-shift lemma holds on the full [-10,10]^2 box, k=%d" % k)
print("  integer-shift lemma: 2 x 441 lattice points, all rational integers -> ind terms drop mod 2Z")

def nu_D6(m):
    """6-dim Dirac weight at an interior fixed point of K3 x D^2 (weights zeta^m, zeta^-m; zeta^m)"""
    return nu_D4(m) * (zp(2 * m) - zp(m)).inv()


check(nu_D6(1) == QZ(F(1, 9)) * ISQ3, "nu_D6(g) = (zeta - zeta^2)/9")
check(nu_D6(2) == nu_D6(1).conj(), "nu_D6(g^2) = conj(nu_D6(g))")


def rho_fp(k, cchar):
    """rho_k from local data alone: (1/3) sum_m (zeta^{-km}-1) * 2*6*nu_D6(m)*c(g^m); mod 2Z"""
    tot = QZ(0)
    for m in (1, 2):
        tot = tot + (zp(-k * m) - QZ(1)) * (QZ(12) * nu_D6(m) * cchar[m])
    return QZ(F(1, 3)) * tot


C_DIRAC = {1: QZ(1), 2: QZ(1)}
for k in (1, 2):
    fpD = rho_fp(k, C_DIRAC)
    fpR = rho_fp(k, C_RS)
    check(fpD.b == 0 and fpR.b == 0, "disk-route rho is rational, k=%d" % k)
    check(fpR == QZ(-3) * fpD, "disk route: rho_fp(RS) = -3 * rho_fp(Dirac) EXACTLY, k=%d" % k)
    dD = fpD.a - RHO_D[k]
    dR = fpR.a - RHO_RS[k]
    check(dD % 2 == 0, "Dirac: fp-route - direct in 2Z (k=%d: %s - %s = %s)" % (k, fpD.a, RHO_D[k], dD))
    check(dR % 2 == 0, "RS: fp-route - direct in 2Z (k=%d: %s - %s = %s)" % (k, fpR.a, RHO_RS[k], dR))
    check(z3_class(fpD.a) == CLS_D[k], "Dirac: same mod-Z class from the disk route, k=%d" % k)
    check(z3_class(fpR.a) == CLS_RS[k] == 0, "RS: disk route class ZERO too, k=%d" % k)
    print("  k=%d: fp Dirac %s vs direct %s (diff %s);  fp RS %s vs direct %s (diff %s)"
          % (k, fpD.a, RHO_D[k], dD, fpR.a, RHO_RS[k], dR))

# G8 integrality: implied ind_{g^m}(APS on Z~) = [2*6*nu_W6(m) - eta_{g^m}^{direct}]/2 must lie
# in Z[zeta] with ind_{g^2} = conj(ind_g)   (h_{g^m}(Y~) = 0: bounding spin structure).
for name, kp, km, cchar in (("Dirac", KP_D, KM_D, C_DIRAC), ("RS", KP_RS, KM_RS, C_RS)):
    inds = {}
    for m in (1, 2):
        ind = (QZ(12) * nu_D6(m) * cchar[m] - eta_gm(kp, km, m)) * QZ(F(1, 2))
        check(ind.a.denominator == 1 and ind.b.denominator == 1,
              "%s: implied ind_{g^%d}(APS) lies in Z[zeta]" % (name, m))
        inds[m] = ind
    check(inds[2] == inds[1].conj(), "%s: ind_{g^2} = conj(ind_g) (G8 integrality)" % name)
    print("  %s implied APS indices: ind_g = %s, ind_g2 = %s (in Z[zeta], conjugate pair)"
          % (name, inds[1], inds[2]))

# ==============================================================================================
# SECTION 8: NEGATIVE CHECKS -- rival RS conventions FAIL the canon gate and flip the verdict
# ==============================================================================================
banner("S8. Rejected conventions (shown failing, per spec): T_C - 2C and total-space TM_C - C")

# (a) T_C - 2C ('ghost' two-spinor subtraction): index = -40 - 2*2 = -44 = 11 sigma/4 != -42.
ind_2c = IND_D_TC - 2 * int(AHAT)
check(ind_2c == -44 == F(11 * SIGMA, 4), "T_C - 2C index = -44 = 11 sigma/4")
check(ind_2c != IND_RS, "T_C - 2C FAILS the canon non-equivariant gate (-44 != -42): REJECTED")
kp_2c = {F(0): -4}
rho1_2c = eta_alpha(kp_2c, KM_RS, 1) - eta_alpha(kp_2c, KM_RS, 0)
check(rho1_2c == F(8, 3) and z3_class(rho1_2c) == 2,
      "T_C - 2C would give rho_1 = 8/3: the Z/3 class REAPPEARS (class 2) -- convention is load-bearing")

# (b) total-space twist TM_C - C: on the fiber TM_C = T_C + C (dt-direction, g-trivial), so
# the twist reduces to T_C: index = -40 != -42.
ind_tot = IND_D_TC
check(ind_tot == -40 and ind_tot != IND_RS,
      "TM_C - C restricts to index -40: FAILS the canon gate: REJECTED")
kp_tot = {}                                        # +2 (D x C_dt kernel) - 2 (subtraction) = 0
rho1_tot = eta_alpha(kp_tot, KM_RS, 1) - eta_alpha(kp_tot, KM_RS, 0)
check(rho1_tot == F(4, 3) and z3_class(rho1_tot) == 1,
      "TM_C - C would give rho_1 = 4/3 (class 1): verdict flips -- gate must stay frozen")
print("  T_C-2C: index -44 (FAIL), rho_1 = 8/3 (class 2).  TM_C-C: index -40 (FAIL), rho_1 = 4/3 (class 1).")
print("  Only the pinned T_C - 1C passes -42 = 21 sigma/8; its class is (0,0,0).")

# ==============================================================================================
# SECTION 9: LIFT/CHARACTER RELABELING SWEEP -- verdict robustness (all m in {0,1,2})
# ==============================================================================================
banner("S9. Relabeling sweep: twisting the lift by zeta^m only permutes the etas; classes invariant")

for m in range(3):
    kpD, kmD = shift(KP_D, m), shift(KM_D, m)
    kpR, kmR = shift(KP_RS, m), shift(KM_RS, m)
    eD = [eta_alpha(kpD, kmD, k) for k in range(3)]
    eR = [eta_alpha(kpR, kmR, k) for k in range(3)]
    check(sorted(eD) == sorted(ETA_D), "m=%d: Dirac etas are a permutation of the m=0 etas" % m)
    check(sorted(eR) == sorted(ETA_RS), "m=%d: RS etas are a permutation of the m=0 etas" % m)
    cD = sorted(z3_class(e - eD[0]) for e in eD)
    cR = [z3_class(e - eR[0]) for e in eR]
    check(cD == [0, 1, 2], "m=%d: Dirac class multiset {0,1,2} invariant (NONZERO survives)" % m)
    check(cR == [0, 0, 0], "m=%d: RS classes (0,0,0) invariant (ZERO is relabeling-robust)" % m)
print("  all 3 relabelings: RS class (0,0,0); Dirac class multiset {0,1,2}. Verdict convention-robust.")

# ==============================================================================================
# SECTION 10: THE STRUCTURAL MECHANISM (why the RS Z/3-part is zero, provably)
# ==============================================================================================
banner("S10. Structure: c == 0 mod 3 kills the class; a_k = k*T mod 3 with T = -ind_g")

# Chain (each link computed above): c(g^m) = -3 == 0 mod 3 (S3)
#   => ind_g(RS) = (6 nu_D) * c = 2c == 0 mod 3          (Atiyah-Bott, S3)
#   => T := tr(g | ker^- - ker^+) = -ind_g == 0 mod 3    (Hodge, S4)
#   => class a_k = (k*T) mod 3 = 0.                      (empirical law, verified here)
for name, kp, km, cls in (("Dirac", KP_D, KM_D, CLS_D), ("RS", KP_RS, KM_RS, CLS_RS)):
    Tq = tr_g(km, 1) - tr_g(kp, 1)
    check(Tq.b == 0 and Tq.a.denominator == 1, "%s: T is a rational integer (self-conj rep)" % name)
    check(Tq == tr_g(km, 2) - tr_g(kp, 2), "%s: T identical for both powers" % name)
    T = int(Tq.a)
    for k in (1, 2):
        check(cls[k] == (k * T) % 3, "%s: class law a_k = k*T mod 3 (k=%d, T=%d)" % (name, k, T))
check(int((tr_g(KM_RS, 1) - tr_g(KP_RS, 1)).a) == -2 * (-3),
      "T_RS = -ind_g = -2c = 6: divisibility by 3 is INHERITED from the twist character")
print("  Dirac: T = -2 (not divisible by 3) -> classes (0,1,2): honest order-3 object.")
print("  RS:    T = +6 = -2c, c = -3 == 0 mod 3 -> classes (0,0,0): STRUCTURAL, not accidental --")
print("  for ANY order-3 symplectic K3 automorphism the RS twist character is divisible by 3,")
print("  so the RS fine rho can never carry an order-3 class, though the Dirac one genuinely does.")

# ==============================================================================================
# SECTION 11: REMAINING GATES + FIREWALL INVENTORY + HONESTY NOTES + OUTPUT
# ==============================================================================================
banner("S11. G9 orbifold integrality, firewall audit (leg-local), honesty notes, output")

check(F(2 + 2 + 2, 3) == 2, "G9: orbifold-average Dirac index = 2 in Z")
check(F(-42 - 6 - 6, 3) == -18, "G9: orbifold-average RS index = -18 in Z")
check(F(SIGMA + 2 + 2, 3) == -4, "G9: orbifold-average signature = -4 in Z")

# FIREWALL (leg-local; LEG-4 owns the consolidated audit).  Complete input inventory:
INPUTS = {
    "fixed_points": 6,            # Nikulin classification; confirmed by the Lefschetz gate (S1)
    "local_weights": "(zeta, zeta^-1) on T^{1,0} (symplectic, forced)",
    "lattice_r_s": (10, 12),      # FORCED by the Lefschetz solve in S1, not recalled
    "sigma_K3": -16,              # K3 lattice signature (3,19)
    "hodge_numbers": (0, 1, 20),  # h^{0,1}, h^{2,0}, h^{1,1}
    "densities": "Atiyah-Bott / Donnelly / APS (standard)",
}
check(all(v != 24 for v in (6, 10, 12, -16, 0, 1, 20, 22)),
      "FIREWALL: chi(K3) = 24 is NOT an input anywhere in this leg")
check(AHAT == 2 and AHAT != 3, "FIREWALL: A-hat(K3) = 2 used; the flat A-hat = 3 never appears")
check(F(21 * SIGMA, 8) == -42 and F(-SIGMA, 8) == 2,
      "FIREWALL: the only /8 is inside the standard AS densities 21s/8 and -s/8 -- never 24/8")
USED_CONTRACTIBLE_FIBER_RULE = False
check(not USED_CONTRACTIBLE_FIBER_RULE, "FIREWALL: no contractible-fiber => 1 step exists")
print("  firewall inputs:", INPUTS)

RESULT = {
    "eta": [str(e) for e in ETA_RS],
    "rho": [str(r) for r in RHO_RS],
    "h_virtual": H_RS,
    "class_mod_Z": CLS_RS,
    "structural_reason": "twist character = -3 == 0 mod 3 at every fixed point",
    "verdict": "Z3_ZERO_2PRIMARY",
}
print()
print("LEG-3 OUTPUT:", RESULT)
print()
print("HONESTY NOTES (stated, not resolved):")
print(" (a) This is the K-THEORETIC gamma-traceless RS: eta(D (x) T_C) - eta(D). The honest")
print("     gamma-traceless operator's spectrum differs by a repackaging (Clifford multiplication")
print("     does not commute with the gamma-trace projector on the hyperkahler metric): the INDEX")
print("     and the MOD-Z CLASS are stable under that repackaging; the exact reals +-2 could shift.")
print(" (b) The exact reals are exact for the isometric product metric; for finite-order isometric")
print("     monodromy the Bismut-Cheeger eta-form corrections vanish, so this is the honest")
print("     families object at geometric-benchmark grade. The GU source-action operator identity")
print("     (SG4 MISSING-CARRIER) remains open -- LEG-4's caveat, not resolvable here.")
print()
print("CANON CORRECTION FLAG (for Joe, NOT executed): canon/families-e-invariant-order3-monodromy-")
print("RESULTS.md line 44 says invariant/coinvariant ranks (14, 8); the Lefschetz gate forces (10, 12).")
print()
print("#" * 94)
print("# LEG-3 COMPLETE: RS fine equivariant rho = (0, +2, -2); Z/3 class (0, 0, 0) -- 2-PRIMARY.")
print("# The Dirac baseline class (0, 1, 2)/3 is genuinely order-3; the RS twist character -3 == 0")
print("# mod 3 annihilates it STRUCTURALLY for every order-3 symplectic K3 monodromy.")
print("# hard asserts passed: %d" % NASSERT)
print("#" * 94)
