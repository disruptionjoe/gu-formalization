#!/usr/bin/env python3
# -*- coding: ascii -*-
"""
HOSTILE-REFEREE independent verification of LEG-C (equivariant rho of the geometric
gamma-traceless RS operator Q).  DIFFERENT MACHINERY from the leg on purpose:
  * sympy exact arithmetic (Rational, sqrt(3), exp(2*pi*I/3)) -- not the leg's hand-rolled
    Q(i,zeta) tower;
  * chiral/Weyl gamma representation from Pauli matrices -- not the leg's quaternionic model;
  * spin lift built by EXPONENTIATING the spin generators cos(t/2)+sin(t/2)g_i g_j -- not the
    leg's diagonal ansatz + intertwiner sweep;
  * Dirac density via the LIFT-FREE holomorphic Lefschetz route (S = Lambda^{0,*}, K trivial
    on K3) -- no half-weight convention at all;
  * circle eta re-derived from HURWITZ ZETA analytic continuation (zeta(0,a) = 1/2 - a),
    not the imported closed form;
  * Donnelly averaging with sympy cot(pi/3) trig exactness.
Every load-bearing LEG-C number is re-derived: multiplier -1, ind_phi(Q) = -2 (three ways),
kernel phases (14,12,12) (integer forcing + rep routes), eta = rho = (0,2/3,-2/3),
classes (0,2,1), convention A alongside (0,+2,-2)/(0,0,0), Dirac (0,-2/3,+2/3)/(0,1,2),
candidate link, class law, disk-route parity.
"""
import sympy as sp
from sympy import Rational as R, I, sqrt, pi, cos, sin, cot, exp, zeta, simplify, eye, zeros, Matrix

NCHK = 0
def chk(c, m):
    global NCHK
    NCHK += 1
    assert c, "REFEREE FAIL: " + m

z3 = exp(2*pi*I/3)          # zeta
def zp(e):                   # zeta^e, exact, in algebraic a+bI form (simplify-safe)
    return sp.simplify(sp.expand_complex(z3**(e % 3)))
chk(zp(1) == R(-1, 2) + sqrt(3)*I/2, "zeta algebraic form")
chk(sp.simplify(zp(1)*zp(2)) == 1 and sp.simplify(zp(1) + zp(2)) == -1, "zeta identities")

# ------------------------------------------------------------------------------------------
# PART 1: chiral gamma rep from Pauli matrices; exponential spin lift; multiplier from traces
# ------------------------------------------------------------------------------------------
s1 = Matrix([[0, 1], [1, 0]])
s2 = Matrix([[0, -I], [I, 0]])
s3 = Matrix([[1, 0], [0, -1]])
id2 = eye(2)
# a_mu = (1, -i s1, -i s2, -i s3); gamma_mu = [[0, -a_mu^dag], [a_mu, 0]]  => {g_mu, g_nu} = -2 delta
A = [id2, -I*s1, -I*s2, -I*s3]
def gam(mu):
    G = zeros(4, 4)
    Ad = A[mu].H
    G[0:2, 2:4] = -Ad
    G[2:4, 0:2] = A[mu]
    return G
G4 = [gam(mu) for mu in range(4)]
n_rel = 0
for mu in range(4):
    for nu in range(4):
        anti = sp.simplify(G4[mu]*G4[nu] + G4[nu]*G4[mu])
        chk(anti == (-2 if mu == nu else 0)*eye(4), "Clifford (%d,%d)" % (mu, nu))
        n_rel += 1
chk(n_rel == 16, "16 relations")
# chirality blocks: indices 0,1 = S+; 2,3 = S-  (gamma odd: block off-diagonal) -- verified:
for mu in range(4):
    chk(G4[mu][0:2, 0:2] == zeros(2, 2) and G4[mu][2:4, 2:4] == zeros(2, 2), "gamma odd")

th = 2*pi/3
def spin_rot(i, j, t):
    """spin lift of rotation by t in plane (e_i, e_j): cos(t/2) + sin(t/2) gamma_i gamma_j"""
    return sp.simplify(cos(t/2)*eye(4) + sin(t/2)*G4[i]*G4[j])

def so_rot(i, j, t):
    Rm = eye(4)
    Rm[i, i] = cos(t); Rm[j, j] = cos(t)
    Rm[i, j] = -sin(t); Rm[j, i] = sin(t)
    return Rm

# try both relative orientations of the two rotation planes; select the one with S+ trivial
sel = None
for sgn in (+1, -1):
    gS = sp.simplify(spin_rot(0, 1, th) * spin_rot(2, 3, sgn*th))
    gT = sp.simplify(so_rot(0, 1, th) * so_rot(2, 3, sgn*th))
    chk(sp.simplify(gS**3) == eye(4), "g_S^3 = 1 (sgn %+d)" % sgn)
    chk(sp.simplify(gT**3) == eye(4), "g_T^3 = 1 (sgn %+d)" % sgn)
    # intertwining: g_S gamma(xi) g_S^-1 = gamma(gT xi)  (check on basis vectors)
    gSi = gS.inv()
    for t in range(4):
        lhs = sp.simplify(gS*G4[t]*gSi)
        rhs = sp.simplify(sum((gT[mu, t]*G4[mu] for mu in range(4)), zeros(4, 4)))
        chk(sp.simplify(lhs - rhs) == zeros(4, 4), "intertwine col %d (sgn %+d)" % (t, sgn))
    trSp = sp.simplify(gS[0, 0] + gS[1, 1])
    trSm = sp.simplify(gS[2, 2] + gS[3, 3])
    if sp.simplify(trSp - 2) == 0:
        sel = (sgn, gS, gT, trSp, trSm)
chk(sel is not None, "exactly one orientation gives S+ trivial (exp-lift route)")
sgn, gS, gT, trSp, trSm = sel
chk(sp.simplify(trSm + 1) == 0, "tr(g|S-) = -1 (weights zeta, zeta^2)")
trT = sp.simplify(gT.trace())
chk(sp.simplify(trT + 2) == 0, "tr(g|T_C) = -2")
detT = sp.simplify((eye(4) - gT).det())
chk(sp.simplify(detT - 9) == 0, "det(1 - g|T) = 9")

# multiplier of Q vs A -- the adjudicated numbers:
mult_B = sp.simplify(trT + 1)   # geometric
mult_A = sp.simplify(trT - 1)   # ghost-subtracted
chk(mult_B == -1, "GEOMETRIC multiplier tr(T_C) + 1 = -1")
chk(mult_A == -3, "convention A multiplier tr(T_C) - 1 = -3")
chk(int(mult_B) % 3 != 0 and int(mult_A) % 3 == 0, "-1 not divisible by 3; -3 divisible")

# contraction, embedding, projector in THIS rep (independent construction):
# S (x) T index: 4*s + t
C = zeros(4, 16)
for a in range(4):
    for s in range(4):
        for t in range(4):
            C[a, 4*s + t] = G4[t][a, s]
IO = zeros(16, 4)
for s in range(4):
    for t in range(4):
        for b in range(4):
            IO[4*s + t, b] = -R(1, 4)*G4[t][s, b]
chk(sp.simplify(C*IO - eye(4)) == zeros(4, 4), "c iota = 1")
P = sp.simplify(eye(16) - IO*C)
chk(sp.simplify(P*P - P) == zeros(16, 16), "P^2 = P")
chk(P.rank() == 12, "rank V = 12")
# chirality bookkeeping: c odd, iota reverses
for a in (0, 1):
    for s in (0, 1):
        for t in range(4):
            chk(C[a, 4*s + t] == 0, "c odd (+)")
for b in (0, 1):
    for s in (0, 1):
        for t in range(4):
            chk(IO[4*s + t, b] == 0, "iota reverses (+ -> -)")
G16 = sp.simplify(sp.kronecker_product(gS, gT))
chk(sp.simplify(G16*P - P*G16) == zeros(16, 16), "[P, g] = 0 (splitting g-invariant)")
GP = sp.simplify(G16*P)
trVp = sp.simplify(sum(GP[i, i] for i in range(8)))
trVm = sp.simplify(sum(GP[i, i] for i in range(8, 16)))
chk(sp.simplify(trVp + 3) == 0, "tr(g|V+) = -3")
chk(sp.simplify(trVm) == 0, "tr(g|V-) = 0")
chk(sp.simplify(trVp - trVm - (trSp - trSm)*(trT + 1)) == 0,
    "character identity (trV+ - trV-) = (trS+ - trS-)(trT_C + 1)")
# Atiyah-Bott general Lefschetz form for the elliptic operator Q, 6 simple fixed points:
ind_phi_Q_model = sp.simplify(6*(trVp - trVm)/detT)
chk(ind_phi_Q_model == -2, "AB: ind_phi(Q) = 6*(-3)/9 = -2 (exp-lift + Pauli rep route)")
print("PART 1 OK: exp-lift chiral-rep model: mult_B = -1, mult_A = -3, tr(g|V+-) = (-3, 0), "
      "ind_phi(Q) = -2")

# ------------------------------------------------------------------------------------------
# PART 2: LIFT-FREE holomorphic-Lefschetz densities (no spin-lift convention anywhere)
#   K3: K trivial => S+- = Lambda^{0,even/odd}; T^{1,0} weights (z, z^2) at all 6 points.
# ------------------------------------------------------------------------------------------
w = [zp(1), zp(2)]                                    # T^{1,0} weights
wb = [zp(2), zp(1)]                                   # conjugates: zbar = z^2 exactly for |z|=1 cube root
chk(sp.simplify(sp.expand_complex(sp.conjugate(w[0]) - wb[0])) == 0, "zbar = z^2 (sanity)")
tr_S_diff = sp.simplify(sp.expand((1 - wb[0])*(1 - wb[1])))
chk(sp.simplify(tr_S_diff - 3) == 0, "tr(S+ - S-) = (1 - zbar1)(1 - zbar2) = 3 (lift-free)")
detR = sp.simplify(sp.expand((1 - w[0])*(1 - w[1])*(1 - wb[0])*(1 - wb[1])))
chk(sp.simplify(detR - 9) == 0, "det(1 - g|T_R) = 9 (lift-free)")
dens_D = sp.simplify(tr_S_diff/detR)
chk(sp.simplify(dens_D - R(1, 3)) == 0, "Dirac density = 1/3, no lift used")
trTC = sp.simplify(sp.expand(w[0] + w[1] + wb[0] + wb[1]))
chk(sp.simplify(trTC + 2) == 0, "tr(g|T_C) = -2 (weights route)")
IND = {}
IND["D"] = sp.simplify(6*dens_D)
IND["DTM"] = sp.simplify(6*dens_D*trTC)
IND["Q"] = sp.simplify(6*dens_D*(trTC + 1))
IND["A"] = sp.simplify(6*dens_D*(trTC - 1))
chk(IND["D"] == 2, "ind_phi(D) = 2 LIFT-FREE == operational pin")
chk(IND["DTM"] == -4, "ind_phi(D_TM) = -4")
chk(IND["Q"] == -2, "ind_phi(Q) = -2 LIFT-FREE == Part 1 model route")
chk(IND["A"] == -6, "ind_phi(A) = -6 (convention A coherent value)")
chk(sp.simplify(IND["Q"] - (IND["DTM"] - (-IND["D"]))) == 0,
    "equivariant additivity with REVERSED chirality: -2 = -4 - (-2)")
chk(sp.simplify(IND["DTM"] - (-IND["D"]) - (IND["DTM"] - IND["D"])) != 0,
    "reversal is detectable: -4 + 2 != -4 - 2 (negative control -6 = A's value)")
# g^2 power check (weights conjugate):
w2 = [zp(2), zp(4)]
w2b = [zp(1), zp(2)]
trTC2 = sp.simplify(sp.expand(w2[0] + w2[1] + w2b[0] + w2b[1]))
chk(sp.simplify(trTC2 + 2) == 0, "tr(g^2|T_C) = -2 (both powers)")
print("PART 2 OK: lift-free holomorphic-Lefschetz: ind_phi (D, DTM, Q, A) = (2, -4, -2, -6)")

# ------------------------------------------------------------------------------------------
# PART 3: non-equivariant indices from sigma = -16 only; -38 derived; published gates
# ------------------------------------------------------------------------------------------
sig = -16
p1 = 3*sig
indD = R(-sig, 8);      chk(indD == 2, "ind D = 2")
indDTM = R(5*p1, 6);    chk(indDTM == -40, "ind D_TM = -40")
indQ = indDTM + indD;   chk(indQ == -38, "ind Q = -38 (additivity, BM eq: ind D_TM+ = ind D- + ind Q+)")
chk(indQ == R(19*sig, 8), "ind Q = 19 sigma/8 (published HS Prop 3.1(i))")
indA = R(7*p1, 8);      chk(indA == -42 == R(21*sig, 8), "ind A = -42 = 21 sigma/8 (physics)")
chk(indQ % 3 == 1 and indA % 3 == 0, "residues: -38 == 1, -42 == 0 mod 3")
chk(indQ - indA == 2*indD, "candidate link at index level: [T_C+1]-[T_C-1] = 2[1]")
print("PART 3 OK: indices (2, -40, -38, -42); -38 = 19 sigma/8 published; link -38 = -42 + 4")

# ------------------------------------------------------------------------------------------
# PART 4: kernel phases -- integer forcing + rep routes, independent re-derivation
# ------------------------------------------------------------------------------------------
# Lefschetz forcing of (r,s): 2 + r - s/2 = 6, r + s = 22
sols = [(r_, 22 - r_) for r_ in range(0, 23) if R(2) + r_ - R(22 - r_, 2) == 6 and (22 - r_) % 2 == 0]
chk(sols == [(10, 12)], "(r,s) = (10,12) forced by Lefschetz = 6")
H11 = {0: 10 - 2, 1: 6, 2: 6}                       # trivial, zeta, zeta^2 in H^{1,1}
chk(sum(H11.values()) == 20, "h^{1,1} = 20")
PRIM = {0: 7, 1: 6, 2: 6}                            # Kahler class phi-trivial
chk(2*sum(PRIM.values()) == 38, "2 x primitive = 38 == published dim ker Q")
KQ = {0: 2*PRIM[0], 1: 2*PRIM[1], 2: 2*PRIM[2]}      # both copy-assignments same multiset
KQ_conj = {0: PRIM[0] + PRIM[0], 1: PRIM[1] + PRIM[2], 2: PRIM[2] + PRIM[1]}
chk(KQ == KQ_conj == {0: 14, 1: 12, 2: 12}, "rep route: ker Q phases {0:14, z:12, z2:12}")
# integer forcing (uses only dim = 38, reality, and ind_phi(Q) = -2 from Parts 1-2):
forced = [(m0, m1) for m0 in range(39) for m1 in range(39)
          if m0 + 2*m1 == 38 and m0 - m1 == 2]
chk(forced == [(14, 12)], "integer forcing unique: (14, 12)")
# ker^+ = 0 forced: |ind| = 38 = dim ker  =>  one-sided kernel
chk(abs(int(indQ)) == 38, "|ind Q| = dim ker Q => ker is one-sided (ker^+ = 0)")
# Hodge trace gate: ind_phi = -(tr g|ker^-) = -(14 + 12 z + 12 z^2) = -(14 - 12) = -2
trker = sp.simplify(14 + 12*zp(1) + 12*zp(2))
chk(sp.simplify(trker - 2) == 0 and sp.simplify(-trker - IND["Q"]) == 0,
    "Hodge trace == AB == -2 (gate closes)")
# twistor-subtraction route: {16,12,12} - {2,0,0} (iota of the 2 phi-trivial parallel spinors)
KDTM = {0: 16, 1: 12, 2: 12}
chk({k: KDTM[k] - (2 if k == 0 else 0) for k in KDTM} == KQ,
    "twistor subtraction route agrees: 40 = 2 + 38 phase-wise")
print("PART 4 OK: ker^-(Q) = {0:14, z:12, z2:12}, ker^+ = 0 -- forced independently")

# ------------------------------------------------------------------------------------------
# PART 5: circle eta from HURWITZ ZETA analytic continuation (independent of imported 1-2t)
#   eta(theta) = zeta_H(0, theta) - zeta_H(0, 1 - theta) for theta in (0,1); 0 at theta = 0
# ------------------------------------------------------------------------------------------
def eta_circle(theta):
    t = sp.Rational(theta) % 1
    if t == 0:
        return R(0)
    return sp.simplify(zeta(0, t) - zeta(0, 1 - t))

chk(eta_circle(R(1, 3)) == R(1, 3), "Hurwitz: eta(1/3) = 1/3")
chk(eta_circle(R(2, 3)) == R(-1, 3), "Hurwitz: eta(2/3) = -1/3")
chk(eta_circle(0) == 0, "eta(0) = 0")
chk(sp.simplify(zeta(0, R(1, 3)) - (R(1, 2) - R(1, 3))) == 0, "zeta_H(0,a) = 1/2 - a spot")

def eta_k(km, kp, k):
    tot = R(0)
    for ph, m in km.items():
        tot += m*eta_circle(R(ph, 3) + R(k, 3))
    for ph, m in kp.items():
        tot -= m*eta_circle(R(ph, 3) + R(k, 3))
    return tot

def hdim(km, kp, k):
    return sum(m for ph, m in list(km.items()) + list(kp.items()) if (R(ph, 3) + R(k, 3)) % 1 == 0)

# operators: (ker_minus phases in units of 1/3, ker_plus)
OPS = {
    "Q":     ({0: 14, 1: 12, 2: 12}, {}),
    "A":     ({0: 16, 1: 12, 2: 12}, {0: -2}),       # virtual: A = D_TM - D; ker^+(A) = 0 - 2 = -2
    "Dirac": ({}, {0: 2}),
}
ETA = {nm: [eta_k(km, kp, k) for k in range(3)] for nm, (km, kp) in OPS.items()}
HH = {nm: [hdim(km, kp, k) for k in range(3)] for nm, (km, kp) in OPS.items()}
chk(ETA["Q"] == [0, R(2, 3), R(-2, 3)], "Q: eta = (0, 2/3, -2/3) [Hurwitz route]")
chk(ETA["A"] == [0, 2, -2], "A: eta = (0, 2, -2) [reproduces prior verified swing]")
chk(ETA["Dirac"] == [0, R(-2, 3), R(2, 3)], "Dirac: eta = (0, -2/3, 2/3)")
chk(HH["Q"] == [14, 12, 12] and HH["Dirac"] == [2, 0, 0], "h dims")
RHO = {nm: [e - ETA[nm][0] for e in ETA[nm]] for nm in ETA}
def cls(r):
    v = (3*r) % 3
    chk(v == int(v), "class integral")
    return int(v)
CL = {nm: [cls(r) for r in RHO[nm]] for nm in RHO}
chk(CL["Q"] == [0, 2, 1], "Q classes (0,2,1) NONZERO order 3")
chk(CL["A"] == [0, 0, 0], "A classes (0,0,0) 2-primary")
chk(CL["Dirac"] == [0, 1, 2], "Dirac classes (0,1,2)")
print("PART 5 OK: Hurwitz-zeta eta assembly: Q (0,2/3,-2/3)/(0,2,1); A (0,2,-2)/(0,0,0); "
      "Dirac (0,-2/3,2/3)/(0,1,2)")

# ------------------------------------------------------------------------------------------
# PART 6: Donnelly isotypic averaging with sympy trig (exact cot(pi/3)) == direct
# ------------------------------------------------------------------------------------------
for nm, (km, kp) in OPS.items():
    for k in range(3):
        tot = sp.Integer(0)
        for m in (1, 2):
            trm = sp.simplify(sum(mu*zp(ph*m) for ph, mu in km.items())
                              - sum(mu*zp(ph*m) for ph, mu in kp.items()))
            tot += zp(-k*m) * (I*cot(pi*m/3)) * trm
        iso = sp.simplify(tot/3)
        chk(sp.simplify(iso - ETA[nm][k]) == 0, "Donnelly == direct: %s k=%d" % (nm, k))
print("PART 6 OK: Donnelly averaging (sympy trig) == Hurwitz direct, 9/9")

# ------------------------------------------------------------------------------------------
# PART 7: class law, candidate link, disk parity
# ------------------------------------------------------------------------------------------
INDX = {"Q": indQ, "A": indA, "Dirac": indD}
for nm in OPS:
    for k in (1, 2):
        chk((RHO[nm][k] + R(k, 3)*INDX[nm]) % 1 == 0,
            "class law %s k=%d: rho == -(k/3) ind mod Z" % (nm, k))
for k in range(3):
    chk(sp.simplify(ETA["Q"][k] - ETA["A"][k] - 2*ETA["Dirac"][k]) == 0,
        "candidate link eta(Q) = eta(A) + 2 eta(Dirac), k=%d" % k)
    chk(CL["Q"][k] == (CL["A"][k] + 2*CL["Dirac"][k]) % 3, "link at class level, k=%d" % k)
# disk route parity (leg's local-data route): rho_fp(Q) = (-4/3, +4/3); differs by even ints
disk = {1: R(-4, 3), 2: R(4, 3)}
for k in (1, 2):
    chk((disk[k] - RHO["Q"][k]) % 2 == 0, "disk - direct in 2Z, k=%d" % k)
    chk(cls(disk[k]) == CL["Q"][k], "disk class == direct class, k=%d" % k)
# disk values recomputed from local data with the geometric multiplier:
nu6 = {m: sp.simplify(R(1, 3) * 1/(zp(2*m) - zp(m))) for m in (1, 2)}
for k in (1, 2):
    tot = sp.Integer(0)
    for m in (1, 2):
        tot += (zp(-k*m) - 1) * 12 * nu6[m] * (-1)     # c_B = -1
    v = sp.simplify(tot/3)
    chk(sp.simplify(v - disk[k]) == 0, "disk route recomputed from local data, k=%d" % k)
print("PART 7 OK: class law, candidate link, disk parity + local-data recompute all pass")

print()
print("REFEREE INDEPENDENT VERIFICATION: %d checks passed, 0 failed." % NCHK)
print("Every load-bearing LEG-C number re-derived with different machinery:")
print("  multiplier -1 / -3 (exp-lift Pauli model AND lift-free weights route)")
print("  ind_phi(Q) = -2 (AB model route, lift-free Lefschetz, additivity, Hodge trace)")
print("  ker^-(Q) = (14,12,12), ker^+ = 0 (integer forcing, rep route, twistor subtraction)")
print("  eta(Q) = (0, 2/3, -2/3) via Hurwitz zeta; classes (0,2,1) NONZERO")
print("  A stays (0,2,-2)/(0,0,0); Dirac (0,-2/3,2/3)/(0,1,2); link exact; disk parity OK")
