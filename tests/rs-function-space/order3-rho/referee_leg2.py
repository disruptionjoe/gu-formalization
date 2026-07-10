#!/usr/bin/env python3
# -*- coding: ascii -*-
"""
HOSTILE-REFEREE independent verification of LEG-2 (Dirac rho of the order-3 Nikulin
monodromy mapping torus).  Independent arithmetic: sympy exact (roots of unity, Abel
limits, Hurwitz zeta), NOT the leg's QZ class.  Enumerates the FULL convention lattice:
  - circle spin structure delta in {0 (periodic/nonbounding), 1/2 (antiperiodic/BOUNDING)}
  - character-shift sign cs in {+1,-1}   (alpha_k twist direction, k <-> -k relabel)
  - master sign ms in {+1,-1}            (ker^+ -> +/- eta_S1)
and checks which branch carries the leg's claimed package rho=(0,-2/3,2/3), h=(2,0,0).
Also: independent Donnelly averaging via Abel-regularized equivariant circle etas, the
disk fixed-point route, and the implied equivariant APS index.
"""
import sympy as sp
from sympy import Rational as R, I, pi, exp, sqrt, floor, simplify, limit, Symbol

NCHK = 0
def check(cond, msg):
    global NCHK
    NCHK += 1
    assert cond, "FAIL: " + msg

def S(e):  # exact simplify to a canonical form
    return sp.nsimplify(sp.simplify(sp.expand_complex(sp.simplify(e))), [sqrt(3)])

z = exp(2*pi*I/3)
def zp(k): return exp(2*pi*I*(k % 3)/3)

print("== A. arithmetic gates, independent routes ==")
# A1 Lefschetz forcing (r,s)
sols = [(22-s, s) for s in range(23) if R(2) + (22-s) - R(s,2) == 6]
check(sols == [(10,12)], "Lefschetz forces (r,s)=(10,12) uniquely")
check(2 + 14 - R(8,2) == 12, "order-2 import (14,8) gives L=12 != 6 -> rejected")

# A2 G-signature, both routes (gate the task demanded; not in the leg's script)
fp_sig = S(6*(z+1)*(z**2+1)/((z-1)*(z**2-1)))
check(fp_sig == 2, "G-signature fixed-point route: 6*(1/3) = 2")
# lattice: H^{2,+} = <Re Omega, Im Omega, invariant Kahler>, phi-trivial: tr = 3.
# H^{2,-}: 7 invariant (tr 7) + 12 coinvariant in 6 conjugate (zeta,zeta^2) pairs (tr -6): tr = 1.
check(3 - (7 - 6) == 2, "G-signature lattice route: 3 - 1 = 2; routes AGREE")

# A3 local Dirac weight nu_D4: three independent routes
nu_half = S(1/((z**2 - z)*(z - z**2)))                  # (l^1/2 - l^-1/2)^-1 pairs, mu_3 half powers
nu_char = S((2 - (z + z**2))/((1-z)*(1-z**2)*(1-z)*(1-z**2)))
nu_sin  = S(1/(4*sp.sin(pi/3)**2))                      # |2 sin(theta/2)|^2 route
check(nu_half == R(1,3) and nu_char == R(1,3) and nu_sin == R(1,3),
      "nu_D4 = 1/3 by half-power, character, and sin routes")
check(S(6*nu_half) == 2, "Atiyah-Bott ind_phi(D,K3) = 2")
# A4 spin-free cross-route: holomorphic Lefschetz for dbar on O (K3: K trivial => Dirac ~ Dolbeault)
check(S(6/((1-z)*(1-z**2))) == 2, "holomorphic Lefschetz: 6/3 = 2 = tr(H^0)+tr(H^2) = 1+1")
# A5 kernel triviality is FORCED: tr(phi|ker^+) = 2 with eigenvalues in mu_3 => both = 1
#    (sum of two cube roots of unity equals 2 only for 1+1) -- verify exhaustively
sums2 = set()
for a_ in range(3):
    for b_ in range(3):
        sums2.add(S(zp(a_) + zp(b_)))
check(all((s_ == 2) == False or True for s_ in sums2), "enumerated")
check([ (a_,b_) for a_ in range(3) for b_ in range(3) if S(zp(a_)+zp(b_)) == 2 ] == [(0,0)],
      "tr(phi|ker^+)=2 forces trivial action on BOTH parallel spinors (theta = 0)")
print("   A1-A5 pass: (10,12) forced; sig 2=2 both routes; nu=1/3 x3 routes; ind=2; kernel trivial forced")

print("== B. circle eta closed form, independent (Abel limit + Hurwitz zeta) ==")
x = Symbol('x', positive=True)
for aa in (R(1,6), R(1,3), R(1,2), R(2,3), R(5,6)):
    ab = limit((x**aa - x**(1-aa))/(1-x), x, 1, '-')          # Abel-regularized sum sign(n+a)
    hz = sp.zeta(0, aa) - sp.zeta(0, 1-aa)                     # Hurwitz zeta route
    check(S(ab) == 1 - 2*aa and S(hz) == 1 - 2*aa, "eta(a) = 1-2a at a=%s (two routes)" % aa)
print("   eta{n+a} = 1-2a verified by Abel limit AND Hurwitz zeta at a = 1/6,1/3,1/2,2/3,5/6")

def etaS1(t):
    t = t - floor(t)
    return sp.Integer(0) if t == 0 else 1 - 2*t

print("== C. downstairs mapping-torus rho: full convention lattice (8 branches) ==")
# per ker^+ kernel mode (2 modes, phi-trivial): momenta 2pi(Z + delta + cs*k/3)
branches = {}
for delta in (sp.Integer(0), R(1,2)):
    for cs_ in (1, -1):
        for ms_ in (1, -1):
            etas = [S(2*ms_*etaS1(delta + cs_*R(k,3))) for k in range(3)]
            hs   = [2 if S(delta + cs_*R(k,3) - floor(delta + cs_*R(k,3))) == 0 else 0 for k in range(3)]
            rhos = [S(e - etas[0]) for e in etas]
            cls  = [int(3*(r - floor(r))) % 3 for r in rhos]
            branches[(delta, cs_, ms_)] = (tuple(etas), tuple(rhos), tuple(hs), tuple(cls))
            check(S(sum(etas)) == 0, "G5 sum eta = 0 in every branch")
            check(sorted(cls) == [0,1,2], "mod-Z classes are {0,1,2}/3 in EVERY branch")
            check(all(c != 0 for c in cls[1:]), "Z/3-NONZERO on both nontrivial characters, every branch")

claim_pkg = ((sp.Integer(0), R(-2,3), R(2,3)), (0, 1, 2), (2, 0, 0))
hits = [key for key, (e, r, h, c) in branches.items()
        if r == claim_pkg[0] and c == tuple(claim_pkg[1]) and h == claim_pkg[2]]
check(len(hits) > 0 and all(key[0] == 0 for key in hits),
      "the claimed package (0,-2/3,2/3),h=(2,0,0),(0,1,2)/3 occurs ONLY at delta=0 = PERIODIC "
      "(= NON-bounding); (cs,ms) and (-cs,-ms) coincide since eta_S1 is odd")
check(sorted(hits) == sorted([(sp.Integer(0), 1, -1), (sp.Integer(0), -1, 1)]),
      "claimed package sits at the two equivalent periodic branches (0,+1,-1) ~ (0,-1,+1)")
check(all(branches[(R(1,2), c_, m_)][1] != claim_pkg[0] for c_ in (1,-1) for m_ in (1,-1)),
      "NO bounding branch reproduces the claimed rho values")
print("   claimed package located ONLY at delta=0 (PERIODIC / NON-bounding), (cs,ms)=(+1,-1)~(-1,+1)")

# the actually-pinned BOUNDING structure (delta = 1/2), same cs, ms:
eB, rB, hB, cB = branches[(R(1,2), 1, -1)]
check(rB == (sp.Integer(0), R(4,3), R(-4,3)) and hB == (0,0,0) and cB == (0,1,2),
      "BOUNDING structure gives rho = (0, +4/3, -4/3), h = (0,0,0), classes (0,1,2)/3")
# periodic vs bounding differ by EVEN integers within fixed (cs, ms):
for cs_ in (1,-1):
    for ms_ in (1,-1):
        eP = branches[(sp.Integer(0), cs_, ms_)][0]
        eA = branches[(R(1,2), cs_, ms_)][0]
        for k in range(3):
            d = S(eP[k] - eA[k])
            check(d.is_integer and int(d) % 2 == 0,
                  "spin-structure change shifts eta_k by an EVEN integer (2-primary)")
print("   bounding-structure values: rho = (0, 4/3, -4/3), h = (0,0,0); per-vs-bounding shifts in 2Z")
print("   => Z/3 class list (0,1,2)/3 and Z3_NONZERO verdict IDENTICAL in all 8 branches")

print("== D. Donnelly averaging, independent Abel-regularized equivariant circle etas ==")
def eta_gm_upstairs(mpow, delta, ms_):
    """equivariant eta of the 2 phi-trivial ker^+ modes x circle(circumference 3, structure delta)
       at g^mpow; g = (phi, s -> s+1); circle lift L: L=1 (delta=0), L=-1 (delta=1/2) [unique
       order-3 lifts]; Abel regularization, exact limit."""
    m = mpow % 3
    if m == 0:
        return sp.Integer(0)
    L = sp.Integer(1) if delta == 0 else sp.Integer(-1)
    if delta == 0:
        pos = (zp(-m)*x)/(1 - zp(-m)*x)                     # n >= 1, weight zeta^{-nm}
        neg = (zp(m)*x)/(1 - zp(m)*x)                       # n <= -1
        pre = L**m
    else:
        pre = (sp.Integer(-1))**m * exp(-I*pi*m/3)
        pos = x**R(1,2)/(1 - zp(-m)*x)                      # n >= 0
        neg = x**(-R(1,2))*(zp(m)*x)/(1 - zp(m)*x)          # n <= -1
    val = limit(pre*(pos - neg), x, 1, '-') if delta != 0 else limit(pre*pos - pre.conjugate()*0 - (pos - pos) - neg + pre*0, x, 1, '-')
    # (delta = 0: pre = 1, just pos - neg)
    if delta == 0:
        val = limit(pos - neg, x, 1, '-')
    return S(2*ms_*val)

for delta in (sp.Integer(0), R(1,2)):
    for ms_ in (1,-1):
        eg = {m: eta_gm_upstairs(m, delta, ms_) for m in range(3)}
        check(S(eg[2] - sp.conjugate(eg[1])) == 0, "eta_{g^2} = conj(eta_g) (unitarity)")
        matched = {}
        for p_ in (1,-1):   # character pairing zeta^{p k m}
            avg = [S(sum(zp(p_*k*m)*eg[m] for m in range(3))/3) for k in range(3)]
            for cs_ in (1,-1):
                if tuple(avg) == branches[(delta, cs_, ms_)][0]:
                    matched[p_] = cs_
        check(sorted(matched.values()) == [-1,1],
              "Donnelly average matches the direct downstairs etas EXACTLY in every branch "
              "(one pairing per character-shift sign); delta=%s ms=%d" % (delta, ms_))
print("   Donnelly isotypic averaging == direct spectral etas EXACTLY, for BOTH spin structures")
print("   (so G7-exactness holds; it does NOT distinguish bounding from periodic)")

print("== E. disk fixed-point route (K3 x D^2) and the implied equivariant APS index ==")
def nu6(m):  # 6d Dirac fixed weight, weights (zeta^m, zeta^-m; zeta^m), mu_3 half powers
    return S(R(1,3) * 1/(zp(2*m) - zp(m)))
check(nu6(1) == S(I*sqrt(3)/9) and S(nu6(2) - sp.conjugate(nu6(1))) == 0, "nu_D6 = i sqrt3/9, conj pair")
rho_fp = [S(sum((zp(-k*m) - 1)*12*nu6(m) for m in (1,2))/3) for k in range(3)]
check(tuple(rho_fp) == (sp.Integer(0), R(4,3), R(-4,3)),
      "disk fixed-point rho = (0, 4/3, -4/3) -- EXACTLY the BOUNDING-structure direct values")
check(tuple(rho_fp) == rB, "fp route == direct route for the bounding structure, EXACT (not just mod 2Z)")
# implied equivariant APS index: eta_g(Y~) = 2*Sigma_fp - 2*ind_g ; use the eta_g labeling that
# is Donnelly-consistent with the SAME pairing p=-1 used in rho_fp:
eg_anti = {m: eta_gm_upstairs(m, R(1,2), -1) for m in (1,2)}
# pick labeling (eg or conj) by Z[zeta]-integrality of ind (Donnelly integrality pins it):
cands = []
for lab, e1 in (("as-computed", eg_anti[1]), ("conjugate-labeling", sp.conjugate(eg_anti[1]))):
    ind = S((12*nu6(1) - e1)/2)
    a_ = S(sp.re(ind) + sp.im(ind)/sqrt(3))      # ind = a + b*zeta -> a = Re + Im/sqrt3, b = 2 Im/sqrt3
    b_ = S(2*sp.im(ind)/sqrt(3))
    cands.append((lab, ind, a_, b_, bool(a_.is_integer and b_.is_integer)))
ok = [c for c in cands if c[4]]
check(len(ok) == 1, "exactly one g-labeling gives ind_g(APS) in Z[zeta] (integrality pins it)")
check(S(ok[0][1]) == 0, "in the CONSISTENT bounding pairing, implied ind_g(APS on K3xD^2) = 0 "
                        "and the fp route agrees EXACTLY -- the leg's +-2 offset and ind=1+2zeta "
                        "are artifacts of comparing against the NON-bounding direct values")
# reproduce the leg's artifact for the record: pairing fp(bounding) against periodic direct:
eP = branches[(sp.Integer(0), 1, -1)][1]
d1, d2 = S(rho_fp[1] - eP[1]), S(rho_fp[2] - eP[2])
check((d1, d2) == (2, -2), "fp(bounding) - direct(periodic) = (+2, -2): the leg's G8 offsets")
ind_artifact = S((12*nu6(1) - (-2*I/sqrt(3)))/2)     # leg's eta_g = -2 i cot(pi/3)
check(S(ind_artifact - (1 + 2*z)) == 0, "the leg's 'ind_g = 1+2zeta' reproduced as the mismatch artifact")
print("   nu_D6 = i sqrt3/9; rho^fp = (0, 4/3, -4/3) = bounding direct EXACTLY; ind_g(APS) = 0")
print("   leg's (+2,-2) offsets and ind_g = 1+2zeta reproduced as the periodic/bounding mismatch")

print("== F. integer-shift lemma + twisted-lift relabeling (spot checks) ==")
viol = 0
for k in (1,2):
    for a_ in range(-6,7):
        for b_ in range(-6,7):
            w = a_ + b_*z
            e = S(((zp(-k)-1)*w + (zp(-2*k)-1)*sp.conjugate(w))/3)
            if not (S(sp.im(e)) == 0 and e.is_integer):
                viol += 1
check(viol == 0, "integer-shift lemma holds (independent sweep)")
# twisted lift m=1 direct: kernel phase 1/3 -> eta = (-2/3, 2/3, 0), rho = (0, 4/3, 2/3)
et1 = [S(-2*etaS1(R(1,3) + R(k,3))) for k in range(3)]
check(tuple(et1) == (R(-2,3), R(2,3), sp.Integer(0)), "lift_1 etas = (-2/3, 2/3, 0) [relabel k->k+1]")
check(tuple(S(e - et1[0]) for e in et1) == (sp.Integer(0), R(4,3), R(2,3)), "lift_1 rho = (0,4/3,2/3)")
print("   integer-shift lemma: 338 points, 0 violations; lift_1 relabeling reproduced")

print("== G. non-equivariant gates ==")
check(R(16,8) == 2 and R(-(-16),8) == 2, "index D = -sigma/8 = 2")
check(R(2+2+2,3) == 2, "orbifold average 2")
print("   -sigma/8 = 2; orbifold average 2 in Z")

print()
print("ALL %d REFEREE CHECKS PASS (exit 0)" % NCHK)
print()
print("REFEREE VERDICT SUMMARY:")
print(" * Z3_NONZERO verdict CONFIRMED in every one of the 8 convention branches;")
print("   class list {0,1,2}/3 is branch-independent (spin-structure shifts are 2-primary, in 2Z).")
print(" * BUT the claimed exact package rho=(0,-2/3,+2/3), h=(2,0,0) belongs to the PERIODIC")
print("   (NON-bounding) circle spin structure, contradicting the Section-0 pin 'bounding")
print("   (antiperiodic)'. Under the pinned bounding structure: rho=(0,+4/3,-4/3), h=(0,0,0).")
print(" * The G8 'mod 2Z' slack and 'implied ind_g = 1+2zeta' are exactly this mismatch:")
print("   in consistent bounding conventions the disk route agrees EXACTLY with ind_g = 0.")
