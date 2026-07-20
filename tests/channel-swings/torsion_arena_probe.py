#!/usr/bin/env python3
"""Torsion generation arena probe -- the J-homomorphism / framing-twist route.

CHANNEL: generation-count torsion arena (Z/3 in Z/24 = pi_3^s).
DESIGN:  explorations/torsion-generation-arena-2026-07-20.md
IMPORTS: tests/generation-sector/gen_sector_bridge.py (verified Cl(9,5)=M(64,H) rep)
STATUS:  exploration tier; R0_COND (framed-reading fork); no claim/canon/posture movement.

WHAT IS COMPUTED (fixture grade, on the actual frozen rep):
  [T]  setup: anchors, K_S, exact J_quat facts, the Z/24 CRT arithmetic, quadrature control.
  [E1] C = e1 e3 e5 e7 e10 e12 is ANTISYMMETRIC unitary => Autonne-Takagi: the commutant
       right-H action on H^64 is unitarily 64 identical copies of the 1-quaternion block.
  [E2] the 1-quaternion control: right multiplication on H = R^4, complexified, winds +-2
       in pi_3(U) => stable class k = +-1 (matches the Hopf-bundle table value p_1 = -+2).
  [E3] ROUTE R1 (commutant twist): winding of the complexified right-Sp(1) action on the
       frozen module = 64 x control = +-128 => k = +-64; direct coarse quadrature corroborates.
  [E4] ROUTE R2 (fiber-core deck family, spin transport): Lambda(v) = v0 I + sum v^k G_b0 G_bk
       implements the native family F_v = (I-2vv^T)(I-2v0v0^T) on the base legs (Ad check),
       carries the deck / co-flip monodromy Lambda(-v0) = -I, and its winding is computed.
  [E5] ROUTE R0 (metric-side family alone): winding of F_v in SO(4) computed (expect 0).
  [E6] carrier-ledger sweep: every native H-multiplicity 64m (m in {1,7,13,14,91}) gives
       J(64m) in {8,16}: order EXACTLY 3, purely 3-primary. Element-3 numerology rejected.
  [F]  falsifier controls: 8|n and 3-not-|n are load-bearing (n=4 -> order 6; n=24 -> 0);
       R1 lives in the commutant (H-linear family), R2's twist is NOT H-linear (typed).
"""
from __future__ import annotations
import os, sys, time
import numpy as np

_HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.normpath(os.path.join(_HERE, "..", "generation-sector")))
import gen_sector_bridge as bridge  # noqa: E402

FAILURES = []
def check(tag, name, ok, detail=""):
    s = "PASS" if ok else "FAIL"
    print(f"[{tag}] {s}  {name}" + (f"  ({detail})" if detail else ""))
    if not ok: FAILURES.append(name)

t0 = time.time()
e, Gamma, Pi_RS, M_D = bridge.constraint_objects()
G = bridge.cl95.jordan_wigner_gammas(7)          # Euclidean gammas, G_a^2 = +1, Hermitian
a = bridge.anchors()
check("T", "rep anchors reproduce", abs(a["bare_commutator"] - 58.7215) < 1e-3
      and abs(a["C2"] - 155.3625) < 1e-3, f"comm={a['bare_commutator']:.4f}, C2={a['C2']:.4f}")

K_S = e[0].copy()
for i in range(1, 9): K_S = K_S @ e[i]
check("T", "K_S Hermitian, K_S^2 = I",
      np.max(np.abs(K_S - K_S.conj().T)) < 1e-12 and
      np.max(np.abs(K_S @ K_S - np.eye(128))) < 1e-12)

C = e[1] @ e[3] @ e[5] @ e[7] @ e[10] @ e[12]     # J_quat = C . conj (canon, exact)
check("T", "J_quat^2 = -1 (C Cbar = -I)", np.max(np.abs(C @ C.conj() + np.eye(128))) == 0.0)
res = max(float(np.max(np.abs(e[k] @ C - C @ e[k].conj()))) for k in (0, 4, 9, 13))
check("T", "sample e_a exactly J_quat-commuting", res == 0.0)

def order24(x): return next(n for n in range(1, 25) if (n * x) % 24 == 0)
check("T", "3-Sylow of Z/24 = {0,8,16}; order(8)=order(16)=3",
      sorted(x for x in range(24) if (3 * x) % 24 == 0) == [0, 8, 16]
      and order24(8) == 3 and order24(16) == 3)

# ---------------- WZW winding quadrature (1/(24 pi^2) int tr(g^-1 dg)^3) ----------------
def wzw_winding(gfun, ngrid):
    ps = np.linspace(0, np.pi, ngrid + 1); th = np.linspace(0, np.pi, ngrid + 1)
    ph = np.linspace(0, 2 * np.pi, 2 * ngrid + 1)
    total = 0.0; h = 1e-5
    for ip in range(ngrid):
        for it in range(ngrid):
            for jf in range(2 * ngrid):
                x = (0.5*(ps[ip]+ps[ip+1]), 0.5*(th[it]+th[it+1]), 0.5*(ph[jf]+ph[jf+1]))
                gi = np.linalg.inv(gfun(*x)); L = []
                for k in range(3):
                    xp = list(x); xm = list(x); xp[k] += h; xm[k] -= h
                    L.append(gi @ ((gfun(*xp) - gfun(*xm)) / (2 * h)))
                s = np.trace(L[0]@L[1]@L[2] - L[0]@L[2]@L[1] + L[1]@L[2]@L[0]
                             - L[1]@L[0]@L[2] + L[2]@L[0]@L[1] - L[2]@L[1]@L[0]) / 6.0
                total += 6.0*s.real*(ps[ip+1]-ps[ip])*(th[it+1]-th[it])*(ph[jf+1]-ph[jf])
    return total / (24 * np.pi ** 2)

def sphere(psi, theta, phi):
    return np.array([np.cos(psi), np.sin(psi)*np.sin(theta)*np.cos(phi),
                     np.sin(psi)*np.sin(theta)*np.sin(phi), np.sin(psi)*np.cos(theta)])

S1 = np.array([[0,1],[1,0]],complex); S2 = np.array([[0,-1j],[1j,0]],complex)
S3 = np.array([[1,0],[0,-1]],complex)
def su2_id(psi, theta, phi):
    v = sphere(psi, theta, phi)
    return v[0]*np.eye(2) + 1j*(v[1]*S1 + v[2]*S2 + v[3]*S3)
w_ctrl = wzw_winding(su2_id, 12)
check("T", "quadrature control: id map S^3 -> SU(2) winds 1", abs(w_ctrl - 1) < 0.02,
      f"{w_ctrl:+.4f}")

# ---------------- [E1] C antisymmetric => Autonne-Takagi block reduction ----------------
anti = float(np.max(np.abs(C + C.T)))
uni  = float(np.max(np.abs(C @ C.conj().T - np.eye(128))))
check("E", "C is antisymmetric unitary (Autonne-Takagi: J_quat unitarily equivalent to 64 "
           "standard j-blocks; the right-H action = 64 identical 1-quaternion blocks)",
      anti == 0.0 and uni < 1e-12, f"||C+C^T||={anti:.1e}, unitarity {uni:.1e}")

# ---------------- [E2] the 1-quaternion control: right mult on H, complexified ----------
def realop_complexify(A, B):
    """R-linear T z = A z + B conj(z) on C^n -> its complexification on C^2n."""
    n = A.shape[0]
    T = np.zeros((2*n, 2*n), dtype=complex)
    T[:n,:n] = A; T[:n,n:] = B; T[n:,:n] = B.conj(); T[n:,n:] = A.conj()
    return T
EPS1 = np.array([[0,1],[-1,0]],complex)          # the standard j on H = C^2, j = EPS1 . conj
def quat_right(v, Cmat):
    n = Cmat.shape[0]
    return realop_complexify((v[0]+1j*v[1])*np.eye(n,dtype=complex), (v[2]+1j*v[3])*Cmat)
w_h1 = wzw_winding(lambda p,t,f: quat_right(sphere(p,t,f), EPS1), 12)
k_h1 = w_h1 / 2.0                                 # c: pi_3(O) -> pi_3(U) is x2 (Bott)
check("E", "1-quaternion control: complexified winding +-2 => stable class k = +-1 "
           "(Hopf-bundle table: |p_1| = 2|k| = 2)", abs(abs(w_h1) - 2) < 0.05,
      f"W_C = {w_h1:+.4f}, k = {k_h1:+.3f}")

# ---------------- [E3] ROUTE R1: the commutant right-Sp(1) twist on the frozen module ---
# structural value: 64 identical blocks (E1) x control block => W_C = 64 * (+-2), k = +-64
k_R1_struct = int(round(64 * k_h1))
# direct corroboration on the actual 256-dim complexification, coarse grid, ratio-calibrated
w_ctrl_coarse = wzw_winding(lambda p,t,f: quat_right(sphere(p,t,f), EPS1), 6)
w_R1_coarse = wzw_winding(lambda p,t,f: quat_right(sphere(p,t,f), C), 6)
ratio = w_R1_coarse / w_ctrl_coarse
check("E", "R1 direct quadrature: winding(commutant twist) / winding(1-quaternion) = 64",
      abs(ratio - 64) < 0.5, f"ratio {ratio:.3f} (coarse W = {w_R1_coarse:+.2f})")
k_R1 = k_R1_struct
check("E", f"R1 stable class k = {k_R1:+d}; k mod 24 = {k_R1 % 24}; order in Z/24 = "
           f"{order24(k_R1 % 24)}; 2-primary part {k_R1 % 8}, 3-primary residue {k_R1 % 3}",
      abs(k_R1) == 64 and (k_R1 % 24) in (8, 16) and order24(k_R1 % 24) == 3
      and k_R1 % 8 == 0 and k_R1 % 3 != 0,
      "PURE 3-primary, order exactly 3, J(k) in {8 nu, 16 nu}")
# H-linearity: R1 commutes with the whole algebra (it IS the commutant) -- sample check
Rv = quat_right(np.array([0.5, 0.5, 0.5, 0.5]), C)
for kk in (0, 9):
    Ek = realop_complexify(e[kk], np.zeros_like(e[kk]))
    check("F", f"R1 family is H-linear (commutes with e_{kk}): the twist lives in the "
               "commutant, NOT in the killed Hermitian-carrier-index class",
          float(np.max(np.abs(Rv @ Ek - Ek @ Rv))) < 1e-12)

# ---------------- [E4] ROUTE R2: fiber-core deck family, spin transport ------------------
# base legs (3,1): three spacelike from the + group, timelike from e_9..e_13 (habitat pin)
for legs in ((9, 0, 1, 2), (13, 3, 7, 8)):
    b0, b1, b2, b3 = legs
    Q = [G[b0] @ G[bk] for bk in (b1, b2, b3)]
    def lam(p, t, f, Q=Q):
        v = sphere(p, t, f)
        return v[0]*np.eye(128, dtype=complex) + v[1]*Q[0] + v[2]*Q[1] + v[3]*Q[2]
    v_test = sphere(0.7, 1.1, 2.3)
    L = lam(0.7, 1.1, 2.3)
    check("T", f"R2 legs {legs}: Lambda(v) unitary; Lambda(-v0) = -I (deck / co-flip "
               "monodromy, the pi_1 shadow)",
          float(np.max(np.abs(L @ L.conj().T - np.eye(128)))) < 1e-12
          and float(np.max(np.abs(lam(np.pi, 0, 0) + np.eye(128)))) < 1e-12)
    # Ad check: the induced rotation M[i,j] = tr(G_bi Lambda G_bj Lambda^dag)/128 equals
    # F_v = (I-2vv^T)(I-2v0v0^T) up to the lift-orientation convention (Ad_Lambda = F_v^-1;
    # the transport matching F_v is Ad of Lambda^dag) -- measured, not assumed.
    v4 = v_test; v0 = np.array([1.0, 0, 0, 0])
    F4 = (np.eye(4) - 2*np.outer(v4, v4)) @ (np.eye(4) - 2*np.outer(v0, v0))
    Gb = [G[b0], G[b1], G[b2], G[b3]]
    M = np.array([[np.trace(Gb[i] @ L @ Gb[j] @ L.conj().T).real / 128.0
                   for j in range(4)] for i in range(4)])
    d_fwd = float(np.max(np.abs(M - F4))); d_inv = float(np.max(np.abs(M - F4.T)))
    which = "Ad_Lambda = F_v" if d_fwd < d_inv else "Ad_Lambda = F_v^-1 (transport = Lambda^dag)"
    c_off = next(c for c in range(9) if c not in legs)
    off = float(np.max(np.abs(L @ G[c_off] - G[c_off] @ L)))
    check("E", f"R2 legs {legs}: Lambda spin-lifts the native deck family exactly "
               f"({which}); identity off the base legs", min(d_fwd, d_inv) < 1e-9
          and off < 1e-12, f"res {min(d_fwd, d_inv):.1e}, off-base {off:.1e}")
    w_R2 = wzw_winding(lam, 10)
    check("E", f"R2 legs {legs}: winding of the spin-transport family = {round(w_R2)} "
               f"({w_R2:+.4f})", abs(w_R2 - round(w_R2)) < 0.2)
    # the R2 twist is NOT H-linear (its generators anti-commute with J_quat): typed
    nl = float(np.max(np.abs(Q[0] @ C - C @ Q[0].conj())))
    check("F", f"R2 legs {legs}: twist generator NOT H-linear (J-residual {nl:.2f}); "
               "the co-flip/deck datum is the Z/2 shadow, not the Z/24 integer", nl > 1.0)

# ---------------- [E5] ROUTE R0: the metric-side family alone ---------------------------
def f_metric(p, t, f):
    v = sphere(p, t, f); v0 = np.array([1.0, 0, 0, 0])
    return ((np.eye(4) - 2*np.outer(v, v)) @ (np.eye(4) - 2*np.outer(v0, v0))).astype(complex)
w_R0 = wzw_winding(f_metric, 12)
check("E", "R0: the fiber-core family (I-2vv^T)(I-2v0v0^T) in SO(4) is STABLY TRIVIAL "
           f"(winding {w_R0:+.4f} -> k = {round(w_R0/2)})", abs(w_R0) < 0.1)

# ---------------- [E6] carrier-ledger sweep + the Z/3 subtlety ---------------------------
ledger = {"H^64 (irreducible Cl(9,5) module)": 64, "H^448 (7x)": 448, "H^832 (13x)": 832,
          "H^896 (14x, vector-spinor)": 896, "H^5824 (91x, so(9,5)-valued)": 5824}
ok_all = True
for name, n in ledger.items():
    j = n % 24; o = order24(j)
    ok = j in (8, 16) and o == 3 and n % 8 == 0 and n % 3 != 0
    ok_all &= ok
    print(f"      {name}: J({n}) = {j} in Z/24, order {o}, (mod8,mod3)=({n%8},{n%3})")
check("E", "EVERY native quaternionic carrier gives a class in {8,16}: order EXACTLY 3, "
           "purely 3-primary (8 | 64m always; 3 never divides the ledger, C-04)", ok_all)
check("E", "Z/3 subtlety: the ELEMENT 3 of Z/24 is NOT in the 3-Sylow (3 mod 8 = 3 != 0); "
           "'count = 3' cannot mean the element 3; residue reading gives 3 = 0 mod 3 = "
           "trivial class; the only well-typed nontrivial reading is count = ORDER of the "
           "class", 3 % 8 != 0 and order24(3) == 8 and 3 % 3 == 0)
check("F", "falsifier control: purity is NOT free -- n=4 gives order 6 (2-primary "
           "contamination), n=24 gives the ZERO class (3 | n kills it)",
      order24(4) == 6 and 24 % 24 == 0 and order24(0) == 1,
      "8|n and 3-not-|n are the load-bearing facts")

print()
ne = sum(1 for _ in FAILURES)
print(f"TORSION ARENA PROBE: {'ALL PASS' if not FAILURES else str(ne)+' FAILURES: '+str(FAILURES)}"
      f"  ({time.time()-t0:.1f}s)")
print(f"HEADLINE: R1 (commutant twist) k = {k_R1:+d}, J(k) = {k_R1 % 24} nu in Z/24, "
      f"order {order24(k_R1 % 24)}; R0 = 0; R2 windings printed above.")
sys.exit(0 if not FAILURES else 1)
