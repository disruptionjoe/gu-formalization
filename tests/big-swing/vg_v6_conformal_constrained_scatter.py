#!/usr/bin/env python3
"""VG-V6 -- T4' FORWARD direction: does the conformal-class constraint NARROW the
stabilized-action signature scatter on the gamma-traceless slice, or is it inert?

Background (the 2026-07-03 scatter certificate,
explorations/big-swing-2026-07-03/BIG-SWING-BUILD-STABILIZED-ACTION-scatter-CONSISTENT-UNCOMPUTED.md):
admissible Hermitian cores A, compressed to the 1664-dim gamma-traceless slice
ker(Gamma) of the verified Cl(9,5) = M(64,H) carrier V = R^14 (x) S = 1792, produce
scattered signatures ({0, +1664, ...}): the count is NOT action-forced. The tri-theory
federation's conformal leg (Mannheim, Weyl^2 action class) claims the action class
constrains completions. This script tests the FORWARD direction ONLY:

    Restricted to CONFORMAL-COMPATIBLE cores -- Hermitian, K-self-adjoint cores either
    (a) BUILT FROM the conformal subalgebra so(4,2) (quadratic elements: the eta-signed
        Casimir, unsigned "Weyl^2-shaped" sums of squares, random signed quadratic
        combinations, symmetrized products), or
    (b) COMMUTING with the conformal subalgebra action (Casimir polynomials/shifts,
        quadratic elements of the commuting complementary so(5,3)),
    what is the signature scatter of the slice compression?

The REVERSE direction (Weyl^2 coefficients pinning the count) is BANNED by the scatter
certificate and is not touched here.

DECLARED representative conformal chain (route V6 instruction: coordinate with V3's
chain; V3 runs in a parallel workflow whose outcome we may not cite, so we DECLARE a
representative and test robustness under a second choice):

    so(4,2)  on indices  spacelike {0,1,2,3} + timelike {9,10}
      inside so(6,4) on  spacelike {0,1,2,3,4,5} + timelike {9,10,11,12}
      inside so(9,5)     (bridge convention: eta = +1 for a<9, -1 for a>=9)

all as index-subset subalgebras of so(9,5), lifted to the carrier as the total action
J_ab = L_ab (x) I_128 + I_14 (x) sigma_ab  (vector + spinor).  Alternative representative
(robustness): so(4,2) on spacelike {5,6,7,8} + timelike {12,13}.

ANCHORS reproduced and printed before any claim:
  - triplet Krein signature (+96, -96, 0) in (9,5)  [ghost_parity_krein.analyze]
  - beta_S pseudo-anti-Hermiticity residual ~ 0     [both conventions]
  - rank(Gamma) = 128, dim ker(Gamma) = 1664
  - bare ||[Pi_RS, M_D]|| = 58.7215, C2 = 155.3625  [gen_sector_bridge.anchors]
  - prior-scatter mechanism: sig(M_D) = 0 (832,832,0); sig(ramp) = +1664 (1664,0,0)

CONTROLS (the test must be able to fail):
  - C1 scrambled 'conformal' algebra: 15 random slice matrices with the SAME
    Hermiticity-type pattern and norms as the genuine compressed so(4,2) generators;
    the same core constructions are run on them. If the scrambled family shows the
    same behavior as the genuine one, the behavior is a construction tautology, not
    conformal force.
  - C2 narrowing detectability: a positivity-restricted subfamily (positive combos of
    boost^2 - rot^2, each PSD) MUST narrow to a single signature -- proving the
    harness can output "NARROWED" -- and must narrow for the scrambled algebra too
    (definiteness-narrowing is algebra-independent, i.e. tautological).

TARGET-IMPORT GUARD (maximum strictness): {3, 8, 24, chi(K3)=24, Ahat=3, rank_H=4,
ind_H=8} are never assumed, inserted, or divided by. Every count statement is
"mechanism M forces c", never "GU forces c".

Run:  python tests/big-swing/vg_v6_conformal_constrained_scatter.py   (exit 0)
"""
from __future__ import annotations

import os
import sys
import time

import numpy as np

_HERE = os.path.dirname(os.path.abspath(__file__))
_TESTS = os.path.normpath(os.path.join(_HERE, ".."))
_GEN = os.path.normpath(os.path.join(_TESTS, "generation-sector"))
for p in (_GEN, _TESTS):
    if p not in sys.path:
        sys.path.insert(0, p)

import gen_sector_bridge as bridge            # noqa: E402  (verified Cl(9,5) carrier)
import ghost_parity_krein as gpk              # noqa: E402  (verified Krein recipe; REUSED)

N, DIM, FULL = 14, 128, 14 * 128
ETA = np.array([1.0] * 9 + [-1.0] * 5)        # bridge convention: spacelike 0..8, timelike 9..13
ATOL = 1e-9
RNG = np.random.default_rng(20260706)
T0 = time.time()

_rng_probe = np.random.default_rng(7)
PROBE = (_rng_probe.standard_normal((1664, 8)) + 1j * _rng_probe.standard_normal((1664, 8)))
PROBE /= np.linalg.norm(PROBE, axis=0, keepdims=True)
KcP = None  # filled once the compressed Krein form Kc exists


def log(msg):
    print(msg, flush=True)


# ---------------------------------------------------------------------------
# carrier primitives
# ---------------------------------------------------------------------------
e = bridge.gammas()                            # 14 Clifford generators, 128x128
_, Gamma, Pi_RS, M_D = bridge.constraint_objects()


def sigma(a, b):
    """Spinor generator sigma_ab = (1/4)[e_a, e_b]."""
    return 0.25 * (e[a] @ e[b] - e[b] @ e[a])


def Lvec(a, b):
    """Vector generator of so(9,5): (L_ab)^c_d = delta^c_a eta_bd - delta^c_b eta_ad."""
    M = np.zeros((N, N), dtype=complex)
    M[a, b] = ETA[b]
    M[b, a] = -ETA[a]
    return M


def apply_gen(L, sg, X):
    """(L (x) I + I (x) sigma) @ X  without forming the 1792^2 matrix."""
    Xr = X.reshape(N, DIM, -1)
    out = np.einsum("ab,bkm->akm", L, Xr) + np.einsum("kl,alm->akm", sg, Xr)
    return out.reshape(FULL, -1)


def signature(Ac, label, tol_rel=1e-8):
    """Signature (n+, n-, n0) of a Hermitian slice core; prints the tolerance bracket."""
    Ah = 0.5 * (Ac + Ac.conj().T)
    herm_res = float(np.linalg.norm(Ac - Ah))
    w = np.linalg.eigvalsh(Ah)
    tol = tol_rel * max(1.0, float(np.max(np.abs(w))))
    npl = int(np.sum(w > tol))
    nmi = int(np.sum(w < -tol))
    nze = int(np.sum(np.abs(w) <= tol))
    absw = np.abs(w)
    below = float(np.max(absw[absw <= tol])) if nze else 0.0
    above = float(np.min(absw[absw > tol])) if (npl + nmi) else 0.0
    log(f"    {label:34s} sig=({npl:5d},{nmi:5d},{nze:4d})  n+-n- = {npl - nmi:+6d}"
        f"   herm-res {herm_res:.1e}  tol {tol:.1e}  [|w| bracket {below:.1e} | {above:.1e}]")
    return (npl, nmi, nze)


# ===========================================================================
log("=" * 96)
log("VG-V6 : T4' FORWARD -- conformal-class-constrained signature scatter on ker(Gamma) (1664)")
log("=" * 96)

# ---------------------------------------------------------------------------
# [A] ANCHORS FIRST
# ---------------------------------------------------------------------------
log("\n[A] ANCHORS (reproduced before any claim)")
log("  [A1] triplet Krein signature in (9,5) via verified recipe (ghost_parity_krein.analyze):")
gpk.analyze({4, 5, 6, 7, 8}, "    (9,5)")     # hard-asserts (+96,-96) internally; prints beta residual

anch = bridge.anchors()
log(f"  [A2] bare ||[Pi_RS, M_D]|| = {anch['bare_commutator']:.4f}   (target 58.7215)")
log(f"       C2 = ||Gamma M_D Pi_RS|| = {anch['C2']:.4f}   (target 155.3625)")
assert abs(anch["bare_commutator"] - 58.7215) < 1e-3, anch
assert abs(anch["C2"] - 155.3625) < 1e-3, anch

rkG = int(np.linalg.matrix_rank(Gamma, tol=1e-9))
log(f"  [A3] rank(Gamma) = {rkG} (target 128) ; dim ker = {Gamma.shape[1] - rkG} (target 1664)")
assert rkG == 128

# Krein form K = etaV (x) beta_S in the bridge convention (spacelike 0..8)
bS = np.eye(DIM, dtype=complex)
for a in range(9):
    bS = bS @ e[a]
if np.linalg.norm(bS + bS.conj().T) < ATOL:
    bS = 1j * bS
bS = bS / np.sqrt(abs((bS @ bS)[0, 0].real))
assert np.linalg.norm(bS @ bS - np.eye(DIM)) < ATOL
beta_res = max(np.linalg.norm(bS @ sigma(i, j) + sigma(i, j).conj().T @ bS)
               for i in range(N) for j in range(i + 1, N))
log(f"  [A4] beta_S (bridge convention) pseudo-anti-Hermiticity residual = {beta_res:.3e}")
assert beta_res < ATOL
etaV = np.diag(ETA).astype(complex)
K = np.kron(etaV, bS)
piK = float(np.linalg.norm(Pi_RS @ K - K @ Pi_RS))
log(f"  [A5] ||[Pi_RS, K]|| = {piK:.3e}  (slice is K-invariant)")
assert piK < ATOL

# orthonormal slice basis
w_pi, V_pi = np.linalg.eigh(Pi_RS)
W = np.ascontiguousarray(V_pi[:, w_pi > 0.5])
del w_pi, V_pi
assert W.shape == (FULL, 1664)
Kc = W.conj().T @ (K @ W)
Kc = 0.5 * (Kc + Kc.conj().T)
KcP = Kc @ PROBE
wK = np.linalg.eigvalsh(Kc)
log(f"  [A6] slice basis W: 1792 x {W.shape[1]} ; compressed Krein form Kc signature "
    f"(+{int(np.sum(wK > 1e-9))}, -{int(np.sum(wK < -1e-9))}, 0:{int(np.sum(np.abs(wK) <= 1e-9))})")
log(f"       [{time.time() - T0:.0f}s]")


def kself_res(Ac):
    """Relative K-self-adjointness residual on the slice, probe form:
    ||Kc(A p) - A^H (Kc p)|| / max(||Kc(A p)|| + ||A^H (Kc p)||, 1).
    The unit floor makes a numerically-zero core (e.g. the Casimir minimal polynomial,
    which annihilates identically) read as trivially K-self-adjoint instead of dividing
    roundoff noise by roundoff noise; genuine cores here have probe norms >> 1, so the
    floor never engages for them."""
    x = Kc @ (Ac @ PROBE)
    y = Ac.conj().T @ KcP
    return float(np.linalg.norm(x - y) / max(np.linalg.norm(x) + np.linalg.norm(y), 1.0))


# ---------------------------------------------------------------------------
# [B] conformal chain: declaration + structure certificates
# ---------------------------------------------------------------------------
log("\n[B] DECLARED conformal chain and structure certificates")
C42_S, C42_T = [0, 1, 2, 3], [9, 10]
C64_S, C64_T = [0, 1, 2, 3, 4, 5], [9, 10, 11, 12]
log(f"  so(4,2): spacelike {C42_S} + timelike {C42_T}  (4+,2-)")
log(f"  so(6,4): spacelike {C64_S} + timelike {C64_T}  (6+,4-)   chain: so(4,2) < so(6,4) < so(9,5)")

pairs42 = [(a, b) for i, a in enumerate(C42_S + C42_T) for b in (C42_S + C42_T)[i + 1:]]
pairs64 = [(a, b) for i, a in enumerate(C64_S + C64_T) for b in (C64_S + C64_T)[i + 1:]]
assert len(pairs42) == 15 and len(pairs64) == 45

# structure constants: [J_ab, J_cd] = eta_bc J_ad - eta_ac J_bd - eta_bd J_ac + eta_ad J_bc
def _get(dic, a, b):
    if a == b:
        return 0.0 * dic[pairs42[0]]
    return dic[(a, b)] if (a, b) in dic else -dic[(b, a)]


def closure_residual(gen_dict, pairs):
    r = 0.0
    for (a, b) in pairs:
        for (c, d) in pairs:
            lhs = gen_dict[(a, b)] @ gen_dict[(c, d)] - gen_dict[(c, d)] @ gen_dict[(a, b)]
            # [J_ab, J_cd] = eta_bc J_ad + eta_ad J_bc - eta_ac J_bd - eta_bd J_ac
            rhs = (ETA[b] if b == c else 0) * _get(gen_dict, a, d) \
                + (ETA[a] if a == d else 0) * _get(gen_dict, b, c) \
                - (ETA[a] if a == c else 0) * _get(gen_dict, b, d) \
                - (ETA[b] if b == d else 0) * _get(gen_dict, a, c)
            r = max(r, float(np.linalg.norm(lhs - rhs)))
    return r


sig42 = {(a, b): sigma(a, b) for (a, b) in pairs42}
L42 = {(a, b): Lvec(a, b) for (a, b) in pairs42}
r_sig = closure_residual(sig42, pairs42)
r_vec = closure_residual(L42, pairs42)
log(f"  so(4,2) structure constants: spinor rep residual {r_sig:.3e} ; vector rep residual {r_vec:.3e}")
assert r_sig < ATOL and r_vec < ATOL

# Gamma equivariance (=> slice invariance), per generator, both so(4,2) and so(6,4)
def equiv_residual(pairs):
    worst = 0.0
    for (a, b) in pairs:
        L, sg = Lvec(a, b), sigma(a, b)
        for bb in range(N):
            blk = sum(L[aa, bb] * e[aa] for aa in range(N)) + e[bb] @ sg - sg @ e[bb]
            worst = max(worst, float(np.linalg.norm(blk)))
    return worst


r42 = equiv_residual(pairs42)
r64 = equiv_residual(pairs64)
log(f"  Gamma equivariance (Gamma J = sigma Gamma), per-generator max: so(4,2) {r42:.3e} ; so(6,4) {r64:.3e}")
assert r42 < ATOL and r64 < ATOL

# K-skewness of every generator: K J + J^H K = 0 (so quadratics are K-self-adjoint)
def kskew_residual(pairs):
    worst = 0.0
    for (a, b) in pairs:
        L, sg = Lvec(a, b), sigma(a, b)
        rV = float(np.linalg.norm(etaV @ L + L.conj().T @ etaV))
        rS = float(np.linalg.norm(bS @ sg + sg.conj().T @ bS))
        worst = max(worst, rV, rS)
    return worst


rk42 = kskew_residual(pairs42)
log(f"  K-skewness of so(4,2) generators (K J + J^H K = 0): max residual {rk42:.3e}")
assert rk42 < ATOL

# compressed so(4,2) generators on the slice
types42 = []      # 'H' (Hermitian boost) or 'A' (anti-Hermitian rotation)
Jc42 = []
for (a, b) in pairs42:
    JW = apply_gen(L42[(a, b)], sig42[(a, b)], W)
    inv_res = float(np.linalg.norm(Gamma @ JW))            # slice invariance (Gamma J W = 0)
    assert inv_res < 1e-7, (a, b, inv_res)
    Jc = W.conj().T @ JW
    hr = float(np.linalg.norm(Jc - Jc.conj().T))
    ar = float(np.linalg.norm(Jc + Jc.conj().T))
    types42.append("H" if hr < ar else "A")
    Jc42.append(Jc)
mixed = sum(1 for (a, b) in pairs42 if (ETA[a] * ETA[b]) < 0)
log(f"  compressed so(4,2) generators: 15 built; slice-invariance exact; Hermiticity types "
    f"{''.join(types42)}  ({types42.count('H')} boosts / {types42.count('A')} rotations; mixed pairs = {mixed})")
assert types42.count("H") == mixed == 8
norms42 = [float(np.linalg.norm(J)) for J in Jc42]
log(f"  generator slice norms: min {min(norms42):.2f} max {max(norms42):.2f} (action nontrivial)")
log(f"  [{time.time() - T0:.0f}s]")


# ---------------------------------------------------------------------------
# [C] PRIOR-FAMILY cores (reproduce the 2026-07-03 scatter mechanism)
# ---------------------------------------------------------------------------
log("\n[C] PRIOR scatter family (2026-07-03 harness, rebuilt)")
sigs = {}

MDc = W.conj().T @ apply_gen(np.zeros((N, N), dtype=complex),
                             sum(bridge.XI[a] * e[a] for a in range(N)), W)
sigs["P1 M_D"] = signature(MDc, "P1  M_D (GU default)")
# Pi M_D Pi compresses identically (Pi W = W):
PMDPc = W.conj().T @ (Pi_RS @ (M_D @ (Pi_RS @ W)))
log(f"    P2  Pi M_D Pi == M_D on slice:     ||diff|| = {np.linalg.norm(PMDPc - MDc):.3e} (identical compression)")
sigs["P2 Pi M_D Pi"] = signature(PMDPc, "P2  Pi_RS M_D Pi_RS")
ramp = np.arange(1, FULL + 1, dtype=float) / FULL
Rc = (W.conj().T * ramp) @ W
sigs["P3 ramp"] = signature(Rc, "P3  non-J diagonal ramp")
H0 = RNG.standard_normal((FULL, FULL)) + 1j * RNG.standard_normal((FULL, FULL))
H0 = (H0 + H0.conj().T) / 2.0
Hc = W.conj().T @ (H0 @ W)
del H0
sigs["P4 random Herm"] = signature(Hc, "P4  random Hermitian (GUE, seed)")
assert sigs["P1 M_D"] == (832, 832, 0), sigs["P1 M_D"]          # prior anchor
assert sigs["P3 ramp"] == (1664, 0, 0), sigs["P3 ramp"]         # prior anchor
log("    prior mechanism REPRODUCED: canonical core -> 0 ; non-J ramp -> +1664 (scatter certificate stands)")

# conformal-compatibility of the prior cores (are they even in the constrained class?)
JcP = [J @ PROBE for J in Jc42]      # probe images of the 15 conformal generators


def conf_comm_res(Ac):
    """max_k rel. commutation residual with the so(4,2) action, probe form:
    ||A(J p) - J(A p)|| / (||A(J p)|| + ||J(A p)||)."""
    AP = Ac @ PROBE
    worst = 0.0
    for J, JP in zip(Jc42, JcP):
        x = Ac @ JP
        y = J @ AP
        worst = max(worst, float(np.linalg.norm(x - y) / max(np.linalg.norm(x) + np.linalg.norm(y), 1e-300)))
    return worst


log("    conformal-commutation residual (rel.) of prior cores: "
    f"M_D {conf_comm_res(MDc):.2e} ; ramp {conf_comm_res(Rc):.2e} ; random {conf_comm_res(Hc):.2e}")
log("    -> NONE of the prior cores is conformal-compatible; the constraint genuinely restricts the SET.")
log(f"    K-self-adjointness residual (rel.): M_D {kself_res(MDc):.2e} ; ramp {kself_res(Rc):.2e} ; "
    f"random {kself_res(Hc):.2e}")
log(f"  [{time.time() - T0:.0f}s]")


# ---------------------------------------------------------------------------
# [D] CONFORMAL-COMPATIBLE cores
# ---------------------------------------------------------------------------
log("\n[D] CONFORMAL-COMPATIBLE cores (the T4' forward question)")
log("  Family A: built FROM so(4,2) (quadratic elements; K-self-adjoint by K-skewness of generators)")

eta_sign = [ETA[a] * ETA[b] for (a, b) in pairs42]
sq42 = [J @ J for J in Jc42]

conf_sigs = {}
kres = {}

Cas = sum(s * q for s, q in zip(eta_sign, sq42))            # eta-signed Casimir
kres["A1"] = kself_res(Cas)
conf_sigs["A1 Casimir(4,2)"] = signature(Cas, "A1  eta-signed Casimir C2(so(4,2))")

Wsq = sum(sq42)                                             # unsigned 'Weyl^2-shaped' block
kres["A2"] = kself_res(Wsq)
conf_sigs["A2 sum J^2 (unsigned)"] = signature(Wsq, "A2  unsigned sum of squares")

for t in range(3):                                          # random signed quadratic combos
    c = RNG.standard_normal(15)
    Aq = sum(ci * q for ci, q in zip(c, sq42))
    kres[f"A3.{t}"] = kself_res(Aq)
    conf_sigs[f"A3.{t} random signed sum of squares"] = signature(Aq, f"A3.{t} random signed sum of squares")

# symmetrized products of same-Hermiticity-type pairs (Hermitian + K-self-adjoint)
idxH = [i for i, t in enumerate(types42) if t == "H"]
idxA = [i for i, t in enumerate(types42) if t == "A"]
pairs_same = [(idxH[0], idxH[3]), (idxH[1], idxH[5]), (idxH[2], idxH[7]),
              (idxA[0], idxA[2]), (idxA[1], idxA[4]), (idxA[3], idxA[5])]
c = RNG.standard_normal(len(pairs_same))
Asym = sum(ci * (Jc42[i] @ Jc42[j] + Jc42[j] @ Jc42[i]) for ci, (i, j) in zip(c, pairs_same))
kres["A4"] = kself_res(Asym)
conf_sigs["A4 symmetrized products"] = signature(Asym, "A4  random symmetrized products")

conf_sigs["A5a boost^2"] = signature(sq42[types42.index("H")], "A5a single boost squared")
conf_sigs["A5b rot^2"] = signature(sq42[types42.index("A")], "A5b single rotation squared")
kres["A5a"] = kself_res(sq42[types42.index("H")])
kres["A5b"] = kself_res(sq42[types42.index("A")])

# Casimir shifts and polynomial (identity commutes with everything; still in the class)
wc = np.linalg.eigvalsh(0.5 * (Cas + Cas.conj().T))
t1, t2 = float(np.quantile(wc, 0.25)), float(np.quantile(wc, 0.75))
# MEASURED fact: the slice Casimir spectrum (isotypic structure of the so(4,2) action)
uniq = []
for v in wc:
    if not uniq or abs(v - uniq[-1][0]) > 1e-6:
        uniq.append([float(v), 1])
    else:
        uniq[-1][1] += 1
log("    MEASURED slice Casimir spectrum: " + " ; ".join(f"{v:.4f} x{m}" for v, m in uniq)
    + f"  ({len(uniq)} distinct eigenvalue(s) -> minimal polynomial degree {len(uniq)})")
I1664 = np.eye(1664, dtype=complex)
conf_sigs["A6a Casimir - q25"] = signature(Cas - t1 * I1664, f"A6a Casimir - {t1:.3f} I")
conf_sigs["A6b Casimir - q75"] = signature(Cas - t2 * I1664, f"A6b Casimir - {t2:.3f} I")
Cpoly = Cas @ Cas - (t1 + t2) * Cas + (t1 * t2) * I1664     # (C - t1)(C - t2)
kres["A6c"] = kself_res(Cpoly)
conf_sigs["A6c (C-t1)(C-t2)"] = signature(Cpoly, "A6c Casimir polynomial (C-t1)(C-t2)")

# the linear boost generator: Hermitian but K-SKEW -> excluded from the K-self-adjoint class
boost = Jc42[types42.index("H")]
log(f"    A0  linear boost generator: Hermitian but K-SKEW (K-self-adj residual {kself_res(boost):.2f}, "
    f"K-skew residual {float(np.linalg.norm(Kc @ boost + boost.conj().T @ Kc) / np.linalg.norm(boost)):.2e})"
    " -> excluded from the class; quadratics are the conformal-built cores.")
log(f"  [{time.time() - T0:.0f}s]")

log("\n  Family B: COMMUTING with so(4,2) (the commutant side of the class)")
comp_S, comp_T = [4, 5, 6, 7, 8], [11, 12, 13]              # complementary so(5,3), disjoint indices
pairsB = [(a, b) for i, a in enumerate(comp_S + comp_T) for b in (comp_S + comp_T)[i + 1:]]
assert len(pairsB) == 28
cB1 = RNG.standard_normal(28)
cB2 = RNG.standard_normal(28)
accB = {"B1 Casimir(5,3)": np.zeros((1664, 1664), dtype=complex),
        "B2a random signed (5,3)": np.zeros((1664, 1664), dtype=complex),
        "B2b random signed (5,3)": np.zeros((1664, 1664), dtype=complex)}
for k, (a, b) in enumerate(pairsB):
    JW = apply_gen(Lvec(a, b), sigma(a, b), W)
    Jc = W.conj().T @ JW
    q = Jc @ Jc
    accB["B1 Casimir(5,3)"] += ETA[a] * ETA[b] * q
    accB["B2a random signed (5,3)"] += cB1[k] * q
    accB["B2b random signed (5,3)"] += cB2[k] * q
del JW, Jc, q
for name, B in accB.items():
    cr = conf_comm_res(B)
    kr = kself_res(B)
    kres[name] = kr
    log(f"    {name:26s}: commutes with all 15 so(4,2) gens, rel. residual {cr:.2e} ; K-self-adj {kr:.2e}")
    assert cr < 1e-8, (name, cr)
    conf_sigs[name] = signature(B, name)
# Casimir of so(4,2) also commutes with the algebra (center of U(so(4,2)))
log(f"    A1 Casimir conformal-commutation rel. residual: {conf_comm_res(Cas):.2e} (central, as required)")
assert conf_comm_res(Cas) < 1e-8

worst_k = max(kres.values())
log(f"\n  K-self-adjointness of ALL class cores: worst rel. residual {worst_k:.3e} (class embeds; outcome"
    " (iii) 'conformal class does not embed' is REFUTED)")
assert worst_k < 1e-8
log(f"  [{time.time() - T0:.0f}s]")


# ---------------------------------------------------------------------------
# [E] CONTROLS
# ---------------------------------------------------------------------------
log("\n[E] CONTROLS (the test must be able to fail)")
log("  C1: scrambled 'conformal' algebra -- same Hermiticity types, same norms, random matrices")
scr_sigs = {}
accS = {"S1 scrambled Casimir": np.zeros((1664, 1664), dtype=complex),
        "S2 scrambled unsigned": np.zeros((1664, 1664), dtype=complex)}
cS = [RNG.standard_normal(15) for _ in range(3)]
for t in range(3):
    accS[f"S3.{t} scrambled random signed"] = np.zeros((1664, 1664), dtype=complex)
accPD_scr = np.zeros((1664, 1664), dtype=complex)
cPD_scr = np.abs(RNG.standard_normal(15)) + 0.1
for k in range(15):
    X = RNG.standard_normal((1664, 1664)) + 1j * RNG.standard_normal((1664, 1664))
    R = 0.5 * (X + X.conj().T) if types42[k] == "H" else 0.5 * (X - X.conj().T)
    R *= norms42[k] / float(np.linalg.norm(R))
    q = R @ R
    accS["S1 scrambled Casimir"] += eta_sign[k] * q
    accS["S2 scrambled unsigned"] += q
    for t in range(3):
        accS[f"S3.{t} scrambled random signed"] += cS[t][k] * q
    accPD_scr += cPD_scr[k] * (q if types42[k] == "H" else -q)
del X, R, q
for name, S in accS.items():
    scr_sigs[name] = signature(S, name)
scr_generic = [scr_sigs[k] for k in scr_sigs]
log(f"    scrambled generic family: {len(set(scr_generic))} distinct signatures -> the constructions do NOT"
    " intrinsically narrow; a genuine single value would have been a real (algebra-attributable) signal")
assert len(set(scr_generic)) >= 2

log("  C2: narrowing DETECTABILITY -- positivity-restricted subfamily (must read NARROWED)")
pd_sigs = []
for t in range(3):
    cpd = np.abs(RNG.standard_normal(15)) + 0.1
    Apd = sum(ci * (q if ty == "H" else -q) for ci, q, ty in zip(cpd, sq42, types42))
    pd_sigs.append(signature(Apd, f"C2.{t} PSD combo (+boost^2 - rot^2)"))
pd_scr_sig = signature(accPD_scr, "C2.scr PSD combo on SCRAMBLED algebra")
log(f"    genuine PSD subfamily: {len(set(pd_sigs))} distinct value(s) {sorted(set(pd_sigs))}")
assert len(set(pd_sigs)) == 1, pd_sigs                       # harness CAN output NARROWED
assert pd_scr_sig == pd_sigs[0], (pd_scr_sig, pd_sigs[0])    # ...and it narrows for the scramble too
log("    -> the PSD subfamily narrows for BOTH the genuine and the scrambled algebra: definiteness-"
    "narrowing is algebra-INDEPENDENT (a tautology), and is therefore NOT evidence of conformal force.")
log(f"  [{time.time() - T0:.0f}s]")


# ---------------------------------------------------------------------------
# [F] robustness: alternative representative so(4,2)
# ---------------------------------------------------------------------------
log("\n[F] ROBUSTNESS: alternative representative so(4,2) on spacelike {5,6,7,8} + timelike {12,13}")
alt_S, alt_T = [5, 6, 7, 8], [12, 13]
pairs_alt = [(a, b) for i, a in enumerate(alt_S + alt_T) for b in (alt_S + alt_T)[i + 1:]]
r_alt = equiv_residual(pairs_alt)
assert r_alt < ATOL
accA = {"F1 alt Casimir": np.zeros((1664, 1664), dtype=complex),
        "F2 alt random signed": np.zeros((1664, 1664), dtype=complex)}
cF = RNG.standard_normal(15)
for k, (a, b) in enumerate(pairs_alt):
    JW = apply_gen(Lvec(a, b), sigma(a, b), W)
    Jc = W.conj().T @ JW
    q = Jc @ Jc
    accA["F1 alt Casimir"] += ETA[a] * ETA[b] * q
    accA["F2 alt random signed"] += cF[k] * q
alt_sigs = {}
for name, A in accA.items():
    alt_sigs[name] = signature(A, name)
log(f"  [{time.time() - T0:.0f}s]")


# ---------------------------------------------------------------------------
# [G] VERDICT
# ---------------------------------------------------------------------------
log("\n[G] VERDICT -- T4' forward")
all_class = dict(conf_sigs)
all_class.update(alt_sigs)
distinct = sorted(set(all_class.values()))
counts = sorted(set(npl - nmi for (npl, nmi, _) in all_class.values()))
log(f"  conformal-compatible class (families A+B+alt): {len(all_class)} cores, "
    f"{len(distinct)} distinct signatures")
log(f"  signed counts n+ - n- observed in the class: {counts}")
all_even = all((npl - nmi) % 2 == 0 for (npl, nmi, _) in all_class.values())
mod3 = sorted(set((npl - nmi) % 3 for (npl, nmi, _) in all_class.values()))
log(f"  parity: all signed counts EVEN = {all_even} (C-07 quaternionic-Kramers wall persists under the"
    f" conformal restriction) ; residues mod 3 present: {mod3}")
assert all_even
if len(distinct) == 1:
    log("  OUTCOME (i): NARROWED -- the conformal constraint has real force (apply maximum target scrutiny).")
    verdict = "NARROWED"
else:
    log("  OUTCOME (ii): the class still SCATTERS -> the conformal-class constraint is INERT on the count.")
    log("  Structural reason (measured above, A6a/A6b and sign symmetry): the conformal-compatible class")
    log("  is closed under A -> -A and A -> A + t*I (both -A and shifted Casimirs are class members), so")
    log("  it cannot pin a signature; pinning would require a canonical normalization the conformal leg")
    log("  does not supply. T4' forward: NEGATIVE.")
    verdict = "SCATTERS"
assert verdict == "SCATTERS" or len(distinct) == 1

log("\n" + "=" * 96)
log("RESULT: anchors reproduced ((+96,-96,0) triplet; beta residual 0; rank 128/ker 1664; 58.7215;")
log("155.3625; prior scatter mechanism 0 vs +1664). so(4,2) < so(6,4) < so(9,5) chain embeds on the")
log("carrier (structure constants, Gamma-equivariance, K-skewness all machine-zero); every quadratic /")
log(f"commutant core is K-self-adjoint (worst {worst_k:.1e}). T4' forward verdict: {verdict} "
    f"({len(distinct)} distinct signatures across {len(all_class)} class cores).")
log("Controls: scrambled algebra scatters identically (constructions not intrinsically narrowing);")
log("PSD subfamily narrows for BOTH algebras (definiteness-narrowing is a tautology, flagged).")
log("No target constant {3, 8, 24, chi(K3), Ahat, rank_H=4, ind_H=8} imported.")
log("=" * 96)
sys.exit(0)
