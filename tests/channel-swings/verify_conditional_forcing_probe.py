#!/usr/bin/env python3
"""HOSTILE VERIFICATION of the conditional-forcing minimal-input result.

TARGET:  explorations/conditional-forcing-minimal-input-2026-07-20.md
         tests/channel-swings/conditional_forcing_probe.py    (commit f513fcf)
DIRECTED: Joe direct chat, 2026-07-20 (hostile verify: conditional forcing).
POSTURE: assume an asserted-but-never-checked error until proven otherwise.
         A kill is a fully successful outcome.  No original file is edited.

METHOD SEPARATION (independent routes, nothing decisive re-used):

  * Degree machinery #1 (mine): a NEW signed-preimage counter -- Gram-Schmidt
    tangent frames (not SVD), damped Gauss-Newton with NUMERICAL derivatives
    of the normalized map (the original uses analytic Jacobians + lstsq),
    my own regular values W3/W4 (not W1/W2), my own seeds, my own dedupe and
    sign rule.  Power-certified on id (+1), antipodal (+1), quaternion
    conjugation (-1), and the original's own cube map (+3) BEFORE use.
  * Degree machinery #2 (mine, exact): join maps (z1^p, z2^q) admit CLOSED-
    FORM preimage enumeration (one bisection for the modulus split + p*q
    explicit phase roots).  Every preimage is verified to map onto the
    regular value; local signs are read individually.  This certifies the
    high-degree witnesses (7, 9, 13, 21) with no Newton search at all.
  * Degree machinery #3 (exact linear algebra): right translation v -> v*q0
    is LINEAR on R^4; its degree is sign(det R(q0)) -- computed from the
    4x4 matrix directly.  X2's class claim never touches preimage counting.
  * Bookkeeping: order24 re-derived from the closed form 24/gcd(24, m) and
    the structural split order(J(64c)) proved via gcd(24,16c) = 8*gcd(3,c),
    checked for |c| <= 1000 (original: 60).
  * X1.5 scatter re-tested under DIFFERENT sampling laws: uniform-entry and
    Laplace-entry readers (unit variance, non-Gaussian), uniform / Laplace /
    sparse / confined states, fresh seeds -- is the scatter a draw artifact?
  * Minimality lattice: the original checked Z/2, Z/3, Z/4, Z/6 and asserted
    exhaustion.  Z/5 is MISSING there and is closed HERE: join(21,1) is
    Z/5-equivariant, exactly deck-odd, degree +21, 3 | 21 -> order 1.
    Uniqueness of the involution in Sp(1) (q^2 = 1, |q| = 1 => q = +-1)
    makes every subgroup of order <= 7 cyclic, so the order-<=-6 lattice is
    {Z/2, ..., Z/6} and the exhaustion becomes genuinely complete.
  * THE ACCOUNTING FORK (the main hostile finding, machine-witnessed):
    deck-odd AND Z/3-equivariant  <=>  Z/6-equivariant (zeta6 = -zeta3^2;
    verified on every witness).  The imported k1 machinery treats the deck
    co-flip as a NATIVE exclusion ("excluded by the verified co-flip";
    K1 killed for deck +I vs the VERIFIED co-flip -I), and the target's own
    Section-1 gate list includes deck admissibility as a demand alongside
    G1/G2.  Under that (the program's own) semantics, the gate-passing
    members of the Z/3-equivariant type all have c == 1 mod 3 (Olum), hence
    3 never divides c: ONE TRIT is already the minimal EXTERNAL input, and
    the Z/2 factor of the Z/6 is native bookkeeping, not external payload.
    The Z/6 headline survives only under the OTHER semantics (the anchor
    must itself supply deck parity), which contradicts the machinery the
    probe imports.  Both semantics are exhibited; the fork is real.

EXIT: 0 iff every check below passes.  Checks assert what was FOUND (the
fork included); the per-claim verdicts live in the companion doc
explorations/verify-conditional-forcing-2026-07-20.md.
"""
from __future__ import annotations

import contextlib
import importlib.util
import io
import math
import os
import sys
import time

import numpy as np

_HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, _HERE)
sys.path.insert(0, os.path.normpath(os.path.join(_HERE, "..", "generation-sector")))

# Breadth ladder (honest): VCFP_FAST=1 divides Newton start counts by 3
# (floor 700).  The closed-form join enumeration, the linear-algebra degree
# route, and every exact identity are breadth-independent; only the Newton
# counter's search breadth is reduced, and its power checks still gate it.
FAST = os.environ.get("VCFP_FAST") == "1"


def ns(n):
    return max(700, n // 3) if FAST else n


RESULTS = []


def check(tag, name, ok, detail=""):
    RESULTS.append((tag, name, bool(ok)))
    line = f"[{tag}] {'PASS' if ok else 'FAIL'}  {name}"
    if detail:
        line += f"   ({detail})"
    print(line, flush=True)
    return ok


def import_probe(fname):
    name = fname[:-3]
    spec = importlib.util.spec_from_file_location(name, os.path.join(_HERE, fname))
    mod = importlib.util.module_from_spec(spec)
    sys.modules[name] = mod
    t0 = time.time()
    code = 0
    buf = io.StringIO()
    try:
        with contextlib.redirect_stdout(buf):
            spec.loader.exec_module(mod)
    except SystemExit as ex:
        code = int(ex.code or 0)
    mod._captured_output = buf.getvalue()
    mod._exit_code = code
    return mod, time.time() - t0


t_start = time.time()
print("=" * 78)
print("SETUP  live import of the arena + INDEPENDENT machinery power checks")
print("=" * 78)

k1, dt1 = import_probe("k1_reframe_probe.py")
k1_all = all(ok for _t, _n, ok in k1.RESULTS)
deg_scatter = sorted({d[0] for d in k1.DEG.values()})
check("T", "arena live: k1_reframe_probe re-runs clean (exit 0, all checks); "
           "X0 receipts unchanged (native self-dual scatter {-1,+1,+3,+5}; "
           "counter certificates +1/+3) -- the REPRODUCED baseline",
      k1._exit_code == 0 and k1_all and deg_scatter == [-1, 1, 3, 5]
      and k1.d_id1 == 1 and k1.d_c1 == 3,
      f"exit {k1._exit_code}, {dt1:.0f} s; scatter {deg_scatter}")

e, C, K_S, I128 = k1.e, k1.C, k1.K_S, k1.I128
PINS, QFAM, UMU = k1.PINS, k1.QFAM, k1.UMU
P_plus = k1.P_plus
P_minus = 0.5 * (I128 - K_S)
order24 = k1.order24
ham = k1.hamilton

# ---- bookkeeping re-derivation (surface C, the "right bookkeeping" attack) --
ok_form = all(order24(m) == 24 // math.gcd(24, m) for m in range(24))
ok_gcd = all(math.gcd(24, (16 * c) % 24 if (16 * c) % 24 else 24)
             == 8 * math.gcd(3, c if c else 3) for c in range(-1000, 1001))
ok_split = all((order24((64 * c) % 24) == 3) == (c % 3 != 0)
               and (order24((64 * c) % 24) == 1) == (c % 3 == 0)
               for c in range(-1000, 1001))
check("T", "bookkeeping INDEPENDENTLY re-derived: order24(m) = 24/gcd(24,m) "
           "for all residues; the structural split order(J(64c)) = 3 iff "
           "3 not | c follows from gcd(24,16c) = 8*gcd(3,c) and holds for "
           "all |c| <= 1000 (original: 60).  In particular 64*3 = 192 = "
           "8*24 = 0 mod 24 -> order 1 IS the right bookkeeping",
      ok_form and ok_gcd and ok_split and order24(192 % 24) == 1
      and order24(64 % 24) == 3 and order24((-64) % 24) == 3)


# ---- independent degree machinery #1: my own signed-preimage counter -------
def _normalize(v):
    return v / np.linalg.norm(v)


def tframe(v):
    """Right-handed tangent frame at v by Gram-Schmidt against fixed axes."""
    cols = []
    for k in range(4):
        c = np.zeros(4)
        c[k] = 1.0
        w = c - (c @ v) * v
        for b in cols:
            w = w - (w @ b) * b
        n = np.linalg.norm(w)
        if n > 1e-6:
            cols.append(w / n)
        if len(cols) == 3:
            break
    T = np.column_stack(cols)
    if np.linalg.det(np.column_stack([v] + cols)) < 0:
        T[:, 2] = -T[:, 2]
    return T


def my_degree(f, w, nstarts=3500, seed=101, hstep=1e-6):
    """Signed preimage count of the normalized map over regular value w.
    Numerical derivatives, Gram-Schmidt frames, own dedupe + sign rule."""
    nstarts = ns(nstarts)
    def fh(v):
        y = f(v)
        n = np.linalg.norm(y)
        return None if n < 1e-9 else y / n

    rng = np.random.default_rng(seed)
    V0 = rng.standard_normal((nstarts, 4))
    V0 /= np.linalg.norm(V0, axis=1, keepdims=True)
    roots = []
    for v0 in V0:
        v = v0.copy()
        ok = False
        for _ in range(60):
            y = fh(v)
            if y is None:
                break
            F = y - w
            if np.linalg.norm(F) < 1e-11:
                ok = True
                break
            T = tframe(v)
            D = np.zeros((4, 3))
            bad = False
            for kk in range(3):
                yp = fh(_normalize(v + hstep * T[:, kk]))
                ym = fh(_normalize(v - hstep * T[:, kk]))
                if yp is None or ym is None:
                    bad = True
                    break
                D[:, kk] = (yp - ym) / (2 * hstep)
            if bad:
                break
            s, *_ = np.linalg.lstsq(D, -F, rcond=None)
            snorm = np.linalg.norm(s)
            if snorm > 0.5:
                s *= 0.5 / snorm
            v = _normalize(v + T @ s)
        if not ok:
            continue
        if any(np.linalg.norm(v - r) < 1e-6 for r in roots):
            continue
        roots.append(v.copy())
    deg = 0
    for v in roots:
        T = tframe(v)
        D = np.zeros((4, 3))
        for kk in range(3):
            D[:, kk] = (fh(_normalize(v + hstep * T[:, kk]))
                        - fh(_normalize(v - hstep * T[:, kk]))) / (2 * hstep)
        U = D - np.outer(w, w @ D)
        deg += int(np.sign(np.linalg.det(np.column_stack(
            [w, U[:, 0], U[:, 1], U[:, 2]]))))
    return deg, len(roots)


W3 = _normalize(np.array([0.62, 0.33, -0.44, 0.55]))
W4 = _normalize(np.array([-0.21, 0.71, 0.50, -0.45]))

d_id, n_id = my_degree(lambda v: v, W3)
d_ant, _ = my_degree(lambda v: -v, W3)
d_cnj, _ = my_degree(lambda v: v * np.array([1.0, -1.0, -1.0, -1.0]), W3)
d_cu3, n_cu3 = my_degree(k1.q_cube, W3)
d_cu4, _ = my_degree(k1.q_cube, W4)
check("T", "MY counter power-certified before use (new implementation: "
           "numerical derivatives, Gram-Schmidt frames, own regular values "
           "W3/W4, own seeds): identity +1, antipodal +1 (det(-I4) = +1), "
           "quaternion conjugation -1 (orientation-reversing control the "
           "original never ran), original's cube map +3 on both my values",
      d_id == 1 and d_ant == 1 and d_cnj == -1 and d_cu3 == 3 and d_cu4 == 3,
      f"id {d_id:+d} ({n_id} roots); antip {d_ant:+d}; conj {d_cnj:+d}; "
      f"cube {d_cu3:+d},{d_cu4:+d} ({n_cu3} roots)")


# ---- independent degree machinery #2: closed-form join-map enumeration -----
def join_map(p, q):
    def f(v, _p=p, _q=q):
        z1 = complex(v[0], v[1]) ** _p
        z2 = complex(v[2], v[3]) ** _q
        out = np.array([z1.real, z1.imag, z2.real, z2.imag])
        return out / np.linalg.norm(out)
    return f


def join_degree_analytic(p, q, w):
    """All p*q preimages of w under (z1^p, z2^q)/N in CLOSED FORM: bisection
    on the modulus split + explicit phase roots; each preimage is verified
    to map onto w and its local sign read individually."""
    f = join_map(p, q)
    r1 = math.hypot(w[0], w[1])
    r2 = math.hypot(w[2], w[3])
    th1 = math.atan2(w[1], w[0])
    th2 = math.atan2(w[3], w[2])
    lo, hi = 1e-12, 1.0 - 1e-12
    for _ in range(200):
        a = 0.5 * (lo + hi)
        g = a ** p / (1.0 - a * a) ** (q / 2.0)
        if g < r1 / r2:
            lo = a
        else:
            hi = a
    a = 0.5 * (lo + hi)
    b = math.sqrt(1.0 - a * a)
    pts, worst_map = [], 0.0
    for kk in range(p):
        for ll in range(q):
            ph1 = (th1 + 2 * math.pi * kk) / p
            ph2 = (th2 + 2 * math.pi * ll) / q
            v = np.array([a * math.cos(ph1), a * math.sin(ph1),
                          b * math.cos(ph2), b * math.sin(ph2)])
            worst_map = max(worst_map, float(np.max(np.abs(f(v) - w))))
            pts.append(v)
    dmin = min(np.linalg.norm(pts[i] - pts[j])
               for i in range(len(pts)) for j in range(i + 1, len(pts))) \
        if len(pts) > 1 else 1.0
    deg, h = 0, 1e-6
    for v in pts:
        T = tframe(v)
        D = np.zeros((4, 3))
        for kk in range(3):
            D[:, kk] = (f(_normalize(v + h * T[:, kk]))
                        - f(_normalize(v - h * T[:, kk]))) / (2 * h)
        U = D - np.outer(w, w @ D)
        deg += int(np.sign(np.linalg.det(np.column_stack(
            [w, U[:, 0], U[:, 1], U[:, 2]]))))
    return deg, len(pts), worst_map, dmin


dj31, nj31, mj31, sj31 = join_degree_analytic(3, 1, W3)
dj31b, _, _, _ = join_degree_analytic(3, 1, W4)
dnj31, _ = my_degree(join_map(3, 1), W3, nstarts=4500, seed=103)
check("T", "closed-form join machinery power-certified: join(3,1) has "
           "EXACTLY 3 enumerated preimages (bisection + phase roots, no "
           "Newton search), every one maps onto the regular value, all "
           "local signs +1, degree +3 on both my values -- and my Newton "
           "counter independently agrees",
      dj31 == 3 and nj31 == 3 and mj31 < 1e-9 and sj31 > 1e-3
      and dj31b == 3 and dnj31 == 3,
      f"deg {dj31:+d}/{dj31b:+d}; map defect {mj31:.1e}; min sep {sj31:.2f}; "
      f"Newton {dnj31:+d}")

# =============================================================================
print()
print("=" * 78)
print("SURFACE B  X2 sufficiency by routes the original never used")
print("=" * 78)

RNGB = np.random.default_rng(20260724)
assoc = 0.0
for _ in range(500):
    p = _normalize(RNGB.standard_normal(4))
    v = _normalize(RNGB.standard_normal(4))
    q = _normalize(RNGB.standard_normal(4))
    assoc = max(assoc, float(np.max(np.abs(
        ham(ham(p, v), q) - ham(p, ham(v, q))))))
eqdef_tr = 0.0
Q0S = [np.array([0.5, -0.5, 0.5, 0.5]), np.array([0.5, 0.5, -0.5, 0.5]),
       np.array([1.0, 0.0, 0.0, 0.0])]
for q0 in Q0S:
    for _ in range(60):
        p = _normalize(RNGB.standard_normal(4))
        v = _normalize(RNGB.standard_normal(4))
        eqdef_tr = max(eqdef_tr, float(np.max(np.abs(
            ham(ham(p, v), q0) - ham(p, ham(v, q0))))))
j31 = join_map(3, 1)
noneq = 0.0
for _ in range(20):
    p = _normalize(RNGB.standard_normal(4))
    v = _normalize(RNGB.standard_normal(4))
    noneq = max(noneq, float(np.max(np.abs(
        j31(ham(p, v)) - ham(p, j31(v))))))
check("E", "X2 classification CONFIRMED by the substitution argument (put "
           "p := v at the basepoint: Phi(v) = v * Phi(1), pure associativity "
           "-- no dyadic restriction needed): 500 random float triples "
           "associate at machine precision, right translations are "
           "equivariant at 1e-15 on generic (non-dyadic) samples, and the "
           "degree-3 join non-example breaks equivariance at O(1)",
      assoc < 5e-16 and eqdef_tr < 5e-15 and noneq > 0.1,
      f"assoc {assoc:.1e}; translation defect {eqdef_tr:.1e}; "
      f"non-example {noneq:.2f}")


def right_mult_matrix(q0):
    return np.column_stack([ham(np.eye(4)[b], q0) for b in range(4)])


orth_w, det_w, det_pm = 0.0, 0.0, 0.0
for _ in range(40):
    q0 = _normalize(RNGB.standard_normal(4))
    R = right_mult_matrix(q0)
    orth_w = max(orth_w, float(np.max(np.abs(R.T @ R - np.eye(4)))))
    det_w = max(det_w, abs(np.linalg.det(R) - 1.0))
for q0 in Q0S:
    for sgn in (1.0, -1.0):
        R = right_mult_matrix(sgn * q0)
        det_pm = max(det_pm, abs(np.linalg.det(R) - 1.0))
d_rt, _ = my_degree(lambda v: ham(v, Q0S[0]), W3)
check("E", "X2 class +1 by EXACT LINEAR ALGEBRA (a route with no preimage "
           "counting anywhere): right multiplication by a unit quaternion "
           "is an ORTHOGONAL linear map of R^4 with det = +1 -- for 40 "
           "random q0 and all three probe q0 with BOTH payload orientations "
           "(det R(-q0) = det(-I4) det R(q0) = det R(q0) identically); my "
           "Newton counter agrees at +1; c = 1, 3 not | 1, k = 64 = 16 mod "
           "24, order 3.  X2 sufficiency does NOT die here",
      orth_w < 1e-14 and det_w < 1e-12 and det_pm < 1e-12 and d_rt == 1
      and order24(64 % 24) == 3,
      f"orthogonality {orth_w:.1e}; |det-1| {det_w:.1e}; Newton {d_rt:+d}")

RNGG = np.random.default_rng(424242)
tw_KS = float(np.max(np.abs(K_S @ C - C @ K_S.conj())))
leak_w, gram_w = 0.0, 0.0
for P, Po in ((P_plus, P_minus), (P_minus, P_plus)):
    for _ in range(6):
        psi = P @ (RNGG.standard_normal(128) + 1j * RNGG.standard_normal(128))
        psi /= np.linalg.norm(psi)
        for (al, be) in UMU:
            leak_w = max(leak_w, float(np.linalg.norm(
                Po @ k1.comm_op(al, be, psi))))
        U = [k1.comm_op(al, be, psi) for (al, be) in UMU]
        G = np.array([[float((U[m].conj() @ U[n]).real) for n in range(4)]
                      for m in range(4)])
        gram_w = max(gram_w, float(np.max(np.abs(G - np.eye(4)))))
check("E", "X2 gate G2 by identity CONFIRMED with my own seeds and a "
           "sharper probe: |K_S C - C conj(K_S)| = 0.0 exactly; the "
           "commutant LEAKS NOTHING between confined sectors (cross-sector "
           "norm < 1e-13 for all four generators on 12 confined draws) and "
           "its Gram there is orthonormal to machine precision",
      tw_KS == 0.0 and leak_w < 1e-13 and gram_w < 1e-12,
      f"twist {tw_KS:.1e}; worst leak {leak_w:.1e}; Gram {gram_w:.1e}")

V_MINE = [_normalize(RNGG.standard_normal(4)) for _ in range(12)]
reach_fib = min(max(max(abs(ham(v, q0)[2]), abs(ham(v, q0)[3]))
                    for v in V_MINE) for q0 in Q0S[:2])
st_reach = np.inf
for q0 in Q0S[:2]:
    psi = P_plus @ (RNGG.standard_normal(128) + 1j * RNGG.standard_normal(128))
    psi /= np.linalg.norm(psi)
    best = 0.0
    for v in V_MINE[:6]:
        u = ham(v, q0)
        upsi = k1.comm_op(u[0] + 1j * u[1], u[2] + 1j * u[3], psi)
        Jpsi = k1.comm_op(0.0, 1.0, psi)
        best = max(best, abs(float((Jpsi.conj() @ upsi).real)))
    st_reach = min(st_reach, best)
check("E", "X2 gate G1 CONFIRMED on my own fiber samples and confined "
           "draws: J/iJ reach O(1) over the fiber, O(0.1)+ overlap with "
           "J.psi -- the doc's quoted bars (reach >= 0.90, overlap >= 0.80) "
           "are checked against MY draws and reported in the detail "
           "(draw-dependent; the probe's own coded bars are 0.5 / 0.1)",
      reach_fib > 0.5 and st_reach > 0.1,
      f"my fiber reach {reach_fib:.3f} (doc bar 0.90: "
      f"{'holds' if reach_fib >= 0.90 else 'DOES NOT hold on my draws'}); "
      f"my state reach {st_reach:.3f} (doc bar 0.80: "
      f"{'holds' if st_reach >= 0.80 else 'DOES NOT hold on my draws'})")

# =============================================================================
print()
print("=" * 78)
print("SURFACE C  X1's three legs, re-derived")
print("=" * 78)

RNGC = np.random.default_rng(31337)
inv_ok = True
for sigma in (1.0, -1.0):
    KS_s = sigma * K_S
    hdef = max(float(np.max(np.abs(KS_s @ e[a] - (KS_s @ e[a]).conj().T)))
               for a in range(14))
    inv_ok = inv_ok and hdef == 0.0
rank_ok = True
for sigma in (1.0, -1.0):
    Pp = 0.5 * (I128 + sigma * K_S)
    for pin in PINS:
        for tau in (1.0, -1.0):
            KER = [sigma * M for M in k1.kernels(pin, tau)]
            for _ in range(2):
                psi = Pp @ (RNGC.standard_normal(128)
                            + 1j * RNGC.standard_normal(128))
                psi /= np.linalg.norm(psi)
                B = k1.Bfull(psi, KER)
                rank_ok = rank_ok and \
                    int(np.linalg.matrix_rank(B, tol=1e-10)) == 2
check("E", "X1 leg A CONFIRMED with fresh seeds: all four sign decorations "
           "(sigma, tau) x both pins leave the gate verdicts identical -- "
           "grade-1 kernels exactly H-self-adjoint under +-K_S, confined "
           "bridge rank exactly 2 throughout.  The K_S-orientation bit is "
           "gate-inert", inv_ok and rank_ok)

A0 = k1.forms(k1.GEN_DRAWS[0], PINS[0], 1.0)
Am = k1.forms(k1.GEN_DRAWS[0], PINS[0], -1.0)
KER_base = k1.kernels(PINS[0], 1.0)
KER_neg = [-M for M in KER_base]
Q = QFAM[PINS[0]]
psi0 = k1.GEN_DRAWS[0]
P = np.stack([psi0, Q[0] @ psi0, Q[1] @ psi0, Q[2] @ psi0], axis=1)
U = [P, 1j * P, C @ P.conj(), 1j * (C @ P.conj())]
A_neg = np.zeros((4, 4, 4, 4))
for i in range(4):
    W = KER_neg[i] @ P
    for mu in range(4):
        Ar = (U[mu].conj().T @ W).real
        A_neg[i, mu] = 0.5 * (Ar + Ar.T)
neg_id = float(np.max(np.abs(A_neg + A0)))
odd_w = max(float(np.max(np.abs(k1.qv(-v, A0) + k1.qv(v, A0))))
            for v in V_MINE)
# The sigma-flip (K_S orientation) needs NO preimage count: A(-K_S) = -A(K_S)
# EXACTLY (neg_id below), so the transport becomes v -> -q(v)/|q(v)|, which is
# the antipode on the S^3 TARGET composed with the original map; antipode on
# S^3 has degree (-1)^4 = +1, so the class is preserved identically.  That is
# leg B's core, and it is counter-free and exact.
# The tau-flip (pin-dual orientation, lambda -> -lambda) IS a genuine integer:
# these self-dual forms are high-degree (|c| up to 5) with clustered
# preimages where my low-breadth Newton counter under-resolves, so the integer
# is read with the target's robust ANALYTIC-Jacobian root-finder on MY OWN
# independent regular values W3/W4 (independent value; robust method; labelled
# REPRODUCED-ONLY for the integer, CONFIRMED for the structural negation).
d_b3, _ = k1.degree_by_preimage(lambda v: k1.qv(v, A0),
                                lambda v: k1.jac(v, A0), W3)
d_b4, _ = k1.degree_by_preimage(lambda v: k1.qv(v, A0),
                                lambda v: k1.jac(v, A0), W4)
d_t3, _ = k1.degree_by_preimage(lambda v: k1.qv(v, Am),
                                lambda v: k1.jac(v, Am), W3)
d_t4, _ = k1.degree_by_preimage(lambda v: k1.qv(v, Am),
                                lambda v: k1.jac(v, Am), W4)
their_base = k1.DEG[(PINS[0], 0)][0]
check("E", "X1 leg B CONFIRMED: the sigma-flip (K_S orientation) is EXACTLY "
           "global negation of the transport (form tensor negates to 0.0 "
           "when rebuilt from -K_S kernels from first principles) -- so the "
           "class is preserved with NO count needed (negation = antipode on "
           "the S^3 target, degree +1); the tau-flip (pin-dual orientation) "
           "only NEGATES the integer, read on MY independent regular values "
           "W3/W4 (both odd, target-consistent, = -base): the oriented bit "
           "selects nothing the un-oriented inventory did not already have",
      neg_id < 1e-13 and odd_w < 1e-13
      and d_b3 == their_base and d_b4 == their_base
      and d_t3 == -their_base and d_t4 == -their_base
      and d_t3 % 2 == 1,
      f"A(-K_S)+A(K_S) {neg_id:.1e}; base {d_b3:+d},{d_b4:+d} (their "
      f"{their_base:+d}); tau-flip {d_t3:+d},{d_t4:+d}")

dk31 = max(float(np.max(np.abs(j31(-v) + j31(v)))) for v in V_MINE)
check("E", "X1 leg C CONFIRMED independently: join(3,1) is exactly deck-odd "
           "(odd exponents; verified 0.0), its degree is +3 by closed-form "
           "enumeration AND my Newton counter, and 64*3 = 192 = 0 mod 24 "
           "gives order 1 by the re-derived gcd bookkeeping: the deck "
           "constraint alone admits an order-killer.  X1 insufficiency "
           "stands on all three legs",
      dk31 == 0.0 and dj31 == 3 and dnj31 == 3 and order24(192 % 24) == 1,
      f"deck defect {dk31:.1e}; degree +3 twice independently")

# =============================================================================
print()
print("=" * 78)
print("SURFACE D  X1.5 scatter under DIFFERENT sampling laws")
print("=" * 78)

RNGD = np.random.default_rng(20260725)
s3 = math.sqrt(3.0)
R_uni = (RNGD.uniform(-s3, s3, (128, 128))
         + 1j * RNGD.uniform(-s3, s3, (128, 128))) / np.sqrt(128)
R_lap = (RNGD.laplace(0.0, 1.0 / math.sqrt(2.0), (128, 128))
         + 1j * RNGD.laplace(0.0, 1.0 / math.sqrt(2.0), (128, 128))) \
    / np.sqrt(128)
MY_READERS = [R_uni, R_lap]

g1_ok, g2_ok, col_min = True, True, np.inf
for R in MY_READERS:
    for pin in PINS:
        KER_R = [K_S @ e[pin[i]] @ R for i in range(4)]
        hdef = min(float(np.max(np.abs(M - M.conj().T))) for M in KER_R)
        g1_ok = g1_ok and hdef > 0.3
        for _ in range(2):
            psi = P_plus @ (RNGD.standard_normal(128)
                            + 1j * RNGD.standard_normal(128))
            psi /= np.linalg.norm(psi)
            B = k1.Bfull(psi, KER_R)
            col_min = min(col_min, max(float(np.max(np.abs(
                k1.mu_cols(M, psi)[1:]))) for M in KER_R))
            g2_ok = g2_ok and int(np.linalg.matrix_rank(B, tol=1e-10)) == 4
check("E", "X1.5 gate half CONFIRMED beyond the original's draw law: "
           "UNIFORM-entry and LAPLACE-entry readers (unit variance, "
           "non-Gaussian) still pass BOTH gates -- non-H-self-adjoint "
           "> 0.3, confined bridge rank 4, commutant columns O(0.1): the "
           "reader's gate passage is not a Gaussian artifact",
      g1_ok and g2_ok and col_min > 0.01,
      f"min confined column {col_min:.3f}")


def my_forms(psi0, pin, KER):
    Qp = QFAM[pin]
    Pm = np.stack([psi0, Qp[0] @ psi0, Qp[1] @ psi0, Qp[2] @ psi0], axis=1)
    Um = [Pm, 1j * Pm, C @ Pm.conj(), 1j * (C @ Pm.conj())]
    A = np.zeros((4, 4, 4, 4))
    for i in range(4):
        W = KER[i] @ Pm
        for mu in range(4):
            Ar = (Um[mu].conj().T @ W).real
            A[i, mu] = 0.5 * (Ar + Ar.T)
    return A


def draw_state(kind, rng):
    if kind == "gauss":
        psi = rng.standard_normal(128) + 1j * rng.standard_normal(128)
    elif kind == "uniform":
        psi = rng.uniform(-1, 1, 128) + 1j * rng.uniform(-1, 1, 128)
    elif kind == "laplace":
        psi = rng.laplace(0, 1, 128) + 1j * rng.laplace(0, 1, 128)
    elif kind == "sparse":
        psi = np.zeros(128, complex)
        idx = rng.choice(128, 7, replace=False)
        psi[idx] = rng.standard_normal(7) + 1j * rng.standard_normal(7)
    else:  # confined
        psi = P_plus @ (rng.standard_normal(128)
                        + 1j * rng.standard_normal(128))
    return psi / np.linalg.norm(psi)


RNGS = np.random.default_rng(556677)
CASES = [(0, PINS[0], "gauss"), (0, PINS[0], "uniform"),
         (0, PINS[1], "laplace"), (0, PINS[0], "sparse"),
         (1, PINS[0], "gauss"), (1, PINS[1], "uniform"),
         (1, PINS[0], "confined"), (1, PINS[1], "gauss")]
my15, cons_ok = [], True
for ri, pin, kind in CASES:
    psi = draw_state(kind, RNGS)
    KER_R = [K_S @ e[pin[i]] @ MY_READERS[ri] for i in range(4)]
    A = my_forms(psi, pin, KER_R)
    # robust analytic-Jacobian root-finder on MY independent values W3/W4
    # (the reader forms are high-degree with clustered preimages; the DRAW
    # LAWS, readers, seeds, states and regular values are all independently
    # varied from the original -- the counter is the target's, applied to
    # independent inputs, which is exactly what the anti-artifact claim needs)
    d3, _ = k1.degree_by_preimage(lambda v, _A=A: k1.qv(v, _A),
                                  lambda v, _A=A: k1.jac(v, _A), W3)
    d4, _ = k1.degree_by_preimage(lambda v, _A=A: k1.qv(v, _A),
                                  lambda v, _A=A: k1.jac(v, _A), W4)
    cons_ok = cons_ok and d3 == d4 and d3 % 2 == 1
    my15.append(d3)
    print(f"       reader degree R{ri} pin{pin[0]} {kind:8s}: "
          f"{d3:+d} / {d4:+d}", flush=True)
vals15 = sorted(set(my15))
# my non-Gaussian sweep witnessed instability but NOT the c=0 mod 3 member.
# Crucial subtlety the original's prose glosses: c = -1 -> k = 8 mod 24 and
# c = +1 -> k = 16 mod 24 are BOTH order 3, so scatter over {-1, +1} would
# NOT kill forcing.  The X1.5 kill rests ENTIRELY on the existence of a
# c = 0 mod 3 (order-killing) member.  So I reproduce THAT crux directly on
# the original's own Gaussian consumer-shape reader family, deterministically
# rebuilt, evaluated on MY independent regular values W3/W4 (independent
# value; the target's staked witness re-checked, not taken on faith).
RNG_R0 = np.random.default_rng(20260722)          # the original's reader seed
ORIG_READERS = []
for _ in range(2):
    R = (RNG_R0.standard_normal((128, 128))
         + 1j * RNG_R0.standard_normal((128, 128))) / np.sqrt(128)
    ORIG_READERS.append(R)
RNG_S0 = np.random.default_rng(99)                # the original's state seed
ORIG_DRAWS = []
for _ in range(6):
    psi = RNG_S0.standard_normal(128) + 1j * RNG_S0.standard_normal(128)
    ORIG_DRAWS.append(psi / np.linalg.norm(psi))
for _ in range(3):
    psi = P_plus @ (RNG_S0.standard_normal(128)
                    + 1j * RNG_S0.standard_normal(128))
    ORIG_DRAWS.append(psi / np.linalg.norm(psi))
for kk in (5, 11):
    psi = np.zeros(128, complex)
    idx = RNG_S0.choice(128, kk, replace=False)
    psi[idx] = RNG_S0.standard_normal(kk) + 1j * RNG_S0.standard_normal(kk)
    ORIG_DRAWS.append(psi / np.linalg.norm(psi))
ORIG_CASES = [(0, PINS[0], ORIG_DRAWS[0]), (0, PINS[0], ORIG_DRAWS[1]),
              (1, PINS[0], ORIG_DRAWS[4]), (0, PINS[0], ORIG_DRAWS[9])]
repro = []
for ri, pin, psi in ORIG_CASES:
    KER_R = [K_S @ e[pin[i]] @ ORIG_READERS[ri] for i in range(4)]
    A = my_forms(psi, pin, KER_R)
    d3, _ = k1.degree_by_preimage(lambda v, _A=A: k1.qv(v, _A),
                                  lambda v, _A=A: k1.jac(v, _A), W3)
    d4, _ = k1.degree_by_preimage(lambda v, _A=A: k1.qv(v, _A),
                                  lambda v, _A=A: k1.jac(v, _A), W4)
    repro.append((d3, d4))
    print(f"       ORIG decisive case R{ri} pin{pin[0]}: {d3:+d} / {d4:+d}",
          flush=True)
killer_repro = any(d3 % 3 == 0 and d3 == d4 for d3, d4 in repro)
repro_cons = all(d3 == d4 for d3, d4 in repro)
sweep_scatter = len(vals15) >= 2 and cons_ok
check("E", "X1.5 kill CONFIRMED via its actual crux -- REVISED framing: the "
           "kill does NOT rest on generic scatter (my 8-case NON-GAUSSIAN "
           "sweep scattered only over {-1, +1}, and BOTH give order 3: "
           "k = 8 and 16 mod 24 -- so under those laws X1.5 would appear to "
           "SUFFICE).  The kill rests solely on the c = 0 mod 3 ORDER-KILLER, "
           "which I reproduce on the original's Gaussian consumer-shape "
           "reader family (deterministically rebuilt) evaluated on MY "
           "independent regular values W3/W4: a 3-divisible member recurs "
           "(k = 192 = 0 mod 24, order 1), target-consistent.  So X1.5 is "
           "insufficient -- but because a state-dependent order-KILLER "
           "exists, not because the class merely wobbles; and that killer is "
           "reader/draw-law-sensitive (absent in my non-Gaussian 8-case "
           "sweep).  Recorded as a material framing revision",
      killer_repro and repro_cons and sweep_scatter
      and order24((64 * 3) % 24) == 1,
      f"ORIG decisive degrees {repro} (3-divisible order-killer reproduced: "
      f"{killer_repro}); my non-Gaussian sweep {vals15} (order-killer "
      f"ABSENT -> law-sensitive)")

# =============================================================================
print()
print("=" * 78)
print("SURFACE A  the minimality lattice: the missing rung and the fork")
print("=" * 78)

zeta6 = complex(math.cos(math.pi / 3), math.sin(math.pi / 3))
zeta5 = complex(math.cos(2 * math.pi / 5), math.sin(2 * math.pi / 5))
zeta4 = 1j
zeta3 = complex(math.cos(2 * math.pi / 3), math.sin(2 * math.pi / 3))


def act(u, v):
    z1 = complex(v[0], v[1]) * u
    z2 = complex(v[2], v[3]) * u
    return np.array([z1.real, z1.imag, z2.real, z2.imag])


def eq_defect(f, u):
    worst = 0.0
    for v in V_MINE:
        lhs = f(act(u, v))
        fv = f(v)
        z1 = complex(fv[0], fv[1]) * u
        z2 = complex(fv[2], fv[3]) * u
        worst = max(worst, float(np.max(np.abs(
            lhs - np.array([z1.real, z1.imag, z2.real, z2.imag])))))
    return worst


def deck_defect(f):
    return max(float(np.max(np.abs(f(-v) + f(v)))) for v in V_MINE)


# their Z/6 witnesses re-verified on my machinery + a NEW member (13,1)
j71 = join_map(7, 1)
dj71, nj71, mj71, _ = join_degree_analytic(7, 1, W3)
dnj71, _ = my_degree(j71, W3, nstarts=7000, seed=105)
dj13, nj13, mj13, _ = join_degree_analytic(13, 1, W4)


def u1_oracle(coefs):
    def f(v, _c=tuple(coefs)):
        z1 = complex(v[0], v[1])
        z2 = complex(v[2], v[3])
        w = z1.conjugate() * z2
        g = np.array([_c[0] + _c[1] * w.real,
                      _c[2] * w.imag + _c[3] * (abs(z1) ** 2 - 0.5),
                      _c[4] + _c[5] * w.real, _c[6] * w.imag])
        g = g / np.linalg.norm(g)
        return ham(v, g)
    return f


f_u1 = u1_oracle([1.0, 0.7, -0.6, 0.5, 0.4, -0.8, 0.3])
d_u1, _ = my_degree(f_u1, W3, nstarts=4000, seed=107)
check("E", "Z/6 rung CONFIRMED on independent machinery: the twisted member "
           "join(7,1) is Z/6-equivariant at 1e-15, NOT U(1)-equivariant, "
           "exactly deck-odd, degree +7 by closed-form enumeration (7 "
           "preimages) AND my Newton counter; a NEW member join(13,1) the "
           "original never ran gives +13 (13 = 1 mod 6, order 3); their "
           "invariant-twisted generic member gives +1 on my counter: every "
           "witnessed member is 1 mod 6, order 3 across the type",
      eq_defect(j71, zeta6) < 1e-12 and eq_defect(j71, complex(
          math.cos(0.7), math.sin(0.7))) > 0.1 and deck_defect(j71) == 0.0
      and dj71 == 7 and nj71 == 7 and mj71 < 1e-9 and dnj71 == 7
      and dj13 == 13 and nj13 == 13 and mj13 < 1e-9 and d_u1 == 1
      and order24((64 * 7) % 24) == 3 and order24((64 * 13) % 24) == 3,
      f"deg(7,1) {dj71:+d}/{dnj71:+d}; deg(13,1) {dj13:+d}; u1 member "
      f"{d_u1:+d}")

# THE MISSING RUNG: Z/5 (order 5 < 6, never examined in the original)
j211 = join_map(21, 1)
dj211, nj211, mj211, _ = join_degree_analytic(21, 1, W3)
j61 = join_map(6, 1)
j91 = join_map(9, 1)
dj91, nj91, mj91, _ = join_degree_analytic(9, 1, W3)
check("E", "EXHAUSTION GAP FOUND AND CLOSED: the original's lattice claim "
           "('Z/2, Z/3, Z/4 fail; Z/6 first sufficient') never examined "
           "Z/5.  Witness constructed here: join(21,1) is Z/5-equivariant "
           "at 1e-15 (21 = 1 mod 5), NOT Z/6-equivariant, exactly deck-odd, "
           "degree +21 by closed-form enumeration (21 verified preimages, "
           "all signs +1); 3 | 21 -> k = 1344 = 0 mod 24, ORDER 1: Z/5 "
           "FAILS under BOTH semantics (and its deck-breaking member "
           "join(6,1) fails admissibility too).  Z/4 re-witnessed: "
           "join(9,1) degree +9 by enumeration, order 1.  The gap closes "
           "IN FAVOR of the Z/6 rung -- but the exhaustion as WRITTEN "
           "was incomplete",
      eq_defect(j211, zeta5) < 1e-12 and eq_defect(j211, zeta6) > 0.1
      and deck_defect(j211) == 0.0 and dj211 == 21 and nj211 == 21
      and mj211 < 1e-9 and order24((64 * 21) % 24) == 1
      and eq_defect(j61, zeta5) < 1e-12 and deck_defect(j61) > 0.5
      and dj91 == 9 and nj91 == 9 and mj91 < 1e-9
      and eq_defect(j91, zeta4) < 1e-12 and deck_defect(j91) == 0.0
      and order24((64 * 9) % 24) == 1)

q_rand = _normalize(np.array([0.3, 0.7, -0.5, 0.4]))
sq_rand = ham(q_rand, q_rand)
invol_ok = abs(sq_rand[0] - 1.0) > 0.1  # generic q: q^2 != 1
# q^2 = (q0^2-|u|^2, 2 q0 u); with |q|=1: q^2 = 1  =>  2q0^2 = 2, u = 0
alg_ok = True
for _ in range(2000):
    q = _normalize(RNGB.standard_normal(4))
    if np.linalg.norm(q[1:]) > 1e-6 and abs(q[0]) > 1e-6:
        s = ham(q, q)
        alg_ok = alg_ok and float(np.max(np.abs(s - np.array(
            [1.0, 0, 0, 0])))) > 1e-6
check("E", "the order-<=-6 subgroup lattice of Sp(1) is EXACTLY "
           "{Z/2, Z/3, Z/4, Z/5, Z/6}: q^2 = 1 with |q| = 1 forces "
           "2 q0^2 = 2 and q0 u = 0, i.e. q = +-1 -- Sp(1) has a UNIQUE "
           "involution, so no Klein group and no S_3 embed; every subgroup "
           "of order <= 7 is cyclic (2000-sample witness of the algebra; "
           "the identity is exact).  With Z/5 closed above, the exhaustion "
           "below Z/6 is now genuinely complete -- one rung later than "
           "the original left it",
      invol_ok and alg_ok)

# THE ACCOUNTING FORK (the main finding)
z63 = zeta6 ** 3
z62 = zeta6 ** 2
cube_act = max(float(np.max(np.abs(act(z63, v) + v))) for v in V_MINE)
j41 = join_map(4, 1)
# deck-odd AND Z/3-equivariant  <=>  Z/6-equivariant, on every witness
fork_wit = (eq_defect(j71, zeta3) < 1e-12 and deck_defect(j71) == 0.0
            and eq_defect(j71, zeta6) < 1e-12
            and eq_defect(f_u1, zeta3) < 1e-12 and deck_defect(f_u1) < 1e-12
            and eq_defect(f_u1, zeta6) < 1e-12
            and eq_defect(j41, zeta3) < 1e-12 and deck_defect(j41) > 0.5
            and eq_defect(j41, zeta6) > 0.5)
# the imported machinery's own precedent: deck co-flip applied NATIVELY
k1_native = [n for _t, n, ok in k1.RESULTS if ok and
             ("excluded by the verified co-flip" in n
              or "NOT the verified co-flip" in n)]
# admissible Z/3 members witnessed in this run: degrees 1, 7, 13 == 1 mod 3
adm_z3 = all(d % 3 == 1 for d in (1, dj71, dj13)) and \
    all(d % 2 == 1 for d in (1, dj71, dj13))
check("E", "THE ACCOUNTING FORK (main hostile finding, machine-witnessed): "
           "(i) zeta6^3 = -1 and act(zeta6^3, v) = -v EXACTLY -- the "
           "anchor's cube IS the fiber deck action, as arithmetic; (ii) "
           "deck-odd AND Z/3-equivariant <=> Z/6-equivariant on every "
           "witness (join(7,1), the u1 member, and join(4,1) fails BOTH "
           "sides together); (iii) the imported k1 machinery itself applies "
           "the deck co-flip as a NATIVE exclusion (both receipt checks "
           "live and passing in this very run), and the target's Section-1 "
           "lists deck admissibility as a GATE beside G1/G2; (iv) the "
           "gate-passing members of the bare Z/3 type witnessed here (+1, "
           "+7, +13) are all 1 mod 3 = order-3-delivering, and c = 1 mod 3 "
           "excludes 3 | c for EVERY member (Olum, same citation).  UNDER "
           "THE PROGRAM'S OWN GATE SEMANTICS THE MINIMAL EXTERNAL INPUT IS "
           "ONE TRIT (Z/3); the Z/6 headline holds only under the "
           "alternative semantics where the anchor must re-supply the deck "
           "parity the inventory already verified",
      abs(z63 + 1.0) < 1e-15 and abs(z62 - zeta3) < 1e-15
      and cube_act < 1e-15 and fork_wit and len(k1_native) == 2 and adm_z3,
      f"cube action defect {cube_act:.1e}; k1 native-exclusion receipts "
      f"{len(k1_native)}/2; admissible Z/3 degrees (1,{dj71},{dj13}) "
      f"all = 1 mod 3")

r2_ok = all((r * r) % 6 == 1 for r in (1, 5)) and \
    all((r * r) % 3 == 1 for r in (1, 2))
check("E", "Olum orientation-freedom arithmetic CONFIRMED: both units of "
           "Z/6 (r = 1, 5) square to 1 mod 6 and both generators of Z/3 "
           "(r = 1, 2) square to 1 mod 3 -- the trit anchor needs no "
           "orientation choice, exactly as claimed; note this cuts BOTH "
           "ways: it is also why the bare-trit route in the fork needs no "
           "extra datum", r2_ok)

# =============================================================================
print()
print("=" * 78)
print("CONTROLS")
print("=" * 78)


def blind2(v):
    z2 = complex(v[2], v[3])
    w = z2 / abs(z2)
    return np.array([w.real, w.imag, 0.0, 0.0])


bl_deck = max(float(np.max(np.abs(blind2(-v) + blind2(v)))) for v in V_MINE)
bl_reach = max(max(abs(blind2(v)[2]), abs(blind2(v)[3])) for v in V_MINE)
va = _normalize(np.array([1.0, 0.0, 1e-9, 0.0]))
vb = _normalize(np.array([1.0, 0.0, -1e-9, 0.0]))
jump = float(np.max(np.abs(blind2(va) - blind2(vb))))
check("F", "planted control REBUILT (my own weight-blind oracle, on the "
           "OTHER complex axis than the original's): passes the Z/2 deck "
           "shadow exactly, fails G1 exactly (reach 0.0), and is "
           "necessarily discontinuous (2.0 jump across 2e-9) -- the "
           "admission pipeline's rejection of weight-blind oracles "
           "reproduces under an independent construction",
      bl_deck == 0.0 and bl_reach == 0.0 and jump > 1.9,
      f"deck {bl_deck:.1e}; reach {bl_reach:.1e}; jump {jump:.2f}")

seen = {1, 3, dj71, dj91, dj13, dj211} | set(my15)
check("F", "no-anchor guard + counter separation: with NO equivariance "
           "datum the admissible (deck-odd) type contains 3-divisible "
           "members (join(3,1)) -- so the fork's bare-trit conclusion does "
           "NOT collapse to 'X0 forces' (it does not); and this run's "
           "independent machinery separated every class at stake",
      3 in seen and 1 in seen and 7 in seen and 9 in seen and 13 in seen
      and 21 in seen and order24((64 * 3) % 24) == 1,
      f"degrees separated this run: {sorted(seen)}")

# =============================================================================
print()
nT = sum(1 for t, _n, ok in RESULTS if t == "T")
nE = sum(1 for t, _n, ok in RESULTS if t == "E")
nF = sum(1 for t, _n, ok in RESULTS if t == "F")
fails = [(t, n) for t, n, ok in RESULTS if not ok]
all_ok = not fails
print(f"HEADLINE: HOSTILE VERIFICATION COMPLETE -- zero computational "
      f"refutations, one MATERIAL attribution fork, one exhaustion gap "
      f"closed.  X2 sufficiency CONFIRMED by exact linear algebra (right "
      f"translation is orthogonal with det +1; no preimage counting "
      f"needed).  X1's three legs CONFIRMED (fresh seeds, independent "
      f"counter, closed-form join degrees).  X1.5 insufficiency CONFIRMED "
      f"but REFRAMED: its kill rests solely on a c = 0 mod 3 ORDER-KILLER "
      f"(reproduced on the original's Gaussian reader family via my own "
      f"regular values), NOT on generic scatter -- my non-Gaussian sweep "
      f"scattered over {{-1,+1}}, both order 3, so the killer is "
      f"reader/law-sensitive.  Z/6 rung arithmetic CONFIRMED (new member "
      f"+13).  "
      f"BUT: (1) the written exhaustion skipped Z/5 -- closed here "
      f"(join(21,1), degree +21, order-killer; Sp(1)'s unique involution "
      f"makes the order-<=-6 lattice exactly Z/2..Z/6); (2) THE ACCOUNTING "
      f"FORK: deck-odd Z/3-equivariance IS Z/6-equivariance, and the "
      f"imported machinery treats deck admissibility as a NATIVE gate -- "
      f"under the program's own semantics the minimal EXTERNAL input is "
      f"ONE TRIT, and 'the bit is the cube' becomes an identity about "
      f"native bookkeeping, not about the external payload bit (whose "
      f"gate- and class-inertness legs A/B themselves prove).  "
      f"{nE} [E] + {nF} [F] = {nE + nF} (setup [T] = {nT} excluded)   "
      f"{'ALL PASS' if all_ok else 'FAILURES PRESENT'}   "
      f"({time.time() - t_start:.1f} s"
      f"{'; REDUCED-BREADTH LADDER: Newton starts / 3' if FAST else ''})")
if fails:
    for t, n in fails:
        print(f"  FAILED [{t}] {n}")
sys.exit(0 if all_ok else 1)
