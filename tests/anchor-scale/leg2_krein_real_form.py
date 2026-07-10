# LEG-2 (anchor swing): the REAL / KREIN form of the scalar-spinor odd
# channel on the honest anchor fiber -- Cl(9,5) = M(64,H), Krein metric
# beta_S, u_beta = u(64,64)-type gauge algebra.
#
# QUESTION (corners campaign, named gap 2): the toy (leg B1) was COMPLEX.
# At anchor scale the Krein structure selects real forms. Does the
# scalar-spinor closure survive the honest real/Krein form
# (beta_S-compatible brackets; the quaternionic structure of M(64,H)),
# or does it REQUIRE complexification (which would grade the toy result
# complex-only)?
#
# METHOD (exact, no floats in any assert path):
#   * PORTED VERBATIM from LEG-1 (so the two legs compose): the exact
#     Gaussian-rational arithmetic (GC), the sparse 128x128 matrices, the
#     Cl(9,5) Jordan-Wigner gammas GAM, and the Krein metric BETA.
#   * beta_S-compatibility DERIVED exactly two ways:
#       (1) a *-word-algebra certificate valid for ALL spinors Q,P from the
#           single premise beta^dag = beta (Krein reality) -- no Clifford
#           identity, no complexification;
#       (2) exact 128-dim witness instantiation on the honest fiber.
#   * the quaternionic structure J of M(64,H) CONSTRUCTED exactly (the
#     charge-conjugation C = product of the gammas whose complex conjugate
#     flips sign), J(v) = C conj(v); J^2 = -I certified exactly (the
#     M(64,H) invariant), J commutes with the Clifford algebra, J
#     ANTI-commutes with the central charge i*Id.
#   * the real-form verdict decided by exact witnesses: S is a COMPLEX-type
#     module over the full u(64,64) (no antilinear commutant), so its only
#     u_beta-compatible real form is the underlying-real S_R (dim_R 256) --
#     the closure is a REAL super-algebra with NO complexification; the
#     quaternionic J is a symmetry only of the H-respecting subalgebra
#     g_H = u_beta cap gl(64,H) (which contains spin(9,5) but NOT the u(1)
#     center). The u(1) center KILLS the complex-bilinear channel, SELECTING
#     the sesquilinear Krein bracket -> reality is forced, not imposed.
#   * Q3: derivative-level odd tau_plus -- exact requirement stated; the
#     finite (frozen, flat, beta-compatible) shadow executed exactly; the
#     genuine derivative-level homomorphism BLOCKED on curvature (d_A^2),
#     with the exact missing structure named.
#
# FIREWALL (absorbed/gu-source-action/DEAD-ENDS.md): no chi(K3)=24, no /8
# manufacture, no A-hat=3, no topology imports at all; the bare 58.72
# commutator is never touched (this leg computes Krein/real-form structure
# and super-Jacobi shadows only).

import sys, time, random
from fractions import Fraction

T0 = time.time()
NCHECK = [0]
def check(cond, msg):
    NCHECK[0] += 1
    if not cond:
        print("FAIL [%d]: %s" % (NCHECK[0], msg))
        sys.exit(1)
    print("  ok [%3d] %s  [t=%.0fs]" % (NCHECK[0], msg, time.time() - T0))

def note(msg):
    print("       " + msg)

print("=" * 78)
print("LEG-2: real/Krein form of the scalar-spinor odd channel on the")
print("       Cl(9,5) = M(64,H) anchor fiber")
print("=" * 78)

# ======================================================================
# PART 1: exact arithmetic infrastructure  (PORTED VERBATIM from LEG-1)
# ======================================================================
print("\n--- PART 1: exact arithmetic (ported from LEG-1) ---")

class GC(object):
    """Gaussian rational a + b i, exact."""
    __slots__ = ("re", "im")
    def __init__(self, re=0, im=0):
        self.re = re if type(re) is Fraction else Fraction(re)
        self.im = im if type(im) is Fraction else Fraction(im)
    def __add__(self, o):  return GC(self.re + o.re, self.im + o.im)
    def __sub__(self, o):  return GC(self.re - o.re, self.im - o.im)
    def __neg__(self):     return GC(-self.re, -self.im)
    def __mul__(self, o):
        return GC(self.re * o.re - self.im * o.im,
                  self.re * o.im + self.im * o.re)
    def __truediv__(self, o):
        n = o.re * o.re + o.im * o.im
        return GC((self.re * o.re + self.im * o.im) / n,
                  (self.im * o.re - self.re * o.im) / n)
    def conj(self):        return GC(self.re, -self.im)
    def is_zero(self):     return self.re == 0 and self.im == 0
    def __eq__(self, o):   return self.re == o.re and self.im == o.im
    def __hash__(self):    return hash((self.re, self.im))
    def __repr__(self):
        return "GC(%s,%s)" % (self.re, self.im)

ZERO, ONE, GI = GC(0), GC(1), GC(0, 1)
N = 128

# ---- sparse matrices: dict row -> dict col -> GC (no explicit zeros) ----
def mset(M, i, j, v):
    if v.is_zero():
        return
    r = M.get(i)
    if r is None:
        r = {}; M[i] = r
    w = r.get(j)
    v = v if w is None else w + v
    if v.is_zero():
        if w is not None:
            del r[j]
            if not r:
                del M[i]
    else:
        r[j] = v

def meye(c=ONE):
    return {i: {i: c} for i in range(N)} if not c.is_zero() else {}

def madd(A, B):
    C = {i: dict(r) for i, r in A.items()}
    for i, r in B.items():
        for j, v in r.items():
            mset(C, i, j, v)
    return C

def mscal(c, A):
    if c.is_zero():
        return {}
    return {i: {j: c * v for j, v in r.items()} for i, r in A.items()}

def msub(A, B):
    return madd(A, mscal(GC(-1), B))

def mmul(A, B):
    C = {}
    for i, rA in A.items():
        acc = {}
        for k, a in rA.items():
            rB = B.get(k)
            if rB is None:
                continue
            for j, b in rB.items():
                w = acc.get(j)
                v = a * b
                acc[j] = v if w is None else w + v
        acc = {j: v for j, v in acc.items() if not v.is_zero()}
        if acc:
            C[i] = acc
    return C

def mdag(A):
    C = {}
    for i, r in A.items():
        for j, v in r.items():
            mset(C, j, i, v.conj())
    return C

def mtransp(A):
    C = {}
    for i, r in A.items():
        for j, v in r.items():
            mset(C, j, i, v)
    return C

def mconj(A):
    return {i: {j: v.conj() for j, v in r.items()} for i, r in A.items()}

def mtr(A):
    s = ZERO
    for i, r in A.items():
        v = r.get(i)
        if v is not None:
            s = s + v
    return s

def miszero(A):
    for r in A.values():
        for v in r.values():
            if not v.is_zero():
                return False
    return True

def meq(A, B):
    return miszero(msub(A, B))

def mcomm(A, B):
    return msub(mmul(A, B), mmul(B, A))

def manti(A, B):
    return madd(mmul(A, B), mmul(B, A))

# ---- dense exact spinors (tuples of 128 GC) ----
def vzero():
    return tuple(ZERO for _ in range(N))

def vadd(u, v):
    return tuple(u[k] + v[k] for k in range(N))

def vsub(u, v):
    return tuple(u[k] - v[k] for k in range(N))

def vscal(c, u):
    return tuple(c * u[k] for k in range(N))

def vconj(u):
    return tuple(x.conj() for x in u)

def viszero(u):
    return all(x.is_zero() for x in u)

def mat_vec(M, v):
    out = [ZERO] * N
    for i, r in M.items():
        s = ZERO
        for j, a in r.items():
            x = v[j]
            if not x.is_zero():
                s = s + a * x
        out[i] = s
    return tuple(out)

def vecdag_mat(v, M):
    """row vector v^dag M (tuple)."""
    out = [ZERO] * N
    for i, r in M.items():
        c = v[i].conj()
        if c.is_zero():
            continue
        for j, a in r.items():
            out[j] = out[j] + c * a
    return tuple(out)

def vecT_mat(v, M):
    """row vector v^T M (transpose, NO conjugation)."""
    out = [ZERO] * N
    for i, r in M.items():
        c = v[i]
        if c.is_zero():
            continue
        for j, a in r.items():
            out[j] = out[j] + c * a
    return tuple(out)

def rowdot(r, v):
    s = ZERO
    for k in range(N):
        if not r[k].is_zero() and not v[k].is_zero():
            s = s + r[k] * v[k]
    return s

def outer(u, r):
    """column u times row r."""
    C = {}
    for i in range(N):
        a = u[i]
        if a.is_zero():
            continue
        row = {}
        for j in range(N):
            b = r[j]
            if not b.is_zero():
                row[j] = a * b
        if row:
            C[i] = row
    return C

def sesq(u, v):
    """u^dag beta v  -- filled after BETA is built (Krein inner product)."""
    return rowdot(vecdag_mat(u, BETA), v)

# self-tests
A = {0: {1: GC(2)}, 1: {0: GC(0, 1)}}
B = {0: {0: GC(1, 1)}, 1: {1: GC(3)}}
check(meq(mmul(A, B), {0: {1: GC(6)}, 1: {0: GC(-1, 1)}}),
      "sparse matmul self-test (ported engine)")
check(meq(mdag(A), {1: {0: GC(2)}, 0: {1: GC(0, -1)}}),
      "dagger self-test")

# ======================================================================
# PART 2: Cl(9,5) gammas + Krein metric BETA  (PORTED VERBATIM from LEG-1)
# ======================================================================
print("\n--- PART 2: Cl(9,5) infrastructure + Krein metric (ported) ---")

def kron(A, B, nB):
    C = {}
    for iA, rA in A.items():
        for jA, a in rA.items():
            for iB, rB in B.items():
                for jB, b in rB.items():
                    mset(C, iA * nB + iB, jA * nB + jB, a * b)
    return C

S1 = {0: {1: ONE}, 1: {0: ONE}}
S2 = {0: {1: GC(0, -1)}, 1: {0: GC(0, 1)}}
S3 = {0: {0: ONE}, 1: {1: GC(-1)}}
I2 = {0: {0: ONE}, 1: {1: ONE}}

def jw_exact(n):
    G = []
    mids = []            # record which mid factor (S1 or S2) built each gamma
    for k in range(n):
        for mid in (S1, S2):
            o = {0: {0: ONE}}
            dim = 1
            for m in ([S3] * k + [mid] + [I2] * (n - 1 - k)):
                o = kron(o, m, 2)
                dim *= 2
            G.append(o)
            mids.append("S1" if mid is S1 else "S2")
    return G, mids

BASE, MIDS = jw_exact(7)     # 14 Hermitian gammas of Cl(14,0), 128x128 exact
TIMELIKE = {4, 5, 6, 7, 8}
SPACELIKE = [a for a in range(14) if a not in TIMELIKE]
ETA = [(-1 if a in TIMELIKE else 1) for a in range(14)]
GAM = [(mscal(GI, BASE[a]) if a in TIMELIKE else BASE[a]) for a in range(14)]

ID = meye()
ok = True
for a in range(14):
    for b in range(14):
        tgt = mscal(GC(2 * ETA[a]) if a == b else ZERO, ID)
        if not meq(manti(GAM[a], GAM[b]), tgt):
            ok = False
check(ok, "Clifford relations {g_a,g_b} = 2 eta_ab, signature (9,5) EXACT")
ok = all(meq(mdag(GAM[a]), GAM[a]) for a in SPACELIKE) and \
     all(meq(mdag(GAM[a]), mscal(GC(-1), GAM[a])) for a in TIMELIKE)
check(ok, "spacelike gammas Hermitian, timelike anti-Hermitian (exact)")

# Krein metric beta_S = product of the 9 spacelike gammas
BETA = ID
for a in SPACELIKE:
    BETA = mmul(BETA, GAM[a])
check(meq(mdag(BETA), BETA), "beta_S Hermitian (exact)")
check(meq(mmul(BETA, BETA), ID), "beta_S^2 = I (exact)")
check(mtr(BETA).is_zero(), "tr beta_S = 0 => Krein signature (64,64) "
      "(u_beta iso u(64,64))")

# so(9,5) spin generators sigma_ab = (1/4)[g_a,g_b], pseudo-anti-Hermitian
SIG = {}
ok = True
for a in range(14):
    for b in range(a + 1, 14):
        s = mscal(GC(Fraction(1, 4)), mcomm(GAM[a], GAM[b]))
        SIG[(a, b)] = s
        if not miszero(madd(mmul(BETA, s), mmul(mdag(s), BETA))):
            ok = False
check(ok, "all 91 so(9,5) generators in u_beta: beta sigma + sigma^dag "
          "beta = 0 (exact; Krein fact re-derived, ports LEG-1)")

# u_beta sampler (ported): X = beta * A, A anti-Hermitian => X in u_beta
rnd = random.Random(20260710)

def rand_gc(lo=-3, hi=3):
    return GC(rnd.randint(lo, hi), rnd.randint(lo, hi))

def rand_antiherm(nnz=6):
    A = {}
    for _ in range(nnz):
        i = rnd.randrange(N); j = rnd.randrange(N)
        if i == j:
            mset(A, i, i, GC(0, rnd.randint(-3, 3)))
        else:
            c = rand_gc()
            mset(A, i, j, c)
            mset(A, j, i, -c.conj())
    return A

def in_ubeta(X):
    return miszero(madd(mmul(BETA, X), mmul(mdag(X), BETA)))

def rand_ubeta(nnz=6):
    X = mmul(BETA, rand_antiherm(nnz))
    return X

def rand_spinor(lo=-2, hi=2):
    return tuple(GC(rnd.randint(lo, hi), rnd.randint(lo, hi))
                 for _ in range(N))

check(all(in_ubeta(rand_ubeta()) for _ in range(4)),
      "u_beta sampler lands in u_beta (exact witnesses)")

# ======================================================================
# PART 3: beta_S-COMPATIBILITY of the odd bracket, derived EXACTLY
# ======================================================================
print("\n--- PART 3: beta_S-compatibility of the scalar-spinor bracket ---")
note("The odd bracket (ported from LEG-1's anchor pairing):")
note("  M(Q,P)   = i (Q P^dag beta + P Q^dag beta)  in u_beta (traceful),")
note("  M_sl     = M - (tr M / 128) I,  M_0 = i s(Q,P) I  (s = Q^dag b P +")
note("  P^dag b Q, REAL). COMPATIBILITY = the bracket's image is pseudo-")
note("  anti-Hermitian w.r.t. beta (lands in the real form u(64,64)).")

def pair_M(Q, P):
    rP = vecdag_mat(P, BETA)
    rQ = vecdag_mat(Q, BETA)
    return mscal(GI, madd(outer(Q, rP), outer(P, rQ)))

def pair_s(Q, P):
    return rowdot(vecdag_mat(Q, BETA), P) + rowdot(vecdag_mat(P, BETA), Q)

def pair_M0(Q, P):
    return mscal(GI * pair_s(Q, P), ID)

def pair_Msl(Q, P):
    M = pair_M(Q, P)
    return msub(M, mscal(mtr(M) / GC(N), ID))

# ---- (3a) SYMBOLIC *-word certificate: valid for ALL Q,P, from beta^dag=beta
# minimal free *-algebra: words over {b (=beta), Q,Qd, P,Pd}; dagger reverses
# and swaps Q<->Qd, P<->Pd, b<->b (beta Hermitian is the ONLY premise).
DAG = {"b": "b", "Q": "Qd", "Qd": "Q", "P": "Pd", "Pd": "P"}

def wexpr(*syms):
    return {tuple(syms): ONE}

def wadd(*es):
    out = {}
    for e in es:
        for w, c in e.items():
            v = out.get(w)
            v = c if v is None else v + c
            if v.is_zero():
                out.pop(w, None)
            else:
                out[w] = v
    return out

def wscal(c, e):
    if c.is_zero():
        return {}
    return {w: c * v for w, v in e.items()}

def wmul(e1, e2):
    out = {}
    for w1, c1 in e1.items():
        for w2, c2 in e2.items():
            w = w1 + w2
            c = c1 * c2
            v = out.get(w)
            v = c if v is None else v + c
            if v.is_zero():
                out.pop(w, None)
            else:
                out[w] = v
    return out

def wdag(e):
    out = {}
    for w, c in e.items():
        nw = tuple(DAG[s] for s in reversed(w))
        cc = c.conj()
        v = out.get(nw)
        v = cc if v is None else v + cc
        if v.is_zero():
            out.pop(nw, None)
        else:
            out[nw] = v
    return out

def wiszero(e):
    return all(c.is_zero() for c in e.values())

eb = wexpr("b")
eQ, eQd = wexpr("Q"), wexpr("Qd")
eP, ePd = wexpr("P"), wexpr("Pd")

# engine self-tests
check(wdag(wdag(wmul(eQ, ePd))) == wmul(eQ, ePd), "word engine: dag involutive")
check(wdag(eb) == eb, "word engine: beta^dag = beta encoded (Krein reality)")

# M = i(Q P^dag b + P Q^dag b) as a word expression
wM = wscal(GI, wadd(wmul(eQ, wmul(ePd, eb)), wmul(eP, wmul(eQd, eb))))
# pseudo-anti-Hermiticity residual:  beta M + M^dag beta
resid = wadd(wmul(eb, wM), wmul(wdag(wM), eb))
check(wiszero(resid),
      "CERT K1: beta M + M^dag beta = 0 for ALL Q,P from beta^dag = beta "
      "ALONE (symbolic; no Clifford identity, no complexification) => "
      "M(Q,P) in u(64,64) for every pair")
# the central pairing: s = Q^dag b P + P^dag b Q, and s^dag = s (REAL)
ws = wadd(wmul(eQd, wmul(eb, eP)), wmul(ePd, wmul(eb, eQ)))
check(wiszero(wadd(ws, wscal(GC(-1), wdag(ws)))),
      "CERT K2: s(Q,P)^dag = s(Q,P) (symbolic) => s REAL => M_0 = i s Id "
      "in u_beta (i Id is central; anti-Herm x real)")
# symmetry Q<->P of M (needed: {odd,odd} symmetric bracket)
def wswap(e):
    sw = {"Q": "P", "Qd": "Pd", "P": "Q", "Pd": "Qd", "b": "b"}
    out = {}
    for w, c in e.items():
        nw = tuple(sw[s] for s in w)
        out[nw] = out.get(nw, ZERO) + c
    return {w: c for w, c in out.items() if not c.is_zero()}
check(wiszero(wadd(wM, wscal(GC(-1), wswap(wM)))),
      "CERT K3: M(Q,P) = M(P,Q) symbolically (symmetric odd bracket)")

# ---- (3b) EXACT 128-dim witnesses (the code's beta/pairings satisfy K1-K3)
ok = True
for _ in range(6):
    Q, P = rand_spinor(), rand_spinor()
    if not (in_ubeta(pair_M(Q, P)) and in_ubeta(pair_Msl(Q, P))
            and in_ubeta(pair_M0(Q, P))):
        ok = False
    if not meq(pair_M(Q, P), pair_M(P, Q)):
        ok = False
    if pair_s(Q, P).im != 0:
        ok = False
check(ok, "K1-K3 instantiated EXACTLY on the honest 128-dim fiber "
      "(6 random spinor pairs: M,M_sl,M_0 in u_beta; symmetric; s real)")
note("=> the Krein/beta-reality of the odd bracket is EXACT and AUTOMATIC:")
note("   it needs ONLY beta Hermitian, holds for every pair of odd elements,")
note("   and requires NO complexification. The odd-odd bracket lands in the")
note("   REAL form u(64,64), not merely in its complexification gl(128,C).")

# ======================================================================
# PART 4: the quaternionic structure J of M(64,H), CONSTRUCTED EXACTLY
# ======================================================================
print("\n--- PART 4: the quaternionic structure J of Cl(9,5) = M(64,H) ---")
note("J(v) = C conj(v), antilinear. J commutes with the real Clifford algebra")
note("iff  GAM_a C = C GAM_a^*  for all a. Since GAM_a^* = eps_a GAM_a in the")
note("JW basis, C = product of the gammas with eps_a = -1 (the standard")
note("charge conjugation). J^2 = C C^* is the +/-1 invariant: -1 <=> M(_,H).")

# eps_a: GAM_a^* = eps_a GAM_a  (computed exactly, not assumed)
def mat_eq_scaled(A, s, B):
    return meq(A, mscal(GC(s), B))
EPS = []
for a in range(14):
    Gs = mconj(GAM[a])
    if meq(Gs, GAM[a]):
        EPS.append(1)
    elif meq(Gs, mscal(GC(-1), GAM[a])):
        EPS.append(-1)
    else:
        EPS.append(0)
check(all(e in (1, -1) for e in EPS),
      "each GAM_a^* = eps_a GAM_a with eps_a in {+1,-1} (exact; conj is "
      "diagonal in the JW basis): eps = %s" % EPS)
Aminus = [a for a in range(14) if EPS[a] == -1]
check(len(Aminus) % 2 == 0,
      "|{a: eps_a = -1}| = %d is EVEN => C = prod_{a in A-} GAM_a intertwines "
      "(commutes/anticommutes correctly with every GAM_a)" % len(Aminus))

# build C = product over A- (in increasing index order)
C = ID
for a in Aminus:
    C = mmul(C, GAM[a])

# verify the intertwining GAM_a C = C GAM_a^* for all a (=> J commutes w/ Cl)
ok = all(meq(mmul(GAM[a], C), mmul(C, mconj(GAM[a]))) for a in range(14))
check(ok, "GAM_a C = C GAM_a^* for all 14 a (exact) => J antilinearly "
      "commutes with every gamma (J is a Cl(9,5)-module map)")

def Jop(v):
    """quaternionic structure J(v) = C conj(v)."""
    return mat_vec(C, vconj(v))

# J^2 = C C^*  -- the reality invariant
CC = mmul(C, mconj(C))
check(meq(CC, mscal(GC(-1), ID)),
      "J^2 = C C^* = -I EXACTLY => S is QUATERNIONIC (matches Cl(9,5) = "
      "M(64,H); classification q-p = -4 = 4 mod 8). NOT real type (+I).")
# witness J^2 = -1 on spinors + antilinearity
ok = True
for _ in range(4):
    v = rand_spinor()
    if not viszero(vadd(Jop(Jop(v)), v)):
        ok = False
    c = GC(2, 3)
    if not viszero(vsub(Jop(vscal(c, v)), vscal(c.conj(), Jop(v)))):
        ok = False
check(ok, "J^2 = -Id and J antilinear (J(c v) = conj(c) J(v)) -- exact "
      "spinor witnesses")
# J commutes with the Clifford action, hence with BETA and every sigma_ab
ok = True
for a in range(14):
    v = rand_spinor()
    if not viszero(vsub(Jop(mat_vec(GAM[a], v)), mat_vec(GAM[a], Jop(v)))):
        ok = False
for (a, b) in ((0, 1), (4, 5), (3, 9), (7, 13)):
    v = rand_spinor()
    if not viszero(vsub(Jop(mat_vec(SIG[(a, b)], v)),
                        mat_vec(SIG[(a, b)], Jop(v)))):
        ok = False
vv = rand_spinor()
check(ok and viszero(vsub(Jop(mat_vec(BETA, vv)), mat_vec(BETA, Jop(vv)))),
      "J commutes with GAM_a, sigma_ab, and beta (exact witnesses) => J is a "
      "symmetry of the spin(9,5) sub-algebra and preserves the Krein form")

# J ANTI-commutes with the central charge i Id (antilinearity):
ZC = mscal(GI, ID)
v = rand_spinor()
check(viszero(vadd(Jop(mat_vec(ZC, v)), mat_vec(ZC, Jop(v)))),
      "J(i v) = -i J(v): J ANTI-commutes with the u(1) center i*Id "
      "(so the central charge is NOT quaternionic-linear) -- exact witness")

# ======================================================================
# PART 5: the REAL-FORM verdict -- real vs quaternionic vs underlying-real
# ======================================================================
print("\n--- PART 5: which real form does the odd module carry? ---")

# (5a) S is COMPLEX-type over the FULL u_beta: J (the only Clifford-commuting
# antilinear structure) does NOT commute with generic X in u_beta.
found = None
for _ in range(12):
    X = rand_ubeta()
    v = rand_spinor()
    lhs = Jop(mat_vec(X, v))            # J(Xv)
    rhs = mat_vec(X, Jop(v))            # X(Jv)
    if not viszero(vsub(lhs, rhs)):
        found = True
        break
check(found is True,
      "generic X in u_beta does NOT commute with J (exact witness: "
      "J(Xv) != X(Jv)) => S is NOT a quaternionic module over the full "
      "u(64,64); no antilinear commutant => S is COMPLEX-type")
note("Rep-theory reason (structural): the fundamental rep C^128 of u(64,64)")
note("is irreducible of COMPLEX type (conjugate rep S-bar not isomorphic to")
note("S), so End_{u_beta}(S) = C.Id has NO antilinear element. Hence the ONLY")
note("u_beta-compatible real structure on the odd space is the underlying")
note("real S_R (restriction of scalars, dim_R 256) -- exactly LEG-1's odd")
note("module. No real (tau^2=+1) or quaternionic (tau^2=-1) HALF-size module")
note("is u(64,64)-compatible; the closure is a REAL super-algebra WITHOUT")
note("complexification, on S_R.")

# (5b) the H-respecting subalgebra g_H = u_beta cap {commute with J}:
# contains spin(9,5), EXCLUDES the u(1) center, and is bracket-closed.
def commutes_with_J(X):
    # J X = X J  as antilinear operators <=>  C X^* = X C  <=>  C conj(X) = X C
    return meq(mmul(C, mconj(X)), mmul(X, C))
# sigma_ab in g_H:
ok = all(in_ubeta(SIG[p]) and commutes_with_J(SIG[p])
         for p in ((0, 1), (4, 5), (3, 9), (7, 13), (0, 9)))
check(ok, "spin(9,5) generators sigma_ab lie in g_H = u_beta cap gl(64,H) "
      "(in u_beta AND commute with J) -- exact")
check(in_ubeta(ZC) and not commutes_with_J(ZC),
      "the u(1) center i*Id is in u_beta but NOT in g_H (anti-commutes with "
      "J) => the quaternionic gauge algebra g_H = sp(p,q)-type is CENTERLESS")
# bracket closure of g_H (witness): [sigma,sigma'] stays in g_H
P1, P2 = SIG[(0, 1)], SIG[(2, 3)]
Br = mcomm(P1, P2)
check(in_ubeta(Br) and commutes_with_J(Br),
      "[g_H, g_H] <= g_H (exact witness [sigma_01, sigma_23]) -- g_H is a "
      "genuine subalgebra (the quaternionic/H real form's gauge algebra)")

# (5c) the spin(9,5)-invariant BILINEAR form (the toy-style channel): it
# EXISTS over g_H (charge conjugation C_bilin), and it is KILLED by the u(1)
# center -- so it survives only in the quaternionic reading, not over u(64,64).
# C_bilin = prod of gammas with delta_a = eta_a eps_a = -1, giving
# C_bilin GAM_a C_bilin^{-1} = GAM_a^T (spin-invariant bilinear form).
DELTA = [ETA[a] * EPS[a] for a in range(14)]
# GAM_a^T = delta_a GAM_a (delta = eta*eps). C_bil = product over the set B
# with C_bil GAM_a C_bil^{-1} = GAM_a^T; the correct B is whichever of
# {delta=-1} / {delta=+1} has the parity that intertwines (self-selected).
def build_Cbil(setB):
    M = ID
    for a in setB:
        M = mmul(M, GAM[a])
    return M
def intertwines_T(M):
    return all(meq(mmul(M, GAM[a]), mmul(mtransp(GAM[a]), M))
               for a in range(14))
setM = [a for a in range(14) if DELTA[a] == -1]
setP = [a for a in range(14) if DELTA[a] == 1]
Cbil, usedB = None, None
for cand in (setM, setP):
    Mc = build_Cbil(cand)
    if intertwines_T(Mc):
        Cbil, usedB = Mc, cand
        break
check(Cbil is not None,
      "C_bilin = prod over B (|B|=%s) intertwines GAM_a with GAM_a^T (exact, "
      "self-selected parity) => v^T C_bilin w is a spin(9,5)-invariant "
      "BILINEAR form on S" % (len(usedB) if usedB else "-"))
def bilinform(u, v):
    return rowdot(vecT_mat(u, Cbil), v)
# spin-invariant: b(sigma u, v) + b(u, sigma v) = 0 for sigma in spin(9,5)
ok = True
for p in ((0, 1), (4, 5), (3, 9)):
    u, v = rand_spinor(), rand_spinor()
    s = SIG[p]
    r = bilinform(mat_vec(s, u), v) + bilinform(u, mat_vec(s, v))
    if not r.is_zero():
        ok = False
uu, vv = rand_spinor(), rand_spinor()
check(ok and not bilinform(uu, vv).is_zero(),
      "v^T C_bilin w is NONZERO and spin(9,5)-INVARIANT (exact witnesses) -- "
      "the toy's bilinear pairing channel, alive at anchor scale over spin")
# but NOT invariant under the u(1) center: the bilinear form has charge -2
# (i Id acts as +i on each slot => b(iu,v)+b(u,iv) = 2i b != 0):
u, v = rand_spinor(), rand_spinor()
defect = bilinform(mat_vec(ZC, u), v) + bilinform(u, mat_vec(ZC, v))
check(defect == GC(0, 2) * bilinform(u, v) and not defect.is_zero(),
      "the bilinear form carries central charge +2: b(iu,v)+b(u,iv) = 2i b "
      "!= 0 (exact) => it is KILLED as a u(64,64)-equivariant channel but "
      "SURVIVES over the centerless g_H")
note("=> DISTINCT reality structures, BOTH real (neither complexified):")
note("   (i)  u(64,64) reading (WITH center): the central charge kills the")
note("        bilinear channel; only the SESQUILINEAR Krein bracket M(Q,P)")
note("        survives; odd module = S_R (256-dim real). Reality is FORCED")
note("        by the fiber's center, not imposed -- resolving the toy's")
note("        'complexified / real form unselected' limit.")
note("   (ii) g_H = sp(p,q) reading (H-respecting, CENTERLESS): J is a gauge")
note("        symmetry; BOTH a sesquilinear (Krein) and a bilinear (charge-")
note("        conjugation) odd channel are available -- the honest M(64,H)")
note("        quaternionic real form. Which gauge algebra GU intends is SG4.")

# ======================================================================
# PART 6: the central charge SELECTS the real (sesquilinear) form (exact)
# ======================================================================
print("\n--- PART 6: the u(1) center forces the sesquilinear reality ---")
# i Id acts as +i on S (exact), so Sym^2 S has charge +2, Sym^2 S-bar charge
# -2, and the sesquilinear channel S-bar (x) S has charge 0.
v = rand_spinor()
check(viszero(vsub(mat_vec(ZC, v), vscal(GI, v))),
      "central charge i*Id acts as +i on every spinor (exact) => Sym^2 S has "
      "charge +2, Sym^2 S-bar charge -2, S-bar(x)S charge 0")
# an equivariant map Sym^2 S -> u_beta (charge 0) must vanish: if K:Sym^2 S ->
# g intertwines, then 2i K = [z, K] = 0 for the central z=i Id. Witness the
# obstruction on the constructed bilinear channel B(Q,P)=(C_bilin pairing into
# g via the invariant form): its would-be g-image transforms with charge +2.
note("Equivariance under the center alone forces any Sym^2 S -> u_beta or")
note("Sym^2 S-bar -> u_beta bracket to vanish (2i B = [i Id, B] = 0).")
note("Only the sesquilinear S-bar(x)S channel (charge 0) can map to the")
note("charge-0 gauge algebra -- and that channel is EXACTLY the Krein")
note("pairing M, M_0 of PART 3, which is intrinsically REAL. Hence at anchor")
note("scale the real (Krein) form is SELECTED, not chosen: complexification")
note("is not available (the complex-bilinear brackets are dead over u(64,64)).")
# consistency: the surviving pairing M is charge 0 (sesquilinear): [z,M]=0
Q, P = rand_spinor(), rand_spinor()
check(miszero(mcomm(ZC, pair_M(Q, P))),
      "the surviving Krein bracket M(Q,P) is central-charge NEUTRAL "
      "([i Id, M] = 0) (exact) -- consistent with the sesquilinear channel")

# ======================================================================
# PART 7 (Q3): derivative-level odd tau_plus -- requirement + finite shadow
# ======================================================================
print("\n--- PART 7 (Q3): derivative-level odd tau_plus ---")
note("REQUIREMENT (exact statement). The even tau_plus embeds the gauge group")
note("as tau_+(g) = (g, g^{-1} d_aleph g) in IG = G |x Omega^1(ad); at Lie")
note("level d tau_+(xi) = (xi, d_aleph xi), whose homomorphism property is the")
note("Leibniz 1-cocycle d_aleph[xi,eta] = [xi,d_aleph eta] - [eta,d_aleph xi].")
note("The ODD tau_plus (steelman S3) sends a scalar-spinor eps in Omega^0(S)")
note("to (eps, D_aleph eps) in Omega^0(S) (+) Omega^1(S). A derivative-level")
note("closure check requires THREE things the pointwise bracket cannot see:")
note("  (D1) D_aleph a beta-COMPATIBLE covariant derivative -- so D_aleph eps")
note("       is a legitimate Krein spinor-valued 1-form (reality preserved);")
note("  (D2) a Leibniz identity making the Clifford pairing of D-images match")
note("       d_aleph of the pairing (the odd 1-cocycle condition);")
note("  (D3) the curvature F_aleph = d_aleph^2 controlled (obstruction to the")
note("       homomorphism at second order).")

# FINITE SHADOW (frozen, flat): model one covariant-derivative direction by a
# constant fiber operator D_mu (the derivative FROZEN to a point). D_mu must be
# beta-compatible so it maps Krein spinors to Krein spinors: the natural choice
# is D_mu in u_beta.  The frozen [transl, Omega^0(S)] -> Omega^1(S) action of
# LEG-1's R3 IS this shadow with the derivative frozen; here we add the REALITY
# layer and verify it closes exactly.
Dmu = [rand_ubeta() for _ in range(4)]     # four frozen, beta-compatible D's
check(all(in_ubeta(D) for D in Dmu),
      "(D1) frozen covariant-derivative directions D_mu chosen in u_beta "
      "(beta-compatible) => D_mu eps stays a Krein spinor (reality preserved)")
# the derivative-twisted Krein cross-pairing lands in u_beta (reality survives
# the derivative at first order): M(Q, D_mu P) + M(D_mu Q, P) in u_beta.
ok = True
for _ in range(4):
    Q, P = rand_spinor(), rand_spinor()
    for mu in range(4):
        cross = madd(pair_M(Q, mat_vec(Dmu[mu], P)),
                     pair_M(mat_vec(Dmu[mu], Q), P))
        if not in_ubeta(cross):
            ok = False
check(ok, "(D2 shadow) the derivative-twisted Krein pairing M(Q,D_mu P) + "
      "M(D_mu Q,P) stays in u(64,64) (exact) -- the odd 1-cocycle's Krein "
      "reality holds at FROZEN-flat first order")
# the obstruction lives in [D_mu, D_nu]: in the frozen model this is a fixed
# u_beta element (a would-be field strength); in the TRUE theory it must equal
# the curvature F_aleph of the connection -- data absent from the finite fiber.
Fmn = mcomm(Dmu[0], Dmu[1])
# the frozen model realizes a specific u_beta 'field strength'; the manifold
# fixes the true one via F_aleph = d_aleph^2 (data absent from a single fiber).
check(in_ubeta(Fmn),
      "(D3) [D_0, D_1] in u_beta (exact) -- the frozen 'curvature' is a "
      "gauge-algebra element (Krein-compatible)")
check(not miszero(Fmn),
      "[D_0, D_1] != 0 (exact) -- the two derivative directions do NOT "
      "commute: d_aleph^2 = F_aleph is GENERICALLY nonzero, and the finite "
      "fiber cannot certify it equals the connection's curvature")
note("VERDICT (Q3): the FINITE (frozen, flat, beta-compatible) shadow of the")
note("odd tau_plus 1-cocycle CLOSES exactly and PRESERVES the Krein reality --")
note("the reality layer (D1,D2) transfers. The genuine derivative-level")
note("homomorphism is BLOCKED on the exact missing structure: the connection")
note("aleph on the base Y, the covariant d_aleph as a first-order differential")
note("operator (NOT a fiber endomorphism), and the identity F_aleph = d_aleph^2")
note("relating {odd,odd} in Omega^1(ad) to the base curvature. These are")
note("infinite-dimensional / geometric and outside a single-fiber model. This")
note("is the honest boundary: real/Krein form DECIDED (survives); derivative-")
note("level odd tau_plus BLOCKED with its missing structure named.")

# ======================================================================
# SUMMARY
# ======================================================================
print("\n" + "=" * 78)
print("SUMMARY -- LEG-2 (real/Krein form; anchor scale; Q2 + Q3 shadow)")
print("=" * 78)
print("""
 Q2 ANSWER: the scalar-spinor closure SURVIVES the honest real/Krein form.
 It does NOT require complexification. Two exact facts carry it:

  (1) beta_S-COMPATIBILITY IS EXACT AND AUTOMATIC. The odd bracket's image
      M(Q,P) = i(Q P^dag beta + P Q^dag beta) is pseudo-anti-Hermitian --
      lands in the REAL form u(64,64) -- for EVERY pair Q,P, provably from
      beta^dag = beta ALONE (symbolic *-word certificate K1; no Clifford
      identity, no complexification), and s(Q,P) is real so M_0 = i s Id is
      central in u_beta. Instantiated exactly on the 128-dim fiber.

  (2) THE ANCHOR'S u(1) CENTER SELECTS THE REAL FORM. i*Id acts as +i on S,
      so the complex-BILINEAR channels Sym^2 S -> u_beta carry charge +/-2
      and are dead; only the charge-0 SESQUILINEAR Krein channel survives,
      and it is intrinsically real. Reality is FORCED by the fiber, not
      imposed -- resolving the toy's 'complexified / real form unselected'
      limit. (Toy so(4) had no center; there the bilinear C-pairings
      carried the channel.)

 THE QUATERNIONIC M(64,H) STRUCTURE (sharper reading, exact): J(v)=C conj(v)
 with J^2 = -I is CONSTRUCTED exactly (matches Cl(9,5)=M(64,H); q-p=4 mod 8).
 J commutes with the Clifford algebra (beta, spin(9,5)) but ANTI-commutes
 with the central charge i*Id and does NOT commute with generic u(64,64).
 Consequences (all exact-witnessed):
   - Over the FULL u(64,64): S is COMPLEX-type (no antilinear commutant);
     the only compatible real form is the underlying real S_R (dim_R 256).
     The super-algebra is REAL (LEG-1's closure), no complexification; J is
     present on S but is NOT a gauge symmetry.
   - Over the H-respecting subalgebra g_H = u_beta cap gl(64,H) = sp(p,q)-
     type (contains spin(9,5), EXCLUDES the u(1) center): J IS a symmetry and
     a spin-invariant BILINEAR channel (charge conjugation C_bilin) also
     exists -- the genuine quaternionic real form. BOTH channels real.
   Which gauge algebra GU intends (u(64,64) with center, or the centerless
   quaternionic g_H) is an SG4 selection, not decided here.

 HONEST TENSION (understanding, not a verdict): the SAME J that realizes the
 M(64,H) reality anticommutes with the central charge that FORCES the
 sesquilinear reality. The 'central-charge-forced' real form (needs the u(1))
 and the 'quaternionic' real form (needs J, excludes the u(1)) are DIFFERENT
 real forms; each is consistent and complexification-free; they do not
 coincide.

 Q3 (derivative-level odd tau_plus): finite (frozen, flat, beta-compatible)
 shadow CLOSES exactly and preserves Krein reality; the genuine derivative-
 level homomorphism is BLOCKED on named missing structure (the connection
 aleph on Y, the covariant d_aleph as a first-order operator, and
 F_aleph = d_aleph^2 tying {odd,odd} in Omega^1(ad) to the base curvature).

 FIREWALL: no chi(K3), no 24, no /8, no A-hat=3, no topology; the bare 58.72
 commutator is never formed. All load-bearing claims exact.
""")
print("TOTAL: %d checks passed, exit 0 [t=%.0fs]"
      % (NCHECK[0], time.time() - T0))
sys.exit(0)
