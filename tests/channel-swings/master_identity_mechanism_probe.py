#!/usr/bin/env python3
"""MASTER IDENTITY MECHANISM -- the F5-shadow identity DERIVED, step by step.

CHANNEL: S_IG/B.5 construction frontier follow-up (named open computation
         from the F5 shadow: derive the master identity).
DESIGN:  explorations/master-identity-mechanism-2026-07-20.md
EXTENDS: tests/channel-swings/f5_shadow_c2_flip_probe.py (the discovery)
         tests/generation-sector/gen_sector_bridge.py (anchors)
         tests/oq_rk1_cl95_explicit_rep.py (the verified Cl(9,5) rep)
STATUS:  exploration tier; UNCONDITIONAL (pure Clifford algebra on the
         verified rep -- no boundary-adapter axiom consumed); no claim,
         canon, or public-posture movement.

WHAT IS PROVED (paper-grade symbolic derivation, every step machine-
corroborated below on the actual matrices). Let e_a (a = 0..13) be the
verified Cl(9,5) gammas (eta = diag(+1 x9, -1 x5)), n = 14, DIM = 128,
c = c(xi) = sum_a xi_a e_a with xi REAL, Gamma = [e_0 ... e_13],
Pi_RS = I - Gamma^+ (Gamma Gamma^+)^{-1} Gamma, M_D = I_14 (x) c,
X = Gamma M_D Pi_RS, A = X X^+, K_S = e_0 ... e_8.

  Step 1 (completeness).   Gamma Gamma^+ = sum_a e_a e_a^+ = n I,
                           so Pi_RS = I - (1/n) Gamma^+ Gamma.
  Step 2 (grade-1 Fierz).  sum_a eta_a e_a w e_a = (2-n) w for grade-1 w
                           [IMPORTED-standard gamma-matrix contraction],
                           so Gamma M_D Gamma^+ = (2-n) c and
                           X = Gamma M_D + ((n-2)/n) c Gamma, i.e. the
                           blocks are X_a = e_a c + lam c e_a, lam=(n-2)/n.
  Step 3 (density input).  e_a^+ = eta_a e_a  =>  c^+ = c(eta xi), and
                           c c^+ = <xi, eta xi>_eta I + xi ^ (eta xi)
                                 = |xi|^2_E I + B,
                           where |xi|^2_E is the EUCLIDEAN norm-square and
                           B = sum_{a<b} xi_a xi_b (eta_b - eta_a) e_a e_b
                           is a PURE MIXED bivector (same-sign coefficients
                           vanish identically for real xi).
  Step 4 (grade-2 Fierz).  sum_a eta_a e_a B e_a = (n-4) B; assembling
                           A = sum_a eta_a X_a X_a^+ term by term gives the
                           closed form of the C2 obstruction density:
                               A = (4(n-1)/n) |xi|^2_E I - (4/n) B
                           (n=14: A = (26/7)|xi|^2 I - (2/7) B).
                           A is scalar + mixed bivector, NOTHING ELSE.
  Step 5 (reflection).     Ad(K_S) e_a = +e_a (a<=8), -e_a (a>=9) -- K_S is
                           the space/time reflection -- so K_S ANTICOMMUTES
                           with every mixed bivector: K_S B = -B K_S. Hence
                               A + K_S A K_S = (8(n-1)/n) |xi|^2_E I.
  Constant identification. tr B = 0, so tr A = C2^2 = DIM*(4(n-1)/n)|xi|^2_E
                           = (3328/7)|xi|^2_E  [NEW closed form for C2],
                           and (8(n-1)/n)|xi|^2_E = 2 tr A / DIM
                           = C2^2/(DIM/2) = C2^2/64.
                           The 64 is DIM/2 TRACE BOOKKEEPING (the factor 2
                           from the two-term K_S-average), not a
                           quaternion-specific quantity -- the same theorem
                           holds verbatim in Cl(5,3) at DIM=16 with
                           constant C2^2/8 (checked below).
  Corollary.               tr(K_S A) = 0: K_S is grade 9 and K_S B is grade
                           9 (one common index), both traceless.

SCOPE (decided below): the identity holds for EVERY real xi -- including
null (q=0) and timelike (q<0) vectors; Pi_RS is xi-independent and no step
divides by q. The frozen gen_sector_bridge.XI is in no way special. For
genuinely COMPLEX xi the closed form for A still holds (the calculus is
xi-agnostic) but B acquires K_S-even same-sign components and the master
identity FAILS by exactly -(4/n)(B + K_S B K_S) -- the real-xi condition is
the single load-bearing input of Step 3, and the failure mode is the one
the mechanism predicts (falsification control).

CONSTRUCTIONS USED (GEOMETER-VS-PHYSICS-OBJECTS discipline): all objects
PROGRAM-NATIVE (the verified Cl(9,5)=M(64,H) rep, the raw gamma-trace
kernel projector Pi_RS, C2 as the native obstruction NORM -- the closed
form C2 = sqrt(3328/7) ||xi||_E is degree-1 homogeneous in xi, confirming
the killed-list typing: C2 is a norm, NOT an index). The two contraction
identities of Steps 2/4 are IMPORTED-standard textbook gamma-matrix
algebra, named as such; both are machine-verified here on the actual rep.

NONCLAIMS. No claim/canon/posture movement; nothing here touches the
sector datum, S_IG, the N-rungs, or the F5 decisive test; the signed
fraction |k|/C2^2 = 0.5975 of the F5 probe is NOT derived here (named
leftover). Deterministic; numpy only; seeded 20260720.
"""
from __future__ import annotations

import os
import sys

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "generation-sector"))
sys.path.insert(0, os.path.join(HERE, ".."))
import gen_sector_bridge as gb  # noqa: E402
import oq_rk1_cl95_explicit_rep as cl95  # noqa: E402

N_DIRS, DIM = 14, 128
ETA = np.array([1.0] * 9 + [-1.0] * 5)
RNG = np.random.default_rng(20260720)

RESULTS = []


def check(tag, name, ok, detail=""):
    RESULTS.append((tag, name, bool(ok)))
    line = f"[{tag}] {'PASS' if ok else 'FAIL'}  {name}"
    if detail:
        line += f"   ({detail})"
    print(line)
    return ok


def rel(x, ref):
    """Relative residual ||x|| / ||ref||."""
    return float(np.linalg.norm(x)) / max(float(np.linalg.norm(ref)), 1e-300)


# --- the actual W229 anchors --------------------------------------------------
e = gb.gammas()
K_S = e[0].copy()
for a in range(1, 9):
    K_S = K_S @ e[a]
I128 = np.eye(DIM, dtype=complex)
XI = np.real(np.asarray(gb.XI)).astype(float)

Gamma = np.hstack(e)
GG = Gamma @ Gamma.conj().T
Pi_RS = (np.eye(N_DIRS * DIM, dtype=complex)
         - Gamma.conj().T @ np.linalg.inv(GG) @ Gamma)


def cvec(v):
    return sum(v[a] * e[a] for a in range(N_DIRS))


def gamma_md(v):
    """Gamma M_D as 128 x 1792 without forming the 1792^2 kron."""
    c = cvec(v)
    return np.hstack([e[a] @ c for a in range(N_DIRS)])


def X_of(v):
    """The original-route obstruction map X = Gamma M_D Pi_RS."""
    return gamma_md(v) @ Pi_RS


def bivec(u, v):
    """The wedge bivector u ^ v = sum_{a<b} (u_a v_b - u_b v_a) e_a e_b."""
    B = np.zeros((DIM, DIM), dtype=complex)
    for a in range(N_DIRS):
        for b in range(a + 1, N_DIRS):
            B += (u[a] * v[b] - u[b] * v[a]) * (e[a] @ e[b])
    return B


# --- [T] setup: reproduce the discovery exactly as found ---------------------
e_, Gamma_gb, Pi_gb, M_D = gb.constraint_objects()
X_orig = Gamma_gb @ M_D @ Pi_gb
A = X_orig @ X_orig.conj().T
C2 = float(np.linalg.norm(X_orig))
bare = float(np.linalg.norm(Pi_gb @ M_D - M_D @ Pi_gb))
Srem = A + K_S @ A @ K_S - (np.trace(A).real / 64.0) * I128
check("T", "the REAL anchors reproduce (bare 58.7215, C2 155.3625) and the "
           "F5-shadow master identity A + K_S A K_S = (C2^2/64) I is "
           "re-verified as discovered; the local fast route Gamma M_D Pi_RS "
           "agrees with gb.constraint_objects exactly",
      abs(bare - 58.7215) < 1e-2 and abs(C2 - 155.3625) < 1e-2
      and rel(Srem, A) < 1e-11 and rel(X_of(XI) - X_orig, X_orig) < 1e-12,
      f"bare {bare:.4f}, C2 {C2:.4f}, master rel-res {rel(Srem, A):.1e}")

adj_ok = max(float(np.max(np.abs(e[a].conj().T - ETA[a] * e[a])))
             for a in range(N_DIRS))
check("T", "rep sanity: e_a^+ = eta_a e_a for all 14 legs; K_S^2 = I and "
           "K_S^+ = K_S (9 factors: reversal sign (-1)^36 = +1)",
      adj_ok < 1e-14
      and float(np.max(np.abs(K_S @ K_S - I128))) < 1e-12
      and float(np.max(np.abs(K_S - K_S.conj().T))) < 1e-12)


# =============================================================================
# Part A -- the derivation, step by step (frozen XI)
# =============================================================================
check("E", "STEP 1 (completeness): Gamma Gamma^+ = 14 I exactly, so "
           "Pi_RS = I - (1/14) Gamma^+ Gamma -- the RS projector is the "
           "gamma-trace kernel with scalar normalizer",
      float(np.max(np.abs(GG - 14.0 * I128))) < 1e-12,
      f"max |Gamma Gamma^+ - 14 I| = {float(np.max(np.abs(GG - 14.0 * I128))):.1e}")

c = cvec(XI)
grade1 = max(rel(sum(ETA[a] * e[a] @ e[b] @ e[a] for a in range(N_DIRS))
                 + 12.0 * e[b], e[b]) for b in range(N_DIRS))
GMDG = gamma_md(XI) @ Gamma.conj().T
check("E", "STEP 2 (grade-1 contraction, IMPORTED-standard): "
           "sum_a eta_a e_a e_b e_a = (2-n) e_b = -12 e_b for every leg, "
           "hence Gamma M_D Gamma^+ = -12 c(xi)",
      grade1 < 1e-13 and rel(GMDG + 12.0 * c, c) < 1e-13,
      f"worst leg rel-res {grade1:.1e}")

lam = (N_DIRS - 2.0) / N_DIRS
X_closed = gamma_md(XI) + lam * np.hstack([c @ e[a] for a in range(N_DIRS)])
check("E", "STEP 3 (block closed form): X = Gamma M_D + (6/7) c Gamma "
           "machine-exactly -- the obstruction map has blocks "
           "X_a = e_a c + (6/7) c e_a; the projector is fully consumed",
      rel(X_closed - X_orig, X_orig) < 1e-12,
      f"rel-res {rel(X_closed - X_orig, X_orig):.1e}")

s_E = float(np.dot(XI, XI))
B = bivec(XI, ETA * XI)
ccdag = c @ c.conj().T
mixed_only = all(abs(XI[a] * XI[b] * (ETA[b] - ETA[a])) < 1e-15
                 for a in range(N_DIRS) for b in range(N_DIRS)
                 if ETA[a] == ETA[b])
check("E", "STEP 4a (density input): c c^+ = |xi|^2_E I + B with "
           "|xi|^2_E the EUCLIDEAN norm-square (= <xi, eta xi>_eta) and "
           "B = xi /\\ (eta xi) a PURE MIXED bivector -- every same-sign "
           "coefficient xi_a xi_b (eta_b - eta_a) vanishes identically "
           "for real xi",
      rel(ccdag - s_E * I128 - B, ccdag) < 1e-13 and mixed_only,
      f"|xi|^2_E = {s_E:.4f}, rel-res {rel(ccdag - s_E * I128 - B, ccdag):.1e}")

grade2 = rel(sum(ETA[a] * e[a] @ B @ e[a] for a in range(N_DIRS)) - 10.0 * B, B)
check("E", "STEP 4b (grade-2 contraction, IMPORTED-standard): "
           "sum_a eta_a e_a B e_a = (n-4) B = +10 B on the actual mixed "
           "bivector",
      grade2 < 1e-13, f"rel-res {grade2:.1e}")

A_closed = (26.0 / 7.0) * s_E * I128 - (2.0 / 7.0) * B
check("E", "STEP 4c (CLOSED FORM of the C2 density): assembling the four "
           "terms of A = sum_a eta_a X_a X_a^+ with Steps 2/4a/4b gives "
           "A = (26/7)|xi|^2_E I - (2/7) B -- scalar plus mixed bivector, "
           "nothing else (coefficients 4(n-1)/n and 4/n) -- machine-exact "
           "against the numerically assembled A",
      rel(A_closed - A, A) < 1e-12,
      f"rel-res {rel(A_closed - A, A):.1e}; scalar (26/7)|xi|^2 = "
      f"{(26.0 / 7.0) * s_E:.4f}")

refl = max(rel(K_S @ e[a] @ K_S - ETA[a] * e[a], e[a]) for a in range(N_DIRS))
anti = rel(K_S @ B + B @ K_S, B @ K_S)
check("E", "STEP 5 (reflection): Ad(K_S) e_a = eta_a e_a -- K_S is the "
           "space/time reflection -- so K_S ANTICOMMUTES with the mixed "
           "bivector: K_S B = -B K_S. The traceless part of A "
           "anticommutes with K_S; the K_S-even part of A is pure scalar",
      refl < 1e-12 and anti < 1e-12,
      f"reflection rel-res {refl:.1e}, anticommutation rel-res {anti:.1e}")

const_derived = (52.0 / 7.0) * s_E
c2_closed = (3328.0 / 7.0) * s_E
master_closed = rel(A + K_S @ A @ K_S - const_derived * I128, A)
check("E", "MASTER IDENTITY DERIVED: A + K_S A K_S = (52/7)|xi|^2_E I "
           "(scalar doubles, bivector cancels), and the constant is "
           "exactly C2^2/64 because tr A = C2^2 = (3328/7)|xi|^2_E -- a "
           "NEW closed form for C2 itself, reproducing the 155.3625 "
           "anchor and confirming C2 as degree-1 homogeneous NORM "
           "(killed-list honored: not an index)",
      master_closed < 1e-12
      and abs(const_derived - C2 ** 2 / 64.0) < 1e-9 * const_derived
      and abs(np.sqrt(c2_closed) - C2) < 1e-9 * C2,
      f"(52/7)|xi|^2 = {const_derived:.4f} = C2^2/64 = {C2 ** 2 / 64.0:.4f}; "
      f"sqrt((3328/7)|xi|^2) = {np.sqrt(c2_closed):.4f} = C2")

check("E", "COROLLARY: tr K_S = 0 and tr(K_S B) = 0 (grade-9 monomials, "
           "traceless), so tr(K_S A) = 0 -- the F5-shadow zero-sum of the "
           "signed accounting is forced by the closed form",
      abs(np.trace(K_S)) < 1e-10 and abs(np.trace(K_S @ B)) < 1e-8
      and abs(np.trace(K_S @ A)) < 1e-8,
      f"|tr K_S A| = {abs(np.trace(K_S @ A)):.1e}")


# =============================================================================
# Part B -- scope: every real xi (the frozen XI is not special)
# =============================================================================
draws = []
v = RNG.standard_normal(N_DIRS)
draws.append(("generic", v))
v = np.zeros(N_DIRS)
v[:9] = RNG.standard_normal(9)
draws.append(("space-only (q>0)", v))
v = np.zeros(N_DIRS)
v[9:] = RNG.standard_normal(5)
draws.append(("time-only (q<0)", v))
v = RNG.standard_normal(N_DIRS)
v[9:] *= np.sqrt(np.sum(v[:9] ** 2) / np.sum(v[9:] ** 2))
draws.append(("null (q=0)", v))
draws.append(("scaled 1e3", 1e3 * RNG.standard_normal(N_DIRS)))

worst_master, worst_closed, worst_const = 0.0, 0.0, 0.0
for label, v in draws:
    Xv = X_of(v)
    Av = Xv @ Xv.conj().T
    sv = float(np.dot(v, v))
    Bv = bivec(v, ETA * v)
    c2v = float(np.linalg.norm(Xv)) ** 2
    worst_master = max(worst_master,
                       rel(Av + K_S @ Av @ K_S - (c2v / 64.0) * I128, Av))
    worst_closed = max(worst_closed,
                       rel(Av - (26.0 / 7.0) * sv * I128 + (2.0 / 7.0) * Bv, Av))
    worst_const = max(worst_const,
                      abs(c2v - (3328.0 / 7.0) * sv) / c2v)
    q = float(np.dot(v, ETA * v))
    print(f"      draw {label:18s} q = {q:+10.3f}  master rel-res "
          f"{rel(Av + K_S @ Av @ K_S - (c2v / 64.0) * I128, Av):.1e}")
check("E", "SCOPE (all-real-xi): for 5 seeded draws -- generic, pure-space "
           "(q>0), pure-time (q<0), exactly null (q=0), and scale 1e3 -- "
           "the master identity, the closed form of A, and "
           "C2^2 = (3328/7)|xi|^2_E all hold at machine precision: the "
           "identity is a THEOREM OF THE CONSTRUCTION for every real xi "
           "(Pi_RS is xi-independent; no step divides by q); the frozen "
           "XI is not special; the constant is the xi-dependent scalar "
           "C2(xi)^2/64",
      worst_master < 1e-11 and worst_closed < 1e-11 and worst_const < 1e-11,
      f"worst rel-res: master {worst_master:.1e}, closed {worst_closed:.1e}, "
      f"C2-form {worst_const:.1e}")

# falsification control: genuinely complex xi
vc = RNG.standard_normal(N_DIRS) + 1j * RNG.standard_normal(N_DIRS)
cc = sum(vc[a] * e[a] for a in range(N_DIRS))
Xc = np.hstack([e[a] @ cc for a in range(N_DIRS)]) @ Pi_RS
Ac = Xc @ Xc.conj().T
sc = float(np.real(np.vdot(vc, vc)))
Bc = bivec(vc, ETA * np.conj(vc))
closed_c = rel(Ac - (26.0 / 7.0) * sc * I128 + (2.0 / 7.0) * Bc, Ac)
Rc = Ac + K_S @ Ac @ K_S - (np.trace(Ac).real / 64.0) * I128
B_even = 0.5 * (Bc + K_S @ Bc @ K_S)
pred = rel(Rc + (4.0 / 7.0) * B_even, Ac)
check("F", "FALSIFICATION CONTROL (mechanism corroborated at its "
           "boundary): for genuinely COMPLEX xi the closed form "
           "A = (26/7)|xi|^2 I - (2/7)B STILL holds (the Clifford "
           "calculus is xi-agnostic) but B acquires K_S-even same-sign "
           "components and the master identity FAILS -- by EXACTLY the "
           "predicted residual -(4/7)(B + K_S B K_S)/2 ... x2 -- so the "
           "real-xi condition of Step 4a is the single load-bearing "
           "input, and the frozen-XI identity holds because XI is real, "
           "not by accident",
      closed_c < 1e-11 and rel(Rc, Ac) > 1e-3 and pred < 1e-11
      and rel(B_even, Bc) > 1e-3,
      f"closed-form rel-res {closed_c:.1e}; master violation {rel(Rc, Ac):.1e} "
      f"(nonzero); predicted-residual match {pred:.1e}")


# =============================================================================
# Part C -- the constant: 1/64 is DIM/2 trace bookkeeping, not H-magic
# =============================================================================
c2_A = float(np.trace(A).real)
check("E", "CONSTANT IDENTIFICATION: the scalar is 2 tr(A)/DIM -- trace "
           "both sides of the identity (tr K_S A K_S = tr A since "
           "K_S^2 = I) -- and tr A = ||X||_F^2 = C2^2 by definition, so "
           "the 64 is DIM/2 = 128/2: pure trace bookkeeping (the factor "
           "2 from the two-term K_S average), numerically confirmed",
      abs(2.0 * c2_A / DIM - C2 ** 2 / 64.0) < 1e-9 * c2_A / 64.0
      and DIM // 2 == 64,
      f"2 tr A/DIM = {2.0 * c2_A / DIM:.4f} = C2^2/64")

# mini-rep control: Cl(5,3), n = 8, DIM = 16 -- same theorem, constant C2^2/8
n8, dim8 = 8, 16
G8 = cl95.jordan_wigner_gammas(4)
eta8 = np.array([1.0] * 5 + [-1.0] * 3)
f = [G8[a] if eta8[a] > 0 else 1j * G8[a] for a in range(n8)]
K8 = f[0] @ f[1] @ f[2] @ f[3] @ f[4]
I16 = np.eye(dim8, dtype=complex)
Gamma8 = np.hstack(f)
Pi8 = (np.eye(n8 * dim8, dtype=complex)
       - Gamma8.conj().T @ np.linalg.inv(Gamma8 @ Gamma8.conj().T) @ Gamma8)
v8 = RNG.standard_normal(n8)
c8 = sum(v8[a] * f[a] for a in range(n8))
X8 = np.hstack([f[a] @ c8 for a in range(n8)]) @ Pi8
A8 = X8 @ X8.conj().T
s8 = float(np.dot(v8, v8))
B8 = np.zeros((dim8, dim8), dtype=complex)
for a in range(n8):
    for b in range(a + 1, n8):
        B8 += v8[a] * v8[b] * (eta8[b] - eta8[a]) * (f[a] @ f[b])
c2_8 = float(np.linalg.norm(X8)) ** 2
ok8_closed = rel(A8 - (4.0 * (n8 - 1.0) / n8) * s8 * I16
                 + (4.0 / n8) * B8, A8)
ok8_master = rel(A8 + K8 @ A8 @ K8 - (c2_8 / (dim8 / 2.0)) * I16, A8)
check("F", "GENERALITY CONTROL (the 64 is not quaternion-specific): the "
           "SAME theorem holds verbatim in Cl(5,3) at n = 8, DIM = 16 "
           "(K = product of the 5 plus-legs, K^2 = I): "
           "A = (4(n-1)/n)|xi|^2 I - (4/n) B and "
           "A + K A K = (C2^2/(DIM/2)) I = (C2^2/8) I -- the constant's "
           "denominator tracks DIM/2 across reps, so 64 = DIM/2 "
           "bookkeeping, and the coefficient formulas are the general-n "
           "ones of Steps 2-4",
      float(np.max(np.abs(K8 @ K8 - I16))) < 1e-12
      and ok8_closed < 1e-11 and ok8_master < 1e-11,
      f"closed rel-res {ok8_closed:.1e}, master rel-res {ok8_master:.1e}")


# --- headline -----------------------------------------------------------------
nE = sum(1 for tag, _n, ok in RESULTS if tag == "E")
nF = sum(1 for tag, _n, ok in RESULTS if tag == "F")
nT = sum(1 for tag, _n, ok in RESULTS if tag == "T")
all_ok = all(ok for _t, _n, ok in RESULTS)
print()
print("MECHANISM VERDICT: DERIVED (paper grade, machine-corroborated "
      "stepwise). Three ingredients: Clifford completeness (Gamma Gamma^+ "
      "= 14 I), the grade-1/2 gamma contraction identities, and the fact "
      "that K_S = e_0...e_8 is the space/time reflection. They force the "
      "closed form A = (26/7)|xi|^2_E I - (2/7) xi/\\(eta xi) -- scalar "
      "plus MIXED bivector -- and mixed bivectors anticommute with K_S, "
      "so the K_S-even part of A is pure scalar. Scope: EVERY real xi "
      "(null and timelike included); constant = C2(xi)^2/64 with 64 = "
      "DIM/2 trace bookkeeping and C2^2 = (3328/7)||xi||_E^2 in closed "
      "form (new).")
print(f"HEADLINE: {nE} [E] + {nF} [F] = {nE + nF}   (setup [T] = {nT} "
      f"excluded)   {'ALL PASS' if all_ok else 'FAILURES PRESENT'}")
sys.exit(0 if all_ok else 1)
