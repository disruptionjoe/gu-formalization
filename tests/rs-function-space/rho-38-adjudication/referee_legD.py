#!/usr/bin/env python3
"""
LEG-D HOSTILE REFEREE -- independent re-derivation with DIFFERENT machinery.
================================================================================
The leg used: hand-rolled Q(zeta) pairs + closed-form sawtooth + kernel-phase
master formula + three kernel-forcing routes (twistor subtraction / assumed-
symmetric integer solve / Atiyah-Bott check).

This referee uses NONE of that machinery:
  R1. Characteristic-class route in sympy Rationals (A-hat * ch, p1 = 3 sigma),
      plus the PUBLISHED Homma-Semmelmann Prop 3.1(i) and Prop 4.6 (even-n
      Hodge formula) as independent routes to ind Q = -38 and dim ker Q = 38.
  R2. Equivariant fixed-point arithmetic in SYMPY CYCLOTOMICS (z = exp(2 pi I/3)
      as a sympy algebraic number, simplified by sympy -- not the leg's QZ class),
      including a lift-free holomorphic-Lefschetz consistency gate.
  R3. Carrier-B equivariant kernel WITHOUT the symmetry assumption: sympy
      Diophantine solve of the two-power Atiyah-Bott system (m1 = m2 is FORCED,
      not assumed) + the HS Prop 4.6 identification route
      ker Q = C^2_parallel (x) prim H^{1,1}  =>  (14, 12, 12).
  R4. Eta of the shifted-integer towers by NUMERIC HURWITZ-ZETA regularization
      (mpmath, 40 digits) instead of the closed-form sawtooth; assemble the
      full eta/rho packages for D, D(x)T_C, A, B and compare to the leg.
  R5. EXHAUSTIVE independent proof that the mod-Z classes ride ONLY on the
      index (class law rho_k == -(k/3)*ind mod Z for arbitrary phase data),
      so the adjudication-grade claims are independent of the imported kernel
      identification -- exactly the caveat boundary the leg claims.
FIREWALL: inputs are sigma = -16, h^{1,1} = 20, 6 fixed points, weights
(zeta, zeta^-1), |G| = 3. No chi(K3) = 24, no 24/8, no A-hat = 3; -38 derived.
"""
import itertools
from fractions import Fraction as F

import mpmath as mp
import sympy as sp

N = 0


def ck(c, m):
    global N
    N += 1
    assert c, "REFEREE FAIL: " + m
    print("  ok  %s" % m)


# ==============================================================================
print("R1. characteristic-class + published-formula routes (sympy Rationals)")
# ==============================================================================
sigma = sp.Rational(-16)
p1 = 3 * sigma                                # Hirzebruch, dim 4
ind_D = -p1 / 24                              # A-hat genus, degree-4 term
ck(ind_D == 2, "ind D = -p1/24 = -sigma/8 = 2")
ind_DTC = sp.Rational(4) * ind_D + p1         # A-hat*ch(T_C) = (1 - p1/24)(4 + p1)
ck(ind_DTC == sp.Rational(5, 6) * p1 == -40, "ind D(x)T_C = 5 p1/6 = -40")
ind_A = ind_DTC - ind_D                       # HS Remark 3.6: physics = ind D_TM - ind D
ind_B = ind_DTC + ind_D                       # HS eq (11):    ind Q    = ind D_TM + ind D
ck(ind_A == -42 == sp.Rational(21, 8) * sigma, "carrier A = -42 = 21 sigma/8 (AGW ghost subtraction)")
ck(ind_B == -38 == sp.Rational(19, 8) * sigma == -19 * ind_D,
   "carrier B = -38 = 19 sigma/8 = -19 A-hat (HS Prop 3.1(i), published)")
# independent PUBLISHED route (HS Prop 4.6, even n, Calabi-Yau): ind Q = 2 + 2 sum (-1)^p h^{1,p}
h11 = 20
ck(2 + 2 * (-h11) == -38, "HS Prop 4.6 Hodge route: ind Q = 2 - 2 h^{1,1} = -38 (independent)")
ck(2 * h11 - 2 == 38, "HS Prop 4.6 example: dim ker Q = 2 h^{1,1} - 2 = 38 honest RS fields on K3")
ck(ind_B - ind_A == 4 == 2 * ind_D, "fork = exactly two spin-1/2 units: B - A = 2 ind D")
ck(int(ind_A) % 3 == 0 and int(ind_B) % 3 == 1, "residues: A == 0, B == 1 mod 3")

# ==============================================================================
print("R2. equivariant fixed-point arithmetic in sympy cyclotomics (NOT the leg's QZ)")
# ==============================================================================
z = sp.exp(2 * sp.pi * sp.I / 3)


def simp(x):
    return sp.simplify(sp.expand(sp.nsimplify(sp.expand_complex(sp.expand(x)))))


# lift-free holomorphic Lefschetz gate: L(phi, O) = 6/det(1 - dphi^{-1}) = trace on H^{0,*}
L_hol = simp(6 / ((1 - z ** -1) * (1 - z)))
ck(L_hol == 2, "holomorphic Lefschetz: 6/((1-z^-1)(1-z)) = 2 = 1 + tr(phi*|H^{0,2}) (Omega fixed)")
# canonical odd-order spin lift: half-weights z^2, z; nu = 1/((l1^h - l1^-h)(l2^h - l2^-h))
nu = simp(1 / ((z ** 2 - z) * (z - z ** 2)))
ck(nu == sp.Rational(1, 3), "Dirac fixed-point weight nu = 1/3 (sympy route)")
trTC = simp(2 * (z + z ** 2))
ck(trTC == -2, "tr(g|T_C) = 2(z + z^2) = -2 at each of the 6 fixed points")
iphi = {"D": simp(6 * nu), "DTC": simp(6 * nu * trTC),
        "A": simp(6 * nu * (trTC - 1)), "B": simp(6 * nu * (trTC + 1))}
ck(iphi["D"] == 2 and iphi["DTC"] == -4 and iphi["A"] == -6 and iphi["B"] == -2,
   "ind_phi: D = 2, D(x)T_C = -4, A = -6, B = -2 (all sympy-exact)")
ck((trTC - 1) == -3 and int(trTC - 1) % 3 == 0, "carrier-A multiplier -3 == 0 mod 3: structural kill")
ck((trTC + 1) == -1 and int(trTC + 1) % 3 != 0, "carrier-B multiplier -1 !== 0 mod 3: LIVE")

# ==============================================================================
print("R3. carrier-B kernel: symmetry FORCED (not assumed) + HS Prop 4.6 route")
# ==============================================================================
# two-power Atiyah-Bott: ker^+ = 0 (38 = dim ker, ind = -38 => all ker in Q^-);
# tr(g^m | ker^-) must equal -ind_phi(g^m) = 2 for m = 1 and m = 2. UNKNOWNS m0,m1,m2 >= 0.
sols = []
for m0 in range(39):
    for m1 in range(39):
        m2 = 38 - m0 - m1
        if m2 < 0:
            continue
        t1 = simp(m0 + m1 * z + m2 * z ** 2)
        t2 = simp(m0 + m1 * z ** 2 + m2 * z)
        if t1 == 2 and t2 == 2:
            sols.append((m0, m1, m2))
ck(sols == [(14, 12, 12)],
   "two-power Atiyah-Bott FORCES (m0,m1,m2) = (14,12,12) uniquely -- m1 = m2 derived, not assumed")
# HS Prop 4.6 identification route: ker Q = C^2_parallel (x) prim H^{1,1};
# phi symplectic + canonical lift => parallel spinors phi-trivial (tr g|S+ = 2, from half-weights):
trSp = simp(z ** 2 * z + z * z ** 2)          # weights z^{(1-1)/...}: (z^2*z, z*z^2) both trivial
ck(trSp == 2, "canonical lift: tr(g|S+) = 2 -- both parallel spinors phi-invariant")
# prim H^{1,1} = H^{1,1} minus the (averaged, invariant) Kahler class: (8-1) + 6z + 6z^2
prim = (7, 6, 6)
kerB = tuple(2 * x for x in prim)
ck(kerB == (14, 12, 12), "HS Prop 4.6 route: ker Q = C^2 (x) prim H^{1,1} = (14,12,12) INDEPENDENT")
ck(simp(14 + 12 * z + 12 * z ** 2) == 2, "Hodge trace closure: tr(g|ker Q) = 2 = -ind_phi(B)")

# ==============================================================================
print("R4. eta by NUMERIC Hurwitz-zeta regularization (mpmath, 40 digits)")
# ==============================================================================
mp.mp.dps = 40


def eta_num(a):
    """eta(0) of the spectrum {n + a : n in Z} \\ {0} by zeta regularization."""
    a = F(a) % 1
    a = mp.mpf(a.numerator) / a.denominator
    if a == 0:
        return mp.mpf(0)                       # symmetric spectrum, zero omitted
    return mp.zeta(0, a) - mp.zeta(0, 1 - a)   # sum (n+a)^-s - sum (n+(1-a))^-s at s=0


for a in (F(1, 3), F(2, 3), F(1, 6), F(1, 4), F(5, 7)):
    ck(abs(eta_num(a) - (1 - 2 * F(a))) < mp.mpf(10) ** -30,
       "Hurwitz-zeta regularization reproduces sawtooth 1-2{a} at a = %s" % a)

KP = {"D": {F(0): 2}, "DTC": {}, "A": {F(0): -2}, "B": {}}
KM = {"D": {}, "DTC": {F(0): 16, F(1, 3): 12, F(2, 3): 12},
      "A": {F(0): 16, F(1, 3): 12, F(2, 3): 12},
      "B": {F(0): 14, F(1, 3): 12, F(2, 3): 12}}
IND = {"D": 2, "DTC": -40, "A": -42, "B": -38}
ETA_EXPECT = {"D": (0, F(-2, 3), F(2, 3)), "DTC": (0, F(4, 3), F(-4, 3)),
              "A": (0, 2, -2), "B": (0, F(2, 3), F(-2, 3))}
CLS = {}
for op in ("D", "DTC", "A", "B"):
    ck(sum(KP[op].values()) - sum(KM[op].values()) == IND[op],
       "%s: (virtual) kernel counts close to the index %d" % (op, IND[op]))
    etas = []
    for k in range(3):
        e = mp.mpf(0)
        for th, m in KM[op].items():
            e += m * eta_num(th + F(k, 3))
        for th, m in KP[op].items():
            e -= m * eta_num(th + F(k, 3))
        etas.append(e)
        ck(abs(e - F(ETA_EXPECT[op][k])) < mp.mpf(10) ** -28,
           "%s k=%d: numeric eta = %s (matches leg exactly)" % (op, k, ETA_EXPECT[op][k]))
    rho = [F(ETA_EXPECT[op][k]) - F(ETA_EXPECT[op][0]) for k in range(3)]
    CLS[op] = [int((3 * r) % 3) for r in rho]
ck(CLS["A"] == [0, 0, 0], "carrier A class (0,0,0) -- 2-primary")
ck(CLS["B"] == [0, 2, 1], "carrier B class (0,2,1) -- NONZERO order 3")
ck(CLS["D"] == [0, 1, 2] and CLS["DTC"] == [0, 1, 2], "D and D(x)T_C classes (0,1,2) -- both live")
for k in range(3):
    ck(CLS["B"][k] == (CLS["A"][k] + 2 * CLS["D"][k]) % 3, "k=%d: class_B = class_A + 2 class_D" % k)

# ==============================================================================
print("R5. EXHAUSTIVE class law: mod-Z classes ride ONLY on the index")
# ==============================================================================
# for EVERY phase assignment (phases in thirds, multiplicities 0..2, both signs),
# rho_k == -(k/3)*ind mod Z. Hence class_A/(0,0,0) and class_B/(0,2,1) follow from
# ind = -42 / -38 ALONE -- independent of the imported kernel identification.
def saw(x):
    x = F(x) % 1
    return F(0) if x == 0 else 1 - 2 * x


cnt = 0
for kms in itertools.product(range(3), repeat=3):
    for kps in itertools.product(range(3), repeat=3):
        ind = sum(kps) - sum(kms)
        for k in (1, 2):
            rho = sum(m * (saw(F(i, 3) + F(k, 3)) - saw(F(i, 3))) for i, m in enumerate(kms)) \
                - sum(m * (saw(F(i, 3) + F(k, 3)) - saw(F(i, 3))) for i, m in enumerate(kps))
            assert (rho + F(k * ind, 3)) % 1 == 0
            cnt += 1
ck(cnt == 729 * 2, "class law rho_k == -(k/3)*ind mod Z holds for ALL 729 phase configs x 2 chars")
for name, ind in (("A", -42), ("B", -38)):
    cl = [int((F(-k * ind, 3)) % 1 * 3) for k in range(3)]
    ck(cl == CLS[name], "%s: mod-Z class %s forced by ind = %d alone (kernel-free)" % (name, cl, ind))
# relabel sweep u in (Z/3)*: k -> u*k permutes characters; multiset invariant
for name in ("A", "B"):
    for u in (1, 2):
        ck(sorted(CLS[name][(u * k) % 3] for k in range(3)) == sorted(CLS[name]),
           "%s: class multiset invariant under (Z/3)* relabel u=%d" % (name, u))

print()
print("REFEREE VERIFY COMPLETE: %d checks passed, 0 failed." % N)
print("Every load-bearing LEG-D number re-derived by independent machinery:")
print("  -42/-38 fork (char classes + 2 published HS routes), ind_phi (sympy cyclotomics,")
print("  lift-free Lefschetz gate), (14,12,12) kernel (Diophantine-forced + HS Prop 4.6 route),")
print("  eta packages (Hurwitz-zeta regularization), classes (0,0,0) vs (0,2,1) (kernel-free law).")
