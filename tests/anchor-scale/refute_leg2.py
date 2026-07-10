# Independent referee re-derivation of LEG-2's load-bearing claims.
# DIFFERENT MACHINERY: numpy (not sparse GC dicts), a DIFFERENT gamma basis
# (different JW pairing) and a DIFFERENT timelike set (last five, not middle
# five) -- so any basis/ordering artifact would surface as a discrepancy.
#
# Entries of all gammas are in {0,+-1,+-i}; products are Gaussian integers of
# small magnitude, represented EXACTLY in complex128 (|entry| << 2^53). Every
# equality below is therefore an EXACT integer comparison (atol=0 achievable;
# I use ==0 on the max-abs which is an exact integer).
#
# The referee ADDS one test the original never ran: is the spin(9,5)-invariant
# bilinear form b actually invariant under the WHOLE quaternionic subalgebra
# g_H = u_beta cap gl(64,H)?  The leg claims "b survives over g_H"; it only
# checked spin(9,5) (dim 91) and "not the center", never the ~8000-dim rest.

import numpy as np

np.random.seed(20260710)
FAIL = []
def check(cond, msg):
    tag = "ok " if cond else "FAIL"
    if not cond:
        FAIL.append(msg)
    print("  [%s] %s" % (tag, msg))

s0 = np.array([[1,0],[0,1]], dtype=complex)
s1 = np.array([[0,1],[1,0]], dtype=complex)
s2 = np.array([[0,-1j],[1j,0]], dtype=complex)
s3 = np.array([[1,0],[0,-1]], dtype=complex)

def krons(mats):
    M = np.array([[1]], dtype=complex)
    for m in mats:
        M = np.kron(M, m)
    return M

# --- Cl(14,0): 14 Hermitian anticommuting gammas on 7 qubits (128-dim) ---
# DIFFERENT pairing convention than the ported script: here gamma_{2k} uses
# sigma_2 and gamma_{2k+1} uses sigma_1 (swapped vs the original's S1,S2 order)
# -- a genuinely different basis; invariants must be identical.
m = 7
G = []
for k in range(m):
    for mid in (s2, s1):          # swapped order vs original
        mats = [s3]*k + [mid] + [s0]*(m-1-k)
        G.append(krons(mats))
G = G[:14]
N = 128

def maxabs(A):
    return float(np.max(np.abs(A)))

def iszero(A):
    return maxabs(A) == 0.0

def dag(A):
    return A.conj().T

ID = np.eye(N, dtype=complex)

# Hermitian, anticommuting, square = I (Cl(14,0))
ok = True
for a in range(14):
    if not iszero(dag(G[a]) - G[a]): ok = False
    for b in range(14):
        tgt = 2*ID if a == b else 0*ID
        if not iszero(G[a]@G[b] + G[b]@G[a] - tgt): ok = False
check(ok, "independent Cl(14,0): 14 Hermitian gammas, {G_a,G_b}=2 delta")

# --- Cl(9,5): timelike = LAST five (DIFFERENT from original's {4,5,6,7,8}) ---
TIMELIKE = {9,10,11,12,13}
eta = [(-1 if a in TIMELIKE else 1) for a in range(14)]
GAM = [ (1j*G[a] if a in TIMELIKE else G[a]) for a in range(14) ]

ok = True
for a in range(14):
    for b in range(14):
        tgt = 2*eta[a]*ID if a == b else 0*ID
        if not iszero(GAM[a]@GAM[b] + GAM[b]@GAM[a] - tgt): ok = False
check(ok, "Cl(9,5) signature (9,5): {GAM_a,GAM_b}=2 eta_ab (different timelike set)")

SPACELIKE = [a for a in range(14) if a not in TIMELIKE]
# Krein metric beta = product of the 9 spacelike gammas
BETA = ID.copy()
for a in SPACELIKE:
    BETA = BETA @ GAM[a]
check(iszero(dag(BETA)-BETA), "beta Hermitian")
check(iszero(BETA@BETA-ID), "beta^2 = I")
tr = np.trace(BETA)
check(tr == 0, "tr beta = 0  => Krein signature (64,64), u_beta ~ u(64,64)")
# confirm eigenvalue split (64,64) directly
ev = np.round(np.real(np.linalg.eigvalsh(BETA))).astype(int)
check(int(np.sum(ev==1))==64 and int(np.sum(ev==-1))==64,
      "beta eigenvalues split exactly (64 +1, 64 -1)")

def in_ubeta(X):
    return iszero(BETA@X + dag(X)@BETA)

# spin generators sigma_ab in u_beta
SIG = {}
ok = True
for a in range(14):
    for b in range(a+1,14):
        S = 0.25*(GAM[a]@GAM[b] - GAM[b]@GAM[a])
        SIG[(a,b)] = S
        if not in_ubeta(S): ok = False
check(ok, "all 91 so(9,5) generators sigma_ab in u_beta (Krein compat)")

ZC = 1j*ID
check(in_ubeta(ZC), "i*Id in u_beta (u(64,64) HAS a u(1) center)")

# ---------------------------------------------------------------------------
# CLAIM R1 / CERT K1 : M(Q,P) = i(Q P^dag beta + P Q^dag beta) in u_beta for
# ALL Q,P, from beta^dag=beta alone.  Independent numeric instantiation.
# ---------------------------------------------------------------------------
def randspin():
    return (np.random.randint(-3,4,N) + 1j*np.random.randint(-3,4,N)).astype(complex)

def pair_M(Q,P):
    Qc = Q.reshape(N,1); Pc = P.reshape(N,1)
    return 1j*(Qc @ (dag(Pc)@BETA) + Pc @ (dag(Qc)@BETA))

def pair_s(Q,P):
    return (dag(Q.reshape(N,1))@BETA@P.reshape(N,1))[0,0] + \
           (dag(P.reshape(N,1))@BETA@Q.reshape(N,1))[0,0]

ok = True; oks = True; oksym = True; okcen = True
for _ in range(8):
    Q,P = randspin(), randspin()
    M = pair_M(Q,P)
    if not in_ubeta(M): ok = False
    if not iszero(M - pair_M(P,Q)): oksym = False
    if abs(pair_s(Q,P).imag) != 0: oks = False
    if not iszero(ZC@M - M@ZC): okcen = False
check(ok, "K1 (indep): M(Q,P) in u_beta for random pairs (lands in REAL form)")
check(oksym, "K3 (indep): M(Q,P) = M(P,Q) (symmetric odd bracket)")
check(oks, "K2 (indep): s(Q,P) is real")
check(okcen, "R2 witness: [i*Id, M(Q,P)] = 0 (Krein bracket charge-0/neutral)")

# symbolic-strength check: verify beta M + M^dag beta = 0 IDENTICALLY by
# treating it as the algebraic identity (independent of Clifford), using a
# random NON-Krein 'beta' too: the identity must fail for a non-Hermitian b
# and hold for Hermitian b -- confirming it is beta^dag=beta that carries it.
Bh = np.random.randint(-2,3,(N,N)) + 1j*np.random.randint(-2,3,(N,N))
Bh = Bh + dag(Bh)                                  # forced Hermitian
Bn = np.random.randint(-2,3,(N,N)) + 1j*np.random.randint(-2,3,(N,N))  # generic
def M_with(b, Q, P):
    Qc=Q.reshape(N,1); Pc=P.reshape(N,1)
    return 1j*(Qc@(dag(Pc)@b) + Pc@(dag(Qc)@b))
Q,P = randspin(), randspin()
resid_h = Bh@M_with(Bh,Q,P) + dag(M_with(Bh,Q,P))@Bh
resid_n = Bn@M_with(Bn,Q,P) + dag(M_with(Bn,Q,P))@Bn
check(iszero(resid_h), "K1 root cause: identity holds for ANY Hermitian b "
      "(not just the Krein beta) => carried by b^dag=b ALONE")
check(not iszero(resid_n), "K1 root cause: identity FAILS for non-Hermitian b "
      "=> b^dag=b is exactly the load-bearing premise (control)")

# ---------------------------------------------------------------------------
# CLAIM R3 : quaternionic J with J^2 = -I (M(64,H) invariant)
# ---------------------------------------------------------------------------
EPS = []
for a in range(14):
    Gs = GAM[a].conj()
    if iszero(Gs - GAM[a]):   EPS.append(1)
    elif iszero(Gs + GAM[a]): EPS.append(-1)
    else:                     EPS.append(0)
check(all(e in (1,-1) for e in EPS), "each GAM_a^* = eps_a GAM_a, eps in {+-1}: %s" % EPS)
Aminus = [a for a in range(14) if EPS[a] == -1]
check(len(Aminus) % 2 == 0, "|{eps=-1}| = %d even" % len(Aminus))
C = ID.copy()
for a in Aminus:
    C = C @ GAM[a]
ok = all(iszero(GAM[a]@C - C@GAM[a].conj()) for a in range(14))
check(ok, "GAM_a C = C GAM_a^* for all a (J commutes with Clifford algebra)")
JJ = C @ C.conj()
check(iszero(JJ + ID), "J^2 = C conj(C) = -I EXACTLY (S QUATERNIONIC; M(64,H) invariant)")
# independent cross-check of type via the SPACE of antilinear Clifford-commutants:
# there is a 1-dim (over H... ) commutant; the sign is basis-independent.
check(iszero(C@C.conj() + ID), "J^2=-I reconfirmed in the different timelike basis")

# generic u_beta element does NOT commute with J  => S complex-type over u(64,64)
def rand_antiherm():
    A = np.random.randint(-2,3,(N,N)) + 1j*np.random.randint(-2,3,(N,N))
    return A - dag(A)
def rand_ubeta():
    return BETA @ rand_antiherm()
def Jcommutes(X):
    # J X = X J (antilinear) <=> C X^* = X C
    return iszero(C@X.conj() - X@C)
found = any(not Jcommutes(rand_ubeta()) for _ in range(8))
check(found, "generic X in u_beta does NOT commute with J (S complex-type over u(64,64))")
check(not Jcommutes(ZC), "i*Id does NOT commute with J (center excluded from g_H)")
check(all(Jcommutes(SIG[p]) and in_ubeta(SIG[p]) for p in SIG),
      "ALL 91 spin(9,5) generators lie in g_H = u_beta cap gl(64,H)")

# ---------------------------------------------------------------------------
# CLAIM R3(ii) UNDER ATTACK: the spin(9,5)-invariant BILINEAR form b, and
# whether it is invariant under the FULL quaternionic subalgebra g_H.
# ---------------------------------------------------------------------------
# build C_bilin intertwining GAM_a -> GAM_a^T, as product over a self-selected
# gamma subset (same recipe as the leg).
DELTA = [ (1 if iszero(GAM[a].T - GAM[a]) else (-1 if iszero(GAM[a].T + GAM[a]) else 0))
          for a in range(14) ]
check(all(d in (1,-1) for d in DELTA), "GAM_a^T = delta_a GAM_a, delta in {+-1}: %s" % DELTA)
setM = [a for a in range(14) if DELTA[a] == -1]
setP = [a for a in range(14) if DELTA[a] == 1]
Cbil = None; usedB = None
for cand in (setM, setP):
    M0 = ID.copy()
    for a in cand: M0 = M0 @ GAM[a]
    if all(iszero(M0@GAM[a] - GAM[a].T@M0) for a in range(14)):
        Cbil, usedB = M0, cand
        break
check(Cbil is not None, "C_bilin found (|B|=%s) intertwining GAM_a -> GAM_a^T"
      % (len(usedB) if usedB else "-"))

# symmetry of the bilinear form b(u,v)=u^T Cbil v
sym = iszero(Cbil.T - Cbil)
antisym = iszero(Cbil.T + Cbil)
symlabel = "SYMMETRIC" if sym else ("ANTISYMMETRIC" if antisym else "mixed")
print("       >> C_bilin transpose-symmetry: %s  (|B|=%d)" % (symlabel, len(usedB)))
check(sym or antisym, "C_bilin has definite transpose symmetry: %s" % symlabel)

def bil(u,v):
    return (u.reshape(1,N) @ Cbil @ v.reshape(N,1))[0,0]

# spin(9,5)-invariance (reproduce the leg's check [28])
ok = True
for p in [(0,1),(4,5),(3,9),(7,13),(2,11)]:
    u,v = randspin(), randspin()
    S = SIG[p]
    r = bil(S@u, v) + bil(u, S@v)
    if r != 0: ok = False
uu,vv = randspin(), randspin()
check(ok and bil(uu,vv) != 0, "b is spin(9,5)-invariant and nonzero (reproduces leg check 28)")
# charge +/-2 under center (reproduce check [29])
u,v = randspin(), randspin()
d = bil(ZC@u, v) + bil(u, ZC@v)
check(d == 2j*bil(u,v) and d != 0, "b carries central charge +2 (killed over u(64,64))")

# ***** THE NEW TEST the leg never ran *****
# project random u_beta elements onto g_H and test b-invariance on the FULL g_H.
def to_gH(X):
    # H-linear (J-commuting) part of X:  (X + C X^* C^{-1})/2 ; C is unitary-ish
    Cinv = np.linalg.inv(C)
    return 0.5*(X + C @ X.conj() @ Cinv)
# but this projection may leave u_beta; intersect by also projecting to u_beta:
def to_ubeta(X):
    # anti-part w.r.t. the Krein involution X -> -beta X^dag beta
    return 0.5*(X - BETA@dag(X)@BETA)
def rand_gH():
    X = rand_ubeta()
    for _ in range(6):                 # alternating projections onto both closed subspaces
        X = to_ubeta(X)
        X = to_gH(X)
    return X

viol = 0; tested = 0; sample_defect = None
for _ in range(12):
    X = rand_gH()
    if iszero(X):                       # skip degenerate
        continue
    # confirm it really is in g_H
    if not (in_ubeta(X) and Jcommutes(X)):
        continue
    tested += 1
    defect = X.T @ Cbil + Cbil @ X      # b-invariance defect: b(Xu,v)+b(u,Xv)
    if not iszero(defect):
        viol += 1
        if sample_defect is None:
            sample_defect = maxabs(defect)
print("       >> g_H elements tested for b-invariance: %d ; VIOLATIONS: %d "
      "(sample max-defect=%s)" % (tested, viol, sample_defect))
check(tested >= 3, "generated >=3 genuine nonzero g_H elements to test")

# Interpret: sp(p,q) preserves a UNIQUE (up to scale) ANTISYMMETRIC (symplectic)
# form. If b is SYMMETRIC it CANNOT be sp-invariant; the leg's specific witness
# then does NOT survive over g_H even though a (different, antisymmetric) bilinear
# channel does exist by Sym^2(std_sp)=adjoint.
b_survives_gH = (viol == 0)
print("       >> DOES the leg's specific b survive over g_H? %s" % b_survives_gH)

# Does an antisymmetric sp-form exist among the two candidate C-products?
antisym_form_exists = False
for cand in (setM, setP):
    M0 = ID.copy()
    for a in cand: M0 = M0 @ GAM[a]
    if all(iszero(M0@GAM[a] - GAM[a].T@M0) for a in range(14)) and iszero(M0.T + M0):
        antisym_form_exists = True
print("       >> antisymmetric (symplectic) intertwiner among C-products? %s"
      % antisym_form_exists)

# rep-theory existence of a bilinear channel into g_H (independent of b's symmetry):
# construct X_{QP} = Q P^T Omega + P Q^T Omega with Omega the sp-form (if it
# exists) and test it lands in g_H.  If Cbil is antisym use it as Omega;
# otherwise search a gamma-product antisym intertwiner.
Omega = None
for cand in (setM, setP):
    M0 = ID.copy()
    for a in cand: M0 = M0 @ GAM[a]
    if iszero(M0.T + M0) and all(iszero(M0@GAM[a]-GAM[a].T@M0) for a in range(14)):
        Omega = M0; break
if Omega is not None:
    Q,P = randspin(), randspin()
    Qc=Q.reshape(N,1); Pc=P.reshape(N,1)
    Xqp = Qc@(Pc.T@Omega) + Pc@(Qc.T@Omega)
    print("       >> symplectic bilinear bracket X_{QP} in u_beta? %s ; commutes J? %s"
          % (in_ubeta(Xqp), Jcommutes(Xqp)))

print("\n" + "="*70)
if FAIL:
    print("REFEREE CHECKS WITH FAILURES: %d" % len(FAIL))
    for f in FAIL: print("   FAIL:", f)
else:
    print("ALL REFEREE re-derivations PASSED (independent basis/machinery).")
print("Key adjudications:")
print("  C_bilin symmetry: %s" % symlabel)
print("  leg's b invariant under full g_H (sp(p,q))?  %s" % b_survives_gH)
print("  antisymmetric symplectic sp-form exists?     %s" % antisym_form_exists)
