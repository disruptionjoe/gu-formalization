#!/usr/bin/env python3
"""
LEG-D -- IDENTIFICATION: which object is the generation-arena carrier?
================================================================================================
THE QUESTION (question 4 of the symbol-adjudication swing). Two published, internally coherent
spin-3/2 objects on K3 differ by exactly two spin-1/2 units:

  (A) GHOST-SUBTRACTED GRAVITINO COMPLEX (the repo's pin):
        K-class  [S+ - S-] (x) (T_C - 1C),  index -42 = 21*sigma/8
        (AGW/Christensen-Duff anomaly density; Witten's ghost subtraction, quoted verbatim in
        Homma-Semmelmann CMP 2019 Remark 3.6; the "-1" is a SAME-chirality spin-1/2 ghost).
  (B) GEOMETRIC GAMMA-TRACELESS OPERATOR Q (the literature's "Rarita-Schwinger operator"):
        K-class  [S+ - S-] (x) (T_C + 1C),  index -38 = 19*sigma/8 = -19*A-hat
        (Homma-Semmelmann CMP 2019 Prop 3.1(i); Baer-Mazzeo CMP 2021; the "+1" is the
        REVERSED-chirality embedded block iota(S-+) of the twistor splitting).

THIS LEG: (i) exact bookkeeping of WHERE the order-3 class lives in the A/B fork (all exact
Q(zeta)/Fraction arithmetic, machinery reused from the adversarially-verified leg2/leg3
scripts); (ii) a repo-pin ledger -- the identification-relevant sentences of the prior
campaigns are READ FROM THE REPO and asserted present, so the ledger is checkable; (iii) the
steelman scorecard and the weakest-defensible identification verdict, with genuine BLOCKED
items reported (a passing script that reports BLOCKED is the honest shape -- the
identification question is NOT decidable from any in-repo computed object).

HOUSE STYLE: exact arithmetic only (Fractions; Q(zeta) as pairs a + b*zeta). check() asserts,
exit 0. FIREWALL (absorbed/gu-source-action/DEAD-ENDS.md): no chi(K3)=24 input, no 24/8=3,
no A-hat=3, no predetermined 3; -38 is DERIVED as -40 + 2, never imported.
"""
import io
import os
import sys
from fractions import Fraction as F

NASSERT = 0
BLOCKED = []          # genuine blocked items, reported honestly at the end


def check(c, m):
    global NASSERT
    NASSERT += 1
    assert c, "FAIL: " + m


def banner(t):
    print()
    print("=" * 96)
    print(t)
    print("=" * 96)


# ==============================================================================================
# S0. ARITHMETIC CORE -- Q(zeta) pairs (verbatim machinery of the verified leg2/leg3 scripts)
# ==============================================================================================
class QZ:
    """a + b*zeta, zeta = e^{2 pi i/3}; zeta^2 = -1 - zeta; conj: zeta -> -1 - zeta."""
    __slots__ = ("a", "b")

    def __init__(self, a=0, b=0):
        self.a, self.b = F(a), F(b)

    @staticmethod
    def co(o):
        return o if isinstance(o, QZ) else QZ(o)

    def __add__(s, o):
        o = QZ.co(o)
        return QZ(s.a + o.a, s.b + o.b)
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
        return QZ(a * c - b * d, a * d + b * c - b * d)
    __rmul__ = __mul__

    def conj(s):
        return QZ(s.a - s.b, -s.b)

    def inv(s):
        n = s * s.conj()
        check(n.b == 0 and n.a != 0, "Q(zeta) norm rational nonzero")
        return QZ(s.conj().a / n.a, s.conj().b / n.a)

    def __truediv__(s, o):
        return s * QZ.co(o).inv()

    def __eq__(s, o):
        o = QZ.co(o)
        return s.a == o.a and s.b == o.b

    def __repr__(s):
        sg = "+" if s.b >= 0 else "-"
        return "(%s %s %s*z)" % (s.a, sg, abs(s.b))


ZP = {0: QZ(1), 1: QZ(0, 1), 2: QZ(0, 1) * QZ(0, 1)}


def zp(e):
    return ZP[e % 3]


check(zp(1) * zp(1) == QZ(-1, -1), "zeta^2 = -1 - zeta")
check(zp(1) + zp(2) == QZ(-1), "zeta + zeta^2 = -1")
ISQ3 = zp(1) - zp(2)                                       # i*sqrt(3)
check(ISQ3 * ISQ3 == QZ(-3), "(i sqrt3)^2 = -3")
ICOT = {1: QZ(F(1, 3)) * ISQ3, 2: QZ(F(-1, 3)) * ISQ3}     # i*cot(pi m/3)


def half(e):
    """canonical odd-order lift half power: (zeta^e)^{1/2} = zeta^{2e}"""
    return zp(2 * e)


def sfac(e):
    return half(e) - half(-e)


def eta_S1(th):
    t = th % 1
    return F(0) if t == 0 else 1 - 2 * t


def eta_alpha(kp, km, k):
    e = F(0)
    for th, m in km.items():
        e += m * eta_S1(th + F(k, 3))
    for th, m in kp.items():
        e -= m * eta_S1(th + F(k, 3))
    return e


def h_of(kp, km, k):
    h = 0
    for th, m in list(km.items()) + list(kp.items()):
        if (th + F(k, 3)) % 1 == 0:
            h += m
    return h


def tr_g(mult, m):
    t = QZ(0)
    for th, mu in mult.items():
        t = t + QZ(mu) * zp(int(3 * th) * m)
    return t


def z3_class(rho):
    check(F(rho).denominator in (1, 3), "|G|=3 caps rho denominator at 3")
    return int((3 * F(rho)) % 3)


def shift(mult, m):
    return {(th + F(m, 3)) % 1: mu for th, mu in mult.items()}


banner("S0 OK: Q(zeta) core + master-formula machinery (leg2/leg3 conventions, reused verbatim)")

# ==============================================================================================
# S1. NON-EQUIVARIANT CONVENTION LEDGER -- everything from sigma = -16 alone (p1 = 3*sigma)
# ==============================================================================================
banner("S1. The A/B fork non-equivariantly: -42 = -40 - 2 (ghost) vs -38 = -40 + 2 (geometric)")

SIGMA = -16
P1 = 3 * SIGMA
AHAT = F(-SIGMA, 8)                       # index D = A-hat[K3]
check(AHAT == 2, "ind D = -sigma/8 = 2")
IND_D = int(AHAT)
IND_DTC = 4 * IND_D + P1                  # A-hat*ch(T_C): rk*Ahat + ch2(T_C)=p1
check(IND_DTC == F(5 * P1, 6) == -40, "ind(D (x) T_C) = 5 p1/6 = -40")

IND_A = IND_DTC - IND_D                   # ghost-subtracted gravitino complex (SAME-chirality -1)
IND_B = IND_DTC + IND_D                   # geometric Q (REVERSED-chirality embedded block => +1)
check(IND_A == -42 == F(21 * SIGMA, 8) == F(7 * P1, 8), "carrier A: -42 = 21 sigma/8 = 7 p1/8")
check(IND_B == -38 == F(19 * SIGMA, 8) == F(19 * P1, 24), "carrier B: -38 = 19 sigma/8 = 19 p1/24")
check(IND_B == -19 * IND_D, "carrier B: ind Q = -19 A-hat (Homma-Semmelmann Prop 3.1(i) form)")
check(IND_B - IND_A == 4 == 2 * IND_D, "the fork is EXACTLY two spin-1/2 units: B - A = 2 ind D")
check(IND_A % 3 == 0 and IND_B % 3 == 1 and IND_DTC % 3 == 2 and IND_D % 3 == 2,
      "residues mod 3: A -> 0, B -> 1, D(x)T_C -> 2, D -> 2")
print("  ind D = 2, ind D(x)T_C = -40;  A = -42 (ghost -1), B = -38 (geometric +1);  B - A = 2*ind D = 4")
print("  K-theory: [B] - [A] = 2*[1C]  --  the fork is the ORIENTATION of the rank-2 spin-1/2 slot")

# ==============================================================================================
# S2. EQUIVARIANT MULTIPLIER LEDGER at the 6 Nikulin fixed points (weights zeta, zeta^{-1})
# ==============================================================================================
banner("S2. Fixed-point multipliers: c_A = -3 == 0 mod 3 (kill), c_B = -1 (live); c_B - c_A = 2")

# Dirac local weight nu_D4 = 1/((l1^{1/2}-l1^{-1/2})(l2^{1/2}-l2^{-1/2})), canonical lift.
def nu_D4(m):
    return (sfac(m) * sfac(-m)).inv()


for m in (1, 2):
    check(nu_D4(m) == QZ(F(1, 3)), "nu_D4(g^%d) = 1/3" % m)

# independent per-point verification: nu_D4 = (trS+ - trS-)/det(1 - g^{-1}|T_C)
TR_SP = half(1) * half(-1) + half(-1) * half(1)            # S+ weights: both trivial
TR_SM = half(1) * half(1) + half(-1) * half(-1)            # S- weights: zeta, zeta^2
check(TR_SP == QZ(2) and TR_SM == QZ(-1), "canonical lift: tr(g|S+) = 2, tr(g|S-) = -1")
DET1G = (QZ(1) - zp(1)) * (QZ(1) - zp(2)) * (QZ(1) - zp(2)) * (QZ(1) - zp(1))
check(DET1G == QZ(9), "det(1 - g^{-1}|T_C) = 9")
check((TR_SP - TR_SM) / DET1G == QZ(F(1, 3)), "nu_D4 = (trS+ - trS-)/det = 3/9 = 1/3 (independent)")

TR_TC = QZ(2) * (zp(1) + zp(2))                            # tr(g^m|T_C) = 2(zeta^m + zeta^-m)
check(TR_TC == QZ(-2), "tr(g^m|T_C) = -2 at every fixed point, both powers")

C_D = QZ(1)                    # plain Dirac twist multiplier (trivial line)
C_A = TR_TC - 1                # ghost-subtracted:      tr(T_C) - 1
C_B = TR_TC + 1                # geometric (reversed):  tr(T_C) + 1
check(C_A == QZ(-3) and int(C_A.a) % 3 == 0, "c_A = -3 == 0 mod 3: STRUCTURAL kill of carrier A")
check(C_B == QZ(-1) and int(C_B.a) % 3 == 2, "c_B = -1 !== 0 mod 3: the kill mechanism is ABSENT in B")
check(C_B - C_A == QZ(2) == QZ(2) * C_D, "multiplier fork = 2*c_Dirac: same 2-spin-1/2 slot")
check(int(TR_TC.a) % 3 == 1, "the pure twist part tr(T_C) = -2 == 1 mod 3 is itself LIVE mod 3")

# V-bundle route to ind_phi(Q) (twistor splitting is Spin-natural, hence phi-equivariant):
TR_V = (TR_SP - TR_SM) * (TR_TC + 1)                       # tr(g|V+) - tr(g|V-)
check(TR_V == QZ(-3), "tr(g|V+) - tr(g|V-) = (trS+ - trS-)(trT_C + 1) = 3*(-1) = -3")
IND_PHI = {}
IND_PHI["D"] = QZ(6) * nu_D4(1) * C_D
IND_PHI["DTC"] = QZ(6) * nu_D4(1) * TR_TC
IND_PHI["A"] = QZ(6) * nu_D4(1) * C_A
IND_PHI["B"] = QZ(6) * nu_D4(1) * C_B
check(IND_PHI["D"] == QZ(2), "ind_phi(D) = 2 (lift pin gate, = Hodge trace)")
check(IND_PHI["DTC"] == QZ(-4), "ind_phi(D (x) T_C) = -4")
check(IND_PHI["A"] == QZ(-6), "ind_phi(A) = -6 (matches the verified leg3 value)")
check(IND_PHI["B"] == QZ(-2), "ind_phi(B) = ind_phi(Q) = -2")
check(QZ(6) * TR_V / DET1G == QZ(-2), "V-bundle route: ind_phi(Q) = 6*(-3)/9 = -2 (independent)")
check(IND_PHI["B"] == IND_PHI["DTC"] + IND_PHI["D"], "equivariant additivity: -2 = -4 + 2")
check(IND_PHI["A"] == IND_PHI["DTC"] - IND_PHI["D"], "equivariant ghost subtraction: -6 = -4 - 2")
print("  c_A = -2 - 1 = -3 (== 0 mod 3);  c_B = -2 + 1 = -1 (== 2 mod 3);  tr(T_C) = -2 (== 1 mod 3)")
print("  ind_phi: D=2, D(x)T_C=-4, A=-6, B=-2;  V-bundle route confirms ind_phi(Q) = -2")

# ==============================================================================================
# S3. RHO PACKAGES via the master formula (periodic S^1 structure; verified leg2/leg3 kernels)
# ==============================================================================================
banner("S3. Exact eta/rho/h/class for all four operators (D, D(x)T_C, A, B)")

# kernel data (verified in the prior swing: Hodge route + exhaustive integer forcing + referees)
KP = {"D": {F(0): 2}, "DTC": {}, "A": {F(0): -2}, "B": {}}
KM = {"D": {},
      "DTC": {F(0): 16, F(1, 3): 12, F(2, 3): 12},
      "A":   {F(0): 16, F(1, 3): 12, F(2, 3): 12},
      "B":   {F(0): 14, F(1, 3): 12, F(2, 3): 12}}

# carrier-B kernel forced three ways (design-3 gates, re-run here):
#  (i) twistor subtraction: iota embeds the 2 parallel (phi-trivial) spinors into ker^-(D(x)T_C)
km_b_sub = dict(KM["DTC"])
km_b_sub[F(0)] = km_b_sub[F(0)] - KP["D"][F(0)]
check(km_b_sub == KM["B"], "(i) ker^-(Q) = ker^-(D(x)T_C) - iota(ker^+(D)) = {0:14, 1/3:12, 2/3:12}")
#  (ii) integer forcing: m0 + 2 m1 = 38 (published dim ker Q), m0 - m1 = -ind_phi(Q) = 2
sols = [(m0, m1) for m0 in range(61) for m1 in range(61) if m0 + 2 * m1 == 38 and m0 - m1 == 2]
check(sols == [(14, 12)], "(ii) integer forcing UNIQUE: (m0, m1) = (14, 12)")
#  (iii) Hodge trace == Atiyah-Bott: tr(g|ker^+) - tr(g|ker^-) = ind_phi
for name in ("D", "DTC", "A", "B"):
    for m in (1, 2):
        check(tr_g(KP[name], m) - tr_g(KM[name], m) == IND_PHI[name],
              "(iii) %s: Hodge trace == Atiyah-Bott (g^%d)" % (name, m))
# non-equivariant closure: ind = dim ker^+ - dim ker^- (virtual where applicable)
IND = {"D": IND_D, "DTC": IND_DTC, "A": IND_A, "B": IND_B}
for name in ("D", "DTC", "A", "B"):
    tot = sum(KP[name].values()) - sum(KM[name].values())
    check(tot == IND[name], "%s: kernel data reproduces the index %d" % (name, IND[name]))
check(sum(KM["B"].values()) == 38, "carrier B kernel is HONEST: 38 actual RS fields (ker^+ = 0)")

ETA, RHO, H, CLS = {}, {}, {}, {}
for name in ("D", "DTC", "A", "B"):
    ETA[name] = [eta_alpha(KP[name], KM[name], k) for k in range(3)]
    RHO[name] = [e - ETA[name][0] for e in ETA[name]]
    H[name] = [h_of(KP[name], KM[name], k) for k in range(3)]
    CLS[name] = [z3_class(r) for r in RHO[name]]
    check(sum(ETA[name]) == 0, "%s: sum_k eta_k = 0" % name)
    check(RHO[name][2] == -RHO[name][1], "%s: rho_2 = -rho_1" % name)

check(ETA["D"] == [F(0), F(-2, 3), F(2, 3)] and CLS["D"] == [0, 1, 2],
      "Dirac: eta (0,-2/3,+2/3), classes (0,1,2)/3 NONZERO (verified leg2 package)")
check(ETA["DTC"] == [F(0), F(4, 3), F(-4, 3)] and CLS["DTC"] == [0, 1, 2],
      "D(x)T_C alone: eta (0,+4/3,-4/3), classes (0,1,2)/3 NONZERO -- the twist itself is live")
check(ETA["A"] == [F(0), F(2), F(-2)] and CLS["A"] == [0, 0, 0],
      "carrier A: eta (0,+2,-2), classes (0,0,0) 2-PRIMARY (verified leg3 package)")
check(ETA["B"] == [F(0), F(2, 3), F(-2, 3)] and CLS["B"] == [0, 2, 1],
      "carrier B: eta (0,+2/3,-2/3), classes (0,2,1)/3 NONZERO ORDER 3")
check(H["A"] == [14, 12, 12] and H["B"] == [14, 12, 12] and H["D"] == [2, 0, 0],
      "h: A virtual (14,12,12), B honest (14,12,12), D (2,0,0)")
for name in ("D", "DTC", "A", "B"):
    print("  %-4s eta=%s  rho=%s  h=%s  class=%s" % (name, ETA[name], RHO[name], H[name], CLS[name]))

# ==============================================================================================
# S4. WHERE THE ORDER-3 CLASS LIVES (the adjudication identity, computed not asserted)
# ==============================================================================================
banner("S4. The order-3 class lives ENTIRELY in the spin-1/2 slot: subtract kills it, add doubles it")

# eta-level additivity (exact reals): rho_B = rho_A + 2*rho_D; rho_A = rho_DTC - rho_D; etc.
for k in range(3):
    check(RHO["A"][k] == RHO["DTC"][k] - RHO["D"][k], "k=%d: rho_A = rho_DTC - rho_D exact" % k)
    check(RHO["B"][k] == RHO["DTC"][k] + RHO["D"][k], "k=%d: rho_B = rho_DTC + rho_D exact" % k)
    check(RHO["B"][k] == RHO["A"][k] + 2 * RHO["D"][k], "k=%d: rho_B = rho_A + 2 rho_D exact" % k)
# class-level: the twisted Dirac ALONE carries (0,1,2); the ghost unit carries (0,1,2);
# A = (0,1,2) - (0,1,2) = (0,0,0): the ghost subtraction cancels the order-3 class EXACTLY;
# B = (0,1,2) + (0,1,2) = (0,2,1): the geometric completion DOUBLES it.
for k in range(3):
    check(CLS["A"][k] == (CLS["DTC"][k] - CLS["D"][k]) % 3, "k=%d: class_A = class_DTC - class_D" % k)
    check(CLS["B"][k] == (CLS["DTC"][k] + CLS["D"][k]) % 3, "k=%d: class_B = class_DTC + class_D" % k)
    check(CLS["B"][k] == (CLS["A"][k] + 2 * CLS["D"][k]) % 3, "k=%d: class_B = class_A + 2*class_D" % k)
check(CLS["A"] == [0, 0, 0] and CLS["B"] != [0, 0, 0], "the fork is REAL: A dead, B live at order 3")
# multiplier decomposition mod 3 (the structural mechanism):
check((int(TR_TC.a) - 1) % 3 == 0 and (int(TR_TC.a) + 1) % 3 != 0,
      "mod-3 mechanism: -2 - 1 == 0 (A killed by the ghost -1); -2 + 1 == 2 (B left live by the +1)")
print("  class(D(x)T_C) = (0,1,2) LIVE;  ghost unit class(D) = (0,1,2)")
print("  A: (0,1,2) - (0,1,2) = (0,0,0)   -- the ghost spin-1/2 subtraction cancels the class EXACTLY")
print("  B: (0,1,2) + (0,1,2) = (0,2,1)   -- the reversed-chirality completion DOUBLES it")
print("  => the ENTIRE order-3 content of the generation arena rides on the ORIENTATION (-1 vs +1)")
print("     of one rank-2 spin-1/2 slot; both bulk pieces (T_C twist, spin-1/2 unit) are order-3 live")

# ==============================================================================================
# S5. CROSS-CHECKS: class law, Donnelly averaging, relabeling sweep, Z/24 arena map
# ==============================================================================================
banner("S5. Cross-checks (all exact): class law, Donnelly == direct, relabel sweep, arena map")

# class law rho_k == -(k/3)*ind mod Z (referee-derived in the prior swing, verified there)
for name in ("D", "DTC", "A", "B"):
    for k in (1, 2):
        check((RHO[name][k] + F(k * IND[name], 3)) % 1 == 0,
              "%s k=%d: class law rho_k == -(k/3)*ind mod Z" % (name, k))

# Donnelly isotypic averaging == direct (both operators of the fork, both characters)
def eta_gm(kp, km, m):
    return (tr_g(km, m) - tr_g(kp, m)) * ICOT[m]


for name in ("A", "B"):
    for k in range(3):
        tot = QZ(0)
        for m in (1, 2):
            tot = tot + zp(-k * m) * eta_gm(KP[name], KM[name], m)
        iso = QZ(F(1, 3)) * tot
        check(iso.b == 0 and iso == QZ(ETA[name][k]),
              "%s k=%d: Donnelly isotypic == direct EXACTLY" % (name, k))
check(eta_gm(KP["B"], KM["B"], 1) == QZ(2) * ICOT[1], "eta_g(Q) = 2 icot(pi/3): tr(g|ker Q) = 2")

# relabeling sweep (lift (x) zeta^m): class MULTISET invariant -- NONZERO/ZERO is convention-free
for m in range(3):
    for name, target in (("A", [0, 0, 0]), ("B", [0, 1, 2])):
        kp2, km2 = shift(KP[name], m), shift(KM[name], m)
        e2 = [eta_alpha(kp2, km2, k) for k in range(3)]
        c2 = sorted(z3_class(e - e2[0]) for e in e2)
        check(c2 == sorted(target), "m=%d: %s class multiset invariant" % (m, name))

# Z/24 arena map (leg4 convention: N = 16*a mod 24 on the class a)
E3 = 16
arena = {name: [(E3 * a) % 24 for a in CLS[name]] for name in ("D", "A", "B")}
check(arena["D"] == [0, 16, 8], "arena: Dirac N = (0,16,8) (verified leg4 value)")
check(arena["A"] == [0, 0, 0], "arena: carrier A N = (0,0,0)")
check(arena["B"] == [0, 8, 16], "arena: carrier B N = (0,8,16) -- inverse Dirac pattern")
print("  class law 8/8, Donnelly 6/6, relabel sweep 6/6, arena map: D (0,16,8) | A (0,0,0) | B (0,8,16)")

# ==============================================================================================
# S6. REPO-PIN LEDGER -- the identification-relevant sentences, read from the repo and asserted
# ==============================================================================================
banner("S6. Repo-pin ledger: what the prior campaigns actually pinned (checked against the files)")

REPO = r"C:\Users\joe\JB\CapacityOS\repos\public\gu-formalization"


def slurp(rel):
    p = os.path.join(REPO, rel)
    with io.open(p, "r", encoding="utf-8", errors="replace") as f:
        return f.read()


# P1: the verified rho machinery pins carrier A by the -42 gate (arithmetic = A everywhere)
leg3 = slurp(r"tests\rs-function-space\order3-rho\leg3_rs_rho.py")
check("21*sigma/8 = -42" in leg3 and "RS = D (x) (T_C X - C)" in leg3,
      "P1: leg3_rs_rho.py pins RS = D(x)(T_C - 1C) via the -42 = 21 sigma/8 gate (carrier A)")

# P2: the function-space SPEC uses carrier A's INDEX but names carrier B's BUNDLE
spec = slurp(r"canon\rs-function-space-framework-SPEC.md")
check("I_{3/2}[X] = 21*sigma/8" in spec,
      "P2a: rs-function-space SPEC pins the bulk index 21 sigma/8 (carrier A arithmetic)")
check("sections of `(T*X (x) S)_gamma-traceless`" in spec,
      "P2b: the SAME SPEC names the bundle 'gamma-traceless' -- that is carrier B's bundle")
# given the adjudicated LEG-A/LEG-B results (+ published HS Prop 3.1: the operator on the
# gamma-traceless bundle has index -38), P2a and P2b cannot both describe one object:
check(IND_A != IND_B, "P2c: PROVEN MISMATCH -- A-index prose attached to B-bundle prose")

# P3: the prior swing's stability claim (honest limit 1) is REFUTED by the adjudication
res = slurp(r"canon\order3-equivariant-rho-RESULTS.md")
check("stable under" in res and "gamma-traceless repackaging" in res,
      "P3a: order3-RESULTS claims index+class stability under the gamma-traceless repackaging")
check(CLS["A"] != CLS["B"] and IND_A != IND_B,
      "P3b: REFUTED -- the honest gamma-traceless operator moves BOTH the index (-42 -> -38) "
      "and the mod-Z class ((0,0,0) -> (0,2,1))")
check("-38 == 1 mod 3" in res,
      "P3c: the -38 thread was already named there as the unadjudicated escape (now adjudicated)")

# P4: the GU-native BRST apparatus that would JUSTIFY the ghost subtraction is itself missing
brst = slurp(r"absorbed\gu-source-action\RS-BRST-CARRIER-PACKET-2026-07-05.md")
check("MissingCarrierError" in brst and "missing_carrier_blocked" in brst,
      "P4: RS-BRST packet: the GU-native BV/BRST carrier raises MissingCarrierError (blocked)")

# P5: GU's own ghost parity cannot chiralize (consistency, not chirality)
gp = slurp(r"canon\swing-ghost-parity-no-chiral-selection.md")
check("ghost parity gives consistency, not chirality" in gp,
      "P5: ghost parity supplies consistency, not a chiral count (no-go, machine-checked)")

# P6: the interface pass criterion is exactly the shape carrier B now exhibits fiberwise
iface = slurp(r"canon\source-action-family-index-interface-SPEC.md")
check("N != 0 mod 3" in iface,
      "P6a: interface SPEC pass bar: families index N != 0 mod 3 WITHOUT chi import")
probe = slurp(r"tests\rs-function-space\family_generation_arena_probe.py")
check("21*sigma/8" in probe and "== 0 mod 3" in probe,
      "P6b: the arena probe's 'every honest number == 0 mod 3' sweep uses carrier-A densities")
check(IND_B % 3 != 0,
      "P6c: SCOPING NOTE -- under carrier B the honest FIBER index -38 !== 0 mod 3 (no chi import); "
      "the probe's blanket 2-primary statement is carrier-A-scoped, not carrier-free")

# P7: firewall doc blocks the target imports this leg must not use (and does not use)
de = slurp(r"absorbed\gu-source-action\DEAD-ENDS.md")
check("24 / 8 = 3" in de and "chi(K3) = 24" in de, "P7: DEAD-ENDS firewall lines present")
print("  P1..P7 all verified against the repo files (pins are as cited, not from memory)")

# ==============================================================================================
# S7. STEELMAN SCORECARD + IDENTIFICATION VERDICT (the deliverable; BLOCKED items honest)
# ==============================================================================================
banner("S7. Steelmen and the weakest-defensible identification verdict")

STEELMAN_A = [
    "A1. The generation count is a QFT statement; the physical (BRST-quantized) gravitino content",
    "    is ind D_TM - ind D (Witten's ghost subtraction, quoted verbatim in HS Remark 3.6).",
    "A2. Every prior in-repo number and gate is carrier-A arithmetic (P1, P2a, P6b): the -42 pin,",
    "    the rs_index_harness, the bulk-even theorem, the leg3 verdict. All of it stands, as A-facts.",
    "A3. The AGW anomaly density A-hat(ch T_C - 1) is the established published physics object;",
    "    if the GU arena is a path-integral/families-anomaly count, A is the honest carrier",
    "    and the order-3 channel is structurally dead (c_A = -3 == 0 mod 3 at every fixed point).",
]
COUNTER_A = [
    "A-. The ghost subtraction is supergravity's BRST bookkeeping. The GU-native BV/BRST carrier",
    "    that would justify importing it is ITSELF the missing carrier (P4: MissingCarrierError),",
    "    and GU's own ghost parity provably cannot chiralize (P5). Carrier A's mechanism is",
    "    borrowed from a theory GU has not been shown to contain.",
]
STEELMAN_B = [
    "B1. The repo's own function-space framing names sections of the GAMMA-TRACELESS bundle and",
    "    'the net chiral index of D_RS on L2-sections' (P2b). The unique formally self-adjoint",
    "    elliptic operator on that bundle is Q (Baer-Mazzeo); its index is -38 (HS Prop 3.1(i));",
    "    its kernel is 38 honest RS fields on K3. 'Zero modes of the arena operator' = ker Q.",
    "B2. Once the bundle is fixed, there is NO convention freedom: chirality-oddness of Clifford",
    "    contraction FORCES the reversed-chirality completion (+1), hence -38 and classes (0,2,1)/3.",
    "B3. The mathematics literature reserves 'the Rarita-Schwinger operator' for Q; the prior",
    "    campaigns' 'gamma-traceless' prose already described B's bundle while computing A (P2c).",
]
COUNTER_B = [
    "B-. Nothing in GU names Q either: the source action is unbuilt, so claiming B as THE carrier",
    "    is the same unproven identification step in the other direction. The prior swing's",
    "    warning against convention promotion applies symmetrically.",
]
for line in STEELMAN_A + COUNTER_A + STEELMAN_B + COUNTER_B:
    print(" " + line)

# the verdict is an identity question the arithmetic CANNOT settle -- record it as BLOCKED
BLOCKED.append(
    "SG4 MISSING-CARRIER (primary): the GU source-action operator is unbuilt; whether the "
    "generation-arena carrier is (A) the ghost-subtracted gravitino complex or (B) the geometric "
    "gamma-traceless Q is NOT decidable from any in-repo computed object. Both are published, "
    "internally coherent, and pass an established gate (21 sigma/8 physics vs 19 sigma/8 math), "
    "so the old freeze rationale 'the gate selects uniquely' no longer discriminates.")
BLOCKED.append(
    "GU-native ghost subtraction: carrier A's mechanism needs a GU BV/BRST carrier; the repo's "
    "own packet reports it missing (MissingCarrierError). Until built, A's ghost bookkeeping is "
    "an import from supergravity, not a GU derivation.")
BLOCKED.append(
    "Families-pushforward N over the metric fiber GL(4,R)/O(3,1) (interface SPEC bar): whether "
    "it inherits carrier B's mod-3 residue requires the unbuilt fibered geometry; the fiberwise "
    "-38 !== 0 mod 3 is a scoping note on the probe, NOT a pass of the families criterion.")

VERDICT = (
    "IDENTIFICATION_OPEN__BOTH_CARRIERS_STAND_AS_DIFFERENT_OBJECTS__ORDER3_RIDES_THE_SPIN_HALF_"
    "SLOT_ORIENTATION__A_PIN_STAYS_FROZEN_FOR_ANOMALY_GATES__B_IS_THE_GEOMETRIC_OPERATOR__"
    "DECISION_IS_SG4_NOT_ARITHMETIC")
print()
print("  WEAKEST-DEFENSIBLE VERDICT: " + VERDICT)
print()
print("  Operational consequences (description-level, no canon mutation performed by this leg):")
print("   1. All prior verdicts stand as facts about carrier A; nothing licenses replacing -42 by")
print("      -38 in canon (that would repeat the convention-freeze failure the prior swing warned")
print("      about). The 2-primary RS verdict is TRUE OF A and now PROVEN FALSE OF B.")
print("   2. Canon prose that calls the A-object 'the gamma-traceless RS' (P2b, P3a) is a proven")
print("      description-level mismatch and needs a correction note (index and class both move).")
print("   3. The generation-arena order-3 verdict is a single binary riding on SG4: ghost-subtract")
print("      => 2-primary; geometric-complete => order-3 nonzero, class (0,2,1)/3 = inverse Dirac.")

# ==============================================================================================
# S8. FIREWALL AUDIT (leg-local) + OUTPUT
# ==============================================================================================
banner("S8. Firewall audit + output")

NUMERIC_INPUTS = (6, -16, 3, 22, 2)     # fixed points, sigma, |G|, b2, ind D pin
check(24 not in NUMERIC_INPUTS, "FIREWALL: chi(K3) = 24 is not an input")
check(AHAT == 2 and AHAT != 3, "FIREWALL: A-hat(K3) = 2; flat A-hat = 3 never appears")
check(F(21 * SIGMA, 8) == -42 and F(19 * SIGMA, 8) == -38 and F(-SIGMA, 8) == 2,
      "FIREWALL: every /8 is a standard AS density (21s/8, 19s/8, -s/8); no 24/8 manufacture")
check(IND_B == IND_DTC + IND_D, "FIREWALL: -38 DERIVED as -40 + 2, never imported as a target")

print()
print("BLOCKED ITEMS (genuine, reported honestly -- the identification is not force-closable):")
for i, b in enumerate(BLOCKED, 1):
    print("  [%d] %s" % (i, b))

RESULT = {
    "fork": {"A": {"ind": IND_A, "c": str(C_A), "eta": [str(e) for e in ETA["A"]],
                   "class": CLS["A"], "arena": arena["A"]},
             "B": {"ind": IND_B, "c": str(C_B), "eta": [str(e) for e in ETA["B"]],
                   "class": CLS["B"], "arena": arena["B"]}},
    "where_order3_lives": "the rank-2 spin-1/2 slot orientation: class_B - class_A = 2*class_Dirac",
    "identity": "rho_B = rho_A + 2*rho_Dirac exact at eta level; [B]-[A] = 2[1C] in K-theory",
    "verdict": VERDICT,
    "blocked": len(BLOCKED),
}
print()
print("LEG-D OUTPUT:", RESULT)
print()
print("#" * 96)
print("# LEG-D COMPLETE: identification adjudicated as OPEN-BY-STRUCTURE (SG4), fork fully")
print("# computed: the order-3 class lives entirely in the +-1 spin-1/2 slot; A (0,0,0) 2-primary,")
print("# B (0,2,1)/3 nonzero, B = A + 2*Dirac exactly. hard asserts passed: %d; blocked: %d" % (NASSERT, len(BLOCKED)))
print("#" * 96)
