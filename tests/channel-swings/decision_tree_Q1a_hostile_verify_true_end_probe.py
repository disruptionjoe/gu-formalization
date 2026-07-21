#!/usr/bin/env python3
r"""
HOSTILE-VERIFY probe for the Q1a-FORCED (limit-point) win.

The win's own probe (decision_tree_Q1a_fiber_end_classification_probe.py) PLANTS
bounded coefficients:
    Pfun = 1.0 + 0.2*sin(0.5 s),  Tfun = 1.0 + 0.5*sin(0.7 s + 1),  phip = 0.24*cos(0.3 s)
and then verifies "bounded W~ => LP". That is circular for the load-bearing gaps
A and C: it never uses the actual GL(4,R)/O(3,1) end geometry. This probe puts the
SAME structural questions (is P floored? is C_0=sqrt|q| / V / winding bounded?) to
the ACTUAL faithful Y14 end-model (n2_end_family_probe.py), along noncompact
degeneration rays to LARGE s (the true ends), not on a bounded collar.

Model (verbatim from n2_end_family_probe.py):
  F = Lorentzian forms g on R^4 (signature (3,1)); induced DeWitt (9,5) form on
  V = R^4 + S^2(R^4); closed-form G-orthonormal frame F_s; boundary Dirac symbol
  D(t,s) = c(xi(t,s)), xi = components of ONE fixed covector XI_VEC in the
  transported frame rho(R_t) F_s; degeneration ray a(s) = exp(2 alpha s).
  ETA = [+1]*9 + [-1]*5;  q(xi) = <xi,xi>_{9,5} = P - T with
     P(s) = sum_{a<9} xi_a(s)^2   (spacelike / c_s norm),
     T(s) = sum_{a>=9} xi_a(s)^2  (timelike  / c_t norm),
     ratio rho = P/(P+T),  C_0 = sqrt|q|.

Deterministic, foreground, numpy only, no writes, no network. EXIT 0 = ran.
The exit code is NOT a verdict; the printed findings are.
"""
from __future__ import annotations

import os
import sys

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "generation-sector"))
import gen_sector_bridge as gb  # noqa: E402

N_DIRS, DIM = 14, 128
ETA = np.array([1.0] * 9 + [-1.0] * 5)
LAM = 0.5
SPACE = np.arange(0, 9)   # P legs
TIME = np.arange(9, 14)   # T legs

# ---- verified Clifford objects (only needed for the faithful K_u winding) ----
e = gb.gammas()
K_S = e[0].copy()
for a in range(1, 9):
    K_S = K_S @ e[a]
I128 = np.eye(DIM, dtype=complex)
XI = np.real(np.asarray(gb.XI)).astype(float)


def cvec(v):
    return sum(v[a] * e[a] for a in range(N_DIRS))


# ---- fiber geometry (verbatim structure from n2_end_family_probe.py) ---------
SYM_IDX = [(0, 0), (1, 1), (2, 2), (3, 3),
           (0, 1), (0, 2), (1, 2), (0, 3), (1, 3), (2, 3)]


def sym_mat(i):
    a, b = SYM_IDX[i]
    m = np.zeros((4, 4))
    if a == b:
        m[a, a] = 1.0
    else:
        m[a, b] = m[b, a] = 1.0 / np.sqrt(2.0)
    return m


HMODES = [sym_mat(i) for i in range(10)]


def dewitt_gram(g, lam=LAM):
    gi = np.linalg.inv(g)
    G = np.zeros((14, 14))
    G[:4, :4] = g
    gih = [gi @ h for h in HMODES]
    tr1 = [float(np.trace(m)) for m in gih]
    for i in range(10):
        for j in range(i, 10):
            v = float(np.trace(gih[i] @ gih[j])) - lam * tr1[i] * tr1[j]
            G[4 + i, 4 + j] = G[4 + j, 4 + i] = v
    return G


def fixsign(v):
    k = int(np.argmax(np.abs(v)))
    return v if v[k] > 0 else -v


def frame_diag(a4, lam=LAM):
    a0, a1, a2, a3 = [float(x) for x in a4]
    F = np.zeros((14, 14))
    F[0, 0] = 1.0 / np.sqrt(a0)
    F[1, 1] = 1.0 / np.sqrt(a1)
    F[2, 2] = 1.0 / np.sqrt(a2)
    F[3, 9] = 1.0 / np.sqrt(a3)
    F[8, 3] = np.sqrt(a0 * a1)
    F[9, 4] = np.sqrt(a0 * a2)
    F[10, 5] = np.sqrt(a1 * a2)
    F[11, 10] = np.sqrt(a0 * a3)
    F[12, 11] = np.sqrt(a1 * a3)
    F[13, 12] = np.sqrt(a2 * a3)
    u = np.array([1.0 / a0, 1.0 / a1, 1.0 / a2, -1.0 / a3])
    M = np.diag(u * u) - lam * np.outer(u, u)
    w, V = np.linalg.eigh(M)
    refs = np.array([[1., -1., 0., 0.], [0., 1., -1., 0.],
                     [0., 0., 1., -1.], [1., 1., 1., 1.]]).T
    k0 = 0
    while k0 < 4:
        k1 = k0 + 1
        while k1 < 4 and abs(w[k1] - w[k0]) <= 1e-9 * max(1.0, abs(w[k0])):
            k1 += 1
        if k1 - k0 > 1:
            P = V[:, k0:k1]
            B = []
            for r in refs.T:
                v = P @ (P.T @ r)
                for b in B:
                    v = v - b * float(b @ v)
                nv = float(np.linalg.norm(v))
                if nv > 1e-8:
                    B.append(v / nv)
                if len(B) == k1 - k0:
                    break
            V[:, k0:k1] = np.stack(B, axis=1)
        k0 = k1
    pos = [k for k in range(4) if w[k] > 0]
    neg = [k for k in range(4) if w[k] < 0]
    if len(pos) != 3 or len(neg) != 1:
        raise ValueError(f"diag block signature not (3,1): {w}")
    for j, k in enumerate(pos):
        F[4:8, 6 + j] = fixsign(V[:, k]) / np.sqrt(w[k])
    F[4:8, 13] = fixsign(V[:, neg[0]]) / np.sqrt(-w[neg[0]])
    return F


def rot4(th):
    R = np.eye(4)
    R[0, 0] = R[3, 3] = np.cos(th)
    R[0, 3] = -np.sin(th)
    R[3, 0] = np.sin(th)
    return R


def rho(R):
    P = np.zeros((14, 14))
    P[:4, :4] = R
    for i in range(10):
        RhR = R @ HMODES[i] @ R.T
        for j in range(10):
            P[4 + j, 4 + i] = float(np.sum(RhR * HMODES[j]))
    return P


F_BASE = frame_diag((1.0, 1.0, 1.0, 1.0))
XI_VEC = F_BASE @ XI


def xi_of(t, a4, lam=LAM):
    F = rho(rot4(np.pi * t)) @ frame_diag(a4, lam)
    return np.linalg.solve(F, XI_VEC)


def xi_safe(t, a4, lam=LAM):
    """xi_of guarded: returns None where the closed-form frame degenerates."""
    try:
        return xi_of(t, a4, lam)
    except (ValueError, np.linalg.LinAlgError):
        return None


def ray(alpha, s):
    al = np.asarray(alpha, dtype=float)
    return tuple(np.exp(2.0 * al * s))


def PT(xi):
    P = float(np.sum(xi[SPACE] ** 2))
    T = float(np.sum(xi[TIME] ** 2))
    return P, T


def loglslope(s_arr, y_arr):
    """Fit log|y| ~ b*s ; return exponential slope b (per unit s)."""
    y = np.abs(np.asarray(y_arr, float))
    m = y > 0
    return float(np.polyfit(np.asarray(s_arr, float)[m], np.log(y[m]), 1)[0])


print("=== Q1a HOSTILE VERIFY: true-end P-floor / C_0 / winding on the ACTUAL "
      "GL(4,R)/O(3,1) model ===\n")

# sanity: reproduce the base anchor xi(0,0) = XI
assert np.max(np.abs(xi_of(0.0, (1., 1., 1., 1.)) - XI)) < 1e-10
P0, T0 = PT(XI)
print(f"[base] xi(0,0)=XI reproduced. P0={P0:.3f} T0={T0:.3f} "
      f"q0={P0 - T0:.3f} rho0={P0 / (P0 + T0):.3f}\n")

# -----------------------------------------------------------------------------
# TEST 1 -- the win says "P,T,C_0=sqrt|P-T|,V bounded at the ends". Is the
# PHYSICAL scale bounded on the actual model? Go to LARGE s on named rays.
# -----------------------------------------------------------------------------
print("[TEST 1] physical scale of xi / P / T / C_0 = sqrt|q| along rays to s=30")
print("         (win's probe planted these BOUNDED ~ O(1); model says otherwise)")
s_big = np.linspace(0.0, 25.0, 51)
rays = {
    "conf-up   (1,1,1,1)": np.array([1., 1., 1., 1.]) / 2.0,
    "conf-down(-1,-1,-1,-1)": np.array([-1., -1., -1., -1.]) / 2.0,
    "boost   (1,0,0,1)": np.array([1., 0., 0., 1.]) / np.sqrt(2.0),
    "timelike (0,0,0,1)": np.array([0., 0., 0., 1.]),
}
for name, al in rays.items():
    xis = [(s, xi_safe(0.0, ray(al, s))) for s in s_big]
    xis = [(s, x) for s, x in xis if x is not None]
    ss = np.array([s for s, _ in xis])
    Ps = np.array([PT(x)[0] for _, x in xis])
    Ts = np.array([PT(x)[1] for _, x in xis])
    C0 = np.sqrt(np.abs(Ps - Ts))
    nrm = np.array([np.linalg.norm(x) for _, x in xis])
    b_C0 = loglslope(ss[C0 > 0], C0[C0 > 0])
    b_nrm = loglslope(ss, nrm)
    tail = f"(frame degenerates past s={ss[-1]:.0f})" if ss[-1] < s_big[-1] - 1e-6 else ""
    print(f"  {name:24s}: |xi|({ss[-1]:.0f})={nrm[-1]:.2e} C_0={C0[-1]:.2e} "
          f"slope(C_0)~{b_C0:+.2f}/s slope(|xi|)~{b_nrm:+.2f}/s {tail}")
print("  => C_0=sqrt|q| and |xi| (hence V and W~=K_u V) grow/decay EXPONENTIALLY;")
print("     they are NOT the bounded O(1) coefficients the win's probe planted.\n")

# -----------------------------------------------------------------------------
# TEST 2 -- the win says min P/(P+T)=0.36 "over 200 rays incl boundary-at-inf",
# read as a UNIVERSAL floor at the true ends. Is rho floored to s->inf on ALL
# rays, or only on the surviving (conf-up) sector? Collar (s=3,4) vs true end.
# -----------------------------------------------------------------------------
print("[TEST 2] rho = P/(P+T) at the COLLAR (s=3,4) vs the TRUE END (s=25) per ray")
f = lambda pt: pt[0] / (pt[0] + pt[1])
for name, al in rays.items():
    def rr(s):
        x = xi_safe(0.0, ray(al, s))
        return None if x is None else PT(x)
    r3, r4, rE = rr(3.0), rr(4.0), rr(25.0)
    if rE is None:
        # step back to the largest s the frame survives
        sE = 25.0
        while sE > 4.0 and rr(sE) is None:
            sE -= 1.0
        rE = rr(sE)
        endlbl = f"rho({sE:.0f})"
    else:
        sE, endlbl = 25.0, "rho(25)"
    q30 = rE[0] - rE[1]
    sector = "gapped q>0" if q30 > 0 else "CROSSED q<0"
    print(f"  {name:24s}: rho(3)={f(r3):.3f} rho(4)={f(r4):.3f} "
          f"{endlbl}={f(rE):.3f}  [{sector}]")
print()

# genericity sweep: does the 0.36 floor survive to the true end over random rays?
rng = np.random.default_rng(20260721)
below, crossed_at_end, n, ok = 0, 0, 4000, 0
min_rho_end = 1.0
worst = None
for _ in range(n):
    al = rng.standard_normal(4)
    al = al / np.linalg.norm(al)
    x30 = xi_safe(0.0, ray(al, 25.0))
    if x30 is None:
        continue
    ok += 1
    P, T = PT(x30)
    r = P / (P + T)
    if r < min_rho_end:
        min_rho_end, worst = r, al.copy()
    if r < 0.36:
        below += 1
    if P - T < 0:
        crossed_at_end += 1
n = ok
print(f"[TEST 2b] {n} random unit rays (frame-survivors), rho at the TRUE END s=25:")
print(f"  rays with rho(25) < 0.36 (below the win's 'floor'): {below}/{n} "
      f"({100 * below / n:.0f}%)")
print(f"  rays landing in the CROSSED sector q<0 at s=25: {crossed_at_end}/{n} "
      f"({100 * crossed_at_end / n:.0f}%)")
print(f"  minimum rho(25) observed: {min_rho_end:.4f} at "
      f"alpha~[{', '.join('%+.2f' % a for a in worst)}]")
print("  => the 0.36 figure is the P>0 existence-domain floor on the SAMPLED")
print("     (surviving) sector at finite collar s; it is NOT a universal floor")
print("     at the true ends. A large fraction of rays leave it / cross q=0.\n")

# -----------------------------------------------------------------------------
# TEST 3 -- can rho -> 0 (space part negligible) at the true end?  P>0 keeps
# B non-degenerate (win step i, scale-free), but rho->0 means the symbol is
# timelike-DOMINATED: q<0, the crossed/timelike sector, where the model's own
# K-null theorem says NO K-definite cut exists -> the operator apparatus feeding
# A~ EXITS its existence domain. LP verdict is undefined there.
# -----------------------------------------------------------------------------
print("[TEST 3] LP control vs breakdown control at the true end:")
for label, al in [("LP control  conf-up", rays["conf-up   (1,1,1,1)"]),
                  ("breakdown   timelike", rays["timelike (0,0,0,1)"])]:
    sE = 25.0
    x = xi_safe(0.0, ray(al, sE))
    while x is None and sE > 4.0:
        sE -= 1.0
        x = xi_safe(0.0, ray(al, sE))
    P, T = PT(x)
    r = P / (P + T)
    q = P - T
    print(f"  {label}: rho({sE:.0f})={r:.4f} q({sE:.0f})={q:+.3e} "
          f"P_space={P:.3e} -> {'q>0 gapped (LP-consistent)' if q > 0 else 'q<0 crossed (K-null; cut DNE)'}")
print()

# -----------------------------------------------------------------------------
# TEST 4 -- faithful K_u = K_S c_s / sqrt(P) winding rate ||dK_u/ds|| along a
# ray, using the full 128-dim rep. Win step iii needs phi' bounded at the end.
# -----------------------------------------------------------------------------
print("[TEST 4] faithful winding rate ||dK_u/ds|| (K_u=K_S c_s/sqrt P) at s=25")


def Ku_of(t, a4):
    x = xi_safe(t, a4)
    if x is None:
        return None
    D = cvec(x)
    c_s = 0.5 * (D + K_S @ D @ K_S)
    P = float(np.real(np.trace(c_s @ c_s))) / 128.0
    if P <= 0:
        return None
    return K_S @ c_s / np.sqrt(P)


for name, al in [("conf-up", rays["conf-up   (1,1,1,1)"]),
                 ("timelike", rays["timelike (0,0,0,1)"]),
                 ("boost", rays["boost   (1,0,0,1)"])]:
    ds = 1e-3
    K1, K2 = Ku_of(0.0, ray(al, 25.0)), Ku_of(0.0, ray(al, 25.0 + ds))
    if K1 is None or K2 is None:
        print(f"  {name:9s}: P=0 (pure-timelike stratum) -- K_u undefined")
        continue
    wind = float(np.linalg.norm(K2 - K1)) / ds
    inv = float(np.max(np.abs(K1 @ K1 - I128)))
    print(f"  {name:9s}: ||dK_u/ds||~{wind:.3e}  (K_u^2=I residual {inv:.1e})")
print("  => on single-exponent-dominant rays the winding DECAYS (K_u aligns): phi'")
print("     bounded there is fair to the win. But this is the NORMALIZED-direction")
print("     winding; it does NOT rescue the physical-scale blow-up of TEST 1, and")
print("     it says nothing on the crossed/undecided rays (TEST 2b) where c_s's")
print("     direction is not asymptotically single-exponent.\n")

# -----------------------------------------------------------------------------
# TEST 5 -- the normalization gauge is NON-UNITARY (changes the L^2 measure).
# lambda(s) ~ alpha_max * s (linear), so lambda' -> const; normalizing removes
# the blow-up but multiplies the section by e^{-lambda}, |e^{-lambda}| != 1.
# Whether coefficients are "bounded" therefore depends on the (unfixed) native
# measure -- exactly the hourly's missing reopen-packet item.
# -----------------------------------------------------------------------------
print("[TEST 5] normalization is a non-unitary similarity (measure-changing)")
al = rays["conf-up   (1,1,1,1)"]
lam_s = np.array([np.log(np.linalg.norm(xi_of(0.0, ray(al, s)))) for s in s_big])
lamp = np.gradient(lam_s, s_big)
_ = lamp
print(f"  d/ds log|xi| on conf-up: {lamp[10]:.3f} -> {lamp[-1]:.3f} "
      f"(-> constant {lamp[-1]:.3f}); e^lambda grows unboundedly, so xi/|xi| is a")
print("  NON-UNITARY rescaling. Bounded-coeff LP only follows in the NORMALIZED")
print("  measure; in the physical (fiber-volume) measure C_0,V blow up. Which")
print("  measure is native is NOT fixed by committed structure (Gap D / hourly")
print("  reopen item 2). Note also: F=GL(4,R)/O(3,1) has NON-COMPACT isotropy")
print("  O(3,1) => no invariant RIEMANNIAN metric exists, only pseudo-Riemannian;")
print("  the Chernoff 'complete Riemannian => LP' default is thus ill-typed here.\n")

print("=== SUMMARY (findings, not a pass/fail verdict) ===")
print(" 1. C_0=sqrt|q|, |xi|, V grow/decay EXPONENTIALLY on generic rays; the")
print("    win's 'bounded W~' rests on planted O(1) toys (its step iii premise).")
print(" 2. rho=P/(P+T) is NOT floored to the true end on all rays; 0.36 is the")
print("    surviving-sector existence floor at finite collar s.")
print(" 3. Timelike-dominant rays reach q<0 (K-null sector, no cut) at the end;")
print("    B stays non-degenerate (P>0, win step i robust) but the cut/section")
print("    apparatus that defines A~ exits its existence domain.")
print(" 4. Winding decays on single-exponent rays (fair to win) but that is the")
print("    normalized direction only.")
print(" 5. Removing the blow-up needs a non-unitary rescaling => the LP/LC answer")
print("    depends on the unfixed native measure; pseudo-Riemannian isotropy voids")
print("    the completeness default. FORCED does not close from committed structure.")
print("EXIT 0")
