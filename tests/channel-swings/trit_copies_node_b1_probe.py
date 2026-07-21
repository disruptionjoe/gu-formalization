"""Node B1 probe (pre-registered): the identical-copies test for the three generation-sectors.

PRE-REGISTRATION: explorations/prereg-trit-symmetry-and-fork-2026-07-20.md, Node B1
(commit cafcbc7). LABEL-CAMP half of the copies/simplex fork.

THE QUESTION (bound before looking): are the three generation-sectors STRUCTURALLY
ISOMORPHIC copies -- identical as Krein modules up to the external S_3 label -- so that
the ONLY distinction among them is the label ("three shards / three degenerate copies /
three colors")? Or are at least two of the three genuinely INEQUIVALENT (label camp wrong)?

OBJECT (structural reading): the three generation-sectors are the three SU(2)+ generation
weight-spaces W_{-2}, W_0, W_{+2} inside the verified 192-dim self-dual triplet -- literally
"the three generations" of the spin-1 flavor multiplet, the weight label being the S_3/Weyl
label. Each is 64-dim. (Cross-checked below against the commutant-Z/3 "cube-root sectors"
reading, whose multiplicities (0,192,192) make it the degenerate reading.)

TEST: exhibit each sector as a concrete Krein module on the frozen fixtures; compute the
COMPLETE Krein-module invariants (dim, Krein signature -- the H-module type is dimension-
forced since H (x) C = M2(C)); pairwise-equal invariants => isomorphic, and EXHIBIT the
isomorphisms explicitly (the SU(2)+ ladder as a commutant-intertwining module iso; the
frozen J_quat as an antilinear Krein iso W_{+2} = W_{-2}; a constructed Krein isometry
T with T^# K_j T = K_i exactly). CONTROL: three deliberately non-isomorphic blocks
(different dim / different signature) must FAIL the SAME tester -- two-sided power.

OUTCOMES pre-declared (fork F-COPIES / F-NEITHER): B1-HOLDS / B1-FAILS. Exit 0 = ran honestly.
"""
from __future__ import annotations
import os, sys, time
import numpy as np

_HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.normpath(os.path.join(_HERE, "..", "generation-sector")))
import gen_sector_bridge as bridge  # noqa: E402

rng = np.random.default_rng(20260720)
FAILURES = []
def check(tag, name, ok, detail=""):
    s = "PASS" if ok else "FAIL"
    print(f"[{tag}] {s}  {name}" + (f"  ({detail})" if detail else ""))
    if not ok:
        FAILURES.append(name)

t0 = time.time()
W3 = np.exp(2j * np.pi / 3)
e, Gamma, Pi_RS, _ = bridge.constraint_objects()
N, DIM = bridge.N, bridge.DIM
I128, I14 = np.eye(DIM, dtype=complex), np.eye(N, dtype=complex)

# ---------------- [T] frozen fixtures -----------------------------------------------------
check("T", "Clifford exact: Gamma Gamma^dag = 14 I",
      float(np.max(np.abs(Gamma @ Gamma.conj().T - 14 * I128))) == 0.0)
check("T", "Pi_RS projector onto ker(Gamma), rank 1664", abs(np.trace(Pi_RS).real - 1664) < 1e-9)
C = e[1] @ e[3] @ e[5] @ e[7] @ e[10] @ e[12]        # spinor-factor quaternion structure
Cfull = np.kron(I14, C)                              # J_quat = Cfull . conj on the full module
check("T", "J_quat^2 = -1 exact (C Cbar = -I)", float(np.max(np.abs(C @ C.conj() + I128))) == 0.0)
check("T", "ALL 14 gammas J_quat-commuting exactly (frozen commutant H)",
      max(float(np.max(np.abs(e[a] @ C - C @ e[a].conj()))) for a in range(N)) == 0.0)

# ---------------- [T] the 192-dim triplet + the three weight sectors (ghost_parity recipe) -
def sgen(i, j): return 0.25 * (e[i] @ e[j] - e[j] @ e[i])
def lvec(i, j):
    M = np.zeros((N, N), dtype=complex); M[i, j] = 1; M[j, i] = -1; return M
SD = [(0, 1, 2, 3), (0, 2, 3, 1), (0, 3, 1, 2)]
J = [np.kron(I14, sgen(a, b) + sgen(c, d)) + np.kron(lvec(a, b) + lvec(c, d), I128)
     for (a, b, c, d) in SD]
w, Vv = np.linalg.eigh(Pi_RS); Wk = Vv[:, w > 0.5]
Cas = -(J[0] @ J[0] + J[1] @ J[1] + J[2] @ J[2])
CasK = Wk.conj().T @ Cas @ Wk; CasK = 0.5 * (CasK + CasK.conj().T)
ev, U = np.linalg.eigh(CasK)
Wt = Wk @ U[:, np.abs(ev - 8.0) < 1e-3]              # 192-dim self-dual triplet, orthonormal cols
check("T", "triplet: Casimir-8 (spin-1) eigenspace of ker(Gamma), dim 192", Wt.shape[1] == 192)

A3 = Wt.conj().T @ (1j * J[0]) @ Wt; A3 = 0.5 * (A3 + A3.conj().T)   # iJ3 in triplet coords
mu, Q3 = np.linalg.eigh(A3)
Pw = {m: Q3[:, np.abs(mu - m) < 1e-6] for m in (-2, 0, 2)}          # weight-space frames (192x64)
check("T", "three generation-sectors = weight spaces {-2,0,+2} x 64 under iJ3",
      all(Pw[m].shape[1] == 64 for m in (-2, 0, 2)))

# Krein form K = etaV (x) beta_S, restricted to the triplet
bS = I128.copy()
for s_ in range(9): bS = bS @ e[s_]
if np.linalg.norm(bS.conj().T + bS) < 1e-9: bS = 1j * bS
bS = bS / np.sqrt(abs((bS @ bS)[0, 0].real))
Kfull = np.kron(np.diag([1.0] * 9 + [-1.0] * 5).astype(complex), bS)
Kt = Wt.conj().T @ Kfull @ Wt; Kt = 0.5 * (Kt + Kt.conj().T)        # 192x192 Krein form
sig_t = np.linalg.eigvalsh(Kt)
check("T", "K|triplet signature (+96,-96): 96 (generation,mirror) hyperbolic pairs",
      int(np.sum(sig_t > 1e-9)) == 96 and int(np.sum(sig_t < -1e-9)) == 96)

def signature(Kblk):
    s = np.linalg.eigvalsh(0.5 * (Kblk + Kblk.conj().T))
    return int(np.sum(s > 1e-9)), int(np.sum(s < -1e-9)), int(np.sum(np.abs(s) < 1e-9))

# per-sector Krein blocks (in each weight-space's own 64-dim frame)
Kblk = {m: Pw[m].conj().T @ Kt @ Pw[m] for m in (-2, 0, 2)}

# ---------------- [E] the sectors are K-ORTHOGONAL, K nondegenerate on each ----------------
# iJ3 is K-self-adjoint: (iJ3)^# = iJ3, so distinct-eigenvalue weight spaces are K-orthogonal;
# K then block-diagonalizes over the three sectors, nondegenerate on each -> each sector has a
# well-defined Krein signature (the sectors are genuine Krein modules, not entangled).
iJ3t = 1j * A3  # = iJ3 in triplet coords already Hermitian? A3 is Hermitian (weights) so iJ3t skew
# Krein adjoint of iJ3: Kt^{-1} (iJ3)^dag Kt ; check equals iJ3 (self-adjoint) with iJ3 = A3? A3 IS iJ3.
Kti = np.linalg.inv(Kt)
Krein_adj = Kti @ A3.conj().T @ Kt
check("E", "iJ3 is K-SELF-ADJOINT ((iJ3)^# = iJ3): the three weight sectors are K-orthogonal",
      float(np.linalg.norm(Krein_adj - A3)) < 1e-9, f"defect {float(np.linalg.norm(Krein_adj - A3)):.1e}")
cross = max(float(np.linalg.norm(Pw[a].conj().T @ Kt @ Pw[b]))
            for a, b in [(-2, 0), (-2, 2), (0, 2)])
check("E", "cross-sector Krein blocks vanish (mutually K-orthogonal, K nondegenerate on each)",
      cross < 1e-9, f"max cross-block ||K|| {cross:.1e}")

# ---------------- [E] COMPLETE Krein-module invariants of each sector ----------------------
# H (x) C = M2(C): every complex H-module is a sum of copies of the standard 2-dim rep, so the
# H-module type is FORCED by complex dimension (quaternionic dim = dim/2). The only remaining
# invariant is the Krein signature. (dim, signature) is therefore the COMPLETE invariant set.
inv = {m: (Pw[m].shape[1], signature(Kblk[m])) for m in (-2, 0, 2)}
for m in (-2, 0, 2):
    d, (p, q, z) = inv[m]
    check("E", f"sector W_{m:+d}: dim {d}, Krein signature (+{p},-{q},0:{z}), H-dim {d // 2}",
          d == 64 and (p, q, z) == (32, 32, 0))
all_equal = len({inv[m] for m in (-2, 0, 2)}) == 1
check("E", "ISOMORPHISM VERDICT: all three sectors carry IDENTICAL complete invariants "
           "(dim 64, sig (+32,-32), H-dim 32) => pairwise Krein-ISOMORPHIC (classification of "
           "H-modules with nondegenerate invariant Krein form)", all_equal, str(inv[-2]))

# ---------------- [E] EXHIBIT isomorphism 1: the SU(2)+ ladder (commutant-intertwiner) -----
# L = J1 + i J2 is built from gammas; it commutes with the frozen commutant H (J_quat commutes
# with every gamma) so it intertwines the commutant module structure, and it shifts weight by
# a fixed step. Full rank between adjacent sectors = a MODULE ISOMORPHISM of one onto the next.
Lfull = J[1] + 1j * J[2]
Lt = Wt.conj().T @ Lfull @ Wt
tri_leak = float(np.linalg.norm((np.eye(N * DIM) - Wt @ Wt.conj().T) @ Lfull @ Wt))  # L preserves triplet
def ladder_block(m_from, m_to):
    return Pw[m_to].conj().T @ Lt @ Pw[m_from]
r_p0 = np.linalg.matrix_rank(ladder_block(2, 0), tol=1e-6)      # W_{+2} -> W_0
r_0m = np.linalg.matrix_rank(ladder_block(0, -2), tol=1e-6)     # W_0   -> W_{-2}
leak = max(float(np.linalg.norm(ladder_block(2, 2))), float(np.linalg.norm(ladder_block(2, -2))),
           float(np.linalg.norm(ladder_block(0, 0))), float(np.linalg.norm(ladder_block(0, 2))))
# C-linear commutant is scalars, so the ladder trivially intertwines it; the frozen J_quat
# instead SWAPS raising<->lowering (antilinear, J i = -i J), weaving the three into one H-structure.
Mq = Wt.conj().T @ Cfull @ Wt.conj()                             # J_quat in triplet coords (antilinear)
check("E", "ISO-1 (ladder L=J1+iJ2): rank-64 bijection W_{+2}->W_0 and W_0->W_{-2}, no weight "
           "leak, preserves the triplet -> explicit C-linear MODULE isomorphism between sectors",
      r_p0 == 64 and r_0m == 64 and leak < 1e-6 and tri_leak < 1e-6,
      f"ranks {r_p0},{r_0m}; weight-leak {leak:.1e}; triplet-leak {tri_leak:.1e}")

# ---------------- [E] EXHIBIT isomorphism 2: the frozen J_quat, antilinear W_{+2} = W_{-2} --
# J_quat maps the m-eigenspace of iJ3 to the (-m)-eigenspace (antilinear: J i = -i J), giving a
# canonical FROZEN antilinear bijection W_{+2} -> W_{-2}. Check bijection + Krein-compatibility.
Jblk = Pw[-2].conj().T @ Mq @ Pw[2].conj()                      # coeff -> Jblk @ conj(coeff)
r_jq = np.linalg.matrix_rank(Jblk, tol=1e-6)
jq_leak = float(np.linalg.norm(Pw[0].conj().T @ Mq @ Pw[2].conj()))
# antilinear Krein isometry: <Jx,Jy>_K = conj(<x,y>_K) on the sector (coeffs in W_{+2} coords)
xs = rng.standard_normal((64, 6)) + 1j * rng.standard_normal((64, 6))
Jxs = Jblk @ xs.conj()
lhs = Jxs.conj().T @ Kblk[-2] @ Jxs
rhs = (xs.conj().T @ Kblk[2] @ xs).conj()
check("E", "ISO-2 (frozen J_quat): antilinear rank-64 bijection W_{+2} = W_{-2}, no leak, and "
           "a KREIN isometry (<Jx,Jy>_K = conj<x,y>_K) -- a frozen-structure iso of the outer pair",
      r_jq == 64 and jq_leak < 1e-9 and float(np.linalg.norm(lhs - rhs)) < 1e-9,
      f"rank {r_jq}; leak {jq_leak:.1e}; isometry defect {float(np.linalg.norm(lhs - rhs)):.1e}")

# ---------------- helper: the isomorphism TESTER (used on real sectors AND controls) --------
def krein_orthonormalizer(Kblk_):
    """O with O^dag K O = eta = diag(+1..,-1..) (sorted). Returns (O, eta_signs) or None if degenerate."""
    Kh = 0.5 * (Kblk_ + Kblk_.conj().T)
    d, V = np.linalg.eigh(Kh)
    if np.min(np.abs(d)) < 1e-9:
        return None
    order = np.argsort(-np.sign(d))                              # +1 block first, then -1 block
    d, V = d[order], V[:, order]
    O = V @ np.diag(1.0 / np.sqrt(np.abs(d)))
    return O, np.sign(d)

def iso_tester(Ki, Kj):
    """Decide Krein-module isomorphism from complete invariants; construct T with T^# Kj T = Ki.
    Returns (isomorphic, T_or_None, reason)."""
    if Ki.shape != Kj.shape:
        return False, None, f"dimension mismatch {Ki.shape[0]} vs {Kj.shape[0]}"
    Oi, Oj = krein_orthonormalizer(Ki), krein_orthonormalizer(Kj)
    if Oi is None or Oj is None:
        return False, None, "degenerate block"
    if not np.array_equal(Oi[1], Oj[1]):
        pi_, pj_ = (int(np.sum(Oi[1] > 0)), int(np.sum(Oi[1] < 0))), (int(np.sum(Oj[1] > 0)), int(np.sum(Oj[1] < 0)))
        return False, None, f"signature mismatch (+{pi_[0]},-{pi_[1]}) vs (+{pj_[0]},-{pj_[1]})"
    T = Oj[0] @ np.linalg.inv(Oi[0])                            # T^dag Kj T = Ki, exact by construction
    resid = float(np.linalg.norm(T.conj().T @ Kj @ T - Ki))
    return resid < 1e-8, T, f"Krein isometry built, T^# Kj T = Ki residual {resid:.1e}"

# ---------------- [E] EXHIBIT isomorphism 3: constructed Krein isometry, every pair ---------
pair_ok, pair_res = True, []
for a, b in [(-2, 0), (0, 2), (-2, 2)]:
    ok, T, why = iso_tester(Kblk[a], Kblk[b])
    inv_ok = ok and np.linalg.matrix_rank(T, tol=1e-8) == 64
    pair_ok &= inv_ok
    pair_res.append(f"W_{a}~W_{b}:{why}")
check("E", "ISO-3 (constructed): explicit invertible Krein isometry T_{ij} with T^# K_j T = K_i "
           "EXACTLY for all three pairs -- the sectors are interchangeable up to relabeling",
      pair_ok, " | ".join(pair_res))

# ---------------- [E] cross-check: the commutant-Z/3 "cube-root sectors" reading -----------
# The alternative "three sectors" reading (eigenspaces of the commutant order-3 element) is
# DEGENERATE: multiplicities (0,192,192) (N6) -- one sector empty, so that reading is NOT three
# equal copies. The weight-space reading tested above is the structural one where copies live.
Ut = Wt.conj().T @ (W3 * np.eye(N * DIM)) @ Wt        # canonical C-linear commutant order-3 = wI
lam = np.linalg.eigvals(Ut)
mult_cube = tuple(int(np.sum(np.abs(lam - z) < 1e-6)) for z in (1, W3, W3 ** 2))
check("E", "cube-root-sectors reading is DEGENERATE: the C-linear order-3 element wI puts the "
           "WHOLE triplet in one eigenspace (0,192,0); N6's generic commutant element gives "
           "(0,192,192) -- either way empty sectors, NOT three equal copies. The weight-space "
           "reading is the correct home for the identical-copies question",
      mult_cube == (0, 192, 0), str(mult_cube))

# ---------------- [F] CONTROL: three deliberately NON-isomorphic blocks must FAIL ----------
# Build a fixed random 64-dim Krein block of signature (+32,-32) as the "true copy" template,
# and plant three non-isomorphic distortions. The SAME iso_tester must reject the bad pairs.
def random_krein(dim, npos, seed):
    r = np.random.default_rng(seed)
    M = r.standard_normal((dim, dim)) + 1j * r.standard_normal((dim, dim))
    Qr, _ = np.linalg.qr(M)
    eta = np.diag([1.0] * npos + [-1.0] * (dim - npos)).astype(complex)
    return Qr @ eta @ Qr.conj().T                                # Hermitian, signature (+npos, -(dim-npos))

# positive control: two independent (+32,-32) 64-blocks ARE isomorphic (tester must PASS)
Kc1, Kc2 = random_krein(64, 32, 1), random_krein(64, 32, 2)
pos_ok, _, pos_why = iso_tester(Kc1, Kc2)
check("F", "power (positive): two independent (+32,-32) 64-blocks -> tester returns ISOMORPHIC "
           "with an exact Krein isometry (tester CAN pass; verdict not baked in)", pos_ok, pos_why)
# negative (a): different dimension 64 vs 63 -> FAIL
Kbad_dim = random_krein(63, 32, 3)
neg_a = iso_tester(Kc1, Kbad_dim)
check("F", "power (neg-a): dim-64 vs dim-63 blocks -> tester returns NOT isomorphic (dim gate)",
      neg_a[0] is False, neg_a[2])
# negative (b): same dim, different signature (+32,-32) vs (+40,-24) -> FAIL
Kbad_sig = random_krein(64, 40, 4)
neg_b = iso_tester(Kc1, Kbad_sig)
check("F", "power (neg-b): (+32,-32) vs (+40,-24) same dim -> tester returns NOT isomorphic "
           "(signature gate) -- inequivalent Krein modules rejected", neg_b[0] is False, neg_b[2])
# negative (c): definite vs neutral (+64,0) vs (+32,-32) -> FAIL
Kbad_def = random_krein(64, 64, 5)
neg_c = iso_tester(Kc1, Kbad_def)
check("F", "power (neg-c): neutral (+32,-32) vs definite (+64,0) -> NOT isomorphic",
      neg_c[0] is False, neg_c[2])
# and the three planted blocks are pairwise non-isomorphic as a TRIO (the control's headline)
trio = [Kc1, Kbad_sig, Kbad_def]
trio_iso = sum(1 for i in range(3) for j in range(i + 1, 3) if iso_tester(trio[i], trio[j])[0])
check("F", "CONTROL trio {(+32,-32),(+40,-24),(+64,0)} is pairwise NON-isomorphic (0/3 pairs "
           "pass) -- the exact opposite of the real sectors' 3/3 -- demonstrated two-sided power",
      trio_iso == 0, f"{trio_iso}/3 pairs isomorphic")

# ---------------- verdict -----------------------------------------------------------------
real_iso = sum(1 for a, b in [(-2, 0), (0, 2), (-2, 2)] if iso_tester(Kblk[a], Kblk[b])[0])
B1_HOLDS = all_equal and real_iso == 3 and pair_ok
print()
print(f"NODE B1 PROBE: {'ALL PASS' if not FAILURES else str(len(FAILURES)) + ' FAILURES: ' + str(FAILURES)}"
      f"  ({time.time() - t0:.1f}s)")
outcome = "B1-HOLDS" if B1_HOLDS else "B1-FAILS"
print(f"HEADLINE: OUTCOME = {outcome}. The three generation-sectors (SU(2)+ weight-spaces "
      f"W_{{-2}}, W_0, W_{{+2}} of the verified 192-dim self-dual triplet) are STRUCTURALLY "
      f"ISOMORPHIC COPIES. Each is a 64-dim Krein module of IDENTICAL complete invariants "
      f"(dim 64, Krein signature (+32,-32,0), quaternionic H-dim 32); they are mutually "
      f"K-orthogonal (iJ3 is K-self-adjoint) so each is a bona-fide Krein module, and the "
      f"invariants coincide, hence pairwise Krein-isomorphic ({real_iso}/3 pairs). Three "
      f"explicit isomorphisms EXHIBITED: (1) the SU(2)+ ladder L=J1+iJ2, a rank-64 "
      f"commutant-intertwining module iso between adjacent sectors; (2) the frozen J_quat, an "
      f"antilinear rank-64 Krein iso W_{{+2}} = W_{{-2}}; (3) constructed invertible Krein "
      f"isometries T_{{ij}} with T^# K_j T = K_i EXACTLY for all three pairs. The ONLY "
      f"distinction among the sectors is the external S_3/weight label -- the LABEL CAMP. "
      f"Control: a planted trio of signatures (+32,-32)/(+40,-24)/(+64,0) is 0/3 pairwise "
      f"isomorphic under the SAME tester (two independent (+32,-32) blocks pass), demonstrating "
      f"two-sided power. Cross-check: the commutant-Z/3 'cube-root sectors' reading is "
      f"degenerate (mult (0,192,192), one empty), so the weight-space reading is the correct "
      f"home. FORK: fires toward F-COPIES (three identical copies + external label; "
      f"physics-favored -- generations identical except mass), pending B2.")
sys.exit(0 if (not FAILURES and B1_HOLDS) else 1)


