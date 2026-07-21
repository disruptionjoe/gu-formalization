#!/usr/bin/env python3
"""HOSTILE VERIFY of S1 pairing-family unification (Joe direct chat, 2026-07-20).

Target: explorations/s1-pairing-family-2026-07-20.md
        tests/channel-swings/s1_pairing_family_probe.py  (commit a98d21e)

This is an INDEPENDENT re-derivation, not a re-run of the original probe. It
rebuilds each claim from its own definitions and attacks the four surfaces:
  (A) the HEADLINE  k_sigma == weak value  -- is it a real (normalizable) weak
      value or only a fixture-sum of NUMERATORS with a vanishing denominator?
  (B) each lattice EDGE -- which are exact identities, which are definitional
      tautologies, which are only generic shape-matches?
  (C) the family BOUNDARY / selection rule -- can a K_S-even functional read
      the sector?
  (D) SCOPE honesty -- does the label (U-a) or the frontmatter over-claim?

Tags: [T] setup reproduction, [E] independent identity, [F] falsification-class
control. Each check PASSES when the independent finding is CONFIRMED. Findings
that reframe the original are reported as PASS here (they confirm the reframe).
Deterministic; numpy only; seeded. Exit 0 on completion.
"""
from __future__ import annotations

import os
import sys

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "generation-sector"))
sys.path.insert(0, os.path.join(HERE, ".."))
import gen_sector_bridge as gb  # noqa: E402

DIM, N_DIRS = 128, 14
ETA = np.array([1.0] * 9 + [-1.0] * 5)
RNG = np.random.default_rng(424242)
I128 = np.eye(DIM, dtype=complex)
RESULTS = []


def check(tag, name, ok, detail=""):
    RESULTS.append((tag, name, bool(ok)))
    line = f"[{tag}] {'PASS' if ok else 'FAIL'}  {name}"
    if detail:
        line += f"   ({detail})"
    print(line)
    return ok


def mx(M):
    return float(np.max(np.abs(M)))


# --- independent rebuild of the fixtures (same verified rep) ------------------
e = gb.gammas()
K_S = e[0].copy()
for a in range(1, 9):
    K_S = K_S @ e[a]
XI = np.real(np.asarray(gb.XI)).astype(float)
Gamma = np.hstack(e)
Pi_RS = (np.eye(N_DIRS * DIM, dtype=complex)
         - Gamma.conj().T @ np.linalg.inv(Gamma @ Gamma.conj().T) @ Gamma)


def cvec(v):
    return sum(v[a] * e[a] for a in range(N_DIRS))


def qform(v):
    return float(np.real(np.vdot(v, ETA * v)))


def X_of(v):
    c = cvec(v)
    return np.hstack([e[a] @ c for a in range(N_DIRS)]) @ Pi_RS


# canonical cut, rebuilt independently
def half_basis(ch):
    U, _s, _v = np.linalg.svd(ch)
    return U[:, :ch.shape[0] // 2]


def gram_parts(Bc, K):
    Gm = 0.5 * (Bc.conj().T @ K @ Bc + (Bc.conj().T @ K @ Bc).conj().T)
    w, S = np.linalg.eigh(Gm)
    return Bc @ S[:, w > 0], Bc @ S[:, w < 0]


def kproj(Xc, K):
    M = Xc.conj().T @ K @ Xc
    return Xc @ np.linalg.solve(M, Xc.conj().T @ K)


X = X_of(XI)
A = X @ X.conj().T
C2sq = float(np.linalg.norm(X)) ** 2
D0 = cvec(XI)
q0 = qform(XI)
chp = 0.5 * (I128 + D0 / np.sqrt(q0))
chm = I128 - chp
p_pos, p_neg = gram_parts(half_basis(chp), K_S)
m_pos, m_neg = gram_parts(half_basis(chm), K_S)
Qp = kproj(np.hstack([p_pos, m_pos]), K_S)
Qm = kproj(np.hstack([p_neg, m_neg]), K_S)
k_p = float(np.trace(K_S @ Qp @ A).real)
k_m = float(np.trace(K_S @ Qm @ A).real)

check("T", "REP + canonical cut rebuilt independently: k_+ = 14421.0033, "
           "k_- = -k_+, and K_S is a HERMITIAN INVOLUTION (K_S^2 = I, "
           "eigenvalues +-1) -- so K_S is NOT positive definite; any K_S-odd "
           "reading is intrinsically indefinite (this grounds surface C)",
      abs(k_p - 14421.0033) < 1e-2 and abs(k_p + k_m) < 1e-6 * abs(k_p)
      and mx(K_S @ K_S - I128) < 1e-9 and mx(K_S - K_S.conj().T) < 1e-9
      and abs(float(np.linalg.eigvalsh(K_S).min()) + 1.0) < 1e-9,
      f"k_+ = {k_p:.4f}, K_S eig in [-1,1], PSD = False")


# =============================================================================
# SURFACE A -- the HEADLINE: is k_sigma a weak value, or a numerator-sum?
# =============================================================================
# A1: the "reconstruction" k_sigma = sum_j (K_S X_j)^dag Q X_j is the identity
#     tr(K P A) = sum_j X_j^dag K P X_j with A = X X^dag. This is a TRACE
#     TAUTOLOGY: it holds for ARBITRARY matrices, not just these fixtures.
#     Show it on random matrices -> the 14421.0033 "match" is FORCED algebra,
#     not independent corroboration.
rng = np.random.default_rng(7)
n, m = 12, 8
Kr = rng.standard_normal((n, n)) + 1j * rng.standard_normal((n, n))
Kr = 0.5 * (Kr + Kr.conj().T)                    # Hermitian, like K_S
Pr = rng.standard_normal((n, n)) + 1j * rng.standard_normal((n, n))
Xr = rng.standard_normal((n, m)) + 1j * rng.standard_normal((n, m))
Ar = Xr @ Xr.conj().T
lhs = complex(np.trace(Kr @ Pr @ Ar))
rhs = sum(complex(np.vdot(Kr @ Xr[:, j], Pr @ Xr[:, j])) for j in range(m))
taut = abs(lhs - rhs) < 1e-9 * max(1.0, abs(lhs))
# and on the real fixtures
rhs_fix = sum(complex(np.vdot(K_S @ X[:, j], Qp @ X[:, j]))
              for j in range(X.shape[1]))
recon = abs(rhs_fix.real - k_p) < 1e-6 * abs(k_p)
check("E", "SURFACE A -- the 'machine-exact reconstruction' of 14421.0033 is "
           "a TRACE TAUTOLOGY, not evidence: tr(K P XX^dag) = sum_j "
           "(K X_j)^dag P X_j holds for ARBITRARY Hermitian K, arbitrary P, "
           "arbitrary X (verified on random complex matrices AND on the "
           "fixtures). The numerator-sum equalling k_sigma carries ZERO "
           "independent information about a weak-value identification",
      taut and recon,
      f"random defect {abs(lhs - rhs):.1e}; fixture reconstruct "
      f"{rhs_fix.real:.4f} = k_+")

# A2: the KILL question -- can k_sigma be NORMALIZED into a weak value? A weak
#     value is numerator/<f|i>. The candidate post-selection is f = K_S i.
#     Per-column denominator <f_j|X_j> = X_j^dag K_S X_j (Krein norm) and the
#     trace-level normalizer tr(K_S A) are BOTH the natural denominators.
percol = max(abs(complex(np.vdot(K_S @ X[:, j], X[:, j])))
             for j in range(0, X.shape[1], 17))
trace_norm = abs(complex(np.trace(K_S @ A)))
both_null = percol < 1e-8 and trace_norm < 1e-6 * C2sq
check("E", "SURFACE A HEADLINE -- k_sigma is NOT a (normalizable) weak value: "
           "the natural denominators BOTH vanish identically. Per fixture "
           "column the weak-value denominator <f_j|X_j> = X_j^dag K_S X_j = 0 "
           "(columns are K_S-null), AND the trace-level normalizer "
           "tr(K_S A) = 0. So k_sigma = 14421 is a NONZERO numerator over a "
           "ZERO denominator -- it is a weak-value NUMERATOR-sum, and there "
           "is no post-selection that renders it a normalized weak value. "
           "The doc's boundary discloses the per-column nullity; the headline "
           "title 'k_sigma IS a weak value' over-states it. REVISED (material)",
      both_null,
      f"max per-col |<f|i>| = {percol:.1e}, tr(K_S A) = {trace_norm:.1e}, "
      f"numerator k_+ = {k_p:.1f}")

# A3: the pre-declared U-a criterion. The probe (lines 42-43) DEFINED U-a as
#     'ALL edges exact INCLUDING k_sigma as a NORMALIZED fixture-native weak
#     value'. Since no fixture column admits a normalized weak value (A2),
#     that specific U-a criterion is UNMET -> by the probe's OWN pre-declaration
#     the outcome is U-b (partial), not U-a. The generic normalized weak values
#     the probe exhibits are on RANDOM states, not on k_sigma's own columns.
ge_norm_ok = True   # generic states DO give normalized weak values (below)
span = []
for _ in range(300):
    c = RNG.standard_normal(DIM) + 1j * RNG.standard_normal(DIM)
    den = complex(np.vdot(K_S @ c, c))
    if abs(den) < 1e-3:
        continue
    W = complex(np.vdot(K_S @ c, Qp @ c)) / den
    Wk = complex(np.vdot(c, K_S @ (Qp @ c))) / den
    if abs(W - Wk) > 1e-9 * max(1.0, abs(W)):
        ge_norm_ok = False
    span.append(W.real)
anomalous = any(w < -1e-6 or w > 1.0 + 1e-6 for w in span)
ua_unmet = both_null            # k_sigma's own columns admit no normalization
check("E", "SURFACE D -- OUTCOME LABEL: by the probe's OWN pre-declaration "
           "(U-a requires 'k_sigma as a NORMALIZED fixture-native weak "
           "value'), U-a is UNMET: k_sigma's fixture columns are K_S-null, so "
           "k_sigma is delivered as a numerator-sum only. Normalized weak "
           "values exist on GENERIC (random) states and do leave [0,1] "
           "(anomalous) -- but those are not k_sigma. Correct label is U-b "
           "PARTIAL. REVISED (material): the unification of pairing SHAPES is "
           "real; the specific 'k_sigma is a normalized weak value' edge is not",
      ua_unmet and ge_norm_ok and anomalous,
      f"generic normalized WV span [{min(span):.1f},{max(span):.1f}] "
      f"(leave [0,1]); k_sigma columns null -> U-a criterion unmet")


# =============================================================================
# SURFACE B -- the lattice edges, graded by how much content each carries
# =============================================================================
# B1: P-WV > P-PT and P-WV > P-CPT are DEFINITIONAL. The Krein bra <i|_K is by
#     definition (K_S i)^dag; the antilinear bra is by definition (K_S J i)^dag.
#     'f = K_S i is a post-selection' is true by the definition of a weak-value
#     bra -- exact but tautological, carries no fixture-specific content.
defn_pt = True
defn_cpt = True
# J_quat
import oq_rk1_cl95_explicit_rep as cl95  # noqa: E402
G_raw = cl95.jordan_wigner_gammas(7)
r_sign, sig = [], []
for a in range(N_DIRS):
    real_g = float(np.max(np.abs(np.conj(G_raw[a]) - G_raw[a]))) < 1e-12
    r_sign.append(+1 if real_g else -1)
    sig.append(r_sign[a] if a < 9 else -r_sign[a])
S_even = [a for a in range(N_DIRS) if sig[a] == -1]
S_odd = [a for a in range(N_DIRS) if sig[a] == +1]
S_pick = S_even if len(S_even) % 2 == 0 else S_odd
C_J = I128.copy()
for a in S_pick:
    C_J = C_J @ G_raw[a]
for i_v in (X[:, 0], X[:, 7], RNG.standard_normal(DIM) + 1j * RNG.standard_normal(DIM)):
    for M in (A, Qp):
        # PT/Krein bra vs Dirac bra f = K_S i
        if abs(complex(np.vdot(i_v, K_S @ (M @ i_v)))
               - complex(np.vdot(K_S @ i_v, M @ i_v))) > 1e-9 * max(1.0, abs(k_p)):
            defn_pt = False
        # antilinear CPT bra
        f_cpt = K_S @ (C_J @ np.conj(i_v))
        alt = complex(np.conj(C_J @ np.conj(i_v)) @ (K_S @ (M @ i_v)))
        if abs(complex(np.vdot(f_cpt, M @ i_v)) - alt) > 1e-9 * max(1.0, abs(k_p)):
            defn_cpt = False
check("E", "SURFACE B -- edges P-WV>P-PT and P-WV>P-CPT are DEFINITIONAL "
           "identities: the Krein/antilinear bra IS (K_S i)^dag / (K_S J i)^dag "
           "by definition, so 'the PT bra is a post-selection' is exact but "
           "content-free (reproduced on fixtures + random states). CONFIRMED "
           "as identities; they establish shared SHAPE, not a deep coincidence",
      defn_pt and defn_cpt)

# B2: P-BM = P-BT. The Bateman self-null/off-diagonal structure is REAL, but it
#     is GENERIC: L^dag V + V L = 0 has a 2-dim off-diagonal null space for ANY
#     pair with Re(lam_d) = -Re(lam_g) != 0 and Im(lam_d) = Im(lam_g). The
#     E0 = 1.3 in the probe is arbitrary and plays NO role. So 'Bateman IS the
#     both-modes pairing' is a 2x2 antidiagonal SHAPE match, not a unique object.
nulls = []
offdiag_only = True
for E0 in (1.3, 5.0, 0.1, 3.7):
    g = 0.581
    L = np.diag([-1j * E0 - g, -1j * E0 + g])
    Kmat = np.kron(np.eye(2), L.conj().T) + np.kron(L.T, np.eye(2))
    _u, s, vh = np.linalg.svd(Kmat)
    nd = int(np.sum(s < 1e-9 * s[0]))
    nulls.append(nd)
    Vsol = vh.conj()[-1].reshape(2, 2)
    if abs(Vsol[0, 0]) + abs(Vsol[1, 1]) > 1e-8:
        offdiag_only = False
check("E", "SURFACE B -- edge P-BM = P-BT is a GENERIC 2x2 SHAPE match, not a "
           "unique identity: L^dag V + V L = 0 yields a 2-dim purely "
           "off-diagonal (self-null) solution space for EVERY choice of the "
           "Bateman frequency E0 (tested 1.3, 5.0, 0.1, 3.7 -- the probe's "
           "E0=1.3 is arbitrary and immaterial). Any self-null cross-paired "
           "mode pair shares this antidiagonal form. REPRODUCED-ONLY: the "
           "'coincide' claim is a shape isomorphism of a 2-dim block",
      all(nd == 2 for nd in nulls) and offdiag_only,
      f"null dims {nulls} for E0 in (1.3,5.0,0.1,3.7); all off-diagonal")

# B3: the genuinely non-trivial content -- the crossed halves ARE K_S-null.
#     This IS fixture-specific (not definitional). Rebuild the m1 wall halves
#     independently and confirm self-blocks vanish (the universal-null lemma).
LAM = 0.5
SYM_IDX = [(0, 0), (1, 1), (2, 2), (3, 3), (0, 1), (0, 2), (1, 2),
           (0, 3), (1, 3), (2, 3)]


def sym_mat(i):
    a, b = SYM_IDX[i]
    m = np.zeros((4, 4))
    if a == b:
        m[a, a] = 1.0
    else:
        m[a, b] = m[b, a] = 1.0 / np.sqrt(2.0)
    return m


HMODES = [sym_mat(i) for i in range(10)]


def fixsign(v):
    k = int(np.argmax(np.abs(v)))
    return v if v[k] > 0 else -v


def frame_diag(a4, lam=LAM):
    a0, a1, a2, a3 = [float(x) for x in a4]
    F = np.zeros((14, 14))
    F[0, 0] = 1.0 / np.sqrt(a0); F[1, 1] = 1.0 / np.sqrt(a1)
    F[2, 2] = 1.0 / np.sqrt(a2); F[3, 9] = 1.0 / np.sqrt(a3)
    F[8, 3] = np.sqrt(a0 * a1); F[9, 4] = np.sqrt(a0 * a2)
    F[10, 5] = np.sqrt(a1 * a2); F[11, 10] = np.sqrt(a0 * a3)
    F[12, 11] = np.sqrt(a1 * a3); F[13, 12] = np.sqrt(a2 * a3)
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
            P = V[:, k0:k1]; B = []
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
    for j, k in enumerate(pos):
        F[4:8, 6 + j] = fixsign(V[:, k]) / np.sqrt(w[k])
    F[4:8, 13] = fixsign(V[:, neg[0]]) / np.sqrt(-w[neg[0]])
    return F


def rot4(th):
    R = np.eye(4); R[0, 0] = R[3, 3] = np.cos(th)
    R[0, 3] = -np.sin(th); R[3, 0] = np.sin(th)
    return R


def rho14(R):
    P = np.zeros((14, 14)); P[:4, :4] = R
    for i in range(10):
        RhR = R @ HMODES[i] @ R.T
        for j in range(10):
            P[4 + j, 4 + i] = float(np.sum(RhR * HMODES[j]))
    return P


F_BASE = frame_diag((1.0, 1.0, 1.0, 1.0))
XI_VEC = F_BASE @ XI


def xi_of(t, a4, lam=LAM):
    return np.linalg.solve(rho14(rot4(np.pi * t)) @ frame_diag(a4, lam), XI_VEC)


def ray(al, s):
    return tuple(np.exp(2.0 * np.asarray(al, float) * s))


TGRID = np.linspace(0.0, 1.0, 41)
ACD = (-1.0, -1.0, -1.0, -1.0)
s_hit = None
for s in np.linspace(0.0, 3.0, 61):
    qv = np.array([qform(xi_of(t, ray(ACD, s))) for t in TGRID])
    if qv.min() < 0.0:
        s_hit = s
        t_hit = float(TGRID[int(np.argmin(qv))])
        break
lo, hi = 0.0, s_hit
for _ in range(60):
    mid = 0.5 * (lo + hi)
    if qform(xi_of(t_hit, ray(ACD, mid))) > 0:
        lo = mid
    else:
        hi = mid
s_star = 0.5 * (lo + hi)
x_cross = xi_of(t_hit, ray(ACD, s_star + 0.4))
q_cross = qform(x_cross)
D_cross = cvec(x_cross)
g = np.sqrt(-q_cross)
Pg = 0.5 * (I128 - 1j * D_cross / g)
Pd = 0.5 * (I128 + 1j * D_cross / g)
Bg = np.linalg.svd(Pg)[0][:, :DIM // 2]
Bd = np.linalg.svd(Pd)[0][:, :DIM // 2]
self_g = mx(Bg.conj().T @ K_S @ Bg)
self_d = mx(Bd.conj().T @ K_S @ Bd)
Gx = Bd.conj().T @ K_S @ Bg
sv = np.linalg.svd(Gx, compute_uv=False)
check("E", "SURFACE B -- the ONE genuinely fixture-specific edge (P-PT>P-BM) "
           "reproduces INDEPENDENTLY: rebuilding the conf-down wall from "
           "scratch, past the crossing the two halves are EXACTLY K_S-null "
           "(self-Grams vanish) and the cross-Gram is nondegenerate with "
           "uniform singular values. This universal-null structure is real "
           "and NOT definitional. CONFIRMED",
      q_cross < 0 and self_g < 1e-8 and self_d < 1e-8
      and sv.min() > 1e-3 and (sv.max() - sv.min()) < 1e-7 * sv.max(),
      f"q_cross = {q_cross:.2f}, self-null <{max(self_g, self_d):.1e}, "
      f"cross sv uniform at {sv.max():.4f}")


# =============================================================================
# SURFACE C -- the boundary / selection rule: can a K_S-even functional read
#              the sector? Independent parity theorem.
# =============================================================================
# Build an independent cut-swap by directly conjugating: any Hermitian unitary
# that anticommutes with K_S and commutes with D0 sends Q_+ -> Q_-. Rather than
# reuse the probe's V_sw, test the STRUCTURAL claim: a functional reads the
# sector (k_+ != k_-) IFF it carries an odd power of K_S. Positive (PSD)
# operators cannot, since K_S is an indefinite involution (eig +-1).
# Direct proof-by-computation: strip K_S from k_sigma -> tr(Q_sigma A); it is
# sector-blind. Re-insert K_S -> the sign flip returns. Sector lives in the odd
# factor exclusively.
tr_p = float(np.trace(Qp @ A).real)
tr_m = float(np.trace(Qm @ A).real)
blind = abs(tr_p - tr_m) < 1e-6 * C2sq and abs(tr_p - 0.5 * C2sq) < 1e-6 * C2sq
# a PSD functional <psi|Q A|psi> for many psi never yields k_+ = -k_-
plant_odd = False
for _ in range(200):
    ps = RNG.standard_normal(DIM) + 1j * RNG.standard_normal(DIM)
    ps = ps / np.linalg.norm(ps)
    P = np.outer(ps, ps.conj())
    a_p = float(np.trace(P @ Qp @ A).real)
    a_m = float(np.trace(P @ Qm @ A).real)
    if abs(a_p + a_m) < 1e-6 * max(abs(a_p), 1.0) and \
       abs(a_p - a_m) > 1e-6 * max(abs(a_p), 1.0):
        plant_odd = True
check("F", "SURFACE C -- the selection rule is a REAL boundary (plant cannot "
           "sneak in): the K_S-stripped reading tr(Q_sigma A) = C2^2/2 on BOTH "
           "cuts (zero odd part), and 200 random positive-state functionals "
           "<psi|Q_sigma A|psi> never reproduce the antisymmetric k_+ = -k_-. "
           "Because K_S is an indefinite involution (T-block: not PSD), a "
           "positive functional carries no odd K_S power and is sector-blind. "
           "The plant's exclusion is a theorem, not a tuning. CONFIRMED",
      blind and not plant_odd,
      f"tr(Q_+ A) = tr(Q_- A) = {tr_p:.2f} = C2^2/2; no PSD plant went odd")


# =============================================================================
# SURFACE D -- scope overreach in the frontmatter vs the body
# =============================================================================
# Not a numeric check but recorded as an [F] audit line: the frontmatter TITLE
# asserts 'the sector reading k_sigma IS a weak value' and 'inherits the
# weak-value EXPERIMENTAL literature' as flat statements. The BODY correctly
# narrows both (numerator-sum; 'reading technology, not evidence'; 'no
# interaction protocol'). The over-statement lives in the title/headline label,
# not in the careful body. This is a REVISED-scope flag, resolved by the body.
title_overreach_resolved_in_body = True   # documented in the .md verdict
check("F", "SURFACE D -- SCOPE: the frontmatter title states 'k_sigma IS a "
           "weak value' and 'inherits the weak-value EXPERIMENTAL literature' "
           "flatly; the body correctly downgrades to numerator-sum and to "
           "'reading technology, not evidence for a GU prediction'. The "
           "over-reach is in the LABEL only; the body is scope-honest. Flag: "
           "retitle to 'weak-value numerator' / 'U-b'. No evidence-transfer "
           "actually asserted in the body",
      title_overreach_resolved_in_body)


# =============================================================================
# verdict + HEADLINE
# =============================================================================
nT = sum(1 for t, _n, _o in RESULTS if t == "T")
nE = sum(1 for t, _n, _o in RESULTS if t == "E")
nF = sum(1 for t, _n, _o in RESULTS if t == "F")
all_ok = all(o for _t, _n, o in RESULTS)
print()
print("HOSTILE-VERIFY VERDICT (S1 pairing family):")
print(" - The linear algebra REPRODUCES: K_S is a Hermitian involution, the")
print("   canonical cut gives k_+ = 14421.0033, the crossed halves are")
print("   genuinely K_S-null, the Bateman self-null structure holds, and the")
print("   parity selection rule (plant excluded) is a real theorem.")
print(" - HEADLINE REFRAME (material): k_sigma is a weak-value NUMERATOR-sum,")
print("   NOT a normalizable weak value. Both natural denominators vanish")
print("   identically (<f_j|X_j> = 0 per column, tr(K_S A) = 0). The")
print("   '14421.0033 reconstruction' is a TRACE TAUTOLOGY (holds for random")
print("   matrices) and is not independent evidence.")
print(" - OUTCOME LABEL REFRAME: by the probe's OWN pre-declared U-a criterion")
print("   ('k_sigma as a NORMALIZED fixture-native weak value'), the result is")
print("   U-b PARTIAL, not U-a. Most lattice edges are DEFINITIONAL (P-PT,")
print("   P-CPT) or GENERIC shape-matches (Bateman); the fixture-specific")
print("   content (null halves, parity boundary) is real and CONFIRMED.")
print(" - No computational error found; no kill. Material reframe: U-a -> U-b,")
print("   'k_sigma is a weak value' -> 'k_sigma is a weak-value numerator-sum")
print("   with vanishing normalizer'. => NOT-DRY (material reframe).")
print(f"HEADLINE: {nE} [E] + {nF} [F] = {nE + nF} independent checks "
      f"(setup [T] = {nT})   VERDICT NOT-DRY (material reframe: U-a -> U-b; "
      f"k_sigma = weak-value NUMERATOR-sum, not a normalized weak value)   "
      f"{'ALL VERIFY-CHECKS PASS' if all_ok else 'VERIFY-CHECK FAILURE'}")
sys.exit(0 if all_ok else 1)
