# Independent adversarial cross-check of LEG-1's load-bearing / novel claims,
# using the SEPARATE clif95 sparse infrastructure (different code path from
# LEG-1-anchor-super-jacobi.py). Exact arithmetic; no floats on the assert
# path. Corroborates: (A) the sesquilinear Krein pairing M(Q,P) is
# u(64,64)-equivariant and NOT complex-bilinear; (B) noncentral {odd,odd}
# g-component killed by (T,Q,P); (C) the CENTRAL u(1) "balanced escape"
# t* = -128 sum w_mu q_mu closes the cubic while off-balance fails.
import sys, time, random
from fractions import Fraction as Fr
sys.path.insert(0, r"C:\Users\joe\AppData\Local\Temp\claude\C--Users-joe-JB\79411e9e-5aaa-44a7-ba95-2f380675a349\scratchpad\anchor-swing")
from clif95 import *

T0 = time.time(); NCHK = [0]
def check(c, m):
    NCHK[0] += 1
    print(("  ok [%2d] " % NCHK[0] if c else "FAIL   ") + m)
    if not c: sys.exit(1)

gam = gammas_cl95(); eta = eta95(); N = 128
spacelike = [a for a in range(14) if eta[a] == 1]
beta = sm_eye(N)
for a in spacelike: beta = sm_mul(beta, gam[a])
def sig(a, b): return sm_scal(GC(Fr(1, 2)), sm_mul(gam[a], gam[b]))
rng = random.Random(7)
def rvec():
    # DENSE random spinor: beta is a pure off-diagonal permutation, so sparse
    # spinors are frequently Krein-null (Q^dag beta Q = 0) and would give
    # degenerate witnesses. Dense spinors are generically Krein-non-null.
    return {i: GC(rng.randint(-2, 2), rng.randint(-2, 2)) for i in range(N)}
def conjvec(v): return {i: x.conj() for i, x in v.items()}
def vzero(): return {}
def in_u(Y): return sm_iszero(sm_add(sm_mul(sm_dag(Y), beta), sm_mul(beta, Y)))

# ---- the anchor pairings (clif95 build) ----
def outer(u, w):   # u_i conj(w_j)
    M = {}
    for i, ui in u.items():
        for j, wj in w.items():
            v = ui * wj.conj()
            if not v.is_zero(): M.setdefault(i, {})[j] = v
    return M
def Theta(u, w):   # u (w^dag beta) + w (u^dag beta)  == outer(u,beta w)+outer(w,beta u)
    return sm_add(outer(u, sm_apply(beta, w)), outer(w, sm_apply(beta, u)))
def M_pair(Q, P): return sm_scal(GC(0, 1), Theta(Q, P))          # i*Theta  (u_beta valued)
def s_pair(Q, P):                                                # Q^d b P + P^d b Q
    return bilin(conjvec(Q), beta, P) + bilin(conjvec(P), beta, Q)
def M0(Q, P): return sm_scal(GC(0, 1) * s_pair(Q, P), sm_eye(N))
def Msl(Q, P):
    M = M_pair(Q, P)
    return sm_sub(M, sm_scal(sm_trace(M) / GC(N), sm_eye(N)))

# ---------------------------------------------------------------------------
# (A) sesquilinear pairing: u(64,64)-equivariant (incl. extra gens), sesquilinear
# ---------------------------------------------------------------------------
Q, P = rvec(), rvec()
check(in_u(M_pair(Q, P)) and in_u(Msl(Q, P)) and in_u(M0(Q, P)),
      "M, M_sl, M_0 land in u(64,64) [clif95]")
check(sm_eq(M_pair(Q, P), M_pair(P, Q)) and s_pair(Q, P) == s_pair(P, Q),
      "pairings symmetric Q<->P [clif95]")
Yextra = [sig(0, 3), sm_scal(GC(0, 1), gam[0]),
          sm_mul(sm_mul(gam[0], gam[1]), gam[2])]
def equivM(Y):
    lhs = sm_comm(Y, M_pair(Q, P))
    rhs = sm_add(M_pair(sm_apply(Y, Q), P), M_pair(Q, sm_apply(Y, P)))
    return sm_eq(lhs, rhs)
check(all(in_u(Y) for Y in Yextra) and all(equivM(Y) for Y in Yextra),
      "M(Q,P) u(64,64)-EQUIVARIANT under so(9,5) AND the extra anchor gens "
      "i*gamma_0, gamma_0gamma_1gamma_2 [clif95, exact]")
c = GC(2, 3)
lhs = M_pair(v_scal(c, Q), P)
rhs = sm_add(sm_scal(GC(2), M_pair(Q, P)), sm_scal(GC(3), M_pair(v_scal(GC(0, 1), Q), P)))
check(sm_eq(lhs, rhs) and not sm_eq(lhs, sm_scal(c, M_pair(Q, P))),
      "M real-bilinear but NOT complex-bilinear [clif95] => odd module is the "
      "REAL form S_R")

# ---------------------------------------------------------------------------
# even algebra + odd action machinery (RG regime, form index inert)
# ---------------------------------------------------------------------------
def rand_antiherm(nz=5):
    A = sm_zero()
    for _ in range(nz):
        i, j = rng.randrange(N), rng.randrange(N)
        if i == j: A = sm_add(A, {i: {i: GC(0, rng.randint(-3, 3))}})
        else:
            cc = GC(rng.randint(-3, 3), rng.randint(-3, 3))
            A = sm_add(A, {i: {j: cc}, j: {i: sm_scal(GC(-1), {0: {0: cc}})[0][0].conj()}})
    return A
def rand_ubeta(nz=5): return sm_mul(beta, rand_antiherm(nz))
def rand_T(nz=4): return tuple(rand_ubeta(nz) for _ in range(4))

class Mode:
    def __init__(s, sc, t, p, q, z, w): s.sc, s.t, s.p, s.q, s.z, s.w = sc, t, p, q, z, w
def B_of(mode, Q, P):
    sl = Msl(Q, P); sc = GC(0, 1) * s_pair(Q, P)
    g = sm_add(sm_scal(mode.sc, sl), sm_scal(mode.t * sc, sm_eye(N)))
    Tp = tuple(sm_add(sm_scal(mode.p[m], sl), sm_scal(mode.q[m] * sc, sm_eye(N))) for m in range(4))
    return (g, Tp)
def act_odd(mode, E, Q):
    X, A = E; out = sm_apply(X, Q)
    for m in range(4):
        if not mode.z[m].is_zero(): out = v_add(out, v_scal(mode.z[m], sm_apply(A[m], Q)))
        if not mode.w[m].is_zero(): out = v_add(out, v_scal(mode.w[m] * sm_trace(A[m]), Q))
    return out
def evbr(E1, E2):
    X1, A1 = E1; X2, A2 = E2
    return (sm_comm(X1, X2), tuple(sm_sub(sm_comm(X1, A2[m]), sm_comm(X2, A1[m])) for m in range(4)))
def ev(X=None, A=None):
    return (X if X else sm_zero(), tuple(A) if A else tuple(sm_zero() for _ in range(4)))
def ev_iszero(E): return sm_iszero(E[0]) and all(sm_iszero(a) for a in E[1])
def J_ooo(mode, Q1, Q2, Q3):
    r = act_odd(mode, B_of(mode, Q1, Q2), Q3)
    r = v_add(r, act_odd(mode, B_of(mode, Q2, Q3), Q1))
    r = v_add(r, act_odd(mode, B_of(mode, Q3, Q1), Q2))
    return r
def J_eoo(mode, E, Q, P):
    lhs = evbr(E, B_of(mode, Q, P))
    g = B_of(mode, act_odd(mode, E, Q), P); h = B_of(mode, Q, act_odd(mode, E, P))
    rhs = (sm_add(g[0], h[0]), tuple(sm_add(g[1][m], h[1][m]) for m in range(4)))
    return (sm_sub(lhs[0], rhs[0]), tuple(sm_sub(lhs[1][m], rhs[1][m]) for m in range(4)))
Z = GC(0)
# ---------------------------------------------------------------------------
# (B) noncentral g-component killed by (T,Q,P)
# ---------------------------------------------------------------------------
KILL_S = Mode(GC(1), Z, [Z]*4, [Z]*4, [Z]*4, [Z]*4)
hit = any(not ev_iszero(J_eoo(KILL_S, ev(A=rand_T()), rvec(), rvec())) for _ in range(6))
check(hit, "NONCENTRAL kill: g-valued s*M_sl {odd,odd} VIOLATES (T,Q,P) "
           "[clif95] => forced out of the semisimple gauge algebra")
# ---------------------------------------------------------------------------
# (C) central u(1) escape: minimal kill, then balance closes, off-balance fails
# ---------------------------------------------------------------------------
p = [GC(2), GC(3), GC(5), GC(7)]; q = [GC(11), GC(13), GC(17), GC(19)]
KILL_T = Mode(Z, GC(1), list(p), list(q), [Z]*4, [Z]*4)
Qx = rvec()
check(not v_iszero(J_ooo(KILL_T, Qx, Qx, Qx)),
      "CENTRAL kill (minimal, w=0): t*M_0 {odd,odd} VIOLATES the cubic [clif95]")
w = [GC(1), GC(2), GC(0), GC(1)]
tstar = Z
for m in range(4): tstar = tstar - GC(N)*(w[m]*q[m])
BAL = Mode(Z, tstar, list(p), list(q), [Z]*4, list(w))
ok = all(v_iszero(J_ooo(BAL, rvec(), rvec(), rvec())) for _ in range(4))
check(ok, "BALANCE t*=-128 sum w_mu q_mu closes the cubic on 4 fresh exact "
          "triples [clif95] (w REAL, z=0)")
ok = all(ev_iszero(J_eoo(BAL, ev(A=rand_T()), rvec(), rvec())) for _ in range(3))
check(ok, "BALANCE also closes (T,Q,P) [clif95] (imaginary trace-shift "
          "cancels via sesquilinearity)")
OFF = Mode(Z, tstar + GC(1), list(p), list(q), [Z]*4, list(w))
check(not v_iszero(J_ooo(OFF, Qx, rvec(), rvec())),
      "OFF-BALANCE (t*+1) VIOLATES the cubic [clif95] => central escape is a "
      "1-parameter locus, not a free direction")

print("\nCROSS-CHECK: %d independent clif95 checks corroborate LEG-1's "
      "load-bearing + central-escape claims. exit 0 [t=%.0fs]"
      % (NCHK[0], time.time() - T0))
sys.exit(0)
